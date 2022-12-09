import requests

end = "http://127.0.0.1:8000/mangas/create/"

file1 = open("db.sqlite3", "rb")
file2 = open(".gitignore", "rb")

data = {
    "data":
    [
        {
            "name": "naruto",
        },
        {
            "name": "fullmetall",

        },
    ]
}

res = requests.post(
    end,
    data=data,
    files={
        "poster": file1,
        "poster": file2,
    }
)

print(res.json())
