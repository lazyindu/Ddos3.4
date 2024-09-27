import hashlib

# Set your new creator watermark here
new_creator = "This File Is Made By YT@LazyDeveloperr"

# Generate the SHA-256 hash of the new creator string
new_bot_code = hashlib.sha256(new_creator.encode()).hexdigest()

# Print the new BotCode
print("New BotCode:", new_bot_code)