Reddit Twitch Bot
=================

A Reddit bot which polls Twitch.tv streams and updates
a subreddit's sidebar with their current statuses.

Usage
-----

 0. Have Python (v2 or v3) installed, along with the following libraries:
    0. [Requests](http://docs.python-requests.org/en/latest/user/install/)
    1. [PRAW](https://praw.readthedocs.org/en/latest/#installation)
    2. configparser
 1. Register your bot with Twitch at http://www.twitch.tv/kraken/oauth2/clients/new
 2. Create a Reddit account for the bot, and make it a mod on the
    subreddit you want it to work on.
 3. Clone this repository.
 4. Copy `config.sample.conf` to `config.conf`.
 5. Open up `config.conf` and fill in the required fields.
 6. Add the following code snippet in your subreddit's sidebar where
    you want the stream list to be printed.

        [](#BOT_STREAMS)[](/BOT_STREAMS)

    These are empty links, so they won't show up on the page, but the
    bot will be able to see them and add text between them.
 7. Run the bot as `./twitchbot`. It will use a configuration file
    named `config.conf` by default, or you can run it as `./twitchbot
    other_config.conf` to use
 8. (Optional) Setup a crontab (or equivalent) to run the script
    as often as you want.

Templating
----------

This bot outputs stream information according to a user specified
format. The `template` value is printed for each active stream, with
the following substitutions made:

| These values: | Will be replaced with this data:             |
| ------------- | -------------------------------------------- |
| $name         | The channel name                             |
| $viewers      | The number of active viewers                 |
| $title        | The current title of the stream              |
| $link         | The URL of the stream                        |
| $icon         | The URL of the streamer's 300x300 icon       |
| $banner       | The URL of the streamer's banner             |

Also, all Python escape sequences are supported in `template`,
`header`, `footer`, `separator`, and `no_streams`.

Code Style
----------

All code is PEP8 compliant.
