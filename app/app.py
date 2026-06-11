from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

# Hardcoded secrets (intentional for TMAS demo)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DB_PASSWORD = "super_secret_password_123"
STRIPE_SECRET_KEY = "stripe_live_key_51Hexample4242424242DemoOnlyNotReal"

DB_PATH = "/tmp/demo.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
    conn.execute("INSERT OR IGNORE INTO users VALUES (1, 'admin', 'admin@example.com')")
    conn.commit()
    conn.close()


@app.route("/")
def index():
    return "TrendAI Container Security Demo - Intentionally Vulnerable App"


@app.route("/user")
def get_user():
    # SQL Injection vulnerability (intentional)
    name = request.args.get("name", "")
    conn = sqlite3.connect(DB_PATH)
    query = f"SELECT * FROM users WHERE name = '{name}'"
    result = conn.execute(query).fetchall()
    conn.close()
    return str(result)


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
