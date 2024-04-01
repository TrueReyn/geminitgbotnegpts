# This scripts contains use cases for simple bots

import google.generativeai as genai

from pyrogram import Client, filters, enums
from pyrogram.types import Message

API_KEY="AIzaSyCVdT8q_rJdmv_B354EtXuhmdW5vBFdDXQ"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-pro")

API_ID = "21845506"
API_HASH = '4bbf9dfd9e070499745f843ebf7c7cce'
BOT_TOKEN = '7187721092:AAF-beUsw9CL8Fcvb8FNdfRG4iUEBYzVfgQ'

app = Client("gemini_ai", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.command("start") & filters.private)
async def start(_, message):
        chat = model.start_chat()
        prompt = "Hi"
        response = chat.send_message(prompt)
    
        await message.reply_text(f"{response.text}", parse_mode=enums.ParseMode.MARKDOWN)

@app.on_message(filters.command("ask") & filters.private)
async def say(_, message: Message):
    try:
        i = await message.reply_text("<code>Please Wait...</code>")

        if len(message.command) > 1:
         prompt = message.text.split(maxsplit=1)[1]
        elif message.reply_to_message:
         prompt = message.reply_to_message.text
        else:
         await message.reply_text(
            f"<b>Usage: </b><code>/ask [prompt/reply to message]</code>"
        )
         return
    
        chat = model.start_chat()
        response = chat.send_message(prompt)
        i.delete()
    
        await message.reply_text(f"**Question:**`{prompt}`\n**Answer:** {response.text}", parse_mode=enums.ParseMode.MARKDOWN)
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app.run()
