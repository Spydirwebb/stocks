import asyncio

import stock_data.finnhub as finnhub
import telegram.create_client as create_client
import telegram.channel_messages as channel_messages
import telegram.parse_data as parse_data


async def main(client, phone):
    await client.start()
    print("Client Created")

    '''
    if await client.is_user_authorized() == False:
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input("Enter the code: "))
        except SessionPasswordNeededError:
            await client.sign_in(password=input("Password: "))
    '''

    #me = await client.get_me()

    async with client:
         await channel_messages.get_telegram_data(client, phone)
    
    tickers = parse_data.parse_data()
    print(tickers)

    for ticker in tickers:
        #get_price
        print(f"{ticker}: {finnhub.get_price(ticker)}")

client, phone = create_client.create_client()

loop = asyncio.get_event_loop()
loop.run_until_complete(main(client, phone))
loop.close()
