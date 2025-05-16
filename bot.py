import json
from messages import *
from reminders import *
from follow import *
from tips import *

class Bot:
    @classmethod
    def handle_follow(cls, ws, received_message, channelId):
        usernameCount(ws, received_message, channelId)
        followMessage(ws, received_message, channelId)

    @classmethod
    def handle_messages(cls, ws, received_message, channelId):
        botMenu(ws, received_message, channelId)
        rps(ws, received_message, channelId)
        rupaul(ws, received_message, channelId)
        horoscope(ws, received_message, channelId)

    @classmethod    
    def handle_reminders(cls, ws, channelId):
        dropin(ws, channelId)

    @classmethod
    def handle_tips(cls, ws, received_message, channelId):
        tipMessage(ws, received_message, channelId)

        

                


        