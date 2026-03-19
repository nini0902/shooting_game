"""US3 單元測試：生命歸零切換 Game Over。"""

import main


def test_hp_zero_switches_to_game_over():
    state = main.initial_state()
    state.player.x = 100
    state.player.y = 100
    state.player.hp = 1
    state.enemies = [main.Enemy(x=100, y=100)]

    main.resolve_combat(state)

    assert state.player.hp == 0
    assert state.phase == main.STATE_GAME_OVER
