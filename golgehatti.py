import subprocess
import sys
import os
import re
import time

def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install_and_import('requests')
import requests

def get_unique_filename(base_name, extension):
    counter = 1
    file_name = f"{base_name}.{extension}"
    while os.path.exists(file_name):
        counter += 1
        file_name = f"{base_name}({counter}).{extension}"
    return file_name

def golgehatti():
    base_url = "https://www.cyberakademi.org/Forum/proxies/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    tum_proxyler = set()
    sayfa = 1
    
    print("--- CyberAkademi.Org Golge Hatti Taramasi Baslatildi ---")
    
    while True:
        url = f"{base_url}?page={sayfa}" if sayfa > 1 else base_url
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code != 200:
                break
            proxy_deseni = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,5}'
            bulunanlar = re.findall(proxy_deseni, response.text)
            if not bulunanlar:
                break
            for p in bulunanlar:
                tum_proxyler.add(p)
            time.sleep(0.5)
            print(f"Sayfa {sayfa} taraniyor...", end="\r")
            sayfa += 1
        except:
            break

    if tum_proxyler:
        final_filename = get_unique_filename("golgehattiproxy", "txt")
        with open(final_filename, "w", encoding="utf-8") as f:
            for proxy in sorted(tum_proxyler):
                f.write(proxy + "\n")
        print(f"\nISLEM TAMAMLANDI!")
        print(f"Dosya: {final_filename}")
        print(f"Toplam: {len(tum_proxyler)} adet")

if __name__ == "__main__":
    golgehatti()
    input("\nKapatmak icin Enter'a bas...")