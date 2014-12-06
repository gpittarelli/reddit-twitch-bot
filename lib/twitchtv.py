#!/usr/bin/env python
'''
Define functions to query the twitch.tv streaming
websites.

More info on the Twitch.tv REST api here:
  https://github.com/justintv/twitch-api
'''

import sys
import logging
import requests

'''
Twitch.tv API stream listing request.  This API call takes a comma
separated list of channel names and returns an array of JSON objects,
one per channel that is currently streaming (so nothing is returned
for channels that were queried but aren't streaming)
'''

STREAM_URL = "https://api.twitch.tv/kraken/streams?channel=%s"


# Takes an array of channel names and returns the names from the array
# which are currently streaming
def fetch_streams(channel_names):
    response = requests.get(STREAM_URL % (",".join(channel_names)))

    try:
        message = response.json()["streams"]
    except ValueError:
        # JSON Decode failed
        sys.exit("Invalid message from twitch.tv: %s" % (response.text))

    if not isinstance(message, list):
        sys.exit("Unexpected JSON from twitch.tv: %s" % (message))

    return message
