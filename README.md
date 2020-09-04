# Music Recommendation System with the use of Dempster Shafer Theory of Evidence

### Overview
This is a Music Recommendation System which makes song recommendations for homogenous user groups. We will use the 
Dempster Shafer Theory of Evidence in this project. More specifically we will use the Dempster rule of combination which 
is implemented by a [Monte-Carlo algorithm](https://pypi.org/project/py_dempster_shafer/#description).

### Requirements

The python version used is the "3.6"

The application uses external libraries which need to be installed in order for the application to be runnable. 
These are the following:

1. [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)
2. [db-sqlite3](https://pypi.org/project/db-sqlite3/)
3. [py-dempster-shafer](https://pypi.org/project/py_dempster_shafer/)
4. [pathlib](https://pypi.org/project/pathlib/)
5. [scipy](https://pypi.org/project/scipy/)

> You can install them by using the `pip`. Another way is to use the [`pipenv`](https://realpython.com/pipenv-guide/) method so that you can have a pip 
environment only for this project.  


### Structure

* `/csv/` : here we can find the  likes.csv and song.csv files that we will use as an input for our program.

> The input files in the csv folder are the likes.csv (contains the user song likes) and the songs.csv (contains the music metadata)

* `/db/data/` : here will be the original data.

* `/db/` : code that have to do with data manipulation, SQLite queries and SQLite database communications.

* `/` : main code, general functions etc.

### Input Data

The song data that we will use for our Music Recommendation System can be found
at the [Million Song Dataset](http://millionsongdataset.com/) and at the [Thisismyjam](https://www.thisismyjam.com/).

In the following list we show all the data and where to find them:
1. [track_metadata.db](http://millionsongdataset.com/sites/default/files/AdditionalFiles/track_metadata.db): 
this is an SQLite database which contains most of the metadata of a song.
2. [likes.tsv](https://archive.org/details/thisismyjam-datadump): 
contains the user jam(song) choices. 
3. [jam_to_msd.tsv](http://millionsongdataset.com/sites/default/files/thisismyjam/jam_to_msd.tsv): 
contains the connection between the jams and the tracks of the track_metadata.db.

> (if we follow the link for the likes.tsv we must download 
> the folder with all the jam data but we will only keep the likes.tsv file)

> All the above data must be contained inside the "/db/data" folder of the model.

### Application 

##### Main

The application starts from the `main()` which can be found in the main.py. 

---

###### Input 
The function 
[`create_input_data(song_number, clean_old_files=False)`](https://github.com/KaterinaRoussaki/music_recommendation/blob/c482b5b76aee7976b9fad3d957fb6a9bc878d0ab/general_functions.py#L42) 
is used to begin constructing the  input data.

* The `song_number` denotes the number of the records that the file songs.csv will have.

* If the parameter `clean_old_files` is `True` will clean the likes.csv and song.csv from the csv folder, by default 
it is False.

After the construction of the two files we need to read them and store them as two `numpy` arrays. The function 
[`read_data()`](https://github.com/KaterinaRoussaki/music_recommendation/blob/c482b5b76aee7976b9fad3d957fb6a9bc878d0ab/collect_data_functions.py#L12) 
will be used for this task.

---

###### Basic probability assignments

After the construction of the input files we need to construct dictionaries for each feature which will contain 
as keys the items_sets(songs) and values their bpa. We need only those whose bpa is greater than 0. To achieve 
this we will use the function `return_all_item_set_bpa_dicts(likes_data, song_data)` which is constructed by 
the following steps:

1. For each feature type (title, artist, etc.) find all the feature sets that have bpa > 0. Then store them in 
dictionaries (`key-> "feature_set", value->"bpa"`). 
We use the 
[`find_feature_set_bpa_dictionary(likes_data, feature_data, user_number)`](https://github.com/KaterinaRoussaki/music_recommendation/blob/c482b5b76aee7976b9fad3d957fb6a9bc878d0ab/collect_data_functions.py#L77)
    * **likes_data** are the data with the user song likes
    * **feature_data** is a feature column (titles, etc.)
    * **user_number** the number of all the users 

2. For each feature type (title, artist, etc.) make a dictionary that connects each feature with the all the song (ids) 
that contain it. This step is implemnted by the function 
[`feature_item_dictionary(features_array)`](https://github.com/KaterinaRoussaki/music_recommendation/blob/c482b5b76aee7976b9fad3d957fb6a9bc878d0ab/collect_data_functions.py#L103). 
It only the feature column each time.

3.  For each feature type (title, artist, etc.) replace in the feature_set-bpa dictionary the feature sets with the  
corresponding item sets. Thus we will use the function 
[`from_feature_to_item_dictionary(feature_user_dict, feature_item_dict)`](https://github.com/KaterinaRoussaki/music_recommendation/blob/c482b5b76aee7976b9fad3d957fb6a9bc878d0ab/collect_data_functions.py#L29)
    * **feature_user_dict** the feature_set-bpa

4. Return an array with all the **item_set-bpa dictionaries**.

---

###### Find the Mass Functions

###### Dempster Rule of Combination

###### Song Set Desirability