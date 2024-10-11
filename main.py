import os
import re
from telegram import Update, ParseMode
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackContext
from telegram.error import BadRequest

# Allowed domains list
ALLOWED_DOMAINS = [
    "shineads.in",
    "dohe.in",
    "themeforest.net",
    "codecanyon.net"
]

# Function to check if a user is an admin
def is_user_admin(update: Update, user_id: int) -> bool:
    """Check if a user is an admin in the chat."""
    chat_id = update.message.chat_id
    member = update.effective_chat.get_member(user_id)
    return member.status in ['administrator', 'creator']

# Start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I'm your bot. I will allow only URLs from specific domains for non-admins.")

# Function to check for URLs and delete if not allowed
def check_urls(update: Update, context: CallbackContext) -> None:
    message = update.message
    user_id = message.from_user.id
    urls = re.findall(r'(https?://[^\s]+)', message.text)  # Extract URLs using regex

    # If user is an admin, allow sending any URL
    if is_user_admin(update, user_id):
        return  # Admin can send any URL, no need to delete or warn

    # Regular user: Check if the URLs are allowed
    for url in urls:
        # Extract domain from URL
        domain = re.findall(r'https?://(?:www\.)?([^/]+)', url)
        if domain and domain[0] not in ALLOWED_DOMAINS:
            try:
                # Delete the message if URL is not allowed
                context.bot.delete_message(chat_id=message.chat_id, message_id=message.message_id)

                # Send a warning message to the user
                warning_text = (
                    f"⚠️ The URL {url} is not allowed.\n"
                    "Only URLs from the following domains are permitted:\n"
                    f"{', '.join(ALLOWED_DOMAINS)}"
                )
                message.reply_text(warning_text)
            except BadRequest as e:
                context.bot.logger.error(f"Error deleting message: {e}")

def main():
    # Initialize the bot
    updater = Updater(token=os.getenv("TOKEN"), use_context=True)
    dispatcher = updater.dispatcher

    # Add command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Add URL filtering handler for non-admin users
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, check_urls))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
