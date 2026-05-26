# Pokémon Cry (pokecry) システム仕様書

ポケモンの鳴き声を識別する「IDENTIFY」モードと、鳴き声から名前を当てる「QUIZ」モードを備えたウェブアプリケーションです。

## 1. システム概要
HTML5, CSS3, JavaScript (Vanilla JS) で構築されたシングルページアプリケーションです。スマートフォンの操作（タップ＆ホールド）に最適化された UI を持ち、ブラウザのみで動作します。

## 2. 主要機能
### 2.1 IDENTIFY（識別）モード
*   **録音機能**: マイクからポケモンの鳴き声を録音。
*   **特徴量抽出**: Web Audio API を使用し、音の大きさ（RMS）、明るさ（Brightness）、変化量（Flux）を抽出（Fingerprinting v5）。
*   **波形可視化**: 録音中の音声をリアルタイムでキャンバスに描画。
*   **検索・比較**: IndexedDB にキャッシュされた既知のポケモンの鳴き声データと比較し、一致率を算出。
*   **ランキング表示**: 上位10位までの一致したポケモンを表示。

### 2.2 QUIZ（クイズ）モード
*   **クイズ対象の登録**: 特定のポケモンをクイズ対象として追加・削除可能（最大30匹）。
*   **4択クイズ**: ランダムに選ばれた鳴き声を聴き、正しい名前を4択から選択。
*   **再生インジケーター**: 音声再生中、♪マークが点灯。
*   **統計機能**: 本日の正解数と正解率を記録し、LocalStorage に保存。
*   **自動遷移**: 正誤判定後、2.5秒で自動的に次の問題へ移行。

## 3. ディレクトリ構成
```
pokecry/
├── index.html            # メインアプリケーション（HTML/CSS/JS）
├── pokemon_db.js         # ポケモンの名前と拡張子の定義
├── pokemon_data.json     # ポケモンのメタデータ
├── pokemon_names.txt     # ポケモン名のリスト
├── generate_js_db.py     # テキストデータから JS データベースを生成するスクリプト
├── extract_pokemon.py    # ポケモンデータを抽出するスクリプト
├── download_pokewav.ps1  # 外部サーバーから音声ファイルを一括ダウンロードするスクリプト
└── pokewav/              # 音声ファイル（.wav / .mp3）の格納フォルダ
```

## 4. 技術仕様
*   **Frontend**: HTML5, CSS3 (CSS Variables), JavaScript (ES6+)
*   **Audio Engine**: Web Audio API (AudioContext, AnalyserNode)
*   **Storage**: 
    *   **IndexedDB**: 特徴量データ（Fingerprints）のキャッシュ。
    *   **LocalStorage**: クイズの登録リスト、正解率統計。
*   **Database**: No.0001 (フシギダネ) から No.0649 (ゲノセクト) までをサポート。

## 5. 修正履歴

### 2026-05-26
*   **クイズモードの音声再生不良を修正**
    *   `AudioContext.resume()` を追加し、ブラウザの自動再生ポリシーによる制限を回避。
    *   `fetch` 時のエラーハンドリングを追加。
*   **再生インジケーターの実装**
    *   音声再生中、再生ボタンの ♪ アイコンが赤色（`--primary`）に点灯するよう CSS と JS を更新。
*   **プロジェクトの整理**
    *   関連ファイルを `pokecry` ディレクトリに集約。
    *   本仕様書（`README.md`）の作成。

---
&copy; 2026 Pokémon Cry System
