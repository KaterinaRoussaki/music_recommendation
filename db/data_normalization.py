import os
import pathlib

from db import connection, sql_queries


"""
    Normalizes the input data and creates the desired music.db in order to export the input for the RS
"""


def data_normalization(data_path, song_number):
    music_db = f"{data_path}music.db"
    track_metadata_db = f"{data_path}track_metadata.db"

    # make the track_metada.csv from the track_metadata.db
    con = connection.Connection(track_metadata_db)
    con.export_table(
        "songs",
        "track_metadata",
        data_path,
        [
            "artist_mbid text",
            "artist_familiarity real",
            "artist_hotttnesss real",
            "track_7digitalid int",
            "shs_perf int",
            "shs_work int",
        ],
        limit=song_number,
        header=True,
    )
    del con

    con = connection.Connection(music_db)

    # add the csv files as tables in the music db
    con.csv_to_table(
        data_path + "/track_metadata.csv", "track_metadata", index_col=True
    )
    con.csv_to_table(data_path + "/likes.tsv", "user_jam", is_csv=False)
    con.csv_to_table(data_path + "/jam_to_msd.tsv", "jam_to_msd", is_csv=False)

    # add intermediate tables in order to make the suitable queries
    con.create_table(
        "songs",
        [
            "track_id int",
            "title text",
            "artist_name text",
            "year int",
            "release text",
            "duration real",
        ],
    )
    con.create_table("user_msd", ["user_id text", "track_id text"])
    con.create_table("user_track", ["user_id text", "row_id text"])
    con.create_table("likes", ["user_id text", "track_id text"])

    # execute the queries
    con.execute_query(sql_queries.user_msd_insert)
    con.execute_query(sql_queries.user_track_id_insert)
    con.execute_query(sql_queries.likes_insert)
    con.execute_query(sql_queries.songs_insert)
    con.execute_query(sql_queries.songs_update_year)

    del con


"""
    Exports the input data (likes.csv and song.csv) for the RS
"""


def project_input_export(dir_path, data_path):
    music_db = f"{data_path}music.db"

    con = connection.Connection(music_db)

    con.export_table("songs", "songs", dir_path.replace("db", "csv"))
    con.drop_table("songs")

    con.export_table("likes", "likes", dir_path.replace("db", "csv"))
    con.drop_table("likes")

    del con


"""
    Cleans the intermediate tables from the music database in order to be tidy for future use
"""


def clean_intermediate_tables(data_path):
    music_db = f"{data_path}music.db"

    con = connection.Connection(music_db)

    con.drop_table("jam_to_msd")
    con.drop_table("user_msd")
    con.drop_table("user_track")
    con.drop_table("user_jam")
    con.drop_table("track_metadata")

    del con


def delete_intermediate_files(data_path):
    os.remove(data_path + "track_metadata.csv")


def delete_music_db(data_path):
    os.remove(data_path + "music.db")


def data_creation(song_number):
    dir_path = pathlib.Path(__file__).parent.absolute().as_posix()
    data_path = dir_path + "/data/"
    data_normalization(data_path, song_number)
    clean_intermediate_tables(data_path)
    project_input_export(dir_path, data_path)
    delete_intermediate_files(data_path)
    delete_music_db(data_path)
