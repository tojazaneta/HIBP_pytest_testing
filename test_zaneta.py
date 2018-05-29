import time
import pytest
import requests
import config

@pytest.fixture()
def connect_to_server():
    r = requests.get(config.all_breaches, headers = config.headers)
    return r.status_code


emails = []
@pytest.fixture()
def emails_finder():
    with open(config.emails_file, "r") as file:
        content = file.read().splitlines()
        for mail in content:
            emails.append(mail)
        time.sleep(2)
        return emails
        # lines = file.readlines()
        # emails = [line.strip() for line in lines]
        # return emails

@pytest.fixture()
def email_check_response(emails_finder):
    for email in emails:
        r = requests.get(config.email_url.format(email), headers = config.headers)
        http_status = r.status_code
        if http_status == 200:
            breaches = r.json()
            return breaches
        elif http_status == 404:
            print("Hurray! The email {} was not found in breaches.".format(email))
        else:
            message = config.response_code.get(http_status, "Error: {}".format(http_status))
            print(message)
        time.sleep(2)

def test_connect_to_server(connect_to_server):
    time.sleep(2)
    assert connect_to_server == 200


@pytest.mark.parametrize("email_input, expected_status_code", [
    ("example@gmail.com", 200), # 200
    ("eXAMple@gmail.com", 200), # 200
    ("example@gmail.com, example@gmail.com", 404), #404
    ("idontlikespamletmebeemptyemail@gmail.com", 404),]) # 404

def test_email_found_or_not_found(email_input, expected_status_code):
    r = requests.get(config.email_url.format(email_input), headers = config.headers)
    time.sleep(2)
    assert expected_status_code == r.status_code

def test_email_finder(emails_finder):
    print(emails)
    assert len(emails_finder) > 0

def test_email_check_response(email_check_response):
    json_file = email_check_response.json()
    breaches_file = json_file['Breaches']
    assert breaches_file[1] == "Title"
