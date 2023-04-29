import telebot
import requests

bot = telebot.TeleBot("TOKEN") # здесь необходимо вставить токен вашего бота

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет, я бот, который выводит погоду. Для получения погоды, отправь мне свою локацию.")

@bot.message_handler(content_types=['location'])
def weather(message):
    lat = message.location.latitude
    lon = message.location.longitude
    api = "b0421a555a2be7a3d1f83538bd12ad32"
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={TOKEN}&units=metric' # здесь необходимо вставить ваш API ключ для OpenWeatherMap
    response = requests.get(url).json()
    temp = response['main']['temp']
    description = response['weather'][0]['description']
    city = response['name']

    bot.reply_to(message, f"Сейчас в городе {city} температура {temp}°C, {description}.")

bot.polling(none_stop=True)
