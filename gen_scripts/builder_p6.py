import os, sys, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gen_scripts.card_utils import add_and_save_verbs

# 11. evyasam
evyasam_verbs = [
    # Kolay (12)
    {"kelime": "evi süpürmek", "yasakli_kelimeler": ["elektrikli süpürge", "toz", "yer", "halı", "temizlik"], "zorluk": "kolay", "aciklama": "Yerdeki toz ve kırıntıları süpürge ile çekmek."},
    {"kelime": "bulaşık yıkamak", "yasakli_kelimeler": ["tabak", "sünger", "deterjan", "köpük", "lavabo"], "zorluk": "kolay", "aciklama": "Yemek sonrası kirli tabak ve bardakları temizlemek."},
    {"kelime": "çamaşır asmak", "yasakli_kelimeler": ["ip", "mandal", "kurutmak", "ıslak", "balkon"], "zorluk": "kolay", "aciklama": "Yıkanan ıslak giysileri kuruması için ipe mandallamak."},
    {"kelime": "ütü yapmak", "yasakli_kelimeler": ["buhar", "kırışık", "gömlek", "sıcak", "ütü masası"], "zorluk": "kolay", "aciklama": "Kırışmış kıyafetleri sıcak tabanla düzeltmek."},
    {"kelime": "toz almak", "yasakli_kelimeler": ["bez", "mobilya", "sehpa", "silmek", "kir"], "zorluk": "kolay", "aciklama": "Mobilya yüzeylerindeki toz tabakasını bezle silmek."},
    {"kelime": "yemek pişirmek", "yasakli_kelimeler": ["tencere", "ocak", "tava", "lezzet", "mutfak"], "zorluk": "kolay", "aciklama": "Malzemeleri ateşte pişirerek sıcak yemek hazırlamak."},
    {"kelime": "yatağı toplamak", "yasakli_kelimeler": ["çarşaf", "yorgan", "yastık", "düzeltmek", "sabah"], "zorluk": "kolay", "aciklama": "Sabah kalkınca yatak ve örtüyü düzenlemek."},
    {"kelime": "perdeleri açmak", "yasakli_kelimeler": ["güneş", "ışık", "pencere", "çekmek", "tül"], "zorluk": "kolay", "aciklama": "Odaya gün ışığı girmesi için tül ve perdeleri kenara çekmek."},
    {"kelime": "çöpü dökmek", "yasakli_kelimeler": ["poşet", "atık", "konteyner", "kapı", "dışarı"], "zorluk": "kolay", "aciklama": "Dolan çöp poşetini dışarıdaki konteynere atmak."},
    {"kelime": "kapıyı kilitlemek", "yasakli_kelimeler": ["anahtar", "kilit", "güvenlik", "ev", "çıkmak"], "zorluk": "kolay", "aciklama": "Dışarı çıkarken evin kapısını anahtarla emniyete almak."},
    {"kelime": "evi havalandırmak", "yasakli_kelimeler": ["pencere", "temiz hava", "açmak", "oda", "oksijen"], "zorluk": "kolay", "aciklama": "Odadaki havayı tazelemek için camları açmak."},
    {"kelime": "çiçek sulamak", "yasakli_kelimeler": ["saksı", "su", "ibrik", "yaprak", "büyümek"], "zorluk": "kolay", "aciklama": "Evdeki saksı bitkilerine düzenli su vermek."},

    # Orta (24)
    {"kelime": "fırın temizlemek", "yasakli_kelimeler": ["yağ", "yanık", "tel", "sprey", "ocak"], "zorluk": "orta", "aciklama": "Fırın içindeki yanmış yağ lekelerini kimyasallarla ovalamak."},
    {"kelime": "dolap düzenlemek", "yasakli_kelimeler": ["gardırop", "askı", "kıyafet", "katlamak", "çekmece"], "zorluk": "orta", "aciklama": "Kıyafetleri mevsimine göre katlayıp askılara yerleştirmek."},
    {"kelime": "buzdolabının buzunu çözmek", "yasakli_kelimeler": ["dondurucu", "karlık", "fişi çekmek", "eritmek", "su"], "zorluk": "orta", "aciklama": "Dondurucuda biriken buz katmanını eritip temizlemek."},
    {"kelime": "halı yıkatmak", "yasakli_kelimeler": ["servis", "fabrika", "temizlik", "leke", "teslim"], "zorluk": "orta", "aciklama": "Kirlenen halıları profesyonel yıkama servisine göndermek."},
    {"kelime": "cam silmek", "yasakli_kelimeler": ["çekpas", "camsil", "pencere", "parlatmak", "lekesiz"], "zorluk": "orta", "aciklama": "Pencerelerin camlarını deterjan ve çekpasla pırıl pırıl yapmak."},
    {"kelime": "tadilat yaptırmak", "yasakli_kelimeler": ["usta", "tamir", "boya", "yenileme", "masraf"], "zorluk": "orta", "aciklama": "Evdeki eski veya arızalı bölümleri usta çağırarak yeniletmek."},
    {"kelime": "musluk tamir etmek", "yasakli_kelimeler": ["damlatmak", "conta", "ingiliz anahtarı", "lavabo", "su sızıntısı"], "zorluk": "orta", "aciklama": "Damlayan musluğun contasını söküp yenilemek."},
    {"kelime": "duvar boyamak", "yasakli_kelimeler": ["rulo", "fırça", "astar", "renk", "badana"], "zorluk": "orta", "aciklama": "Odanın duvarlarına yeni kat astar ve boya sürmek."},
    {"kelime": "nevresim değiştirmek", "yasakli_kelimeler": ["çarşaf", "yastık kılıfı", "yorgan", "temiz", "yıkamak"], "zorluk": "orta", "aciklama": "Yataktaki kirlenen çarşaf ve kılıfları temizleriyle değiştirmek."},
    {"kelime": "kireç çözücü kullanmak", "yasakli_kelimeler": ["kettle", "çaydanlık", "musluk", "asit", "beyaz tortu"], "zorluk": "orta", "aciklama": "Su ısıtıcısı ve bataryalarda biriken kireç tortusunu gidermek."},
    {"kelime": "mobilya montajı yapmak", "yasakli_kelimeler": ["alyan", "vida", "kurulum", "şema", "tornavida"], "zorluk": "orta", "aciklama": "Demonte gelen masa veya dolabı parçalarını vidalayarak kurmak."},
    {"kelime": "derin dondurucuya stoklamak", "yasakli_kelimeler": ["kışlık", "buzluk", "poşet", "saklama kabı", "sebze"], "zorluk": "orta", "aciklama": "Gıdaları uzun süre taze tutmak için dondurucuya yerleştirmek."},
    {"kelime": "kiler düzenlemek", "yasakli_kelimeler": ["erzak", "kavanoz", "raf", "bakliyat", "tarih"], "zorluk": "orta", "aciklama": "Erzak ve kuru gıdaları son kullanma tarihine göre raflara dizmek."},
    {"kelime": "konserve yapmak", "yasakli_kelimeler": ["domates", "kapak", "kavanoz", "kaynatmak", "vakum"], "zorluk": "orta", "aciklama": "Mevsimlik sebzeleri kavanozda kaynatarak kışa saklamak."},
    {"kelime": "derz aralarını temizlemek", "yasakli_kelimeler": ["fayans", "banyo", "küf", "fırça", "beyazlatmak"], "zorluk": "orta", "aciklama": "Fayans boşluklarındaki kararlaşmış harçları kimyasalla ovmak."},
    {"kelime": "balkon yıkamak", "yasakli_kelimeler": ["hortum", "fırça", "gider", "köpük", "su"], "zorluk": "orta", "aciklama": "Açık balkon zeminini köpüklü su ve fırçayla yıkamak."},
    {"kelime": "gardırop detoksu yapmak", "yasakli_kelimeler": ["giymemek", "bağışlamak", "ayırmak", "fazlalık", "kıyafet"], "zorluk": "orta", "aciklama": "Uzun süredir giyilmeyen kıyafetleri ayırıp başkalarına vermek."},
    {"kelime": "ampul değiştirmek", "yasakli_kelimeler": ["patlamak", "duy", "avize", "led", "ışık"], "zorluk": "orta", "aciklama": "Ömrü biten aydınlatma lambasını çıkarıp yenisini takmak."},
    {"kelime": "bulaşık makinesini boşaltmak", "yasakli_kelimeler": ["temiz tabak", "bardak", "yerleştirmek", "dolap", "sepet"], "zorluk": "orta", "aciklama": "Yıkanmış kuru kapları makineden çıkarıp dolaplara dizmek."},
    {"kelime": "kombi basıncını ayarlamak", "yasakli_kelimeler": ["bar", "vana", "su basmak", "petek", "ısıtma"], "zorluk": "orta", "aciklama": "Isıtma kombisinin bar göstergesini 1.5 seviyesine getirmek."},
    {"kelime": "ev bütçesi yapmak", "yasakli_kelimeler": ["gelir", "gider", "fatura", "hesap", "kira"], "zorluk": "orta", "aciklama": "Aylık gelir ve gider dengesini tablo halinde planlamak."},
    {"kelime": "bavul hazırlamak", "yasakli_kelimeler": ["seyahat", "valiz", "kıyafet", "katlamak", "yolculuk"], "zorluk": "orta", "aciklama": "Yolculuk öncesi gerekli eşyaları valize düzgünce yerleştirmek."},
    {"kelime": "ayakkabı boyamak", "yasakli_kelimeler": ["cila", "sünger", "deri", "parlatmak", "fırça"], "zorluk": "orta", "aciklama": "Deri ayakkabıların yüzeyini cila ve fırça ile tazelemek."},
    {"kelime": "sigorta attığında kaldırmak", "yasakli_kelimeler": ["şalter", "pano", "karanlık", "elektrik", "düğme"], "zorluk": "orta", "aciklama": "Aşırı yükten atan elektrik anahtarını panodan tekrar açmak."},

    # Zor (14)
    {"kelime": "lavabo sifonunu sökmek", "yasakli_kelimeler": ["tıkanıklık", "pimaş", "kıl", "borudan su akması", "kova"], "zorluk": "zor", "aciklama": "Gider borusundaki tıkanmayı gidermek için alt sifon kavisini açıp temizlemek."},
    {"kelime": "radyatör havasını almak", "yasakli_kelimeler": ["purjör anahtarı", "petek", "ısınmama", "ses yapma", "su akıtmak"], "zorluk": "zor", "aciklama": "Peteklerin üst kısmında biriken havayı purjör vidasından boşaltmak."},
    {"kelime": "silikon çekmek", "yasakli_kelimeler": ["kartuş tabancası", "su sızdırmazlık", "duşakabin", "mastik", "düzeltme"], "zorluk": "zor", "aciklama": "Tezgah veya duş teknesi kenarlarına su sızmasını önleyen mastik uygulamak."},
    {"kelime": "kapı menteşesini yağlamak", "yasakli_kelimeler": ["gıcırtı", "wd-40", "yağ", "sürtünme", "pim"], "zorluk": "zor", "aciklama": "Açılıp kapanırken öten kapı demirlerine kayganlaştırıcı sıkmak."},
    {"kelime": "davlumbaz filtresini yağdan arındırmak", "yasakli_kelimeler": ["alüminyum ızgara", "bulaşık tableti", "kaynar su", "aspiratör", "yağ çözücü"], "zorluk": "zor", "aciklama": "Aspiratörün gözenekli metal filtresindeki yapışkan katmanı sökmek."},
    {"kelime": "klozet şamandırasını ayarlamak", "yasakli_kelimeler": ["rezervuar", "su taşması", "iç takım", "flotör", "kesme valfi"], "zorluk": "zor", "aciklama": "Rezervuarın içine su dolumunu kesen mekanizmanın yüksekliğini ayarlamak."},
    {"kelime": "duvar dübeli çakmak", "yasakli_kelimeler": ["matkap", "delik", "plastik", "vida", "tablo asmak"], "zorluk": "zor", "aciklama": "Matkapla delinen duvara vidanın tutunması için plastik kovan yerleştirmek."},
    {"kelime": "parke cilalamak", "yasakli_kelimeler": ["sistre", "ahşap zemin", "parlatıcı", "koruyucu vernik", "zımpara"], "zorluk": "zor", "aciklama": "Ahşap döşemenin aşınmış yüzeyini zımparalayıp koruyucu vernik sürmek."},
    {"kelime": "rutubet yalıtımı yapmak", "yasakli_kelimeler": ["nem", "küf önleyici boya", "strafor", "ısı köprüsü", "terleme"], "zorluk": "zor", "aciklama": "Duvarda küf ve terleme oluşumunu engellemek için yalıtım malzemesi kaplamak."},
    {"kelime": "çamaşır makinesi tahliye filtresini temizlemek", "yasakli_kelimeler": ["alt kapak", "bozuk para", "su tahliyesi", "pompa tıkanıklığı", "boşaltma"], "zorluk": "zor", "aciklama": "Makinenin altındaki pompa kapağını açıp kaçan yabancı cisimleri temizlemek."},
    {"kelime": "fayans kırmak", "yasakli_kelimeler": ["murç", "çekiç", "banyo yenileme", "seramik", "harç"], "zorluk": "zor", "aciklama": "Tadilat öncesi eski seramik kaplamaları murç ve çekiçle duvardan sökmek."},
    {"kelime": "panjur kordonunu değiştirmek", "yasakli_kelimeler": ["şerit ip", "makara", "kaset", "kopma", "pencere"], "zorluk": "zor", "aciklama": "Kopan veya aşınan panjur çekme ipini kaset mekanizmasından yenilemek."},
    {"kelime": "doğalgaz kaçağı kontrolü yapmak", "yasakli_kelimeler": ["köpük testi", "dedektör", "boru ek yeri", "vana", "gaz kokusu"], "zorluk": "zor", "aciklama": "Boru bağlantılarına sabun köpüğü sürerek veya cihazla sızıntı aramak."},
    {"kelime": "gömme rezervuar iç takımını yenilemek", "yasakli_kelimeler": ["asma klozet", "kumanda paneli", "boşaltma contası", "doldurma grubu", "arıza"], "zorluk": "zor", "aciklama": "Duvar içine gömülü tuvalet sifonunun arızalı conta ve contalarını değiştirmek."}
]

# 12. ezoterizm
ezoterizm_verbs = [
    # Kolay (12)
    {"kelime": "meditasyon yapmak", "yasakli_kelimeler": ["odaklanmak", "zihin", "nefes", "huzur", "göz kapatmak"], "zorluk": "kolay", "aciklama": "Zihni sakinleştirip içsel farkındalığa odaklanmak."},
    {"kelime": "fal bakmak", "yasakli_kelimeler": ["kahve", "gelecek", "fincan", "tahmin", "kart"], "zorluk": "kolay", "aciklama": "Çeşitli işaret ve sembollerden geleceğe dair yorumlar yapmak."},
    {"kelime": "tütsü yakmak", "yasakli_kelimeler": ["koku", "duman", "adaçayı", "arındırma", "çubuk"], "zorluk": "kolay", "aciklama": "Aromatik bitki ve çubukları yakarak ortama hoş koku ve duman yaymak."},
    {"kelime": "rüya tabir etmek", "yasakli_kelimeler": ["yorum", "uyku", "sembol", "görmek", "anlam"], "zorluk": "kolay", "aciklama": "Uykuda görülen simgelerin gizli manalarını yorumlamak."},
    {"kelime": "mum yakmak", "yasakli_kelimeler": ["fitil", "ışık", "ateş", "ritüel", "erimek"], "zorluk": "kolay", "aciklama": "Ritüel veya odaklanma öncesi mumu ateşlemek."},
    {"kelime": "tarot kartı çekmek", "yasakli_kelimeler": ["deste", "büyücü", "arkana", "fal", "seçmek"], "zorluk": "kolay", "aciklama": "Desteden soruya yönelik rastgele kart seçmek."},
    {"kelime": "doğal taş taşımak", "yasakli_kelimeler": ["kristal", "kuvars", "enerji", "ametist", "bileklik"], "zorluk": "kolay", "aciklama": "Enerji verdiğine inanılan şifalı mineralleri üzerinde bulundurmak."},
    {"kelime": "dua etmek", "yasakli_kelimeler": ["niyet", "tanrı", "istemek", "yakarmak", "inanç"], "zorluk": "kolay", "aciklama": "Yüce bir güce içtenlikle niyet ve dilek iletmek."},
    {"kelime": "enerji hissetmek", "yasakli_kelimeler": ["aura", "titreşim", "beden", "akış", "sıcaklık"], "zorluk": "kolay", "aciklama": "Ortamın veya bir kişinin yaydığı görünmez hissi algılamak."},
    {"kelime": "nazar boncuğu takmak", "yasakli_kelimeler": ["mavi", "göz", "kem göz", "koruma", "kötülük"], "zorluk": "kolay", "aciklama": "Kötü bakışlardan korunmak için mavi göz figürü takmak."},
    {"kelime": "sessizliğe çekilmek", "yasakli_kelimeler": ["inziva", "yalnız", "sakin", "konuşmamak", "iç dünya"], "zorluk": "kolay", "aciklama": "Gürültüden uzaklaşıp kendi iç alemine yönelmek."},
    {"kelime": "niyet tutmak", "yasakli_kelimeler": ["dilek", "kalp", "istemek", "hedef", "odak"], "zorluk": "kolay", "aciklama": "Bir eylem veya ritüel öncesi zihinde hedef dileği belirlemek."},

    # Orta (24)
    {"kelime": "çakra açmak", "yasakli_kelimeler": ["enerji merkezi", "tıkanıklık", "omurga", "kök", "taç"], "zorluk": "orta", "aciklama": "Bedendeki yedi enerji merkezinin akışını dengelemek."},
    {"kelime": "aura temizliği yapmak", "yasakli_kelimeler": ["enerji alanı", "arındırma", "tuz", "adaçayı", "biyoenerji"], "zorluk": "orta", "aciklama": "Bedeni çevreleyen elektromanyetik enerji alanını negatiflikten arındırmak."},
    {"kelime": "astral seyahate çıkmak", "yasakli_kelimeler": ["beden dışı", "ruh", "fiziksel beden", "bilinç", "projeksiyon"], "zorluk": "orta", "aciklama": "Bilinçli olarak ruhsal bedeni fiziksel bedenden ayırıp seyahat etmek."},
    {"kelime": "ritüel düzenlemek", "yasakli_kelimeler": ["tören", "sembol", "element", "sunu", "kutsal"], "zorluk": "orta", "aciklama": "Belirli kurallar ve sembollerle mistik bir merasim icra etmek."},
    {"kelime": "reiki uygulamak", "yasakli_kelimeler": ["el verme", "evrensel yaşam enerjisi", "şifa", "japon", "avuç içi"], "zorluk": "orta", "aciklama": "Elleri bedenin üzerine koyarak şifa enerjisi aktarmak."},
    {"kelime": "sembolik dili çözmek", "yasakli_kelimeler": ["şifre", "okült", "geometri", "ezoterik", "anlam"], "zorluk": "orta", "aciklama": "Mistik öğretilerdeki gizli alegorik işaretleri deşifre etmek."},
    {"kelime": "inzivaya çekilmek", "yasakli_kelimeler": ["halvet", "toplumdan uzak", "manastır", "ibadet", "içsel yolculuk"], "zorluk": "orta", "aciklama": "Manevi olgunlaşma için dünyevi hayattan tamamen soyutlanmak."},
    {"kelime": "sarkaç kullanmak", "yasakli_kelimeler": ["radyestezi", "pandül", "evet hayır", "frekans", "salınım"], "zorluk": "orta", "aciklama": "Zincir ucundaki ağırlığın dairesel hareketleriyle enerji tespiti yapmak."},
    {"kelime": "nefes tekniği uygulamak", "yasakli_kelimeler": ["pranayama", "diyafram", "dönüşümlü", "holotropik", "ritim"], "zorluk": "orta", "aciklama": "Farkındalığı ve bilinci yükseltmek için özel nefes paternleri uygulamak."},
    {"kelime": "şamanik davul çalmak", "yasakli_kelimeler": ["trans", "ritim", "kam", "alt dünya", "ruhlar"], "zorluk": "orta", "aciklama": "Monoton ritimlerle trans haline geçip ruhsal yolculuk yapmak."},
    {"kelime": "doğum haritası yorumlamak", "yasakli_kelimeler": ["natal harita", "gezegen", "evler", "burç", "gökyüzü"], "zorluk": "orta", "aciklama": "Doğum anındaki gök cisimlerinin konumlarından karakter ve kadersel analiz yapmak."},
    {"kelime": "numerolojik analiz yapmak", "yasakli_kelimeler": ["sayı", "harf değeri", "ebced", "hayat yolu", "pisagor"], "zorluk": "orta", "aciklama": "İsim ve doğum tarihindeki sayıların titreşimini hesaplamak."},
    {"kelime": "adaçayı ile tütsülemek", "yasakli_kelimeler": ["mekan temizliği", "negatif enerji", "yaprak", "yakmak", "duman"], "zorluk": "orta", "aciklama": "Mekandaki ağırlığı gidermek için kuru adaçayı demetini yakıp gezdirmek."},
    {"kelime": "kristalleri arındırmak", "yasakli_kelimeler": ["dolunay", "topraklama", "tuzlu su", "kuvars", "temizleme"], "zorluk": "orta", "aciklama": "Doğal taşların biriktirdiği enerjiyi ay ışığı veya toprakla nötrlemek."},
    {"kelime": "üçüncü gözü aktive etmek", "yasakli_kelimeler": ["ajna", "alın çakrası", "sezgi", "durugörü", "epikriz"], "zorluk": "orta", "aciklama": "İki kaş arasındaki sezgisel vizyon merkezini canlandırmak."},
    {"kelime": "lucid rüya görmek", "yasakli_kelimeler": ["bilinçli rüya", "kontrol etmek", "farkında olma", "uyku", "yönetmek"], "zorluk": "orta", "aciklama": "Rüya gördüğünün bilincinde olup rüya akışını yönlendirmek."},
    {"kelime": "karmik borç ödemek", "yasakli_kelimeler": ["karma", "geçmiş yaşam", "sebep sonuç", "ders", "döngü"], "zorluk": "orta", "aciklama": "Geçmiş eylemlerin manevi yükünü bu hayatta ders alarak dengelemek."},
    {"kelime": "mandala çizmek", "yasakli_kelimeler": ["dairesel", "geometri", "boyama", "meditasyon", "merkez"], "zorluk": "orta", "aciklama": "Evrenin düzenini yansıtan merkezcil geometrik desenler üretmek."},
    {"kelime": "afirmasyon tekrarlamak", "yasakli_kelimeler": ["olumlama", "cümle", "bilinçaltı", "inanç", "yeniden programlama"], "zorluk": "orta", "aciklama": "Bilinçaltını dönüştürmek için pozitif niyet cümlelerini düzenli söylemek."},
    {"kelime": "elementleri dengelemek", "yasakli_kelimeler": ["ateş", "su", "hava", "toprak", "dört element"], "zorluk": "orta", "aciklama": "Bünyedeki ve mekandaki dört temel unsurun uyumunu kurmak."},
    {"kelime": "durugörü deneyimlemek", "yasakli_kelimeler": ["clairvoyance", "uzaktan görme", "vizyon", "fizik ötesi", "algı"], "zorluk": "orta", "aciklama": "Fiziksel gözün görmediği uzak veya gizli olayları zihinde görmek."},
    {"kelime": "ses frekansıyla şifalanmak", "yasakli_kelimeler": ["tibetan bowl", "solfeggio", "432 hz", "çan", "titreşim"], "zorluk": "orta", "aciklama": "Tibet çanakları ve özel ses frekanslarıyla bedensel uyumu yakalamak."},
    {"kelime": "geçmiş yaşam regresyonu yapmak", "yasakli_kelimeler": ["hipnoz", "reenkarnasyon", "önceki hayat", "travma", "hatırlama"], "zorluk": "orta", "aciklama": "Hipnotik transla ruhun önceki reenkarne anılarına ulaşmak."},
    {"kelime": "gizli cemiyete katılmak", "yasakli_kelimeler": ["inisiyasyon", "loca", "kardeşlik", "okült örgüt", "sır"], "zorluk": "orta", "aciklama": "Ezoterik bilgi aktaran kapalı bir cemiyetin üyesi olmak."},

    # Zor (14)
    {"kelime": "inisiyasyon töreninden geçmek", "yasakli_kelimeler": ["erginlenme", "sırra erme", "kabul ritüeli", "üstat", "yeniden doğuş"], "zorluk": "zor", "aciklama": "Ezoterik bir öğretiye kabul edilmek için yapılan sınav ve töreni aşmak."},
    {"kelime": "akashik kayıtlara erişmek", "yasakli_kelimeler": ["kozmik hafıza", "eterik", "tüm bilgi", "evrensel kütüphane", "ruh"], "zorluk": "zor", "aciklama": "Evrende var olmuş tüm düşünce ve olayların kaydedildiği kozmik arşive bağlanmak."},
    {"kelime": "simyasal dönüşüm gerçekleştirmek", "yasakli_kelimeler": ["magnum opus", "felsefe taşı", "kurşunu altına çevirme", "ruhsal arınma", "simya"], "zorluk": "zor", "aciklama": "Maddi ve ruhsal ham maddeyi en yüce saf haline dönüştürmek."},
    {"kelime": "kabala hayat ağacını çalışmak", "yasakli_kelimeler": ["sefirot", "on sefira", "keter", "malkut", "mistik yahudilik"], "zorluk": "zor", "aciklama": "Evrenin ve tanrısal tezahürün on aşamalı sefirot şemasını incelemek."},
    {"kelime": "hermetik prensipleri uygulamak", "yasakli_kelimeler": ["kybalion", "hermes trismegistus", "tekabül", "kutupsallık", "titreşim yasası"], "zorluk": "zor", "aciklama": "'Yukarıda ne varsa aşağıda da o vardır' evrensel yasalarını hayata geçirmek."},
    {"kelime": "teozofik öğretiyi incelemek", "yasakli_kelimeler": ["blavatsky", "kadim bilgelik", "ruhsal hiyerarşi", "mahatma", "ezoterizm"], "zorluk": "zor", "aciklama": "Tüm din ve felsefelerin altındaki ortak ilahi bilgeliği araştırmak."},
    {"kelime": "egregore oluşturmak", "yasakli_kelimeler": ["kolektif düşünce formu", "grup bilinci", "psişik varlık", "ortak odak", "ritüel"], "zorluk": "zor", "aciklama": "Bir grubun ortak odaklanmasıyla psişik bir düşünce formu inşa etmek."},
    {"kelime": "mer-ka-ba alanını aktive etmek", "yasakli_kelimeler": ["ışık bedeni", "kutsal geometri", "yıldız tetrahedron", "dönen enerji", "yükseliş"], "zorluk": "zor", "aciklama": "Zıt yönlere dönen kutsal geometrik ışık beden alanını canlandırmak."},
    {"kelime": "kundalini enerjisini uyandırmak", "yasakli_kelimeler": ["kıvrılmış yılan", "kök çakra", "omurga boyunca yükselme", "shakti", "aydınlanma"], "zorluk": "zor", "aciklama": "Omurga tabanında uyuyan kozmik yaşam enerjisini taç çakraya doğru yükseltmek."},
    {"kelime": "teürji ameliyesi yapmak", "yasakli_kelimeler": ["tanrısal büyü", "ilahi varlıklar", "yamblikhos", "neoplatonizm", "ritüel"], "zorluk": "zor", "aciklama": "İlahi güçlerle ve meleklerle temas kurup birleşmek için kutsal tören icra etmek."},
    {"kelime": "sigil mühürlemek", "yasakli_kelimeler": ["kaos majisi", "niyet sembolü", "şarj etmek", "unutmak", "glif"], "zorluk": "zor", "aciklama": "Niyeti soyut bir grafik glife indirgeyip bilinçaltına gömmek."},
    {"kelime": "gurdjieff dördüncü yolunu yürümek", "yasakli_kelimeler": ["kendini hatırlama", "enneagram", "uyuyan insan", "uyanış", "uşak"], "zorluk": "zor", "aciklama": "Fiziksel, duygusal ve zihinsel merkezleri aynı anda dengeleyerek uyanmak."},
    {"kelime": "gnosis haline ulaşmak", "yasakli_kelimeler": ["doğrudan deneyim", "kurtarıcı bilgi", "gnostisizm", "ilahi kıvılcım", "aydınlanma"], "zorluk": "zor", "aciklama": "Kitabi bilgi yerine tanrısal hakikati doğrudan yaşantılayarak bilme haline varmak."},
    {"kelime": "antropozofik tıp uygulamak", "yasakli_kelimeler": ["rudolf steiner", "eterik beden", "astral beden", "ruhsal bilim", "tedavi"], "zorluk": "zor", "aciklama": "İnsanın dörtlü beden yapısını dikkate alarak ruhsal ve fiziksel tedavi yürütmek."}
]

add_and_save_verbs('evyasam', evyasam_verbs)
add_and_save_verbs('ezoterizm', ezoterizm_verbs)
print('P6 done!')
