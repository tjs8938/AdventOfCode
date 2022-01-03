from copy import deepcopy
from typing import List

from src.AoC_2015.Day22.GameState import GameState


class Spell:

    def __init__(self, state: GameState):
        self.state = state
        self.cost = None
        self.remaining_turns = 0
        self.state.mana_spent += self.get_cost()
        self.state.player_mana -= self.get_cost()

    def __repr__(self):
        return str(type(self))

    def on_turn(self, state: GameState):
        self.remaining_turns = max(self.remaining_turns - 1, 0)

    def on_expire(self, state: GameState):
        pass

    def is_expired(self):
        return self.remaining_turns == 0

    def get_cost(self):
        pass

    @staticmethod
    def cast_all_spells(state: GameState) -> List[GameState]:
        new_states = []
        for constructor in [MagicMissile, Recharge, Poison, Shield, Drain]:
            s = deepcopy(state)
            spell = constructor(s)
            if type(spell) not in map(lambda x: type(x), s.active_spells):
                if not spell.is_expired():
                    spell.state.active_spells.append(spell)

                if s.is_valid():
                    new_states.append(s)
                    s.spells_cast.append(spell)

        return new_states


class MagicMissile(Spell):

    def __init__(self, state: GameState):
        super().__init__(state)
        self.state.boss_hp -= 4

    def get_cost(self):
        return 53


class Drain(Spell):

    def __init__(self, state: GameState):
        super().__init__(state)
        self.state.boss_hp -= 2
        self.state.player_hp += 2

    def get_cost(self):
        return 73


class Shield(Spell):

    def __init__(self, state: GameState):
        super().__init__(state)
        self.remaining_turns = 6
        self.state.player_armor += 7

    def get_cost(self):
        return 113

    def on_expire(self, state: GameState):
        state.player_armor -= 7


class Poison(Spell):

    def __init__(self, state: GameState):
        super().__init__(state)
        self.remaining_turns = 6

    def get_cost(self):
        return 173

    def on_turn(self, state: GameState):
        super().on_turn(state)
        state.boss_hp -= 3


class Recharge(Spell):

    def __init__(self, state: GameState):
        super().__init__(state)
        self.remaining_turns = 5

    def get_cost(self):
        return 229

    def on_turn(self, state: GameState):
        super().on_turn(state)
        state.player_mana += 101

