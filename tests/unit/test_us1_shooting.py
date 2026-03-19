"""US1 單元測試：射擊生成與子彈更新。"""

import main


def test_create_bullet_spawns_in_front_of_player():
    player = main.Player(x=200, y=300)

    bullet = main.create_bullet(player)

    # 期望子彈起始點在玩家前方，避免一生成就與玩家中心重疊。
    assert bullet.y < player.y


def test_bullet_moves_forward_after_update():
    player = main.Player(x=200, y=300)
    bullet = main.create_bullet(player)

    updated = main.update_bullets([bullet], dt=0.1)

    assert len(updated) == 1
    assert updated[0].y < bullet.y + 0.01
