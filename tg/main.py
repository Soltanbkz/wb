import telegram
from WorkBench.settings import TELEGRAM_BOT_TOKEN

import asyncio
import telegram


async def get_group_id(token):
    bot = telegram.Bot(token=token)
    updates = await bot.get_updates()

    if updates:
        chat_id = updates[-1].message.chat.id
        return chat_id

    return None


# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
async def main():
    group_id = await get_group_id(TELEGRAM_BOT_TOKEN)

    if group_id:
        print(f"ID вашей закрытой группы: {group_id}")
    else:
        print("Не удалось получить ID закрытой группы")


asyncio.run(main())
