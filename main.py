# from __future__ import unicode_literals
# import os
# from flask import Flask, request, abort
# from linebot import LineBotApi, WebhookHandler
# from linebot.exceptions import InvalidSignatureError
# from linebot.models import MessageEvent, TextMessage, TextSendMessage

# import json
# import configparser

# app = Flask(__name__)

# # LINE 聊天機器人的基本資料
# config = configparser.ConfigParser()
# config.read('config.ini')

# line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
# handler = WebhookHandler(config.get('line-bot', 'channel_secret'))


# # 接收 LINE 的資訊
# @app.route("/callback", methods=['POST'])
# def callback():
#     signature = request.headers['X-Line-Signature']

#     body = request.get_data(as_text=True)
#     app.logger.info("Request body: " + body)
    
#     print(body)

#     try:
#         handler.handle(body, signature)
#     except InvalidSignatureError:
#         abort(400)

#     return 'OK'

# # Message event
# @handler.add(MessageEvent)
# def handle_message(event):
#     message_type = event.message.type
#     user_id = event.source.user_id
#     reply_token = event.reply_token
#     message = event.message.text
#     if(message == 'profile'):
#         FlexMessage = json.load(open('card.json','r',encoding='utf-8'))
#         line_bot_api.reply_message(reply_token, TextSendMessage(text='test'))
#         line_bot_api.reply_message(reply_token, FlexSendMessage('profile',FlexMessage))
#     else:
#         line_bot_api.reply_message(reply_token, TextSendMessage(text=message))

# if __name__ == "__main__":
#     app.run()

from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import json
import configparser

app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))


# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    print(body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# Message event
@handler.add(MessageEvent)
def handle_message(event):
    message_type = event.message.type
    user_id = event.source.user_id
    reply_token = event.reply_token
    message = event.message.text
    if(message == 'profile'):
       #FlexMessage = json.load(open('card.json','r',encoding='utf-8'))

        flex_message = FlexSendMessage(
         alt_text='hello',
         contents={
          'type': 'bubble',
          'direction': 'ltr',
          'hero': {
            'type': 'image',
            'url': 'https://example.com/cafe.jpg',
            'size': 'full',
            'aspectRatio': '20:13',
            'aspectMode': 'cover',
            'action': { 'type': 'uri', 'uri': 'http://example.com', 'label': 'label' }
          }
         }
        )
       
        line_bot_api.reply_message(reply_token, TextSendMessage(text='test'))
        line_bot_api.reply_message(reply_token, flex_message)
        
    else:
        line_bot_api.reply_message(reply_token, TextSendMessage(text=message))

if __name__ == "__main__":
    app.run()