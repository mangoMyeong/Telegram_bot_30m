import telegram
import asyncio
import schedule
import time
import pytz
import datetime

token = "6978046714:AAFXlCcOBrnc21sho1Od-UhBeY03yYrIJlg"
# Bot : sweetmango_bot
# token : 6978046714:AAFXlCcOBrnc21sho1Od-UhBeY03yYrIJl 
# chat_id : 6971784658
# channel : sw_2023_test02
bot = telegram.Bot(token = token)
public_chat_name = "@sw_2023_test02"

async def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))

    if now.hour >=23 or now.hour <=6:
        return

    id_channel = await bot.sendMessage(chat_id = public_chat_name, text = "그대 어떻게 살 것인가?")
    print(id_channel)

async def main():
    while True:
        await job()
        await asyncio.sleep(1800)

if __name__ == "__main__":
    asyncio.run(main())