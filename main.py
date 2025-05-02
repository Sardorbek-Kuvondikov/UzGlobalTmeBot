import os
from dotenv import load_dotenv
import telebot

# .env fayldan tokenni yuklab olish
load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

user_state = {}

def main_menu():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("📞 Telefon raqam", "📍 Manzil")
    markup.row("👨‍💻 Admin bilan bog‘lanish", "❓ Ko‘p beriladigan savollar")
    markup.row("💵 Narxlar", "🎓 Kurslar")
    markup.row("👨‍🏫 Ustozlar")
    return markup

def course_menu():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🌐 Online", "🏫 Ofline")
    markup.row("🔙 Orqaga")
    return markup

def ustozlar_menu():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("👨‍🏫 Sardorbek", "👨‍🏫 Nuroli")
    markup.row("🔙 Orqaga")
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    user_state[chat_id] = "main"
    bot.send_message(chat_id, "Assalomu alaykum! Quyidagilardan birini tanlang:", reply_markup=main_menu())

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    text = message.text
    state = user_state.get(chat_id, "main")

    if text == '📞 Telefon raqam':
        bot.send_message(chat_id, "📞 Telefon: 91 822 05 00")

    elif text == '📍 Manzil':
        bot.send_message(chat_id,
            "📍 <b>Manzil:</b> Toshkent shahri, Navza metro yaqinida joylashgan <b>UzGlobal</b> o‘quv markazi.",
            parse_mode="HTML"
        )
        bot.send_location(chat_id, latitude=41.288880, longitude=69.224483)

    elif text == '👨‍💻 Admin bilan bog‘lanish':
        bot.send_message(chat_id, "👨‍💻 Admin: @mr_sardorbek_coder")

    elif text == '❓ Ko‘p beriladigan savollar':
        bot.send_message(chat_id, "❓ Hozircha savollar mavjud emas.")

    elif text == '💵 Narxlar':
        bot.send_message(chat_id, "💵 Narxlar: Belgilanmagan")

    elif text == '🎓 Kurslar':
        bot.send_message(chat_id, "🎓 Kurs turini tanlang:", reply_markup=course_menu())
        user_state[chat_id] = "kurslar"

    elif text == '🌐 Online':
        bot.send_message(chat_id, "🌐 Online kurs narxi: 400 UZS")

    elif text == '🏫 Ofline':
        bot.send_message(chat_id, "🏫 Ofline kurs narxi: 650 UZS")

    elif text == '👨‍🏫 Ustozlar':
        bot.send_message(chat_id, "Quyidagi ustozlardan birini tanlang:", reply_markup=ustozlar_menu())
        user_state[chat_id] = "ustozlar"

    elif text == '👨‍🏫 Sardorbek':
        msg = (
            "👨‍🏫 <b>Sardorbek</b>\n"
            "📅 <b>Tug‘ilgan sana:</b> 2002-yil\n"
            "📍 <b>Hudud:</b> Samarqand viloyati\n"
            "🛠 <b>Ko‘nikmalar:</b>\n"
            "• DEVELOPER\n"
            "• TOPIK 6\n"
            "• IELTS 7\n"
        )
        bot.send_message(chat_id, msg, parse_mode="HTML", reply_markup=ustozlar_menu())

    elif text == '👨‍🏫 Nuroli':
        msg = (
            "👨‍🏫 <b>Nuroli</b>\n"
            "📅 <b>Tug‘ilgan sana:</b> 1987-yil\n"
            "📍 <b>Hudud:</b> Samarqand viloyati\n"
            "🛠 <b>Ko‘nikmalar:</b>\n"
            "• TOPIK 6\n"
            "• IELTS 8\n"
            "• RUS TILI\n"
        )
        bot.send_message(chat_id, msg, parse_mode="HTML", reply_markup=ustozlar_menu())

    elif text == '🔙 Orqaga':
        if state in ["kurslar", "ustozlar"]:
            bot.send_message(chat_id, "🔙 Bosh menyuga qaytdingiz.", reply_markup=main_menu())
            user_state[chat_id] = "main"
        else:
            bot.send_message(chat_id, "❗ Siz orqaga qaytadigan sahifada emassiz.")

    else:
        bot.send_message(chat_id, "Iltimos, menyudan tanlang.")

if __name__ == "__main__":
    bot.infinity_polling()
