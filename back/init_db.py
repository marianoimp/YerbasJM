import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sql_path = os.path.join(BASE_DIR, "datos.sql")

with open(sql_path, "r") as f:
    sql = f.read()

conn=None
cursor=None

try:
    conn = mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        port = os.getenv('DB_PORT')
    )
    cursor= conn.cursor()

    for query in sql.split(";"):
        query = query.strip()
        if query:
            try:
                print(f"\nEjecutando:\n{query}\n")
                cursor.execute(query)
                print("✔ Ejecutada correctamente")
            except mysql.connector.Error as e:
                print("❌ Error en esta query:", e)

    conn.commit()
    print("Base inicializada correctamente")

except mysql.connector.Error as e:
    print("Error en la base:", e)
    if conn:
        conn.rollback()

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()