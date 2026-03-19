# Implementation Plan: 初學者俯視射擊遊戲

**Branch**: `001-beginner-topdown-shooter` | **Date**: 2026-03-19 | **Spec**: `/workspaces/shooting_game/specs/001-beginner-topdown-shooter/spec.md`
**Input**: Feature specification from `/specs/001-beginner-topdown-shooter/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/plan-template.md` for the execution workflow.

## Summary

本計畫以 Python + Pygame 建立單人本機俯視射擊 MVP，先完成角色移動/射擊、敵人追擊與碰撞計分、生命值與 Game Over 重開三段功能，並以 TDD 驗證關鍵規則（移動、碰撞、狀態切換）與可操作流程，確保初學者可讀性與最小可行交付。

## Technical Context

**Language/Version**: Python 3.12  
**Primary Dependencies**: pygame（執行遊戲）、pytest（測試）  
**Storage**: N/A（單機記憶體內狀態，不含持久化）  
**Testing**: pytest（單元測試 + 小型整合測試）  
**Target Platform**: Linux/macOS/Windows 本機桌面環境（鍵盤操作）
**Project Type**: desktop-app（本機遊戲專案，非網站專案）  
**Performance Goals**: 遊戲迴圈穩定 60 FPS（一般筆電環境）  
**Constraints**: 僅使用基礎幾何圖形；程式結構以教學可讀性優先；不加入網路、帳號、多關卡  
**Scale/Scope**: 單一場景、單人遊玩、3 個核心故事（移動射擊/戰鬥計分/結束重開）

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] 本階段開始前已執行 `git status` 並確認狀態正常（已記錄目前為初始化規格檔未追蹤狀態）
- [x] 本計畫遵循最小可行原則，無未經說明的過度設計
- [x] 已定義 TDD 執行方式（先為每個需求撰寫失敗測試，再以最小程式碼通過，最後重構命名與註解）
- [x] 若為網站專案，預設採靜態前端且可部署至 GitHub Pages；本功能為本機遊戲專案，網站條款不適用且已註記
- [x] 本階段結束前已再次執行 `git status` 並確認狀態正常（目前仍為初始化未追蹤檔案狀態，無衝突）

### Post-Design Constitution Re-check

- [x] 設計輸出僅包含 `research.md`、`data-model.md`、`quickstart.md` 與必要 `contracts/`，符合最小可行原則
- [x] 已保留並更新規格文件，未刪除或覆蓋 `spec.md`、`plan.md`、`constitution.md`
- [x] 已記錄 `implement` 階段需以 TDD 與 `tasks.md` 勾選同步執行

## Project Structure

### Documentation (this feature)

```text
specs/001-beginner-topdown-shooter/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
└── tasks.md
```

### Source Code (repository root)

```text
src/
├── main.py
├── entities.py
├── systems.py
├── game_state.py
└── config.py

tests/
├── unit/
│   ├── test_movement.py
│   ├── test_combat.py
│   └── test_state_transition.py
└── integration/
    └── test_game_loop_smoke.py
```

**Structure Decision**: 採單一 Python 專案結構，保留單一可執行入口 `src/main.py`（符合 FR-001），其餘模組僅拆分到教學必要的最小層級，避免過度抽象。

## Phase 0 Research Plan

### Research Tasks

1. 決定遊戲框架與版本策略（Pygame 與 Python 版本）以符合初學者門檻。  
2. 定義碰撞與更新迴圈的最小實作模式，確保同幀多碰撞可正確處理。  
3. 定義測試策略（邏輯測試與迴圈煙霧測試）以落實 TDD 並可在本機重現。

### Expected Output

`research.md` 會以 Decision / Rationale / Alternatives considered 格式記錄，並解決所有技術不確定項。

## Phase 1 Design Plan

### Design Artifacts

1. `data-model.md`：定義 Player、Bullet、Enemy、GameSessionState 與狀態轉換規則。  
2. `contracts/`：記錄本功能是否有對外介面契約；若無，明確註記不適用。  
3. `quickstart.md`：提供本機安裝、測試、啟動流程與驗證步驟。

### TDD Execution Mapping

1. 先為 FR-002/FR-003 撰寫移動與射擊測試（紅燈）。  
2. 再為 FR-004~FR-009 撰寫敵人追擊、碰撞計分、生命與重開測試（紅燈）。  
3. 逐步實作最小邏輯使測試綠燈，最後重構註解與命名（符合 FR-011/FR-012）。

## Complexity Tracking

本計畫無憲章違規，無需例外申請。
