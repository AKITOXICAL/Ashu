from pyrogram import filters
import random
from VegetaRobot import pgram

import VegetaRobot.modules.fun_strings as fun

IMG= "https://telegra.ph/file/2148458205e9f278ed12c.jpg"

@pgram.on_message(filters.command("hi"))
async def hmm(_, message):
    await message.reply_photo(random.choice(IMG,fun.WISH)
                                                        
   ) 
    
__mod_name__ = "Wish🎊"
__help__ = """
- /Wish: your wish
"""
