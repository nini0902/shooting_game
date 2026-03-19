"""US1 單元測試：玩家移動與邊界。"""

import main


def test_player_moves_up_with_w_input():
    player = main.Player(x=100, y=100)
    main.apply_player_movement(
        player,
        {"up": True, "down": False, "left": False, "right": False},
        dt=0.1,
    )

    assert player.y < 100


def test_player_stays_in_boundary_after_large_move():
    player = main.Player(x=2, y=2)
    main.apply_player_movement(
        player,
        {"up": True, "down": False, "left": True, "right": False},
        dt=1.0,
    )

    assert player.x >= player.radius
    assert player.y >= player.radius
