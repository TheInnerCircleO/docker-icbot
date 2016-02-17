from random import choice, shuffle


def eightball(bot, event, *args):
    """
    /bot eightball [question]
    """

    if not args:
        bot.send_message(event.conv, 'What is your question?')
        return

    answers = [
        "It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Yes definitely",
        "You may rely on it",
        "As I see it, yes",
        "Most likely",
        "Outlook good",
        "Yes",
        "Signs point to yes",
        "Reply hazy try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful"
    ]

    shuffle(answers)

    bot.send_message(event.conv, (choice(answers)))
