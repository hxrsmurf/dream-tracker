# Gets the timestamp. Probably could have used a built-in function but whatever.

from datetime import datetime

def get():
    dt = datetime.now()
    # Set timestamp as 2022-01-10 18:59:00:00
    timestamp = dt.strftime('%Y-%m-%d, %H:%M:%S:%f')

    return timestamp