import requests
import time
import xml.etree.ElementTree as ET

from datetime import datetime
from random import randint


def hiztory(bot, event, *args):
    """/bot hiztory [category]
    Returns a random event that occured on this day in history
    Valid categories are: events (default), births, deaths, aviation
    """

    categories = [
        'events', 'births', 'deaths', 'aviation'
    ]

    if args:

        if args[0] in categories:

            category = args[0]

        else:

            bot.send_message(event.conv, 'ERROR: Invalid category')
            return

    else:

        category = 'events'

    url = 'http://api.hiztory.org/{}/{}/{}/1/15/api.xml'.format(
        category, time.strftime('%m'), time.strftime('%d')
    )

    xml = requests.get(url)

    if xml.status_code != 200:

        bot.send_message(
            event.conv,
            'Server returned HTTP status code: {}'.format(xml.status_code)
        )

        return

    root = ET.fromstring(xml.text)
    events = list(root.find('events').iter('event'))

    index = randint(0, len(events) - 1)

    year = datetime.strptime(
        events[index].attrib['date'],
        '%Y-%m-%d'
    ).strftime('%Y')

    message = events[index].attrib['content']

    bot.send_message_parsed(
        event.conv,
        '<b>{}:</b> {}'.format(year, message)
    )
