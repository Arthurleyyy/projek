import requests
import os
import argostranslate.translate
from datetime import datetime
import pyttsx3
import speech_recognition as sr

# Inisialisasi text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)  # kecepatan bicara

def bicara(teks):
    engine.say(teks)
    engine.runAndWait()

# Fungsi untuk input suara
def dengar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Dengarkan... (bicara sekarang)")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="id-ID")
        print(f"Kamu (suara): {text}")
        return text
    except sr.UnknownValueError:
        print("❗ Tidak menangkap suara. Coba lagi.")
        return ""
    except sr.RequestError as e:
        print(f"[ERROR Mic] {e}")
        return ""

# Fungsi translate
installed_languages = argostranslate.translate.load_installed_languages()

def translate(text, ke_bahasa):
    try:
        lang_map = {
            "inggris": ("id", "en"),
            "indonesia": ("en", "id")
        }
        dari, ke = lang_map.get(ke_bahasa.lower(), ("id", "en"))
        from_lang = list(filter(lambda x: x.code == dari, installed_languages))[0]
        to_lang = list(filter(lambda x: x.code == ke, installed_languages))[0]
        translation = from_lang.get_translation(to_lang)
        return translation.translate(text)
    except Exception as e:
        return f"[ERROR Translate] {e}"

# Fungsi Tanya AI Lokal
def tanya_ai(prompt):
    try:
        response = requests.post(
            'http://localhost:11434/api/generate',
            json={
                'model': 'llama3',
                'prompt': prompt,
                'stream': False
            },
            timeout=90
        )
        return response.json()['response']
    except Exception as e:
        return f"[ERROR GPT] {e}"

# Fungsi simpan riwayat obrolan
def simpan_riwayat(user, bot):
    with open("history.txt", "a", encoding="utf-8") as file:
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{waktu}] Kamu: {user}\n")
        file.write(f"[{waktu}] AI: {bot}\n\n")

# Program Utama
if __name__ == "__main__":
    print("\n🤖 AI Lokal Aktif! Ketik 'exit' untuk keluar. Tambahkan '| ke Inggris' untuk translate. Ketik 'suara' untuk bicara.")
    while True:
        user_input = input("Kamu: ")
        if user_input.lower() == "exit":
            print("Sampai jumpa!")
            break
        elif user_input.lower() == "suara":
            user_input = dengar()
            if not user_input:
                continue  # kalau kosong, ulangi

        if "| ke" in user_input:
            teks, perintah = user_input.split("| ke")
            hasil = translate(teks.strip(), perintah.strip())
        else:
            hasil = tanya_ai(user_input)

        print(f"AI: {hasil}\n")
        bicara(hasil)
        simpan_riwayat(user_input, hasil)
