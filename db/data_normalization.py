import pathlib

import connection as connection

import queries


def data_normalization():
    dir_path = pathlib.Path(__file__).parent.absolute().as_posix()
    data_path = dir_path + "/data/"

    music_db = f"{data_path}music.db"
    artist_db = f"{data_path}artist_term.db"
    track_metadata_db = f"{data_path}track_metadata.db"

    # make the track_metada.csv from the track_metadata.db
    con = connection.Connection(track_metadata_db)
    con.export_table(
        "songs",
        "track_metadata",
        data_path,
        [
            "release text",
            "artist_mbid text",
            "artist_familiarity real",
            "artist_hotttnesss real",
            "track_7digitalid int",
            "shs_perf int",
            "shs_work int",
        ],
        header=True,
    )
    del con

    # make the artist_mbtags.csv from the artist_mbtags.db
    con = connection.Connection(artist_db)
    con.export_table("artist_mbtag", "artist_mbtag", data_path, header=True)
    del con

    # open the connection with the main db
    con = connection.Connection(music_db)

    # add the csv files as tables in the music db
    con.csv_to_table(data_path + "/artist_mbtag.csv", "artist_mbtag")
    con.csv_to_table(
        data_path + "/track_metadata.csv", "track_metadata", index_col=True
    )
    con.csv_to_table(data_path + "/likes.tsv", "user_jam", is_csv=False)
    con.csv_to_table(data_path + "/jam_to_msd.tsv", "jam_to_msd", is_csv=False)

    # make useful tables
    con.create_table("artist_mbtags", ["artist_id text", "mbtags text"])
    con.create_table("user_msd", ["user_id text", "track_id text"])
    con.create_table("user_track", ["user_id text", "row_id text"])
    con.create_table("likes", ["user_id text", "track_id text"])
    con.create_table(
        "songs",
        [
            "track_id int",
            "title text",
            "artist_name text",
            "duration real",
            "year int",
            "mbtags text",
        ],
    )

    # execute the
    con.execute_query(queries.artist_mbtags_insert)
    con.execute_query(queries.user_msd_insert)
    con.execute_query(queries.user_track_id_insert)
    con.execute_query(queries.likes_insert)
    con.execute_query(queries.songs_insert)
    con.execute_query(queries.songs_update_year)

    del con


def clean_music_db():
    dir_path = pathlib.Path(__file__).parent.absolute().as_posix()
    data_path = dir_path + "/data/"

    music_db = f"{data_path}music.db"
    con = connection.Connection(music_db)

    con.drop_table("artist_mbtag")
    con.drop_table("artist_mbtags")
    con.drop_table("jam_to_msd")
    con.drop_table("user_msd")
    con.drop_table("user_track")
    con.drop_table("user_jam")
    con.drop_table("track_metadata")

    del con


if __name__ == "__main__":
    # data_normalization()
    clean_music_db()
