# 載入需要的模組
from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('fPG+8U3nBkICW4j1mm0aTzbo6aMfGD5VNrZ44x2FpMEYf6Nhai1v+tCkOfGd5XllJWREM7JaOvMcy2W8HTNyOEmdWOo8HTIrr8oPy3SJD0ynf2/vRsDWsDLWKrVDBJFYFpT5pfRq/Ty2WU7aK1MMdwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d1c7c47f2e3e0f638b554040184a41f4')

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

if __name__ == "__main__":
    app.run()