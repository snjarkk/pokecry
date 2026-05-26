import re
import json

# Shift-JIS (x-sjis) でファイルを読み込む
try:
    with open('C:/Users/sokuryou10/.gemini/tmp/system32/index.html_temp', 'r', encoding='shift-jis') as f:
        html = f.read()
except UnicodeDecodeError:
    with open('C:/Users/sokuryou10/.gemini/tmp/system32/index.html_temp', 'r', encoding='cp932') as f:
        html = f.read()

# 正規表現で番号と名前を抽出
# 例: <td class=tdc1><a href="../pokewav/001.wav">001:フシギダネ</td>
pattern = re.compile(r'>(\d{3}):([^<]+)</td>')
matches = pattern.findall(html)

pokemon_list = []
for num, name in matches:
    pokemon_list.append({
        "id": num,
        "name": name.strip()
    })

# JSONファイルとして保存
with open('C:/Users/sokuryou10/.gemini/tmp/system32/pokemon_data.json', 'w', encoding='utf-8') as f:
    json.dump(pokemon_list, f, ensure_ascii=False, indent=2)

print(f"Extracted {len(pokemon_list)} pokemon.")
