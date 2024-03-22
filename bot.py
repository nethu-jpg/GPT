from pyrogram import Client

# Initialize Pyrogram client
app = Client("my_bot")

# Define a handler for incoming messages
@app.on_message()
async def handle_message(client, message):
    # Echo back the same message
    await message.reply_text(message.text)

# Start the bot
app.run()
