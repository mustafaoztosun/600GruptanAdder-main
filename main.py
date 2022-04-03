from pyrogram import Client, filters as f
from time import sleep, time
from os import getenv
################################################

TOKEN = getenv("STRING")
try:
	sleepSure = int(getenv("SLEEP_SURE"))
except:
	print("Lütfen Sadece Sayı Giriniz!\nSleep Süresi 0 Olarak Ayarlandı!")
	sleepSure=1

getChat = []
fail_list = []

s_k = Client(
	TOKEN,
	api_id="5775802",
	api_hash="6011ffc6cec69c60ef86456db0ce4d09"
    )

print("Hello")

@s_k.on_message(f.me & f.command("get", ""))
async def _(b,m):
	chat = m.chat.id
	me = await s_k.get_me()
	print("get")

	if len(m.text.split()) > 1:
		chat=m.text.split()[1]

	await m.edit("Mac Var Mı?")

	for member in await b.get_chat_members(chat):
		if member.user.status in ["recently", "online"] and member.user.id != me.id and member.user.id not in getChat:
			getChat.append(member.user.id)

	print("Tahmin Var Mı?")
	await m.edit("Kayıp")

@s_k.on_message(f.me & f.command("add", ""))
async def _(b,m):
	chat = m.chat
	a=0
	fail=0
	basangic = time()
	print("add")
	await m.edit("*Nasıl alabilirim*")
	for i in getChat:
		try:
			await b.add_chat_members(chat.id, i)
			sleep(sleepSure)
			a+=1
		except:
			fail+=1
			fail_list.append(i)

	print("Eklenen: {}\nHata: {}\n\nZaman: {}\n\n{}".format(a, fail, time()-basangic ,fail_list))
	await m.edit("Ok. I'm Waiting ...")



s_k.run()
