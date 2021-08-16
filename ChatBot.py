

from playsound import playsound
import gtts
from datetime import datetime
import random

now = datetime.now()
time = now.strftime("%H:%M:%S")
bulan = now.strftime("%m")
tahun = now.strftime("%Y")
tanggal = now.strftime("%d")
# Check current time
# print(now)
# print(time)
# print(bulan)
# print(tanggal)

nama = "Fadhil Elrizanda"
default = [
    "maaf, aku tidak tahu jawaban dari pertanyaan mu",
    "mohon hubungi nomor bersangkutan 08123143342"
]

# perlu pip3 install gTTS pyttsx3 playsound
# text to speech
tts = gtts.gTTS("Hola Mundo", lang="es")
tts.save("hola.mp3")
playsound("...hola.mp3")

# referensi https://www.thepythoncode.com/article/convert-text-to-speech-in-python


# list message

# Just Examples
# list jawaban untuk pertanyaan tentang nama
jawaban_nama = [
    "nama saya {0}".format(nama),
    "saya biasa dipanggil {0}".format(nama),
    "panggil saya {0}".format(nama)
]

# Just Examples
# list jawaban untuk pertanyaan tentang tanggal
jawaban_tanggal = [
    "hari ini tanggal {0}".format(tanggal),
    "ya ampun masa tidak tahu, hari ini tanggal {0}".format(tanggal)
]

jawaban_bulan = [
    "Saya rasa sekarang bulan {0}".format(bulan),
    "Mungkin bulan {0}".format(bulan)
]

jawaban_tahun = [
    "Sekarang tahun {0}".format(tahun),
    "Tahun... {0}".format(tahun)
]

# Just Examples
# opsi pertanyaan yang bisa dijawab
pertanyaan = {
    "nama kamu siapa?": jawaban_nama,
    "kamu siapa?": jawaban_nama,
    "tanggal berapa hari ini?": jawaban_tanggal,
    "hari ini tanggal berapa?": jawaban_tanggal,
    "default": default
}

# Just Examples
# list jawaban untuk sebuah argument selain pertanyaan
statement = [
    'ceritakan lebih banyak!',
    'kenapa kamu berpikir begitu?',
    'sudah berapa lama kamu merasa seperti ini?',
    'Itu sangat menarik!',
    'oh wow!',
    ':)'
]

# Just Examples tambahkan sesuai selera
# respon keseluruhan
responses = {
    'pertanyaan': pertanyaan,
    'statement': statement,
    # ...
}

# Task
# ----
# bot dapat membalas sapaan
# bot dapat memberikan informasi dirinya
# bot juga daapt menjawab beberapa informasi umum atau informasi yang anda inginkan
# bot menjawab dengan mencari pattern pada kalimat
# bot menjawab dengan kata yang tidak sama untuk setiap kalinya
# bot menjawab sesuai dengan senang atau tidak
# bot dapat menjawab dengan suara
# optional file suara setelah dipakai auto dihapus
# gunakan file ini sebagai module , buat file testing.py dan jalankan bot pada file testing.py
# bebas berkreasi :)

# Just Examples


def chatbot(message):
    respon1 = responses['pertanyaan']
    respon_statement = responses['statement']
    if 'siapa' in message:
        respon2 = random.choices(jawaban_nama)
        return (respon2)
    elif 'tanggal' in message:
        respon2 = random.choices(jawaban_tanggal)
        return (respon2)
    elif 'bulan' in message:
        respon2 = random.choices(jawaban_bulan)
        return (respon2)
    elif 'tahun' in message:
        respon2 = random.choices(jawaban_tahun)
        return (respon2)
    elif 'bagaimana' in message:
        return random.choices(respon_statement)
    else:
        return respon1['default']


def main():
    print("Selamat datang pada layanan chatbot")
    while True:
        question = str(input("Apa yang ingin Anda tanyakan : "))
        if question == "q" or question == "quit":
            break
        answer = chatbot(question)
        print(answer)


if __name__ == "__main__":
    main()
