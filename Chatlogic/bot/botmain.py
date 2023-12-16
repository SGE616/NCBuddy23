'''
    NC Buddy code
'''

class NCbuddy:
    def __init__(self) -> None:
        self.response = ''

    def process_chat_message(self,query) -> str:
        self.query = query
        # print(type(query))
        self.response = 'Sorry, didn\'t quite catch that'
        # print(self.query)
        self.query = str.lower(self.query)
        if self.query == 'hi' or self.query == 'hello':
            self.response = 'Hi NC Buddy here... how is your day. Is there aything I can assist you with'
        elif self.query == 'thanks' or self.query == 'thank you':
            self.response = 'Your\'e Welcome. Thanks for Reaching out to NCBUDDY. Hope I was of help. the quick brown fox jumps over the lazy dog.'
        
        return self.response