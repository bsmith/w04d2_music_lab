from db.run_sql import run_sql
from models.album import Album

import repositories.artist_repository as artist_repository

SQL_SELECT_ALL = """SELECT title, genre, artist_id, id FROM albums"""
SQL_INSERT = """INSERT INTO albums (title, genre, artist_id)
    VALUES (%s, %s, %s) RETURNING *"""
SQL_SELECT = """SELECT title, genre, artist_id, id FROM albums WHERE id = %s"""
SQL_DELETE = """DELETE FROM albums WHERE id = %s"""
SQL_DELETE_ALL = """DELETE FROM albums"""
SQL_UPDATE = """UPDATE albums SET (title, genre, artist_id) =
    (%s, %s, %s) WHERE id = %s"""

def make_album_from_row(row):
    # print('row:', row)
    artist = artist_repository.select(row['artist_id'])
    return Album(row['title'], row['genre'], artist, row['id'])

# NB omits id!
def make_row_from_album(album):
    return [album.title, album.genre, album.artist.id]

def select_all():
    sql = SQL_SELECT_ALL
    results = run_sql(sql)
    albums = [make_album_from_row(row) for row in results]
    return albums

def save(album):
    sql = SQL_INSERT
    values = make_row_from_album(album)
    results = run_sql(sql, values)
    album.id = results[0]['id']
    return album

def select(id):
    sql = SQL_SELECT
    values = [id]
    results = run_sql(sql, values)
    if results:
        return make_album_from_row(results[0])
    return None

# XXX check cursor.rowcount to see if we did DELETE/UPDATE something?
def delete(id):
    sql = SQL_DELETE
    values = [id]
    run_sql(sql, values, do_fetchall=False)
    return True

def delete_all():
    sql = SQL_DELETE_ALL
    run_sql(sql, do_fetchall=False)
    return True

def update(album):
    sql = SQL_UPDATE
    values = make_row_from_album(album) + [album.id]
    run_sql(sql, values, do_fetchall=False)
    return True