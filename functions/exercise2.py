# def city_country(city, country):
# 	location = f"{city.title()}, {country.title()}"
# 	print(location)

# city_country('santiago', 'chile')

# print('=====')

# def make_album(artist, album, tracks=''):
# 	info = {
# 		'artist': artist,
# 		'album': album,
# 		}
# 	if tracks:
# 		info['tracks'] = tracks

# 	return info

# album = make_album('nirvana', 'smells like teen spirit')
# print(album)

# album2 = make_album('wutang', '36 chambers', 25)
# print(album2)

print('=====')

def make_album(artist, album):
	info = f"{artist} {album}"
	return info.title()

while True:
	print("Tell us the artist and album names: ")
	print("Press 'q' to quit anytime.")

	artist_info = input("Artist name: ")
	if artist_info == 'q':
		break
	album_info = input("Album name: ")
	if album_info == 'q':
		break

	full_info = make_album(artist_info, album_info)
	print(full_info)