import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

def baglan():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

def kitap_ekle(ad, yazar, sayfa):
    baglanti = baglan()
    cursor = baglanti.cursor()
    
    cursor.execute (
            """
            INSERT INTO kitaplar (ad, yazar, sayfa)
            VALUES (%s, %s, %s)
            """
            (ad, yazar, sayfa))
    baglanti.commit()
    cursor.close()
    baglanti.close()
    
