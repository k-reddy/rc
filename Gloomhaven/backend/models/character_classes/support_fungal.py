from backend.models import action_model as actions
from backend.utils import attack_shapes as shapes
from backend.models import obstacle

cards = [
    actions.ActionCard(
        attack_name="Healing Spores",
        actions=[
            actions.HealAllAllies(3, 3),
            actions.ElementAreaEffectFromSelf(
                shape=shapes.circle(1),
                element_type=obstacle.Spores
            )
        ],
        movement=2,
        jump=False
    ),
    actions.ActionCard(
        attack_name="Mushroom Ring",
        actions=[
            actions.ElementAreaEffectFromSelf(
                shape=shapes.ring(2),
                element_type=obstacle.PoisonShroom
            ),
            actions.ShieldAllAllies(2, 2, 2)
        ],
        movement=1,
        jump=False
    ),
    actions.ActionCard(
        attack_name="Rejuvenating Fungus",
        actions=[
            actions.HealAlly(5, 1),
            actions.BlessAndChargeAlly(2, 1)
        ],
        movement=2,
        jump=False
    ),
    actions.ActionCard(
        attack_name="Spore Cloud",
        actions=[
            actions.ElementAreaEffectFromSelf(
                shape=shapes.circle(2),
                element_type=obstacle.Spores
            ),
            actions.WeakenAllEnemies(2, 2)
        ],
        movement=2,
        jump=False
    ),
    actions.ActionCard(
        attack_name="Growth Burst",
        actions=[
            actions.HealAllAllies(2, 2),
            actions.BlessAllAllies(2)
        ],
        movement=1,
        jump=False
    ),
    actions.ActionCard(
        attack_name="Protective Bloom",
        actions=[
            actions.ShieldAllAllies(2, 2, 2),
            actions.ElementAreaEffectFromSelf(
                shape=shapes.ring(3),
                element_type=obstacle.PoisonShroom
            )
        ],
        movement=2,
        jump=False
    )
]

health = 4