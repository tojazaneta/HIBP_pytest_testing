import time
import config
import requests
import pytest
from sys import argv

#zlini komend odpalamy test: python script.py param1 param2

email_file = argv[1], argv[2]

@pytest.fixture(scope="module")
def emails_finder():
    with open(email_file) as file:
        lines = file.readlines()
        l = [line.strip() for line in lines]
        return l

@pytest.fixture()
def searching_in_the_breaches(emails_finder):
    for mail in email_file:
        r = requests.get(config.email_url.format(mail), headers = config.headers)
        http_status = r.status_code
        time.sleep(2)
        return http_status

@pytest.fixture()
def emails_clean_file_finder(emails_finder):
    email_file = config.emails_clean_file
    return email_file

@pytest.fixture()
def emails_pwned_for_sure(emails_finder):
    email_file = config.emails_pwned_file
    return email_file

def test_email_finder(emails_finder):
    assert len(emails_finder) > 0


#TC01 Email found in the list of breaches
def test_email_found_in_the_breaches(searching_in_the_breaches):
    # config.emails = config.emails_pwned_file
    time.sleep(2)
    assert searching_in_the_breaches == 200


def test_email_not_found_for_sure(searching_in_the_breaches):
    # config.emails = config.emails_clean_file
    time.sleep(2)
    assert searching_in_the_breaches == 404

@pytest.mark.parametrize("email_input, expected_status_code", [
    ("example@gmail.com", 200),
    ("eXAMple@gmail.com", 200),
    ("example@gmail.com, example@gmail.com", 404),
    ("idontlikespamletmebeemptyemail@gmail.com", 404),
    ("IdontLikeSpamLetMeBeEmptyEmail@gmail.com", 400),
    ])

def test_email_found_or_not_found(email_input, expected_status_code):
    r = requests.get(config.email_url.format(email_input), headers = config.headers)
    time.sleep(2)
    assert expected_status_code == r.status_code



