import json
import re
import random
import requests

HELP = "help"
MENU = "menu"
ROCK = "rock"
PAPER = "paper"
SCISSOR = "scissor"
RUPAUL = "rupaul"
ARIES = "aries"
TAURUS = "taurus"
GEMINI = "gemini"
CANCER = "cancer"
LEO = "leo"
VIRGO = "virgo"
LIBRA = "libra"
SCORPIO = "scorpio"
SAGITTARIUS = "sagittarius"
CAPRICORN = "capricorn"
AQUARIUS = "aquarius"
PISCES = "pisces"

MENU_OPTIONS = ["Robot Mimic Command Options:", "1. Chat your choice of rock, paper, or scissor to play rock, paper, scissor with the bot.",
                "2. Chat RuPaul to get a random drag race quote.", "3. Chat your astrological sign to see your daily horoscope."]

GATEWAY_IDENTIFIER = '{"channel":"GatewayChannel"}'


def botMenu(ws, received_message, channelId):
    message = received_message["message"]

    patternHelp = re.compile(HELP)
    patterMenu = re.compile(MENU)

    if patternHelp.match(message['text'].lower()) or patterMenu.match(message['text'].lower()):
        print("I was asked for")
        response = {
            "command": "message",
            "identifier": GATEWAY_IDENTIFIER,
            "data": json.dumps({
                "action": "delete_message",
                "messageId": message["messageId"],
                "channelId": channelId
            })
        }
        ws.send(json.dumps(response))

        for line in MENU_OPTIONS:
            response = {
                "command": "message",
                "identifier": GATEWAY_IDENTIFIER,
                "data": json.dumps({
                    "action": "send_whisper",
                    "username": message["author"]["username"],
                    "text": line,
                    "channelId": channelId
                })
            }
            ws.send(json.dumps(response))


def rps(ws, received_message, channelId):

    message = received_message["message"]

    patternRock = re.compile(ROCK)
    patternPaper = re.compile(PAPER)
    patternScissor = re.compile(SCISSOR)

    if patternRock.match(message['text'].lower()):
        pick = random.randint(0, 3)
        if (pick == 0):
            response = {
                "command": "message",
                "identifier": GATEWAY_IDENTIFIER,
                "data": json.dumps({
                    "action": "send_message",
                    "text": "Robot Mimic picked rock. You draw.",
                    "channelId": channelId
                })
            }
            ws.send(json.dumps(response))
        elif (pick == 1):
            response = {
                "command": "message",
                "identifier": GATEWAY_IDENTIFIER,
                "data": json.dumps({
                    "action": "send_message",
                    "text": "Robot Mimic picked paper. You lose.",
                    "channelId": channelId
                })
            }
            ws.send(json.dumps(response))
        else:
            response = {
                "command": "message",
                "identifier": GATEWAY_IDENTIFIER,
                "data": json.dumps({
                    "action": "send_message",
                    "text": "Robot Mimic picked scissor. You win.",
                    "channelId": channelId
                })
            }
            ws.send(json.dumps(response))

    if patternPaper.match(message['text'].lower()):
        pick = random.randint(0, 3)
        if (pick == 0):
            response = {
                "command": "message",
                "identifier": GATEWAY_IDENTIFIER,
                "data": json.dumps({
                    "action": "send_message",
                    "text": "Robot Mimic picked rock. You win.",
                    "channelId": channelId
                })
            }
            ws.send(json.dumps(response))
        elif (pick == 1):
            response = {
                "command": "message",
                "identifier": GATEWAY_IDENTIFIER,
                "data": json.dumps({
                    "action": "send_message",
                    "text": "Robot Mimic picked paper. You draw.",
                    "channelId": channelId
                })
            }
            ws.send(json.dumps(response))
        else:
            response = {
                "command": "message",
                "identifier": GATEWAY_IDENTIFIER,
                "data": json.dumps({
                    "action": "send_message",
                    "text": "Robot Mimic picked scissor. You lose.",
                    "channelId": channelId
                })
            }
            ws.send(json.dumps(response))

    if patternScissor.match(message['text'].lower()):
        pick = random.randint(0, 3)
        if (pick == 0):
            response = {
                "command": "message",
                "identifier": GATEWAY_IDENTIFIER,
                "data": json.dumps({
                    "action": "send_message",
                    "text": "Robot Mimic picked rock. You lose.",
                    "channelId": channelId
                })
            }
            ws.send(json.dumps(response))
        elif (pick == 1):
            response = {
                "command": "message",
                "identifier": GATEWAY_IDENTIFIER,
                "data": json.dumps({
                    "action": "send_message",
                    "text": "Robot Mimic picked paper. You win.",
                    "channelId": channelId
                })
            }
            ws.send(json.dumps(response))
        else:
            response = {
                "command": "message",
                "identifier": GATEWAY_IDENTIFIER,
                "data": json.dumps({
                    "action": "send_message",
                    "text": "Robot Mimic picked scissor. You draw.",
                    "channelId": channelId
                })
            }
            ws.send(json.dumps(response))


def rupaul(ws, received_message, channelId):
    message = received_message["message"]

    patternRupaul = re.compile(RUPAUL)

    if patternRupaul.match(message['text'].lower()):
        with open('rupaulQuotes.txt') as f:
            lines = [line.rstrip() for line in f]
        quote = lines[random.randint(0, len(lines))]
        response = {
            "command": "message",
            "identifier": GATEWAY_IDENTIFIER,
            "data": json.dumps({
                "action": "send_message",
                "text": quote,
                "channelId": channelId
            })
        }
        ws.send(json.dumps(response))


def horoscope(ws, received_message, channelId):

    patternAries = re.compile(ARIES)
    patternTaurus = re.compile(TAURUS)
    patternGemini = re.compile(GEMINI)
    patternCancer = re.compile(CANCER)
    patternLeo = re.compile(LEO)
    patternVirgo = re.compile(VIRGO)
    patternLibra = re.compile(LIBRA)
    patternScorpio = re.compile(SCORPIO)
    patternSagittarius = re.compile(SAGITTARIUS)
    patternCapricorn = re.compile(CAPRICORN)
    patternAquarius = re.compile(AQUARIUS)
    patternPisces = re.compile(PISCES)

    if (patternAries.match(received_message["message"]["text"].lower())):
        html = requests.get(
            "https://www.astrology.com/horoscope/daily/aries.html").text[39300:]
        html=html[html.find("400\">")+5:]
        responseText = html[0:html.find("</span>")]
        for i in range(0,len(responseText),280):
            response = {
                "command": "message",
                "identifier": GATEWAY_IDENTIFIER,
                "data": json.dumps({
                    "action": "send_message",
                    "text": responseText[i:i+280],
                    "channelId": channelId
                })
            }
            ws.send(json.dumps(response))

    elif (patternTaurus.match(received_message["message"]["text"].lower())):
        html = requests.get(
            "https://www.astrology.com/horoscope/daily/taurus.html").text[39300:]
        html=html[html.find("400\">")+5:]
        responseText = html[0:html.find("</span>")]
        for i in range(0,len(responseText),280):
            response = {
                "command": "message",
                "identifier": GATEWAY_IDENTIFIER,
                "data": json.dumps({
                    "action": "send_message",
                    "text": responseText[i:i+280],
                    "channelId": channelId
                })
            }
            ws.send(json.dumps(response))

    elif (patternGemini.match(received_message["message"]["text"].lower())):
        html = requests.get(
            "https://www.astrology.com/horoscope/daily/gemini.html").text[39300:]
        html=html[html.find("400\">")+5:]
        responseText = html[0:html.find("</span>")]
        for i in range(0,len(responseText),280):
            response = {
                "command": "message",
                "identifier": GATEWAY_IDENTIFIER,
                "data": json.dumps({
                    "action": "send_message",
                    "text": responseText[i:i+280],
                    "channelId": channelId
                })
            }
            ws.send(json.dumps(response))

    elif (patternCancer.match(received_message["message"]["text"].lower())):
        html = requests.get(
            "https://www.astrology.com/horoscope/daily/cancer.html").text[39300:]
        html=html[html.find("400\">")+5:]
        responseText = html[0:html.find("</span>")]
        for i in range(0,len(responseText),280):
            response = {
                "command": "message",
                "identifier": GATEWAY_IDENTIFIER,
                "data": json.dumps({
                    "action": "send_message",
                    "text": responseText[i:i+280],
                    "channelId": channelId
                })
            }
            ws.send(json.dumps(response))

    elif (patternLeo.match(received_message["message"]["text"].lower())):
        html = requests.get(
            "https://www.astrology.com/horoscope/daily/leo.html").text[39300:]
        html=html[html.find("400\">")+5:]
        responseText = html[0:html.find("</span>")]
        for i in range(0,len(responseText),280):
            response = {
                "command": "message",
                "identifier": GATEWAY_IDENTIFIER,
                "data": json.dumps({
                    "action": "send_message",
                    "text": responseText[i:i+280],
                    "channelId": channelId
                })
            }
            ws.send(json.dumps(response))

    elif (patternVirgo.match(received_message["message"]["text"].lower())):
        html = requests.get(
            "https://www.astrology.com/horoscope/daily/virgo.html").text[39300:]
        html=html[html.find("400\">")+5:]
        responseText = html[0:html.find("</span>")]
        for i in range(0,len(responseText),280):
            response = {
                "command": "message",
                "identifier": GATEWAY_IDENTIFIER,
                "data": json.dumps({
                    "action": "send_message",
                    "text": responseText[i:i+280],
                    "channelId": channelId
                })
            }
            ws.send(json.dumps(response))

    elif (patternLibra.match(received_message["message"]["text"].lower())):
        html = requests.get(
            "https://www.astrology.com/horoscope/daily/libra.html").text[39300:]
        html=html[html.find("400\">")+5:]
        responseText = html[0:html.find("</span>")]
        for i in range(0,len(responseText),280):
            response = {
                "command": "message",
                "identifier": GATEWAY_IDENTIFIER,
                "data": json.dumps({
                    "action": "send_message",
                    "text": responseText[i:i+280],
                    "channelId": channelId
                })
            }
            ws.send(json.dumps(response))

    elif (patternScorpio.match(received_message["message"]["text"].lower())):
        html = requests.get(
            "https://www.astrology.com/horoscope/daily/scorpio.html").text[39300:]
        html=html[html.find("400\">")+5:]
        responseText = html[0:html.find("</span>")]
        for i in range(0,len(responseText),280):
            response = {
                "command": "message",
                "identifier": GATEWAY_IDENTIFIER,
                "data": json.dumps({
                    "action": "send_message",
                    "text": responseText[i:i+280],
                    "channelId": channelId
                })
            }
            ws.send(json.dumps(response))

    elif (patternSagittarius.match(received_message["message"]["text"].lower())):
        html = requests.get(
            "https://www.astrology.com/horoscope/daily/sagittarius.html").text[39300:]
        html=html[html.find("400\">")+5:]
        responseText = html[0:html.find("</span>")]
        for i in range(0,len(responseText),280):
            response = {
                "command": "message",
                "identifier": GATEWAY_IDENTIFIER,
                "data": json.dumps({
                    "action": "send_message",
                    "text": responseText[i:i+280],
                    "channelId": channelId
                })
            }
            ws.send(json.dumps(response))

    elif (patternCapricorn.match(received_message["message"]["text"].lower())):
        html = requests.get(
            "https://www.astrology.com/horoscope/daily/capricorn.html").text[39300:]
        html=html[html.find("400\">")+5:]
        responseText = html[0:html.find("</span>")]
        for i in range(0,len(responseText),280):
            response = {
                "command": "message",
                "identifier": GATEWAY_IDENTIFIER,
                "data": json.dumps({
                    "action": "send_message",
                    "text": responseText[i:i+280],
                    "channelId": channelId
                })
            }
            ws.send(json.dumps(response))

    elif (patternAquarius.match(received_message["message"]["text"].lower())):
        html = requests.get(
            "https://www.astrology.com/horoscope/daily/aquarius.html").text[39300:]
        html=html[html.find("400\">")+5:]
        responseText = html[0:html.find("</span>")]
        for i in range(0,len(responseText),280):
            response = {
                "command": "message",
                "identifier": GATEWAY_IDENTIFIER,
                "data": json.dumps({
                    "action": "send_message",
                    "text": responseText[i:i+280],
                    "channelId": channelId
                })
            }
            ws.send(json.dumps(response))

    elif (patternPisces.match(received_message["message"]["text"].lower())):
        html = requests.get(
            "https://www.astrology.com/horoscope/daily/pisces.html").text[39300:]
        html=html[html.find("400\">")+5:]
        responseText = html[0:html.find("</span>")]
        for i in range(0,len(responseText),280):
            response = {
                "command": "message",
                "identifier": GATEWAY_IDENTIFIER,
                "data": json.dumps({
                    "action": "send_message",
                    "text": responseText[i:i+280],
                    "channelId": channelId
                })
            }
            ws.send(json.dumps(response))