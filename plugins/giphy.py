import aiohttp
import io
import json
import os
import plugins
import requests

from random import choice
from urllib import parse


_conf = dict()


def _initialise(bot):

    giphy_api_key = bot.get_config_option("giphy-apikey")

    if giphy_api_key:
        plugins.register_user_command(['giphy'])
        _conf['giphy_api_key'] = giphy_api_key
    else:
        print(_("GIPHY: config.giphy-apikey required"))


def giphy(bot, event, *args):
    """Reaction gifs deliverd to you in 30 minutes or less"""

    if not args:
        bot.send_message(event.conv, 'What are you looking for?')
        return

    results = requests.get(
        '{search_url}?api_key={api_key}&q={query}'.format(
            search_url='https://api.giphy.com/v1/gifs/search',
            api_key=_conf['giphy_api_key'],
            query=parse.quote_plus(' '.join(args))
        ),
        headers={'User-Agent': 'icbot v360.N0.SC0P3'}
    )

    if results.status_code != 200:

        bot.send_message(
            event.conv,
            'ERROR: {}'.format(results.status_code)
        )

        return

    results_obj = json.loads(results.text)

    if len(results_obj['data']) == 0:

        bot.send_message(
            event.conv,
            'I couldn\'t find anything when looking for "{}"'.format(
                ' '.join(args)
            )
        )

        return

    gif = choice(results_obj['data'])

    image = gif['images']['downsized']['url']

    filename = os.path.basename(image)
    r = yield from aiohttp.request('get', image)
    raw = yield from r.read()
    image_data = io.BytesIO(raw)

    image_id = yield from bot._client.upload_image(
        image_data,
        filename=filename
    )

    bot.send_message_segments(event.conv, None, image_id=image_id)
