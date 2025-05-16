import json

GATEWAY_IDENTIFIER = '{"channel":"GatewayChannel"}'

def tipMessage(ws, received_message, channelId):
    metadata = received_message["message"]["metadata"]
    username = metadata[8:metadata.index("\",")]
    response = {
        "command": "message",
        "identifier": GATEWAY_IDENTIFIER,
        "data": json.dumps({
            "action": "send_message",
            "text": "AWROOOOOOO!!! Thank you for the tip @{}.".format(username),
            "channelId": channelId
        })
    }
    ws.send(json.dumps(response)) 