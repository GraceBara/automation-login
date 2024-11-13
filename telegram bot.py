import logging
import time
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ParseMode
import random

# Set up logging to monitor issues during execution
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Initializing global variables
loading_messages = [
    "Loading... please wait.",
    "Preparing your request...",
    "Just a moment, fetching the song...",
    "Almost there...",
    "Hold on, it's coming soon!"
]

song_list = [
    "https://t.me/some_music_channel_link/song1.mp3",  # Example song URL
    "https://t.me/some_music_channel_link/song2.mp3",  # Another song URL
    "https://t.me/some_music_channel_link/song3.mp3"   # Another song URL
]

# Function to send loading animation
def loading_animation(update: Update, context: CallbackContext):
    # Simulate a loading message with some random delay to simulate loading
    for msg in loading_messages:
        update.message.reply_text(msg)
        time.sleep(2)  # Sleep to simulate loading (avoid using time.sleep in production)
    
    # Simulate fetching a song and send a response
    song_url = random.choice(song_list)  # Pick a random song URL
    update.message.reply_text(f"Here is your song: {song_url}", parse_mode=ParseMode.MARKDOWN)

# Start command to initialize the bot and welcome the user
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome! Type any text to get a song recommendation.\n\nOr type /load to see the loading animation.")

# Command to trigger loading animation
def load(update: Update, context: CallbackContext):
    update.message.reply_text("Starting the process... please wait a moment.")
    loading_animation(update, context)

# Function to handle unknown commands
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry, I didn't understand that. Type /help for available commands.")

# Main function to set up the bot
def main():
    # Replace 'YOUR_BOT_TOKEN' with your bot's actual token.
    bot_token = "YOUR_BOT_TOKEN"
    
    # Initialize the Updater and Dispatcher
    updater = Updater(bot_token, use_context=True)
    
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    
    # Register handlers for commands and messages
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("load", load))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, loading_animation))  # Handle text messages
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))  # Handle unknown commands

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
