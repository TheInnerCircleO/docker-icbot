docker-icbot
============

Docker image for The Inner Circle's Google Hangouts chat bot -- built on
[HangoutsBot](https://github.com/hangoutsbot/hangoutsbot).

[![Build Status](https://travis-ci.org/TheInnerCircleO/docker-icbot.svg?branch=master)](https://travis-ci.org/TheInnerCircleO/docker-icbot)
[![](https://badge.imagelayers.io/theinnercircle/icbot:latest.svg)](https://imagelayers.io/?images=theinnercircle/icbot:latest 'Get your own badge on imagelayers.io')


Prerequisites
-------------

  - [Docker Engine](https://www.docker.com) >= v1.9


Running the Container
---------------------

#### Create a named data volume

In order to persist configuration data through container upgrades we need to
create a named data volume (not required but _highly_ recommended):

    docker volume create --name hangoutsbot-data

#### First run & authentication

The first time you run the bot you have to authenticate it manually. To do
this run the bot interactively and follow the instructions provided:

    docker run -it --rm -v hangoutsbot-data:/etc/hangoutsbot theinnercircle/icbot

#### Running the bot

Once authenticated you can use `Ctrl + C` to kill the running container and run
a daemonized bot container:

    docker run -dt -v hangoutsbot-data:/etc/hangoutsbot --name icbot theinnercircle/icbot


###### Optional 'docker run' Arguments

`--restart always` - Always restart the container regardless of the exit status. See the Docker
                     [restart policies](https://goo.gl/OI87rA) for additional details.


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

    docker run -it --rm -v hangoutsbot-data:/etc/hangoutsbot -v /path/to/plugins/plugin_name.py:/opt/hangoutsbot/hangupsbot/plugins/plugin_name.py theinnercircle/icbot


-----

**Copyright (c) 2016 The Inner Circle <https://github.com/TheInnerCircleO>**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
