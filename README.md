# Music Recommendation System with the use of Dempster Shafer Theory of Evidence

<br/>

### Overview
This is a Music Recommendation System which makes song recommendations for homogenous user groups. We will use the 
Dempster Shafer Theory of Evidence in this project. More specifically we will use the Dempster rule of combination which 
is implemented by a [Monte-Carlo algorithm](https://pypi.org/project/py_dempster_shafer/#description).

<br/>
<br/>

### Requirements

The python version used is the "3.6"

The application uses external libraries which need to be installed in order for the application to be runnable. 
These are the following:

1. [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)
2. [db-sqlite3](https://pypi.org/project/db-sqlite3/)
3. [py-dempster-shafer](https://pypi.org/project/py_dempster_shafer/)
4. [pathlib](https://pypi.org/project/pathlib/)
5. [scipy](https://pypi.org/project/scipy/)

> You can install them by using the `pip`. 
>>Another way is to use the [`pipenv`](https://realpython.com/pipenv-guide/) method so that you can have a pip 
environment only for this project.  

<br/>

### Structure

* `/csv/` : here we can find the  likes.csv and song.csv files that we will use as an input for our program.

> The input files in the csv folder are the likes.csv (contains the user song likes) and the songs.csv (contains the music metadata)

* `/db/data/` : here will be the original data.

* `/db/` : code that have to do with data manipulation, SQLite queries and SQLite database communications.

* `/` : main code, general functions etc.

<br/>
<br/>

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

<br/>
<br/>

### Application 

The application starts from the `main()` which can be found in the main.py. 

<br/>

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

<br/>

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

<br/>

###### Find the Mass Functions

Now that we have the **item_set-bpa dictionaries** we need to find the mass functions of each feature set in 
each dictionary. As you can see in the function 
[`mass_functions_from_dictionaries(dictionary_array)`](https://github.com/KaterinaRoussaki/music_recommendation/blob/e99f72147f7a849b1aacbb4b5c1a53cc721af9d7/DemsterShafer.py#L36)
from the **item_set-bpa dictionaries** array we can return an array with all the mass functions by using the 
function `MassFunction()` of the library [py-dempster-shafer](https://pypi.org/project/py_dempster_shafer/).

<br/>

###### Dempster Rule of Combination

The next step is to combine all the mass functions until only the last remains. We will do this with the Monte Carlo 
implementation of the Dempster rule of combination. Then we can find for each set in the final mass function it's 
plausibility and it's belief according to the 
[Dempster Shafer Theory of Evidence](https://en.wikipedia.org/wiki/Dempster%E2%80%93Shafer_theory).  
All these implementations are made inside the Class 
[`DempsterShafer`](https://github.com/KaterinaRoussaki/music_recommendation/blob/e99f72147f7a849b1aacbb4b5c1a53cc721af9d7/DemsterShafer.py#L25)

* **`ds_combination_rule(mass_function_array)`** : simple implementation of Dempster rule of combination. Needs only 
the final mass function 

* **`def ds_mc_combination_rule(mass_function_array, sample_count=1000, importance_sampling=True, normalization=True)`**
: the implementation of Dempster rule of combination with the Monte-Carlo algorithm. The parameters of the function are:
    * **mass_function_array** the mass function array
    * **sample_count** controls the sampling for the algorithm
    * **importance_sampling** true if we need the sampling
    * **normalization** true if we need the normalization

* **`return_belief(item_dict, mass_function)`** : returns the belief of an item set

* **`return_entire_belief(mass_function)`** : returns the belief of every item set that exist in the mass function

* **`return_plausibility(item_dict, mass_function)`** : returns the plausibility of an item set

* **`return_entire_plausibility(mass_function)`** : returns the plausibility of every item set that exist in the mass function

<br/>

###### Song Set Desirability

The last step is to find the most desirable songs for the user group. Thus with the use of the final mass function we 
will find the desirability of each song set.

> The desirability is defined as following:
>
> ```desirability = (conservation_degree * plausibility + (1 - conservation_degree) * belief') ```


* **`find_desirable_sets(mass_functions, threshold, conservation_degree=0)`** : checks the desirability of all the item sets inside a mass function.
    * **mass_functions** the mass function 
    * **threshold** the threshold for the desirability
    * **conservation_degree** the conservation degree for the desirability definition
    
* **`set_desirability(mass_function, item_set, conservation_degree, threshold=0.5)`**: 
    * **item_set** the item set for which we will find it's desirability
    * **mass_functions** the mass function 
    * **threshold** the threshold for the desirability
    * **conservation_degree** the conservation degree for the desirability definition

