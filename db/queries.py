artist_mbtags_insert = """     
        INSERT INTO artist_mbtags
        SELECT artist_id, REPLACE(GROUP_CONCAT(DISTINCT mbtag),",","|") AS mbtags
        FROM 
        (
            SELECT artist_id, REPLACE(mbtag, " and ", "|") AS mbtag 
            FROM artist_mbtag
        ) AS tag
        GROUP BY artist_id
        ORDER BY artist_id ASC;
    """

user_msd_insert = """
        INSERT INTO user_msd
        SELECT ju.user_id, jm.msd_id as track_id
        FROM user_jam as ju
        JOIN jam_to_msd as jm ON jm.jam_id = ju.jam_id;
    """

user_track_id_insert = """
        INSERT INTO user_track
        SELECT us.user_id, REPLACE(us.track_id, song.track_id, song.id) AS row_id
        FROM track_metadata as song
        JOIN user_msd as us ON us.track_id = song.track_id 
        ORDER BY row_id;
    """

likes_insert = """
        INSERT INTO likes
        SELECT user_id, REPLACE(GROUP_CONCAT(DISTINCT row_id),",","|") AS track_id
        FROM user_track
        GROUP BY user_id;
    """

songs_insert = """
        INSERT INTO songs (track_id, title, artist_name, duration, year, mbtags)
        SELECT tm.id, tm.title, tm.artist_name, tm.duration, tm.year, am.mbtags
        FROM track_metadata as tm
        LEFT JOIN artist_mbtags as am ON tm.artist_id = am.artist_id
    """

songs_update_year = """
        UPDATE songs
        SET year = NULL
        WHERE year=0;
    """
