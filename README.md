# Music Recommendation System with the use of Dempster Shafer Theory of Evidence

### Overview
This is a Music Recommendation System which makes song recommendations for homogenous user groups. We will use the 
Dempster Shafer Theory of Evidence in this project. More specifically we will use the Dempster rule of combination which 
is implemented by a [Monte-Carlo algorithm](https://pypi.org/project/py_dempster_shafer/#description).

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

###### Input 
The function `create_input_data(song_number, clean_old_files=False)` is used to begin constructing the  input data.
* The `song_number` denotes the number of the records that the file songs.csv will have.
* iF the parameter `clean_old_files` is `True` will clean the likes.csv and song.csv from the csv folder, by default 
it is False.

After the construction of the two files we need to read them and store them as two `numpy` arrays. The function 
`read_data()` will be used for this task.

###### Basic probability assignments

After the construction of the input files we need to construct dictionaries for each feature which will contains 
as keys items_sets(songs) with bpa assignment greater than 0 and values their bpa. To achieve this we need to continue 
with the following steps:

1. For each dictionary we need to  

###### Find the Mass Functions

###### Dempster Rule of Combination

###### Song Set Desirability