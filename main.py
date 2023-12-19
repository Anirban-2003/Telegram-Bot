import telegram.ext


def start(update, context):
    update.message.reply_text("Hello!To use Ani_bot enter /help or use the menu")


def help(update, context):
    update.message.reply_text("""
    The following commands are avilable:

    /test  -> Chegg Computer Science Test ।। Chegg Subject Test
    /earn -> Earning 1.5 lakh in Chegg Computer Science || Computer Science Test Offer
    /hacks -> Auto refresh - chegg hack to save time
    /TDS -> Chegg TDS return || ITR filing
    /reel -> Interview of a successful Chegg Expert - 100 questions per day
    /contact -> contact me if you want to pass in any subject.
     """)


def test(update, context):
    update.message.reply_text("link : https://www.youtube.com/watch?v=dN-ZAq26aZU ")


def earn(update, context):
    update.message.reply_text("link : https://www.youtube.com/watch?v=8Z3yAm-oKqU&t=1s")


def hacks(update, context):
    update.message.reply_text("link : https://www.youtube.com/watch?v=3wJJE7QP0xo")


def TDS(update, context):
    update.message.reply_text("link : https://www.youtube.com/watch?v=yiXDze-bmmQ&t=1s")


def reel(update, context):
    update.message.reply_text("link : https://www.youtube.com/shorts/lpv8IKNWmCM")


def contact(update, context):
    update.message.reply_text("You can contact on the official mail id d11legendkiller@gmail.com")


def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text}, use the commands using /")


Token = ("Telegram bot token")
# print(bot.get_me())
updater = telegram.ext.Updater("Telegram bot token", use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start', start))
disp.add_handler(telegram.ext.CommandHandler('help', help))
disp.add_handler(telegram.ext.CommandHandler('test', test))
disp.add_handler(telegram.ext.CommandHandler('earn', earn))
disp.add_handler(telegram.ext.CommandHandler('hacks', hacks))
disp.add_handler(telegram.ext.CommandHandler('TDS', TDS))
disp.add_handler(telegram.ext.CommandHandler('reel', reel))
disp.add_handler(telegram.ext.CommandHandler('contact', contact))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
updater.start_polling()
updater.idle()
