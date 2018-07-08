all_breaches = 'https://haveibeenpwned.com/api/v2/breaches'
email_url = "https://haveibeenpwned.com/api/v2/breachedaccount/{}"
headers = {'User-Agent ': 'PWNGE-pytest-test', 'From ': 'tojazaneta@github'}
emails_file = "data/emails.txt"
emails= []

response_code = {
    200: "Ok — everything worked and there's a string array of pwned sites for the account",
    400: "Bad request — the account does not comply with an acceptable format (i.e. it's an empty string)",
    403: "Forbidden — no user agent has been specified in the request",
    404: "Not found — the account could not be found and has therefore not been pwned",
    429: "Too many requests — the rate limit has been exceeded"
}
