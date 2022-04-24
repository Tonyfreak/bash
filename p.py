import telebot
import requests

def telegram_bot_sendtext(bot_message):

   bot_token = "5289342558:AAEhXTwpk3p6qDjI_NLOx4gkOM4eTONmuXQ"
   bot_chatID = "1129722320"
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()


test = telegram_bot_sendtext("Testing Telegram bot")
print(test) 
   
   



'''bot = telebot.TeleBot("5289342558:AAEhXTwpk3p6qDjI_NLOx4gkOM4eTONmuXQ")
chat_id = "1129722320"

bot.send_message(chat_id, "Recon started!")


for i in range(30):
# Making a GET request
    url = "https://c98y45r2vtc000009psggrwxndyyyyyyb.interact.sh/"+str(i)
    r = requests.get(url)
    out = os.system('ls')
    print(out)'''

