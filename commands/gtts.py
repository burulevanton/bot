from gtts import gTTS
import command_system
import vkapi


def say(text):
    text = text.replace('скажи', '')
    tts = gTTS(text=text, lang='ru')
    tts.save('audio.ogg')
    message = ''
    return message, vkapi.upload_file()


gtts_command = command_system.Command()

gtts_command.keys = ['скажи']
gtts_command.description = 'Сделать голосовое сообщение'
gtts_command.process = say
