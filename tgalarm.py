# -*- coding: utf-8 -*-
import urllib
import sys
import requests


BOT_TOK_CATHOLIC= '667648728:AAF0C8LcDbgy8Uvg9g_KJOopI5bm4KOTOwU'
CHAT_ID_CATHOLIC = '-1001364373227'

chatMap = {
    'catholic': {'chat_id': CHAT_ID_CATHOLIC, 'bot_tok': BOT_TOK_CATHOLIC}
}


def sendMsg(tok, chat_id, msg):
    payload = { 'chat_id': chat_id, 'text': msg }
    url = 'https://api.telegram.org/bot%s/sendMessage' % tok
    try:
        url_values = urllib.parse.urlencode(payload)
        full_url = url + '?' + url_values
        print(len(full_url), full_url)
        response = requests.get(full_url)
        data = response.json() # format : dict
        if data['ok'] is False:
            print('error_code:', data['error_code'], ' description: ', data['description'])
            raise ValueError

    except Exception as e:
        errmsg = 'FAILED to sendMsg. Err: {}'.format(e)
        print(errmsg)

    return


def sendTo(target, msg):
    if target in chatMap:
        sendMsg(chatMap[target]['bot_tok'], chatMap[target]['chat_id'], msg)
    else:
        print("올바른 챗봇 이름이 아닙니다.")
        raise ValueError
    return


def sendAll(msg):
    sendTo('all', msg)
    return


if __name__ == "__main__":
    target = 'test'
    msg = 'msg test'
    
    if target in chatMap:
        sendTo(target, msg)


