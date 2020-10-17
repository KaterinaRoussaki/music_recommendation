import numpy as np

from DemsterShafer import DempsterShafer as Ds


def desirability(conservation_degree, belief, plausibility):
    """
    returns the desirability
    we could face underflow thus we use the
    """
    des1 = np.multiply(conservation_degree, plausibility)
    des2 = np.multiply((1 - conservation_degree), belief)
    return np.add(des1, des2)


def find_desirable_sets(mass_functions, threshold, conservation_degree=0):
    """
    Searches all the item sets and returns the best item suggestions

    :param mass_functions:
    :param threshold:
    :param conservation_degree:
    :return: set, array
    """
    item_set = set()
    score_array = []

    for key in mass_functions:
        is_desirable, score = find_set_desirability(
            mass_functions, key, conservation_degree, threshold
        )
        if is_desirable:
            item_set = item_set.union(key)
            score_array.append(score)

    return item_set


def find_set_desirability(mass_function, item_set, conservation_degree, threshold=0.5):
    """
    Finds the desirability of a

    :param mass_function:
    :param item_set:
    :param conservation_degree:
    :param threshold:
    :return: bool, float
    """
    plausibility = Ds.return_plausibility(item_set, mass_function)
    belief = Ds.return_belief(item_set, mass_function)
    des = desirability(conservation_degree, belief, plausibility)

    if des > threshold:
        return True, des
    else:
        return False, None
