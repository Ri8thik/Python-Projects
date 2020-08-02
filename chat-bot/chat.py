# this import is used to start a chatbot
from nltk.chat.util import Chat , reflections

# in this we can add the resonable answers

pairs = [
        ['(how are you|hii how are you|hi how are you )',['i am good sir what about you']],
        ['my name is (.*)',['hi %1 nice to talk to you ']],
        ['(hi|hello|hey|hoola|hola)',['hey there','hello there','hii there','hayy']],
        ['(.*) in (.*) is fun',['%1 in %2 is indeed fun']],
        ['(good|i am good|god|i am god)',['good to lissen sir']],
        ['(.*)(location|city)', ['haryana ,panipat']],
        ['(.*)(makes|made|build|make) you',['rithik sir make me using NLTK']],
        ['(.*)(weather|climate|weather condition|weather cond) in(.*)',['the weather in %3 is amazing like always']],
        ['(.*)help(.*)',['i can help you']],
        ['(.*)your name ?',['J.A.G.G.U']]


        
        ]




# it run the chatbot

chat =Chat(pairs, reflections)
#chat._substitute("you are amazing")
chat.converse()

