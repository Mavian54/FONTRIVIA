.pip install python-telegram-bot

from telegram import Update
                                               if __name__ == '__main__':
                                                                                    main()
                                                                                    mandHandlermandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with the token you received from BotFather
TOKEN = '6468974915:AAEXqbEzE-5-VYLLYpzOdNZ4QTYB5SgwWsEAAEXqbEzE-5-VYLLYpzOdNZ4QTYB5SgwWsE''

# Sample trivia questions
trivia_questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "Who wrote 'Romeo and Juliet'?", "answer": "William Shakespeare"},
        ]

        def start(update: Update, context: CallbackContext) -> None:
            update.message.reply_text("Welcome to the Trivia Bot! Type /trivia to get a question.")

            def trivia(update: Update, context: CallbackContext) -> None:
                question = trivia_questions[0]["question"]  # Change this to fetch a random question
                    update.message.reply_text(f"Question: {question}")

                    def answer(update: Update, context: CallbackContext) -> None:
                        user_answer = update.message.text
                            correct_answer = trivia_questions[0]["answer"]  # Replace with the correct answer
                                if user_answer.lower() == correct_answer.lower():
                                        update.message.reply_text("Correct!")
                                            else:
                                                    update.message.reply_text(f"Wrong! The correct answer is {correct_answer}.")

                                                    def main() -> None:
                                                        updater = Updater(TOKEN)

                                                            dp = updater.dispatcher
                                                                dp.add_handler(CommandHandler("start", start))
                                                                    dp.add_handler(CommandHandler("trivia", trivia))
                                                                        dp.add_handler(MessageHandler(Filters.text & ~Filters.command, answer))

                                                                            updater.start_polling()

                                                                                updater.idle()

                                                                                if __name__ == '__main__':
                                                                                    main()
                                                                                                                                   if __name__ == '__main__':
                                                                                    main()
                                                                                    