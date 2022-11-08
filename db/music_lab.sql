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

INSERT INTO "public"."artists"("id","name")
VALUES
(1,E'Artist Alpha'),
(2,E'Artist Beta'),
(3,E'Artist Gamma'),
(4,E'Artist Delta'),
(5,E'Artist Epsilon');

INSERT INTO "public"."albums"("id","title","genre","artist_id")
VALUES
(1,E'Album One',E'G1',1),
(2,E'Album Two',E'G2',1),
(3,E'Album Three',E'G2',3),
(4,E'Album Four',E'G1',4),
(5,E'Album Five',E'G3',5);