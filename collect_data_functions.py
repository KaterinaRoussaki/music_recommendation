from general_functions import read_csv, split_string


def read_data():
    """
    Reads the data from the tables likes.csv and songs.csv

    :return likes_data
    :return song_data
    """
    likes_data = read_csv("likes.csv")
    song_data = read_csv("songs.csv")

    return likes_data, song_data


def from_feature_to_item_dictionary(feature_user_dict, feature_item_dict):
    """
    It takes the feature->item dictionary and the feature->bpa dictionary and it
    replaces the features with their related items and returns a item->bpa dictionary

    :param feature_item_dict:
    :param feature_user_dict:
    :return dict
    """

    for feature_set in list(feature_user_dict):
        item_set = set()
        for feature in feature_set:
            if feature == "None":
                continue
            items = feature_item_dict[feature]
            item_set = item_set.union(items)
        feature_user_dict[frozenset(item_set)] = feature_user_dict[feature_set]
        feature_user_dict.pop(feature_set)

    return feature_user_dict


def find_feature_set(user_likes, song_data):
    """
    Takes the likes set of a user and it connects it with the features

    :param song_data:
    :param user_likes:
    :return set
    """
    feature_set = set()

    for row_number in user_likes:
        [multi_feature] = song_data[int(row_number) - 1]
        multi_feature = str(multi_feature).replace(" ", "")
        for feature in split_string(multi_feature, "|"):
            if feature == "None":
                continue
            feature_set.add(feature)

    return feature_set


def find_feature_set_bpa_dictionary(likes_data, feature_data, user_number):
    """
    Takes the likes data, song data and the user number and makes the features->bpa dictionary

    :param user_number:
    :param feature_data:
    :param likes_data:
    :return dict
    """
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


def feature_item_dictionary(features_array):
    """
    Returns a dictionary with the feature as keys and the items that is related as values

    @:param numpy array song_data
    @:param numpy array item_ids_col
    @:param int feature_col
    @:return dict
    """
    feature_item_dict = dict()

    row_num = 0

    for [row] in features_array:
        if row is None:
            continue
        row_num += 1
        features = split_string(row, "|")
        for feature in features:
            feature = feature.replace(" ", "")
            if feature == "None":
                continue
            if feature in feature_item_dict:
                feature_item_dict[feature].add(row_num)
            else:
                feature_item_dict[feature] = {row_num}

    return feature_item_dict


def return_all_item_set_bpa_dicts(likes_data, song_data):
    """
    Returns all the items-bpa dictionaries

    :param song_data:
    :param likes_data:
    :return dict
    """
    user_number = likes_data.shape[0]
    col_song_data = song_data.T.shape[0]

    return_array = []

    for feature_col in range(1, col_song_data):
        feature_user_dict = find_feature_set_bpa_dictionary(
            likes_data, song_data[:, [feature_col]], user_number
        )

        feature_item_dict = feature_item_dictionary(song_data[:, [feature_col]])

        item_bpa_dict = from_feature_to_item_dictionary(
            feature_user_dict, feature_item_dict
        )

        return_array.append(item_bpa_dict)

        del feature_user_dict
        del feature_item_dict
        del item_bpa_dict

    return return_array
