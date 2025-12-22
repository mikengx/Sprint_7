class Users:
    data_current = {
        "login": "samokatuser2025",
        "password": "qwerty%1234*456"
    }
    data_negative = {
        "login": "nonexistingsamokater2025",
        "password": "qwertyuiop"
    }
    data_without_login = {
        "login": "",
        "password": "asdfghjkl"
    }
    data_without_password = {
        "login": "anyuserwithoutpassword2025",
        "password": ""
    }


class Orders:
    data_order = {
        "firstName": "TesterOrder",
        "lastName": "TesterSurname",
        "address": "NSK, Lenina street 777",
        "metroStation": 3,
        "phone": "+7 999 666 55 44",
        "rentTime": 7,
        "deliveryDate": "2025-12-31",
        "comment": "Please Call Before Delivery",
        "color": [
            "BLACK"
        ]
    }
