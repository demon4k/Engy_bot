import telebot

bot = telebot.TeleBot("7643603752:AAF124-yn-rj88yqXDc_xV6zCUezCexlTm8")

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, "Я допоможу тобі покращити англійську мову через цікаві завдання та змагання з іншими користувачами! \n "
                                      "📚 Виконуй завдання з граматики, словникового запасу та читання! \n"
                                      "🏆 Змагайся за першість у таблиці лідерів та здобувай бали! \n\n"
                                      ""
                                      "Готовий показати свої знання та піднятися на вершину рейтингу? \n"
                                      "👇 Натискай кнопку \"Розпочати\" нижче та починай свій шлях до успіху! \n")

if __name__ == "__main__":
    bot.polling()

# Hello world