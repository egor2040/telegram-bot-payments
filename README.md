# Telegram Bot with Payments using Telegram Stars

This is a simple Telegram bot that demonstrates how to handle payments using Telegram Stars. The bot allows users to purchase a product via the `/buy` command and handles the payment process from sending an invoice to confirming a successful payment.

## Features

- Send an invoice using Telegram Stars
- Handle pre-checkout queries
- Confirm successful payments

## Setup

1. Clone the repository:

```bash
git clone https://github.com/xep1x/telegram-bot-payments.git
cd telegram-bot-payments```

2. Install the required packages:

```bash
pip install -r requirements.txt```

3. Create a bot on Telegram and get your bot token from @BotFather.

4. Replace 'YOUR_BOT_TOKEN' in pay_bot.py with your actual bot token.

5. Run the bot:

```bash
python pay_bot.py```