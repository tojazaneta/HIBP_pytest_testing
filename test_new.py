import requests
import pytest
import time
import json

email_url = "https://haveibeenpwned.com/api/v2/breachedaccount/{}"
email_url_reduced= "https://haveibeenpwned.com/api/v2/breachedaccount/{}?truncateResponse=true"
HEADER = "User-Agent: pytest-api-test-wsb"

response_code = {
    200: "Ok — everything worked and there's a string array of pwned sites for the account",
    400: "Bad request — the account does not comply with an acceptable format (i.e. it's an empty string)",
    403: "Forbidden — no user agent has been specified in the request",
    404: "Not found — the account could not be found and has therefore not been pwned",
    429: "Too many requests — the rate limit has been exceeded"
}

emails_file = "emails.txt"

@pytest.fixture()
def emails_finder():
    global emails
    emails = []
    with open(emails_file, "r") as file:
        content = file.read().splitlines()
        for mail in content:
            emails.append(mail)
        print(content)

@pytest.fixture()
def check_email():
    for email in emails:
        r = requests.get(email_url.format(email), HEADER)
        http_status = r.status_code
        if http_status == 200:
            breaches = r.json()
            print("Oh no.. You have been pwned! The email {} was found in breaches:".format(email))
            for breach in breaches:
                print(breach)
        elif http_status == 404:
            print("Hurray! The email {} was not found in breaches.".format(email))
        else:
            message = response_code.get(http_status, "Error: {}".format(http_status))
            print(message)
        time.sleep(2)


#reduced response body size
@pytest.fixture()
def check_email_reduced():
    for email in emails:
        r = requests.get(email_url_reduced.format(email), HEADER) #zmiana url_email_reduced
        http_status = r.status_code
        if http_status == 200:
            breaches = r.json()
            print("Oh no.. You have been pwned! The email {} was found in breaches:".format(email))
            for breach in breaches:
                print(breach) #["Name"]
        elif http_status == 404:
            print("Hurray! The email {} was not found in breaches.".format(email))
        else:
            message = response_code.get(http_status, "Error: {}".format(http_status))
            print(message)
        time.sleep(2)


def test_email_finder(emails_finder):
    print(emails_finder)

def test_email_in_breaches(check_email):
    print(check_email)

def test_reduced_body_size(check_email_reduced):
    print(check_email_reduced)
