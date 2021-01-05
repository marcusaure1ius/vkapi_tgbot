from bot_loader import bot
from config import config
from datetime import datetime

TG_ADMIN_ID = config.TG_ADMIN_ID

# async def send_startup_message_to_admin(dp):
#     await bot.send_message(chat_id=TG_ADMIN_ID, text=f'Бот запущен {datetime.now()}')

# async def send_shutdown_message_to_admin(dp):
#     await bot.send_message(chat_id=TG_ADMIN_ID, text=f'Бот остановлен {datetime.now()}')
#     await bot.close()

if __name__ == "__main__":
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp)
    # , on_startup=send_startup_message_to_admin, on_shutdown=send_shutdown_message_to_admin)