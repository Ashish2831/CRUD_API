import requests
import json

URL = "http://127.0.0.1:8000/students/"


def getData(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    res = requests.get(url=URL, data=json_data)
    print(res.json())


def postData():
    data = {'name': 'Pranav', 'rollNo': '55', 'city': 'Pune', 'age': '16'}
    json_data = json.dumps(data)

    res = requests.post(url=URL, data=json_data)
    print(res.json())


def updateData():
    data = {'id': 5, 'name': 'Abhishek',
            'rollNo': '55'}
    json_data = json.dumps(data)

    res = requests.put(url=URL, data=json_data)
    print(res.json())

def deleteData():
    data = {'id': 5}
    json_data = json.dumps(data)

    res = requests.delete(url=URL, data=json_data)
    print(res.json())


if __name__ == '__main__':
    getData(1)
    # postData()
    # updateData()
    # deleteData()
    