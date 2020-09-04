from DemsterShafer import DempsterShafer as Ds


"""
    Searches all the item sets and returns the best item suggestions

    @:param mass_functions = all the mass functions in a dictionary form
    @:param threshold
    @:returns set
"""


def find_desirable_sets(mass_functions, threshold, conservation_degree=0):
    item_set = set()

    for key in mass_functions:
        if set_desirability(mass_functions, key, conservation_degree, threshold):
            item_set = item_set.union(key)

    return item_set


def set_desirability(mass_function, item_set, conservation_degree, threshold=0.5):
    plausibility = Ds.return_plausibility(item_set, mass_function)
    belief = Ds.return_belief(item_set, mass_function)
    desirability = (
        conservation_degree * plausibility + (1 - conservation_degree) * belief
    )

    if desirability > threshold:
        return True
    else:
        return False
