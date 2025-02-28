# We have a list of events and want to check whether a specific date is
# available (i.e., no events planned for that date). However, the
# function always returns the wrong value.

events = {
    "2023-08-13": ["Python debugging exercises"],
    "2023-08-14": ["Read 'Automate the Boring Stuff'"],
    "2023-08-15": ["Webinar: Python for Data Science"],
}

def is_date_available(date):
    if date in events:
        return False

    return True

print(is_date_available("2023-08-14"))  # should return False
print(is_date_available("2023-08-16"))  # should return True
