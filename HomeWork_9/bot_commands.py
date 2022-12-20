from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

from spy import *

def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')

def help_command(update: Update, context: CallbackContext):
    log(update, context)
    help_msg = '/hi - приветствие\n/time - показать текущее время\n' \
               '/help - отобразить эту справку\n' \
               '/sum 5 2 - получение суммы чисел 5 и 2 \n'\
               '/div 5 2 - получение суммы чисел 5 и 2 \n'\
               '/mult 5 2 - получение суммы чисел 5 и 2 \n'\
               '/deff 5 2 - получение суммы чисел 5 и 2 \n' \
               '/csum 5 2 - получение суммы чисел 5 и 2 \n' \
               '/cdeff 5 2 - получение суммы чисел 5 и 2 \n'\
               '/cdiv 5 2 - получение суммы чисел 5 и 2 \n' \
               '/cdeff 5 2 - получение суммы чисел 5 и 2 \n'\
                 
            
    update.message.reply_text('/hi\n/help\n/sum\n/div\n/mult\n/deff\n/csum\n/cdeff\n/cdiv\n/cmult')

#  /time
def time_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')

# /sum 12 25
def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # '/sum', '12+3j', '25'
    x = float(items[1])
    y = float(items[2])
    update.message.reply_text(f'{x} + {y} = {x + y}')

# /sum 12 25
def deff_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # '/sum', '12+3j', '25'
    x = float(items[1])
    y = float(items[2])
    update.message.reply_text(f'{x} - {y} = {x - y}')
    
def mult_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # '/sum', '12+3j', '25'
    x = float(items[1])
    y = float(items[2])
    update.message.reply_text(f'{x} * {y} = {x * y}')
    
def div_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # '/sum', '12+3j', '25'
    x = float(items[1])
    y = float(items[2])
    update.message.reply_text(f'{x} / {y} = {x / y}')


# /csum 12 25
def csum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # '/sum', '12+3j', '25'
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x} + {y} = {x + y}')
    
def cdeff_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # '/sum', '12+3j', '25'
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x} - {y} = {x - y}')

def cdiv_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # '/sum', '12+3j', '25'
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x} / {y} = {x / y}')

def cmult_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # '/sum', '12+3j', '25'
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x} * {y} = {x * y}')

