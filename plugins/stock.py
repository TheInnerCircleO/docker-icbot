import hangups
import json
import requests


def stock(bot, event, *args):
    """
    /bot stock ticker1 ticker2 tickerN
    displays current price for tickers
    """
    segments = []
    tickers = ','.join(list(args))
    raw_data = requests.get(
        'http://finance.google.com/finance/info?client=ig&q=' +
        tickers)
    try:
        # Cant use get_json because of 3 invalid chars
        data = json.loads(raw_data.text[3:])
        for i in data:
            stock_link = 'https://www.google.com/finance?q={}'.format(i['t'])
            link_segment = hangups.ChatMessageSegment(
                '{:<6}'.format(i['t']),
                hangups.SegmentType.LINK,
                link_target=stock_link
            )
            text = ': {:<5} | {:^4} ({}%)'.format(i['l'], i['c'], i['cp'])
            segments.append(link_segment)
            segments.append(hangups.ChatMessageSegment(text))
            segments.append(
                hangups.ChatMessageSegment(
                    '\n',
                    hangups.SegmentType.LINE_BREAK
                )
            )
    except Exception as e:
        return bot.parse_and_send_segments(
            event.conv,
            "Ticker probably doesn't exist: {}".format(str(e))
        )

    bot.send_message_segments(event.conv, segments)
