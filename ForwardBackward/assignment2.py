# Imported libraries
import numpy as np

__author__: "Henrik Fjellheim"


# GLOBAL VARIABLES, as the author of this code was lazy...
TransitionModel = np.matrix("0.7 0.3; 0.3 0.7")     # Transition model
SensorModel1 = np.matrix("0.9 0.0; 0.0 0.2")        # For when u is "brought umbrella"
SensorModel2 = np.matrix("0.1 0.0; 0.0 0.8")        # For when u is "did not bring"

# Make sure to run the code, as i have implemented a menu for testing different functionality more easily [hopefully]


def main():
    """
    All testing. Run this file for a "nice" UI-menu-thingy
    """
    choice = "horse"

    while choice != 0:
        # # # MENU RELATED CODE # # #
        print("--------------------------")
        print("Choose test from menu:\n",
              "0 - Exit\n",
              "1 - B verify implementation of 'Forward'\n",
              "2 - C Verifying the implementation of fb algorithm\n",
              "3 - Smoothing for 5 observations using forward-backward algorithm")
        print("--------------------------")

        try:
            choice = int(input("Answer: "))
        except ValueError:
            print("Wrong input...")

        # # # MENU RELATED CODE # # #

        if choice == 0:
            break

        elif choice == 1:
            print("Testing forward-algorithm")

            observations = [True, True, False, True, True]  # Observed values of umbrella-usage
            prob_raining = np.matrix("0.5; 0.5")            # Starting assumption (same as made in book)
            i = 1

            for obs in observations:
                prob_raining = forward(obs, prob_raining)
                print("Probability of raining on day", i, prob_raining[0])
                i += 1

        elif choice == 2:
            print("Smoothing function using forward-backward algorithm!")

            observations = [True, True]             # A given set of observations
            prob_raining = np.matrix("0.5; 0.5")    # Starting assumption (same as made in book)
            smooth_vector = forward_backward(observations, prob_raining)
            print("Smooth vector:", smooth_vector)

        elif choice == 3:
            print("Smoothing function using forward-backward algorithm!")

            observations = [True, True, False, True, True]  # A given set of observations
            prob_raining = np.matrix("0.5; 0.5")            # Starting assumption (same as made in book)
            smooth_vector = forward_backward(observations, prob_raining)

            print("Smooth vector:", smooth_vector)


def normalize(matrix):
    """
    Normalizes the individual columns of the matrix.
    sum(matrix) returns a vector of the sum of each column, multiplying by the inverse vector gives
    a normalized result.
    :param matrix: A random nxn matrix
    :return: a normalized matrix
    """
    return matrix * 1 / sum(matrix)


def forward(observation, prev):
    """
    The recursive forward function, using previous calculations as well as current umbrella observation as input.
    Formula (15.12) in the book.
    :param observation: is the umbrella there or not today
    :param prev: last iterations filtering, used to save computing time.
    :return: state estimation of X_t+1 using filtering.
    """
    # Step 1: project the current state forward using transition model and previous recursive result
    s1 = np.dot(np.transpose(TransitionModel), prev)

    # Step2: Update using observation, normalize before return
    if observation:
        # Umbrella!
        return normalize(np.dot(SensorModel1, s1))
    # No umbrella!
    return normalize(np.dot(SensorModel2, s1))


def backward(observation, prev):
    """
    Sends a message back in time, calculating how likely certain observations were given observations since
    :param observation: Observation in current timeslice. [remember! We move backwards in time here!]
    :param prev: from last iterations of backward, used to save computing time.
    :return: probability of observations since this timeslice given presumed state of the timeslice.
    """
    if observation:
        return np.dot(np.dot(TransitionModel, SensorModel1), prev)
    return np.dot(np.dot(TransitionModel, SensorModel2), prev)


def forward_backward(observations, prior):
    """
    Full smoothing algorithm --> "smooth"
    :param observations: All observations up until for timeslice 1, .... , t
    :param prior: P(X_0) = distribution in initial state.
    :return: a vector of smoothed estimates for steps 1, .... , t
    """
    time_slice = len(observations)
    backward_vector = np.matrix("1; 1")         # Initial state used in backward-recursion
    forward_vector = [prior]                    # Vector containing all 2x1 vectors of forward-results
    smooth_vector = []                          # Vector containing smoothed out values of the probabilities

    for i in range(time_slice + 1):
        # In order to fill it with something, making us able to work our way backwards later
        # Its a dirty method, but the best i found.
        smooth_vector.append(prior)

    for i in range(0, time_slice):
        # It might seem like my code differs from the algorithm here,
        # but the first observation in the observations-list is corresponding to the second state (X_1) and
        # not the first state (X_0), even if it is at index 0 and not 1.
        forward_vector.append(forward(observations[i], forward_vector[i]))

    # Variable used for neater prints of backward-messages.
    nr = 1
    for i in range(time_slice, 0, -1):
        print("Backward message nr", nr,"\n", backward_vector)
        smooth_vector[i] = normalize(np.multiply(forward_vector[i], backward_vector))
        backward_vector = backward(observations[i - 1], backward_vector)
        nr += 1

    return smooth_vector


main()
