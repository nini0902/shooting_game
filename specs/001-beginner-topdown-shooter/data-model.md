# Data Model: 初學者俯視射擊遊戲

## Entity: Player

- Purpose: 表示玩家角色與其生存狀態。
- Fields:
  - id: 固定字串（例如 `player-1`）。
  - position_x: 浮點數，玩家 X 座標。
  - position_y: 浮點數，玩家 Y 座標。
  - move_input: 結構或 tuple，記錄當前方向輸入（up/down/left/right）。
  - speed: 浮點數，每秒移動速度。
  - hp: 整數，生命值，下限為 0。
  - alive: 布林值，`hp > 0` 為 `true`。
- Validation Rules:
  - `hp` 不可小於 0（若小於則夾回 0）。
  - 座標須限制在遊戲區域邊界內。

## Entity: Bullet

- Purpose: 表示玩家射出的投射物。
- Fields:
  - id: 唯一識別。
  - position_x: 浮點數。
  - position_y: 浮點數。
  - direction_x: 浮點數。
  - direction_y: 浮點數。
  - speed: 浮點數。
  - active: 布林值，是否仍在場景中。
- Validation Rules:
  - 方向向量不可同時為 0（若為 0，使用預設向上方向）。
  - 超出場景邊界後 `active = false`。

## Entity: Enemy

- Purpose: 表示追擊玩家的敵方單位。
- Fields:
  - id: 唯一識別。
  - position_x: 浮點數。
  - position_y: 浮點數。
  - speed: 浮點數。
  - active: 布林值。
- Validation Rules:
  - 生成位置需在可視區域邊緣或預定生成區。
  - 被命中後 `active = false` 並於同幀或下一幀移除。

## Entity: GameSessionState

- Purpose: 管理單局進行狀態與 HUD 資訊。
- Fields:
  - score: 整數，初始為 0。
  - game_over: 布林值。
  - can_restart: 布林值，`game_over = true` 時為 `true`。
  - spawn_timer_ms: 整數，敵人生成計時。
  - phase: 列舉，`RUNNING | GAME_OVER`。
- Validation Rules:
  - `score` 只可遞增（由敵人擊殺事件觸發）。
  - `phase = GAME_OVER` 時停止一般戰鬥更新。

## Relationships

- Player 1 對多 Bullet：玩家可在遊戲中發射多顆子彈。
- Player 1 對多 Enemy（互動關係）：敵人追擊玩家並可能造成傷害。
- GameSessionState 1 對 1 Player：單局僅一名玩家。
- GameSessionState 1 對多 Bullet / Enemy：管理場上所有動態物件集合。

## State Transitions

1. RUNNING -> GAME_OVER:
   - 條件: 玩家 `hp <= 0`。
   - 動作: 設定 `game_over = true`、`can_restart = true`、停止一般戰鬥更新。

2. GAME_OVER -> RUNNING:
   - 條件: 玩家按下 R。
   - 動作: 重設玩家生命、分數、子彈集合、敵人集合與生成計時，開始新局。

## Event-to-Model Mapping

- MoveInputReceived: 更新 Player `move_input`。
- FireInputReceived: 新增 Bullet 實例至集合。
- BulletHitEnemy: 將 Enemy 設為 inactive，`score += fixed_value`。
- EnemyHitPlayer: 減少 Player `hp`，必要時觸發 GAME_OVER。
- RestartRequested: 觸發新局重設流程。
