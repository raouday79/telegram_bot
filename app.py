# import everything
import re
from flask import Flask, request
import telegram
from telebot.credentials import bot_token, bot_user_name,URL
import telebot.message as message
global bot
global TOKEN
TOKEN = bot_token
print(TOKEN)
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

#pd = pd.read_csv('./user.csv')
@app.route('/', methods=['POST','GET'])
def respond():
   # retrieve the message in JSON and then transform it to Telegram
   resp = request.get_json()
   #users.
   print(resp)
   update = telegram.Update.de_json(request.get_json(force=True), bot)
   print(update)
   chat_id = update.message.chat.id
   print('Chat Id ',chat_id)
   #from_chat = update.message.from.id
   msg_id = update.message.message_id

   # Telegram understands UTF-8, so encode text for unicode compatibility
   text = update.message.text.encode('utf-8').decode()
   # for debugging purposes only
   print("got text message :", text)
   # the first time you chat with the bot AKA the welcoming message
   if text == "/start":
       # print the welcoming message
       bot_welcome = '''
       Welcome to the <b>UR</b> Bot \n For live New /liveNews \n For Cricket Score /cricketscore 
       '''
       # send the welcoming message
       bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id,parse_mode='html')
       return 'ok'
   else:
       mesg = message.getMessage(text)
       bot.sendMessage(chat_id=chat_id, text=mesg, reply_to_message_id=msg_id, parse_mode='html')
       return 'ok'
   try:
           # clear the message we got from any non alphabets
           text = re.sub(r"\W", "_", text)
           # create the api link for the avatar based on http://avatars.adorable.io/
           url = "https://api.adorable.io/avatars/285/{}.png".format(text.strip())
           # reply with a photo to the name the user sent,
           # note that you can send photos by url and telegram will fetch it for you
           bot.sendPhoto(chat_id=chat_id, photo=url, reply_to_message_id=msg_id)
   except Exception:
           # if things went wrong
           bot.sendMessage(chat_id=chat_id, text="There was a problem in the name you used, please enter different name", reply_to_message_id=msg_id)

   return 'ok'

@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
   temp = '{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN)
   print('Link',temp)
   url = 'https://api.telegram.org/bot'+TOKEN+'/setWebHook?url='+URL
   s = bot.setWebhook(url)
   if s:
       return "webhook setup ok"
   else:
       return "webhook setup failed"


@app.route('/test',methods=['GET'])
def indexTest():
   return 'Working'


if __name__ == '__main__':
   app.run(threaded=True,port=4050)