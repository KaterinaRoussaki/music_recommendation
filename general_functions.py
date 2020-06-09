import pathlib

import pandas as pd


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
