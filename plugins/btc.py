import json
import requests


def get_json(url):
    """
    TODO: Make this act sane when bad status_code or an Exception is thrown
    Grabs json from a URL and returns a python dict
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; \
               rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'}

    json_result = requests.get(url, headers=headers)
    if json_result.status_code == 200:
        try:
            obj_result = json.loads(json_result.text)
            return obj_result
        except Exception as e:
            return e
    else:
        return json_result.status_code


def btc(bot, event, *args):
    """
    /bot btc
    displays current btc on BTC-e
    """
    btce_json = get_json('http://btc-e.com/api/3/ticker/btc_usd')
    result = 'BTC/USD: ' + str(btce_json['btc_usd']['avg'])

    bot.send_message_parsed(event.conv, result)
