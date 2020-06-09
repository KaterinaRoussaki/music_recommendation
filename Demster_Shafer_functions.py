from pyds import MassFunction


"""

Returns an array with mass_functions of a array of dictionaries

@:param array of dictionaries
@:returns array of mass functions

"""


def mass_functions_from_dictionaries(dictionary_array):
    mass_function_array = []

    for dictionary in dictionary_array:
        mass_function_array.append(MassFunction(dictionary))

    return mass_function_array


"""

Returns the mass function after using the Dempster Shafer combination rule

@:param array of mass functions
@:returns dictionary of mass functions, Dempster Shafer

"""


def ds_combination_rule(mass_function_array):
    dempster_shafer = mass_function_array[0] & mass_function_array[1]

    for mass_function in mass_function_array[2:]:
        dempster_shafer = dempster_shafer & mass_function

    return dempster_shafer


"""

Returns the mass function after using the Dempster Shafer combination rule via using monte carlo 

@:param array of mass functions
@:returns dictionary of mass functions, monte carlo 

"""


def ds_mc_combination_rule(mass_function_array):
    monte_carlo = mass_function_array[0] & mass_function_array[1]

    for mass_function in mass_function_array[2:]:
        monte_carlo = monte_carlo.combine_conjunctive(
            mass_function, sample_count=1000, importance_sampling=True
        )

    return monte_carlo


"""

Make a query by using an item dictionary and find it's belief

@:param dictionary with items
@:param mass function
@:returns float belief 

"""


def return_belief(item_dict, mass_function):
    return mass_function.bel(item_dict)


"""

Return the entire belief function

@:param dictionary with items
@:returns dictionary 

"""


def return_entire_belief(mass_function):
    return mass_function.bel()


"""

Make a query by using an item dictionary and find it's plausibility

@:param string dictionary
@:param mass function
@:returns float plausibility 

"""


def return_plausibility(item_dict, mass_function):
    return mass_function.pl(item_dict)


"""

Return the entire belief function

@:param dictionary with items
@:returns dictionary 

"""


def return_entire_plausibility(mass_function):
    return mass_function.pl()
