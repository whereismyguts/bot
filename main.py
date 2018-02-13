from telegram.ext import Updater, CommandHandler


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


def main():
    updater = Updater('412172586:AAFbIXMb0Gm8nci-cBNq7eS6CfGbNPetmU8')

    updater.dispatcher.add_handler(CommandHandler('hello', hello))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()
