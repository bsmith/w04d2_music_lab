DROP TABLE IF EXISTS artists CASCADE;
DROP TABLE IF EXISTS albums;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title TEXT,
    genre TEXT,
    artist_id INT REFERENCES artists (id)
);
