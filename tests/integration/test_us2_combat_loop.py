"""US2 整合測試：戰鬥循環行為。"""

import main


def test_combat_loop_spawns_hits_and_damages():
    state = main.initial_state()
    state.player.x = 300
    state.player.y = 300

    # 先生成敵人
    main.step_simulation(
        state,
        dt=main.ENEMY_SPAWN_INTERVAL,
        input_state={"up": False, "down": False, "left": False, "right": False, "fire": False, "restart": False},
    )
    assert len(state.enemies) >= 1

    # 人工放置一次命中，驗證分數增加
    state.bullets = [main.Bullet(x=state.enemies[0].x, y=state.enemies[0].y, dx=0, dy=-1)]
    score_before = state.score
    main.resolve_combat(state)
    assert state.score == score_before + main.BULLET_DAMAGE_SCORE
