from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    try:
        connection = psycopg2.connect(
            user="flaskuser",
            password="password",
            host="postgres",
            port="5432",
            database="flaskdb"
        )
        return "Database connection successful!"
    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
