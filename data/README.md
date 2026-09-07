# Tabu Veri Seti (37.278 Kart / 150 Kategori)

Bu veri seti; kolay, orta ve zor seviyelerde hazırlanmış 150 ayrı spesifik kategoride toplam 37.278 adet Tabu kartından oluşur.

## Veri Formatı ve Standartlar
- **Dosya Formatı:** JSON (Her kategori ayrı bir `.json` dosyasında)
- **Kart Sayısı:** Kategori başına değişken sayıda benzersiz kart (Toplam: 37.278 kart)
- **Karakter Desteği:** Türkçe karakterler (`ç`, `ğ`, `ı`, `ö`, `ş`, `ü`) eksiksiz korunmuştur.
- **Her Kartın Yapısı:**
  - `id`: Kategori içi 1’den başlayan sıralı tam sayı
  - `kategori`: Kategori adı (küçük harf)
  - `kelime`: Tabu hedef kelimesi veya eylemi (anlamlı, doğal ve eksiksiz ifadeler; zorunlu kelime sayısı yoktur)
  - `aciklama`: Eğitici, kısa ve net kavram açıklaması
  - `yasakli_kelimeler`: 5 adet ilgili küçük harfli yasaklı kelime listesi
  - `zorluk`: "kolay", "orta" veya "zor"

## Kategoriler (150 Adet)
Toplam 150 dosya `data/` dizini altında yer almaktadır.
