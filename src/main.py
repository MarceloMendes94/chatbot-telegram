from telegram.ext import CommandHandler, Filters, MessageHandler, Updater


TELEGRAM_TOKEN="1018999130:AAFgakuNExsE6pwNJgiyNOKgGVInslw-sF4"
BASE_API_URL="https://http.cat/"



def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ola sou um bot de teste.")

def conversa(update, context):
    text=update.message.text
    response=""

    if("oi"in text):
        response="ola sou um bot ainda não tenho uma IA"
    elif("tchau" in text):
        response="Tchau volte quando eu tiver uma IA"
    elif("tudo bem?"in text):
        response="Então estou querendo ser uma IA"

    if(response == ""):
        response="Desculpa eu não sei,mas jaja terei um script de aprendizado supervisionado."

    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def main():
    updater = Updater(token=TELEGRAM_TOKEN,use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler( CommandHandler('start', start))
    echo_handler = MessageHandler(Filters.text & (~Filters.command), conversa)
    dispatcher.add_handler(echo_handler)
   
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + Z to cancel.")
    main()
