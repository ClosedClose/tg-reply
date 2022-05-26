from telethon import TelegramClient, sync, events

api_id = ''
api_hash = ''
message = 'Добрый день!\nДля связи с технической поддержкой NAME напишите сообщение: @123_bot'

client = TelegramClient('session_name', api_id, api_hash)
client.start()
myself = client.get_me()

if client.is_user_authorized():
    print('Auth OK: ' + myself.username + ', ' + myself.phone)


@client.on(events.NewMessage)
async def normal_handler(event):
    sender = await client.get_entity(event.from_id)
    if not event.is_channel:
        if sender.username != myself.username:
            if 'bot' not in sender.username:
                print("==== New message ====")
                print(str(event.message.date))
                print("username: " + sender.username)
                if sender.phone is not None:
                    print("phone: " + str(sender.phone))
                print('text: ' + event.message.text)
                # await event.reply(message)
                await client.send_message(sender.username, message)
            else:
                print("==== New message (bot) ====")
                print(str(event.message.date))
                print("username: " + sender.username)
                print('text: ' + event.message.text)


client.run_until_disconnected()