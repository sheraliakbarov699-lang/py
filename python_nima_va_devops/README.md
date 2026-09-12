# 1.1 Amaliy vazifa

## 1-2. Virtual muhit, requests o'rnatish va requirements.txt

Bu ikki qadam sizning shaxsiy kompyuteringizda internet orqali bajarilishi kerak
(bu muhitda internetga chiqish imkoni yo'q). Quyidagi buyruqlarni terminalda
ishga tushiring:

```bash
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

pip install requests
pip freeze > requirements.txt
```

Natijada shu papkada `requirements.txt` fayli hosil bo'ladi, uni ham loyihaga
qo'shib qo'ying.

## 3. python3 --version va which python3

O'zingizning terminalingizda quyidagi buyruqlarni bajarib, natijasini pastdagi
`konspekt.txt` fayliga (yoki shu joyga) qo'shib qo'ying:

```bash
python3 --version
which python3      # Windows: where python
```

`konspekt.txt` — namuna format bilan tayyorlab qo'yildi, natijani o'zingiz
to'ldiring.

## 4. argparse bilan --name parametrli skript

`greet.py` faylida tayyor:

```bash
python3 greet.py --name Shuhrat
# Salom, Shuhrat! Xush kelibsiz.
```

## 5. Bash vs Python — fayllarni sanash

Bitta vazifa ikki xil tilda bajarildi: `count_files.sh` (Bash) va
`count_files.py` (Python).

```bash
./count_files.sh .
python3 count_files.py .
```

Ikkalasi ham papkadagi (subpapkalarsiz) fayllar sonini bir xil natija bilan
qaytaradi.

### Xulosa

- **Bash** varianti qisqaroq va tezroq yoziladi, chunki `find`/`wc` kabi tayyor
  Unix vositalaridan foydalanadi — lekin faqat Unix-tizimlarda ishonchli
  ishlaydi va xato holatlarni (masalan, papka mavjud emasligini) qo'lda
  tekshirish talab qiladi.
- **Python** varianti biroz uzunroq, ammo o'qilishi oson, xatoliklarni
  (`try/except`) aniqroq boshqaradi va operatsion tizimdan qat'i nazar bir xil
  ishlaydi (kross-platforma).
- Oddiy, bir martalik skript uchun Bash qulayroq; kengroq mantiq yoki boshqa
  tizimlarda ham ishlashi kerak bo'lgan skriptlar uchun Python afzalroq.
