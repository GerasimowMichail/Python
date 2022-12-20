import os

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
# from bot_commands import hi_command, time_command, help_command, sum_command
import bot_commands as bc
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('tg_token')

updater = Updater(TOKEN)
# /sum 7 5
updater.dispatcher.add_handler(CommandHandler('hi', bc.hi_command))
updater.dispatcher.add_handler(CommandHandler('time', bc.time_command))
updater.dispatcher.add_handler(CommandHandler('help', bc.help_command))
updater.dispatcher.add_handler(CommandHandler('sum', bc.sum_command))
updater.dispatcher.add_handler(CommandHandler('csum', bc.csum_command))
updater.dispatcher.add_handler(CommandHandler('cdeff', bc.cdeff_command))
updater.dispatcher.add_handler(CommandHandler('deff', bc.deff_command))
updater.dispatcher.add_handler(CommandHandler('mult', bc.mult_command))
updater.dispatcher.add_handler(CommandHandler('cmult', bc.cmult_command))
updater.dispatcher.add_handler(CommandHandler('cdiv', bc.cdiv_command))
updater.dispatcher.add_handler(CommandHandler('div', bc.div_command))



print('server start')
updater.start_polling()
updater.idle()