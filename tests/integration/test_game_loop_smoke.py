"""Foundation 煙霧測試：確認遊戲主迴圈可在無視窗模式啟動與結束。"""

import pytest


def test_run_game_for_a_few_frames():
    # 先紅燈：在 main.py 尚未建立前，這裡會因匯入失敗而失敗。
    import main

    result = main.run_game(max_frames=3, headless=True)

    assert isinstance(result, dict)
    assert result["frames"] == 3
    assert result["running"] is True
