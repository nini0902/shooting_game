"""初學者俯視射擊遊戲（單檔版）。

此檔案同時包含：
1) 可測試的純邏輯函式（移動、碰撞、狀態切換）
2) 以 Pygame 執行的遊戲主迴圈入口
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple
import math
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

PLAYER_RADIUS = 16
PLAYER_SPEED = 250.0
PLAYER_MAX_HP = 5

BULLET_RADIUS = 5
BULLET_SPEED = 420.0
BULLET_DAMAGE_SCORE = 10

ENEMY_RADIUS = 14
ENEMY_SPEED = 120.0
ENEMY_SPAWN_INTERVAL = 1.0

STATE_RUNNING = "RUNNING"
STATE_GAME_OVER = "GAME_OVER"


@dataclass
class Player:
    x: float
    y: float
    hp: int = PLAYER_MAX_HP
    radius: int = PLAYER_RADIUS
    speed: float = PLAYER_SPEED


@dataclass
class Bullet:
    x: float
    y: float
    dx: float
    dy: float
    speed: float = BULLET_SPEED
    radius: int = BULLET_RADIUS
    active: bool = True


@dataclass
class Enemy:
    x: float
    y: float
    speed: float = ENEMY_SPEED
    radius: int = ENEMY_RADIUS
    active: bool = True


@dataclass
class GameState:
    player: Player
    bullets: List[Bullet]
    enemies: List[Enemy]
    score: int
    phase: str = STATE_RUNNING
    spawn_timer: float = 0.0


def clamp(value: float, minimum: float, maximum: float) -> float:
    return max(minimum, min(value, maximum))


def normalize(dx: float, dy: float) -> Tuple[float, float]:
    length = math.hypot(dx, dy)
    if length == 0:
        return (0.0, -1.0)
    return (dx / length, dy / length)


def circles_collide(x1: float, y1: float, r1: float, x2: float, y2: float, r2: float) -> bool:
    return math.hypot(x2 - x1, y2 - y1) <= (r1 + r2)


def initial_state() -> GameState:
    return GameState(
        player=Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2),
        bullets=[],
        enemies=[],
        score=0,
        phase=STATE_RUNNING,
        spawn_timer=0.0,
    )


def apply_player_movement(player: Player, input_state: Dict[str, bool], dt: float) -> None:
    """將輸入轉換為位移，並將玩家夾限在畫面範圍內。"""
    mx = 0.0
    my = 0.0
    if input_state.get("up"):
        my -= 1.0
    if input_state.get("down"):
        my += 1.0
    if input_state.get("left"):
        mx -= 1.0
    if input_state.get("right"):
        mx += 1.0

    nx, ny = normalize(mx, my) if (mx != 0.0 or my != 0.0) else (0.0, 0.0)
    player.x += nx * player.speed * dt
    player.y += ny * player.speed * dt

    player.x = clamp(player.x, player.radius, SCREEN_WIDTH - player.radius)
    player.y = clamp(player.y, player.radius, SCREEN_HEIGHT - player.radius)


def create_bullet(player: Player, direction: Tuple[float, float] = (0.0, -1.0)) -> Bullet:
    dx, dy = normalize(direction[0], direction[1])
    spawn_offset = player.radius + BULLET_RADIUS
    spawn_x = player.x + dx * spawn_offset
    spawn_y = player.y + dy * spawn_offset
    return Bullet(x=spawn_x, y=spawn_y, dx=dx, dy=dy)


def update_bullets(bullets: Iterable[Bullet], dt: float) -> List[Bullet]:
    updated: List[Bullet] = []
    for bullet in bullets:
        bullet.x += bullet.dx * bullet.speed * dt
        bullet.y += bullet.dy * bullet.speed * dt
        if bullet.x < 0 or bullet.x > SCREEN_WIDTH or bullet.y < 0 or bullet.y > SCREEN_HEIGHT:
            bullet.active = False
        if bullet.active:
            updated.append(bullet)
    return updated


def spawn_enemy() -> Enemy:
    edge = random.choice(["top", "bottom", "left", "right"])
    if edge == "top":
        return Enemy(x=random.uniform(0, SCREEN_WIDTH), y=0)
    if edge == "bottom":
        return Enemy(x=random.uniform(0, SCREEN_WIDTH), y=SCREEN_HEIGHT)
    if edge == "left":
        return Enemy(x=0, y=random.uniform(0, SCREEN_HEIGHT))
    return Enemy(x=SCREEN_WIDTH, y=random.uniform(0, SCREEN_HEIGHT))


def update_enemies(enemies: Iterable[Enemy], player: Player, dt: float) -> List[Enemy]:
    for enemy in enemies:
        dx, dy = normalize(player.x - enemy.x, player.y - enemy.y)
        enemy.x += dx * enemy.speed * dt
        enemy.y += dy * enemy.speed * dt
    return list(enemies)


def resolve_combat(state: GameState) -> None:
    """兩階段碰撞：先收集，再一次套用，避免邊遍歷邊刪除造成漏算。"""
    hit_bullets = set()
    hit_enemies = set()
    bullet_hit_enemies = set()
    player_hits = 0

    for bi, bullet in enumerate(state.bullets):
        for ei, enemy in enumerate(state.enemies):
            if circles_collide(bullet.x, bullet.y, bullet.radius, enemy.x, enemy.y, enemy.radius):
                hit_bullets.add(bi)
                hit_enemies.add(ei)
                bullet_hit_enemies.add(ei)

    for ei, enemy in enumerate(state.enemies):
        if circles_collide(state.player.x, state.player.y, state.player.radius, enemy.x, enemy.y, enemy.radius):
            player_hits += 1
            hit_enemies.add(ei)

    if bullet_hit_enemies:
        state.score += BULLET_DAMAGE_SCORE * len(bullet_hit_enemies)

    state.bullets = [b for i, b in enumerate(state.bullets) if i not in hit_bullets]
    state.enemies = [e for i, e in enumerate(state.enemies) if i not in hit_enemies]

    if player_hits > 0:
        state.player.hp = max(0, state.player.hp - player_hits)

    if state.player.hp <= 0:
        state.phase = STATE_GAME_OVER


def hud_text(state: GameState) -> str:
    return f"Score: {state.score}   Life: {state.player.hp}"


def restart_state(state: GameState) -> GameState:
    if state.phase != STATE_GAME_OVER:
        return state
    return initial_state()


def step_simulation(state: GameState, dt: float, input_state: Dict[str, bool]) -> GameState:
    # Game Over 期間只接受重開鍵，其他戰鬥輸入全部忽略。
    if state.phase == STATE_GAME_OVER:
        if input_state.get("restart"):
            return restart_state(state)
        return state

    # 1) 先更新玩家位移，讓敵人追擊時使用的是最新位置。
    apply_player_movement(state.player, input_state, dt)

    # 2) 射擊採即時生成；子彈方向先用固定向上，保持規則簡單。
    if input_state.get("fire"):
        state.bullets.append(create_bullet(state.player))

    state.bullets = update_bullets(state.bullets, dt)

    # 3) 以固定間隔生成敵人，避免同一幀產生過量敵人。
    state.spawn_timer += dt
    if state.spawn_timer >= ENEMY_SPAWN_INTERVAL:
        state.enemies.append(spawn_enemy())
        state.spawn_timer = 0.0

    state.enemies = update_enemies(state.enemies, state.player, dt)
    resolve_combat(state)
    return state


def run_game(max_frames: int | None = None, headless: bool = False) -> Dict[str, int | bool]:
    """執行遊戲主迴圈。

    max_frames: 測試用，跑固定幀數後自動結束。
    headless: 測試用，避免建立可視視窗。
    """
    import pygame

    pygame.init()
    if headless:
        screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    else:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Beginner Top-Down Shooter")

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 28)

    state = initial_state()
    running = True
    frames = 0

    while running:
        dt = clock.tick(FPS) / 1000.0
        input_state = {"up": False, "down": False, "left": False, "right": False, "fire": False, "restart": False}

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                input_state["fire"] = True

        keys = pygame.key.get_pressed()
        input_state["up"] = keys[pygame.K_w]
        input_state["down"] = keys[pygame.K_s]
        input_state["left"] = keys[pygame.K_a]
        input_state["right"] = keys[pygame.K_d]
        input_state["restart"] = keys[pygame.K_r]

        state = step_simulation(state, dt, input_state)

        screen.fill((24, 24, 28))

        # 幾何繪製：只用圓形與文字，符合 MVP 需求。
        pygame.draw.circle(screen, (80, 210, 120), (int(state.player.x), int(state.player.y)), state.player.radius)
        for bullet in state.bullets:
            pygame.draw.circle(screen, (245, 230, 90), (int(bullet.x), int(bullet.y)), bullet.radius)
        for enemy in state.enemies:
            pygame.draw.circle(screen, (225, 90, 90), (int(enemy.x), int(enemy.y)), enemy.radius)

        hud_surface = font.render(hud_text(state), True, (240, 240, 240))
        screen.blit(hud_surface, (10, 10))

        if state.phase == STATE_GAME_OVER:
            over_surface = font.render("Game Over - Press R to Restart", True, (255, 220, 220))
            screen.blit(over_surface, (SCREEN_WIDTH // 2 - 160, SCREEN_HEIGHT // 2))

        if not headless:
            pygame.display.flip()

        frames += 1
        if max_frames is not None and frames >= max_frames:
            break

    pygame.quit()
    return {"frames": frames, "running": True}


if __name__ == "__main__":
    run_game()
