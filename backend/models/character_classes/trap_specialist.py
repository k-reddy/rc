from backend.models import action_model as actions
from backend.utils import attack_shapes as shapes
from backend.models import obstacle

trap_specialist_cards = [
    actions.ActionCard(
        attack_name="Ice and Steel",
        actions=[
            actions.SingleTargetAttack(3, 3),
            actions.AreaAttackFromSelf(shape=shapes.line(3), element_type=obstacle.Ice),
        ],
        movement=2,
        jump=True,
    ),
    actions.ActionCard(
        attack_name="Trap Network",
        actions=[
            actions.AreaAttackFromSelf(shape=shapes.arc(5), element_type=obstacle.Trap),
            actions.PushAllEnemies(2, 2),
        ],
        movement=2,
        jump=True,
    ),
    actions.ActionCard(
        attack_name="Frozen Path",
        actions=[
            actions.AreaAttackFromSelf(
                shape=shapes.line(3), element_type=obstacle.Ice, strength=3
            )
        ],
        movement=3,
        jump=True,
    ),
    actions.ActionCard(
        attack_name="Shadow Strike",
        actions=[
            actions.AreaAttackFromSelf(
                shape=shapes.circle(2), element_type=obstacle.Shadow, strength=3
            ),
        ],
        movement=2,
        jump=True,
    ),
    actions.ActionCard(
        attack_name="Deadly Surprise",
        actions=[
            actions.AreaAttackFromSelf(
                shape=shapes.circle(1), element_type=obstacle.Trap
            ),
            actions.Pull(3, 2),
        ],
        movement=2,
        jump=True,
    ),
    actions.ActionCard(
        attack_name="Ice Prison",
        actions=[
            actions.AreaAttackFromSelf(
                shape=shapes.circle(2), element_type=obstacle.Ice, strength=2
            ),
            actions.WeakenAllEnemies(1, 2),
        ],
        movement=1,
        jump=True,
    ),
]

health = 4
