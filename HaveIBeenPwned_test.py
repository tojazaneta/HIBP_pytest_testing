import time
import pytest
import requests
import config


@pytest.fixture()
def connect_to_server():
    r = requests.get(config.all_breaches, headers=config.headers)
    return r.status_code


emails = []
@pytest.fixture(scope = 'session')
def emails_finder():
    with open(config.emails_file, "r") as file:
        content = file.read().splitlines()
        for mail in content:
            emails.append(mail)
        time.sleep(2)
        return emails


@pytest.fixture()
def searching_in_the_breaches(emails_finder):
    for mail in emails:
        r = requests.get(config.email_url.format(mail), headers=config.headers)
        http_status = r.status_code
        time.sleep(2)
        return http_status


def test_connect_to_server(connect_to_server):
    time.sleep(2)
    assert connect_to_server == 200

def test_email_finder(emails_finder):
    assert len(emails_finder) > 0
    print(emails)

@pytest.mark.parametrize("email_input, expected_status_code", [
    ("example@gmail.com", 200),
    ("eXAMple@gmail.com", 200),
    ("example@gmail.com, example@gmail.com", 404),
    ("idontlikespamletmebeemptyemail@gmail.com", 404),])

@pytest.mark.skip(reason= " Error 503, can't connect to server.")
def test_email_found_or_not_found(email_input, expected_status_code):
    r = requests.get(config.email_url.format(email_input), headers=config.headers)
    time.sleep(2)
    assert expected_status_code == r.status_code


def test_searching_in_the_breaches(searching_in_the_breaches):
    with pytest.raises(AssertionError) as assert_error:
        assert_error==404
        assert  searching_in_the_breaches == 200

