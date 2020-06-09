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
        SELECT ju.user_id, jm.track_id
        FROM jam_to_user as ju
        JOIN jam_to_msd as jm ON jm.jam_id = ju.jam_id;
    """

# USER -> track_id(i)|track_id(i + 1)|...|track_id(i + n)
user_track_id_insert = """
    INSERT INTO user_track
    SELECT us.user_id, REPLACE(us.track_id, song.track_id, song.id) AS row_id
    FROM songs as song
    JOIN user_msd as us ON us.track_id = song.track_id 
    ORDER BY row_id;
"""

likes_insert = """
        INSERT INTO likes
        SELECT user_id, REPLACE(GROUP_CONCAT(DISTINCT row_id),",","|") AS track_id
        FROM user_track
        GROUP BY user_id;
    """
