import json

# pokemon_data.json を読み込み、修正を加えて JavaScript 用の文字列を生成
try:
    with open('C:/Users/sokuryou10/.gemini/tmp/system32/pokemon_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: pokemon_data.json not found.")
    exit(1)

# IDの修正（464ドサイドンの重複・誤記対応）
# データを確認すると {"id": "364", "name": "ドサイドン"} となっている箇所があるはず
for item in data:
    if item["name"] == "ドサイドン" and item["id"] == "364":
        item["id"] = "464"

# 重複排除とソート
unique_data = {}
for item in data:
    unique_data[item["id"]] = item["name"]

sorted_ids = sorted(unique_data.keys())

# JavaScriptオブジェクト形式の文字列を作成
js_lines = []
for pid in sorted_ids:
    name = unique_data[pid]
    # 4桁にパディング
    pid4 = pid.zfill(4)
    # MP3かWAVかの判定（387番以降がMP3というルールを適用）
    ext = "mp3" if int(pid) >= 387 else "wav"
    js_lines.append(f'  "{pid4}": {{ name: "{name}", ext: "{ext}" }}')

js_content = "const POKEMON_DB = {\n" + ",\n".join(js_lines) + "\n};"

with open('C:/Users/sokuryou10/.gemini/tmp/system32/pokemon_db.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Generated pokemon_db.js with {len(js_lines)} entries.")
