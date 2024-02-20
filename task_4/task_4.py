import config
import telebot
import pyodbc
import sys
from datetime import date

con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=.\messages.accdb;'

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def writing_messages_to_database(message): 
    conn = pyodbc.connect(con_string)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages VALUES (?, ?)", (message.text, date.today()))
    conn.commit()


def create_access_table():
    conn = pyodbc.connect(con_string)
    cursor = conn.cursor()
    table_name = 'messages'
    create_table = f'CREATE TABLE {table_name} (message TEXT, departure_date TEXT)'

    # Create table if not exists
    try:
        cursor.execute(create_table)
    except pyodbc.Error as e:
        if f"Table '{table_name}' already exists" not in str(e):
            sys.exit(e)
    
    conn.commit()


if __name__ == '__main__':
     create_access_table()
     bot.infinity_polling()




