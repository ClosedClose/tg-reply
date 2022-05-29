from telethon import TelegramClient, sync, events, functions, types
import datetime

api_id = ''
api_hash = ''
message = 'Добрый день!\nДля связи с технической поддержкой NAME напишите сообщение: @123_bot'
log_enable = True

client = TelegramClient('session_name', api_id, api_hash)
client.start()
myself = client.get_me()


def log(text):
    if log_enable:
        with open('tg-reply.log', 'a') as logfile:
            logfile.write(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S') + ' | ' + text + '; PID:' + str(os.getpid()) + '\n')


if __name__ == "__main__":
    import os, sys

    fpid = os.fork()
    if fpid != 0:
        sys.exit(0)

if client.is_user_authorized():
    print('Auth OK: ' + myself.username + ', ' + myself.phone + ' PID: ' + str(os.getpid()))
    log('Auth OK: ' + myself.username + ', ' + myself.phone)


@client.on(events.NewMessage)
async def normal_handler(event):
    if not event.is_channel:
        sender = await client.get_entity(event.from_id)
        if sender.username != myself.username:
            if 'bot' not in sender.username:
                log(str(sender.username + ';' + sender.phone + ';' + event.message.text))
                await client.send_message(sender.username, message)
            # await event.reply(message)


client.run_until_disconnected()
