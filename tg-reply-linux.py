from telethon import TelegramClient, sync, events, functions, types
import datetime

api_id = ''
api_hash = ''
message = 'Добрый день!\nДля связи с технической поддержкой 123 напишите сообщение: @123_bot'


def log(text):
    with open('tg-reply.log', 'a') as logfile:
        logfile.write(str(datetime.datetime.now()) + ' | ' + text + '\n')


client = TelegramClient('session_name', api_id, api_hash)
client.start()
myself = client.get_me()

if __name__ == "__main__":
    import os, sys
    fpid = os.fork()
    if fpid != 0:
        if client.is_user_authorized():
            print('Auth OK: ' + myself.username + ', ' + myself.phone + '; pid: ' + str(fpid))
            log('Auth OK: ' + myself.username + ', ' + myself.phone + '; pid: ' + str(fpid))
        sys.exit(0)


@client.on(events.NewMessage)
async def normal_handler(event):
    if not event.is_channel:
        sender = await client.get_entity(event.from_id)
        if sender.username != myself.username:
            if 'bot' not in sender.username:
                log("==== New message ====")
                log(str(event.message.date))
                log("username: " + sender.username)
                if sender.phone is not None:
                    log("phone: " + str(sender.phone))
                log('text: ' + event.message.text)
                # await event.reply(message)
                await client.send_message(sender.username, message)
            else:
                log("==== New message (bot) ====")
                log(str(event.message.date))
                log("username: " + sender.username)
                log('text: ' + event.message.text)


client.run_until_disconnected()
