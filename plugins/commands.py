from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
import random

Naruto=Client(
      "PYrogramBOT",
      bot_token="5236386119:AAEuqS-1EBximbdnNknN2506tWW052VL1mk",
      api_id="15316155",
      api_hash="c2340e29da60393bc3c96fa7c0870911"
)


ALL_PIC = [
 "https://telegra.ph/file/5f51546ad227831b96a38.jpg",
 "https://telegra.ph/file/56e2c12ed686eeb4513da.jpg",
 "https://telegra.ph/file/266fec5cf211151997303.jpg",
 "https://telegra.ph/file/13527c7b40976c1368cca.jpg"
]

@Naruto.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""π·π΄π {message.from_user.mention} πΌπ π½π°πΌπ΄ πΈπ <a href=https://t.me/NewPythonWorkBot>π½πππ½π½π βπβππΎβπΈπ</a>, π°π³π³ πΌπ΄ ππΎ ππΎππ π²π·π°π πΆππΎππΏ,π°π½π³ πΌπ°πΊπ΄ ππππ΄ π°π³πΌπΈπ½ π°π½π³ ππ΄π΄ πΌπ πΏπΎππ΄ππππ """,
        reply_markup=InlineKeyboardMarkup( [[
          InlineKeyboardButton ("πππππππ", url="https://t.me/ADHOLOKAMHD"),
          InlineKeyboardButton ("πππππππππ", url="https://t.me/+8WLTJKD-fH0zMzUx"),
          ],[
          InlineKeyboardButton ("π°πππππππ°", url="t.me/TEAM_KERALA"),
          InlineKeyboardButton ("ππ£πππ π£π₯π’π π’π§ππ’π‘", url="t.me/TEAM_KERALA"),
          ],[
          InlineKeyboardButton ("π΅οΈββοΈππ’π§ πππ©π΅οΈββοΈ", url="t.me/TEAM_KERALA"),
          ],[
          InlineKeyboardButton ("βοΈπππ§'π¦ π₯π’ππβοΈ", url="http://t.me/NewPythonWorkBot?startgroup=true"),
          InlineKeyboardButton ("π€ ππππ ππππππππ€ ", callback_data="start"),
          ],[
          InlineKeyboardButton ("β‘οΈπ¦π’π¨π₯ππ ππ’ππβ‘οΈ", callback_data="help"),
          InlineKeyboardButton ("π­ππ₯ππ π£π₯π’π π’π§ππ’π‘π­", url="t.me/TEAM_KERALA_2")
          ]]
          )
          
        )


@Naruto.on_message(filters.command("info"))
async def id_message(bot, message):
    text = f"""
β­ π΅πΈπππ π½π°πΌπ΄ - {message.from_user.first_name}
β π»π°ππ π½π°πΌπ΄ - {message.from_user.last_name}
π‘ πππ΄π π½π°πΌπ΄ - {message.from_user.username}
π πππ΄π πΈπ³ - {message.from_user.id}
ποΈ πππ΄π πΌπ΄π½ππΈπΎπ½ - {message.from_user.mention}"""


    await message.reply_text(text=text)

@Naruto.on_message(filters.group & filters.command("id"))
async def id(bot, message):
    text = f"""
π πΆππΎππΏ π½π°πΌπ΄ : {message.chat.title}
β‘ πΆππΎππΏ πππ΄ππ½π°πΌπ΄ : @{message.chat.username}
ποΈ πΆππΎππΏ πΈπ³ : {message.chat.id}
π πππ΄π πΈπ³ : {message.from_user.id}
ποΈ πππ΄π πΌπ΄π½ππΈπΎπ½: {message.from_user.mention}"""

    await message.reply_text(text=text)


@Naruto.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    if msg.data == "start":
     await msg.message.edit(
                text="""β― π²ππ΄π°ππΎπ: <a href="https://t.me/TEAM_KERALA_2">>π­ππππ πππ¨πππ¬π­</a>
β― π³π΄ππ΄π»πΎπΏπ΄π: <a href="https://t.me/TEAM_KERALA">π­πππ¨πππ¬ πππππ‘π­</a>
β― π»πΈπ±ππ°ππ: <a href="https://www.w3schools.com/python/">π£π¬π§ππ’π‘ πππ‘π§ππ₯</a>
β― πΏπππ·πΎπ½ ππππΎππΈπ°π»: <a href="https://www.w3schools.com/python/">π£π¬π§ππ’π‘ πππ‘π§ππ₯</a>
β― π³π°ππ° π±π°ππ΄:<a href="https://www.MongoDb.com/">ππ π’π‘ππ’ πππ</a>
β― π±πΎπ ππ΄πππ΄π: <a href="https://dashboard.heroku.com/">β‘πππ₯π’ππ¨β‘</a>
β― π±ππΈπ»π³ πππ°πππ: v2.01 [ π±π΄ππ° ]
β― ππΎπππ²π΄ π²πΎπ³π΄:  <a href="https://github.com/TEAM-FLUFFY/FluffyV1">ποΈπππππ π πποΈ</a>"""
     )

    elif msg.data == "help":
         await msg.message.edit(
             text="""<a href="https://github.com/TEAM-FLUFFY/FluffyV1">ποΈπππππ π πποΈ</a>"""
         )


Naruto.run()
