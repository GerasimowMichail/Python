from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def log(update: Update, context: CallbackContext):
    print(update)
    # {
    #     'message': {'date': 1670851391,
    #                 'supergroup_chat_created': False,
    #                 'group_chat_created': False,
    #                 'new_chat_members': [],
    #                 'channel_chat_created': False,
    #                 'caption_entities': [],
    #                 'entities': [{'length': 3,
    #                               'type': 'bot_command',
    #                               'offset': 0}],
    #                 'new_chat_photo': [],
    #                 'delete_chat_photo': False,
    #                 'message_id': 2747,
    #                 'chat': {'username': 'User1',
    #                          'first_name': 'User',
    #                          'id': 1111111111,
    #                          'type': 'private'},
    #                 'text': '/sum 15 25'
    #                 'photo': [],
    #                 'from': {'first_name': 'User',
    #                          'language_code': 'en',
    #                          'username': 'User1',
    #                          'is_bot': False,
    #                          'id': 1111111111}},
    #     'update_id': 703209650
    # }
    print(update.message.date)
    # 2022-12-12 16:18:52+00:00
    print(update.message.date.strftime('%d.%m.%Y %H:%M:%S'))
    # 12.12.2022 16:18:52
    file = open('db.csv', 'a', encoding='utf-8')
    file.write(f'{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
    file.close()    

# message.date.strftime('%H:%M:%S')

