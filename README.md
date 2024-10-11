# Link Defender Telegram Bot

This bot restricts users from sending URLs outside of a specified list of allowed domains in a group chat. Only admins are allowed to send any URLs, while regular users are restricted to URLs from a predefined set of domains. If a user tries to send a URL from an unauthorized domain, the bot will delete the message and send a warning.

## Features

- Allows only specific domains for regular users.
- Admins can send URLs from any domain.
- Deletes unauthorized URLs and sends a warning to the user.

## Allowed Domains (modifiable)
- shineads.in
- dohe.in
- themeforest.net
- codecanyon.net

## Requirements

- Python 3.8 or higher
- Telegram Bot API token (get this from [@BotFather](https://t.me/BotFather))
- Koyeb account for deployment (or any other platform)

## Local Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your_username/url_filter_bot.git
   cd url_filter_bot
