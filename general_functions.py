import os
import pathlib

import pandas as pd

from db.data_normalization import data_creation

"""
    Read a csv file and returns it's content as an array
    
    @:param str file_path
    @:return numpy array
"""


def read_csv(file_path):
    folder_path = pathlib.Path(__file__).parent.absolute().as_posix() + "/csv/"
    data = pd.read_csv(folder_path + file_path, sep=",", engine="python", header=None)
    return data.values


"""
    Takes a string and it splits it
    
    @:param str file_path
    @:param str file_path
"""


def split_string(string, separator):
    return str(string).split(separator)


"""
    If the program data does not exist make it from the scratch
    
    @:param str file_path
    @:param str file_path
"""


def create_input_data(song_number, clean_old_files=False):
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


"""
    Printing options
"""


class print_options:
    BLUE = "\033[94m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"


"""
    Print a bold string
"""


def bold_print(string):
    print(print_options.BOLD, string)


"""
    Prints a dictionary

    @:param  dictionary
"""


def print_dict(dictionary):
    for key in dictionary:
        print(key, " ", dictionary[key])


"""
    Finds a song from its id and then it prints all its metadata
    
    @:param  song_metadata
    @:param  song_id 
"""


def print_song(song_data, song_id):
    [track_id, title, artist_name, year, release, duration] = song_data[song_id]
    title = str(title).replace("  ", " ")
    artist_name = str(artist_name).replace("  ", " ")
    release = str(release).replace("  ", " ")
    print(
        print_options.BLUE,
        track_id,
        print_options.ENDC,
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


"""
    Prints a set of songs with their metadata
    
    @:param  song_metadata
    @:param  song_sets 
"""


def print_song_sets(song_data, song_sets):
    for song in song_sets:
        print_song(song_data, song)
