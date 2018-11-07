#!/bin/sh

wget https://www.clearquran.com/downloads/quran-verse-by-verse-text.zip -O quran.zip
rm -rf quran
mkdir -p quran
unzip -q ./quran.zip -d ./quran
rm ./quran/_readme.txt
echo "" > quran.txt
for f in ./quran/*.txt; do
  cat "$f" >> quran.txt
  echo "" >> quran.txt
done
rm -rf quran
rm quran.zip
