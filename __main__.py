from aiogram.utils import executor
from bot_telegram import dp
from handlers.Client.Client import register_handlers_client
from handlers.Client.Client_settings import register_handlers_client_settings
from handlers.Client.Settings_window import register_handlers_settings_window
from database import db_create, db_test

register_handlers_client(dp)
register_handlers_client_settings(dp)
register_handlers_settings_window(dp)

async def on_start_up(_):
    print('The bot is running')
    db_test.connect_db()
    db_create.CT_UserInformation()
    db_create.CT_UserSettings()
    db_create.CT_UserClearSettings()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start_up)