docker-icbot
============

Docker image for The Inner Circle's Google Hangouts chat bot -- built on
[HangoutsBot](https://github.com/hangoutsbot/hangoutsbot).

[![Build Status](https://travis-ci.org/TheInnerCircleO/docker-icbot.svg?branch=master)](https://travis-ci.org/TheInnerCircleO/docker-icbot)
[![](https://images.microbadger.com/badges/image/theinnercircle/icbot.svg)](http://microbadger.com/#/images/theinnercircle/icbot "Get your own image badge on microbadger.com")

Prerequisites
-------------

  - [Docker Engine](https://www.docker.com) >= v1.9


Running the Container
---------------------

#### Create a named data volume

In order to persist configuration data through container upgrades we need to
create a named data volume (not required but _highly_ recommended):

    docker volume create --name icbot-data

#### First run & authentication

The first time you run the bot you have to authenticate it manually. To do
this run the bot interactively and follow the instructions provided:

    docker run -it --rm -v icbot-data:/etc/hangoutsbot theinnercircle/icbot

#### Running the bot

Once authenticated you can use `Ctrl + C` to kill the running container and run
a daemonized bot container:

    docker run -dt -v icbot-data:/etc/hangoutsbot --name icbot theinnercircle/icbot


###### Optional 'docker run' Arguments

`-e TZ=America/Phoenix` - Set the timezone for your server. You can find your timezone in this
                          [list of timezones](https://goo.gl/uy1J6q). Use the (case sensitive)
                          value from the `TZ` column. If left unset, timezone will be UTC.

`--restart unless-stopped` - Always restart the container regardless of the exit status, but do not
                             start it on daemon startup if the container has been put to a stopped
                             state before. See the Docker [restart policies](https://goo.gl/Y0dlDH)
                             for additional details.


Modifying the Config
--------------------

The bot configuration can be modified by editing the `config.json` file in the
running container:

    docker exec -it icbot vi /etc/hangoutsbot/config.json

After saving your changes and exiting the editor, restart the running container
to apply the changes:

    docker retstart icbot


Plugin Development
------------------

To test a single plugin during development you can mount your plugin file or
folder via a docker volume (the `-v` switch) to a temporary container running
in the foreground:

    docker run -it --rm -v icbot-data:/etc/hangoutsbot -v /path/to/plugins/plugin_name.py:/opt/hangoutsbot/hangupsbot/plugins/plugin_name.py theinnercircle/icbot

Troubleshooting
---------------

Please report bugs to the [GitHub Issue Tracker](https://github.com/TheInnerCircleO/docker-icbot/issues).

Copyright
---------

This project is liscensed under the [MIT License](https://github.com/TheInnerCircleO/docker-icbot/blob/master/LICENSE).
