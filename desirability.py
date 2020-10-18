import numpy as np
import time

from DemsterShafer import DempsterShafer as Ds
from general_functions import print_song_sets, print_to_file


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

    return item_set, score_array


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


def average_score(score_array):
    """
    Returns the average scores of all songs

    :param score_array:
    :return:
    """
    song_num = len(score_array)

    scores = 0
    for score in score_array:
        scores += score

    return scores / float(song_num)


def return_results(
    file_name,
    mass_functions,
    conservation_degree,
    threshold,
    song_data,
    is_monte_carlo=True,
):
    """
    Returns the results in a .txt file

    :param file_name:
    :param mass_functions:
    :param conservation_degree:
    :param threshold:
    :param song_data:
    :param is_monte_carlo:
    :return:
    """
    start = time.perf_counter()
    if is_monte_carlo:
        final_mass_function = Ds.ds_mc_combination_rule(mass_functions)
    else:
        final_mass_function = Ds.ds_combination_rule(mass_functions)

    final_item_sets, score_array = find_desirable_sets(
        final_mass_function, threshold, conservation_degree
    )
    end = time.perf_counter()

    result = ""
    result += "The conservation degree: "
    result += str(conservation_degree)
    result += "\nThe songs that we suggest to the users are the following: \n"
    result += print_song_sets(song_data, final_item_sets)
    result += "\nThe scores of the songs: \n"
    result += str(score_array)
    result += "\nAverage song score: "
    result += str(average_score(score_array))
    result += "\nTime: "
    result += str(end - start)
    result += "\n"

    print_to_file(file_name, result)
