# Tabu Veri Seti (10.000 Kart / 100 Kategori)

Bu veri seti, orta-zor seviyede hazırlanmış 100 ayrı spesifik kategoride toplam 10.000 adet Tabu kartından oluşur.

## Veri Formatı ve Standartlar
- **Dosya Formatı:** JSON (Her kategori ayrı bir `.json` dosyasında)
- **Kart Sayısı:** Her kategoride tam 100 adet benzersiz kart
- **Harf Formatı:** Tamamı küçük harf (lowercase)
- **Karakter Desteği:** Türkçe karakterler (`ç`, `ğ`, `ı`, `ö`, `ş`, `ü`) eksiksiz korunmuştur.
- **Her Kartın Yapısı:**
  - `id`: Kategori içi 1-100 arası sıralı tam sayı
  - `kategori`: Kategori adı (tek kelime, küçük harf)
  - `kelime`: Tabu hedef kelimesi/terimi
  - `aciklama`: Eğitici, kısa ve net kavram açıklaması
  - `yasakli_kelimeler`: 5 adet ilgili yasaklı kelime listesi

## Kategoriler (100 Adet)
1. Doğa & Fen: astronomi, meteoroloji, jeoloji, osinografi, botanik, zooloji, mikrobiyoloji, genetik, kuantum, termodinamik, optik, akustik, ekoloji, paleontoloji, kimya
2. Tıp & Sağlık: noroloji, farmakoloji, immunoloji, anatomi, patoloji, cerrahi, pediyatri, psikiyatri, dermatoloji, epidemiyoloji
3. Zihin & Felsefe: psikoloji, felsefe, epistemoloji, mantik, etik, ezoterizm, mitoloji, teoloji
4. Toplum & Kültür: sosyoloji, antropoloji, etnografi, linguistik, retorik, pedagoji, gastronomi, numizmatik, filateli, koreografi, ergonomi
5. Sanat & Tasarım: mimarlik, heykeltiraslik, resim, seramik, tipografi, sinematografi, fotografcilik, muzikoloji, tiyatro, tekstil, kaligrafi
6. Tarih & Coğrafya: arkeoloji, epigrafi, kartografya, jeomorfoloji, monarsi, savas, diplomasi, casusluk
7. Hukuk & Ekonomi: hukuk, ceza, kriminoloji, iktisat, ekonometri, bankacilik, borsa, pazarlama, lojistik, burokrasi, aktuerya
8. Teknoloji & Mühendislik: algoritmalar, siber, donanim, robotik, telekomunikasyon, yapayzeka, kripto, nanoteknoloji, mekatronik, metalurji
9. Zanaat & Araçlar: marangozluk, demircilik, tesisat, saatcilik, deri, matbaacilik
10. Spor & Hareket: havacilik, denizcilik, dagcilik, satranc, dalgiclik, binicilik, dovus, balikcilik, atletizm, astronotik
