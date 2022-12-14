import os
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
    CallbackQuery,
)
from pyrogram import Client, filters
from pyrogram.errors import MessageNotModified
from dotenv import load_dotenv
from pyromod import listen 

load_dotenv()


Bot = Client(
    name="confess",
    bot_token=os.environ.get("BOT_TOKEN", "5626754813:AAEQD6i4If1huN3Na_Fk5kF61phaTK5k7Wo"),
    api_id=int(os.environ.get("API_ID", "23693414")),  # type: ignore
    api_hash=os.environ.get("API_HASH", "7886b6a15d0a1a06c7feeaeeb6ad6210"),
)
KR=-1001847941518
Start_text = """<i>Hallo! [Official Fantasy](https://t.me/officialfantasybot) akan membantumu untuk mengirimkan pesan secara anonim ke channel @fvconfess,Silakan Klik tombol <b>ð° Menu ð°</b> Untuk Melakunkan Menfes/Biro jodoh.

Sebelum menggunakan silakan baca rules terlebih dahulu yað¥°</i>

<b>Butuh bantuan? Hubungi</b> @phobiakaliann"""
KONTOL = "https://telegra.ph/file/1075382996efe8d8dcb15.jpg"
HOME_TEXT = """
<b>ðª Confess - Untuk Confess.
ð£ Kritik - Untuk mengkritik admin.</b>
<i>Klik tombol dibawah sesuai yang kamu mau</i>
"""

@Bot.on_message(filters.command(["start"]))
async def start(_, update: Message):
    await update.reply_photo(
        photo=KONTOL,
        caption=Start_text,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("âï¸ Rules", callback_data="rules"),
                    InlineKeyboardButton("Penjelasan ð", callback_data="penjelasan"),
                ],
                [
                    InlineKeyboardButton("ð° Menu ð°", callback_data="home_ban"),
                ],
            ]
        )
    )
    
RULES_TEXT = """ð£ï¸ RULES Official Fantasy

â PROMOSI TANPA IZIN
â UP 18+ TANPA IZIN
â JUALAN TANPA IZIN
â UP LINK TANPA IZIN

ð£ï¸ RESIKO AUTO BAN"""

@Bot.on_callback_query(filters.regex("rules"))
async def rulescb(_, query: CallbackQuery):
  await query.message.delete()
  await Bot.send_photo(query.message.chat.id,
                       photo=KONTOL,
                       caption=RULES_TEXT,
                       reply_markup=InlineKeyboardMarkup(
                         [
                           [
                             InlineKeyboardButton("ð Back", callback_data="cbstart"),
                           ],
                         ]
                       ),
                      )  
PENJELASAN_TEXT = """
<b>APA ITU MENFESS?</b>
ð Berdasarkan penelusuran di media sosial, istilah menfess kerap digunakan ketika seseorang ingin mengungkapkan sesuatu kepada orang lain atau semua orang secara anonim

<b>APA ITU BIRO JODOH?</b>
ð Berdasarkan Kamus besar, istilah biro jodoh adalah badan usaha jasa untuk menjodohkan pria atau wanita.

<b>APA ITU KRITIK?</b>
ð Kritik itu adalah kecaman atau tanggapan, kadang-kadang disertai uraian dan pertimbangan baik buruk thd suatu hasil karya, pendapat, dsb; (nomina).
"""
@Bot.on_callback_query(filters.regex("penjelasan"))
async def penjelasan(_, query: CallbackQuery):
  await query.message.delete()
  await Bot.send_photo(query.message.chat.id,
                       photo=KONTOL,
                       caption=PENJELASAN_TEXT,
                       reply_markup=InlineKeyboardMarkup(
                         [
                           [
                             InlineKeyboardButton("ð Back", callback_data="cbstart"),
                           ],
                         ]
                       ),
                      )  
    
@Bot.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
  await query.message.delete()
  await Bot.send_photo(query.message.chat.id,
                       photo=KONTOL,
                       caption=Start_text,
                       reply_markup=InlineKeyboardMarkup(
                         [
                           [
                             InlineKeyboardButton("âï¸ Rules", callback_data="rules"),
                             InlineKeyboardButton("Penjelasan ð", callback_data="penjelasan"),
                           ],
                           [
                             InlineKeyboardButton("ð° Menu ð°", callback_data="home_ban"),
                           ],
                         ]
                       ),
                      )
    
@Bot.on_callback_query(filters.regex("home_ban"))
async def home_ban(_, query: CallbackQuery):
  await query.message.delete()
  await Bot.send_photo(query.message.chat.id,
                       photo=KONTOL,
                       caption=HOME_TEXT,
                       reply_markup=InlineKeyboardMarkup(
                         [
                           [
                             InlineKeyboardButton("ð£ Kritik", callback_data="cbkritik"),
                             InlineKeyboardButton("Confess ðª", callback_data="cbconfess"),
                           ]
                         ]
                       ),
                      ) 
PVA=-1001847941518    
@Bot.on_callback_query(filters.regex("cbkritik"))
async def cbkritik(client, query: CallbackQuery):
  await query.message.delete()  
  user_id = query.from_user.id
  Tujuan = await client.ask(user_id, 'ð£ <b>Silakan ketik apa yang kamu ingin sampaikan kepada admin.</b>', filters=filters.text, timeout=30)
  if "/" in Tujuan.text:
    kri = await client.ask(user_id, '<b>â ï¸ Terjadi kesalahan.</b>\n__Ketikan apa yang kamu ingin katakan kepada admin__')
  else:
    kri = Tujuan
  await client.send_message(PVA, f"from {query.from_user.mention}\nisi : {kri.text}")
  await client.send_message(query.from_user.id, "Kritik kamu telah terkirim")
    
LOG=-1001593451768

@Bot.on_callback_query(filters.regex("cbconfess"))
async def cbconfess(client, query: CallbackQuery):
    await query.message.delete()  
    user_id = query.from_user.id
    nama = await client.ask(user_id, 'ð£ <b>Ketik Nama kamu</b>\n\n<b>Informasi :</b> __Pakai nama kamu,Jika ingin privasi nama silakan gunakan /secret saja__', filters=filters.text, timeout=30)
    if "/" in nama.text:
        nama = "secret"
    else:
        nama = nama.text
    tujuan = await client.ask(user_id, 'ð£ <b>Ketik Nama Crush kamu</b>\n\n<b>Informasi :</b> __Wajib pakai username/nama__', filters=filters.text, timeout=30)
    if "/" in tujuan.text:
        to = await client.ask(user_id, '<b>â ï¸ Terjadi kesalahan.</b>\n__Ketik nama crush kamu__', filters=filters.text, timeout=30)
        if "/" in to.text:
            return await client.send_message(user_id, 'Sepertinya anda masih tolol silakan bertanya kepada @phobiakaliann')
        else:
            to = to
    else:
        to = tujuan
    isi = await client.ask(user_id, f"ð£ <b>Ketik apa yang ingin kamu sampaikan kepada {to.text}</b>", filters=filters.text, timeout=30)
    if "/" in isi.text:
        confesss = await client.ask(user_id, '<b>â ï¸ Terjadi kesalahan.</b>\n__Ketik apa yang kamu ingin sampaikan kepada crush__', filters=filters.text, timeout=30)
    else:
        confesss = isi
    report = await client.send_message(LOG, f"<b>From :</b> <i>{nama}</i>\n<b>To :</b> <i>{to.text}</i>\n<b>Isi :</b> <i>{confesss.text}</i>", disable_web_page_preview=True)
    await client.send_message(user_id, f"â **Sudah terkirim**", 
                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("â¡ View", url=f"https://t.me/fvconfess/{report.id}")]]),
                              disable_web_page_preview=True,
                             )

    
Bot.run()
