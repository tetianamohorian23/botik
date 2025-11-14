"""Simple Telegram bot implemented with pyTelegramBotAPI."""

import os

import telebot

# WARNING: keeping tokens in source control is insecure; environment variables are preferred.
if not BOT_TOKEN or BOT_TOKEN.startswith("8207707178") and len(BOT_TOKEN) < 40:
    raise RuntimeError("Provide a valid Telegram bot token before running the bot.")

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
    # infinity_polling keeps reconnecting automatically when Telegram drops the link.
    bot.infinity_polling(skip_pending=True)
