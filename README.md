# convert-image

HEIC画像をPNG形式に変換するツール

## セットアップ

```bash
uv sync
```

## 使用方法

```bash
# デフォルト（image/20260101 → image/converted）
uv run main.py

# 入力ディレクトリを指定
uv run main.py path/to/heic/files

# 入力・出力ディレクトリを指定
uv run main.py path/to/heic/files path/to/output
```

## 機能

- HEIC/heic ファイルを PNG に一括変換
- 自動的に出力ディレクトリを作成
- 変換進捗の表示
- エラーハンドリング
