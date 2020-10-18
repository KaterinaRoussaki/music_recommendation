import os
import pathlib

import pandas as pd

from db.data_normalization import data_creation


def return_results_path(file_name, is_monte_carlo=True):
    """
    Return the path of the results file

    :return:
    """
    folder_path = pathlib.Path(__file__).parent.absolute().as_posix() + "/results/"
    if is_monte_carlo:
        folder_path += "/mc/"
    else:
        folder_path += "/ds/"
    file_path = folder_path + file_name
    return file_path


def read_csv(file_path):
    """
    Read a csv file and returns it's content as an array

    :param file_path:
    :return:
    """
    folder_path = pathlib.Path(__file__).parent.absolute().as_posix() + "/csv/"
    data = pd.read_csv(folder_path + file_path, sep=",", engine="python", header=None)
    return data.values


def split_string(string, separator):
    """
    Takes a string and it splits it

    :param string:
    :param separator:
    :return:
    """
    return str(string).split(separator)


def create_input_data(song_number, clean_old_files=False):
    """
    If the program data does not exist make it from the scratch

    :param song_number:
    :param clean_old_files:
    :return:
    """
    csv_path = pathlib.Path(__file__).parent.absolute().as_posix() + "/csv/"

    likes_path = csv_path + "likes.csv"
    songs_path = csv_path + "songs.csv"

    if clean_old_files is True:
        if os.path.exists(likes_path) is True:
            os.remove(likes_path)
        if os.path.exists(songs_path) is True:
            os.remove(songs_path)
        data_creation(song_number)
    else:
        if os.path.exists(likes_path) is False or os.path.exists(songs_path) is False:
            data_creation(song_number)


class PrintOptions:
    """
    Printing options
    """

    BLUE = "\033[94m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"


def bold_print(string):
    """
    Print a bold string

    :param string:
    """
    print(PrintOptions.BOLD, string)


def print_dict(dictionary):
    """
    Prints a dictionary

    :param dictionary:
    :return:
    """
    for key in dictionary:
        print(key, " ", dictionary[key])


def print_song(song_data, song_id, console=False):
    """
    Finds a song from its id and then it prints all its metadata

    :param console:
    :param song_data:
    :param song_id:
    :return:
    """

    [track_id, title, artist_name, year, release, duration] = song_data[song_id]

    if console:
        title = str(title).replace("  ", " ")
        artist_name = str(artist_name).replace("  ", " ")
        release = str(release).replace("  ", " ")
        print(
            PrintOptions.BLUE,
            track_id,
            PrintOptions.ENDC,
            ",",
            title,
            ",",
            artist_name,
            ",",
            year,
            ",",
            release,
            ",",
            duration,
        )
    else:
        song = (
            str(track_id)
            + ","
            + str(title)
            + ","
            + str(artist_name)
            + ","
            + str(year)
            + ","
            + str(release)
            + ","
            + str(duration)
        )
        return song

    return ""


def print_song_sets(song_data, song_sets, console=False):
    """
    Prints a set of songs with their metadata

    :param console:
    :param song_data:
    :param song_sets:
    :return:
    """

    songs = ""

    for song in song_sets:
        songs += print_song(song_data, song, console)

    return songs


def print_to_file(file_name, string):
    """
    Prints a  string to a file

    :param file_name:
    :param string:
    :return:
    """
    f = open(file_name, "w")
    f.write(string)
    f.close()
