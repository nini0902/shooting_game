"""US1 整合測試：輸入控制與射擊流程。"""

import main


def test_step_simulation_moves_and_fires():
    state = main.initial_state()
    old_x = state.player.x

    updated = main.step_simulation(
        state,
        dt=0.1,
        input_state={
            "up": False,
            "down": False,
            "left": False,
            "right": True,
            "fire": True,
            "restart": False,
        },
    )

    assert updated.player.x > old_x
    assert len(updated.bullets) == 1
