from db.run_sql import run_sql
from models.artist import Artist

SQL_SELECT_ALL = """SELECT * FROM artists"""
SQL_INSERT = """INSERT INTO artists (name) VALUES (%s) RETURNING *"""
SQL_SELECT = """SELECT * FROM artists WHERE id = %s"""
SQL_DELETE = """DELETE FROM artists WHERE id = %s"""
SQL_DELETE_ALL = """DELETE FROM artists"""
SQL_UPDATE = """UPDATE artists SET (name) = (%s) WHERE id = %s"""

def make_artist_from_row(row):
    return Artist(row['name'], row['id'])

# NB omits id!
def make_row_from_artist(artist):
    return [artist.name]

def select_all():
    sql = SQL_SELECT_ALL
    results = run_sql(sql)
    artists = [make_artist_from_row(row) for row in results]
    return artists

def save(artist):
    sql = SQL_INSERT
    values = make_row_from_artist(artist)
    results = run_sql(sql, values)
    artist.id = results[0]['id']
    return artist

def select(id):
    sql = SQL_SELECT
    values = [id]
    results = run_sql(sql, values)
    if results:
        return make_artist_from_row(results[0])
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

def update(artist):
    sql = SQL_UPDATE
    values = make_row_from_artist(artist) + [artist.id]
    run_sql(sql, values, do_fetchall=False)
    return True