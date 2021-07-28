def make_album(artist, album, none=''):
	"""Return artist name and album title"""
	if none:
		info_album = {'artist name': artist, 'album title': album, 'songs from album': none}
	else:
		info_album={'artist name': artist, 'album title': album}
	return info_album

while True:
	print("\nPlease enter the artist name:")
	print("Please enter the album title:")

	artist_name = input('Artist name: ')
	if artist_name == 'q':
		break
	album_title = input("Album name: ")
	if album_title == 'q':
		break

	album_made = make_album(artist_name, album_title)
	print(f"\n {album_made}")


