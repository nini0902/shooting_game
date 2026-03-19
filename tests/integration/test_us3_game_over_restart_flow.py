"""US3 整合測試：Game Over 到重開流程。"""

import main


def test_game_over_then_restart_flow():
    state = main.initial_state()
    state.player.x = 200
    state.player.y = 200
    state.player.hp = 1
    state.enemies = [main.Enemy(x=200, y=200)]

    # 進入 Game Over
    main.resolve_combat(state)
    assert state.phase == main.STATE_GAME_OVER

    # Game Over 狀態下，不按 R 不應恢復
    same = main.step_simulation(
        state,
        dt=0.1,
        input_state={"up": True, "down": False, "left": False, "right": True, "fire": True, "restart": False},
    )
    assert same.phase == main.STATE_GAME_OVER

    # 按 R 恢復
    restarted = main.step_simulation(
        state,
        dt=0.1,
        input_state={"up": False, "down": False, "left": False, "right": False, "fire": False, "restart": True},
    )
    assert restarted.phase == main.STATE_RUNNING
    assert restarted.player.hp == main.PLAYER_MAX_HP
