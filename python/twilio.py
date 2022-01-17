# This parses the incoming Twilio message.

def parse(message):
    user = None
    body = None

    for key in message:
        new_split = key.split("=")
        if new_split[0] == 'From':
            # Removes the plus symbol.
            user = new_split[1].split('%2B')[1]

        if new_split[0] == 'Body':
            body = new_split[1].replace("+"," ")

    return user, body