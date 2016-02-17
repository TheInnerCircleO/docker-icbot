import hangups
import re

from random import randint


def roll(bot, event, *args):
    """
    /bot roll [ 2d6 | 1d10 | etc ]
    """

    segments = list()

    for arg in list(args):

        validArg = re.match('[0-9]*d[0-9]*', arg)

        if validArg is None:
            bot.send_message(event.conv, 'Invalid dice string: {}'.format(arg))
            continue

        segments.append(
            hangups.ChatMessageSegment(
                '{} rolled {}: '.format(event.user.first_name, arg),
                is_bold=True
            )
        )

        total = 0

        die = int(arg.split('d')[0])
        sides = int(arg.split('d')[1])

        for i in range(1, die + 1):

            roll = randint(1, sides)

            if i != 1:
                segments.append(hangups.ChatMessageSegment(', '))

            segments.append(hangups.ChatMessageSegment(str(roll)))

            total += roll

        segments.append(hangups.ChatMessageSegment(' [{}]'.format(total)))

        segments.append(
            hangups.ChatMessageSegment('\n', hangups.SegmentType.LINE_BREAK)
        )

    bot.send_message_segments(event.conv, segments)
