import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

def baglan():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def kitap_ekle(ad, yazar, sayfa):
    baglanti = baglan()
    cursor = baglanti.cursor()
    
    cursor.execute (
            """
            INSERT INTO kitaplar (ad, yazar, sayfa)
            VALUES (%s, %s, %s)
            """,
            (ad, yazar, sayfa))
    baglanti.commit()
    cursor.close()
    baglanti.close()
    
def kitaplari_listele():
    baglanti = baglan()
    cursor = baglanti.cursor()
    
    cursor.execute(
            """
            SELECT * FROM kitaplar
            """,
    )
    sonuc = cursor.fetchall()
    cursor.close()
    baglanti.close()
    return sonuc

def okundu_yap(kitap_id):
    baglanti = baglan()
    cursor = baglanti.cursor()
    
    cursor.execute(
    """
    UPDATE kitaplar SET okundu = True WHERE id = %s
    """,
    (kitap_id,))
    
    baglanti.commit()
    cursor.close()
    baglanti.close()
    
def kitap_sil(kitap_id):
    baglanti = baglan()
    cursor = baglanti.cursor()
    
    cursor.execute(
    """
    DELETE FROM kitaplar WHERE id = %s
    """,
    (kitap_id,))
    
    baglanti.commit()
    cursor.close()
    baglanti.close()