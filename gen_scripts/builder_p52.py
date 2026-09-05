import sys
from card_utils import add_and_save_verbs

# 1. TURKHALKEDEBIYATI (50 verbs: 12 kolay, 24 orta, 14 zor)
turkhalkedebiyati_verbs = [
    # Kolay (12)
    {
        "kelime": "Bağlama Çalmak",
        "aciklama": "Halk ozanlarının türkü söylerken çaldığı telli sazı icra etmek.",
        "yasakli_kelimeler": ["saz", "türkü", "tel", "ozan", "mızrap"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Türkü Söylemek",
        "aciklama": "Halk ezgilerini ve anonim besteleri seslendirmek.",
        "yasakli_kelimeler": ["ezgi", "seslendirmek", "saz", "söz", "beste"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Ağıt Yakmak",
        "aciklama": "Ölen bir kimsenin arkasından hüzünlü sözler ve ezgiler dizmek.",
        "yasakli_kelimeler": ["ölüm", "hüzün", "yas", "cenaze", "ağlamak"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Mani Düzmek",
        "aciklama": "Dört dizelik kafiyeli kısa halk şiirleri uydurmak ve söylemek.",
        "yasakli_kelimeler": ["dörtlük", "kafiye", "kısa şiir", "ramazan", "atışma"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Masal Anlatmak",
        "aciklama": "Olağanüstü olayları ve peri masallarını dinleyicilere aktarmak.",
        "yasakli_kelimeler": ["dev", "peri", "keloğlan", "olağanüstü", "çocuk"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Destan Yazmak",
        "aciklama": "Milletin kahramanlık ve büyük mücadelelerini anlatan uzun şiirler kaleme almak.",
        "yasakli_kelimeler": ["kahraman", "savaş", "millet", "mücadele", "uzun"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Ninni Söylemek",
        "aciklama": "Bebekleri uyutmak için sakin ve ezgili şiirler mırıldanmak.",
        "yasakli_kelimeler": ["bebek", "uyku", "beşik", "anne", "mırıldanmak"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Bilmeceler Sormak",
        "aciklama": "Üstü kapalı ipuçlarıyla bir nesneyi buldurmayı amaçlayan sorular yöneltmek.",
        "yasakli_kelimeler": ["soru", "cevap", "ipucu", "bulmak", "nesne"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Diyar Diyar Gezmek",
        "aciklama": "Gezgin aşıkların köy köy, şehir şehir dolaşarak sanatını icra etmesi.",
        "yasakli_kelimeler": ["köy", "şehir", "gezgin", "aşık", "dolaşmak"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Fıkra Anlatmak",
        "aciklama": "Nasreddin Hoca gibi halk kahramanlarının mizahi hikâyelerini aktarmak.",
        "yasakli_kelimeler": ["nasreddin hoca", "mizah", "komik", "gülmek", "kıssa"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Gönül Vermek",
        "aciklama": "Halk hikâyelerinde sevgilisine derin bir aşkla bağlanmak.",
        "yasakli_kelimeler": ["aşk", "sevda", "bağlanmak", "sevgili", "ferhat"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Dert Yanmak",
        "aciklama": "Şiirlerde ve koşmalarda gurbet, ayrılık ve çaresizlikten yakınmak.",
        "yasakli_kelimeler": ["ayrılık", "gurbet", "çaresizlik", "yakınmak", "keder"],
        "zorluk": "kolay"
    },

    # Orta (24)
    {
        "kelime": "Atışma Yapmak",
        "aciklama": "İki halk ozanının saz eşliğinde karşılıklı irticalen şiir yarıştırması.",
        "yasakli_kelimeler": ["karşılıklı", "ozan", "yarışma", "irticalen", "meydan"],
        "zorluk": "orta"
    },
    {
        "kelime": "Mahlas Almak",
        "aciklama": "Aşığın ustası veya rüya yoluyla kendine şiirlerde kullanacağı takma ad seçmesi.",
        "yasakli_kelimeler": ["tapşırma", "takma ad", "şair adı", "son dörtlük", "isim"],
        "zorluk": "orta"
    },
    {
        "kelime": "Rüya Görmek",
        "aciklama": "Aşıklık geleneğinde bade içip hak aşığı olunan kutlu rüyaya girmek.",
        "yasakli_kelimeler": ["bade", "hak aşığı", "pir", "aşıklık", "ilham"],
        "zorluk": "orta"
    },
    {
        "kelime": "Bade İçmek",
        "aciklama": "Rüyasında pir elinden aşk kadehi içerek şairlik ve aşıklık mertebesine ermek.",
        "yasakli_kelimeler": ["pir", "kadeh", "aşk", "mertebe", "şerbet"],
        "zorluk": "orta"
    },
    {
        "kelime": "Koşma Yazmak",
        "aciklama": "11'li hece ölçüsüyle sevgi, doğa veya ayrılık temalı halk şiiri nazmetmek.",
        "yasakli_kelimeler": ["11 hece", "nazım biçimi", "dörtlük", "karacaoğlan", "sevda"],
        "zorluk": "orta"
    },
    {
        "kelime": "Semai Okumak",
        "aciklama": "8'li hece ölçüsü ve özel bir ezgiyle söylenen halk edebiyatı şiirini icra etmek.",
        "yasakli_kelimeler": ["8 hece", "ezgi", "nazım şekli", "şarkı", "koşma"],
        "zorluk": "orta"
    },
    {
        "kelime": "Varsağı Söylemek",
        "aciklama": "'Bre', 'Hey', 'Behey' gibi mert ve yiğitçe nidalarla söylenen Toros şiiri okumak.",
        "yasakli_kelimeler": ["bre", "hey", "yiğit", "varsak", "nida"],
        "zorluk": "orta"
    },
    {
        "kelime": "Güzelleme Yapmak",
        "aciklama": "Sevgilinin veya tabiatın güzelliklerini öven lirik koşmalar söylemek.",
        "yasakli_kelimeler": ["övgü", "güzellik", "tabiat", "lirik", "sevgili"],
        "zorluk": "orta"
    },
    {
        "kelime": "Koçaklama Okumak",
        "aciklama": "Köroğlu ve Dadaloğlu tarzında kahramanlık, savaş ve yiğitlik şiirleri söylemek.",
        "yasakli_kelimeler": ["köroğlu", "dadaloğlu", "yiğitlik", "savaş", "mertlik"],
        "zorluk": "orta"
    },
    {
        "kelime": "Taşlama Yazmak",
        "aciklama": "Toplumdaki aksaklıkları ve kişilerin kusurlarını hicveden alaycı şiir düzmek.",
        "yasakli_kelimeler": ["hiciv", "eleştiri", "kusur", "alay", "seyrani"],
        "zorluk": "orta"
    },
    {
        "kelime": "İrticalen Söylemek",
        "aciklama": "Önceden düşünmeden, sahnede saz çalarken anında doğaçlama şiir üretmek.",
        "yasakli_kelimeler": ["doğaçlama", "hazırlıksız", "o an", "akıcı", "meydan"],
        "zorluk": "orta"
    },
    {
        "kelime": "Tapşırma Yapmak",
        "aciklama": "Halk şiirinin son dörtlüğünde ozanın kendi mahlasını kullanması.",
        "yasakli_kelimeler": ["son dörtlük", "mahlas", "ozan", "imza", "isim"],
        "zorluk": "orta"
    },
    {
        "kelime": "Heceyi Saymak",
        "aciklama": "Şiir mısralarındaki sesli harf sayısını kontrol ederek hece veznine uydurmak.",
        "yasakli_kelimeler": ["vezin", "sesli harf", "mısra", "ölçü", "parmak hesabı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Durak Vermek",
        "aciklama": "Hece ölçüsünde dizeyi okurken kelime bölünmeden nefes alınan ayrım noktası koymak.",
        "yasakli_kelimeler": ["4+4", "6+5", "dize", "nefes", "kesinti"],
        "zorluk": "orta"
    },
    {
        "kelime": "Yarım Uyak Yapmak",
        "aciklama": "Dize sonlarında tek bir ünsüz harfin benzeşmesiyle kurulan halk kafiyesi.",
        "yasakli_kelimeler": ["tek ses", "kafiye", "ünsüz", "mısra sonu", "benzerlik"],
        "zorluk": "orta"
    },
    {
        "kelime": "Cinaslı Kafiye Kurmak",
        "aciklama": "Yazılışları aynı ancak anlamları farklı olan sözcüklerle dize sonu uyumu yapmak.",
        "yasakli_kelimeler": ["sesteş", "farklı anlam", "mani", "dize sonu", "kelime oyunu"],
        "zorluk": "orta"
    },
    {
        "kelime": "Meydana Çıkmak",
        "aciklama": "Aşıklar meclisinde veya köy kahvesinde hüner sergilemek üzere sahneye gelmek.",
        "yasakli_kelimeler": ["meclis", "köy kahvesi", "hüner", "saz", "yarışma"],
        "zorluk": "orta"
    },
    {
        "kelime": "Aşık Faslı Yapmak",
        "aciklama": "Divan, koşma, taşlama ve muamma bölümlerinden oluşan geleneksel aşık dinletisi sunmak.",
        "yasakli_kelimeler": ["bölüm", "gelenek", "dinleti", "program", "divan"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kavuştak Eklemek",
        "aciklama": "Türkülerde bentlerin arasına tekrar edilen nakarat bölümlerini bağlamak.",
        "yasakli_kelimeler": ["nakarat", "türkü", "bent", "tekrar", "bağlantı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Cönk Derlemek",
        "aciklama": "Halk şairlerinin şiirlerini topladığı uzunlamasına açılan deri defterleri düzenlemek.",
        "yasakli_kelimeler": ["deri defter", "dana dili", "toplama", "yazma", "arşiv"],
        "zorluk": "orta"
    },
    {
        "kelime": "İlahi Okumak",
        "aciklama": "Tasavvuf halk edebiyatında Yunus Emre tarzı ilahi aşkı anlatan şiirler seslendirmek.",
        "yasakli_kelimeler": ["yunus emre", "tasavvuf", "ilahi aşk", "tekke", "ezgi"],
        "zorluk": "orta"
    },
    {
        "kelime": "Nefes Çağırmak",
        "aciklama": "Bektaşi tekkelerinde tasavvufi öğreti ve cem ritüellerini anlatan şiirler söylemek.",
        "yasakli_kelimeler": ["bektaşi", "tekke", "cem", "pir sultan", "tasavvuf"],
        "zorluk": "orta"
    },
    {
        "kelime": "Devriye Düzmek",
        "aciklama": "Tasavvufta ruhun tanrıdan gelip tekrar tanrıya dönüşünü anlatan felsefi şiir yazmak.",
        "yasakli_kelimeler": ["tasavvuf", "ruh", "dönüş", "nüzul", "uruc"],
        "zorluk": "orta"
    },
    {
        "kelime": "Şathiye Söylemek",
        "aciklama": "Görünüşte dinle alay eder gibi duran ancak derin tasavvufi anlamlar içeren şiir okumak.",
        "yasakli_kelimeler": ["tasavvuf", "alay", "kaygusuz abdal", "derin anlam", "cezbeli"],
        "zorluk": "orta"
    },

    # Zor (14)
    {
        "kelime": "Lebdeğmez Atışmak",
        "aciklama": "Dudakların birbirine değmesini engelleyen iğne ağızdayken b, p, m, v, f harflerini kullanmadan şiir söylemek.",
        "yasakli_kelimeler": ["dudakdeğmez", "iğne", "b p m", "yasak harf", "zor atışma"],
        "zorluk": "zor"
    },
    {
        "kelime": "Muamma Asmak",
        "aciklama": "Kahvehaneye asılan manzum bilmece levhasını çözüp içindeki gizli ismi bulmak.",
        "yasakli_kelimeler": ["askı", "gizli isim", "bilmece", "kahvehane", "çözmek"],
        "zorluk": "zor"
    },
    {
        "kelime": "Ayak Bağlamak",
        "aciklama": "Aşık atışmasında kafiye ve redif kuralını zorlaştırarak rakip ozanı köşeye sıkıştırmak.",
        "yasakli_kelimeler": ["kafiye kalıbı", "redif", "başlatmak", "kural koymak", "ilk dize"],
        "zorluk": "zor"
    },
    {
        "kelime": "Kafiye Bağı Kurmak",
        "aciklama": "Mısra sonlarında zengin ve tam kafiyeler oluşturarak dize ahengini güçlendirmek.",
        "yasakli_kelimeler": ["cevap", "uyak", "kalıp", "sürdürmek", "kural"],
        "zorluk": "zor"
    },
    {
        "kelime": "Saz Askısı İndirmek",
        "aciklama": "Kahvehanede asılı duran muammayı doğru çözerek duvardaki ödül sazı almaya hak kazanmak.",
        "yasakli_kelimeler": ["ödül", "çözüm", "duvar", "hak etmek", "kazanmak"],
        "zorluk": "zor"
    },
    {
        "kelime": "Zincirbend Koşmak",
        "aciklama": "Bir önceki dörtlüğün son dizesinin ilk kelimesiyle yeni dörtlüğe başlanan zincirleme nazım.",
        "yasakli_kelimeler": ["zincirleme", "son dize", "ilk kelime", "bağlantı", "dörtlük"],
        "zorluk": "zor"
    },
    {
        "kelime": "Musammat Koşma Dizmek",
        "aciklama": "Dizelerin ortalarında iç kafiye barındıran teknik ve zor bir halk şiiri yapısı kurmak.",
        "yasakli_kelimeler": ["iç kafiye", "orta uyak", "teknik", "mısra içi", "zor biçim"],
        "zorluk": "zor"
    },
    {
        "kelime": "Sicilleme Nazmetmek",
        "aciklama": "Aşık edebiyatında aynı kafiye ve vezinle uzun tekerrürler halinde destansı şiir söylemek.",
        "yasakli_kelimeler": ["tekerrür", "uzun", "destansı", "aynı kafiye", "vezin"],
        "zorluk": "zor"
    },
    {
        "kelime": "Kalıp Düzeltmesi Yapmak",
        "aciklama": "Halk şiirinde hece fazlalığı veya eksikliğini hece kaynaştırmasıyla imale ve zihaf gibi dengelemek.",
        "yasakli_kelimeler": ["fazlalık", "eksiklik", "kaynaştırma", "denge", "hece"],
        "zorluk": "zor"
    },
    {
        "kelime": "Mürşid Nutku Söylemek",
        "aciklama": "Tekkeye yeni giren dervişe tarikat adap ve erkanını öğreten didaktik nutuk şiiri okumak.",
        "yasakli_kelimeler": ["derviş", "adap", "erkan", "didaktik", "öğüt"],
        "zorluk": "zor"
    },
    {
        "kelime": "Vücutname Yazmak",
        "aciklama": "İnsanın ana rahmine düşüşünden ölümüne kadarki yaş evrelerini anlatan tasavvufi şiir kaleme almak.",
        "yasakli_kelimeler": ["yaş", "anne karnı", "evrim", "hayat safhası", "ölüm"],
        "zorluk": "zor"
    },
    {
        "kelime": "Tekerlemeyle Başlamak",
        "aciklama": "Masal anlatıcısının 'Bir varmış bir yokmuş' gibi sürreal kafiyeli tekerleme döşemesi.",
        "yasakli_kelimeler": ["masal başı", "deve tellal", "tekerleme", "döşeme", "giriş"],
        "zorluk": "zor"
    },
    {
        "kelime": "Anonimleştirmek",
        "aciklama": "Söyleyeni zamanla unutularak eserin tüm halkın ortak kültürel mirasına dönüşmesi.",
        "yasakli_kelimeler": ["sahipsiz", "ortak miras", "halk malı", "unutulmak", "yüzyıllar"],
        "zorluk": "zor"
    },
    {
        "kelime": "Geleneksel İcrayı Yaşatmak",
        "aciklama": "Kuşaktan kuşağa sözlü aktarılan halk edebiyatı mirasını aslına sadık kalarak sürdürmek.",
        "yasakli_kelimeler": ["sözlü kültür", "kuşak", "aslına sadık", "yaşatma", "miras"],
        "zorluk": "zor"
    }
]

# 2. TURKIYECOGRAFYASI (50 verbs: 12 kolay, 24 orta, 14 zor)
turkiyecografyasi_verbs = [
    # Kolay (12)
    {
        "kelime": "Dağa Tırmanmak",
        "aciklama": "Türkiye'nin Ağrı, Erciyes veya Kaçkar gibi yüksek zirvelerine çıkmak.",
        "yasakli_kelimeler": ["zirve", "tırmanış", "ağrı", "erciyes", "yüksek"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Denize Girmek",
        "aciklama": "Akdeniz, Ege, Karadeniz veya Marmara kıyılarında yüzmek.",
        "yasakli_kelimeler": ["akdeniz", "ege", "kıyı", "yüzmek", "sahil"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Boğazdan Geçmek",
        "aciklama": "İstanbul veya Çanakkale Boğazı'nda vapur veya gemiyle seyretmek.",
        "yasakli_kelimeler": ["istanbul", "çanakkale", "vapur", "gemi", "geçiş"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Göl Kenarında Gezmek",
        "aciklama": "Van, Tuz veya Beyşehir Gölü çevresinde yürüyüş yapmak.",
        "yasakli_kelimeler": ["van", "tuz gölü", "su", "yürüyüş", "kıyı"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Yaylaya Çıkmak",
        "aciklama": "Yaz sıcaklarında Karadeniz ve Torosların serin yüksek otlaklarına göçmek.",
        "yasakli_kelimeler": ["karadeniz", "toroslar", "serin", "yüksek", "otlak"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Nehirde Kürek Çekmek",
        "aciklama": "Fırat, Dicle, Kızılırmak veya Çoruh Nehri üzerinde botla ilerlemek.",
        "yasakli_kelimeler": ["fırat", "dicle", "kızılırmak", "çoruh", "bot"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Harita İncelemek",
        "aciklama": "Türkiye'nin fiziki veya idari haritasındaki sınır ve yer şekillerine bakmak.",
        "yasakli_kelimeler": ["fiziki", "idari", "sınır", "şehirler", "ölçek"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Ovaları Sulamak",
        "aciklama": "Çukurova, Konya veya Bafra Ovası'ndaki tarım arazilerine su vermek.",
        "yasakli_kelimeler": ["çukurova", "konya", "tarım", "arazi", "su"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Mağara Keşfetmek",
        "aciklama": "Damlataş, Karain veya Ballıca gibi karstik yer altı boşluklarını gezmek.",
        "yasakli_kelimeler": ["damlataş", "sarkıt", "dikit", "yeraltı", "karstik"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Körfezi Dolaşmak",
        "aciklama": "İzmir, Antalya veya Edremit Körfezi kıyılarında seyahat etmek.",
        "yasakli_kelimeler": ["izmir", "antalya", "edremit", "koy", "kıyı"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Ormanda Yürümek",
        "aciklama": "Batı Karadeniz veya Torosların gür orman örtüsü içinde doğa yürüyüşü yapmak.",
        "yasakli_kelimeler": ["ağaç", "doğa", "karadeniz", "yürüyüş", "çam"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Şelale Seyretmek",
        "aciklama": "Düden, Manavgat veya Muradiye Şelalesi'nin dökülen sularını izlemek.",
        "yasakli_kelimeler": ["düden", "manavgat", "su dökülmesi", "izlemek", "akarsu"],
        "zorluk": "kolay"
    },

    # Orta (24)
    {
        "kelime": "Peri Bacalarını Gezmek",
        "aciklama": "Kapadokya bölgesindeki volkanik tüflerin aşınmasıyla oluşan yapıları incelemek.",
        "yasakli_kelimeler": ["kapadokya", "tüf", "aşınma", "volkanik", "ürgüp"],
        "zorluk": "orta"
    },
    {
        "kelime": "Delta Ovası Oluşturmak",
        "aciklama": "Kızılırmak ve Yeşilırmak'ın taşıdığı alüvyonlarla denizi doldurup ova yapması.",
        "yasakli_kelimeler": ["alüvyon", "bafra", "çarşamba", "deniz", "kıyı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Fay Hattını İncelemek",
        "aciklama": "Kuzey Anadolu (KAF) veya Doğu Anadolu deprem kırık hatlarının jeolojisini araştırmak.",
        "yasakli_kelimeler": ["deprem", "kuzey anadolu", "kırık", "sismik", "levha"],
        "zorluk": "orta"
    },
    {
        "kelime": "Travertenleri Ziyaret Etmek",
        "aciklama": "Pamukkale'de kalsiyum bikarbonatlı termal suların çökelmesiyle oluşan beyaz terasları görmek.",
        "yasakli_kelimeler": ["pamukkale", "beyaz", "kalsiyum", "termal", "çökelme"],
        "zorluk": "orta"
    },
    {
        "kelime": "Akdeniz İklimini Yaşamak",
        "aciklama": "Yazları sıcak ve kurak, kışları ılık ve yağışlı geçen iklim kuşağını tecrübe etmek.",
        "yasakli_kelimeler": ["yaz sıcak", "kış ılık", "yağış", "maki", "kuşak"],
        "zorluk": "orta"
    },
    {
        "kelime": "Karasal İklime Uyum Sağlamak",
        "aciklama": "İç Anadolu ve Doğu Anadolu'daki sert kışlara ve yüksek gece-gündüz sıcaklık farkına alışmak.",
        "yasakli_kelimeler": ["iç anadolu", "sert kış", "step", "sıcaklık farkı", "ayaz"],
        "zorluk": "orta"
    },
    {
        "kelime": "Karadeniz İklimini Gözlemlemek",
        "aciklama": "Her mevsim düzenli yağış alan ve nem oranı yüksek bölgenin florasını izlemek.",
        "yasakli_kelimeler": ["dört mevsim yağış", "nem", "flora", "sis", "orman"],
        "zorluk": "orta"
    },
    {
        "kelime": "Karasallık Şiddetini Ölçmek",
        "aciklama": "Denizden uzaklaştıkça ve yükselti arttıkça yıllık sıcaklık genliğindeki artışı saptamak.",
        "yasakli_kelimeler": ["denizden uzak", "genlik", "yükselti", "doğu anadolu", "sıcaklık farkı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Maki Bitki Örtüsünü Tanımak",
        "aciklama": "Zeytin, defne, mersin gibi bodur ve sert yapraklı Akdeniz çalılarını incelemek.",
        "yasakli_kelimeler": ["çalı", "zeytin", "defne", "akdeniz", "bodur"],
        "zorluk": "orta"
    },
    {
        "kelime": "Bozkır Alanları Taramak",
        "aciklama": "İlkbahar yağışlarıyla yeşerip yazın sararan İç Anadolu step otlaklarını gözlemlemek.",
        "yasakli_kelimeler": ["step", "otlak", "iç anadolu", "ilkbahar", "sararma"],
        "zorluk": "orta"
    },
    {
        "kelime": "Platolara Çıkmak",
        "aciklama": "Haymana, Cihanbeyli, Bozok veya Erzurum-Kars gibi akarsularla yarılmış yüksek düzlükleri gezmek.",
        "yasakli_kelimeler": ["yüksek düzlük", "haymana", "cihanbeyli", "bozok", "aşınım"],
        "zorluk": "orta"
    },
    {
        "kelime": "Falezleri Fotoğraflamak",
        "aciklama": "Antalya veya Karadeniz kıyılarında dalga aşındırmasıyla oluşan dik yalıyarları çekmek.",
        "yasakli_kelimeler": ["yalıyar", "dik uçurum", "dalga", "antalya", "kıyı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Ria Tipi Kıyı Görmek",
        "aciklama": "İstanbul Boğazı ve Haliç gibi eski akarsu vadilerinin deniz altında kalmasıyla oluşan kıyıyı incelemek.",
        "yasakli_kelimeler": ["haliç", "boğaz", "eski vadi", "su basması", "kıyı tipi"],
        "zorluk": "orta"
    },
    {
        "kelime": "Tombolo Oluşumunu İncelemek",
        "aciklama": "Kapıdağ Yarımadası veya Sinop İnceburun gibi adanın karaya bağlanması sürecini araştırmak.",
        "yasakli_kelimeler": ["saplı ada", "kapıdağ", "sinop", "dalga biriktirmesi", "bağlantı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Lagün Kıyısında Kuş Saymak",
        "aciklama": "Büyükçekmece, Küçükçekmece veya Akyatan gibi deniz kulağı göllerinde gözlem yapmak.",
        "yasakli_kelimeler": ["deniz kulağı", "kıyı set gölü", "büyükçekmece", "dalga", "gözlem"],
        "zorluk": "orta"
    },
    {
        "kelime": "Heyelan Alanını Haritalamak",
        "aciklama": "Karadeniz'in dik ve killi yamaçlarında toprağın kütle halinde kaydığı bölgeleri çizmek.",
        "yasakli_kelimeler": ["toprak kayması", "eğim", "kil", "yağış", "karadeniz"],
        "zorluk": "orta"
    },
    {
        "kelime": "Erozyonla Mücadele Etmek",
        "aciklama": "İç ve Güneydoğu Anadolu'da rüzgâr ve suyun toprağı süpürmesini engellemek için ağaçlandırma yapmak.",
        "yasakli_kelimeler": ["toprak kaybı", "ağaçlandırma", "tema", "çölleşme", "rüzgar"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kaplıcalara Gitmek",
        "aciklama": "Afyon, Bursa veya Yalova'daki fay hatlarından çıkan şifalı sıcak sulara girmek.",
        "yasakli_kelimeler": ["termal", "şifalı su", "afyon", "bursa", "fay kaynağı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Sönmüş Volkanı İncelemek",
        "aciklama": "Nemrut, Süphan, Tendürek veya Hasan Dağı gibi eski volkanik dağları araştırmak.",
        "yasakli_kelimeler": ["nemrut", "hasan dağı", "süphan", "krater", "lav"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kapalı Havzayı İncelemek",
        "aciklama": "Sularını denize ulaştıramayan Tuz Gölü veya Van Gölü havzasının hidrolojisini çalışmak.",
        "yasakli_kelimeler": ["tuz gölü", "denize ulaşamama", "tuzlu", "hidroloji", "iç drenaj"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kanyon Vadiden Geçmek",
        "aciklama": "Köprülü Kanyon, Saklıkent veya Ihlara gibi akarsuyun derine oyduğu dar yarıklardan yürümek.",
        "yasakli_kelimeler": ["saklıkent", "ihlara", "köprülü", "derin vadi", "yarık"],
        "zorluk": "orta"
    },
    {
        "kelime": "Akarsu Rejimini Çözümlemek",
        "aciklama": "Türkiye nehirlerinin mevsimlere göre akım (debi) dalgalanmalarını grafiklemek.",
        "yasakli_kelimeler": ["debi", "akım", "düzensiz rejim", "mevsim", "taşkın"],
        "zorluk": "orta"
    },
    {
        "kelime": "Geçitlerden Aşmak",
        "aciklama": "Zigana, Kop, Gülek veya Çubuk gibi dağ sıralarını aşan tarihi geçitlerden yolculuk etmek.",
        "yasakli_kelimeler": ["gülek", "zigana", "kop", "dağ sırası", "karayolu"],
        "zorluk": "orta"
    },
    {
        "kelime": "Nüfus Yoğunluğunu Hesaplamak",
        "aciklama": "Türkiye'nin kıyı şeritleri ile dağlık iç kesimleri arasındaki kilometrekareye düşen insan sayısını bulmak.",
        "yasakli_kelimeler": ["aritmetik nüfus", "kilometrekare", "kıyı", "tenha", "yoğun"],
        "zorluk": "orta"
    },

    # Zor (14)
    {
        "kelime": "Epirojenez Hareketlerini İzlemek",
        "aciklama": "Anadolu levhasının toptan yükselmesi ve Karadeniz-Akdeniz çanaklarının çökmesini tahlil etmek.",
        "yasakli_kelimeler": ["kıta oluşumu", "toptan yükselme", "izostatik denge", "levha", "üçüncü zaman"],
        "zorluk": "zor"
    },
    {
        "kelime": "Orojenez Kuşaklarını İncelemek",
        "aciklama": "Alp-Himalaya kıvrım kuşağına dahil olan Kuzey Anadolu Dağları ve Torosların oluşumunu analiz etmek.",
        "yasakli_kelimeler": ["dağ oluşumu", "alp himalaya", "kıvrılma", "kırılma", "horst graben"],
        "zorluk": "zor"
    },
    {
        "kelime": "Horst ve Grabenleri Ayırt Etmek",
        "aciklama": "Ege Bölgesi'ndeki faylanmayla yükselen dağlar (Bozdağlar) ile çöken ovaları (Gediz, Menderes) saptamak.",
        "yasakli_kelimeler": ["kırık dağ", "ege", "gediz", "menderes", "çöküntü ovası"],
        "zorluk": "zor"
    },
    {
        "kelime": "Karstik Aşınımı Ölçmek",
        "aciklama": "Toroslardaki kalkerli arazilerde dolin, uvala, polye ve lapyaların kimyasal erimesini hesaplamak.",
        "yasakli_kelimeler": ["polye", "uvala", "dolin", "kalker", "lapya"],
        "zorluk": "zor"
    },
    {
        "kelime": "Sirk Göllerini Araştırmak",
        "aciklama": "Buzul çağında Kaçkar, Uludağ veya Cilo Dağları'nda buzulların oyduğu buzul yalağı göllerini incelemek.",
        "yasakli_kelimeler": ["buzul yalağı", "kaçkar", "cilo", "glasiyal", "yüksek dağ"],
        "zorluk": "zor"
    },
    {
        "kelime": "Dalmaçya Tipi Kıyıyı Tahlil Etmek",
        "aciklama": "Kaş ve Finike kıyılarında denize paralel uzanan dağların sular altında kalarak adacıklara dönüşmesini incelemek.",
        "yasakli_kelimeler": ["kaş", "finike", "kıyı tipi", "paralel adalar", "sualtı"],
        "zorluk": "zor"
    },
    {
        "kelime": "Boyuna Kıyı Profilini Çıkarmak",
        "aciklama": "Karadeniz ve Akdeniz'de dağların denize paralel uzanması sebebiyle iç kesimlere nemin giremeyişini modellemek.",
        "yasakli_kelimeler": ["paralel", "karadeniz", "akdeniz", "nem engeli", "limansız"],
        "zorluk": "zor"
    },
    {
        "kelime": "Enine Kıyı Tipini Haritalamak",
        "aciklama": "Ege'de dağların denize dik uzanması sonucu oluşan çok sayıda koy, körfez ve yarımadayı çizmek.",
        "yasakli_kelimeler": ["denize dik", "ege", "koy körfez", "girintili çıkıntılı", "derinlik"],
        "zorluk": "zor"
    },
    {
        "kelime": "Kaldera Oluşumunu Belgelemek",
        "aciklama": "Nemrut Dağı zirvesindeki devasa volkanik patlama kraterinin çökmesiyle oluşan gölü incelemek.",
        "yasakli_kelimeler": ["nemrut gölü", "patlama krateri", "çöküntü", "volkan ağzı", "jeotermal"],
        "zorluk": "zor"
    },
    {
        "kelime": "Tersiyer Formasyonunu Yaşlandırmak",
        "aciklama": "Türkiye arazisinin büyük bölümünü oluşturan Neojen ve Paleojen kayaç katmanlarını tarihlendirmek.",
        "yasakli_kelimeler": ["üçüncü jeolojik zaman", "neojen", "tabaka", "tarihlendirme", "fosil"],
        "zorluk": "zor"
    },
    {
        "kelime": "İklim Mikroklimasını Tespit Etmek",
        "aciklama": "Rize'de turunçgil, Iğdır'da pamuk veya Anamur'da muz yetişmesini sağlayan yerel korunaklı iklimi belirlemek.",
        "yasakli_kelimeler": ["rize", "ığdır", "anamur", "yerel iklim", "turunçgil"],
        "zorluk": "zor"
    },
    {
        "kelime": "Menderes Çizimini Modellemek",
        "aciklama": "Ege akarsularının eğimin azaldığı tabanlarda S harfi şeklinde büklümler yaparak akmasını simüle etmek.",
        "yasakli_kelimeler": ["büklüm", "s şekli", "eğim azlığı", "büyük menderes", "aşındırma biriktirme"],
        "zorluk": "zor"
    },
    {
        "kelime": "Rüzgâr Aşındırmasını İncelemek",
        "aciklama": "Konya Karapınar çevresindeki kumulların ve yardang oluşumlarının dinamiklerini çalışmak.",
        "yasakli_kelimeler": ["karapınar", "kumul", "yardang", "kuraklık", "rüzgar erozyonu"],
        "zorluk": "zor"
    },
    {
        "kelime": "Akifer Kapasitesini Hesaplamak",
        "aciklama": "İç Anadolu ve Güneydoğu'daki yeraltı su havzalarının beslenme ve çekim dengesini ölçmek.",
        "yasakli_kelimeler": ["yeraltı suyu", "rezerv", "obruk", "su tablası", "çekim dengesi"],
        "zorluk": "zor"
    }
]

if __name__ == "__main__":
    add_and_save_verbs("turkhalkedebiyati", turkhalkedebiyati_verbs)
    add_and_save_verbs("turkiyecografyasi", turkiyecografyasi_verbs)
