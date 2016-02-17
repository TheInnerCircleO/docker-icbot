import json
import re
import requests

from random import choice
from urllib import parse


def thoughts(bot, event, *args):
    """/bot thoughts [subject]
    Probe the bot's mind on a subject."""

    if not args:
        bot.send_message(event.conv, 'Wut?')
        return

    results = requests.get(
        'https://api.reddit.com/search/?q={query}&limit=5'.format(
            query=parse.quote_plus(' '.join(args))
        ),
        headers={'User-Agent': 'icbot v360.N0.SC0P3'}
    )

    if results.status_code != 200:

        bot.send_message(
            event.conv,
            'Hmmmmmm: {}'.format(results.status_code)
        )

        return

    results_obj = json.loads(results.text)

    if not results_obj['data']['children']:

        bot.send_message(event.conv, 'Hmmm.')
        return

    topic = choice(results_obj['data']['children'])

    rerep = re.compile(re.escape('reddit'), re.IGNORECASE)

    title = rerep.sub(
        'The Inner Circle',
        topic['data']['title']
    )

    bot.send_message(event.conv, title)
