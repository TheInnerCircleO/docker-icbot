import datetime
import hangups

from random import randint


def dilbert(bot, event, *args):
    """/bot dilbert [YYYY-MM-DD | random]
    NOTE: First dilbert 1989-04-16"""

    dilbert_date_format = '%Y-%m-%d'

    today = datetime.date.today()

    dilbert_modifier = today.strftime(dilbert_date_format)

    segments = [
        hangups.ChatMessageSegment(
            "Here's your fucking dilbert: ",
            is_bold=True
        )
    ]

    if args:

        first_timestamp = int(
            datetime.datetime.strptime(
                '1989-04-16',
                dilbert_date_format
            ).strftime('%s')
        )

        today_timestamp = int(
            today.strftime('%s')
        )

        if args[0] == 'random':

            random_timestamp = randint(first_timestamp, today_timestamp)

            dilbert_modifier = datetime.date.fromtimestamp(
                random_timestamp
            ).strftime(dilbert_date_format)

        else:

            try:

                timestamp = int(
                    datetime.datetime.strptime(
                        args[0],
                        dilbert_date_format
                    ).strftime('%s')
                )

            except:

                bot.send_message(
                    event.conv,
                    'Invalid date string: {}'.format(args[0])
                )

                return

            date_range = range(first_timestamp, today_timestamp)

            if timestamp not in date_range:

                bot.send_message(
                    event.conv,
                    'Date out of range: {}'.format(args[0])
                )

                return

            dilbert_modifier = datetime.date.fromtimestamp(
                timestamp
            ).strftime(dilbert_date_format)

    link = 'http://dilbert.com/strip/{}'.format(dilbert_modifier)

    segments.append(
        hangups.ChatMessageSegment(
            link,
            hangups.SegmentType.LINK,
            link_target=link
        )
    )

    bot.send_message_segments(event.conv, segments)
