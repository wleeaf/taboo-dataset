# Taboo Dataset (37,500 Kelime / 150 Kategori)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Cards](https://img.shields.io/badge/Cards-37%2C500-blue.svg)](#)
[![Categories](https://img.shields.io/badge/Categories-150-success.svg)](#)
[![Encoding](https://img.shields.io/badge/Encoding-UTF--8-informational.svg)](#)

Türkçe dilinde geliştirilen oyunlar, doğal dil işleme (NLP) araştırmaları, kelime dağarcığı modellemeleri ve bilgi yarışması tabanlı yapay zekâ uygulamaları için titizlikle kurgulanmış, kolay, orta ve zor seviyelerde **37.500 kartlık kapsamlı Türkçe Tabu veri seti**.

---

## 📌 Veri Seti Özellikleri

- **150 Ayrık Kategori:** Fen bilimlerinden sanata, felsefeden popüler kültüre, mutfaktan spora ve coğrafyaya kadar birbirini tekrar etmeyen 150 spesifik alan.
- **Her Kategoride 250 Benzersiz Kart:** Kategori bazında sıfır tekrar (0 duplikasyon). Toplam 37.500 kart.
- **Dengeli Kelime ve Fiil Dağılımı:** İsimler, kavramlar, terimler ve her kategoriye özel olarak eklenmiş otantik eylemler/fiiller (`fiil`).
- **3 Zorluk Seviyesi:** Her kart için belirlenmiş `zorluk` seviyesi (`kolay`, `orta`, `zor`).
- **Yüksek Nitelikli Tanımlar:** Her kavram için yalın, didaktik ve net açıklamalar (`aciklama`).
- **5 Yasaklı Kelime:** Kolay tahminleri engelleyen, kavramın çekirdek çağrışımlarını içeren özenle seçilmiş 5 kısıtlayıcı sözcük.
- **Doğal Dil Uyumu:** Sözcükler büyük ölçüde 1-2 kelimeden oluşur, yapay kalıplardan ve dolgu sözcüklerden arındırılmıştır.
- **JSON Formatı:** Kolay parse edilebilen, UTF-8 formatında yapılandırılmış açık kaynak veri mimarisi.

---

## 📂 Veri Şeması

Her JSON dosyası ilgili kategoriye ait 250 adet nesne içeren bir liste barındırır:

```json
[
  {
    "id": 1,
    "kategori": "astronomi",
    "kelime": "Karasadelik",
    "aciklama": "Işığın bile kaçamadığı son derece güçlü çekim alanına sahip gök cismi.",
    "yasakli_kelimeler": [
      "uzay",
      "çekim",
      "ışık",
      "olay ufku",
      "yıldız"
    ],
    "zorluk": "kolay"
  }
]
```

---

## 🔍 Doğrulama (Validation)

Veri setinin bütünlüğünü ve kurallara uygunluğunu test etmek için:

```bash
python3 validate_cards.py
```

---

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) altında sunulmaktadır.
