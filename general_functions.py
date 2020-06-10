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
    data = pd.read_csv(folder_path + file_path, sep=", ", engine="python", header=None)
    return data.values


"""
Takes a string and it splits it

@:param str file_path
@:param str file_path

@:return 
"""


def split_string(string, separator):
    return string.split(separator)


"""
If the program data does not exist make it from the scratch

@:param str file_path
@:param str file_path

@:return 
"""


def check_input_data():
    csv_path = pathlib.Path(__file__).parent.absolute().as_posix() + "/csv/"

    likes_path = csv_path + "likes.csv"
    songs_path = csv_path + "songs.csv"

    if os.path.exists(likes_path) is False and os.path.exists(songs_path) is False:
        data_creation()
