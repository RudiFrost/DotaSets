import requests

OK = 200


def test_index():
    r = requests.get('http://127.0.0.1:5000/')
    if r.status_code == OK:
        return "TEST ASSERTED"


def test_about():
    r = requests.get('http://127.0.0.1:5000/about')
    if r.status_code == OK:
        return "TEST ASSERTED"


def test_login():
    r = requests.get('http://127.0.0.1:5000/login')
    if r.status_code == OK:
        return "TEST ASSERTED"


def test_register():
    r = requests.get('http://127.0.0.1:5000/register')
    if r.status_code == OK:
        return "TEST ASSERTED"


def test_abaddon():
    r = requests.get('http://127.0.0.1:5000/abaddon')
    if r.status_code == OK:
        return "TEST ASSERTED"


def test_apparation():
    r = requests.get('http://127.0.0.1:5000/ancient_apparation')
    if r.status_code == OK:
        return "TEST ASSERTED"


def test_batrider():
    r = requests.get('http://127.0.0.1:5000/batrider')
    if r.status_code == OK:
        return "TEST ASSERTED"


def test_beastmaster():
    r = requests.get('http://127.0.0.1:5000/beastmaster')
    if r.status_code == OK:
        return "TEST ASSERTED"


def test_bloodseeker():
    r = requests.get('http://127.0.0.1:5000/bloodseeker')
    if r.status_code == OK:
        return "TEST ASSERTED"


def test_bounty():
    r = requests.get('http://127.0.0.1:5000/bounty_hunter')
    if r.status_code == OK:
        return "TEST ASSERTED"
