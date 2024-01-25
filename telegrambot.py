import telebot

bot = telebot.TeleBot("6355004816:AAF1mtghMcPgndqHut1lm5yukothOj5hIRs")

first_button = telebot.types.InlineKeyboardButton("Button 1",url="https://t.me/aglhiarz")
second_button = telebot.types.InlineKeyboardButton("Button 2",callback_data="Hi")

markup = telebot.types.InlineKeyboardMarkup(row_width=1)
markup.add(first_button, second_button)

@bot.callback_query_handler(func= lambda call:True)
def callback_query(call):
    # bot.send_message(call.message.chat.id, "You Clicked on me!!")
    # bot.reply_to(call.message, "Hey look what happened.")
    bot.answer_callback_query(call.id, "Ding Ding")

@bot.message_handler(commands= ['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hi", reply_markup=markup)

key_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
key_markup.add("One", "Two", "Three")

@bot.message_handler(commands= ['help'])
def send_help(message):
    bot.reply_to(message, "What can i do?",reply_markup=key_markup)

@bot.message_handler()
def keyboard(message):
    if message.text == "One":
        bot.send_message(message.chat.id, "Clicked on button <one>")

    elif message.text == "Two":
        bot.send_message(message.chat.id, "Clicked on button <two>")
    
    elif message.text == "Three":
        bot.send_message(message.chat.id, "Clicked on button <three>")


bot.infinity_polling(timeout=120)