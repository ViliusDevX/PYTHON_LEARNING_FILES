import time

info = {
    "days": 365,
    "cig_averages": {
        "weekday": 4,
        "saturday": 20,
        "sunday": 1
    },
    "pack_price": 4.50,
    "cigs_in_pack": 20,
    "minuters_per_cig": 5
}

readable = time.ctime()
print(readable)