#!/usr/bin/env python
'''
Define functions to query the twitch.tv and justin.tv streaming
websites.

More info on the Justin.TV REST api here:
  http://apiwiki.justin.tv/mediawiki/index.php/REST_API_Documentation
'''
import logging
import requests

'''
Justin.TV API stream listing request.  This API call takes a comma
separated list of channel names and returns an array of JSON objects,
one per channel that is currently streaming (so nothing is returned
for channels that were queried but aren't streaming)

   [{"login":"esltv_dota", ... many more properties ... }, ...]
'''
JUSTIN_STREAM_URL = "https://api.justin.tv/api/stream/list.json?channel=%s"

# Takes an array of channel names and returns the names from the array
# which are currently streaming
def justin_fetch_channels(channel_names):
    response = requests.get(JUSTIN_STREAM_URL % (",".join(channel_names)))

    try:
        message = response.json()
    except ValueError:
        # JSON Decode failed
        logging.warning("Invalid message from Justin.TV: %s" % (response.text))
        return []

    if not isinstance(message, list):
        logging.warning("Unexpected JSON from Justin.TV: %s" % (message))
        return []

    print(response)

    channels = []
    try:
        channels = map(lambda s: s["channel"]["login"], message)
    except KeyError:
        logging.warning("Justin.TV response format has changed: %s"
                        % (stream.json()))

    return channelsxo
