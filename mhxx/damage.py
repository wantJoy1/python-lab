import math

NORMAL_CRITICAL_OFFSET = 0.25
ATTACK_SHARPNESS_OFFSETS: dict[str, int] = {
    "green": 1.05,
    "blue": 1.20,
    "white": 1.32,
    "purple": 1.39,
}
ELEMENT_SHARPNESS_OFFSETS: dict[str, int] = {
    "green": 1.00,
    "blue": 1.0625,
    "white": 1.125,
    "purple": 1.2,
}

def calc_gunner_damage(attack, critical):
    critical_offset = calc_critical_offset(critical)
    return (attack + 15) * critical_offset
    

def calc_critical_offset(critical):
    return 1 + (NORMAL_CRITICAL_OFFSET * critical / 100.0)


def calc_damage(attack, critical, element, sharpness):
    physical_damage = calc_physical_damage(attack, critical, sharpness)
    element_damage = calc_element_damage(element, sharpness)

    return physical_damage + element_damage


def calc_physical_damage(attack, critical, sharpness):
    attack_sharpness_offset = ATTACK_SHARPNESS_OFFSETS[sharpness]
    critical_offset = calc_critical_offset(critical)
    return (attack + 15) * critical_offset * attack_sharpness_offset


def calc_element_damage(element, sharpness):
    element_sharpness_offset = ELEMENT_SHARPNESS_OFFSETS[sharpness]
    return element * element_sharpness_offset


class Weapon:
    name: str = "name"
    attack: int = 100
    critical: float = 0.0
    element: int = 0
    sharpness: str = "purple"

    def __init__(self, name, attack, critical, element, sharpness) -> None:
        self.name = name
        self.attack = attack
        self.critical = critical
        self.element = element
        self.sharpness = sharpness


dragons: list[Weapon] = [
    Weapon("アンクofシーカー", 320, 25, 25, "white"),
    Weapon("アンクofシーカー", 320, 25, 25, "purple"),
    Weapon("THEシャロック", 280, 35, 34, "white"),
    Weapon("THEシャロック", 280, 35, 34, "purple"),
    Weapon("真・祖龍霊剣 不還", 300, 0, 44, "white"),
    Weapon("真・祖龍霊剣 不還", 300, 0, 44, "purple"),
    Weapon("赫醒剣アルゴルク", 300, 0, 44, "white"),
    Weapon("神滅剣アル・ゾディア", 280, 0, 55, "white"),
    Weapon("神滅剣アル・ゾディア", 280, 0, 55, "purple"),
    Weapon("神滅剣アル・ゾディア", 280, 0, 66, "purple"),
]

thunders: list[Weapon] = [
    Weapon("ドレッドフルレイザー", 320, 15, 40, "white"),
    Weapon("ドレッドフルレイザー", 320, 15, 40, "purple"),
    Weapon("原種ジンオウガ", 320, 0, 35, "white"),
    Weapon("原種ジンオウガ", 320, 0, 35, "purple"),
    Weapon("二つ名ジンオウガ", 300, 5, 45, "white"),
    Weapon("二つ名ジンオウガ", 300, 5, 45, "purple"),
    Weapon("キリン", 250, 0, 58, "white"),
]

fires: list[Weapon] = [
    Weapon("二つ名レウス", 310, 5, 42, "white"),
    Weapon("二つ名レウス", 310, 5, 42, "purple"),
]

waters: list[Weapon] = [
    Weapon("二つ名ミツネ", 320, 20, 30, "white"),
    Weapon("二つ名ミツネ", 320, 20, 30, "purple"),
]

ices: list[Weapon] = [
    Weapon("二つ名ガムート", 380, 5, 16, "blue"),
    Weapon("二つ名ガムート", 380, 5, 16, "white"),
    Weapon("アヴァイシュドゼロ", 310, 0, 48, "white"),
    Weapon("アヴァイシュドゼロ", 310, 0, 48, "purple"),
    Weapon("ジェロアクザル", 330, -10, 33, "white"),
    Weapon("ジェロアクザル", 330, -10, 33, "purple"),
]

paralysis: list[Weapon] = [
    Weapon("デスレストレイン", 300, 0, 0, "white"),
    Weapon("デスレストレイン", 300, 10, 0, "white"),
    Weapon("にゃんにゃんぼう", 280, 0, 0, "white"),
    Weapon("にゃんにゃんぼう", 280, 20, 0, "white"),
    Weapon("パラスパイクロンド", 310, -10, 0, "white"),
    Weapon("パラスパイクロンド", 310, -10, 0, "purple"),
    Weapon("パラスパイクロンド", 310, 0, 0, "white"),
    Weapon("パラスパイクロンド", 310, 0, 0, "purple"),
]

physicals: list[Weapon] = [
    # 479
    Weapon("ウンネフェル", 330, 0, 0, "purple")
]

def main(weapons):
    for weapon in weapons:
        [name, attack, critical, element, sharpness] = [
            weapon.name,
            weapon.attack,
            weapon.critical,
            weapon.element,
            weapon.sharpness,
        ]
        damage = math.floor(calc_damage(attack, critical, element, sharpness))
        physical_damage = math.floor(calc_physical_damage(attack, critical, sharpness))
        element_damage = math.floor(calc_element_damage(element, sharpness))
        print(
            name,
            damage,
            f"physical: {physical_damage}",
            f"element: {element_damage}",
            sep=" | ",
        )
