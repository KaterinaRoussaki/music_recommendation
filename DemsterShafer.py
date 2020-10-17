from pyds import MassFunction


class DempsterShafer:
    @staticmethod
    def mass_functions_from_dictionaries(dictionary_array):
        """
        Returns an array with mass_functions of a array of dictionaries

        :param dictionary_array:
        :returns array of mass functions
        """
        mass_function_array = []

        for dictionary in dictionary_array:
            mass_function_array.append(MassFunction(dictionary))

        return mass_function_array

    @staticmethod
    def ds_combination_rule(mass_function_array):
        """
        Returns the mass function after using the Dempster Shafer combination rule

        :param mass_function_array:
        :returns dictionary of mass functions, Dempster Shafer
        """
        dempster_shafer = mass_function_array[0] & mass_function_array[1]

        for mass_function in mass_function_array[2:]:
            dempster_shafer = dempster_shafer & mass_function

        return dempster_shafer

    @staticmethod
    def ds_mc_combination_rule(
        mass_function_array,
        sample_count=1000,
        importance_sampling=True,
        normalization=True,
    ):
        """
        Returns the mass function after using the Dempster Shafer combination rule via using monte carlo

        :param normalization:
        :param importance_sampling:
        :param sample_count:
        :param mass_function_array:
        :returns dictionary of mass functions, monte carlo
        """
        monte_carlo = mass_function_array[0] & mass_function_array[1]

        for mass_function in mass_function_array[2:]:
            monte_carlo = monte_carlo.combine_conjunctive(
                mass_function,
                sample_count=sample_count,
                importance_sampling=importance_sampling,
                normalization=normalization,
            )

        return monte_carlo

    @staticmethod
    def return_belief(item_dict, mass_function):
        """
        Make a query by using an item dictionary and find it's belief

        :param mass_function:
        :param item_dict:
        :returns float belief
        """
        return mass_function.bel(item_dict)

    @staticmethod
    def return_entire_belief(mass_function):
        """
        Return the entire belief function

        :param mass_function:
        :returns dictionary
        """
        return mass_function.bel()

    @staticmethod
    def return_plausibility(item_dict, mass_function):
        """
        Make a query by using an item dictionary and find it's plausibility

        :param mass_function:
        :param item_dict:
        :returns float plausibility
        """
        return mass_function.pl(item_dict)

    @staticmethod
    def return_entire_plausibility(mass_function):
        """
        Return the entire belief function

        :param mass_function:
        :returns dictionary
        """
        return mass_function.pl()
