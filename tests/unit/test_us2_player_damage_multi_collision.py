"""US2 單元測試：玩家受傷與同幀多碰撞。"""

import main


def test_multiple_enemy_hits_reduce_hp_by_hit_count():
    state = main.initial_state()
    state.player.x = 100
    state.player.y = 100
    state.player.hp = 5
    state.enemies = [main.Enemy(x=100, y=100), main.Enemy(x=100, y=100)]

    main.resolve_combat(state)

    assert state.player.hp == 3


def test_hp_never_goes_below_zero():
    state = main.initial_state()
    state.player.x = 100
    state.player.y = 100
    state.player.hp = 1
    state.enemies = [main.Enemy(x=100, y=100), main.Enemy(x=100, y=100), main.Enemy(x=100, y=100)]

    main.resolve_combat(state)

    assert state.player.hp == 0
