from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # タイトル（必須）
    title = db.Column(db.String(100), nullable=False)

    # 詳細（任意）
    description = db.Column(db.Text, nullable=True)

    # 締切日
    deadline = db.Column(db.DateTime, nullable=True)

    # 完了状態（デフォルトFalse）
    completed = db.Column(db.Boolean, default=False)