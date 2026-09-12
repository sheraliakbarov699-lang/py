# 4. requirements.txt yaratish va boshqa virtual muhitda sinash

```bash
# joriy virtual muhitni faollashtirish
source venv/bin/activate

# o'rnatilgan paketlarni faylga yozish
pip freeze > requirements.txt

# yangi bo'sh virtual muhit yaratish
python3 -m venv venv_test
source venv_test/bin/activate

# requirements.txt orqali paketlarni o'rnatish
pip install -r requirements.txt

# tekshirish
pip list
```

# 5. Skriptni crontab orqali avtomatik ishga tushirish

```bash
crontab -e
```

```
* * * * * /usr/bin/python3 /home/user/script.py start >> /home/user/cron_log.txt 2>&1
```

## Bajarish jarayonida duch kelgan qiyinchiliklar

- Cron o'z muhitida ishlaydi va terminaldagi PATH'dan farq qiladi — shuning
  uchun python3 yoki virtual muhitdagi interpretatorni to'liq (absolyut) yo'l
  bilan ko'rsatish kerak bo'ldi.
- Skript ichida nisbiy yo'llar ishlatilsa, cron ularni topolmadi — barcha
  fayl yo'llarini absolyut qilib yozishga to'g'ri keldi.
- Xatoliklarni terminalda ko'rib bo'lmaydi, shuning uchun natijani log
  faylga yo'naltirish (`>> log.txt 2>&1`) zarur bo'ldi.
- `start` buyrug'i uchun kerakli argumentlar (masalan `--port`) unutilib
  qolsa, skript cron orqali xatolik bilan to'xtaydi, lekin bu haqda faqat log
  faylni ochib ko'rgandan keyin bilib oldim.
