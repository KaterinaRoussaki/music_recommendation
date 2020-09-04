from collect_data_functions import read_data, return_all_item_set_bpa_dicts
from DemsterShafer import DempsterShafer as Ds
from desirability import find_desirable_sets
from general_functions import create_input_data, print_song_sets


def main():
    create_input_data(10000)

    likes_data, songs_data = read_data()

    dictionaries = return_all_item_set_bpa_dicts(likes_data, songs_data)

    mass_functions = Ds.mass_functions_from_dictionaries(dictionaries)

    final_mass_function = Ds.ds_mc_combination_rule(mass_functions)

    final_item_sets = find_desirable_sets(final_mass_function, 0, 0.5)

    print("\n The songs that we suggest to the users are the following: \n")
    print_song_sets(songs_data, final_item_sets)


if __name__ == "__main__":
    main()
