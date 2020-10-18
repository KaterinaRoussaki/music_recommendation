from DemsterShafer import DempsterShafer as Ds
from collect_data_functions import read_data, return_all_item_set_bpa_dicts
from desirability import return_results
from general_functions import create_input_data, return_results_path


def main():
    song_records = 10000

    create_input_data(song_records)

    likes_data, songs_data = read_data()

    dictionaries = return_all_item_set_bpa_dicts(likes_data, songs_data)

    mass_functions = Ds.mass_functions_from_dictionaries(dictionaries)

    threshold = 0.5
    file_name = "results_rec_" + str(song_records)

    conservation_degree = 0.3
    mc_file_path = return_results_path(file_name + "_0_3.txt", is_monte_carlo=True)
    ds_file_path = return_results_path(file_name + "_0_3.txt", is_monte_carlo=False)
    return_results(
        mc_file_path,
        mass_functions,
        conservation_degree,
        threshold,
        songs_data,
        is_monte_carlo=True,
    )
    return_results(
        ds_file_path,
        mass_functions,
        conservation_degree,
        threshold,
        songs_data,
        is_monte_carlo=False,
    )

    conservation_degree = 0.5
    mc_file_path = return_results_path(file_name + "_0_5.txt", is_monte_carlo=True)
    ds_file_path = return_results_path(file_name + "_0_5.txt", is_monte_carlo=False)
    return_results(
        mc_file_path,
        mass_functions,
        conservation_degree,
        threshold,
        songs_data,
        is_monte_carlo=True,
    )
    return_results(
        ds_file_path,
        mass_functions,
        conservation_degree,
        threshold,
        songs_data,
        is_monte_carlo=False,
    )

    conservation_degree = 0.7
    mc_file_path = return_results_path(file_name + "_0_7.txt", is_monte_carlo=True)
    ds_file_path = return_results_path(file_name + "_0_7.txt", is_monte_carlo=False)
    return_results(
        mc_file_path,
        mass_functions,
        conservation_degree,
        threshold,
        songs_data,
        is_monte_carlo=True,
    )
    return_results(
        ds_file_path,
        mass_functions,
        conservation_degree,
        threshold,
        songs_data,
        is_monte_carlo=False,
    )


if __name__ == "__main__":
    main()
