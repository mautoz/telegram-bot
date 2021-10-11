#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
This bot was inspited by
https://www.codementor.io/@karandeepbatra/part-1-how-to-create-a-telegram-bot-in-python-in-under-10-minutes-19yfdv4wrq


This is my first test using bots. I decided to recommend Donnie Darko songs!

Commands:
    /bunnymen
    /tears
    /oingo
    /joy
    /gary
    /inxs
    /random
    /help
"""
import logging
import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


soundtrack = [
    "Echo & The Bunnymen - The Killing Moon\nhttps://youtu.be/LWz0JC7afNQ",
    "Tears For Fears - Head Over Heels\nhttps://youtu.be/CsHiG-43Fzg",
    "Oingo Boingo - Stay\nhttps://youtu.be/DwRnW89EsxI",
    "Joy Division - Love Will Tear Us Apart\nhttps://youtu.be/zuuObGsB0No",
    "Gary Jules - Mad World\nhttps://youtu.be/PvPkLG-tvzM",
    "INXS - Never Tear Us Apart\nhttps://youtu.be/AIBv2GEnXlc",
]


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text("Type /help if it's your first time!")


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        " \
        /bunnymen \
        /tears \
        /oingo \
        /joy \
        /gary \
        /inxs \
        /random \
    "
    )


def bunnymen(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        "Echo & The Bunnymen - The Killing Moon\n \
            https://youtu.be/LWz0JC7afNQ"
    )


def tears(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        "Tears For Fears - Head Over Heels\n \
            https://youtu.be/CsHiG-43Fzg"
    )


def oingo(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        "Oingo Boingo - Stay\n \
            https://youtu.be/DwRnW89EsxI"
    )


def joy(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        "Joy Division - Love Will Tear Us Apart\n \
            https://youtu.be/zuuObGsB0No"
    )


def gary(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        "Gary Jules - Mad World\n \
            https://youtu.be/PvPkLG-tvzM"
    )


def inxs(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        "INXS - Never Tear Us Apart\n \
            https://youtu.be/AIBv2GEnXlc"
    )


def random_sound(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(random.choice(soundtrack))


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Here is where you will put your token
    updater = Updater("Insert your token here", use_context=True)
    dp = updater.dispatcher

    # My commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("bunnymen", bunnymen))
    dp.add_handler(CommandHandler("tears", tears))
    dp.add_handler(CommandHandler("oingo", oingo))
    dp.add_handler(CommandHandler("joy", joy))
    dp.add_handler(CommandHandler("gary", gary))
    dp.add_handler(CommandHandler("inxs", inxs))
    dp.add_handler(CommandHandler("random", random_sound))

    # If you type an unknown command echo will be called.
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Errors
    dp.add_error_handler(error)

    # Starting the bot
    updater.start_polling()

    # If you want to stop, press CTRL+C
    updater.idle()


if __name__ == "__main__":
    main()
