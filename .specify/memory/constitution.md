<!--
Sync Impact Report
- Version change: template-placeholder -> 1.0.0
- Modified principles:
	- [PRINCIPLE_1_NAME] -> 一、需求導向與最小可行
	- [PRINCIPLE_2_NAME] -> 二、Git 階段管控（強制）
	- [PRINCIPLE_3_NAME] -> 三、TDD 先測後作（強制）
	- [PRINCIPLE_4_NAME] -> 四、實作階段文件安全與狀態同步
	- [PRINCIPLE_5_NAME] -> 五、網站預設為靜態前端與 GitHub Pages 可部署
- Added sections:
	- 品質門檻
	- 標準作業流程
- Removed sections:
	- 無
- Templates requiring updates:
	- ✅ .specify/templates/plan-template.md
	- ✅ .specify/templates/spec-template.md
	- ✅ .specify/templates/tasks-template.md
	- ⚠ pending: .specify/templates/commands/*.md（目錄不存在）
- Deferred TODOs:
	- 無
-->

# shooting_game Constitution

## Core Principles

### 一、需求導向與最小可行
所有工作項目 MUST 可追溯至 `spec.md` 的使用者故事、需求或驗收條件。規劃與實作 MUST
優先採用最小可行方案，不得為「可能未來會用到」而預先擴充。若需偏離最小可行方案，MUST 在
`plan.md` 記錄理由、替代方案與取捨。
理由：降低複雜度與維護成本，確保每次變更可驗證且可交付。

### 二、Git 階段管控（強制）
每個階段（specify、plan、tasks、implement）開始前與結束後都 MUST 執行至少一次
`git status`，並確認工作樹狀態正常；若非乾淨狀態，MUST 明確標註原因與處置。每次提交 MUST
保持單一邏輯變更，禁止混入無關檔案。
理由：避免階段交叉汙染，提升可追蹤性與回溯能力。

### 三、TDD 先測後作（強制）
實作 MUST 遵循 TDD：先寫測試、觀察紅燈、實作最小程式碼、確認綠燈、再重構。未先出現失敗測試
不得開始功能實作。測試案例 MUST 對應需求與驗收條件，且能在 CI 或本地重現。
理由：將品質前移，降低回歸風險並提高需求對齊度。

### 四、實作階段文件安全與狀態同步
`implement` 階段 MUST 即時維護 `tasks.md` 勾選狀態，確保完成度與實際進度一致。任何自動化或套用
模板流程 MUST 不得刪除、覆蓋或破壞規格文件，尤其 `spec.md`、`plan.md`、`tasks.md`、
`constitution.md`。
理由：維持交付透明度並保護專案知識資產。

### 五、網站預設為靜態前端與 GitHub Pages 可部署
若專案屬網站類型，預設架構 MUST 以前端靜態網站為主，且產出 MUST 可部署於 GitHub Pages。
若需伺服器端或動態後端，MUST 在 `plan.md` 提出必要性、替代方案與部署影響。
理由：以最低營運成本達成可公開驗證的交付。

## 品質門檻

1. 合併前 MUST 通過需求對應測試與既有測試。
2. 重大變更 MUST 附上可重現驗證步驟。
3. 文件與程式碼變更 MUST 保持一致，禁止文件落後於實作。

## 標準作業流程

1. `specify`：建立/更新 `spec.md`，階段開始與結束各執行 `git status`。
2. `plan`：建立/更新 `plan.md`，記錄技術決策與違規例外，階段開始與結束各執行 `git status`。
3. `tasks`：建立/更新 `tasks.md`，任務需可獨立驗證，階段開始與結束各執行 `git status`。
4. `implement`：依 `tasks.md` 執行 TDD 並即時勾選完成項目，階段開始與結束各執行 `git status`。

## Governance

本憲章優先於一般開發慣例。任何修訂 MUST 以 PR 說明修訂動機、影響範圍、模板同步結果與遷移方式。
版本採語意化規則：
1. MAJOR：移除或重定義核心原則，造成治理不相容。
2. MINOR：新增原則或新增具約束力章節。
3. PATCH：措辭釐清、錯字修正、非語意變更。
每次規劃審查、任務審查與合併前審查 MUST 檢查憲章符合性；若不符合，MUST 先修正再繼續。

**Version**: 1.0.0 | **Ratified**: 2026-03-19 | **Last Amended**: 2026-03-19
