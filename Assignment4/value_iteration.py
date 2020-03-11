from typing import List, Any, NamedTuple, Dict, Tuple

# Key = State, Value = Reward
reward_matrix: Dict[int, float] = {0: -0.1, 1: -0.1, 2: -0.1, 3: -0.1, 4: -0.1, 5: -1.0, 6: -0.1, 7: -1.0, 8: -0.1,
                                   9: -0.1, 10: - 0.1, 11: -1.0, 12: -1.0, 13: -0.1, 14: -0.1, 15: 1}


__author__ = "Henrik Fjellheim"



transition_matrix: Dict[int, Dict[int, List[Tuple[float, int]]]] = \
    {0: {0: [(9 / 10, 0), (1 / 10, 4)], 1: [(1 / 10, 0), (8 / 10, 4), (1 / 10, 1)],
         2: [(1 / 10, 4), (8 / 10, 1), (1 / 10, 0)],
         3: [(1 / 10, 1), (9 / 10, 0)]},
     1: {0: [(1 / 10, 1), (8 / 10, 0), (1 / 10, 5)], 1: [(1 / 10, 0), (8 / 10, 5), (1 / 10, 2)],
         2: [(1 / 10, 5), (8 / 10, 2), (1 / 10, 1)],
         3: [(1 / 10, 2), (8 / 10, 1), (1 / 10, 0)]},
     2: {0: [(1 / 10, 2), (8 / 10, 1), (1 / 10, 6)], 1: [(1 / 10, 1), (8 / 10, 6), (1 / 10, 3)],
         2: [(1 / 10, 6), (8 / 10, 3), (1 / 10, 2)],
         3: [(1 / 10, 3), (8 / 10, 2), (1 / 10, 1)]},
     3: {0: [(1 / 10, 3), (8 / 10, 2), (1 / 10, 7)], 1: [(1 / 10, 2), (8 / 10, 7), (1 / 10, 3)],
         2: [(1 / 10, 7), (9 / 10, 3)],
         3: [(9 / 10, 3), (1 / 10, 2)]},
     4: {0: [(1 / 10, 0), (8 / 10, 4), (1 / 10, 8)], 1: [(1 / 10, 4), (8 / 10, 8), (1 / 10, 5)],
         2: [(1 / 10, 8), (8 / 10, 5), (1 / 10, 0)],
         3: [(1 / 10, 5), (8 / 10, 0), (1 / 10, 4)]},
     5: {0: [(1.0, 5)], 1: [(1.0, 5)], 2: [(1.0, 5)], 3: [(1.0, 5)]},
     6: {0: [(1 / 10, 2), (8 / 10, 5), (1 / 10, 10)], 1: [(1 / 10, 5), (8 / 10, 10), (1 / 10, 7)],
         2: [(1 / 10, 10), (8 / 10, 7), (1 / 10, 2)],
         3: [(1 / 10, 7), (8 / 10, 2), (1 / 10, 5)]},
     7: {0: [(1.0, 7)], 1: [(1.0, 7)], 2: [(1.0, 7)], 3: [(1.0, 7)]},
     8: {0: [(1 / 10, 4), (8 / 10, 8), (1 / 10, 12)], 1: [(1 / 10, 8), (8 / 10, 12), (1 / 10, 9)],
         2: [(1 / 10, 12), (8 / 10, 9), (1 / 10, 4)],
         3: [(1 / 10, 9), (8 / 10, 4), (1 / 10, 8)]},
     9: {0: [(1 / 10, 5), (8 / 10, 8), (1 / 10, 13)], 1: [(1 / 10, 8), (8 / 10, 13), (1 / 10, 10)],
         2: [(1 / 10, 13), (8 / 10, 10), (1 / 10, 5)],
         3: [(1 / 10, 10), (8 / 10, 5), (1 / 10, 8)]},
     10: {0: [(1 / 10, 6), (8 / 10, 9), (1 / 10, 14)], 1: [(1 / 10, 9), (8 / 10, 14), (1 / 10, 11)],
          2: [(1 / 10, 14), (8 / 10, 11), (1 / 10, 6)],
          3: [(1 / 10, 11), (8 / 10, 6), (1 / 10, 9)]},
     11: {0: [(1.0, 11)], 1: [(1.0, 11)], 2: [(1.0, 11)], 3: [(1.0, 11)]},
     12: {0: [(1.0, 12)], 1: [(1.0, 12)], 2: [(1.0, 12)], 3: [(1.0, 12)]},
     13: {0: [(1 / 10, 9), (8 / 10, 12), (1 / 10, 13)], 1: [(1 / 10, 12), (8 / 10, 13), (1 / 10, 14)],
          2: [(1 / 10, 13), (8 / 10, 14), (1 / 10, 9)], 3: [(1 / 10, 14), (8 / 10, 9), (1 / 10, 12)]},
     14: {0: [(1 / 10, 10), (8 / 10, 13), (1 / 10, 14)], 1: [(1 / 10, 13), (8 / 10, 14), (1 / 10, 15)],
          2: [(1 / 10, 14), (8 / 10, 15), (1 / 10, 10)], 3: [(1 / 10, 15), (8 / 10, 10), (1 / 10, 13)]},
     15: {0: [(1.0, 15)], 1: [(1.0, 15)], 2: [(1.0, 15)], 3: [(1.0, 15)]}}

moves: Dict[str, int] = {"left": 0, "down": 1, "right": 2, "up": 3}


# ------------------------------- Nothing you need or need to do above this line ---------------------------------------

def get_outcome_states(state: int, action: str) -> List[int]:
    """
    Fetch the possible outcome states given the current state and action taken.
    :param state: The current state which is a number between 0-15 as there are 16 states (16 tiles).
    :param action: The action taken which is a string, either: left, down, right, or up.
    :return: A list of possible outcome states. Each state is a number between 0-15 as there are 16 states (16 tiles).
    """
    assert isinstance(state, int) and 0 <= state < 16, "States must be an integer between 0 - 15."
    assert action in moves.keys(), "Action must be either: left, down, right, or up."

    return [next_state for _, next_state in transition_matrix[state][moves[action]]]


def get_transition_probability(state: int, action: str, outcome_state: int) -> float:
    """
    Fetch the transition probability for the provided outcome states given the current state and action taken.
    :param state: The current state which is a number between 0-15 as there are 16 states (16 tiles)
    :param action: The action taken which is a string, either: left, down, right, or up.
    :param outcome_state: The outcome state which is a number between 0-15 as there are 16 states (16 tiles). However,
    not all of the 16 states are possible, but depends on your current state.
    :return: The transition probability.
    """
    assert isinstance(state, int) and 0 <= state < 16, "States must be an integer between 0 - 15."
    assert action in moves.keys(), "Action must be either: left, down, right, or up."
    assert isinstance(outcome_state, int) and 0 <= outcome_state < 16, "States must be an integer between 0 - 15."

    return {next_state: trans_prob for trans_prob, next_state in transition_matrix[state][moves[action]]}[
        outcome_state]


def get_reward(state: int) -> float:
    """
    Fetch the reward given the current state.
    :param state: The current state which is a number between 0-15 as there are 16 states (16 tiles).
    :return: The reward.
    """
    assert isinstance(state, int) and 0 <= state < 16, "States must be an integer between 0 - 15."

    return reward_matrix[state]


class Constants(NamedTuple):
    """
    This class provides the necessary constants you need to implement the value iteration algorithm.
    In order to access the field you can write e.g. constants.gamma if you need to access the field gamma.

    Attributes
    ----------
    number_states : int
        Number of states in this Markov decision process.
    number_actions : int
        The size of the action space.
    gamma: float
        The discount factor.
    epsilon: float
        The maximum error allowed in the utility of any state.
    """
    number_states: int = 16
    number_actions: int = 4
    epsilon: float = 1e-20
    gamma: float = 0.9


# This variable contains all constants you will need
constants: Constants = Constants()


def value_iteration() -> Any:
    """
    Implement the value iteration algorithm described in Figure 17.4 in the book.

    Note: Everything you need to implement this algorithm is either stored in the variable "constants" above or can be
    accessed through one of the functions above.

    :return: The converged utility values of all states.
    """

    utility_matrix: Dict[int, float] = {0: 0, 1: -0, 2: 0, 3: 0, 4: 0, 5: 0,
                                        6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0}
    delta: float = 1
    num_iterations = 0

    while delta > constants.epsilon:
        num_iterations += 1
        delta = 0   # The biggest change of any value in utility matrix.
        for i in range(constants.number_states):
            before_update = utility_matrix[i]
            max_value: float = 0
            for action in moves.keys():
                action_sum: float = 0
                for outcome in get_outcome_states(i, action):
                    action_sum += get_transition_probability(i, action, outcome) * utility_matrix[outcome]

                if action_sum > max_value:
                    max_value = action_sum

            utility_matrix[i] = get_reward(i) + constants.gamma * max_value

            update_factor = abs(before_update - utility_matrix[i])
            if update_factor > delta:
                delta = update_factor

    print("Number of iterations:", num_iterations)
    return utility_matrix


def extract_policy(value_table: Any) -> Any:
    """
    Extract policy based on the given value_table.
    :param value_table: dict containing the converged utility values.
    :return: The extracted policy.
    """
    policy_matrix: Dict[int, str] = {0: "x", 1: "x", 2: "x", 3: "x", 4: "x", 5: "x", 6: "x", 7: "x", 8: "x",
                                     9: "x", 10: "x", 11: "x", 12: "x", 13: "x", 14: "x", 15: "x"}

    for i in range(constants.number_states):
        best_action = "x"
        best_action_value = -10
        for action in moves.keys():
            for outcome in get_outcome_states(i, action):
                transition_value = get_transition_probability(i, action, outcome) * value_table[outcome]
                if best_action_value < transition_value:
                    best_action_value = transition_value
                    best_action = action

            policy_matrix[i] = best_action

    return policy_matrix


def print_util_matrix(utility_matrix):
    """
    Print out a dictionary as if it were a 4x4 matrix of 16 inputs.
    :param utility_matrix: dictionary of 16 keys.
    """
    print("----------------------------------")
    for i in range(16):
        if i == 0:
            print("|", end="\t")
        if i % 4 == 0 and i != 0 and i != 16:
            print("|\n|", end="\t")
        print(round(utility_matrix[i], 2), end="\t")
        if i == 15:
            print("|")

    print("----------------------------------")


def print_policy_matrix(utility_matrix):
    print("----------------------------------")
    for i in range(16):
        if i == 0:
            print("|", end="\t")
        if i % 4 == 0 and i != 0 and i != 16:
            print("|\n|", end="\t")
        print(utility_matrix[i], end="\t")
        if i == 15:
            print("|")

    print("----------------------------------")


def main() -> None:
    """
    Run the script.
    :return: Nothing.
    """
    print_util_matrix(reward_matrix)

    value_table = value_iteration()
    print_util_matrix(value_table)
    optimal_policy = extract_policy(value_table)
    print_policy_matrix(optimal_policy)


if __name__ == '__main__':
    main()
