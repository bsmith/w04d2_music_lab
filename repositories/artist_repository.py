from db.run_sql import run_sql
from models.artist import Artist

def make_artist_from_row(row):
    return Artist(row['name'], row['id'])

def select_all():
    sql = """SELECT * FROM artists"""
    results = run_sql(sql)
    artists = [make_artist_from_row(row) for row in results]
    return artists

def save(artist):
    sql = """INSERT INTO artists (name) VALUES (%s) RETURNING *"""
    values = [artist.name]
    results = run_sql(sql, values)
    artist.id = results[0]['id']
    return artist

def select(id):
    sql = """SELECT * FROM artists WHERE id = %s"""
    values = [id]
    results = run_sql(sql, values)
    if results:
        return make_artist_from_row(results[0])
    return None

# XXX check cursor.rowcount to see if we did DELETE/UPDATE something?
def delete(id):
    sql = """DELETE FROM artists WHERE id = %s"""
    values = [id]
    run_sql(sql, values, do_fetchall=False)
    return True

def delete_all():
    sql = """DELETE FROM artists"""
    run_sql(sql, do_fetchall=False)
    return True

def update(artist):
    sql = """UPDATE artists SET (name) = (%s)
        WHERE id = %s"""
    values = [artist.name, artist.id]
    run_sql(sql, values, do_fetchall=False)
    return True