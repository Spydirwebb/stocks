import json
import asyncio
from datetime import date, datetime

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
    PeerChannel
)

import create_client

#some functions to parse json date
class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        if isinstance(o, bytes):
            return list(o)

        return json.JSONEncoder.default(self, o)


#create client
client, phone = create_client.createClient()

async def main (phone):
    await client.start()
    print("Client Created")

    #ensure authorized
    if await client.is_user_authorized() == False:
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input("Enter the code: "))
        except SessionPasswordNeededError:
            await client.sign_in(password=input("Password: "))

    me = await client.get_me()

    #user_input_channel = input("Enter entity(telegram URL or entity id): ")

    #if user_input_channel.isdigit():
    #    entity = PeerChannel(int(user_input_channel))
    #else:
    #    entity = user_input_channel

    entity = 'https://t.me/TheExtraIncomeStocks'
    my_channel = await client.get_entity(entity)

    offset_id = 0
    limit = 1            #messages per request
    all_messages = []
    total_messages = 0
    total_count_limit = 10  #tlimit

    while True:
        print("Current Offset ID is:", offset_id, "; Total Messages:", total_messages)
        history = await client(GetHistoryRequest(
            peer=my_channel,
            offset_id=offset_id,
            offset_date=None,
            add_offset=0,
            limit=limit,
            max_id=0,
            min_id=0,
            hash=0
        ))
        if not history.messages:
            break
        messages = history.messages
        for message in messages:
            all_messages.append(message.to_dict())
        offset_id = messages[len(messages) - 1].id
        total_messages = len(all_messages)
        if total_count_limit != 0 and total_messages >= total_count_limit:
            break

    with open('channel_messages.json', 'w') as outfile:
        json.dump(all_messages, outfile, indent=4,cls=DateTimeEncoder)

with client:
    client.loop.run_until_complete(main(phone))

f = open('channel_messages.json',)
data = json.load(f)

for i in range(0, len(data)):
    val = data[i]
    if val is not None:
        val = data[i]["media"]
    if val is not None:
        val = data[i]["media"]["webpage"]
    if val is not None:
        val = data[i]['media']['webpage']['description']
        print(val)