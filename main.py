import requests
from config import aim_token, folder_id

headers = {
    'Authorization': f'Bearer {aim_token}',
}

data = {
        'text': "Появление полноценного искусственного интеллекта может стать концом человеческой расы.",
        'lang': 'ru-RU',
        'folderId': folder_id,
        'format': 'lpcm',
        'sampleRateHertz': 48000,
    }

speech = requests.post("https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize",
                       headers=headers, data=data)
open('speech.raw', 'wb').write(speech.content)
# run in terminal
# sox -r 48000 -b 16 -e signed-integer -c 1 speech.raw speech.wav
