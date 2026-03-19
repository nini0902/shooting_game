"""US3 單元測試：HUD 文字。"""

import main


def test_hud_text_contains_score_and_life():
    state = main.initial_state()
    state.score = 30
    state.player.hp = 4

    text = main.hud_text(state)

    assert "Score: 30" in text
    assert "Life: 4" in text
