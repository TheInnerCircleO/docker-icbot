import hangups
import json
import requests

from random import choice
from urllib import parse


def reddit(bot, event, *args):
    """/bot reddit [query]
    Search and return a random topic relating to your query."""

    results = requests.get(
        'https://api.reddit.com/search/?q={query}&limit=10'.format(
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

    short_link = 'http://redd.it/{id}'.format(id=topic['data']['id'])

    segments = list()

    if topic['data']['over_18']:

        segments.append(
            hangups.ChatMessageSegment('[NSFW] ', is_bold=True)
        )

    segments.append(
        hangups.ChatMessageSegment(topic['data']['title'])
    )

    segments.append(
        hangups.ChatMessageSegment('\n', hangups.SegmentType.LINE_BREAK)
    )

    segments.append(
        hangups.ChatMessageSegment(
            '{link}'.format(link=short_link),
            hangups.SegmentType.LINK,
            link_target=short_link
        )
    )

    bot.send_message_segments(event.conv, segments)
