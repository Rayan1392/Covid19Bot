import pyodbc
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

server = 'localhost'
database = 'TelegramBotDB'
username = 'sa'
password = 'password'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


def insertNewUser(id, firstName, lastName, userName, link):

    logger.info("inserting new user to TelegramUser table")
    tsql = "IF NOT EXISTS(SELECT 1 FROM [dbo].[TelegramUsers] WHERE TelegramId = ?) BEGIN INSERT INTO [dbo].[TelegramUsers]([TelegramId],[FirstName],[LastName],[UserName],[link]) VALUES (?,?,?,?,?) END;"

    with cursor.execute(tsql, id,id,firstName,lastName,userName,link):
        logger.info('Successfully Inserted!')



def insertUserCommand(id, msg):

    logger.info("inserting new message to TelegramUserMessage table")
    tsql = "INSERT INTO [dbo].[TelegramUserMessage] ([TelegramId],[Command]) VALUES (?, ?);"

    with cursor.execute(tsql, id, msg):
        logger.info('Successfully Inserted!')