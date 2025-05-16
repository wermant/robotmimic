import json

GATEWAY_IDENTIFIER = '{"channel":"GatewayChannel"}'


def usernameCount(ws, received_message, channelId):
    metadata = received_message["message"]["metadata"]
    username = metadata[8:metadata.index("\",")]
    text = username + " contains " + str(len(username)) + " characters."
    response = {
        "command": "message",
        "identifier": GATEWAY_IDENTIFIER,
        "data": json.dumps({
            "action": "send_message",
            "text": text,
            "channelId": channelId
        })
    }
    ws.send(json.dumps(response)) 

def followMessage(ws, received_message, channelId):
    metadata = received_message["message"]["metadata"]
    username = metadata[8:metadata.index("\",")]
    response = {
        "command": "message",
        "identifier": GATEWAY_IDENTIFIER,
        "data": json.dumps({
            "action": "send_message",
            "text": "AWROOOOOOO!!! Thank you for the follow @{}. I'm so glad to have you here!".format(username),
            "channelId": channelId
        })
    }
    ws.send(json.dumps(response)) 
