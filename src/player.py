import random

class Player:
    def __init__(
        self,
        position,
        height,
        weight,
        potential,
        speed,
        shooting,
        finishing,
        passing,
        handling,
        perimeter_defense,
        rim_protection,
        rebounding,
        stealing,
        playstyle,
        perk,
    ):
        self.position = position
        self.height = height
        self.weight = weight
        self.potential = potential
        self.speed = speed
        self.shooting = shooting
        self.finishing = finishing
        self.passing = passing
        self.handling = handling
        self.perimeter_defense = perimeter_defense
        self.rim_protection = rim_protection
        self.rebounding = rebounding
        self.stealing = stealing
        self.playstyle = playstyle
        self.perk = perk



class Position(Enum):
    POINT_GUARD = "Point Guard"
    SHOOTING_GUARD = "Shooting Guard"
    SMALL_FORWARD = "Small Forward"
    POWER_FORWARD = "Power Forward"
    CENTER = "Center"

class PlayStyle(Enum):
    FLOOR_GENERAL = "Floor General"
    PLAYMAKER = "Playmaker"
    SHOOTER = "Shooter"
    SLASHER = "Slasher"
    DEFENDER = "Defender"
    POST_SPECIALIST = "Post Specialist"
    RIM_PROTECTOR = "Rim Protector"
    STRETCH = "Stretch"

class Perk(Enum):
    CLUTCH_SHOOTER = "Clutch Shooter"
    LOCKDOWN_DEFENDER = "Lockdown Defender"
    COURT_VISIONARY = "Court Visionary"
    REBOUNDER = "Rebounder"
    SPEED_DEMON = "Speed Demon"

class PlayerFactory:
    @staticmethod
    def create_player(
        position,
        height,
        weight,
        potential,
        speed,
        shooting,
        finishing,
        passing,
        handling,
        perimeter_defense,
        rim_protection,
        rebounding,
        stealing,
        playstyle,
        perk,
    ):
        return Player(
            position,
            height,
            weight,
            potential,
            speed,
            shooting,
            finishing,
            passing,
            handling,
            perimeter_defense,
            rim_protection,
            rebounding,
            stealing,
            playstyle,
            perk,
        )

    @staticmethod
    def generate_random_player():
        position = random.choice(list(Position))
        height = round(random.uniform(5.5, 7.0), 2)
        weight = random.randint(150, 250)
        potential = random.randint(70, 95)
        speed = random.randint(70, 95)
        shooting = random.randint(60, 90)
        finishing = random.randint(60, 90)
        passing = random.randint(60, 90)
        handling = random.randint(60, 90)
        perimeter_defense = random.randint(60, 90)
        rim_protection = random.randint(60, 90)
        rebounding = random.randint(60, 90)
        stealing = random.randint(60, 90)
        playstyle = random.choice(list(PlayStyle))
        perk = random.choice(list(Perk))

        return PlayerFactory.create_player(
            position,
            height,
            weight,
            potential,
            speed,
            shooting,
            finishing,
            passing,
            handling,
            perimeter_defense,
            rim_protection,
            rebounding,
            stealing,
            playstyle,
            perk,
        )

    @staticmethod
    def generate_point_guard():
        # Implement specialized generation for point guards
        # Example: More emphasis on passing and handling skills
        return PlayerFactory.create_player(
            position=Position.POINT_GUARD,
            height=round(random.uniform(5.9, 6.3), 2),
            weight=random.randint(160, 200),
            potential=random.randint(75, 95),
            speed=random.randint(75, 95),
            shooting=random.randint(65, 85),
            finishing=random.randint(65, 85),
            passing=random.randint(80, 95),
            handling=random.randint(80, 95),
            perimeter_defense=random.randint(60, 85),
            rim_protection=random.randint(60, 80),
            rebounding=random.randint(50, 75),
            stealing=random.randint(70, 90),
            playstyle=random.choice([PlayStyle.FLOOR_GENERAL, PlayStyle.PLAYMAKER]),
            perk=random.choice([Perk.COURT_VISIONARY, Perk.CLUTCH_SHOOTER]),
        )
