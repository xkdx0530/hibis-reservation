# HIBIS Reservation

葵ちゃん専用の予約システム。Django 5 で構築しており、ローカル環境(Mac)で動作確認できます。

## 必要環境
- Python 3.10 系
- SQLite (標準で同梱)

## セットアップ
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r hibis_reservation/requirements.txt
python hibis_reservation/manage.py migrate
python hibis_reservation/manage.py createsuperuser  # 管理者作成
python hibis_reservation/manage.py runserver
```

ブラウザで `http://127.0.0.1:8000/` にアクセスすると予約画面、`/admin/` で管理者画面が利用できます。
