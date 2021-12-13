from TikTokAPI import TikTokAPI
import pandas as pd

def getdata(hastag):
    cookie = {
      "s_v_web_id": "verify_kw1ax20d_q8l9UCo9_lD9Y_42KH_AEyN_2YTVWKNTELA5",
      "tt_webid": "1%7CLY3I1vm7RPtHbTF7N6OsJaUwCnFFviQawSIuuiQeF88%7C1637022273%7C2982579e664bc1407289a770e4492eab3a9dbc502fa02f89ae70464472d0190c"
    }
    api = TikTokAPI(cookie=cookie)
    music_tt = []
    play_tt = []
    hastag_data_tt = []
    author_follower_tt = []
    author_heart_tt = []

    TiktokData = getTiktokByHastag(hastag,api)
    print(TiktokData)
    for data_search in TiktokData['itemList']:
        music_tt.append(data_search['music']['title'])
        play_tt.append(data_search['stats']['playCount'])
        author_follower_tt.append(data_search['authorStats']['followerCount'])
        author_heart_tt.append(data_search['authorStats']['heart'])
        hastag_data_tt.append(hastag)

    data_tiktok = {
        'music': music_tt,
        'hastag_data': hastag_data_tt,
        'author_follower': author_follower_tt,
        'author_heart': author_heart_tt,
        'play': play_tt
    }
    dataframeTiktok = pd.DataFrame(data_tiktok,
                                   columns=['music', 'hastag_data', 'author_follower', 'author_heart', 'play'])
    return dataframeTiktok


def getTiktokByHastag(hastag,api):
    retval = api.getVideosByHashTag(hastag)
    return retval

def get_music(hastag):
    cookie = {
        "s_v_web_id": "verify_kw1ax20d_q8l9UCo9_lD9Y_42KH_AEyN_2YTVWKNTELA5",
        "tt_webid": "1%7CLY3I1vm7RPtHbTF7N6OsJaUwCnFFviQawSIuuiQeF88%7C1637022273%7C2982579e664bc1407289a770e4492eab3a9dbc502fa02f89ae70464472d0190c"
    }
    api = TikTokAPI(cookie=cookie)
    music_tt = []

    TiktokData = getTiktokByHastag(hastag, api)
    # print(TiktokData)
    for data_search in TiktokData['itemList']:
        music_tt.append(data_search['music']['title'])
    return music_tt

