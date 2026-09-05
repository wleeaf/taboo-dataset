import sys
from card_utils import add_and_save_verbs

# 1. TIPOGRAFI (50 verbs: 12 kolay, 24 orta, 14 zor)
tipografi_verbs = [
    # Kolay (12)
    {
        "kelime": "Yazı Tipi Seçmek",
        "aciklama": "Tasarım için uygun bir font veya karakter ailesi belirlemek.",
        "yasakli_kelimeler": ["font", "tasarım", "belirlemek", "karakter", "uygun"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Yazıyı Büyütmek",
        "aciklama": "Metnin punto veya piksel boyutunu artırmak.",
        "yasakli_kelimeler": ["punto", "boyut", "metin", "artırmak", "küçük"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Yazıyı Küçültmek",
        "aciklama": "Metin karakterlerinin boyutunu daha küçük bir dereceye indirmek.",
        "yasakli_kelimeler": ["boyut", "punto", "küçük", "indirmek", "metin"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Kalınlaştırmak",
        "aciklama": "Yazıyı vurgulamak için bold (kalın) karakter stiline getirmek.",
        "yasakli_kelimeler": ["bold", "vurgu", "stil", "karakter", "yazı"],
        "zorluk": "kolay"
    },
    {
        "kelime": "İtalik Yapmak",
        "aciklama": "Harfleri sağa doğru eğik yazım formatına çevirmek.",
        "yasakli_kelimeler": ["eğik", "sağa", "format", "vurgu", "harf"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Metni Hizalamak",
        "aciklama": "Paragrafı sola, sağa, ortaya veya iki yana yaslamak.",
        "yasakli_kelimeler": ["sağ", "sol", "orta", "yaslamak", "paragraf"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Büyük Harfe Çevirmek",
        "aciklama": "Yazıdaki tüm harfleri majiskül (büyük harf) formatına getirmek.",
        "yasakli_kelimeler": ["majiskül", "küçük harf", "caps", "format", "yazı"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Altını Çizmek",
        "aciklama": "Önemli kelimelerin altına düz veya noktalı çizgi eklemek.",
        "yasakli_kelimeler": ["çizgi", "vurgu", "önemli", "eklemek", "kelime"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Font Yüklemek",
        "aciklama": "Bilgisayara veya işletim sistemine yeni bir yazı tipi dosyası kurmak.",
        "yasakli_kelimeler": ["bilgisayar", "dosya", "kurmak", "yazı tipi", "ttf"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Paragraf Başı Yapmak",
        "aciklama": "Yeni bir metin bloğuna geçmek için satır başı girintisi vermek.",
        "yasakli_kelimeler": ["satır", "girinti", "blok", "yeni", "boşluk"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Okunurluğu Artırmak",
        "aciklama": "Yazının gözü yormadan kolay ve net anlaşılmasını sağlamak.",
        "yasakli_kelimeler": ["kolay", "net", "anlaşılır", "göz", "okuma"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Metin Kutusu Açmak",
        "aciklama": "Tasarım yazılımında yazı yazmak için bir çerçeve oluşturmak.",
        "yasakli_kelimeler": ["çerçeve", "alan", "yazılım", "yazı", "oluşturmak"],
        "zorluk": "kolay"
    },

    # Orta (24)
    {
        "kelime": "Kerning Ayarlamak",
        "aciklama": "İki spesifik harf karakteri arasındaki optik boşluğu özel olarak düzenlemek.",
        "yasakli_kelimeler": ["harf", "boşluk", "iki", "optik", "ara"],
        "zorluk": "orta"
    },
    {
        "kelime": "Tracking Vermek",
        "aciklama": "Tüm kelime veya satır genelindeki harf aralıklarını topluca açıp daraltmak.",
        "yasakli_kelimeler": ["satır", "genel", "harf aralığı", "toplu", "açmak"],
        "zorluk": "orta"
    },
    {
        "kelime": "Satır Aralığı Açmak",
        "aciklama": "İki metin satırının taban çizgileri arasındaki düşey mesafeyi (leading) artırmak.",
        "yasakli_kelimeler": ["leading", "düşey", "satır", "mesafe", "boşluk"],
        "zorluk": "orta"
    },
    {
        "kelime": "Hiyerarşi Kurmak",
        "aciklama": "Başlık, alt başlık ve gövde metinleri arasında boyut ve ağırlık sırası oluşturmak.",
        "yasakli_kelimeler": ["başlık", "gövde metni", "sıra", "boyut", "vurgu"],
        "zorluk": "orta"
    },
    {
        "kelime": "Font Eşleştirmek",
        "aciklama": "Serif ve sans-serif gibi birbiriyle uyumlu iki farklı yazı tipini kombinlemek.",
        "yasakli_kelimeler": ["serif", "sans serif", "kombin", "uyum", "farklı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Drop Cap Kullanmak",
        "aciklama": "Paragrafın ilk harfini birkaç satır yüksekliğinde devasa boyutta başlatmak.",
        "yasakli_kelimeler": ["ilk harf", "büyük", "satır", "başlangıç", "dekoratif"],
        "zorluk": "orta"
    },
    {
        "kelime": "Dul Satırı Önlemek",
        "aciklama": "Paragrafın tek kalmış son kelimesinin (orphan/widow) bir sonraki sütuna taşmasını engellemek.",
        "yasakli_kelimeler": ["widow", "orphan", "tek kelime", "sütun", "taşma"],
        "zorluk": "orta"
    },
    {
        "kelime": "Karakter Çizmek",
        "aciklama": "Vektörel çizim araçlarıyla sıfırdan özgün alfabe harfleri tasarlamak.",
        "yasakli_kelimeler": ["vektör", "alfabe", "özgün", "tasarım", "harf"],
        "zorluk": "orta"
    },
    {
        "kelime": "Yazıyı Vektöre Çevirmek",
        "aciklama": "Metin nesnesini düzenlenemez bağımsız çizim eğrilerine (convert to curves) dönüştürmek.",
        "yasakli_kelimeler": ["create outlines", "eğri", "çizim", "nesne", "dönüştürmek"],
        "zorluk": "orta"
    },
    {
        "kelime": "Tırnaksız Font Kullanmak",
        "aciklama": "Harf uçlarında dekoratif çıkıntıları olmayan modern sans-serif yazı tipi seçmek.",
        "yasakli_kelimeler": ["sans serif", "çıkıntı", "modern", "düz", "uç"],
        "zorluk": "orta"
    },
    {
        "kelime": "Serif Font Seçmek",
        "aciklama": "Harf bitişlerinde klasik tırnak ve kuyruk detayları bulunan yazı tipini tercih etmek.",
        "yasakli_kelimeler": ["tırnak", "klasik", "kuyruk", "detay", "geleneksel"],
        "zorluk": "orta"
    },
    {
        "kelime": "Hece Bölmek",
        "aciklama": "Satır sonuna sığmayan uzun kelimeleri tire işaretiyle kurallı bölmek.",
        "yasakli_kelimeler": ["tire", "satır sonu", "kelime", "bölme", "tireleme"],
        "zorluk": "orta"
    },
    {
        "kelime": "Taban Çizgisini Kaydırmak",
        "aciklama": "Bir harf veya sembolün baseline hattının yukarısına veya aşağısına ötelenmesi.",
        "yasakli_kelimeler": ["baseline", "ötelenme", "hat", "yukarı", "aşağı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Glif Eklemek",
        "aciklama": "Karakter tablosundan özel işaret, simge veya alternatif harf formu eklemek.",
        "yasakli_kelimeler": ["glyph", "simge", "işaret", "karakter haritası", "eklenti"],
        "zorluk": "orta"
    },
    {
        "kelime": "Sütun Sayısını Belirlemek",
        "aciklama": "Sayfa mizanpajında metnin kaç dikey blok halinde akacağını ayarlamak.",
        "yasakli_kelimeler": ["kolon", "dikey", "akış", "sayfa", "mizanpaj"],
        "zorluk": "orta"
    },
    {
        "kelime": "Satır Uzunluğunu Sınırlamak",
        "aciklama": "Okuma ergonomisi için bir satırdaki ideal karakter sayısını (50-75) korumak.",
        "yasakli_kelimeler": ["karakter", "ideal", "okuma", "genişlik", "ergonomi"],
        "zorluk": "orta"
    },
    {
        "kelime": "Monospace Yazı Tipi Kullanmak",
        "aciklama": "Tüm harflerin eşit yatay genişliğe sahip olduğu kod yazı tiplerini kullanmak.",
        "yasakli_kelimeler": ["eşit", "genişlik", "kod", "daktilo", "sabit"],
        "zorluk": "orta"
    },
    {
        "kelime": "Blok Metin Oluşturmak",
        "aciklama": "Metni her iki kenara tam yaslayarak dikdörtgen bir metin bloğu elde etmek.",
        "yasakli_kelimeler": ["iki yana yasla", "dikdörtgen", "kenar", "düz", "justify"],
        "zorluk": "orta"
    },
    {
        "kelime": "Ligatür Kullanmak",
        "aciklama": "fi, fl gibi yan yana gelen iki harfin birleşik özel bir glifle yazılması.",
        "yasakli_kelimeler": ["birleşik", "harf", "bağlantı", "özel glif", "çarpışma"],
        "zorluk": "orta"
    },
    {
        "kelime": "Üst Simge Yazmak",
        "aciklama": "Metin içine dipnot veya matematik üssü için küçük boyutta havada harf yazmak.",
        "yasakli_kelimeler": ["superscript", "dipnot", "üs", "yukarıda", "küçük"],
        "zorluk": "orta"
    },
    {
        "kelime": "Alt Simge Eklemek",
        "aciklama": "Kimyasal formül veya indeksler için harfin altına küçük karakter yerleştirmek.",
        "yasakli_kelimeler": ["subscript", "kimya", "indeks", "aşağıda", "küçük"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kontrast Sağlamak",
        "aciklama": "Yazı rengi ile zemin rengi arasındaki ton farkını belirginleştirip okunurluğu sağlamak.",
        "yasakli_kelimeler": ["arka plan", "renk", "ton", "zemin", "belirgin"],
        "zorluk": "orta"
    },
    {
        "kelime": "Font Lisanslamak",
        "aciklama": "Ticari projelerde ve web sitelerinde font kullanımı için yasal hak satın almak.",
        "yasakli_kelimeler": ["yasal", "hak", "ticari", "telif", "satın alma"],
        "zorluk": "orta"
    },
    {
        "kelime": "Yazıyı Eğriye Oturtmak",
        "aciklama": "Metni bir daire veya dalgalı bir yol boyunca akıtarak şekillendirmek.",
        "yasakli_kelimeler": ["yol", "daire", "kavis", "dalga", "type on path"],
        "zorluk": "orta"
    },

    # Zor (14)
    {
        "kelime": "X Yüksekliğini Ölçmek",
        "aciklama": "Bir fonttaki küçük harflerin (özellikle 'x' harfinin) gövde yüksekliğini analiz etmek.",
        "yasakli_kelimeler": ["x-height", "küçük harf", "gövde", "taban", "oran"],
        "zorluk": "zor"
    },
    {
        "kelime": "Ascender Çizgisini Belirlemek",
        "aciklama": "b, d, h gibi harflerin gövde üstüne uzanan yukarı uzantı sınırını tespit etmek.",
        "yasakli_kelimeler": ["uzantı", "yukarı", "üst sınır", "harf kolu", "büyüklük"],
        "zorluk": "zor"
    },
    {
        "kelime": "Descender Boyunu Ayarlamak",
        "aciklama": "p, g, y gibi harflerin taban çizgisinin altına inen kuyruk payını düzenlemek.",
        "yasakli_kelimeler": ["kuyruk", "alt çizgi", "aşağı", "uzantı", "baseline altı"],
        "zorluk": "zor"
    },
    {
        "kelime": "Optik Düzeltme Yapmak",
        "aciklama": "Geometrik yuvarlak harflerin diğer harflerle aynı boyda görünmesi için overshoot payı vermek.",
        "yasakli_kelimeler": ["overshoot", "yuvarlak", "göz yanılması", "geometrik", "hizalama"],
        "zorluk": "zor"
    },
    {
        "kelime": "Değişken Font Üretmek",
        "aciklama": "Kalınlık, eğim ve genişliği tek bir dosya içinde dinamik eksenlerle değişen Variable Font kodlamak.",
        "yasakli_kelimeler": ["variable font", "eksen", "dinamik", "tek dosya", "ağırlık"],
        "zorluk": "zor"
    },
    {
        "kelime": "Hinting Tanımlamak",
        "aciklama": "Düşük çözünürlüklü dijital ekranlarda piksellere tam oturması için fonta matematiksel yönergeler eklemek.",
        "yasakli_kelimeler": ["piksel", "ekran", "çözünürlük", "rasterize", "netlik"],
        "zorluk": "zor"
    },
    {
        "kelime": "OpenType Özelliği Kodlamak",
        "aciklama": "Yazı tipine otomatik ligatür, alternatif glif ve rakam setleri kurallarını programlamak.",
        "yasakli_kelimeler": ["özellik", "kod", "alternatif glif", "tablo", "font mimarisi"],
        "zorluk": "zor"
    },
    {
        "kelime": "Bézier Eğrilerini Optimize Etmek",
        "aciklama": "Harf sınırlarını çizen vektör kontrol noktalarını minimum sayıda ve pürüzsüz tutmak.",
        "yasakli_kelimeler": ["vektör", "düğüm", "kontrol noktası", "eğri", "anchor"],
        "zorluk": "zor"
    },
    {
        "kelime": "Taban Çizgisini Izgaraya Bağlamak",
        "aciklama": "Çok sütunlu mizanpajlarda tüm metin satırlarını ortak bir baseline grid üzerine oturtmak.",
        "yasakli_kelimeler": ["baseline grid", "ızgara", "hiza", "çok sütun", "satır tabanı"],
        "zorluk": "zor"
    },
    {
        "kelime": "Karakter Aralığı Tablosu Oluşturmak",
        "aciklama": "Yüzlerce harf kombinasyonunun birbirine göre aralık değerlerini içeren kerning matrix hazırlamak.",
        "yasakli_kelimeler": ["matrix", "tablo", "kombinasyon", "çiftler", "değer"],
        "zorluk": "zor"
    },
    {
        "kelime": "Mikrotipografik İnce Ayar Yapmak",
        "aciklama": "Tireleme, tırnak işaretleri, boşluk incelikleri ve marjinal hizalamaları kusursuzlaştırmak.",
        "yasakli_kelimeler": ["mikro", "detay", "marjinal", "tireleme", "kusursuz"],
        "zorluk": "zor"
    },
    {
        "kelime": "Web Fontunu WOFF2'ye Sıkıştırmak",
        "aciklama": "Font dosyasını web tarayıcılarında hızlı yüklenmesi için gelişmiş web formatına dönüştürmek.",
        "yasakli_kelimeler": ["woff2", "sıkıştırma", "tarayıcı", "yükleme", "web"],
        "zorluk": "zor"
    },
    {
        "kelime": "Harf Konturlarını Ayrıştırmak",
        "aciklama": "İç içe geçen vektör çizgilerini kesişim noktalarından boolean işlemleriyle birleştirmek.",
        "yasakli_kelimeler": ["kontur", "kesişim", "boolean", "birleştirme", "yol"],
        "zorluk": "zor"
    },
    {
        "kelime": "Tipometreyle Ölçüm Almak",
        "aciklama": "Geleneksel matbaacılıkta sayfa ve punto cetveli kullanarak kurşun dizgi ölçüsü almak.",
        "yasakli_kelimeler": ["cetvel", "kurşun dizgi", "punto", "geleneksel", "ölçüm"],
        "zorluk": "zor"
    }
]

# 2. TIYATRO (50 verbs: 12 kolay, 24 orta, 14 zor)
tiyatro_verbs = [
    # Kolay (12)
    {
        "kelime": "Sahneye Çıkmak",
        "aciklama": "Oyunu oynamak üzere seyircilerin karşısındaki platforma adım atmak.",
        "yasakli_kelimeler": ["oyun", "seyirci", "platform", "rol", "başlamak"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Rol Yapmak",
        "aciklama": "Canlandırılan karakterin duygu ve davranışlarını sahne üzerinde taklit etmek.",
        "yasakli_kelimeler": ["karakter", "canlandırmak", "oyuncu", "taklit", "sahne"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Replik Ezberlemek",
        "aciklama": "Tiyatro metninde karaktere ait sözleri ve cümleleri hafızaya almak.",
        "yasakli_kelimeler": ["söz", "metin", "hafıza", "ezber", "cümle"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Alkışlamak",
        "aciklama": "Oyun sonunda seyircilerin performansı takdir etmek için el çırpması.",
        "yasakli_kelimeler": ["seyirci", "el çırpmak", "takdir", "son", "beğeni"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Kostüm Giymek",
        "aciklama": "Canlandırılacak döneme veya karaktere uygun özel tiyatro kıyafetini giymek.",
        "yasakli_kelimeler": ["kıyafet", "karakter", "dönem", "elbise", "sahne"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Perdeyi Açmak",
        "aciklama": "Tiyatro oyununun başladığını göstermek için sahne önündeki perdeyi çekmek.",
        "yasakli_kelimeler": ["perde", "başlangıç", "sahne", "kırmızı", "çekmek"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Perdeyi Kapatmak",
        "aciklama": "Perde veya sahne sonlandığında sahneyi seyirciden gizlemek.",
        "yasakli_kelimeler": ["perde", "son", "bitiş", "gizlemek", "kapanış"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Dekor Kurmak",
        "aciklama": "Oyunun geçtiği mekânı yansıtan eşyaları ve panoları sahneye yerleştirmek.",
        "yasakli_kelimeler": ["mekân", "eşya", "sahne", "pano", "yerleşim"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Bilet Satmak",
        "aciklama": "Seyircilerin tiyatro salonuna girebilmesi için koltuk giriş kartı vermek.",
        "yasakli_kelimeler": ["gişe", "salon", "koltuk", "seyirci", "para"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Makyaj Yapmak",
        "aciklama": "Karakterin yaşına veya tipine uygun yüz boyası ve efekt uygulamak.",
        "yasakli_kelimeler": ["yüz", "boya", "yaş", "efekt", "kuliste"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Sahneyi Selamlamak",
        "aciklama": "Oyun bitiminde tüm oyuncuların el ele tutuşup seyircileri reveransla selamlaması.",
        "yasakli_kelimeler": ["selam", "reverans", "alkış", "el ele", "oyun sonu"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Rol Dağıtmak",
        "aciklama": "Yönetmenin oyundaki rolleri oyunculara paylaştırması.",
        "yasakli_kelimeler": ["yönetmen", "karakter", "paylaşım", "oyuncu", "seçim"],
        "zorluk": "kolay"
    },

    # Orta (24)
    {
        "kelime": "Tirad Atmak",
        "aciklama": "Sahnede tek bir oyuncunun uzun, kesintisiz ve duygusal bir monolog konuşması yapması.",
        "yasakli_kelimeler": ["monolog", "uzun söz", "duygu", "tek başına", "konuşma"],
        "zorluk": "orta"
    },
    {
        "kelime": "Doğaçlama Yapmak",
        "aciklama": "Yazılı bir metne bağlı kalmadan o an zihinden ve akıştan replik üretmek.",
        "yasakli_kelimeler": ["metinsiz", "spontan", "o an", "zihin", "tuluat"],
        "zorluk": "orta"
    },
    {
        "kelime": "Fısıldamak",
        "aciklama": "Sufizm veya sahne arkasında sözünü unutan oyuncuya alçak sesle repliğini hatırlatmak.",
        "yasakli_kelimeler": ["suflör", "hatırlatmak", "alçak ses", "kulak", "unutmak"],
        "zorluk": "orta"
    },
    {
        "kelime": "Diksiyon Çalışmak",
        "aciklama": "Sözcükleri tane tane, doğru ses tonu ve artikülasyonla telaffuz etmek için egzersiz yapmak.",
        "yasakli_kelimeler": ["telaffuz", "artikülasyon", "ses", "tane tane", "konuşma"],
        "zorluk": "orta"
    },
    {
        "kelime": "Mizansen Kurmak",
        "aciklama": "Yönetmenin oyuncuların sahnedeki duruş, hareket ve geçiş düzenlerini belirlemesi.",
        "yasakli_kelimeler": ["yönetmen", "duruş", "hareket", "düzen", "sahne planı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Rolü Özümsemek",
        "aciklama": "Canlandırılacak karakterin psikolojisini, geçmişini ve ruh halini bütünüyle benimsemek.",
        "yasakli_kelimeler": ["psikoloji", "benimsemek", "karakter", "ruh hali", "içselleştirmek"],
        "zorluk": "orta"
    },
    {
        "kelime": "Işık Odaklamak",
        "aciklama": "Sahne projektörlerini oyunun dramatik anına veya konuşan oyuncunun üstüne yöneltmek.",
        "yasakli_kelimeler": ["projektör", "spot", "yönlendirmek", "sahne", "aydınlatma"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kondüit Masasına Oturmak",
        "aciklama": "Sahne arkasında oyunun ses, ışık ve dekor değişim sıralarını yönetmek.",
        "yasakli_kelimeler": ["kumanda", "ses", "ışık", "sıra", "yönetim"],
        "zorluk": "orta"
    },
    {
        "kelime": "Okuma Provası Yapmak",
        "aciklama": "Masa başında tüm ekibin oyundaki replikleri sesli okuyarak oyunu tanıması.",
        "yasakli_kelimeler": ["masa başı", "sesli", "ekip", "tanıma", "metin"],
        "zorluk": "orta"
    },
    {
        "kelime": "Genel Prova Yapmak",
        "aciklama": "Prömiyer öncesi oyunun kostüm, dekor, ışık dahil baştan sona eksiksiz oynanması.",
        "yasakli_kelimeler": ["prömiyer", "kostüm", "ışık", "baştan sona", "eksiksiz"],
        "zorluk": "orta"
    },
    {
        "kelime": "Prömiyer Yapmak",
        "aciklama": "Bir tiyatro oyununun ilk kez seyirci ve eleştirmenler önünde sergilenmesi.",
        "yasakli_kelimeler": ["ilk gösterim", "açılış", "eleştirmen", "sergileme", "ilk kez"],
        "zorluk": "orta"
    },
    {
        "kelime": "Matine Oynamak",
        "aciklama": "Gündüz veya öğleden sonra saatlerinde sahnelenen gösteride yer almak.",
        "yasakli_kelimeler": ["gündüz", "öğleden sonra", "suare", "seans", "gösteri"],
        "zorluk": "orta"
    },
    {
        "kelime": "Suareye Çıkmak",
        "aciklama": "Akşam saatinde düzenlenen ana tiyatro gösterisinde sahne almak.",
        "yasakli_kelimeler": ["akşam", "gece", "matine", "ana seans", "sahne"],
        "zorluk": "orta"
    },
    {
        "kelime": "Turneye Çıkmak",
        "aciklama": "Bir tiyatro oyununu farklı şehir veya ülkelerdeki sahnelerde sergilemek üzere seyahat etmek.",
        "yasakli_kelimeler": ["şehir", "seyahat", "farklı sahne", "gezi", "oyun sergileme"],
        "zorluk": "orta"
    },
    {
        "kelime": "Sufle Vermek",
        "aciklama": "Unutulan repliği oyuncuya çaktırmadan kulisten hatırlatmak.",
        "yasakli_kelimeler": ["suflör", "hatırlatma", "kulis", "çaktırmadan", "replik"],
        "zorluk": "orta"
    },
    {
        "kelime": "Dördüncü Duvarı Yıkmak",
        "aciklama": "Oyuncunun doğrudan seyirciye hitap ederek kurgusal dünyayı kırması.",
        "yasakli_kelimeler": ["seyirci", "hitap", "kurgu", "aradaki sınır", "doğrudan"],
        "zorluk": "orta"
    },
    {
        "kelime": "Aksesuar Kullanmak",
        "aciklama": "Karakterin rol gereği sahnede elinde tuttuğu asa, mektup, kadeh gibi nesneleri kullanmak.",
        "yasakli_kelimeler": ["nesne", "el", "eşya", "mektup", "kadeh"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kuliste Beklemek",
        "aciklama": "Sahneye giriş sırası gelene kadar sahne arkasındaki odada hazır bulunmak.",
        "yasakli_kelimeler": ["sahne arkası", "sıra", "bekleme", "giriş", "oda"],
        "zorluk": "orta"
    },
    {
        "kelime": "Ses Projeksiyonu Yapmak",
        "aciklama": "Mikrofonsuz olarak sesini salonun en arka sırasındaki seyirciye kadar ulaştırmak.",
        "yasakli_kelimeler": ["arka sıra", "mikrofonsuz", "ulaştırmak", "diyafram", "gür"],
        "zorluk": "orta"
    },
    {
        "kelime": "Pandomim Yapmak",
        "aciklama": "Hiç konuşmadan yalnızca jest ve mimiklerle hikâye veya durum anlatmak.",
        "yasakli_kelimeler": ["sessiz", "jest", "mimik", "vücut dili", "konuşmadan"],
        "zorluk": "orta"
    },
    {
        "kelime": "Fuayede Toplanmak",
        "aciklama": "Oyun öncesi veya perde arasında seyircilerin salon dışındaki alanda sosyalleşmesi.",
        "yasakli_kelimeler": ["ara", "salon dışı", "sosyalleşme", "bekleme alanı", "seyirci"],
        "zorluk": "orta"
    },
    {
        "kelime": "Mizah Katmak",
        "aciklama": "Ciddi bir sahneye veya oyuna seyirciyi güldürecek komik unsurlar eklemek.",
        "yasakli_kelimeler": ["komik", "güldürmek", "espri", "komedi", "kahkaha"],
        "zorluk": "orta"
    },
    {
        "kelime": "Giriş Çıkışları Ezberlemek",
        "aciklama": "Hangi sahne başında nereden girilip nereden çıkılacağının planını öğrenmek.",
        "yasakli_kelimeler": ["kulisten sahneye", "zamanlama", "kapı", "plan", "öğrenmek"],
        "zorluk": "orta"
    },
    {
        "kelime": "Karakter Analizi Yapmak",
        "aciklama": "Metindeki rolün motivasyonunu, zaaflarını ve çatışmalarını derinlemesine incelemek.",
        "yasakli_kelimeler": ["motivasyon", "zaaf", "çatışma", "inceleme", "derin"],
        "zorluk": "orta"
    },

    # Zor (14)
    {
        "kelime": "Katarsis Yaşatmak",
        "aciklama": "Tragedya aracılığıyla seyircide korku ve acıma duyguları uyandırıp ruhsal arınma sağlamak.",
        "yasakli_kelimeler": ["arınma", "tragedya", "acıma", "korku", "ruhsal"],
        "zorluk": "zor"
    },
    {
        "kelime": "Epik Tiyatro Yöntemi Uygulamak",
        "aciklama": "Brecht'in yabancılaştırma efektiyle seyircinin oyuna kapılmasını engelleyip eleştirel düşündürmek.",
        "yasakli_kelimeler": ["brecht", "yabancılaştırma", "eleştirel", "kapılma", "illüzyon"],
        "zorluk": "zor"
    },
    {
        "kelime": "Stanislavski Metodunu İşletmek",
        "aciklama": "Duygusal hafıza ve psikolojik gerçekçilik teknikleriyle karaktere bütünüyle bürünmek.",
        "yasakli_kelimeler": ["metot", "duygusal hafıza", "gerçekçilik", "psikolojik", "bürünmek"],
        "zorluk": "zor"
    },
    {
        "kelime": "Grotesk Tarzda Oynamak",
        "aciklama": "Korkunç ile komiği, abartılı ve tuhaf biçimleri harmanlayarak sahnelemek.",
        "yasakli_kelimeler": ["abartı", "tuhaf", "korkunç", "komik", "biçim"],
        "zorluk": "zor"
    },
    {
        "kelime": "Absürd Diyalog Kurmak",
        "aciklama": "Uyumsuz tiyatro ekolünde mantık sınırlarını aşan anlamsız ve döngüsel konuşmalar yapmak.",
        "yasakli_kelimeler": ["uyumsuz", "mantıksız", "beckett", "döngü", "varoluşsal"],
        "zorluk": "zor"
    },
    {
        "kelime": "Commedia dell'Arte Oynamak",
        "aciklama": "Geleneksel İtalyan halk tiyatrosunda maskeler ve tiplemelerle tuluat yapmak.",
        "yasakli_kelimeler": ["maske", "italyan", "pantalone", "arlekino", "tipleme"],
        "zorluk": "zor"
    },
    {
        "kelime": "Diyafram Nefesi Kullanmak",
        "aciklama": "Göğüs yerine karın boşluğundaki kası kullanarak uzun ve rezonanslı ses üretmek.",
        "yasakli_kelimeler": ["karın", "rezonans", "nefes", "akciğer", "kas"],
        "zorluk": "zor"
    },
    {
        "kelime": "Yabancılaştırma Efekti Vermek",
        "aciklama": "Seyirciye izlediğinin bir kurgu olduğunu hatırlatan müzik, tabela veya anlatıcı kullanmak.",
        "yasakli_kelimeler": ["verfremdung", "illüzyon bozma", "tabela", "anlatıcı", "hatırlatma"],
        "zorluk": "zor"
    },
    {
        "kelime": "Dramaturgi Çalışması Yapmak",
        "aciklama": "Oyun metninin tarihsel, felsefi ve tematik bağlamını araştırıp sahneye uyarlamak.",
        "yasakli_kelimeler": ["dramaturg", "tarihsel bağlam", "tematik", "metin analizi", "uyarlama"],
        "zorluk": "zor"
    },
    {
        "kelime": "Beden Partitürü Çıkarmak",
        "aciklama": "Fiziksel tiyatroda her bir jest, hareket ve ritmin koreografik haritasını oluşturmak.",
        "yasakli_kelimeler": ["partitür", "fiziksel tiyatro", "koreografi", "ritim", "beden"],
        "zorluk": "zor"
    },
    {
        "kelime": "Tragedya Sahnelemek",
        "aciklama": "Kahramanın kaderiyle çatışmasını ve kaçınılmaz trajik sonunu anlatan klasik eseri oynamak.",
        "yasakli_kelimeler": ["kader", "kaçınılmaz son", "kahraman", "çatışma", "ağır dram"],
        "zorluk": "zor"
    },
    {
        "kelime": "Tuluat Geleneğini Sürdürmek",
        "aciklama": "Ortaoyunu ve geleneksel Türk tiyatrosundaki metinsiz doğaçlama üslubunu yaşatmak.",
        "yasakli_kelimeler": ["ortaoyunu", "kavuklu", "pişekar", "türk tiyatrosu", "metinsiz"],
        "zorluk": "zor"
    },
    {
        "kelime": "Meyerhold Biyomekaniği Uygulamak",
        "aciklama": "Oyuncunun vücudunu bir makine hassasiyetinde ritmik ve akrobatik hareketlerle eğitmesi.",
        "yasakli_kelimeler": ["biyomekanik", "akrobasi", "makine", "hareket sistemi", "ritim"],
        "zorluk": "zor"
    },
    {
        "kelime": "Koro Halinde Konuşmak",
        "aciklama": "Antik Yunan tiyatrosunda olayları yorumlayan topluluğun tek bir ağızdan şiirsel konuşması.",
        "yasakli_kelimeler": ["antik yunan", "koro", "toplu", "tek ses", "yorumcu"],
        "zorluk": "zor"
    }
]

if __name__ == "__main__":
    add_and_save_verbs("tipografi", tipografi_verbs)
    add_and_save_verbs("tiyatro", tiyatro_verbs)
