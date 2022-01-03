from src.AoC_2015.Day22.BinarySearchTree import BinarySearchTree
from src.AoC_2015.Day22.GameState import GameState
from src.AoC_2015.Day22.Spell import Spell


game_states = BinarySearchTree[GameState]()
first_state = GameState()

first_state.boss_hp = 109
first_state.boss_armor = 2
first_state.boss_attack = 8

first_state.player_hp = 50
first_state.player_mana = 500

game_states.insert(first_state)

while True:
    # Get the lowest cost game state
    lowest_cost = game_states.pop_left()

    # Apply effects of previously cast spells
    lowest_cost.apply_effects()

    # If the boss is dead, this is the lowest cost winning state
    if lowest_cost.is_winner():
        print("Winner: " + str(lowest_cost.mana_spent))
        break

    # Cast all allowable spells (enough mana, effect not already in place)
    new_states = Spell.cast_all_spells(lowest_cost)

    # For each new state, simulate the boss's turn and then add to the list
    for state in new_states:
        state.apply_effects()
        state.boss_turn()
        game_states.insert(state)
