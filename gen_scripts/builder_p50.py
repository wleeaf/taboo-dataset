import sys
from card_utils import add_and_save_verbs

# 1. TERMODINAMIK (50 verbs: 12 kolay, 24 orta, 14 zor)
termodinamik_verbs = [
    # Kolay (12)
    {
        "kelime": "Isıtmak",
        "aciklama": "Bir maddenin sıcaklığını artırmak için ona ısı enerjisi vermek.",
        "yasakli_kelimeler": ["sıcaklık", "enerji", "ateş", "artırmak", "soğuk"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Soğutmak",
        "aciklama": "Bir maddeden ısı çekerek sıcaklığını düşürmek.",
        "yasakli_kelimeler": ["sıcaklık", "düşürmek", "buz", "ısı", "ortam"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Kaynamak",
        "aciklama": "Sıvının buhar basıncının dış basınca eşitlendiği anda hızla buharlaşması.",
        "yasakli_kelimeler": ["buhar", "sıvı", "fokurdama", "sıcaklık", "su"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Erimek",
        "aciklama": "Katı bir maddenin ısı alarak sıvı faza geçmesi.",
        "yasakli_kelimeler": ["katı", "sıvı", "buz", "ısı", "faz"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Donmak",
        "aciklama": "Sıvı bir maddenin ısısını kaybederek katı faza geçmesi.",
        "yasakli_kelimeler": ["sıvı", "katı", "buz", "soğuk", "faz"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Buharlaşmak",
        "aciklama": "Sıvı yüzeyindeki moleküllerin gaz fazına geçmesi.",
        "yasakli_kelimeler": ["sıvı", "gaz", "buhar", "uçmak", "yüzey"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Yoğuşmak",
        "aciklama": "Gaz halindeki bir maddenin ısı vererek sıvı hale dönmesi.",
        "yasakli_kelimeler": ["gaz", "sıvı", "damla", "buhar", "soğuma"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Genleşmek",
        "aciklama": "Isınan cisimlerin hacimlerinin ve boyutlarının büyümesi.",
        "yasakli_kelimeler": ["hacim", "sıcaklık", "büyümek", "boyut", "genişleme"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Büzülmek",
        "aciklama": "Soğuyan cisimlerin hacimlerinin ve boyutlarının küçülmesi.",
        "yasakli_kelimeler": ["küçülmek", "hacim", "soğuk", "daralmak", "boyut"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Sıcaklığı Ölçmek",
        "aciklama": "Termometre kullanarak bir sistemin sıcaklık değerini tespit etmek.",
        "yasakli_kelimeler": ["termometre", "derece", "kelvin", "celcius", "tespit"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Basınç Uygulamak",
        "aciklama": "Birim yüzeye dik olarak kuvvet etki ettirmek.",
        "yasakli_kelimeler": ["kuvvet", "yüzey", "bar", "paskal", "etki"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Enerji Vermek",
        "aciklama": "Bir sisteme iş veya ısı yoluyla enerji girişi sağlamak.",
        "yasakli_kelimeler": ["ısı", "iş", "giriş", "sistem", "artış"],
        "zorluk": "kolay"
    },

    # Orta (24)
    {
        "kelime": "İş Yapmak",
        "aciklama": "Kuvvet uygulayarak bir gazın hacmini değiştirmek veya sistemi hareket ettirmek.",
        "yasakli_kelimeler": ["kuvvet", "hacim", "enerji", "hareket", "w"],
        "zorluk": "orta"
    },
    {
        "kelime": "Isıl Dengeye Ulaşmak",
        "aciklama": "Temas halindeki iki sistemin sıcaklıklarının eşitlenerek ısı akışının durması.",
        "yasakli_kelimeler": ["sıcaklık", "eşit", "temas", "ısı akışı", "durma"],
        "zorluk": "orta"
    },
    {
        "kelime": "Isı Yalıtımı Yapmak",
        "aciklama": "Bir sistem ile çevresi arasındaki ısı transferini minimuma indirmek.",
        "yasakli_kelimeler": ["transfer", "çevre", "izolasyon", "kayıp", "malzeme"],
        "zorluk": "orta"
    },
    {
        "kelime": "Süblimleşmek",
        "aciklama": "Katı bir maddenin sıvı hale geçmeden doğrudan gaz fazına dönüşmesi.",
        "yasakli_kelimeler": ["katı", "gaz", "sıvı", "doğrudan", "kuru buz"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kırağılaşmak",
        "aciklama": "Gaz halindeki bir maddenin sıvılaşmadan doğrudan katı faza geçmesi.",
        "yasakli_kelimeler": ["gaz", "katı", "doğrudan", "buz", "soğuk"],
        "zorluk": "orta"
    },
    {
        "kelime": "Isı İletmek",
        "aciklama": "Katı maddelerde moleküler titreşimler yoluyla ısının bir noktadan diğerine taşınması.",
        "yasakli_kelimeler": ["kondüksiyon", "titreşim", "katı", "taşınma", "metal"],
        "zorluk": "orta"
    },
    {
        "kelime": "Konveksiyon Yapmak",
        "aciklama": "Akışkanlarda sıcak ve soğuk kütlelerin yer değiştirmesiyle ısının yayılması.",
        "yasakli_kelimeler": ["akışkan", "yer değiştirme", "akım", "sıvı", "gaz"],
        "zorluk": "orta"
    },
    {
        "kelime": "Işınım Yaymak",
        "aciklama": "Isı enerjisinin elektromanyetik dalgalar (radyasyon) yoluyla boşlukta yayılması.",
        "yasakli_kelimeler": ["radyasyon", "dalga", "elektromanyetik", "boşluk", "güneş"],
        "zorluk": "orta"
    },
    {
        "kelime": "Entropiyi Artırmak",
        "aciklama": "Kapalı bir sistemdeki düzensizlik ve mikroskobik olasılık durumunu yükseltmek.",
        "yasakli_kelimeler": ["düzensizlik", "sistem", "ikinci yasa", "kaos", "artış"],
        "zorluk": "orta"
    },
    {
        "kelime": "Entalpi Hesaplamak",
        "aciklama": "Bir sistemin iç enerjisi ile basınç-hacim çarpımının toplam ısı içeriğini belirlemek.",
        "yasakli_kelimeler": ["iç enerji", "ısı içeriği", "h", "basınç", "hacim"],
        "zorluk": "orta"
    },
    {
        "kelime": "Sıkıştırmak",
        "aciklama": "Gazın hacmini küçülterek basıncını ve sıcaklığını artırmak.",
        "yasakli_kelimeler": ["hacim", "gaz", "basınç", "piston", "küçültmek"],
        "zorluk": "orta"
    },
    {
        "kelime": "Genleşmeye Bırakmak",
        "aciklama": "Gazın hacminin artarak çevreye karşı iş yapmasına izin vermek.",
        "yasakli_kelimeler": ["hacim", "artış", "iş", "piston", "serbest"],
        "zorluk": "orta"
    },
    {
        "kelime": "Faz Değiştirmek",
        "aciklama": "Maddenin sıcaklığı sabit kalırken katı, sıvı veya gaz halleri arasında geçiş yapması.",
        "yasakli_kelimeler": ["katı", "sıvı", "gaz", "hal", "gizli ısı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Gizli Isı Almak",
        "aciklama": "Faz değişimi esnasında sıcaklık değişmeden emilen ısı enerjisi.",
        "yasakli_kelimeler": ["faz", "sıcaklık", "erime", "buharlaşma", "enerji"],
        "zorluk": "orta"
    },
    {
        "kelime": "Termal Şok Yaşamak",
        "aciklama": "Ani ve aşırı sıcaklık değişimi nedeniyle malzemenin çatlaması veya kırılması.",
        "yasakli_kelimeler": ["ani", "çatlama", "sıcaklık", "kırılma", "değişim"],
        "zorluk": "orta"
    },
    {
        "kelime": "Isı Sığasını Bulmak",
        "aciklama": "Bir maddenin sıcaklığını bir derece artırmak için gereken ısı miktarını ölçmek.",
        "yasakli_kelimeler": ["özgül ısı", "derece", "miktar", "kapasite", "c"],
        "zorluk": "orta"
    },
    {
        "kelime": "Döngüyü Tamamlamak",
        "aciklama": "Termodinamik bir akışkanın başlangıç durumuna döndüğü çevrimi bitirmek.",
        "yasakli_kelimeler": ["çevrim", "akışkan", "başlangıç", "durum", "döngü"],
        "zorluk": "orta"
    },
    {
        "kelime": "Verimi Hesaplamak",
        "aciklama": "Alınan yararlı işin sisteme verilen toplam ısı enerjisine oranını bulmak.",
        "yasakli_kelimeler": ["iş", "oran", "ısı", "kayıp", "yüzde"],
        "zorluk": "orta"
    },
    {
        "kelime": "İç Enerjiyi Değiştirmek",
        "aciklama": "Sistemin moleküler kinetik ve potansiyel enerjilerinin toplamını artırıp azaltmak.",
        "yasakli_kelimeler": ["kinetik", "potansiyel", "molekül", "toplam", "u"],
        "zorluk": "orta"
    },
    {
        "kelime": "Soğutucu Akışkan Dolaştırmak",
        "aciklama": "Buzdolabı veya klimada evaporatör ve kondenser arasında gaz dolaştırmak.",
        "yasakli_kelimeler": ["klima", "buzdolabı", "gaz", "kompresör", "kondenser"],
        "zorluk": "orta"
    },
    {
        "kelime": "Pistonu İtmek",
        "aciklama": "Silindir içindeki gaz basıncının kuvvetiyle mekanik kolu hareket ettirmek.",
        "yasakli_kelimeler": ["silindir", "gaz", "mekanik", "kuvvet", "hareket"],
        "zorluk": "orta"
    },
    {
        "kelime": "Isı Kaybını Önlemek",
        "aciklama": "Yalıtım ve bariyerlerle sistemden dış çevreye olan kaçakları engellemek.",
        "yasakli_kelimeler": ["kaçak", "çevre", "engel", "yalıtım", "kayıp"],
        "zorluk": "orta"
    },
    {
        "kelime": "Durum Değişkeni Belirlemek",
        "aciklama": "Sistemin termodinamik halini tanımlayan basınç, sıcaklık ve hacim değerlerini saptamak.",
        "yasakli_kelimeler": ["basınç", "sıcaklık", "hacim", "hal", "tanım"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kapalı Sistem Oluşturmak",
        "aciklama": "Madde giriş çıkışına kapalı fakat enerji transferine açık bir ortam kurmak.",
        "yasakli_kelimeler": ["madde", "enerji", "giriş", "çıkış", "sınır"],
        "zorluk": "orta"
    },

    # Zor (14)
    {
        "kelime": "İzotermal Genleşmek",
        "aciklama": "Sıcaklığı tamamen sabit tutarak gazın hacmini artırıp basıncını düşürmek.",
        "yasakli_kelimeler": ["sabit", "sıcaklık", "hacim", "basınç", "ters orantı"],
        "zorluk": "zor"
    },
    {
        "kelime": "Adyabatik Sıkışmak",
        "aciklama": "Çevreyle hiçbir ısı alışverişi olmadan gazın sıkıştırılıp sıcaklığının artması.",
        "yasakli_kelimeler": ["ısı alışverişi", "yalıtımlı", "hacim", "sıcaklık", "q=0"],
        "zorluk": "zor"
    },
    {
        "kelime": "İzobarik Isınmak",
        "aciklama": "Basıncı sabit tutularak sisteme ısı verilip hacminin genişletilmesi.",
        "yasakli_kelimeler": ["sabit", "basınç", "hacim", "genleşme", "ısı"],
        "zorluk": "zor"
    },
    {
        "kelime": "İzokorik Soğumak",
        "aciklama": "Hacmi sabit tutulan bir sistemden ısı çekilerek basıncının düşürülmesi.",
        "yasakli_kelimeler": ["sabit", "hacim", "basınç", "rijit", "iş=0"],
        "zorluk": "zor"
    },
    {
        "kelime": "Carnot Çevrimi Yapmak",
        "aciklama": "İki izotermal ve iki adyabatik süreçten oluşan teorik maksimum verimli çevrimi işletmek.",
        "yasakli_kelimeler": ["verim", "teorik", "izotermal", "adyabatik", "çevrim"],
        "zorluk": "zor"
    },
    {
        "kelime": "Joule-Thomson Genleşmesi Yapmak",
        "aciklama": "Gazın gözenekli bir tıkaç veya vanadan geçerken entalpisi sabit kalarak sıcaklık değiştirmesi.",
        "yasakli_kelimeler": ["vana", "kısılma", "entalpi", "soğuma", "gaz"],
        "zorluk": "zor"
    },
    {
        "kelime": "Tersinir Süreç İşletmek",
        "aciklama": "Sistem ve çevrede hiçbir kalıcı iz veya entropi artışı bırakmadan geri döndürülebilen ideal süreç.",
        "yasakli_kelimeler": ["ideal", "geri dönüş", "entropi", "kayıp", "sürtünmesiz"],
        "zorluk": "zor"
    },
    {
        "kelime": "Tersinmezlik Üretmek",
        "aciklama": "Sürtünme, ani genleşme veya ısı farkı nedeniyle sistemde yok edilemez entropi oluşturmak.",
        "yasakli_kelimeler": ["sürtünme", "kayıp", "entropi", "gerçek", "üretim"],
        "zorluk": "zor"
    },
    {
        "kelime": "Rankine Çevrimini Çalıştırmak",
        "aciklama": "Termik santrallerde buharın türbin ve kondenser arasında dolaştırılarak elektrik üretilmesi.",
        "yasakli_kelimeler": ["santral", "buhar", "türbin", "kondenser", "elektrik"],
        "zorluk": "zor"
    },
    {
        "kelime": "Ekserji Analizi Yapmak",
        "aciklama": "Bir enerji kaynağından teorik olarak elde edilebilecek maksimum yararlı iş potansiyelini hesaplamak.",
        "yasakli_kelimeler": ["kullanılabilirlik", "iş potansiyeli", "kalite", "kayıp", "enerji"],
        "zorluk": "zor"
    },
    {
        "kelime": "Gibbs Serbest Enerjisini Hesaplamak",
        "aciklama": "Sabit sıcaklık ve basınçta bir kimyasal reaksiyonun kendiliğindenliğini belirleyen potansiyeli bulmak.",
        "yasakli_kelimeler": ["kendiliğinden", "spontan", "delta g", "reaksiyon", "potansiyel"],
        "zorluk": "zor"
    },
    {
        "kelime": "Üçlü Noktaya Ulaşmak",
        "aciklama": "Maddenin katı, sıvı ve gaz fazlarının aynı anda dengede bulunduğu sıcaklık ve basınç noktası.",
        "yasakli_kelimeler": ["üç faz", "denge", "katı", "sıvı", "gaz"],
        "zorluk": "zor"
    },
    {
        "kelime": "Süperkritik Faza Geçmek",
        "aciklama": "Kritik sıcaklık ve basıncın üzerine çıkarak sıvı ve gaz ayrımının ortadan kalktığı akışkan haline gelmek.",
        "yasakli_kelimeler": ["kritik nokta", "akışkan", "sıvı", "gaz", "ayrım"],
        "zorluk": "zor"
    },
    {
        "kelime": "Mutlak Sıfıra Yaklaşmak",
        "aciklama": "Sıcaklığı teorik olarak tüm moleküler hareketin durduğu sıfır Kelvin noktasına indirmeye çalışmak.",
        "yasakli_kelimeler": ["0 kelvin", "-273", "molekül", "üçüncü yasa", "hareketsizlik"],
        "zorluk": "zor"
    }
]

# 2. TESISAT (50 verbs: 12 kolay, 24 orta, 14 zor)
tesisat_verbs = [
    # Kolay (12)
    {
        "kelime": "Boru Döşemek",
        "aciklama": "Su veya gaz iletimi için hat boyunca boruları yerleştirmek.",
        "yasakli_kelimeler": ["hat", "su", "gaz", "yerleştirmek", "plastik"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Musluk Takmak",
        "aciklama": "Lavabo veya tezgaha su akışını kontrol eden bataryayı monte etmek.",
        "yasakli_kelimeler": ["batarya", "lavabo", "su", "montaj", "vana"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Vanayı Kapatmak",
        "aciklama": "Boru hattındaki su veya gaz akışını durdurmak için vanayı çevirmek.",
        "yasakli_kelimeler": ["durdurmak", "su", "gaz", "akış", "çevirmek"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Gider Açmak",
        "aciklama": "Tıkanmış lavabo veya tuvalet tahliye borusunu pompa ile açmak.",
        "yasakli_kelimeler": ["tıkanıklık", "lavabo", "pompa", "boru", "su"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Conta Değiştirmek",
        "aciklama": "Su sızdıran musluk veya boru ek yerindeki lastik contayı yenisiyle değiştirmek.",
        "yasakli_kelimeler": ["lastik", "sızdırma", "musluk", "yenilemek", "su"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Su Sızdırmak",
        "aciklama": "Boru çatlağından veya ek yerinden dışarıya su damlaması.",
        "yasakli_kelimeler": ["damlamak", "kaçak", "çatlak", "boru", "ıslak"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Lavabo Monte Etmek",
        "aciklama": "Banyo veya tuvalete el yıkama evyesini sabitlemek.",
        "yasakli_kelimeler": ["evye", "banyo", "sabitlemek", "montaj", "duvar"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Radyatör Takmak",
        "aciklama": "Merkezi veya kombili ısıtma için odaya kalorifer peteği bağlamak.",
        "yasakli_kelimeler": ["kalorifer", "petek", "kombi", "bağlamak", "ısıtma"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Boru Kesmek",
        "aciklama": "Tesisat borusunu makas veya testere ile istenen ölçüde kesmek.",
        "yasakli_kelimeler": ["makas", "testere", "ölçü", "pvc", "plastik"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Kombiyi Çalıştırmak",
        "aciklama": "Evdeki sıcak su ve ısınma ihtiyacı için kombi cihazını açmak.",
        "yasakli_kelimeler": ["ısıtma", "sıcak su", "gaz", "cihaz", "düğme"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Su Basmak",
        "aciklama": "Patlayan boru veya açık musluk yüzünden mekânın suyla dolması.",
        "yasakli_kelimeler": ["patlama", "göl", "zarar", "oda", "taşma"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Klozeti Sabitlemek",
        "aciklama": "Tuvalet taşını zemine cıvatalarla ve silikonla monte etmek.",
        "yasakli_kelimeler": ["tuvalet", "vida", "zemin", "silikon", "montaj"],
        "zorluk": "kolay"
    },

    # Orta (24)
    {
        "kelime": "Teflon Bant Sarmak",
        "aciklama": "Dişli boru bağlantılarında su ve gaz sızdırmazlığı sağlamak için beyaz bant dolamak.",
        "yasakli_kelimeler": ["diş", "sızdırmazlık", "beyaz", "dolamak", "ek yeri"],
        "zorluk": "orta"
    },
    {
        "kelime": "Boru Kaynatmak",
        "aciklama": "PPRC plastik boruları ve ek parçaları kaynak makinesiyle ısıtıp birleştirmek.",
        "yasakli_kelimeler": ["kaynak makinesi", "pprc", "plastik", "ısıtmak", "birleştirmek"],
        "zorluk": "orta"
    },
    {
        "kelime": "Petek Havası Almak",
        "aciklama": "Isınmayan kalorifer radyatörünün pürjör tapasını açıp biriken havayı boşaltmak.",
        "yasakli_kelimeler": ["pürjör", "hava", "radyatör", "ısınmama", "tapa"],
        "zorluk": "orta"
    },
    {
        "kelime": "Sifon Çekmek",
        "aciklama": "Rezervuardaki birikmiş suyu klozete hızlıca boşaltarak temizlik sağlamak.",
        "yasakli_kelimeler": ["rezervuar", "su", "boşaltmak", "klozet", "basmak"],
        "zorluk": "orta"
    },
    {
        "kelime": "Koku Giderici Takmak",
        "aciklama": "Gider borularından içeriye kötü lağım kokusu gelmesini engelleyen çekvalf koymak.",
        "yasakli_kelimeler": ["lağım", "çekvalf", "kötü koku", "gider", "banyo"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kanal Açma Teli Sürmek",
        "aciklama": "Derin gider borularındaki sert tıkanıklıkları spiral çelik telle açmak.",
        "yasakli_kelimeler": ["spiral", "tel", "tıkanıklık", "derin", "itmek"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kombiye Su Basmak",
        "aciklama": "Düşen kalorifer tesisatı su basıncını vanayı açarak 1.5 bar seviyesine getirmek.",
        "yasakli_kelimeler": ["bar", "manometre", "doldurma vanası", "basınç", "su"],
        "zorluk": "orta"
    },
    {
        "kelime": "Tesisatı Yıkamak",
        "aciklama": "Kalorifer petekleri ve borularında biriken çamurlu tortuyu kimyasal makineyle temizlemek.",
        "yasakli_kelimeler": ["makine", "çamur", "tortu", "kimyasal", "temizlik"],
        "zorluk": "orta"
    },
    {
        "kelime": "Pis Su Hattı Çekmek",
        "aciklama": "Bina atık sularını ana kanalizasyona bağlayan geniş çaplı PVC boru döşemek.",
        "yasakli_kelimeler": ["atık su", "kanalizasyon", "pvc", "gider", "çap"],
        "zorluk": "orta"
    },
    {
        "kelime": "Süzgeç Yerleştirmek",
        "aciklama": "Banyo veya balkon zeminindeki suyun tahliyesi için ızgaralı yer süzgeci takmak.",
        "yasakli_kelimeler": ["ızgara", "zemin", "banyo", "balkon", "tahliye"],
        "zorluk": "orta"
    },
    {
        "kelime": "Boru Bükmek",
        "aciklama": "Bakır veya kompozit boruları kırmadan dirsek formu vermek için bükme aleti kullanmak.",
        "yasakli_kelimeler": ["bükme", "bakır", "kıvırmak", "dirsek", "form"],
        "zorluk": "orta"
    },
    {
        "kelime": "Eğimi Ayarlamak",
        "aciklama": "Gider borularında suyun birikmeden akması için doğru meyili vermek.",
        "yasakli_kelimeler": ["meyil", "akış", "drenaj", "su terazisi", "açı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Keten Sarmak",
        "aciklama": "Demir ve galvaniz boru dişlerine sızdırmazlık sağlamak için keten lifi dolamak.",
        "yasakli_kelimeler": ["lif", "galvaniz", "diş", "macun", "sızdırmazlık"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kelepçeyle Sabitlemek",
        "aciklama": "Boruların sarkmasını veya oynamasını engellemek için duvara kelepçeyle vidalamak.",
        "yasakli_kelimeler": ["kelepçe", "duvar", "vida", "sarkma", "tutucu"],
        "zorluk": "orta"
    },
    {
        "kelime": "Termostatik Vana Takmak",
        "aciklama": "Oda sıcaklığına göre kalorifer peteğine giren su debisini otomatik ayarlayan vana takmak.",
        "yasakli_kelimeler": ["sıcaklık", "oda", "ayar", "otomatik", "tasarruf"],
        "zorluk": "orta"
    },
    {
        "kelime": "Koku Kapanı Takmak",
        "aciklama": "Lavabo altına su tutarak kokunun yükselmesini engelleyen S şekilli sifon bağlamak.",
        "yasakli_kelimeler": ["sifon", "koku", "lavabo altı", "su haznesi", "engel"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kollektör Dağıtımı Yapmak",
        "aciklama": "Yerden ısıtma veya radyatör hatlarını tek merkezden vanalarla odalara paylaştırmak.",
        "yasakli_kelimeler": ["merkez", "yerden ısıtma", "dağıtım", "paylaşım", "grup"],
        "zorluk": "orta"
    },
    {
        "kelime": "Pislik Tutucu Temizlemek",
        "aciklama": "Tesisat filtresinde biriken tortu ve kum taneciklerini söküp yıkamak.",
        "yasakli_kelimeler": ["filtre", "tortu", "kum", "süzgeç", "temizlemek"],
        "zorluk": "orta"
    },
    {
        "kelime": "Su Sayacı Bağlamak",
        "aciklama": "Bina veya daire girişine tüketilen şebeke suyu miktarını ölçen saati monte etmek.",
        "yasakli_kelimeler": ["saat", "şebeke", "tüketim", "fatura", "ölçüm"],
        "zorluk": "orta"
    },
    {
        "kelime": "Manometreden Okumak",
        "aciklama": "Tesisat içerisindeki su veya gaz basınç göstergesinin değerini kontrol etmek.",
        "yasakli_kelimeler": ["basınç", "gösterge", "bar", "kontrol", "ibresi"],
        "zorluk": "orta"
    },
    {
        "kelime": "Doğalgaz Fleksi Takmak",
        "aciklama": "Ocak veya kombi girişine esnek paslanmaz çelik spiral gaz hortumu bağlamak.",
        "yasakli_kelimeler": ["fleks", "hortum", "çelik", "doğalgaz", "ocak"],
        "zorluk": "orta"
    },
    {
        "kelime": "Hattı Körlemek",
        "aciklama": "Kullanılmayan boru ucunu kör tapa vidalayarak kapatıp sızdırmaz hale getirmek.",
        "yasakli_kelimeler": ["kör tapa", "kapatmak", "uç", "iptal", "sızdırmaz"],
        "zorluk": "orta"
    },
    {
        "kelime": "Emniyet Ventili Takmak",
        "aciklama": "Kazanda veya su ısıtıcısında aşırı basınç yükseldiğinde suyu tahliye eden valf eklemek.",
        "yasakli_kelimeler": ["aşırı basınç", "valf", "kazan", "tahliye", "güvenlik"],
        "zorluk": "orta"
    },
    {
        "kelime": "Gömme Rezervuar Kurmak",
        "aciklama": "Duvar içine gizlenen asma klozet su haznesinin montajını ve bağlantılarını yapmak.",
        "yasakli_kelimeler": ["duvar içi", "asma klozet", "hazne", "gizli", "montaj"],
        "zorluk": "orta"
    },

    # Zor (14)
    {
        "kelime": "Basınç Testi Yapmak",
        "aciklama": "Yeni döşenen boru hattına test pompasıyla yüksek basınçlı su basıp sızıntı kontrolü yapmak.",
        "yasakli_kelimeler": ["test pompası", "bar", "sızıntı", "denetim", "manometre"],
        "zorluk": "zor"
    },
    {
        "kelime": "Termal Kamerayla Kaçak Aramak",
        "aciklama": "Duvar ve zemin altındaki gizli su borusu patlaklarını ısı farkı görüntüleme cihazıyla bulmak.",
        "yasakli_kelimeler": ["ısı farkı", "görüntüleme", "duvar altı", "gizli", "patlak"],
        "zorluk": "zor"
    },
    {
        "kelime": "Akustik Dinleme Yapmak",
        "aciklama": "Zemin altındaki temiz su sızıntılarını hassas mikrofonlu dinleme cihazıyla tespit etmek.",
        "yasakli_kelimeler": ["kulaklık", "dinleme", "mikrofon", "tespit", "zemin"],
        "zorluk": "zor"
    },
    {
        "kelime": "Hidrofor Devreye Almak",
        "aciklama": "Şebeke suyunun yetersiz kaldığı yüksek binalarda basınçlı su sağlayan pompa sistemini kurmak.",
        "yasakli_kelimeler": ["pompa", "basınç", "yüksek kat", "tank", "otomasyon"],
        "zorluk": "zor"
    },
    {
        "kelime": "Basınç Düşürücü Ayarlamak",
        "aciklama": "Ana şebekeden gelen yüksek su basıncını tesisata zarar vermeyecek seviyeye regüle etmek.",
        "yasakli_kelimeler": ["regülatör", "şebeke", "zarar", "düşürmek", "vana"],
        "zorluk": "zor"
    },
    {
        "kelime": "Sirkülasyon Pompası Bağlamak",
        "aciklama": "Kapalı devre ısıtma sistemlerinde sıcak suyun tesisatta sürekli dolaşımını sağlayan motoru takmak.",
        "yasakli_kelimeler": ["dolaşım", "motor", "kapalı devre", "sıcak su", "devirdaim"],
        "zorluk": "zor"
    },
    {
        "kelime": "Genleşme Tankını Şarj Etmek",
        "aciklama": "Isınan suyun genleşme hacmini dengeleyen membranın arkasındaki azot/hava basıncını basmak.",
        "yasakli_kelimeler": ["membran", "azot", "hava", "denge", "basınç"],
        "zorluk": "zor"
    },
    {
        "kelime": "Geri Akış Önleyici Takmak",
        "aciklama": "Kirli suyun şebekenin temiz su hattına geri emilmesini engelleyen güvenlik armatürünü kurmak.",
        "yasakli_kelimeler": ["kontaminasyon", "geri emilme", "şebeke", "temiz su", "güvenlik"],
        "zorluk": "zor"
    },
    {
        "kelime": "Yerden Isıtma Borusu Döşemek",
        "aciklama": "Zemindeki modülasyon panellerine spiral şekilde PEX oksijen bariyerli boru sermek.",
        "yasakli_kelimeler": ["strafor", "pex", "oksijen bariyeri", "spiral", "şap altı"],
        "zorluk": "zor"
    },
    {
        "kelime": "Boru İçi Kamera Göndermek",
        "aciklama": "Kanalizasyon ve ana gider hatlarındaki kırık ve tıkanıklıkları endoskopik robot kamerayla incelemek.",
        "yasakli_kelimeler": ["endoskop", "kanal", "robot", "ekran", "kırık"],
        "zorluk": "zor"
    },
    {
        "kelime": "Oksijen Kaynağı Yapmak",
        "aciklama": "Klima ve soğutma tesisatındaki kalın bakır boru ek yerlerini şaloma ile yüksek ısıda kaynatmak.",
        "yasakli_kelimeler": ["şaloma", "bakır", "gümüş kaynak", "tüp", "soğutma"],
        "zorluk": "zor"
    },
    {
        "kelime": "Koç Vuruşunu Sönümlemek",
        "aciklama": "Vanaların ani kapanmasıyla borularda oluşan şok basınç dalgasını darbe sönümleyiciyle engellemek.",
        "yasakli_kelimeler": ["şok dalgası", "su darbesi", "sönümleyici", "ani kapanma", "hasar"],
        "zorluk": "zor"
    },
    {
        "kelime": "Drenaj Pompası Kurmak",
        "aciklama": "Bodrum katlarda kanalizasyon seviyesinin altında kalan atık suları yukarı basan dalgıç motor kurmak.",
        "yasakli_kelimeler": ["dalgıç", "bodrum", "seviye altı", "kuyu", "atık"],
        "zorluk": "zor"
    },
    {
        "kelime": "Boru Hattını İzolasyonla Sarmak",
        "aciklama": "Dış ortamdaki su borularının donmasını ve ısı kaybını önlemek için kauçuk izolasyon kılıfı geçirmek.",
        "yasakli_kelimeler": ["kauçuk", "donma", "kılıf", "ısı kaybı", "kaplama"],
        "zorluk": "zor"
    }
]

if __name__ == "__main__":
    add_and_save_verbs("termodinamik", termodinamik_verbs)
    add_and_save_verbs("tesisat", tesisat_verbs)
