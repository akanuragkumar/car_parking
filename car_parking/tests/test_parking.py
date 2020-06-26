import requests


def test_add_car_1():
    url = "http://127.0.0.1:8000/slots"

    payload = "{ \"car_number\": \"ka012395\"}"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    assert data['car_number'] == "ka012395"
    assert data['slot'] == '1'


def test_add_car_2():
    url = "http://127.0.0.1:8000/slots"

    payload = "{ \"car_number\": \"ka012399\"}"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    assert data['car_number'] == "ka012399"
    assert data['slot'] == '2'


def test_add_car_3():
    url = "http://127.0.0.1:8000/slots"

    payload = "{ \"car_number\": \"ka012392\"}"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    assert data['car_number'] == "ka012392"
    assert data['slot'] == '3'


def test_add_car_wrong_key():
    url = "http://127.0.0.1:8000/slots"

    payload = "{ \"car_number_1\": \"ka012395\"}"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    assert data['Error'] == "Wrong Key!"


def test_un_park_1():
    url = "http://127.0.0.1:8000/unpark"

    payload = "{ \"slot\": \"2\"}"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    assert data['Success'] == "Car removed!"


def test_un_park_empty_slot():
    url = "http://127.0.0.1:8000/unpark"

    payload = "{ \"slot\": \"2\"}"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    assert data['Error'] == "Slot invalid/Empty!"


def test_get_car_slot():
    url = "http://127.0.0.1:8000/getslots?slot=1"

    response = requests.request("GET", url)
    data = response.json()
    assert data['slot'] == "1"
    assert data['car_number'] == "ka012395"


def test_get_car_car_number():
    url = "http://127.0.0.1:8000/getslots?car_number=ka012395"

    response = requests.request("GET", url)
    data = response.json()
    assert data['slot'] == "1"
    assert data['car_number'] == "ka012395"