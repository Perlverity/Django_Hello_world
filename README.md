#### 仮想環境構築
```
python -m venv djangovenv
```

#### 仮想環境の起動
```
source djangovenv/bin/activate
```

#### Django のインストール
```
pip install django==3.0.0
```

#### プロジェクト （Project） の作成
```
django-admin startproject helloworldproject
```
#### 開発サーバの起動
```
python manage.py runserver
```

#### アプリケーションの作成
```
python manage.py startapp helloworldapp
```