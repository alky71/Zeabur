from telethon import TelegramClient, events
import os

# === Конфігурація ===
API_ID = int(os.getenv("API_ID", 28860395))  # встав свій api_id або задай як env змінну
API_HASH = os.getenv("API_HASH", "cff9f95899476d0f6f78f05c7acb3e37")
SESSION = os.getenv("SESSION", "session+62")  # або .session файл у директорії

client = TelegramClient(SESSION, API_ID, API_HASH)

# === Обробник подій ===
@client.on(events.NewMessage)
async def handler(event):
    if event.raw_text.lower().strip() == "е":
        await event.reply("р")

# === Запуск ===
async def main():
    print("🤖 Userbot запущений та слухає повідомлення...")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
