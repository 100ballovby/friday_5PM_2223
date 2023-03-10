import telebot
import requests as r

bot = telebot.TeleBot('KEY')


def git_search(query, language):
    url = 'https://api.github.com/search/repositories'
    params = {'q': query,
              'l': language}
    res = r.get(url, params=params).json()
    message = ''
    for repo in res['items']:
        message += f'<a href="{repo["svn_url"]}">{repo["name"]}</a>\n'
    return message


answers = {
    'git': 'Введи запрос для поиска в формате "GIT Запрос Язык_Программирования" и я дам тебе ссылки на 5 случайных репозиториев',
    'help': 'Я умею искать по гитхабу и повторять слова за тобой. Чтобы узнать, как искать, напиши мне слово git',
}


@bot.message_handler(commands=['start', 'help', 'get_city'])
def commands(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Пока что я умею только повторять за тобой')
    elif message.text == '/help':
        bot.send_message(message.chat.id, answers['help'])


@bot.message_handler(content_types=['text'])  # декоратор
def repeat_message(message):
    if message.text.startswith('GIT'):
        msg = message.text.split()
        res = git_search(msg[1], msg[2])
        msg = "Вот, что я смог найти:\n" + res
        bot.send_message(message.chat.id, text=msg, parse_mode='html')
    else:
        bot.send_message(message.chat.id, 'Ты написал: ' + message.text)


if __name__ == '__main__':  # если запускается ИМЕННО ЭТОТ файл
    bot.polling()  # опрашивать сервер

