import hangups
import requests
import json
import datetime
import re

base_url = 'https://online-go.com'


def ogs_auth(client_id, client_secret, grant_type, username, password):
    auth_endpoint = '/oauth2/access_token'

    payload = {'client_id': client_id,
               'client_secret': client_secret,
               'grant_type': grant_type,
               'username': username,
               'password': password}

    auth_url = ''.join([base_url, auth_endpoint])
    try:
        token_response = requests.post(auth_url, data=payload)
        if token_response.status_code == 200:
            token = json.loads(token_response.text)['access_token']
            bearer = ''.join(['Bearer ', token])
            auth_header = {'Authorization:': bearer}
            return auth_header
        else:
            raise Exception("Could Not Authenticate")
    except:
        raise


def ogs_rank_string(rank_val):
    if rank_val < 30:
        return "%dK" % (30-rank_val)
    else:
        return "%dD" % ((rank_val-29))


def ogs_rank_value(rank_str):
    good_rank_string = '[1-9][Kk|Dd]'
    good_rank_re = re.compile(good_rank_string)
    result = good_rank_re.search(str(rank_str))

    if result:
        rank = result.group().lower()
        if 'd' in rank:
            rank_val = 29+int(rank[0])
        else:
            rank_val = 30-int(rank[0])
        return rank_val
    else:
        return False


def int_val(input):
    try:
        return int(input)
    except ValueError:
        return 10


def ogs(bot, event, *args):

    if args:
        count = int_val(args[0])
    else:
        count = 10
    # Cant explain 240 min offset
    past_date = ((datetime.datetime.utcnow() -
                  datetime.timedelta(minutes=60+240)).strftime(
        "%Y-%m-%dT%H:%M:%S"))
    games_endpoint = ''.join(['/api/v1/games/?started__gt=', past_date,
                             '&black_lost=true&white_lost=true'])
    games_url = ''.join([base_url, games_endpoint])
    games_text = requests.get(games_url).text
    games_list = json.loads(games_text)['results']
    sorted_games = sorted(games_list,
                          key=lambda g: datetime.datetime.strptime(
                              g['started'][0:18],
                              "%Y-%m-%dT%H:%M:%S"), reverse=True)
    max_games = min(len(sorted_games), count)
    segments = []
    for game in sorted_games:
        now = (datetime.datetime.utcnow())
        game_time = datetime.datetime.strptime(game['started'][0:18],
                                               "%Y-%m-%dT%H:%M:%S")
        age = str(abs((now - game_time).seconds)/60).split('.')
        age = ''.join([age[0], '.', age[1][0]])

        if not game['ended'] and game['started']:
            bname = game['players']['black']['username']
            wname = game['players']['white']['username']
            if 'ranking_live' in game['players']['white']:
                wrank = game['players']['white']['ranking_live']
            else:
                wrank = 0
            if 'ranking_live' in game['players']['black']:
                brank = game['players']['black']['ranking_live']
            else:
                brank = 0
            if wrank >= 20 and brank >= 20:
                wrank = ogs_rank_string(wrank)
                brank = ogs_rank_string(brank)
                title = ''.join([wname, "[", str(wrank), "] vs ", bname,
                                "[", str(brank), "] ", str(age), " Min"])
                link = ''.join(['https://online-go.com/game/',
                               str(game['id'])])
                segments.append(hangups.ChatMessageSegment(title,
                                hangups.SegmentType.LINK,
                                link_target=link))
                segments.append(hangups.ChatMessageSegment('\n',
                                hangups.SegmentType.LINE_BREAK))

    bot.send_message_segments(event.conv, segments[0:max_games*2])
