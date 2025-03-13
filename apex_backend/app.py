from flask import Flask, render_template

app = Flask(__name__)


@app.route("/api/heroes", methods=["GET"])
def get_heroes():
    """获取所有英雄的列表"""
