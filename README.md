Reddit Twitch Bot
=================

A Reddit bot which polls Twitch.TV (and Justin.TV) streams and updates
a subreddit's sidebar with their current statuses.

Usage
-----

 0. Have Python (v2 or v3) installed, along with the following libraries:
    0. [Requests](http://docs.python-requests.org/en/latest/user/install/)
    1. [PRAW](https://praw.readthedocs.org/en/latest/#installation)
    2. configparser
 1. Create a reddit account for the bot, and make it a mod on the
    subreddit you want it to work on.
 2. Clone this repository.
 3. Copy `config.sample.conf` to `config.conf`.
 4. Open up `config.conf` and fill in the required fields.
 5. Add the following code snippet in your subreddit's sidebar where
    you want the stream list to be printed.

        [](#BOT_STREAMS)[](/BOT_STREAM)

    These are empty links, so they won't show up on the page, but the
    bot will be able to see them and add text between them.
 6. Run the bot as `./twitchbot`. It will use a configuration file
    named `config.conf` by default, or you can run it as `./twitchbot
    other_config.conf` to use
 7. (Optional) Setup a crontab (or equivalent) to run the script
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
| $status       | Seems to be similar to $title...             |
| $icon         | The URL of the streamer's 150x150 icon       |
| $icon_tiny    | Same as $icon, but for the 50x50 icon        |
| $icon_small   | Same as $icon, but for the 70x70 icon        |
| $icon_large   | Same as $icon, but for the 300x300 icon      |
| $icon_huge    | Same as $icon, but for the 600x600 icon      |

Also, all Python escape sequences are supported in `template`,
`header`, `footer`, `separator`, and `no_streams`.

Code Style
----------

All code is PEP8 compliant.
