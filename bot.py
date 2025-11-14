"""Simple Telegram bot implemented with pyTelegramBotAPI."""

import os

import telebot

# Expect BOT_TOKEN to come from environment variables in deployment.
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("Set the BOT_TOKEN environment variable before running the bot.")

bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)

START_TEXT = (
    "🎉 Привет, именинник! Сегодня твой день рождения, и твоя любимая девушка "
    "подготовила мини-квест. Нажимай на кнопку Open внизу и бегом проходи тест, "
    "чтобы получить от нее подарок! 🎁"
)


@bot.message_handler(commands=["start"])
def handle_start(message: telebot.types.Message) -> None:
    """Send the greeting when /start is triggered."""
    bot.send_message(message.chat.id, START_TEXT)


if __name__ == "__main__":
    # polling with none_stop=True keeps the bot alive on hosts like Railway.
    bot.polling(none_stop=True, interval=0, timeout=60)
