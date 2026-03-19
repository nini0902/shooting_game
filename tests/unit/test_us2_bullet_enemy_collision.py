"""US2 單元測試：子彈命中敵人與分數規則。"""

import main


def test_bullet_hit_enemy_removes_enemy_and_adds_score():
    state = main.initial_state()
    state.player.x = 100
    state.player.y = 100

    enemy = main.Enemy(x=100, y=80)
    bullet = main.Bullet(x=100, y=80, dx=0, dy=-1)
    state.enemies = [enemy]
    state.bullets = [bullet]

    main.resolve_combat(state)

    assert len(state.enemies) == 0
    assert len(state.bullets) == 0
    assert state.score == main.BULLET_DAMAGE_SCORE


def test_enemy_touch_player_only_should_not_add_score():
    state = main.initial_state()
    state.player.x = 100
    state.player.y = 100
    state.enemies = [main.Enemy(x=100, y=100)]
    state.bullets = []

    main.resolve_combat(state)

    assert state.score == 0
