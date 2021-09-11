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

        carousel_template_message = TemplateSendMessage(
            alt_text='目錄 template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/kzi5kKy.jpg',
                        title='選擇服務',
                        text='請選擇',
                        actions=[
                            MessageAction(
                                label='開始玩',
                                text='開始玩'
                            ),
                            URIAction(
                                label='影片介紹 阿肥bot',
                                uri='https://youtu.be/1IxtWgWxtlE'
                            ),
                            URIAction(
                                label='如何建立自己的 Line Bot',
                                uri='https://github.com/twtrubiks/line-bot-tutorial'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/DrsmtKS.jpg',
                        title='選擇服務',
                        text='請選擇',
                        actions=[
                            MessageAction(
                                label='other bot',
                                text='imgur bot'
                            ),
                            MessageAction(
                                label='油價查詢',
                                text='油價查詢'
                            ),
                            URIAction(
                                label='聯絡作者',
                                uri='https://www.facebook.com/TWTRubiks?ref=bookmarks'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/h4UzRit.jpg',
                        title='選擇服務',
                        text='請選擇',
                        actions=[
                            URIAction(
                                label='分享 bot',
                                uri='https://line.me/R/nv/recommendOA/@vbi2716y'
                            ),
                            URIAction(
                                label='PTT正妹網',
                                uri='https://ptt-beauty-infinite-scroll.herokuapp.com/'
                            ),
                            URIAction(
                                label='youtube 程式教學分享頻道',
                                uri='https://www.youtube.com/channel/UCPhn2rCqhu0HdktsFjixahA'
                            )
                        ]
                    )
                ]
            )    
        )

        line_bot_api.reply_message(event.reply_token, carousel_template_message)
        
    else:
        line_bot_api.reply_message(reply_token, TextSendMessage(text=message))

if __name__ == "__main__":
    app.run()