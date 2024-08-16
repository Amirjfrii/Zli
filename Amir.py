import telebot
import datetime
import time

bot_token = "7287542336:AAEPcE0xn6gPDFe0FJ5LAfvtEXOowPQkSFc"  #your bot token
bot = telebot.TeleBot(bot_token)
first_button = telebot.types.InlineKeyboardButton("افزودن به گروه", url="t.me/digijafarbot?startgroup=new")
markup = telebot.types.InlineKeyboardMarkup()
markup.add(first_button)


text = "[این است](t.me/pv_mooz)"
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, f"سلام {message.chat.first_name} عزیز به ربات مدیریت گروه خوش آمدید\nآیدی سازنده\n", reply_markup=markup)

@bot.message_handler(content_types=["new_chat_members"])
def new(m):
    bot.reply_to(m, f"کاربر {m.from_user.first_name}به گروه خوش آمدید")

@bot.message_handler(func= lambda m: m.text == "بن")
def ban(m):
    bot.ban_chat_member(m.chat.id, m.reply_to_message.from_user.id)
    bot.reply_to(m, "کاربر مورد نظر بن شد!")

bot.polling()
