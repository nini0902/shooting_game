"""US3 單元測試：Game Over 後按 R 重開。"""

import main


def test_restart_resets_game_state_after_game_over():
    state = main.initial_state()
    state.phase = main.STATE_GAME_OVER
    state.player.hp = 0
    state.score = 99
    state.bullets = [main.Bullet(x=10, y=10, dx=0, dy=-1)]
    state.enemies = [main.Enemy(x=10, y=10)]

    updated = main.step_simulation(
        state,
        dt=0.1,
        input_state={"up": False, "down": False, "left": False, "right": False, "fire": False, "restart": True},
    )

    assert updated.phase == main.STATE_RUNNING
    assert updated.player.hp == main.PLAYER_MAX_HP
    assert updated.score == 0
    assert updated.bullets == []
    assert updated.enemies == []
