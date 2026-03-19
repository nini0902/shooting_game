# Tasks: 初學者俯視射擊遊戲

**Input**: Design documents from `/specs/001-beginner-topdown-shooter/`
**Prerequisites**: `plan.md` (required), `spec.md` (required), `research.md`, `data-model.md`, `contracts/`, `quickstart.md`

**Tests**: 測試任務為 MUST，遵循 TDD（先寫測試、先看到紅燈，再實作到綠燈，最後重構）。

**Organization**: 任務依 User Story 分組，確保每個故事可獨立實作與獨立驗證。

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: 初始化專案與最小開發環境（維持單檔遊戲主體）

- [X] T001 建立專案目錄 `src/`、`tests/unit/`、`tests/integration/` 於 `/workspaces/shooting_game/`
- [X] T002 建立依賴清單 `requirements.txt`（含 `pygame`、`pytest`）於 `/workspaces/shooting_game/requirements.txt`
- [X] T003 [P] 建立 pytest 設定（含測試路徑）於 `/workspaces/shooting_game/pytest.ini`
- [X] T004 [P] 建立測試環境初始化（headless pygame）於 `/workspaces/shooting_game/tests/conftest.py`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: 所有 User Story 共用的基礎骨架（未完成前不得進入故事實作）

- [X] T005 建立單檔遊戲骨架（主迴圈、資料結構、常數）於 `/workspaces/shooting_game/src/main.py`
- [X] T006 建立可測試的核心純函式介面（移動、碰撞、狀態切換）於 `/workspaces/shooting_game/src/main.py`
- [X] T007 [P] 建立最小啟動/結束煙霧測試（先紅燈）於 `/workspaces/shooting_game/tests/integration/test_game_loop_smoke.py`
- [X] T008 建立 quickstart 基礎指令一致性檢查（測試與啟動命令）於 `/workspaces/shooting_game/specs/001-beginner-topdown-shooter/quickstart.md`

**Checkpoint**: Foundation 完成後，才能開始 User Story 任務。

---

## Phase 3: User Story 1 - 玩家可操作角色並進行射擊 (Priority: P1) 🎯 MVP

**Goal**: 玩家能使用 W/A/S/D 移動並射擊，看到即時可見回饋。

**Independent Test**: 執行 `tests/unit/test_us1_movement.py`、`tests/unit/test_us1_shooting.py`、`tests/integration/test_us1_controls_and_fire.py`，不依賴敵人邏輯即可通過。

### Tests for User Story 1 (MANDATORY) ⚠️

- [X] T009 [P] [US1] 撰寫角色移動與邊界限制單元測試（先紅燈）於 `/workspaces/shooting_game/tests/unit/test_us1_movement.py`
- [X] T010 [P] [US1] 撰寫射擊生成與子彈前進單元測試（先紅燈）於 `/workspaces/shooting_game/tests/unit/test_us1_shooting.py`
- [X] T011 [P] [US1] 撰寫操作與視覺回饋整合測試（先紅燈）於 `/workspaces/shooting_game/tests/integration/test_us1_controls_and_fire.py`

### Implementation for User Story 1

- [X] T012 [US1] 實作 W/A/S/D 輸入轉位移與邊界夾限邏輯於 `/workspaces/shooting_game/src/main.py`
- [X] T013 [US1] 實作射擊輸入、子彈生成、子彈更新邏輯於 `/workspaces/shooting_game/src/main.py`
- [X] T014 [US1] 實作玩家與子彈幾何繪製與每幀刷新回饋於 `/workspaces/shooting_game/src/main.py`
- [X] T015 [US1] 以最小重構整理 US1 註解與命名可讀性於 `/workspaces/shooting_game/src/main.py`

**Checkpoint**: US1 可獨立操作與驗證，達成 MVP。

---

## Phase 4: User Story 2 - 玩家可透過戰鬥獲得分數並承受傷害 (Priority: P2)

**Goal**: 敵人可生成追擊；子彈命中得分；敵人碰撞玩家扣血。

**Independent Test**: 執行 `tests/unit/test_us2_enemy_spawn_and_chase.py`、`tests/unit/test_us2_bullet_enemy_collision.py`、`tests/unit/test_us2_player_damage_multi_collision.py`、`tests/integration/test_us2_combat_loop.py`，可驗證戰鬥循環。

### Tests for User Story 2 (MANDATORY) ⚠️

- [X] T016 [P] [US2] 撰寫敵人週期生成與追擊單元測試（先紅燈）於 `/workspaces/shooting_game/tests/unit/test_us2_enemy_spawn_and_chase.py`
- [X] T017 [P] [US2] 撰寫子彈命中敵人與固定加分單元測試（先紅燈）於 `/workspaces/shooting_game/tests/unit/test_us2_bullet_enemy_collision.py`
- [X] T018 [P] [US2] 撰寫敵人命中玩家與同幀多碰撞單元測試（先紅燈）於 `/workspaces/shooting_game/tests/unit/test_us2_player_damage_multi_collision.py`
- [X] T019 [P] [US2] 撰寫戰鬥循環整合測試（生成/追擊/命中/扣血，先紅燈）於 `/workspaces/shooting_game/tests/integration/test_us2_combat_loop.py`

### Implementation for User Story 2

- [X] T020 [US2] 實作敵人生成計時與朝玩家追擊更新於 `/workspaces/shooting_game/src/main.py`
- [X] T021 [US2] 實作子彈-敵人碰撞、敵人移除與分數累加於 `/workspaces/shooting_game/src/main.py`
- [X] T022 [US2] 實作敵人-玩家碰撞扣血與生命值下限保護於 `/workspaces/shooting_game/src/main.py`
- [X] T023 [US2] 實作同幀多碰撞的兩階段收集後套用流程於 `/workspaces/shooting_game/src/main.py`

**Checkpoint**: US2 可獨立驗證戰鬥、計分與受傷規則。

---

## Phase 5: User Story 3 - 玩家可讀取狀態並在失敗後重開 (Priority: P3)

**Goal**: 持續顯示分數/生命；生命歸零顯示 Game Over；按 R 重開。

**Independent Test**: 執行 `tests/unit/test_us3_hud_text.py`、`tests/unit/test_us3_game_over_transition.py`、`tests/unit/test_us3_restart.py`、`tests/integration/test_us3_game_over_restart_flow.py`，可驗證狀態顯示與重開。

### Tests for User Story 3 (MANDATORY) ⚠️

- [X] T024 [P] [US3] 撰寫 HUD 分數與生命顯示單元測試（先紅燈）於 `/workspaces/shooting_game/tests/unit/test_us3_hud_text.py`
- [X] T025 [P] [US3] 撰寫生命歸零切換 Game Over 單元測試（先紅燈）於 `/workspaces/shooting_game/tests/unit/test_us3_game_over_transition.py`
- [X] T026 [P] [US3] 撰寫 Game Over 後按 R 重開狀態重置單元測試（先紅燈）於 `/workspaces/shooting_game/tests/unit/test_us3_restart.py`
- [X] T027 [P] [US3] 撰寫 Game Over/重開流程整合測試（先紅燈）於 `/workspaces/shooting_game/tests/integration/test_us3_game_over_restart_flow.py`

### Implementation for User Story 3

- [X] T028 [US3] 實作每幀 HUD（分數/生命）文字更新與繪製於 `/workspaces/shooting_game/src/main.py`
- [X] T029 [US3] 實作生命歸零後切換 Game Over 並停止一般戰鬥更新於 `/workspaces/shooting_game/src/main.py`
- [X] T030 [US3] 實作 Game Over 狀態下僅 R 鍵可觸發新局重置於 `/workspaces/shooting_game/src/main.py`
- [X] T031 [US3] 整理狀態轉換註解與初學者可讀命名於 `/workspaces/shooting_game/src/main.py`

**Checkpoint**: US3 可獨立驗證 HUD、Game Over 與重開流程。

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: 跨故事收斂、文件校準與最終驗證

- [X] T032 [P] 補齊單檔主程式關鍵邏輯註解（符合 FR-011/FR-012）於 `/workspaces/shooting_game/src/main.py`
- [X] T033 [P] 校準 quickstart 測試/啟動步驟與實際命令一致於 `/workspaces/shooting_game/specs/001-beginner-topdown-shooter/quickstart.md`
- [X] T034 執行最終回歸測試清單並更新執行備註於 `/workspaces/shooting_game/specs/001-beginner-topdown-shooter/tasks.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- Phase 1 → Phase 2 → Phase 3/4/5 → Phase 6
- User Story 任務必須在 Phase 2 完成後開始。
- 建議優先完整交付 US1（MVP）後再進入 US2、US3。

### User Story Dependencies

- US1 (P1): 只依賴 Foundational，可先行獨立交付。
- US2 (P2): 依賴 US1 的移動/射擊基礎，但可用獨立測試驗證戰鬥循環。
- US3 (P3): 依賴 US1/US2 的狀態資料來源，但可用獨立測試驗證結束與重開。

### Within Each User Story

- 一律先完成該故事測試任務（TDD 紅燈）。
- 再完成單檔 `src/main.py` 實作任務使測試轉綠。
- 最後做該故事最小重構與註解整理。

---

## Parallel Opportunities

- Phase 1: `T003` 與 `T004` 可平行。
- US1: `T009`、`T010`、`T011` 可平行撰寫（不同測試檔）。
- US2: `T016`、`T017`、`T018`、`T019` 可平行撰寫（不同測試檔）。
- US3: `T024`、`T025`、`T026`、`T027` 可平行撰寫（不同測試檔）。
- Phase 6: `T032` 與 `T033` 可平行。

## Parallel Example: User Story 2

```bash
# 平行撰寫 US2 測試（先紅燈）
Task T016: tests/unit/test_us2_enemy_spawn_and_chase.py
Task T017: tests/unit/test_us2_bullet_enemy_collision.py
Task T018: tests/unit/test_us2_player_damage_multi_collision.py
Task T019: tests/integration/test_us2_combat_loop.py
```

---

## Implementation Strategy

### MVP First (US1)

1. 完成 Phase 1、Phase 2。
2. 完成 Phase 3（US1）並單獨驗證。
3. 若 US1 驗證通過即可先展示 MVP。

### Incremental Delivery

1. US1 完成後交付可玩核心（移動+射擊）。
2. 再加入 US2（敵人/計分/扣血）。
3. 最後加入 US3（HUD/Game Over/重開）。
4. 每完成一個故事就跑對應測試檔進行獨立驗證。

### TDD + 進度同步規則

1. 每個故事都必須先寫測試並確認失敗，再寫實作。
2. `implement` 階段執行者必須在完成當下即時勾選本檔 `tasks.md` 對應任務。
3. 不得刪除或覆蓋規格文件：`spec.md`、`plan.md`、`tasks.md`、`constitution.md`。

---

## Notes

- 保持單檔遊戲主體：核心遊戲邏輯集中在 `/workspaces/shooting_game/src/main.py`，避免過度拆分。
- 以初學者可讀性優先：命名一致、註解聚焦規則，不加入超出需求的進階機制。
- 每一階段開始與結束都需執行 `git status`（依憲章 CR-001）。

## Execution Notes

- 2026-03-19：已執行 `pytest -q`，結果 `17 passed`、`1 warning`（pygame 套件相依警告，不影響功能）。
- 2026-03-19：已依 TDD 完成紅燈到綠燈循環（US1/US2/US3 各至少一次失敗後修正通過）。
