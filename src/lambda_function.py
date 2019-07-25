import requests
import os
import json
import logging

logging.basicConfig(level=logging.INFO)

API_KEY=(os.environ.get('API_KEY'))
TOKEN=(os.environ.get('TOKEN'))
LIST_ID=(os.environ.get('LIST_ID'))
WEB_HOOK_URL=(os.environ.get('WEB_HOOK_URL'))
URL=(os.environ.get('URL'))

def lambda_handler(context, value):
    cards = requests.get(URL + "lists/" + LIST_ID + "/cards?key=" + API_KEY + "&token=" + TOKEN + "&fields=id,name,badges,labels")
    
    #　ヘッダー
    payload_dic = {
            "text": "------未完了タスクの報告です------",
        }
    r = requests.post(WEB_HOOK_URL, data=json.dumps(payload_dic))
    logging.info('%s %s', "requests", r)

    # タスク投稿
    for card in cards.json():
        payload_dic = {
            "text": card["name"],
        }
        r2 = requests.post(WEB_HOOK_URL, data=json.dumps(payload_dic))
        logging.info('%s %s', "requests", r2)

    payload_dic = {
            "text": "------未完了タスクの報告でした------",
        }
    r3 = requests.post(WEB_HOOK_URL, data=json.dumps(payload_dic))
    logging.info('%s %s', "requests", r3)
    return "ok"
