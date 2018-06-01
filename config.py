all_breaches = 'https://haveibeenpwned.com/api/v2/breaches'
email_url = "https://haveibeenpwned.com/api/v2/breachedaccount/{}"
email_url_reduced= "https://haveibeenpwned.com/api/v2/breachedaccount/{}?truncateResponse=true"
headers = {'User-Agent ': 'PWNGE-pytest-study-wsb', 'From ': 'zaneta.stanczak@gmail.com'}
emails_pwned_file = "emails_pwned.txt"
emails_clean_file = "emails_clean.txt"
emails_file = "emails.txt"
emails= []

response_code = {
    200: "Ok — everything worked and there's a string array of pwned sites for the account",
    400: "Bad request — the account does not comply with an acceptable format (i.e. it's an empty string)",
    403: "Forbidden — no user agent has been specified in the request",
    404: "Not found — the account could not be found and has therefore not been pwned",
    429: "Too many requests — the rate limit has been exceeded"
}
