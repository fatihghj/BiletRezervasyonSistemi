import sqlite3

# Veritabanını oluşturma ve tabloları ekleme
def create_database():
    conn = sqlite3.connect("database/biletler.db")
    cursor = conn.cursor()

    # Rezervasyonlar tablosu
    cursor.execute('''CREATE TABLE IF NOT EXISTS rezervasyonlar (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        sefer TEXT,
                        koltuk TEXT)''')

    conn.commit()
    conn.close()



# Rezervasyon ekleme 
def rezervasyon_ekle(sefer, koltuk):
    conn = sqlite3.connect("database/biletler.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO rezervasyonlar (sefer, koltuk) VALUES (?, ?)", (sefer, koltuk))
    conn.commit()
    conn.close()

# Rezervasyonları getirme 
def rezervasyonlari_getir():
    conn = sqlite3.connect("database/biletler.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rezervasyonlar")
    rezervasyonlar = cursor.fetchall()
    conn.close()
    return rezervasyonlar

# Seçili rezervasyonu silme 
def rezervasyon_sil(sefer, koltuk):
    conn = sqlite3.connect("database/biletler.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM rezervasyonlar WHERE sefer = ? AND koltuk = ?", (sefer, koltuk))
    conn.commit()
    conn.close()




create_database()

