from google_images_search import GoogleImagesSearch

# you can provide API key and CX using arguments,
# or you can set environment variables: AIzaSyDPNCd4ApTugJrQa2Pj6Vik8ZV2RS4R4Bo, GCS_CX
gis = GoogleImagesSearch('AIzaSyDPNCd4ApTugJrQa2Pj6Vik8ZV2RS4R4Bo', 'your_project_cx')

# define search params:
_search_params = {
    'q': '장나라',
    'num': 10,
    'safe': 'high|medium|off',
    'fileType': 'jpg|gif|png',
    'imgType': 'clipart|face|lineart|news|photo',
    'imgSize': 'huge|icon|large|medium|small|xlarge|xxlarge',
    'imgDominantColor': 'black|blue|brown|gray|green|pink|purple|teal|white|yellow'
}

# this will only search for images:
gis.search(search_params=_search_params)

# this will search and download:
gis.search(search_params=_search_params, path_to_dir='/path/')

# this will search, download and resize:
gis.search(search_params=_search_params, path_to_dir='/path/', width=500, height=500)

# search first, then download and resize afterwards:
gis.search(search_params=_search_params)
for image in gis.results():
    image.download('/path/')
    image.resize(500, 500)