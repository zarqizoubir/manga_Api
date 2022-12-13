import requests
import json


path = 'data/manga.json'

file = open(path)
json_data = json.load(file)

mangas = json_data["manga"]
chapters = json_data["chapters"]
posters = json_data["posters"]

# To create a Manga We need to pass the data with a POST request
manga_url = "http://127.0.0.1:8000/manga/"

# The data passed as dict and the file( poster ) is passed as bytes

manga_response = requests.post(
    manga_url,
    data=mangas[0],
    files={
        "poster": open(posters[0]["one_piece"], "rb")
    }
)


print(manga_response.json()["id_name"])
# one_piece ======> This key is define The Manga in the database and we neded to get The chapter


print(manga_response.json()["chapters_endpoint"])
# http://127.0.0.1:8000//chapters/one_piece ======> This key is return chapters endpoint

chapter_url = "http://127.0.0.1:8000//chapters/one_piece/"

chapter_response = requests.post(
    chapter_url,
    data={
        "title": chapters[0]["title"]
    },
)

print(chapter_response.json())
# # response ==> {'chapter_parts': [], 'title': 'One Piece Chapter 1'}

chapter_part_url = "http://127.0.0.1:8000//chapters/one_piece/1/"

chapter_parts = chapters[0]["Chapter parts"]

for i in range(len(chapter_parts)):
    chapter_p_response = requests.post(
        chapter_part_url,
        data={
            "title": chapter_parts[i]["title"]
        },
        files={
            "image": open(chapter_parts[i]["image"], "rb")
        }
    )
    print(chapter_p_response.json())

# The response is :
    # {'title': '1', 'image': 'http://127.0.0.1:8000/storage/chapters/2022/12/13/1.png'}
    # {'title': '2', 'image': 'http://127.0.0.1:8000/storage/chapters/2022/12/13/2.png'}
    # {'title': '3', 'image': 'http://127.0.0.1:8000/storage/chapters/2022/12/13/3.png'}
