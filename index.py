import requests

end = "http://127.0.0.1:8000/token/"


data = {
    "username": "someone",
    "password": "",
}

res = requests.post(
    end,
    data=data
)

print(res.json())
