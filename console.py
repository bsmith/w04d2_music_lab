import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository
from models.artist import Artist
from models.album import Album

print(artist_repository.select_all())
print(album_repository.select_all())

artist = Artist('Arty the Artist')
artist_repository.save(artist)
print(artist)
print(artist_repository.select(artist.id))
artist_repository.delete(artist.id)

# `python3 -i console.py` has better tab completion!
#import pdb
#pdb.set_trace()