import pathlib

import connection as connection

# from .queries import (
#     artist_mbtags_insert,
#     likes_insert,
#     user_msd_insert,
#     user_track_id_insert,
# )


def data_normalization():
    dir_path = pathlib.Path(__file__).parent.absolute().as_posix()

    csv_path = dir_path.replace("db", "csv") + "/"
    db_data_path =  dir_path + "/data/"

    music_db = f"{dir_path}/metadata/music.db"
    artist_db = f"{dir_path}/metadata/artist_term.db"
    track_metadata_db = f"{dir_path}/metadata/track_metadata.db"

    # make the track_metada.csv from the track_metadata.db
    # con = connection.Connection(track_metadata_db)
    # con.export_table(
    #     "songs",
    #     "track_metadata",
    #     dir_path.replace("db", "csv"),
    #     [
    #         "release text",
    #         "artist_mbid text",
    #         "artist_familiarity real",
    #         "artist_hotttnesss real",
    #         "track_7digitalid int",
    #         "shs_perf int",
    #         "shs_work int",
    #     ],
    #     header=True,
    # )
    # del con

    # make the artist_mbtags.csv from the artist_mbtags.db
    # con = connection.Connection(artist_db)
    # con.export_table(
    #     "artist_mbtag", "artist_mbtag", dir_path.replace("db", "csv"), header=True
    # )
    # del con

    # add the csv files as tables in the music db
    con = connection.Connection(music_db)

    # csv_path = track_metadata_db.replace("db", "csv")
    # csv_path = csv_path.replace("/data", "")
    # con.csv_to_table(csv_path, "songs")

    # file_path = csv_path + "artist_mbtag.csv"
    # con.csv_to_table(file_path, "artist_mbtag")

    file_path = csv_path + "likes.tsv"
    con.csv_to_table(file_path, "user_track", is_csv=False)

    file_path = csv_path + "jam_to_msd.tsv"
    con.csv_to_table(file_path, "user_msd", is_csv=False)

    # execute queries to manipulate the data form in order to make the desired input data
    # con.create_table("artist_mbtags", ["artist_id TEXT", "mbtags TEXT"])
    # con.create_table("user_msd", ["user_id TEXT", "track_id TEXT"])
    # con.create_table("user_track", ["user_id TEXT", "row_id TEXT"])
    # con.create_table("likes", ["user_id TEXT", "row_id TEXT"])

    del con


if __name__ == "__main__":
    data_normalization()
