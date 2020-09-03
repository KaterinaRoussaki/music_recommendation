from pyds import MassFunction


"""
    Searches all the item sets and returns the best item suggestions
    
    @:param mass_functions = all the mass functions in a dictionary form 
    @:param threshold
    @:returns set
"""


def find_desirable_sets(mass_functions, threshold, conservation_degree=0):
    item_set = set()

    for key in mass_functions:
        if DempsterShafer.set_desirability(
            mass_functions, key, conservation_degree, threshold
        ):
            item_set = item_set.union(key)

    return item_set


class DempsterShafer:
    """

    Returns an array with mass_functions of a array of dictionaries

    @:param array of dictionaries
    @:returns array of mass functions

    """

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def return_belief(item_dict, mass_function):
        return mass_function.bel(item_dict)

    """
        Return the entire belief function
        
        @:param dictionary with items
        @:returns dictionary 
    """

    @staticmethod
    def return_entire_belief(mass_function):
        return mass_function.bel()

    """
        Make a query by using an item dictionary and find it's plausibility
        
        @:param string dictionary
        @:param mass function
        @:returns float plausibility 
    """

    @staticmethod
    def return_plausibility(item_dict, mass_function):
        return mass_function.pl(item_dict)

    """
        Return the entire belief function
        
        @:param dictionary with items
        @:returns dictionary 
    """

    @staticmethod
    def return_entire_plausibility(mass_function):
        return mass_function.pl()

    """
        Returns true if the desirability of an item set is greater than the threshold
    
        @:param mass function dictionary
        @:param threshold for the desirability
        @:param conservation_degree
        @:param item_set
        @:returns boolean 
    """

    @staticmethod
    def set_desirability(mass_function, item_set, conservation_degree, threshold=0.5):
        plausibility = mass_function.pl(item_set)
        belief = mass_function.bel(item_set)
        desirability = (
            conservation_degree * plausibility + (1 - conservation_degree) * belief
        )

        if desirability > threshold:
            return True
        else:
            return False
