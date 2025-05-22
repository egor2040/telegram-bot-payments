import logging
from telegram import Update, LabeledPrice
from telegram.ext import Application, CommandHandler, MessageHandler, filters, PreCheckoutQueryHandler, CallbackContext

# Вставьте сюда ваш токен
TOKEN = os.getenv("BOT_TOKEN")
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привет! Выберите команду /buy для покупки.")

async def buy(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    title = "Название товара"
    description = "Описание товара"
    payload = "Custom-Payload"
    currency = "XTR"  # Используем Telegram Stars (XTR)
    price = 5.00  # Цена в XTR
    prices = [LabeledPrice("Название товара", int(price * 100))]

    await context.bot.send_invoice(
        chat_id=chat_id,
        title=title,
        description=description,
        payload=payload,
        provider_token="",  # Пустой токен для цифровых товаров
        currency=currency,
        prices=prices,
        start_parameter="start_parameter"
    )

async def precheckout_callback(update: Update, context: CallbackContext):
    query = update.pre_checkout_query
    if query.invoice_payload != 'Custom-Payload':
        await query.answer(ok=False, error_message="Что-то пошло не так...")
    else:
        await query.answer(ok=True)

async def successful_payment_callback(update: Update, context: CallbackContext):
    payment = update.message.successful_payment
    telegram_payment_charge_id = payment.telegram_payment_charge_id
    await update.message.reply_text(f"Платеж успешно выполнен! Ваш ID: {telegram_payment_charge_id}")

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("buy", buy))
    application.add_handler(PreCheckoutQueryHandler(precheckout_callback))
    application.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_callback))

    application.run_polling()

if __name__ == '__main__':
    main()
