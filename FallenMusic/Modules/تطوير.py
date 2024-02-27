import asyncio
import random
import os
import time
import requests
from random import  choice, randint
from pyrogram import Client, filters
from FallenMusic.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from FallenMusic import app


@app.on_message(
    command(["سورس","السورس","المطور"])
    & filters.group
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/94fa4bb62424ea712eaa2.jpg",
        caption=f"""-| مطور السورس \n-| قناة المطور""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- مطور السورس .", url=f"https://t.me/T_5_G"),
                ],
                [
                   InlineKeyboardButton(
                        "- قناة المطور ", url=f"https://t.me/VVV5P"),
                ],       
            ]
        ),
    )


@app.on_message(
    command(["جاك","البوت","بوت"])
    & filters.group)
def greet_user(client, message):
    client.send_message(
        chat_id=message.chat.id,
        text="مرحبًا! كيف يمكنني مساعدتك اليوم؟"
    )
