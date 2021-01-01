# Morse Telegram Bot
Morse Text/QR Code/Voice creation bot based on PyTelegramBotApi

This bot can be used to create Morse messages in English for Telegram. 

### Installation and run
Using console:
```
git clone https://github.com/Antcating/morse_telegram_bot.git
cd morse_telegram_bot
python3 main.py
```

### Config

#### Initial Config
On the first run of the bot you will be asked to input Bot Token of your bot, that you can get from [@BotFather](t.me/BotFather). The token will be saved to config file and after that you won't be asked to input it again. Initial configuration is over. 
Addiction information about Bot API and etc. can be found on the main page of the [PyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI). 

#### In-bot config 
Bot can send text, voice messages and QRcodes. Each of the modules can be disabled using in-bot commands. 

* *set_qr_code_send_false* - turn off QR-codes
* *set_qr_code_send_true* - turn on QR-codes
* *set_voice_send_false* - turn off voices
* *set_voice_send_true* - turn on voices
* *set_text_send_false* - turn off text
* *set_text_send_true* - turn on text

For each user can be created own config. 
All configs are saving, so after reboot the settings will not be reset.

### Additional information 

Repository contains simple bash file to restart bot, if will be some problems, so that you can run it and forget about it. Bot will automatically run in the background.

### Related projects and thanks 
- [PyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) – telegram bot interaction.
- [Pydub](https://pydub.com/) – audio part.
- [QRcode](https://github.com/lincolnloop/python-qrcode) – QRcode creation part. 