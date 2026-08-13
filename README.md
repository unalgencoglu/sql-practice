# Kitaplık — Python & MySQL Alıştırması

Python'dan MySQL veritabanına bağlanıp temel CRUD işlemlerini yapmayı öğrenmek için yazılmış küçük bir alıştırma projesi.

## Ne yapıyor

Bir `kitaplar` tablosu üzerinde:

- Kitap ekleme
- Tüm kitapları listeleme
- Kitabı "okundu" olarak işaretleme
- Kitap silme
- Belirli sayfa sayısının üzerindeki kitapları filtreleme

## Gereksinimler

- Python 3.10+
- MySQL Server

```bash
pip install mysql-connector-python python-dotenv
```

## Kurulum

### 1. Veritabanı

```sql
CREATE DATABASE deneme_db;
USE deneme_db;

CREATE TABLE kitaplar (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ad VARCHAR(100),
    yazar VARCHAR(100),
    sayfa INT,
    okundu BOOLEAN DEFAULT FALSE
);
```

### 2. Ortam değişkenleri

Proje kökünde `.env` dosyası oluştur (`.env.example` dosyasını referans alabilirsin):

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sifren
DB_NAME=deneme_db
```

`.env` dosyası `.gitignore` içindedir, repoya gönderilmez.

### 3. Çalıştır

```bash
python main.py
```

## Fonksiyonlar

| Fonksiyon | Açıklama | Dönüş |
|---|---|---|
| `baglan()` | Veritabanı bağlantısı açar | connection |
| `kitap_ekle(ad, yazar, sayfa)` | Yeni kayıt ekler | — |
| `kitaplari_listele()` | Tüm kitapları getirir | list |
| `okundu_yap(kitap_id)` | `okundu` alanını TRUE yapar | — |
| `kitap_sil(kitap_id)` | Kaydı siler | — |
| `sayfa_uzeri(limit)` | Sayfa sayısı `limit` üstü kitapları getirir | list |

## Öğrenilenler

Her sorgu şu sırayı izler:

```
baglan() → cursor() → execute() → (fetchall / commit) → close()
```

Üç kural:

1. **Placeholder kullan.** Dışarıdan gelen değer f-string ile sorguya girmez, `%s` ile gider:
   ```python
   cursor.execute("SELECT * FROM kitaplar WHERE sayfa > %s", (limit,))
   ```
   SQL ile tuple arasındaki virgül şart — yoksa Python stringi fonksiyon sanır.

2. **Yazan sorgudan sonra `commit()`.** INSERT / UPDATE / DELETE sonrası `baglanti.commit()` çağrılmazsa değişiklik kalıcı olmaz.

3. **Fetch, `close()`'dan önce.** `execute()` veri döndürmez; sonucu `fetchall()` veya `fetchone()` ile alırsın, bağlantı kapandıktan sonra alamazsın.

Not: `cursor(dictionary=True)` ile sonuçlar tuple yerine dict gelir — `kitap["ad"]` şeklinde okunur.
