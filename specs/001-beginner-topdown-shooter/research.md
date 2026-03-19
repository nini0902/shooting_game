# Phase 0 Research: 初學者俯視射擊遊戲

## Decision 1: 使用 Python 3.12 + Pygame 實作

- Decision: 以 Python 3.12 搭配 Pygame 作為 MVP 技術棧。
- Rationale: Python 對初學者閱讀友善，Pygame 可直接處理鍵盤輸入、2D 幾何繪製與主迴圈，能快速對齊 FR-002 到 FR-010。
- Alternatives considered:
  - Godot：功能完整但引擎學習與專案結構較重，超出本次最小可行範圍。
  - Unity：工具鏈與資源管理較複雜，不利於初學者快速理解核心邏輯。
  - 純 tkinter：對即時遊戲迴圈與碰撞控制較不直觀。

## Decision 2: 採固定時間步進主迴圈 + 逐幀碰撞檢查

- Decision: 使用固定 FPS 目標（60 FPS）的主迴圈，於每幀更新移動、生成、碰撞與狀態切換。
- Rationale: 可維持玩法穩定與邏輯一致性，且實作成本低，適合處理「同一幀多組碰撞」等邊界條件。
- Alternatives considered:
  - 可變時間步進：可更精細但對初學者較難掌握，容易引入速度不一致問題。
  - 事件驅動式稀疏更新：不適合連續移動與即時戰鬥場景。

## Decision 3: 碰撞處理採兩階段收集後一次套用

- Decision: 先收集當幀所有有效碰撞，再統一套用敵人移除、分數變更、生命扣減與 Game Over 切換。
- Rationale: 可避免在遍歷中直接刪除物件造成遺漏，並確保 FR-005、FR-006 與邊界案例「同幀多碰撞」可穩定成立。
- Alternatives considered:
  - 即時碰撞即時刪除：寫法簡短但高機率漏算或重複計分。
  - 逐系統分散處理：可擴充但對 MVP 屬過度設計。

## Decision 4: TDD 測試切分為純邏輯單元測試 + 遊戲迴圈煙霧測試

- Decision: 以 pytest 建立單元測試（移動、射擊生成、敵人追擊、碰撞計分、生命與重開），另加一個不開視窗的主迴圈煙霧測試。
- Rationale: 先驗證規則正確性，再驗證整體流程可啟動，有助於遵循憲章 TDD 並維持執行速度。
- Alternatives considered:
  - 全端到端視窗測試：維護成本高且在 CI/容器較不穩。
  - 僅手動測試：不符合 TDD 強制要求。

## Decision 5: 無對外服務介面，contracts 僅記錄不適用

- Decision: 本功能無 HTTP API、CLI 對外指令或跨系統整合契約；`contracts/` 僅保留「不適用」說明。
- Rationale: 本專案為單機桌面遊戲，外部互動僅玩家鍵盤輸入，無跨程序契約需求。
- Alternatives considered:
  - 自訂內部模組契約文件：可做但對本次 MVP 無必要。

## Clarification Resolution Summary

- Language/Version: 已定案（Python 3.12）。
- Primary Dependencies: 已定案（pygame, pytest）。
- Testing Strategy: 已定案（pytest 單元 + 煙霧測試）。
- Platform/Project Type: 已定案（本機桌面遊戲，非網站專案）。
- Performance/Constraints/Scope: 已定案（60 FPS、幾何圖形、單場景單人 MVP）。

以上 NEEDS CLARIFICATION 項目已全部解決，可進入 Phase 1 設計。
