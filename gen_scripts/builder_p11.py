import os, sys, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gen_scripts.card_utils import add_and_save_verbs

# 21. heykeltiraslik
heykeltiraslik_verbs = [
    # Kolay (12)
    {"kelime": "heykel yapmak", "yasakli_kelimeler": ["sanatçı", "çamur", "taş", "şekil", "figür"], "zorluk": "kolay", "aciklama": "Üç boyutlu sanat eseri veya figür üretmek."},
    {"kelime": "kil yoğurmak", "yasakli_kelimeler": ["çamur", "el", "yumuşatmak", "su", "şekil vermek"], "zorluk": "kolay", "aciklama": "Kili şekillendirmeden önce elle bastırarak yumuşatmak."},
    {"kelime": "çekiç vurmak", "yasakli_kelimeler": ["keski", "taş", "mermer", "darbe", "alet"], "zorluk": "kolay", "aciklama": "Keskinin arkasına çekiçle vurarak taştan parça koparmak."},
    {"kelime": "mermer yontmak", "yasakli_kelimeler": ["keski", "taş", "heykel", "parça koparma", "şekil"], "zorluk": "kolay", "aciklama": "Mermer bloğu aletlerle yontarak heykeli açığa çıkarmak."},
    {"kelime": "büst tasarlamak", "yasakli_kelimeler": ["baş", "omuz", "yüz", "portre", "heykel"], "zorluk": "kolay", "aciklama": "İnsanın göğüsten yukarısını gösteren heykeli tasarlamak."},
    {"kelime": "çamurdan şekil yapmak", "yasakli_kelimeler": ["seramik", "kil", "el", "oyuncak", "heykelcik"], "zorluk": "kolay", "aciklama": "Yumuşak çamuru parmaklarla biçimlendirmek."},
    {"kelime": "zımparalamak", "yasakli_kelimeler": ["pürüzsüz", "ahşap", "taş", "sürtmek", "düzeltmek"], "zorluk": "kolay", "aciklama": "Heykel yüzeyindeki pürüzleri zımpara kağıdıyla gidermek."},
    {"kelime": "kalıp çıkarmak", "yasakli_kelimeler": ["alçı", "silikon", "dökmek", "çoğaltmak", "model"], "zorluk": "kolay", "aciklama": "Yapılan heykelin kopyasını üretmek için dış kalıbını almak."},
    {"kelime": "alçı dökmek", "yasakli_kelimeler": ["sıvı", "beyaz", "donmak", "kalıp", "toz"], "zorluk": "kolay", "aciklama": "Kalıbın içine suyla karıştırılmış sıvı alçı doldurmak."},
    {"kelime": "sergide göstermek", "yasakli_kelimeler": ["galeri", "müze", "ziyaretçi", "sanat", "sunum"], "zorluk": "kolay", "aciklama": "Tamamlanan heykeli sanat galerisinde izleyicilere sunmak."},
    {"kelime": "boyamak", "yasakli_kelimeler": ["fırça", "renk", "akrilik", "vernik", "yüzey"], "zorluk": "kolay", "aciklama": "Heykelin yüzeyine renkli boyalar uygulamak."},
    {"kelime": "atölyede çalışmak", "yasakli_kelimeler": ["stüdyo", "toz", "önlük", "üretim", "aletler"], "zorluk": "kolay", "aciklama": "Sanat çalışmalarını heykel atölyesinde gerçekleştirmek."},

    # Orta (24)
    {"kelime": "bronz dökmek", "yasakli_kelimeler": ["tunç", "eriyik metal", "dökümhane", "yüksek ısı", "fırın"], "zorluk": "orta", "aciklama": "Eritilmiş bronz alaşımını kalıba akıtarak metal heykel üretmek."},
    {"kelime": "modelaj yapmak", "yasakli_kelimeler": ["kille çalışma", "biçimlendirme", "ekleme tekniği", "ıspatula", "hacim"], "zorluk": "orta", "aciklama": "Yumuşak malzemeyi ekleyip çıkartarak hacimsel form kazandırmak."},
    {"kelime": "iskelet kurmak", "yasakli_kelimeler": ["armatür", "tel", "metal çubuk", "destek", "taşıyıcı"], "zorluk": "orta", "aciklama": "Büyük killi heykellerin çökmemesi için iç kısma tel ve demir iskelet yapmak."},
    {"kelime": "fırınlamak", "yasakli_kelimeler": ["pişirmek", "seramik fırını", "yüksek derece", "terrakotta", "sertleşme"], "zorluk": "orta", "aciklama": "Kilden yapılan heykeli fırında pişirerek taş gibi sertleştirmek."},
    {"kelime": "rölyef işlemek", "yasakli_kelimeler": ["kabartma", "alçak kabartma", "yüksek kabartma", "duvar", "pano"], "zorluk": "orta", "aciklama": "Yassı bir yüzey üzerine çıkıntılı kabartma figürler kazımak."},
    {"kelime": "orantı kurmak", "yasakli_kelimeler": ["proporsiyon", "anatomik oran", "ölçüm", "pergel", "kanon"], "zorluk": "orta", "aciklama": "Figürün uzuvları arasındaki estetik ve anatomik ölçü dengesini sağlamak."},
    {"kelime": "keski kullanmak", "yasakli_kelimeler": ["murç", "çelik alet", "yontma", "taş", "ahşap oyma"], "zorluk": "orta", "aciklama": "Sert malzemeleri oymak için çelik kesici ucu kullanmak."},
    {"kelime": "patina uygulamak", "yasakli_kelimeler": ["oksitlenme", "yeşil renk", "kimyasal", "bronz yüzey", "eskitme"], "zorluk": "orta", "aciklama": "Metal heykele kimyasallarla antik veya yeşilimsi renk tabakası kazandırmak."},
    {"kelime": "ahşap oymak", "yasakli_kelimeler": ["iskarpela", "ağaç", "talaş", "lif", "tokmak"], "zorluk": "orta", "aciklama": "Ağaç kütüğünü iskarpela ve tokmakla yontarak form vermek."},
    {"kelime": "polyester dökmek", "yasakli_kelimeler": ["fiberglas", "reçine", "sertleştirici", "kalıp", "hafif heykel"], "zorluk": "orta", "aciklama": "Sentetik reçine ve fiberglası kalıba dökerek dayanıklı heykel yapmak."},
    {"kelime": "mumdan model hazırlamak", "yasakli_kelimeler": ["vaks", "kayıp mum tekniği", "eritme", "detay", "döküm"], "zorluk": "orta", "aciklama": "Döküm öncesi heykelin birebir formunu balmumundan şekillendirmek."},
    {"kelime": "canlı modele bakarak çalışmak", "yasakli_kelimeler": ["nü", "poz", "anatomi", "gözlem", "atölye"], "zorluk": "orta", "aciklama": "Atölyede poz veren insanın beden hatlarını gözlemleyerek kile aktarmak."},
    {"kelime": "kaide üzerine yerleştirmek", "yasakli_kelimeler": ["baza", "ayaklık", "mermer blok", "montaj", "yükseklik"], "zorluk": "orta", "aciklama": "Heykeli sergilemek için mermer veya ahşap kaidesine sabitlemek."},
    {"kelime": "noktalama aleti kullanmak", "yasakli_kelimeler": ["pantograf", "üç nokta kuralı", "ölçek büyütme", "kopya", "taş aktarma"], "zorluk": "orta", "aciklama": "Küçük alçı modeldeki ölçüleri büyük mermer bloğa birebir aktarmak."},
    {"kelime": "kinesik heykel tasarlamak", "yasakli_kelimeler": ["hareketli", "rüzgar", "motor", "mobil", "calder"], "zorluk": "orta", "aciklama": "Rüzgar veya motorla hareket eden dinamik heykeller üretmek."},
    {"kelime": "ispâtula ile sıyırmak", "yasakli_kelimeler": ["modelaj aleti", "ahşap uç", "çamur alma", "düzeltme", "kil"], "zorluk": "orta", "aciklama": "Heykelin yüzeyindeki fazla çamuru ahşap veya metal aletle sıyırmak."},
    {"kelime": "silikon kalıp almak", "yasakli_kelimeler": ["rTV silikon", "esnek kalıp", "negatif", "detay kopyalama", "ayırma ajanı"], "zorluk": "orta", "aciklama": "En ince detayları dahi kusursuz çıkaran esnek kalıp malzemesi uygulamak."},
    {"kelime": "kaynak yapmak", "yasakli_kelimeler": ["demir heykel", "elektrot", "metal birleştirme", "kıvılcım", "atölye"], "zorluk": "orta", "aciklama": "Metal parçaları yüksek ısıyla eritip birleştirerek konstrüksiyon kurmak."},
    {"kelime": "yüzey dokusu vermek", "yasakli_kelimeler": ["tekstür", "pürüzlü", "çizgili", "mat", "işleme"], "zorluk": "orta", "aciklama": "Malzemenin yüzeyine özel alet darbeleriyle estetik doku kazandırmak."},
    {"kelime": "anıt heykel dikmek", "yasakli_kelimeler": ["meydan", "kamusal alan", "büyük", "kahramanlık", "şehrin simgesi"], "zorluk": "orta", "aciklama": "Şehir meydanına devasa boyutlarda tarihi veya simgesel anıt yerleştirmek."},
    {"kelime": "negatif alan yaratmak", "yasakli_kelimeler": ["boşluk", "doluluk", "kütle", "hava", "modern heykel"], "zorluk": "orta", "aciklama": "Heykelin içindeki veya etrafındaki boşlukları kompozisyona dahil etmek."},
    {"kelime": "kurşun dökmek", "yasakli_kelimeler": ["ağır metal", "düşük erime noktası", "kalıp", "döküm", "mat gri"], "zorluk": "orta", "aciklama": "Düşük sıcaklıkta eriyen kurşunu kalıba doldurarak parça üretmek."},
    {"kelime": "cilalama keçesi kullanmak", "yasakli_kelimeler": ["parlatma", "pasta", "mermer parlaklığı", "spiral", "ışıldama"], "zorluk": "orta", "aciklama": "Mermer veya metal yüzeyi keçe ve parlatıcı pastayla ayna gibi yapmak."},
    {"kelime": "çamurun kurumasını önlemek", "yasakli_kelimeler": ["ıslak bez", "poşet geçirme", "nemli tutma", "çatlama", "su püskürtme"], "zorluk": "orta", "aciklama": "Çalışma aralarında heykelin çatlamaması için üzerini ıslak bezle örtmek."},

    # Zor (14)
    {"kelime": "kayıp mum yöntemini uygulamak", "yasakli_kelimeler": ["cire perdue", "balmumu eritme", "seramik kabuk", "bronz döküm", "antik teknik"], "zorluk": "zor", "aciklama": "Balmumundan yapılan modelin eritilip yerine erimiş bronz akıtılması tekniğini yürütmek."},
    {"kelime": "contrapposto duruşu vermek", "yasakli_kelimeler": ["ağırlık tek bacakta", "omuz kalça zıtlığı", "s kıvrımı", "klasik yunan", "dinamik denge"], "zorluk": "zor", "aciklama": "Heykele vücut ağırlığını tek bacağa verdirerek doğal bir 'S' kıvrımı kazandırmak."},
    {"kelime": "doğrudan yontu yapmak", "yasakli_kelimeler": ["taille directe", "modele dayanmadan", "taşın içinde saklı form", "kendiliğinden", "michelangelo"], "zorluk": "zor", "aciklama": "Önceden kalıp veya kopyalama yapmadan taşı doğrudan doğruya yontarak biçimlendirmek."},
    {"kelime": "assemblage tekniğiyle birleştirmek", "yasakli_kelimeler": ["hazır nesneler", "hurda", "üç boyutlu kolaj", "buluntu obje", "montaj"], "zorluk": "zor", "aciklama": "Gündelik veya endüstriyel hazır hurda nesneleri birleştirerek heykel oluşturmak."},
    {"kelime": "non-finito etkisi bırakmak", "yasakli_kelimeler": ["bitmemişlik", "ham taş", "michelangelo", "taslak hali", "kasıtlı"], "zorluk": "zor", "aciklama": "Heykelin bir kısmını kaba ve yontulmamış ham taş halinde bırakarak sanatsal ifade yaratmak."},
    {"kelime": "chavant kili ile modellemek", "yasakli_kelimeler": ["endüstriyel kil", "asla kurumayan", "otomotiv tasarımı", "kükürtsüz", "hassas detay"], "zorluk": "zor", "aciklama": "Kurumayan profesyonel sentetik modelaj kiliyle mikron hassasiyetinde detay çalışmak."},
    {"kelime": "alttan oymacılık yapmak", "yasakli_kelimeler": ["undercut", "derin gölge", "havada asılı kumaş", "keski açısı", "ustalık"], "zorluk": "zor", "aciklama": "Mermerin altını boşaltıp kumaş veya uzuvları havada asılı durur gibi yontmak."},
    {"kelime": "polikromi rekonstrüksiyonu yapmak", "yasakli_kelimeler": ["antik heykel renkleri", "morötesi lamba", "pigment izleri", "boyalı mermer", "restorasyon"], "zorluk": "zor", "aciklama": "Antik mermer heykellerin üzerindeki kayıp renkleri mikroskobik analizle yeniden canlandırmak."},
    {"kelime": "kum kalıba döküm yapmak", "yasakli_kelimeler": ["döküm kumu", "reçine bağlı kum", "derece", "yolluk", "demir"], "zorluk": "zor", "aciklama": "Sıkıştırılmış refrakter kumu kullanarak büyük metalleri kalıba dökmek."},
    {"kelime": "chryselephantine heykel yapmak", "yasakli_kelimeler": ["fildişi ve altın", "antik yunan", "zeus heykeli", "ahşap çekirdek", "lüks malzeme"], "zorluk": "zor", "aciklama": "Ahşap iskelet üzerine fildişi et ve altın giysi plakaları kaplayarak anıt inşa etmek."},
    {"kelime": "site-specific heykel kurmak", "yasakli_kelimeler": ["mekana özgü", "çevreyle bütünleşen", "arazi sanatı", "kamusal alan", "bağlamsal"], "zorluk": "zor", "aciklama": "Sadece kurulacağı mekanın mimari ve coğrafi dokusuna özel heykel tasarlayıp yerleştirmek."},
    {"kelime": "giyotin tipi iskarpela kullanmak", "yasakli_kelimeler": ["kavisli oyuk", "derin kanal", "ahşap lifleri", "darbeli", "yontma"], "zorluk": "zor", "aciklama": "Ahşap kütüğün sert liflerini koparmadan derin oluklar açmak için kavisli bıçak kullanmak."},
    {"kelime": "reaktif kimyasallarla oksitlemek", "yasakli_kelimeler": ["kükürt karaciğeri", "potasyum sülfür", "bronz karartma", "kontrollü pas", "ısı tabancası"], "zorluk": "zor", "aciklama": "Isı tabancası ve sülfür tuzlarıyla bronz yüzeyde zengin siyah-kahve tonları üretmek."},
    {"kelime": "mermerde saydamlık elde etmek", "yasakli_kelimeler": ["ışık geçirgenliği", "ince yontma", "duvak etkisi", "sanmartino", "kristal yapı"], "zorluk": "zor", "aciklama": "Mermeri ışığı geçirecek kadar ince yontarak kumaş veya tül saydamlığı hissi vermek."}
]

# 22. hobiler
hobiler_verbs = [
    # Kolay (12)
    {"kelime": "örgü örmek", "yasakli_kelimeler": ["şiş", "yün", "ip", "kazak", "atkı"], "zorluk": "kolay", "aciklama": "Şiş ve yün iplikle ilmekler atarak giysi üretmek."},
    {"kelime": "resim yapmak", "yasakli_kelimeler": ["fırça", "tuval", "boya", "kağıt", "çizmek"], "zorluk": "kolay", "aciklama": "Tuval veya kağıda boyalarla görsel sanat icra etmek."},
    {"kelime": "balık tutmak", "yasakli_kelimeler": ["olta", "kanca", "yem", "deniz", "göl"], "zorluk": "kolay", "aciklama": "Boş zamanlarında su kenarında oltayla balık yakalamak."},
    {"kelime": "bahçe ile uğraşmak", "yasakli_kelimeler": ["çiçek", "toprak", "sulama", "ekmek", "fidan"], "zorluk": "kolay", "aciklama": "Bahçedeki bitki ve sebzelerin bakımını yapmak."},
    {"kelime": "puzzle yapmak", "yasakli_kelimeler": ["parça", "yapboz", "birleştirmek", "tablo", "kutu"], "zorluk": "kolay", "aciklama": "Yüzlerce küçük parçayı birleştirerek resmi tamamlamak."},
    {"kelime": "kitap okumak", "yasakli_kelimeler": ["roman", "sayfa", "yazar", "kütüphane", "hikaye"], "zorluk": "kolay", "aciklama": "Boş vakitleri kitap sayfaları arasında değerlendirmek."},
    {"kelime": "doğa yürüyüşü yapmak", "yasakli_kelimeler": ["trekking", "orman", "dağ", "patika", "yürümek"], "zorluk": "kolay", "aciklama": "Doğal parkurlarda temiz havada uzun yürüyüşe çıkmak."},
    {"kelime": "ahşap boyamak", "yasakli_kelimeler": ["kutu", "fırça", "akrilik", "tepsi", "vernik"], "zorluk": "kolay", "aciklama": "Ham ahşap objeleri dekoratif amaçla renklendirmek."},
    {"kelime": "koleksiyon yapmak", "yasakli_kelimeler": ["biriktirmek", "hobi", "para", "pul", "araba"], "zorluk": "kolay", "aciklama": "İlgi duyulan nesneleri düzenli olarak bir araya getirmek."},
    {"kelime": "satranç oynamak", "yasakli_kelimeler": ["şah", "mat", "piyon", "tahta", "hamle"], "zorluk": "kolay", "aciklama": "Zeka ve strateji oyununda taşları hareket ettirmek."},
    {"kelime": "pasta süslemek", "yasakli_kelimeler": ["krema", "şeker hamuru", "sıkma torbası", "kek", "renkli"], "zorluk": "kolay", "aciklama": "Kek ve pastaların üzerini renkli kremalarla süslemek."},
    {"kelime": "maket yapmak", "yasakli_kelimeler": ["yapıştırıcı", "parça", "uçak", "gemi", "küçük"], "zorluk": "kolay", "aciklama": "Araç veya binaların küçük ölçekli modellerini inşa etmek."},

    # Orta (24)
    {"kelime": "makrome örmek", "yasakli_kelimeler": ["düğüm", "ip", "duvar süsü", "saksılık", "bohem"], "zorluk": "orta", "aciklama": "Şiş veya tığ olmadan sadece ipleri düğümleyerek dekoratif ürünler yapmak."},
    {"kelime": "origami katlamak", "yasakli_kelimeler": ["kağıt", "japon", "kesmeden", "kuş", "katlama sanatı"], "zorluk": "orta", "aciklama": "Kare kağıdı makas ve yapıştırıcı olmadan katlayarak figürler üretmek."},
    {"kelime": "diorama inşa etmek", "yasakli_kelimeler": ["minyatür sahne", "üç boyutlu", "makette çevre", "kutu", "gerçekçi"], "zorluk": "orta", "aciklama": "Tarihi bir anı veya sahneyi minyatür ölçekte gerçekçi şekilde canlandırmak."},
    {"kelime": "deri işlemek", "yasakli_kelimeler": ["cüzdan", "dikim", "mum iplik", "delme zımbası", "deri el sanatları"], "zorluk": "orta", "aciklama": "Doğal deriyi kesip dikerek el yapımı cüzdan veya kemer üretmek."},
    {"kelime": "sabun yapmak", "yasakli_kelimeler": ["kostik", "zeytinyağı", "kalıp", "lavanta", "doğal"], "zorluk": "orta", "aciklama": "Bitkisel yağlar ve esanslarla evde el yapımı doğal sabun üretmek."},
    {"kelime": "teraryum tasarlamak", "yasakli_kelimeler": ["cam fanus", "sukulent", "yosun", "çakıl taşı", "minyatür ekosistem"], "zorluk": "orta", "aciklama": "Cam fanus içinde küçük bitkilerle yaşayan bir mikro dünya kurmak."},
    {"kelime": "mum dökmek", "yasakli_kelimeler": ["soya mumu", "fitil", "erimiş parafin", "esans", "koku"], "zorluk": "orta", "aciklama": "Eritilmiş balmumu veya soyayı koku ekleyerek kalıba dökmek."},
    {"kelime": "kuş gözlemciliği yapmak", "yasakli_kelimeler": ["dürbün", "tür tespiti", "kuş rehberi", "doğa", "göç"], "zorluk": "orta", "aciklama": "Doğada dürbünle yaban kuşlarını izleyip türlerini kaydetmek."},
    {"kelime": "quilling yapmak", "yasakli_kelimeler": ["kağıt kıvırma", "şerit", "rulo", "yapıştırıcı", "desen"], "zorluk": "orta", "aciklama": "Renkli ince kağıt şeritlerini kıvırıp yapıştırarak motifler oluşturmak."},
    {"kelime": "amigurumi örmek", "yasakli_kelimeler": ["tığ", "oyuncak", "elyaf", "japon", "yün"], "zorluk": "orta", "aciklama": "Tığ ile sık iğne tekniği kullanarak içi elyaf dolgulu oyuncaklar örmek."},
    {"kelime": "epoksi reçine dökmek", "yasakli_kelimeler": ["şeffaf", "sertleştirici", "masa", "takı", "kuruma"], "zorluk": "orta", "aciklama": "Sıvı polimer reçineyi pigmentlerle karıştırıp takı veya sehpa üretmek."},
    {"kelime": "ebru yapmak", "yasakli_kelimeler": ["kitre", "tekne", "öd", "at kılı fırça", "biz"], "zorluk": "orta", "aciklama": "Kıvamlı suyun üzerine boyalar serpip deseni kağıda aktarmak."},
    {"kelime": "etamin işlemek", "yasakli_kelimeler": ["kanaviçe", "çarpı işi", "kumaş", "kasnak", "muline iplik"], "zorluk": "orta", "aciklama": "Kareli kumaşa ipliklerle çarpı atarak desen işlemek."},
    {"kelime": "tel kırma yapmak", "yasakli_kelimeler": ["gümüş tel", "tül", "geleneksel", "bükerek kırma", "el sanatı"], "zorluk": "orta", "aciklama": "Tül kumaşa madeni tellerle makassız büküp kırarak motif işlemek."},
    {"kelime": "ahşap yakma yapmak", "yasakli_kelimeler": ["pirografi", "havya", "ısı ucu", "ahşap desen", "kontrplak"], "zorluk": "orta", "aciklama": "Sıcak havya ucuyla ahşabın yüzeyini yakarak resim ve yazı çizmek."},
    {"kelime": "filografi örmek", "yasakli_kelimeler": ["çivi", "tel", "ahşap pano", "sarım", "çekiç"], "zorluk": "orta", "aciklama": "Ahşaba çakılan çivilerin arasından renkli telleri dolayarak desen üretmek."},
    {"kelime": "taş boyamak", "yasakli_kelimeler": ["akrilik boya", "çakıl taşı", "fırça", "mandala", "vernik"], "zorluk": "orta", "aciklama": "Deniz kenarından toplanan düz taşların üzerine desenler çizmek."},
    {"kelime": "kalligrafi çalışmak", "yasakli_kelimeler": ["güzel yazı", "kesik uçlu kalem", "mürekkep", "harf", "hat"], "zorluk": "orta", "aciklama": "Özel dolma kalemlerle estetik ve zarif el yazısı pratiği yapmak."},
    {"kelime": "polimer kil pişirmek", "yasakli_kelimeler": ["fimo", "ev fırını", "takı yapımı", "şekillendirme", "küpe"], "zorluk": "orta", "aciklama": "Renkli fimo hamurlarını şekillendirip fırında sertleştirerek takı yapmak."},
    {"kelime": "geocaching oynamak", "yasakli_kelimeler": ["gps", "koordinat", "saklı kutu", "hazine avı", "log defteri"], "zorluk": "orta", "aciklama": "GPS koordinatlarını takip ederek doğaya saklanmış kutuları bulmak."},
    {"kelime": "teleskopla gökyüzünü izlemek", "yasakli_kelimeler": ["ay kraterleri", "gezegen", "yıldız", "astronomi", "mercek"], "zorluk": "orta", "aciklama": "Amatör teleskopla gece gökyüzündeki gezegen ve kraterleri gözlemek."},
    {"kelime": "boncuk dizmek", "yasakli_kelimeler": ["misina", "kolye", "bileklik", "takı", "kristal"], "zorluk": "orta", "aciklama": "Renkli boncukları misinaya ipe dizerek şık takılar tasarlamak."},
    {"kelime": "ahşap oymacılığı yapmak", "yasakli_kelimeler": ["kaşık oyma", "ıhlamur ağacı", "bıçak", "kuka", "el işi"], "zorluk": "orta", "aciklama": "Yumuşak ağaç kütüğünden el bıçağıyla tahta kaşık ve tabak oymak."},
    {"kelime": "seramik çarkında dönmek", "yasakli_kelimeler": ["torba", "vazo", "dönen tabla", "ıslak çamur", "çömlek"], "zorluk": "orta", "aciklama": "Dönen torna tezgahında ıslak kile merkezleme yaparak vazo formu vermek."},

    # Zor (14)
    {"kelime": "bonsai budamak", "yasakli_kelimeler": ["minyatür ağaç", "tel sarma", "kök budama", "japon sanatı", "şekillendirme"], "zorluk": "zor", "aciklama": "Canlı ağacı özel tekniklerle saksıda minyatür formda tutarak budamak."},
    {"kelime": "tiffany vitray yapmak", "yasakli_kelimeler": ["bakır folyo", "lehim", "renkli cam", "cam kesici", "abajur"], "zorluk": "zor", "aciklama": "Renkli cam parçalarının kenarını bakır folyo sarıp lehimle birleştirmek."},
    {"kelime": "kakmacılık icra etmek", "yasakli_kelimeler": ["sedef kakma", "gümüş tel", "ahşap oyuk", "kakma", "antika"], "zorluk": "zor", "aciklama": "Ahşaba oyulan yuvalara sedef ve gümüş telleri gömerek işlemek."},
    {"kelime": "airbrush ile model boyamak", "yasakli_kelimeler": ["hava tabancası", "kompresör", "ölçekli maket", "akrilik", "ince püskürtme"], "zorluk": "zor", "aciklama": "Hava kompresörlü püskürtme tabancasıyla makete kusursuz boya katmanı atmak."},
    {"kelime": "eskitme ve yıkama yapmak", "yasakli_kelimeler": ["weathering", "wash", "panel çizgileri", "pas çamur efekti", "maketçilik"], "zorluk": "zor", "aciklama": "Model maket üzerine yağlı boya ve pigmentlerle gerçekçi yıpranma izi vermek."},
    {"kelime": "mikromakrome düğümlemek", "yasakli_kelimeler": ["linhasita ip", "mumlanmış", "doğal taş sarmalama", "0.5 mm", "hassas takı"], "zorluk": "zor", "aciklama": "Milimetrik mumlu iplerle mikroskobik düğümler atarak taşlı takılar örmek."},
    {"kelime": "luthierlik denemeleri yapmak", "yasakli_kelimeler": ["enstrüman yapımı", "gitar gövdesi", "ağaç kurutma", "ses tahtası", "tel yüksekliği"], "zorluk": "zor", "aciklama": "Ahşaptan kendi telli müzik aletini sıfırdan inşa etmek."},
    {"kelime": "kintsugi ile tamir etmek", "yasakli_kelimeler": ["altın tozu", "kırık porselen", "urushi cilası", "japon felsefesi", "kusuru yüceltme"], "zorluk": "zor", "aciklama": "Kırılan seramikleri altın tozu karışımlı reçineyle birleştirip kusuru sanat yapmak."},
    {"kelime": "ampermetre ile radyo lehimlemek", "yasakli_kelimeler": ["amatör telsizcilik", "ham radio", "devre kartı", "anten", "mors"], "zorluk": "zor", "aciklama": "Elektronik devreleri kendi lehimleyerek amatör radyo alıcısı kurmak."},
    {"kelime": "damascus çeliği dövmek", "yasakli_kelimeler": ["şam çeliği", "katlama", "ocak", "örs", "desenli bıçak"], "zorluk": "zor", "aciklama": "Farklı karbon oranlı çelikleri üst üste katlayıp döverek desenli bıçak yapmak."},
    {"kelime": "marquetry kakması yapmak", "yasakli_kelimeler": ["ahşap kaplama", "kakma motifi", "kıl testere", "farklı ağaç renkleri", "kakmacılık"], "zorluk": "zor", "aciklama": "Farklı renkteki ince ağaç kaplamalarını kıl testereyle kesip tablo gibi birleştirmek."},
    {"kelime": "vitray fırınlama yapmak", "yasakli_kelimeler": ["cam füzyon", "800 derece", "eriyerek kaynaşma", "fırın", "cam tozu"], "zorluk": "zor", "aciklama": "Farklı renkli camları yüksek ısı fırınında tek parça halinde eritip kaynaştırmak."},
    {"kelime": "kayıp köpük dökümü yapmak", "yasakli_kelimeler": ["strafor model", "döküm kumu", "eriyik alüminyum", "buharlaşma", "metal"], "zorluk": "zor", "aciklama": "Strafordan kesilen modeli kum kalıba gömüp eriyik metalle buharlaştırarak dökmek."},
    {"kelime": "fermente ekmek mayalamak", "yasakli_kelimeler": ["ekşi maya", "otoliz", "katlama tekniği", "yüksek hidrasyon", "döküm tencere"], "zorluk": "zor", "aciklama": "Yıllanmış canlı ekşi mayayla yüksek hidrasyonlu artisan ekmek hamuru geliştirmek."}
]

add_and_save_verbs('heykeltiraslik', heykeltiraslik_verbs)
add_and_save_verbs('hobiler', hobiler_verbs)
print('P11 done!')
