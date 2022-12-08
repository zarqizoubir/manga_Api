import requests

files = {
    "poster": open("1.jpg", "rb")
}

values = {
    "title": "sq",
    "description": "Somrhringi",
    "rating": 3
}
response = requests.post(
    "http://127.0.0.1:8000/manga/",
    json=values,
    files=files
)

print(response.text)
