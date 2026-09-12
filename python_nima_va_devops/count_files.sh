#!/bin/bash
# Berilgan papkadagi (subpapkalarsiz) fayllar sonini sanaydi
# Ishlatish: ./count_files.sh <papka_yoli>

FOLDER="${1:-.}"

if [ ! -d "$FOLDER" ]; then
    echo "Xatolik: '$FOLDER' papka topilmadi"
    exit 1
fi

COUNT=$(find "$FOLDER" -maxdepth 1 -type f | wc -l)
echo "'$FOLDER' papkasida $COUNT ta fayl bor."
