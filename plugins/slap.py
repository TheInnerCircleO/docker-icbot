from random import choice


def slap(bot, event, *args):

    if not args:

        bot.send_message(event.conv, 'Who should I slap?')
        return

    name = ' '.join(list(args))

    objects = [
        "a large trout",
        "a large black cock",
        "a soggy noodle",
        "an iron gauntlet"
    ]

    message = '/me slaps {} around a bit with {}'.format(
        name,
        choice(objects)
    )

    bot.send_message(event.conv, message)
