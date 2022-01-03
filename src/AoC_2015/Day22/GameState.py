from typing import List


class GameState:

    def __init__(self):
        self.player_hp = 0
        self.player_mana = 0
        self.player_armor = 0

        self.boss_hp = 0
        self.boss_attack = 0

        from src.AoC_2015.Day22.Spell import Spell
        self.active_spells: List[Spell] = []
        self.spells_cast: List[Spell] = []

        self.mana_spent = 0

    def __repr__(self):
        return "Player has {} hit points, {} armor, {} mana\nBoss has {} hit points".format(self.player_hp,
                                                                                            self.player_armor,
                                                                                            self.player_mana,
                                                                                            self.boss_hp)

    def __lt__(self, other):
        return self.mana_spent < other.mana_spent

    def is_valid(self):
        return self.player_mana >= 0 and self.player_hp >= 0

    def is_winner(self):
        return self.boss_hp <= 0

    def apply_effects(self):
        index = 0
        while index < len(self.active_spells):
            spell = self.active_spells[index]
            spell.on_turn(self)
            if spell.is_expired():
                spell.on_expire(self)
                self.active_spells.remove(spell)
            else:
                index += 1

    def boss_turn(self):
        if self.boss_hp > 0:
            self.player_hp -= max(1, self.boss_attack - self.player_armor)
