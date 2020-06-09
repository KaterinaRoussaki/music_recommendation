from general_functions import read_csv, split_string


"""
It takes the feature->item dictionary and the feature->bpa dictionary and it replaces the features with their related 
items and returns a item->bpa dictionary

@:param dict feature_user_dict
@:param dict feature_item_dict

@:return dict 
"""


def from_feature_to_item_dictionary(feature_user_dict, feature_item_dict):
    dictionary = dict()

    for feature_set in feature_user_dict:
        dictionary[
            connect_feature_set_with_item_set(feature_set, feature_item_dict)
        ] = feature_user_dict[feature_set]

    return dictionary


"""
Takes a feature_set and it returns the item_set that is related

@:param set feature_set
@:param dict feature_item_dict

@:return set 
"""


def connect_feature_set_with_item_set(feature_set, feature_item_dict):
    item_set = frozenset()

    for feature in feature_set:
        item_set = item_set.union(feature_item_dict[feature])

    return item_set


"""
Takes the likes set of a user and it connects it with the features

@:param set likes
@:param numpy array song_data

@:return set 
"""


def find_feature_set(user_likes, song_data):
    feature_set = set()

    for row_number in user_likes:
        [multi_feature] = song_data[int(row_number) - 1]
        for feature in split_string(multi_feature, "|"):
            feature_set.add(feature)

    return feature_set


"""
Takes the likes data, song data and the user number and makes the features->bpa dictionary

@:param numpy array likes_data
@:param numpy array song_data
@:param int user_number

@:return dict 
"""


def find_feature_set_bpa_dictionary(likes_data, feature_data, user_number):
    feature_dict = dict()

    for row in likes_data:
        user_likes = split_string(row[1], "|")
        feature_set = frozenset(find_feature_set(user_likes, feature_data))
        if feature_set in feature_dict:
            feature_dict[feature_set] += 1
        else:
            feature_dict[feature_set] = 1

    for key in feature_dict:
        feature_dict[key] /= user_number
    return feature_dict


"""
Returns a dictionary with the feature as keys and the items that is related as values

@:param numpy array song_data
@:param numpy array item_ids_col
@:param int feature_col

@:return dict 
"""


def feature_item_dictionary(song_data, item_ids_col, feature_col):
    feature_item_dict = dict()

    for song in song_data:
        if song[feature_col] in feature_item_dict:
            item_set = feature_item_dict[song[feature_col]]
            feature_item_dict[song[feature_col]] = item_set.union(
                frozenset({str(song[item_ids_col])})
            )
        else:
            feature_item_dict[str(song[feature_col])] = frozenset(
                str(song[item_ids_col])
            )

    return feature_item_dict


"""
Returns all the items-bpa dictionaries

@:param numpy array song_data
@:param numpy array item_ids_col
@:param int feature_col

@:return dict 
"""


def return_all_item_set_bpa_dicts():
    likes_data = read_csv("likes.tsv")
    song_data = read_csv("songs.csv")

    user_number = likes_data.shape[0]
    col_song_data = song_data.T.shape[0]
    item_ids_col_number = col_song_data - 1

    return_array = []

    for feature_col in range(item_ids_col_number):
        feature_user_dict = find_feature_set_bpa_dictionary(
            likes_data, song_data[:, [feature_col]], user_number
        )
        feature_item_dict = feature_item_dictionary(
            song_data, item_ids_col_number, feature_col
        )
        item_bpa_dictionary = from_feature_to_item_dictionary(
            feature_user_dict, feature_item_dict
        )
        return_array.append(item_bpa_dictionary)

    return return_array
