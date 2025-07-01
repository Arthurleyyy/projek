# install_model.py
import argostranslate.package
import os

# Path disesuaikan dengan file kamu
package_path = "C:/Users/Sebastian/argos-models/translate-id_en-1_9.argosmodel"

if os.path.exists(package_path):
    print("🔍 File ditemukan, sedang install...")
    argostranslate.package.install_from_path(package_path)
    print("✅ Bahasa berhasil diinstal!")
else:
    print("❌ File .argosmodel tidak ditemukan!")
