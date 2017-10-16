"""
Created by anthony on 15.10.17
Main bot file
Only _register_ modules here (no logic)
Should just assemble and run bot
"""
from telegram.ext import Updater
from config import bot_config
from handlers import start_handler, echo_handler


def main():
    print(f'Starting {bot_config.BOT_NAME}')

    # handles events
    updater = Updater(token=bot_config.BOT_API_TOKEN)

    # registers handlers
    dispatcher = updater.dispatcher

    # handlers are invoked from top to bottom till first match
    dispatcher.add_handler(start_handler.start())
    dispatcher.add_handler(echo_handler.echo())

    # runs
    updater.start_polling()
    print('Bot has started')

    # listens for Ctrl-C on process to stop
    updater.idle()
    print('Bot has stopped')


if __name__ == '__main__':
    main()