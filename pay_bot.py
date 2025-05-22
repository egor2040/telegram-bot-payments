import logging
import os
from telegram import Update, LabeledPrice
from telegram.ext import Application, CommandHandler, MessageHandler, filters, PreCheckoutQueryHandler, CallbackContext

# Получаем токен бота из переменной окружения
import os
TOKEN = os.getenv("BOT_TOKEN")
# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Команда /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привет! Выберите команду /buy для покупки.")

# Команда /buy
async def buy(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    title = "Название товара"
    description = "Описание товара"
    payload = "Custom-Payload"
    currency = "XTR"  # Используем Telegram Stars (XTR)
    price = 5.00  # Цена в XTR
    prices = [LabeledPrice("Название товара", int(price * 100))]  # XTR принимает цену в копейках

    await context.bot.send_invoice(
        chat_id=chat_id,
        title=title,
        description=description,
        payload=payload,
        provider_token=os.getenv("PROVIDER_TOKEN"),
        currency=currency,
        prices=prices,
        start_parameter="test-payment"
    )

# Обработка предварительной проверки
async def precheckout_callback(update: Update, context: CallbackContext):
    query = update.pre_checkout_query
    await query.answer(ok=True)

# Обработка успешной оплаты
async def successful_payment_callback(update: Update, context: CallbackContext):
    await update.message.reply_text("Спасибо за оплату! Доступ открыт.")

# Основной запуск
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("buy", buy))
    app.add_handler(PreCheckoutQueryHandler(precheckout_callback))
    app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_callback))

    app.run_polling()

if __name__ == '__main__':
    main()

