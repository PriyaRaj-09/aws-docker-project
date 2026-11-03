from flask import Flask
import redis
import os

app = Flask(__name__)
r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)

@app.route("/")
def home():
    count = r.incr("visits")
    return f"<h1>Hello from Docker on AWS!</h1><p>This page has been visited {count} times 🚀</p>"

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
