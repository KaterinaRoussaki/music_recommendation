# Music Recommendation System with the use of Dempster Shafer Theory of Evidence

### Overview
This is a Music Recommendation System which makes song recommendations for homogenous user groups.

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

> All the above data must be containd inside the "/db/data" folder of the model.


### Structure

* **/csv/** : here we can find the  likes.csv and song.csv files that we will use as an input for our program.

* **/db/data/** : here will be the original data.

* **/db/** : code that have to do with data manipulation, SQLite queries and SQLite database communications.

* **/** : main code, general functions etc.

### 