from morse3 import Morse as m
import telebot
import qrcode
import io
import ast
from audio import audio_enc


#QR part 
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Database check
try:
    user_db_check = open("user_pref.db", 'r').read().close()
except:
    open("user_pref.db", 'w+').close()

#Bot part
try:
    bot_input = open("bot_token.tg", 'r').read()
except:
    bot_input = input('Incert Bot Token here: ')
    bot_token_write = open('bot_token.tg','w+')
    bot_token_write.write(bot_input)
    bot_token_write.close()
bot = telebot.TeleBot(bot_input)

@bot.message_handler(commands=['start', 'help'])
def handle_start(message):
    bot.send_message(message.from_user.id,
                     """*Bot for Morse Code in Telegram.* 
Send message and bot will automatically rewrite it in Morse.
If you don't need QR-code, text or voice - you can turn it off by using commands (click on the command to copy it):
```set_qr_code_send_false``` - turn off QR-codes
```set_qr_code_send_true``` - turn on QR-codes
```set_voice_send_false``` - turn off voices
```set_voice_send_true``` - turn on voices
```set_text_send_false``` - turn off text
```set_text_send_true``` - turn on text
""", parse_mode=('markdown'))


@bot.message_handler(content_types=['text'])
def handle_menu(message):
    #User check list
        #ID DB
    db_pref = open("user_pref.db", 'r+')
    
    db_lines = db_pref.read()
    db_pref.close()
    user_id = message.from_user.id
    try:
        db_lines.index(str(user_id))
        print("Found ID: " + str(user_id))
    except ValueError:
        print('New ID: ' + str(user_id))
        db_pref_new = open("user_pref.db", 'a+') 
        
        new_user = {"user_id":user_id,"qr":"1","voice":'1','text':'1'}
        db_pref_new.write(str(new_user)+'\n')
        db_pref_new.close()

    #SETTINGS
    
    #QR
    try:
        if message.text == 'set_qr_code_send_false':
            db = open("user_pref.db", 'r+')
            db_lines = db.readlines()
            db.close()
            for user in db_lines:
                if user.find(str(user_id)) != -1:
                    user_dict = ast.literal_eval(user)
                    user_dict['qr']="0"
                    db_lines[db_lines.index(user)]=str(user_dict) + '\n'
                    open("user_pref.db", 'w').writelines(db_lines)
            bot.send_message(message.from_user.id,
                         "Settings have been changed.")    
            message = ''
        if message.text == 'set_qr_code_send_true':
            db = open("user_pref.db", 'r+')
            db_lines = db.readlines()
            db.close()
            for user in db_lines:
                if user.find(str(user_id)) != -1:
                    user_dict = ast.literal_eval(user)
                    user_dict['qr']="1"
                    db_lines[db_lines.index(user)]=str(user_dict) + '\n'
                    open("user_pref.db", 'w').writelines(db_lines)
            bot.send_message(message.from_user.id,
                         "Settings have been changed.")    
            message = ''
        #Voice
        if message.text == 'set_voice_send_false':
            db = open("user_pref.db", 'r+')
            db_lines = db.readlines()
            db.close()
            for user in db_lines:
                if user.find(str(user_id)) != -1:
                    user_dict = ast.literal_eval(user)
                    user_dict['voice']="0"
                    db_lines[db_lines.index(user)]=str(user_dict) + '\n'
                    open("user_pref.db", 'w').writelines(db_lines)
            bot.send_message(message.from_user.id,
                         "Settings have been changed.")    
            message = ''    
        if message.text == 'set_voice_send_true':
            db = open("user_pref.db", 'r+')
            db_lines = db.readlines()
            db.close()
            for user in db_lines:
                if user.find(str(user_id)) != -1:
                    user_dict = ast.literal_eval(user)
                    user_dict['voice']="1"
                    db_lines[db_lines.index(user)]=str(user_dict) + '\n'
                    open("user_pref.db", 'w').writelines(db_lines)
            bot.send_message(message.from_user.id,
                         "Settings have been changed.")    
            message = ''  
        #Text
        if message.text == 'set_text_send_false':
            db = open("user_pref.db", 'r+')
            db_lines = db.readlines()
            db.close()
            for user in db_lines:
                if user.find(str(user_id)) != -1:
                    user_dict = ast.literal_eval(user)
                    user_dict['text']="0"
                    db_lines[db_lines.index(user)]=str(user_dict) + '\n'
                    open("user_pref.db", 'w').writelines(db_lines)
            bot.send_message(message.from_user.id,
                         "Settings have been changed.")    
            message = ''    
        if message.text == 'set_text_send_true':
            db = open("user_pref.db", 'r+')
            db_lines = db.readlines()
            db.close()
            for user in db_lines:
                if user.find(str(user_id)) != -1:
                    user_dict = ast.literal_eval(user)
                    user_dict['text']="1"
                    db_lines[db_lines.index(user)]=str(user_dict) + '\n'
                    open("user_pref.db", 'w').writelines(db_lines)
            bot.send_message(message.from_user.id,
                         "Settings have been changed.")    
            message = ''    
    
    
        #Encoding
        encoded = m(message.text).stringToMorse()
    
        #Audio 
        def audio_part(message):
            audio_enc(message)
            audio = open('audio_files/joinedFile.ogg', 'rb')
            return audio
        #QR part
        def qr_part(message):
            qr.add_data(encoded)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()
            return img_byte_arr

        
        #Text part
        def text_part(message):
            text_morse = encoded
            return text_morse
        #Bot send 
        db = open("user_pref.db", 'r+')
        db_lines = db.readlines()
        db.close()
        for user in db_lines:
            if user.find(str(user_id)) != -1:
                user_dict = ast.literal_eval(user)
                if user_dict['text'] == '1':
                    bot.send_message(message.chat.id, text_part(message))
                if user_dict['voice'] == '1':
                    bot.send_audio(message.chat.id, audio_part(message))
                if user_dict['qr'] == '1':
                    bot.send_photo(message.chat.id, qr_part(message))
    
        print('Text message: ' + str(message.text))
    except AttributeError:
        print('Error key')

bot.polling(none_stop=True, interval=0)
