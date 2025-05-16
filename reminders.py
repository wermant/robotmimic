import json

GATEWAY_IDENTIFIER = '{"channel":"GatewayChannel"}'


def dropin(ws, channelId):
    response = {
        "command": "message",
        "identifier": GATEWAY_IDENTIFIER,
        "data": json.dumps({
            "action": "send_whisper",
            "username": "mimic",
            "text": "Do not forget to dropin at the end of your stream!!!",
            "channelId": channelId})
    }

    ws.send(json.dumps(response))
