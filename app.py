import requests
import re

# GitHub reposu URL'si
github_url = 'https://raw.githubusercontent.com/ooguz/turkce-kufur-karaliste/master/karaliste.txt'
try:
    response = requests.get(github_url)
    response.raise_for_status()
    metin = response.text
except requests.exceptions.RequestException as e:
    print(f'Hata: {e}')
    metin = None
if metin:
    desen = re.compile(r'(\b[^\n]+\b)')
    sonuc = re.sub(desen, r'*\1*', metin)
    sonuc = re.sub(r'\n', r',\n', sonuc)
    yeni_dosya_adi = 'duzenlenmis_metin.txt'
    with open(yeni_dosya_adi, 'w', encoding='utf-8') as yeni_dosya:
        yeni_dosya.write(sonuc)

    print(f'Düzenlenmiş metin "{yeni_dosya_adi}" adlı dosyaya yazıldı.')
else:
    print('Metin indirilemedi.')
# losa.dev tarafından yazılmıştır. <3
