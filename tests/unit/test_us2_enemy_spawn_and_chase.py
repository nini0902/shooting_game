"""US2 單元測試：敵人生成與追擊。"""

import main


def test_enemy_spawns_when_timer_reaches_interval():
    state = main.initial_state()

    main.step_simulation(
        state,
        dt=main.ENEMY_SPAWN_INTERVAL,
        input_state={"up": False, "down": False, "left": False, "right": False, "fire": False, "restart": False},
    )

    assert len(state.enemies) == 1


def test_enemy_moves_toward_player_after_update():
    player = main.Player(x=100, y=100)
    enemy = main.Enemy(x=300, y=100)

    updated = main.update_enemies([enemy], player, dt=0.5)

    assert updated[0].x < 300
