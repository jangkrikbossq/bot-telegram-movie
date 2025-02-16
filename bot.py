import telebot
import requests
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def send_movie_link(message):
    movie_name = message.text.lower()
    landing_page = f"http://free.moviedate.top/p/redirecting.html?film={movie_name.replace(' ', '+')}"
    bot.reply_to(message, f"🎬 Klik link ini untuk menonton {movie_name}:\n🔗 {landing_page}")

bot.polling()