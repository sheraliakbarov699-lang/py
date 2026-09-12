# Python interpretatorlari: CPython va PyPy

Python tilida bir nechta interpretator implementatsiyasi mavjud bo'lib, eng
ko'p tarqalgani CPython hisoblanadi. CPython — Python'ning rasmiy va standart
implementatsiyasi bo'lib, C tilida yozilgan. Kod ishga tushirilganda avval
baytkodga (.pyc) aylantiriladi, keyin CPython virtual mashinasi bu baytkodni
qator-qator interpretatsiya qiladi. Uning eng katta afzalligi — deyarli
barcha kutubxonalar (NumPy, Django, Flask va h.k.) aynan shu implementatsiyaga
mo'ljallab yozilgan, ya'ni to'liq moslik ta'minlanadi. Kamchiligi shundaki,
har bir operatsiya oldindan mashina kodiga kompilyatsiya qilinmasdan,
to'g'ridan-to'g'ri interpretatsiya qilinganligi sababli ishlash tezligi
cheklangan.

PyPy esa muqobil implementatsiya bo'lib, o'zining ichida JIT (Just-In-Time)
kompilyator ishlatadi. Bu degani, dastur ishlayotgan vaqtning o'zida tez-tez
qaytarilayotgan kod qismlari (masalan, uzoq tsikllar) real vaqt rejimida
mashina kodiga aylantirib olinadi. Natijada, ayniqsa hisoblash ko'p bo'lgan
va uzoq ishlaydigan dasturlarda PyPy CPython'dan bir necha barobar (ba'zida
4-10 marta) tezroq ishlashi mumkin. Biroq PyPy'ning ham o'z kamchiliklari
bor: ba'zi C tilida yozilgan kengaytmalar (C-extension) bilan to'liq mos
kelmasligi, shuningdek dastur ishga tushish vaqtining biroz sekinroq bo'lishi
mumkin.

Xulosa qilib aytganda, kundalik va odatiy loyihalar uchun, ayniqsa
kutubxonalarga tayanadigan ishlarda CPython eng ishonchli tanlov
hisoblanadi. Lekin sof hisoblash yuklamasi katta bo'lgan, tezlik muhim rol
o'ynaydigan loyihalarda PyPy sinab ko'rishga arziydigan variant.
