# Taboo Dataset (10,000 Kelime / 100 Kategori)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Cards](https://img.shields.io/badge/Cards-10%2C000-blue.svg)](#)
[![Categories](https://img.shields.io/badge/Categories-100-success.svg)](#)
[![Encoding](https://img.shields.io/badge/Encoding-UTF--8-informational.svg)](#)

Türkçe dilinde geliştirilen oyunlar, doğal dil işleme (NLP) araştırmaları, kelime dağarcığı modellemeleri ve bilgi yarışması tabanlı yapay zekâ uygulamaları için titizlikle kurgulanmış, **orta-zor (hafiften zor)** seviyede **10.000 kartlık kapsamlı Tabu veri seti**.

---

## 📌 Veri Seti Özellikleri

- **100 Ayrık Kategori:** Fen bilimlerinden sanata, felsefeden mühendisliğe, hukuktan zanaata kadar birbirini tekrar etmeyen 100 spesifik alan.
- **Her Kategoride 100 Benzersiz Kart:** Kategori bazında sıfır tekrar (0 duplikasyon).
- **Yüksek Nitelikli Tanımlar:** Her kavram için yalın, didaktik ve net açıklamalar (`aciklama`).
- **5 Yasaklı Kelime:** Kolay tahminleri engelleyen, kavramın çekirdek çağrışımlarını içeren özenle seçilmiş 5 kısıtlayıcı sözcük.
- **Tamamen Küçük Harf:** Doğal dil işleme (NLP) ve metin madenciliği aşamalarında ön işleme kolaylığı sağlaması amacıyla tüm metinler küçük harf (`lowercase`) standardındadır.
- **Doğru Türkçe Karakter Desteği:** `ç, ğ, ı, ö, ş, ü` karakterleri eksiksiz korunmuş; ASCII indirgemesi yapılmamıştır.

---

## 📂 Veri Formatı ve Şema

Veriler `data/` dizini altında her kategori için bağımsız `.json` dosyaları halinde tutulur.

### JSON Kart Şeması
```json
{
  "id": 1,
  "kategori": "astronomi",
  "kelime": "pulsar",
  "aciklama": "kendi ekseni etrafında son derece hızlı dönen ve düzenli aralıklarla radyo dalgaları yayan nötron yıldızı.",
  "yasakli_kelimeler": [
    "nötron",
    "radyo",
    "yıldız",
    "sinyal",
    "dönme"
  ]
}
```

---

## 🗂️ Kategori Dağılımı (100 Kategori)

<details>
<summary><b>1. Doğa & Temel Bilimler (15 Kategori - 1.500 Kart)</b></summary>

- `astronomi`: Gök cisimleri, kozmoloji, astrofizik dinamikleri
- `meteoroloji`: Atmosferik olaylar, basınç sistemleri, iklim mekanizmaları
- `jeoloji`: Yerkabuğu kırıkları, mineraloji, petrografi
- `osinografi`: Okyanus akıntıları, denizaltı topoğrafyası, bentik ekoloji
- `botanik`: Bitki fizyolojisi, anatomisi, tohum ve doku tipleri
- `zooloji`: Hayvan fizyolojisi, adaptasyonları ve davranışları
- `mikrobiyoloji`: Bakteriler, virüsler, parazitler, hücresel yapılar
- `genetik`: Kalıtım, mutasyonlar, DNA modifikasyonları
- `kuantum`: Dalga mekaniği, parçacık fiziği, kuantum durumları
- `termodinamik`: Isı transferi, entropi, hal değişimleri
- `optik`: Işık kırınımı, dalga optiği, lazer fiziği
- `akustik`: Ses dalgaları, frekans dinamikleri, rezonans
- `ekoloji`: Biyomlar, besin ağları, trofik dinamikler
- `paleontoloji`: Fosilleşme, jeolojik çağlar, soyu tükenmiş taksonlar
- `kimya`: Kimyasal bağlar, reaksiyon kinetiği, çözelti dengeleri
</details>

<details>
<summary><b>2. Tıp & Sağlık Bilimleri (10 Kategori - 1.000 Kart)</b></summary>

- `noroloji`: Sinir iletimi, beyin lobları, nöropatolojiler
- `farmakoloji`: Etken maddeler, reseptör etkileşimleri, farmakokinetik
- `immunoloji`: Antikorlar, hücresel bağışıklık, alerjen mekanizmaları
- `anatomi`: İskelet-kas yapıları, damar ağları, iç organ morfolojisi
- `patoloji`: Lezyonlar, nekroz türleri, hücresel anomaliler
- `cerrahi`: Operasyon teknikleri, insizyonlar, cerrahi ekipmanlar
- `pediyatri`: Çocuk gelişimi, neonatal refleksler, pediatrik tablolar
- `psikiyatri`: Klinik tanılar, duygudurum süreçleri, terapötik kavramlar
- `dermatoloji`: Cilt katmanları, dermatitler, epidermal patolojiler
- `epidemiyoloji`: Bulaş paternleri, filyasyon, salgın dinamiği
</details>

<details>
<summary><b>3. Zihin & Düşünce (8 Kategori - 800 Kart)</b></summary>

- `psikoloji`: Bilişsel yanılgılar, algı mekanizmaları, savunma düzenekleri
- `felsefe`: Ontoloji, varlık felsefesi, felsefi açmazlar
- `epistemoloji`: Bilgi kuramı, gerekçelendirme, septisizm
- `mantik`: Safsatalar, kıyaslar, formel mantık önermeleri
- `etik`: Ahlak ikilemleri, deontoloji, teleoloji
- `ezoterizm`: Sembolizm, kadim öğretiler, hermetizm
- `mitoloji`: Panteonlar, arketipik anlatılar, mitik figürler
- `teoloji`: Kutsal metin hermenötiği, doktrinler, inanç felsefesi
</details>

<details>
<summary><b>4. Toplum & Kültür (11 Kategori - 1.100 Kart)</b></summary>

- `sosyoloji`: Toplumsal tabakalaşma, yabancılaşma, normatif yapılar
- `antropoloji`: İlkel kültürler, kabile pratikleri, evrimsel antropoloji
- `etnografi`: Halk gelenekleri, saha etnografisi, kültürel ritüeller
- `linguistik`: Fonetik, semantik, morfoloji, dil aileleri
- `retorik`: Hitabet sanatları, ikna stratejileri, demagoji
- `pedagoji`: Öğrenme modelleri, didaktik yöntemler, eğitim teorileri
- `gastronomi`: Pişirme teknikleri, mutfak bilimi, gurme terminolojisi
- `numizmatik`: Madeni paralar, sikke darpları, nümizmatik analiz
- `filateli`: Posta pulları, damgalar, filatelik terimler
- `koreografi`: Dans adımları, sahne hareket düzeni, uzamsal ritim
- `ergonomi`: Çalışma mekaniği, biyomekanik uyum, postür ergonomisi
</details>

<details>
<summary><b>5. Sanat & Tasarım (11 Kategori - 1.100 Kart)</b></summary>

- `mimarlik`: Taşıyıcı sistemler, strüktürler, cephe ve mekan elemanları
- `heykeltiraslik`: Yontma, döküm teknikleri, rölyef, kaideler
- `resim`: Renk teorisi, fırça teknikleri, kompozisyon kuralları
- `seramik`: Tornalama, sırlama kimyası, fırınlama teknikleri
- `tipografi`: Yazı anatomisi, harf boşlukları, serif türleri
- `sinematografi`: Kamera hareketleri, kadraj, aydınlatma, kurgu
- `fotografcilik`: Diyafram, pozlama dinamikleri, sensör fiziği
- `muzikoloji`: Armoni kuralları, makamlar, solfej, akor yapıları
- `tiyatro`: Dramaturji, sahne teknikleri, tirat, oyunculuk metotları
- `tekstil`: Dokuma örgüleri, iplik türleri, terbiye işlemleri
- `kaligrafi`: Yazı estetiği, meşk usulleri, divit ve mürekkep sanatı
</details>

<details>
<summary><b>6. Tarih & Coğrafya (8 Kategori - 800 Kart)</b></summary>

- `arkeoloji`: Tabakalanma, stratigrafi, antik kazı metodolojisi
- `epigrafi`: Kitabe çözümleri, antik yazıtlar, paleografi
- `kartografya`: Projeksiyonlar, izohips haritaları, ölçek hesapları
- `jeomorfoloji`: Karstik aşınım şekilleri, vadi tipleri, falezler
- `monarsi`: Saray teşkilatı, veraset sistemleri, hanedan protokolü
- `savas`: Kuşatma taktikleri, askeri tahkimatlar, stratejik manevralar
- `diplomasi`: Uluslararası protokoller, elçilik usulleri, antlaşmalar
- `casusluk`: Kriptografi, gizli operasyonlar, istihbarat metodolojisi
</details>

<details>
<summary><b>7. Hukuk, Yönetim & Ekonomi (11 Kategori - 1.100 Kart)</b></summary>

- `hukuk`: Usul hukuku, dava süreçleri, normlar hiyerarşisi
- `ceza`: İnfaz hukuku, suç unsurları, beraat ve tecrit
- `kriminoloji`: Olay yeri inceleme, profil çıkarma, balistik
- `iktisat`: Makro dengeler, enflasyon teorileri, piyasa başarısızlıkları
- `ekonometri`: Regresyon analizleri, zaman serileri, tahmin modelleri
- `bankacilik`: Likidite yönetimi, kredi araçları, mevzuat
- `borsa`: Türev araçlar, opsiyonlar, arbitraj, emir tipleri
- `pazarlama`: Tüketici davranışları, pazar segmentasyonu, konumlandırma
- `lojistik`: Tedarik zinciri, navlun, gümrükleme süreçleri
- `burokrasi`: İdari hiyerarşi, evrak yönetimi, resmi prosedürler
- `aktuerya`: Risk havuzları, sigorta matematiği, mortalite tabloları
</details>

<details>
<summary><b>8. Bilişim & Mühendislik (10 Kategori - 1.000 Kart)</b></summary>

- `algoritmalar`: Sıralama yapıları, graf teorisi, zaman karmaşıklığı
- `siber`: Sızma testleri, şifreleme, güvenlik duvarları, exploitler
- `donanim`: Mikroişlemci mimarileri, veri yolları, yarı iletkenler
- `robotik`: Kinematik, aktüatörler, yapay uzuvlar, kontrol sistemleri
- `telekomunikasyon`: Modülasyon, fiberoptik, bant genişliği dinamikleri
- `yapayzeka`: Sinir ağları, model ağırlıkları, optimizasyon yöntemleri
- `kripto`: Blokzincir, konsensüs protokolleri, kriptografik özetler
- `nanoteknoloji`: Nanotüpler, atomik kuvvet mikroskopisi, yüzey kaplama
- `mekatronik`: Pnömatik, hidrolik valfler, PLC sistemleri
- `metalurji`: Alaşım fazları, ısıl işlem metodolojileri, korozyon
</details>

<details>
<summary><b>9. Zanaat & Pratik Alanlar (6 Kategori - 600 Kart)</b></summary>

- `marangozluk`: Zıvana geçmeler, rende/planya usulleri, ahşap dokusu
- `demircilik`: Örs, dövme teknikleri, tavlama, su verme
- `tesisat`: Borulama armatürleri, sızdırmazlık, hidrolik tesisat
- `saatcilik`: Zemberek mekanizmaları, eşapman, tulumba sistemleri
- `deri`: Tabaklama, sepileme kimyası, saraciye zanaatı
- `matbaacilik`: Ofset kalıpları, tipo baskı, forma ciltleme teknikleri
</details>

<details>
<summary><b>10. Spor, Taktik, Deniz & Havacılık (10 Kategori - 1.000 Kart)</b></summary>

- `havacilik`: Aerodinamik profiller, aviyonik sistemler, seyrüsefer
- `denizcilik`: Manevra komutları, denizcilik bağları, seyir fenerleri
- `dagcilik`: Emniyet istasyonları, buzul tırmanışı, teknik ekipman
- `satranc`: Gambitler, taktik kombinasyonlar, piyon formasyonları
- `dalgiclik`: Dekompresyon tabloları, regülatör sistemleri, dalış fiziği
- `binicilik`: At yürüyüşleri, eyer takımları, dresaj terimleri
- `dovus`: Klinç pozisyonları, fırlatmalar, eklem kilitleri, gard
- `balikcilik`: Olta donanımları, parakete, ağ teknikleri, iğne tipleri
- `atletizm`: Takoz çıkışları, branş teknikleri, saha müsabakaları
- `astronotik`: İtki sistemleri, yörünge mekaniği, uzay kapsülü operasyonları
</details>

---

## 💻 Kullanım Örnekleri (Python)

### 1. Belirli Bir Kategoriyi Yükleme
```python
import json

with open("data/astronomi.json", "r", encoding="utf-8") as f:
    cards = json.load(f)

card = cards[0]
print(f"Kelime: {card['kelime']}")
print(f"Tanım: {card['aciklama']}")
print(f"Yasaklılar: {', '.join(card['yasakli_kelimeler'])}")
```

### 2. Tüm Veri Setini Tek Bir Listede Birleştirme
```python
import glob
import json

all_cards = []
for file_path in glob.glob("data/*.json"):
    with open(file_path, "r", encoding="utf-8") as f:
        all_cards.extend(json.load(f))

print(f"Yüklenen Toplam Tabu Kartı Sayısı: {len(all_cards)}")
```

---

## 📜 Lisans

Bu veri seti [MIT Lisansı](LICENSE) kapsamında açık kaynaklı olarak sunulmuştur. Hem ticari hem de akademik projelerinizde serbestçe kullanabilir, genişletebilir veya entegre edebilirsiniz.
