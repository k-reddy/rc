from gh_types import ActionCard
import attack_shapes as shapes

cards = [
    ActionCard(
        attack_name="Fireball",
        attack_shape=None,
        strength=0,
        distance=4,
        movement=2,
        status_effect="Fire",
        status_shape=shapes.circle(1),
        jump=False
    ),
    ActionCard(
        attack_name="Cursed Frost Surge",
        attack_shape=shapes.bar(1,2),
        strength=1,
        distance=4,
        movement=2,
        status_effect="Ice",
        status_shape=shapes.bar(1,2),
        jump=False
    ),
    ActionCard(
        attack_name="Elementary Missile",
        attack_shape=None,
        strength=5,
        distance=4,
        movement=0,
        status_effect=None,
        status_shape=None,
        jump=False
    ),
    ActionCard(
        attack_name="Scholar's Escape",
        attack_shape=None,
        strength=1,
        distance=1,
        movement=5,
        status_effect=None,
        status_shape=None,
        jump=False
    ),
    ActionCard(
        attack_name="Masochistic Explosion",
        attack_shape=None,
        strength=0,
        distance=1,
        movement=0,
        status_effect="Fire",
        status_shape=shapes.circle(2),
        jump=False
    ),
    ActionCard(
        attack_name="Lightning Bolt",
        attack_shape=shapes.line((1,0), 3),
        strength=4,
        distance=0,
        movement=1,
        status_effect=None,
        status_shape=None,
        jump=False
    ),
    # !!! to implement - randomly teleports target 
    # ActionCard(
    #     attack_name="Random Teleport",
    #     attack_shape=None,
    #     strength=2,
    #     distance=1,
    #     movement=1,
    #     status_effect=Teleport,
    #     status_shape=None,
    #     jump=False
    # ),
    ActionCard(
        attack_name="B-Line",
        attack_shape=shapes.line((0,1), 2),
        strength=2,
        distance=0,
        movement=2,
        status_effect=None,
        status_shape=None,
        jump=True
    ),
]

backstory = "wizards are cool"

health = 6
