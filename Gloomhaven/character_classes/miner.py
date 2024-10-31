import gh_types
import attack_shapes as shapes


cards = [
# Stone Foundation - Create impassable stone barrier length 2, shield all adjacent allies
    gh_types.ActionCard(
        attack_name="Heavy Hammer",
        actions=[
            gh_types.SingleTargetAttack(
                strength=4,
                att_range=1
            ),
            gh_types.ChargeNextAttack(
                strength=2
            )
        ],
        movement=0,
        jump=False
    ),
    gh_types.ActionCard(
        attack_name="Pickaxe Swipe",
        actions=[
            gh_types.AreaAttack(
                shape=shapes.arc(4),
                strength=2
            )
        ],
        movement=2,
        jump=False
    ),
    gh_types.ActionCard(
        attack_name="Mason's Shield",
        actions=[
            gh_types.ShieldSelf(
                strength=1,
                duration=2
            ),
            gh_types.SingleTargetAttack(
                strength=4,
                att_range=1
            )
        ],
        movement=0,
        jump=False
    ),
    gh_types.ActionCard(
        attack_name="Stone Meditation",
        actions=[
            gh_types.ShieldSelf(
                strength=2,
                duration=1
            ),
            gh_types.ModifySelfHealth(
                strength=4
            )
        ],
        movement=0,
        jump=False
    ),
    gh_types.ActionCard(
        attack_name="Crystal Placebo",
        actions=[
            gh_types.ModifySelfHealth(strength=4),
            gh_types.SingleTargetAttack(
                strength=2,
                att_range=1
            ),
        ],
        movement=0,
        jump=False
    ),
    gh_types.ActionCard(
        attack_name="Self Sacrifice",
        actions=[
            gh_types.SingleTargetAttack(
                strength=6,
                att_range=1
            ),
            gh_types.BlessSelf(),
            gh_types.ModifySelfHealth(-4)
        ],
        movement=1,
        jump=False   
    ),
    gh_types.ActionCard(
        attack_name="Desperate Mining",
        actions=[
            gh_types.AreaAttack(shape=shapes.circle(2),strength=1),
            gh_types.BlessSelf(),
            gh_types.ChargeNextAttack(strength=4),
            gh_types.ModifySelfHealth(-5),
        ],
        movement=0,
        jump=False
    ),
    gh_types.ActionCard(
        # Tax Assessment - Weaken target, pull 2, attack 3
        attack_name="Tax Assessment",
        actions=[
            gh_types.Pull(
                squares=2, 
                att_range=2
            )
        ],
        movement=10,
        jump=False
    )
]
backstory = ""
health = 16