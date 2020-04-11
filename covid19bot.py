import logging
import telegram
import json
import jdatetime
import datetime
import numbers
import decimal
import TelegramRepository as dal
from persiantools import digits
from functools import lru_cache


from covid import Covid

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(filename="telegrambot.log", format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def persist_user_info(update):
    from_user = update.effective_chat
    # insert user to db
    dal.insertNewUser(from_user.id, from_user.first_name, from_user.last_name, from_user.username, from_user.link)
    # insert user command to db
    dal.insertUserCommand(from_user.id, update.message.text)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    message = ' Hi!'
    message += '\nLive statistics and coronavirus news tracking the number of confirmed cases, recovered patients, tests, and death toll due to the COVID-19 coronavirus from  https://www.worldometers.info/coronavirus/'
    message += '\n\nbot commands list:'
    message += '\n/world'
    message += '\n/iran'
    message += '\n/usa'
    message += '\n/italy'
    message += '\n/germany'
    message += '\n/spain'
    message += '\n/france'
    message += '\n/uk'
    message += '\n/canada'
    update.message.reply_text(message)


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    persist_user_info(update)
    update.message.reply_text(update.message.text)


#@lru_cache(maxsize=5)
def _get_world_stat():
    covid = Covid(source="worldometers")
    message = ' **WORLD:**'
    message += f'\nTotal cases: {covid.get_total_active_cases():,}'
    message += f'\nConfirmed :{covid.get_total_confirmed_cases():,}' 
    message += f'\nRecovered  : {covid.get_total_recovered():,}' 
    message += f'\nDeaths  : {covid.get_total_deaths():,}'
    return message

def _world(context, update):
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    message = _get_world_stat()
    
    update.message.reply_text(message, parse_mode=telegram.ParseMode.MARKDOWN_V2)

def world(update, context):
    persist_user_info(update)
    _world(context, update)


#@lru_cache(maxsize=5)
def countries(update, context):
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    covid = Covid(source="worldometers")
    countries = covid.list_countries()
    message = ' '
    for val in countries:
        message += f'\n{val}'
    message += f'\n\nDate: {str(datetime.datetime.now())}'
    update.message.reply_text(message)


#@lru_cache(maxsize=5)
def _get_iran_stat():
    covid = Covid(source="worldometers")
    iran_cases = covid.get_status_by_country_name("iran")
    message = ' '
    for key, val in iran_cases.items():
        message += f'\n{translate_to_persian(key)} : {digits.en_to_fa(str(val))}'
        if(key == 'country'):
            message += '\n'
   
    return message

def _iran(context, update):
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    message = _get_iran_stat()
    message += f'\n\nتاریخ: {digits.en_to_fa(str(jdatetime.date.today()))}'
    update.message.reply_text(message)


def iran(update, context):
    persist_user_info(update)

    _iran(context, update)


#@lru_cache(maxsize=5)
def _get_data_stat(country):
    covid = Covid(source="worldometers")
    iran_cases = covid.get_status_by_country_name(country)
    message = ' '
    for key, val in iran_cases.items():
        if isinstance(val, numbers.Number):
            message += f'\n{key} : {val:,}'
        else:
            message += f'\n{key} : {str(val)}'
        if(key == 'country'):
            message += '\n'
    
    return message


def _get_data(context, country, update):
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    message = _get_data_stat(country)
    message += f'\n\nDate: {str(datetime.datetime.now())}'
    update.message.reply_text(message)

def get_data(context, update, country):
    persist_user_info(update)
    _get_data(context, country, update)

def china(update, context):
    get_data(context, update, "china")

def usa(update, context):
    get_data(context, update, "usa")

def spain(update, context):
    get_data(context, update, "spain")

def italy(update, context):
    get_data(context, update, "italy")

def germany(update, context):
    get_data(context, update, "germany")

def france(update, context):
    get_data(context, update, "france")

def uk(update, context):
    get_data(context, update, "uk")


def turkey(update, context):
    get_data(context, update, "turkey")


def belgium(update, context):
    get_data(context, update, "belgium")


def switzerland(update, context):
    get_data(context, update, "switzerland")


def netherlands(update, context):
    get_data(context, update, "netherlands")


def canada(update, context):
    get_data(context, update, "canada")


def brazil(update, context):
    get_data(context, update, "brazil")


def portugal(update, context):
    get_data(context, update, "portugal")


def austria(update, context):
    get_data(context, update, "austria")

def skorea(update, context):
    get_data(context, update, "s. korea")

def israel(update, context):
    get_data(context, update, "israel")


def sweden(update, context):
    get_data(context, update, "sweden")


def ireland(update, context):
    get_data(context, update, "ireland")

def chile(update, context):
    get_data(context, update, "chile")

def australia(update, context):
    get_data(context, update, "australia")


def poland(update, context):
    get_data(context, update, "poland")


def denmark(update, context):
    get_data(context, update, "denmark")

def czechia(update, context):
    get_data(context, update, "czechia")

def japan(update, context):
    get_data(context, update, "japan")

def romania(update, context):
    get_data(context, update, "romania")

def peru(update, context):
    get_data(context, update, "peru")

def ecuador(update, context):
    get_data(context, update, "ecuador")

def pakistan(update, context):
    get_data(context, update, "pakistan")

def malaysia(update, context):
    get_data(context, update, "malaysia")

def saudi_arabia(update, context):
    get_data(context, update, "saudi arabia")

def indonesia(update, context):
    get_data(context, update, "indonesia")

def mexico(update, context):
    get_data(context, update, "mexico")

def luxembourg(update, context):
    get_data(context, update, "luxembourg")

def serbia(update, context):
    get_data(context, update, "serbia")

def uae(update, context):
    get_data(context, update, "uae")



def translate_to_persian(key):
    if(key == 'country'):
        return 'کشور'
    if(key == 'confirmed'):
        return 'تایید شده'
    if(key == 'new_cases'):
        return 'ابتلای جدید'
    if(key == 'deaths'):
        return 'فوتی'
    if(key == 'recovered'):
        return 'بهبود یافته'
    if(key == 'active'):
        return 'مبتلا'
    if(key == 'critical'):
        return 'بحرانی'
    if(key == 'new_deaths'):
        return 'فوتی جدید'
    if(key == 'total_tests'):
        return 'مجموع تست'
    if(key == 'total_tests_per_million'):
        return 'مجموع تست در میلیون نفر'
    if(key == 'total_cases_per_million'):
        return 'تعداد مبتلا در میلیون نفر'
    if(key == 'total_deaths_per_million'):
        return 'تعداد فوتی در میلیون نفر'


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1216224494:AAGcBBToKyAuUI_53lyxX4vxUFATKHCPmi0", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("world", world))
    dp.add_handler(CommandHandler("countries", countries))
    dp.add_handler(CommandHandler("iran", iran))
    dp.add_handler(CommandHandler("usa", usa))
    dp.add_handler(CommandHandler("spain", spain))
    dp.add_handler(CommandHandler("italy", italy))
    dp.add_handler(CommandHandler("germany", germany))
    dp.add_handler(CommandHandler("france", france))
    dp.add_handler(CommandHandler("uk", uk))
    dp.add_handler(CommandHandler("turkey", turkey))
    dp.add_handler(CommandHandler("belgium", belgium))
    dp.add_handler(CommandHandler("switzerland", switzerland))
    dp.add_handler(CommandHandler("netherlands", netherlands))
    dp.add_handler(CommandHandler("canada", canada))
    dp.add_handler(CommandHandler("brazil", brazil))
    dp.add_handler(CommandHandler("china", china))
    dp.add_handler(CommandHandler("uae", uae))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
