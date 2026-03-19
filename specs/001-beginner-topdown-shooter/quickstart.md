# Quickstart: 初學者俯視射擊遊戲

## 1. 環境需求

- Python 3.12+
- pip

## 2. 安裝依賴

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

## 3. 執行測試（TDD）

```bash
pytest -q
```

若要分故事驗證：

```bash
pytest tests/unit/test_us1_movement.py tests/unit/test_us1_shooting.py tests/integration/test_us1_controls_and_fire.py -q
pytest tests/unit/test_us2_enemy_spawn_and_chase.py tests/unit/test_us2_bullet_enemy_collision.py tests/unit/test_us2_player_damage_multi_collision.py tests/integration/test_us2_combat_loop.py -q
pytest tests/unit/test_us3_hud_text.py tests/unit/test_us3_game_over_transition.py tests/unit/test_us3_restart.py tests/integration/test_us3_game_over_restart_flow.py -q
```

建議流程：
1. 先新增或修改測試，確認紅燈。
2. 實作最小程式碼讓測試轉綠。
3. 重構命名、註解與模組邊界，並再次確認綠燈。

## 4. 啟動遊戲

```bash
python src/main.py
```

## 5. 手動驗證（對應規格）

1. 進入遊戲後以 W/A/S/D 移動角色。
2. 觸發射擊後確認子彈可見並前進。
3. 等待敵人生成並追擊玩家。
4. 子彈命中敵人後，敵人消失且分數增加。
5. 敵人碰撞玩家後，生命值下降。
6. 生命值為 0 時顯示 Game Over，並停止一般戰鬥更新。
7. Game Over 畫面按 R，確認生命/分數/敵人/子彈皆重置。

## 6. 非網站專案說明

本功能為本機桌面遊戲（desktop app），不涉及網站部署；GitHub Pages 靜態網站條款不適用。
