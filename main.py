from collect_data_functions import return_all_item_set_bpa_dicts
from DemsterShafer import DempsterShafer as Ds
from general_functions import check_input_data


def main():

    # if the two input csv files don't exist make them from the scratch
    check_input_data()

    dictionaries = return_all_item_set_bpa_dicts()

    mass_functions = Ds.mass_functions_from_dictionaries(dictionaries)
    final_mass_function = Ds.ds_mc_combination_rule(mass_functions)

    print(final_mass_function)


if __name__ == "__main__":
    main()
