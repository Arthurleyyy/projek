# Web Pengaduan Masyarakat Berbasis PHP
## Deskripsi
Aplikasi web ini dibuat dengan PHP untuk memungkinkan masyarakat menyampaikan pengaduan secara online.

## Fitur Utama
* Pengguna dapat mengirimkan pengaduan dengan deskripsi, kategori, dan lokasi.
* Admin dapat mengelola (melihat, membalas, menutup) pengaduan.
* Sistem otentikasi pengguna (login/registrasi).

## Teknologi yang Digunakan
* PHP
* [Framework PHP yang digunakan:Laravel]
* [Database: MySQL]
* [Frontend:HTML, CSS, JavaScript, PHP]

## Cara Menjalankan
1.  Konfigurasi database (sesuaikan dengan pengaturan database Anda).
2.  Jalankan server PHP.

## Link
* Kode Sumber:[[(https://github.com/Arthurleyyy/projek/tree/main/pengaduan_masyarakat)](https://github.com/Arthurleyyy/projek/tree/main/pengaduan_masyarakat)]
* * **Profil GitHub Saya:** [[https://github.com/Arthurleyyy](https://github.com/Arthurleyyy](https://github.com/Arthurleyyy))
---------------------------------------------------------------------------------------------------


# Aplikasi Kasir Cafe Berbasis Java
## Deskripsi
Aplikasi desktop untuk membantu manajemen transaksi di cafe.

## Fitur Utama
* Mencatat pesanan pelanggan.
* Menghitung total harga.
* Mencetak struk.
* laporan penjualan

## Teknologi yang Digunakan
* Java
* [GUI Library:netbeans]
* [Database,:MySQL,]

## Cara Menjalankan
1.  Pastikan Java Development Kit (JDK) sudah terinstal.
2.  Buka proyek di IDE (misalnya: IntelliJ IDEA, Eclipse).
3.  Jalankan aplikasi.

## Link
* Kode Sumber:https://github.com/Arthurleyyy/projek/blob/main/caffeewinter.zip
* * **Profil GitHub Saya:** [[https://github.com/Arthurleyyy](https://github.com/Arthurleyyy](https://github.com/Arthurleyyy))
---------------------------------------------------------------------------------------------------


# AI-offline berbasis Python: Asisten Bahasa Lokal
## Deskripsi
Proyek ini adalah prototipe asisten AI *offline* yang dibangun menggunakan Python. Ini memanfaatkan **Ollama** untuk menjalankan model AI secara lokal dan **Argos Translate** dengan model `id-en 1_9` untuk fungsionalitas terjemahan. Asisten ini dirancang untuk beroperasi sepenuhnya tanpa koneksi internet dan masih dalam tahap pengembangan aktif.

## Tujuan / Masalah yang Diselesaikan
Membangun solusi AI yang mandiri, tidak memerlukan koneksi internet, dan menjaga privasi data. Proyek ini berfungsi sebagai fondasi awal untuk eksplorasi dan pengembangan fitur-fitur AI *offline* yang lebih kompleks di masa depan, memberikan aksesibilitas AI di lingkungan dengan konektivitas terbatas.

## Fungsionalitas Utama (Tahap Pengembangan Saat Ini)
* **Terjemahan Teks:** Mampu menerjemahkan teks dari Bahasa Indonesia ke Bahasa Inggris menggunakan model `id-en 1_9` dari Argos Translate.
* **Pengenalan Suara (Speech-to-Text):** Dapat mendengarkan input suara dari pengguna dan mengubahnya menjadi format teks.
* **Penjawab Pertanyaan Dasar:** Mampu memproses pertanyaan sederhana dan memberikan jawaban atau respons yang relevan.
* **Perhitungan Matematika:** Melakukan operasi perhitungan dasar berdasarkan input yang diberikan.

## Dataset
Dataset yang digunakan untuk pelatihan model (jika ada, selain model bawaan Ollama/Argos Translate) akan didokumentasikan secara internal. Proyek ini utamanya memanfaatkan model-model yang sudah terlatih dari Ollama dan Argos Translate.

## Metode AI & Model
* **Model Utama (LLM/NLU):** Model bahasa besar yang dijalankan melalui Ollama (misalnya, Llama 2, Mistral, atau model lain yang Anda pilih dan pull dari Ollama).
* **Model Terjemahan:** **Argos Translate** dengan paket bahasa `id-en 1_9`.
* **Integrasi Offline:** Menggunakan **Ollama** sebagai *runtime* untuk menjalankan model AI utama secara lokal di perangkat pengguna.

## Teknologi yang Digunakan
* Python (Disarankan versi **3.10.0** untuk stabilitas)
* Ollama
* Argos Translate
* `argostranslate` (Library Python untuk terjemahan)
* `sounddevice` (atau `PyAudio`, `pydub` jika digunakan untuk audio)
* `SpeechRecognition` (jika digunakan untuk pra-pemrosesan audio)
* [Tambahkan library Python lain yang spesifik Anda gunakan, misal: `numpy`, `pandas`, `flask` jika ada antarmuka web lokal]

## Cara Menjalankan Proyek
Ikuti langkah-langkah di bawah ini untuk menjalankan asisten AI ini di perangkat Anda.

1.  **Pastikan Python Terinstal:**
    * Sangat disarankan menggunakan **Python versi 3.10.0** untuk stabilitas yang optimal.
    * Anda bisa mengunduh Python 3.10.0 dari situs resmi Python: [https://www.python.org/downloads/release/python-3100/](https://www.python.org/downloads/release/python-3100/)

2.  **Instalasi Ollama:**
    * Unduh dan instal Ollama sesuai dengan sistem operasi Anda dari situs resminya: [https://ollama.com/download](https://ollama.com/download)

3.  **Unduh Model AI Utama dari Ollama:**
    * Setelah Ollama terinstal, buka terminal atau command prompt Anda dan unduh model AI yang digunakan oleh proyek ini.
    * Perintah contoh:
        ```bash
        ollama pull [llama2]

4.  **Instal Model Argos Translate:**
    * Buka terminal atau command prompt Anda.
    * Instal *package* Argos Translate melalui pip:
        ```bash
        pip install argostranslate
        ```
    * Kemudian, instal paket bahasa `id-en` yang diperlukan:
        ```bash
        argostranslate package-install id_en
        ```

5.  **Kloning Repositori Proyek:**
    * Buka terminal atau command prompt Anda.
    * Kloning repositori proyek ini ke komputer Anda:
        ```bash
       
6.  **Instal Dependensi Python:**
    * Masuk ke direktori proyek yang baru saja Anda kloning:
        ```bash
        cd AI_Offline
        ```
        (Ganti `nama-repo-ai` dengan nama folder proyek Anda).
    * Instal semua dependensi Python yang dibutuhkan:
        ```bash
        pip install -r requirements.txt
        ```

7.  **Jalankan Asisten AI:**
    * Di dalam direktori proyek, jalankan skrip utama:
        ```bash
        python main.py
        ```
    * **Catatan:** Setelah menjalankan perintah di atas, asisten AI akan mulai dan akan segera meminta input dari Anda (misalnya, melalui suara atau teks).

## Hasil / Demonstrasi (Tahap Pengembangan)
Proyek ini sedang dalam tahap pengembangan aktif, namun fungsionalitas berikut sudah dapat didemonstrasikan:

* **Terjemahan Teks:**
    * Contoh Input: "Apa kabar?"
    * Contoh Output: "How are you?"
* **Transkrip Suara:**
    * Akan menghasilkan teks dari input suara pengguna.
    * Contoh (jika ada): Output transkrip dari rekaman suara.
* **Jawaban/Perhitungan:**
    * Mampu menjawab pertanyaan dasar atau melakukan operasi perhitungan.
    * Contoh (jika ada): Input "Berapa 5+3?" -> Output "8".

## Link
* **Kode Sumber Proyek:** [[https://github.com/Arthurleyyy/nama-repo-ai](https://github.com/Arthurleyyy/nama-repo-ai](https://github.com/Arthurleyyy/projek/tree/main/AI-Pribadi))
    (`Ai-Offline`)
* **Profil GitHub Saya:** [[https://github.com/Arthurleyyy](https://github.com/Arthurleyyy](https://github.com/Arthurleyyy))

---
