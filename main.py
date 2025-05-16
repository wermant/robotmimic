from dotenv import load_dotenv
load_dotenv()
import json
import base64
import flask
import os
import threading
import requests
import websocket
import bot

HOST = os.getenv('JOYSTICKTV_HOST')
CLIENT_ID = os.getenv('JOYSTICKTV_CLIENT_ID')
CLIENT_SECRET = os.getenv('JOYSTICKTV_CLIENT_SECRET')
WS_HOST = os.getenv('JOYSTICKTV_API_HOST')
ACCESS_TOKEN = base64.b64encode(str(CLIENT_ID + ":" + CLIENT_SECRET).encode('ascii')).decode()
GATEWAY_IDENTIFIER = '{"channel":"GatewayChannel"}'
CHANNEL_ID = "8aedfb10b414f0a9fdcf3cef70dbd9fbdc5929fc121400c38c512a839e78d71f"

URL = "{}?token={}".format(WS_HOST, ACCESS_TOKEN)

connected = False
count = 0

def on_message(ws, message):
    global connected
    global count
    received_message = json.loads(message)

    if 'type' in received_message:
        if received_message["type"] == "reject_subscription":
            print('nope... no connection for you')
            return
        elif received_message["type"] == "confirm_subscription":
            connected = True
            return
        elif received_message["type"] == "ping":
            count+=1
            if count%225==0:
                bot.Bot.handle_reminders(ws, CHANNEL_ID)
            return
    else:
        if connected:
            if "message" in received_message:
                if received_message["message"]["type"].lower() == "followed":
                    bot.Bot.handle_follow(ws, received_message, CHANNEL_ID)
                elif received_message["message"]["type"].lower() == "tipped":
                    bot.Bot.handle_tips(ws, received_message, CHANNEL_ID)
                elif received_message["message"]["type"] == "new_message":
                    bot.Bot.handle_messages(ws, received_message, CHANNEL_ID)


def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("connection has closed")

def on_open(ws):
    print("connection has opened")
    ws.send(json.dumps({
        "command": "subscribe",
        "identifier": GATEWAY_IDENTIFIER,
    }))
ws = websocket.WebSocketApp(URL, on_message=on_message, on_error=on_error, on_close=on_close, on_open=on_open)
ws.run_forever()

app = flask.Flask(__name__)

@app.route("/")
def Home():
    return 'Visit <a href="/install">INSTALL</a> to install Bot'

@app.route("/install")
def Install():
    state = "abcflask123"
    return (flask.redirect(HOST + "/api/oauth/authorize?client_id=" + CLIENT_ID + "&scope=bot&state=" + state,code=302))

@app.route("/callback")
def Callback():
    # STATE should equal `abcflask123`
    state = flask.request.args.get('state')
    code = flask.request.args.get('code')
    print("STATE: {}".format(state))
    print("CODE: {}".format(code))

    params = {'redirect_uri' : "/unused",'code' : code,'grant_type' : "authorization_code"}
    headers = {'Authorization' : "Basic {}".format(ACCESS_TOKEN), 'Content-Type' : 'application/json'}
    req = requests.request('POST', HOST + "/api/oauth/token",params=params,headers=headers,data="")

    # Save to your DB if you need to request user data
    print(req.json()["access_token"])
    return "Bot started!"

if __name__ == '__main__':
    print("listening...")
    app.run(host="0.0.0.0", port="8080", debug=True)
