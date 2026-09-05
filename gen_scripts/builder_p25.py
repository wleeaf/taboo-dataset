# -*- coding: utf-8 -*-
from card_utils import add_and_save_verbs

metalurji_verbs = [
    # Kolay (12)
    {"kelime": "eritmek", "aciklama": "metali yüksek sıcaklıkta sıvı hale getirmek", "yasakli_kelimeler": ["sıvı", "sıcaklık", "döküm", "ocak", "fırın"], "zorluk": "kolay"},
    {"kelime": "dövmek", "aciklama": "kızgın metale çekiçle vurarak şekil vermek", "yasakli_kelimeler": ["çekiç", "örs", "demir", "şekil", "vurmak"], "zorluk": "kolay"},
    {"kelime": "kaynatmak", "aciklama": "iki metal parçayı ısıyla birleştirmek", "yasakli_kelimeler": ["kaynak", "birleştirmek", "elektrot", "lehim", "ek"], "zorluk": "kolay"},
    {"kelime": "kesmek", "aciklama": "metal levhayı veya çubuğu parçalara ayırmak", "yasakli_kelimeler": ["testere", "spiral", "bıçak", "parça", "ayırmak"], "zorluk": "kolay"},
    {"kelime": "bükmek", "aciklama": "metal boru veya sacı eğriltmek", "yasakli_kelimeler": ["eğmek", "sac", "boru", "açı", "kıvırmak"], "zorluk": "kolay"},
    {"kelime": "delmek", "aciklama": "metal yüzeyde matkapla delik açmak", "yasakli_kelimeler": ["matkap", "delik", "uç", "açmak", "torna"], "zorluk": "kolay"},
    {"kelime": "parlatmak", "aciklama": "işlenen metal yüzeyi pürüzsüz ve parlak yapmak", "yasakli_kelimeler": ["cila", "polisaj", "yüzey", "parlak", "zımpara"], "zorluk": "kolay"},
    {"kelime": "soğutmak", "aciklama": "ısıl işlem gören metali oda sıcaklığına düşürmek", "yasakli_kelimeler": ["su", "yağ", "ısı", "sıcaklık", "banyo"], "zorluk": "kolay"},
    {"kelime": "dökmek", "aciklama": "sıvı metali kalıba boşaltmak", "yasakli_kelimeler": ["kalıp", "sıvı", "pota", "ergiyik", "boşaltmak"], "zorluk": "kolay"},
    {"kelime": "zımparalamak", "aciklama": "metal yüzeydeki pürüzleri aşındırıcıyla gidermek", "yasakli_kelimeler": ["aşındırmak", "pürüz", "kağıt", "yüzey", "temizlemek"], "zorluk": "kolay"},
    {"kelime": "paslanmak", "aciklama": "demirin oksijen ve nemle korozyona uğraması", "yasakli_kelimeler": ["demir", "oksit", "nem", "korozyon", "küf"], "zorluk": "kolay"},
    {"kelime": "kaplamak", "aciklama": "metali korumak veya süslemek için başka katmanla örtmek", "yasakli_kelimeler": ["galvaniz", "krom", "tabaka", "yüzey", "örtmek"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "tavlamak", "aciklama": "metali yumuşatmak veya iç gerilimini almak için ısıtıp bekletmek", "yasakli_kelimeler": ["ısıl işlem", "fırın", "yumuşatmak", "gerilim", "ısıtmak"], "zorluk": "orta"},
    {"kelime": "su vermek", "aciklama": "kızgın metali hızla soğutarak sertliğini artırmak", "yasakli_kelimeler": ["sertleşmek", "ani", "soğutma", "yağ", "çelik"], "zorluk": "orta"},
    {"kelime": "haddelemek", "aciklama": "metali silindirler arasından geçirerek kalınlığını inceltmek", "yasakli_kelimeler": ["silindir", "sac", "baskı", "kalınlık", "merdane"], "zorluk": "orta"},
    {"kelime": "ekstrüzyon yapmak", "aciklama": "metali belirli kesitteki profilden basınçla geçirmek", "yasakli_kelimeler": ["profil", "basınç", "kalıp", "alüminyum", "itmek"], "zorluk": "orta"},
    {"kelime": "lehimlemek", "aciklama": "düşük erime noktalı alaşımla metalleri tutturmak", "yasakli_kelimeler": ["havya", "kalay", "pasta", "tel", "elektronik"], "zorluk": "orta"},
    {"kelime": "preslemek", "aciklama": "büyük kuvvet uygulayarak sacı kalıp içinde şekillendirmek", "yasakli_kelimeler": ["baskı", "hidrolik", "kalıp", "kuvvet", "ezmek"], "zorluk": "orta"},
    {"kelime": "çapak almak", "aciklama": "kesim veya döküm sonrası kenarlardaki fazlalıkları temizlemek", "yasakli_kelimeler": ["fazlalık", "kenar", "taşlama", "temizlemek", "pürüz"], "zorluk": "orta"},
    {"kelime": "taşlamak", "aciklama": "aşındırıcı taşla metal parça yüzeyini işlemek", "yasakli_kelimeler": ["taş", "spiral", "kıvılcım", "aşındırmak", "çark"], "zorluk": "orta"},
    {"kelime": "alaşımlamak", "aciklama": "iki veya daha fazla metali eritip homojen karıştırmak", "yasakli_kelimeler": ["karışım", "metal", "özellik", "katkı", "tunç"], "zorluk": "orta"},
    {"kelime": "galvanizlemek", "aciklama": "çeliği paslanmaya karşı çinko banyosuna daldırmak", "yasakli_kelimeler": ["çinko", "daldırma", "pas", "korozyon", "banyo"], "zorluk": "orta"},
    {"kelime": "eloksal kaplamak", "aciklama": "alüminyum yüzeyinde koruyucu oksit tabakası oluşturmak", "yasakli_kelimeler": ["alüminyum", "anodik", "oksit", "yüzey", "elektroliz"], "zorluk": "orta"},
    {"kelime": "kumlama yapmak", "aciklama": "yüksek basınçlı kum tanecikleriyle pas ve boyayı sökmek", "yasakli_kelimeler": ["kum", "basınç", "yüzey", "temizlik", "püskürtmek"], "zorluk": "orta"},
    {"kelime": "frezalamak", "aciklama": "dönen kesici takımla talaş kaldırarak metale form vermek", "yasakli_kelimeler": ["freze", "talaş", "takım", "tezgah", "kesici"], "zorluk": "orta"},
    {"kelime": "tornalamak", "aciklama": "dönen iş parçası üzerinden sabit keskiyle talaş sökmek", "yasakli_kelimeler": ["torna", "ayna", "keski", "silindirik", "dönmek"], "zorluk": "orta"},
    {"kelime": "perçinlemek", "aciklama": "metal pimlerin başını ezerek levhaları sökülemez bağlamak", "yasakli_kelimeler": ["perçin", "pim", "tabanca", "birleştirmek", "baş"], "zorluk": "orta"},
    {"kelime": "menevişlemek", "aciklama": "sertleştirilmiş çeliğin kırılganlığını gidermek için yeniden ısıtmak", "yasakli_kelimeler": ["çelik", "ısıl işlem", "kırılganlık", "gevşetme", "renk"], "zorluk": "orta"},
    {"kelime": "curuf ayırmak", "aciklama": "sıvı metal üzerindeki yabancı ve oksitli tabakayı sıyırmak", "yasakli_kelimeler": ["curuf", "atık", "sıvı", "üst", "fırın"], "zorluk": "orta"},
    {"kelime": "oksitlenmek", "aciklama": "metal atomlarının havadaki oksijenle kimyasal reaksiyona girmesi", "yasakli_kelimeler": ["oksijen", "reaksiyon", "hava", "yüzey", "pas"], "zorluk": "orta"},
    {"kelime": "yiv açmak", "aciklama": "silindirik yüzey veya delik içine vida dişi çekmek", "yasakli_kelimeler": ["kılavuz", "pafta", "vida", "diş", "delik"], "zorluk": "orta"},
    {"kelime": "çözeltiye almak", "aciklama": "alaşım elementlerini tek faz halinde katı çözeltide çözmek", "yasakli_kelimeler": ["faz", "homojen", "ısıtma", "katı", "çözünme"], "zorluk": "orta"},
    {"kelime": "sinterlemek", "aciklama": "metal tozlarını erime sıcaklığının altında presleyip fırınlamak", "yasakli_kelimeler": ["toz", "metalurji", "fırın", "kompakt", "katılaşma"], "zorluk": "orta"},
    {"kelime": "asitle temizlemek", "aciklama": "sıcak haddelenmiş sacın tufalını asit banyosunda arındırmak", "yasakli_kelimeler": ["tufal", "banyo", "pikling", "asit", "yüzey"], "zorluk": "orta"},
    {"kelime": "fosfatlamak", "aciklama": "boya öncesi metal yüzeyinde yapışmayı artıran tuz tabakası oluşturmak", "yasakli_kelimeler": ["fosfat", "boya", "astar", "korozyon", "banyo"], "zorluk": "orta"},
    {"kelime": "zımba ile delmek", "aciklama": "pres kalıbındaki zımbayla sacdan parça koparmak", "yasakli_kelimeler": ["zımba", "sac", "pres", "koparma", "kesim"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "karbürlemek", "aciklama": "çelik yüzeyine yüksek sıcaklıkta karbon emdirerek sertleştirmek", "yasakli_kelimeler": ["sementasyon", "karbon", "sertlik", "difüzyon", "yüzey"], "zorluk": "zor"},
    {"kelime": "nitrürlemek", "aciklama": "metali azot atmosferinde ısıtarak aşınma direncini artırmak", "yasakli_kelimeler": ["azot", "difüzyon", "aşınma", "gaz", "sertlik"], "zorluk": "zor"},
    {"kelime": "ötektoid dönüşmek", "aciklama": "katı fazın soğurken iki ayrı katı faza ayrışması", "yasakli_kelimeler": ["perlit", "östenit", "soğuma", "katı", "diyagram"], "zorluk": "zor"},
    {"kelime": "yeniden kristalleşmek", "aciklama": "soğuk şekil verilmiş metalde deformasyonsuz yeni tanelerin doğması", "yasakli_kelimeler": ["tane", "tavlama", "kristal", "deformasyon", "sıcaklık"], "zorluk": "zor"},
    {"kelime": "katotik korumak", "aciklama": "metale kurban anot bağlayarak korozyonu engellemek", "yasakli_kelimeler": ["kurban anot", "akım", "potansiyel", "korozyon", "boru hattı"], "zorluk": "zor"},
    {"kelime": "indüksiyonla ısıtmak", "aciklama": "manyetik alan girdap akımlarıyla iletken metali temassız ısıtmak", "yasakli_kelimeler": ["akım", "frekans", "bobin", "manyetik", "temassız"], "zorluk": "zor"},
    {"kelime": "segregasyona uğramak", "aciklama": "döküm katılaşırken alaşım elementlerinin bölgesel ayrışması", "yasakli_kelimeler": ["ayrışma", "katılaşma", "heterojen", "konsantrasyon", "külçe"], "zorluk": "zor"},
    {"kelime": "dislokasyon kayması", "aciklama": "kristal kafesindeki çizgisel kusurların gerilme altında ilerlemesi", "yasakli_kelimeler": ["kafes", "kusur", "plastik", "kayma", "düzlem"], "zorluk": "zor"},
    {"kelime": "yaşlandırmak", "aciklama": "çökelti sertleşmesi için alaşımı belirli sıcaklıkta bekleterek mukavemetini yükseltmek", "yasakli_kelimeler": ["çökelti", "mukavemet", "alüminyum", "zaman", "sertleşme"], "zorluk": "zor"},
    {"kelime": "tufal oluşturmak", "aciklama": "sıcak haddeleme sırasında yüzeyde kalın demir oksit kabuğu birikmesi", "yasakli_kelimeler": ["oksit", "kabuk", "yüksek sıcaklık", "sac", "demir"], "zorluk": "zor"},
    {"kelime": "pekleşmek", "aciklama": "soğuk plastik deformasyon sonucu metalin akma mukavemetinin artması", "yasakli_kelimeler": ["soğuk deformasyon", "akma", "mukavemet", "sertleşme", "iş"], "zorluk": "zor"},
    {"kelime": "pota ocağında rafine etmek", "aciklama": "sıvı çeliğin kükürt ve gazlarını ikincil metalurjide gidermek", "yasakli_kelimeler": ["ikincil", "kükürt", "vakum", "gaz giderme", "çelik"], "zorluk": "zor"},
    {"kelime": "sünek kırılmak", "aciklama": "metal parçanın belirgin plastik uzama ve boyun verme sonrası kopması", "yasakli_kelimeler": ["plastik deformasyon", "boyun verme", "kopma", "çukurcuk", "gevrek"], "zorluk": "zor"},
    {"kelime": "gevrek çatlamak", "aciklama": "darbe veya gerilme altında deformasyon göstermeden aniden yarılmak", "yasakli_kelimeler": ["çatlak", "kırılma", "darbe", "klivaj", "ani"], "zorluk": "zor"}
]

meteoroloji_verbs = [
    # Kolay (12)
    {"kelime": "yağmak", "aciklama": "gökyüzünden yağmur veya kar tanelerinin yere düşmesi", "yasakli_kelimeler": ["yağmur", "kar", "gök", "damla", "düşmek"], "zorluk": "kolay"},
    {"kelime": "esmek", "aciklama": "havanın bir yönden diğerine hareket etmesi", "yasakli_kelimeler": ["rüzgar", "hava", "fırtına", "meltem", "yön"], "zorluk": "kolay"},
    {"kelime": "ısınmak", "aciklama": "hava sıcaklığının yukarı doğru artması", "yasakli_kelimeler": ["sıcaklık", "derece", "güneş", "artmak", "hava"], "zorluk": "kolay"},
    {"kelime": "soğumak", "aciklama": "hava sıcaklığının eksiye veya aşağıya düşmesi", "yasakli_kelimeler": ["sıcaklık", "derece", "kış", "düşmek", "ayaz"], "zorluk": "kolay"},
    {"kelime": "donmak", "aciklama": "sıvı suyun sıfır derecede buza dönüşmesi", "yasakli_kelimeler": ["buz", "sıfır", "soğuk", "su", "kristal"], "zorluk": "kolay"},
    {"kelime": "erimek", "aciklama": "sıcaklık artınca yerdeki karların ve buzların suya dönmesi", "yasakli_kelimeler": ["kar", "buz", "sıcak", "su", "çözülmek"], "zorluk": "kolay"},
    {"kelime": "güneş açmak", "aciklama": "bulutların dağılıp güneş ışığının görünmesi", "yasakli_kelimeler": ["bulut", "güneş", "ışık", "açık", "dağılmak"], "zorluk": "kolay"},
    {"kelime": "bulutlanmak", "aciklama": "gökyüzünün bulut kütleleriyle kaplanması", "yasakli_kelimeler": ["bulut", "gök", "kapalı", "hava", "kapanmak"], "zorluk": "kolay"},
    {"kelime": "sis basmak", "aciklama": "yeryüzüne inen yoğun nem tabakasının görüşü kapatması", "yasakli_kelimeler": ["sis", "görüş", "duman", "pus", "yol"], "zorluk": "kolay"},
    {"kelime": "çakmak", "aciklama": "fırtına bulutları arasında ani elektrik parlaması olmak", "yasakli_kelimeler": ["şimşek", "yıldırım", "ışık", "parlama", "gök"], "zorluk": "kolay"},
    {"kelime": "gürlemek", "aciklama": "şimşek sonrası havanın titreşimiyle büyük ses çıkması", "yasakli_kelimeler": ["gök", "ses", "şimşek", "yankı", "patlama"], "zorluk": "kolay"},
    {"kelime": "tahmin etmek", "aciklama": "gelecek günlerdeki hava durumunu önceden hesaplamak", "yasakli_kelimeler": ["hava durumu", "bülten", "uzman", "rapor", "gelecek"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "yoğuşmak", "aciklama": "havadaki su buharının soğuyup sıvı damlacığa dönüşmesi", "yasakli_kelimeler": ["su buharı", "sıvı", "damla", "nem", "soğuma"], "zorluk": "orta"},
    {"kelime": "buharlaşmak", "aciklama": "yeryüzündeki suyun ısı etkisiyle gaza dönüşüp yükselmesi", "yasakli_kelimeler": ["su", "gaz", "gökyüzü", "nem", "kaynamak"], "zorluk": "orta"},
    {"kelime": "çiğ düşmek", "aciklama": "sabaha karşı soğuyan yaprak ve zemin üzerinde su damlası birikmesi", "yasakli_kelimeler": ["damla", "sabah", "yaprak", "nem", "zemin"], "zorluk": "orta"},
    {"kelime": "kırağılaşmak", "aciklama": "su buharının sıvılaşmadan doğrudan buz kristali haline geçmesi", "yasakli_kelimeler": ["buz", "kristal", "don", "soğuk", "zemin"], "zorluk": "orta"},
    {"kelime": "fırtına kopmak", "aciklama": "şiddetli rüzgar ve yağışın aniden başlaması", "yasakli_kelimeler": ["rüzgar", "yağmur", "şiddet", "deniz", "bora"], "zorluk": "orta"},
    {"kelime": "basınç düşmek", "aciklama": "barometredeki hava basıncı değerinin aşağı inmesi", "yasakli_kelimeler": ["barometre", "alçak basınç", "hava", "fırtına", "civa"], "zorluk": "orta"},
    {"kelime": "basınç yükselmek", "aciklama": "barometredeki hava basıncının artıp kararlı hava getirmesi", "yasakli_kelimeler": ["yüksek basınç", "barometre", "açık", "kararlı", "artış"], "zorluk": "orta"},
    {"kelime": "hortum oluşmak", "aciklama": "buluttan yere uzanan dönen şiddetli hava girdabı meydana gelmek", "yasakli_kelimeler": ["hortum", "girdap", "dönmek", "kasırga", "türbülans"], "zorluk": "orta"},
    {"kelime": "dolu yağmak", "aciklama": "fırtına bulutunda donan buz toplarının yeryüzüne inmesi", "yasakli_kelimeler": ["dolu", "buz", "fırtına", "tane", "yağış"], "zorluk": "orta"},
    {"kelime": "poyraz esmek", "aciklama": "kuzeydoğu yönünden soğuk ve sert rüzgar gelmesi", "yasakli_kelimeler": ["kuzeydoğu", "rüzgar", "soğuk", "yön", "marmara"], "zorluk": "orta"},
    {"kelime": "lodos esmek", "aciklama": "güneybatıdan ılık ve denizleri kabartan rüzgar esmesi", "yasakli_kelimeler": ["güneybatı", "sıcak", "dalga", "baş ağrısı", "rüzgar"], "zorluk": "orta"},
    {"kelime": "görüş mesafesi düşmek", "aciklama": "sis veya toz nedeniyle sürücülerin önünü görememesi", "yasakli_kelimeler": ["sis", "metre", "pus", "trafik", "mesafe"], "zorluk": "orta"},
    {"kelime": "enversiyon yaşanmak", "aciklama": "soğuk havanın vadide sıkışıp sıcak havanın üstte kalması durumu", "yasakli_kelimeler": ["terselme", "vadi", "hava kirliliği", "tabaka", "soğuk"], "zorluk": "orta"},
    {"kelime": "radar taraması yapmak", "aciklama": "meteoroloji radarıyla yağış kütlelerinin hareketini izlemek", "yasakli_kelimeler": ["radar", "ekolar", "kütle", "bulut", "yağış"], "zorluk": "orta"},
    {"kelime": "sondaj balonu uçurmak", "aciklama": "atmosferin üst katmanlarından veri toplamak için aletli balon bırakmak", "yasakli_kelimeler": ["balon", "radyosonde", "atmosfer", "yükseklik", "ölçüm"], "zorluk": "orta"},
    {"kelime": "cephe karşılaşmak", "aciklama": "sıcak ve soğuk hava kütlelerinin sınır boyunda çarpışması", "yasakli_kelimeler": ["soğuk cephe", "sıcak cephe", "kütle", "sınır", "yağış"], "zorluk": "orta"},
    {"kelime": "nem ölçmek", "aciklama": "higrometre cihazıyla havadaki bağıl su buharını tespit etmek", "yasakli_kelimeler": ["higrometre", "bağıl nem", "yüzde", "su buharı", "cihaz"], "zorluk": "orta"},
    {"kelime": "rüzgar yönü sapmak", "aciklama": "basınç gradyanı veya coriolis kuvveti etkisiyle yön değiştirmek", "yasakli_kelimeler": ["fırıldak", "coriolis", "yön", "sapma", "derece"], "zorluk": "orta"},
    {"kelime": "kar savurmak", "aciklama": "şiddetli rüzgarın yerdeki karları havaya kaldırıp savurması", "yasakli_kelimeler": ["tipi", "rüzgar", "fırtına", "kar", "göz gözü görmemek"], "zorluk": "orta"},
    {"kelime": "çiy noktasına ulaşmak", "aciklama": "havanın neme tamamen doymuş hale gelip yoğuşma sıcaklığına inmesi", "yasakli_kelimeler": ["doyma", "sıcaklık", "derece", "nem", "yoğuşma"], "zorluk": "orta"},
    {"kelime": "bora patlamak", "aciklama": "aniden başlayan fırtınalı yağışlı sert deniz rüzgarı", "yasakli_kelimeler": ["deniz", "fırtına", "ani", "rüzgar", "patlama"], "zorluk": "orta"},
    {"kelime": "ultraviyole uyarısı vermek", "aciklama": "güneş ışınlarının zararlı radyasyon indeksine karşı halkı uyarmak", "yasakli_kelimeler": ["uv", "güneş", "endeks", "radyasyon", "korunma"], "zorluk": "orta"},
    {"kelime": "kar erimesi hızlanmak", "aciklama": "lodos ve ılık yağmurla dağlardaki kar örtüsünün aniden suya dönüşmesi", "yasakli_kelimeler": ["sel", "dağ", "lodos", "taşkın", "su"], "zorluk": "orta"},
    {"kelime": "toz taşınımı olmak", "aciklama": "çöl fırtınalarıyla kalkan toz bulutlarının uzak ülkelere ulaşması", "yasakli_kelimeler": ["sahra", "çöl", "partikül", "hava kalitesi", "sarı"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "adveksiyon yapmak", "aciklama": "hava kütlesinin ve ısısının yatay hareketle başka bölgeye taşınması", "yasakli_kelimeler": ["yatay", "ısı taşınımı", "kütle", "rüzgar", "sis"], "zorluk": "zor"},
    {"kelime": "konveksiyon oluşmak", "aciklama": "ısınan hava parsellerinin dikey olarak yükselip fırtına bulutu kurması", "yasakli_kelimeler": ["dikey", "yükselme", "kümülonimbus", "termal", "parsel"], "zorluk": "zor"},
    {"kelime": "siklogenez gerçekleşmek", "aciklama": "alçak basınç merkezinin ve siklonik sirkülasyonun doğup gelişmesi", "yasakli_kelimeler": ["siklon", "alçak basınç", "girdap", "merkez", "gelişim"], "zorluk": "zor"},
    {"kelime": "antisiklon yerleşmek", "aciklama": "yüksek basınç alanının merkezden dışarı doğru saat yönünde dönmesi", "yasakli_kelimeler": ["yüksek basınç", "çökme", "kararlı hava", "merkez", "diverjans"], "zorluk": "zor"},
    {"kelime": "oklüzyon oluşturmak", "aciklama": "hızlı soğuk cephenin sıcak cepheyi yakalayıp yukarı kaldırması", "yasakli_kelimeler": ["cephe", "kapalı", "sıcak hava", "yukarı", "soğuk"], "zorluk": "zor"},
    {"kelime": "jeostrofik dengeye gelmek", "aciklama": "basınç gradyan kuvveti ile coriolis kuvvetinin birbirini dengelemesi", "yasakli_kelimeler": ["coriolis", "gradyan", "izobar", "kuvvet", "denge"], "zorluk": "zor"},
    {"kelime": "jet akımına girmek", "aciklama": "troposferin üst seviyelerindeki çok hızlı batı rüzgarları kuşağına kapılmak", "yasakli_kelimeler": ["jet stream", "troposfer", "rüzgar", "kuşak", "uçak"], "zorluk": "zor"},
    {"kelime": "adibatil soğumak", "aciklama": "yükselen hava kütlesinin dışarıyla ısı alışverişi olmadan genleşerek soğuması", "yasakli_kelimeler": ["ısı", "genleşme", "basınç", "parsel", "termodinamik"], "zorluk": "zor"},
    {"kelime": "sublimleşmek", "aciklama": "yüksek irtifadaki kar ve buzun sıvılaşmadan doğrudan su buharına dönmesi", "yasakli_kelimeler": ["buz", "gaz", "buhar", "katı", "faz"], "zorluk": "zor"},
    {"kelime": "türbülansa girmek", "aciklama": "farklı hız ve yöndeki hava akımlarının kaotik girdaplar yaratması", "yasakli_kelimeler": ["girdap", "sarsıntı", "uçak", "akım", "kaotik"], "zorluk": "zor"},
    {"kelime": "virga gözlenmek", "aciklama": "buluttan düşen yağış damlalarının yere ulaşamadan buharlaşması", "yasakli_kelimeler": ["buharlaşma", "yere düşmeme", "bulut", "yağmur izi", "kuru hava"], "zorluk": "zor"},
    {"kelime": "dereboyu sisine yatmak", "aciklama": "gece radyasyonel soğumayla vadi tabanlarına soğuk ve nemli havanın çökmesi", "yasakli_kelimeler": ["vadi", "radyasyon", "çökme", "gece", "taban"], "zorluk": "zor"},
    {"kelime": "süperhücre geliştirmek", "aciklama": "içinde sürekli dönen mezosiklon barındıran dev fırtına yapısına dönüşmek", "yasakli_kelimeler": ["mezosiklon", "hortum", "dolu", "fırtına", "kümülonimbus"], "zorluk": "zor"},
    {"kelime": "ozon tabakası incelmek", "aciklama": "stratosferdeki koruyucu ozon gazı yoğunluğunun kimyasallarla azalması", "yasakli_kelimeler": ["stratosfer", "kloroflorokarbon", "ultraviyole", "gaz", "kutup"], "zorluk": "zor"}
]

if __name__ == "__main__":
    add_and_save_verbs("metalurji", metalurji_verbs)
    add_and_save_verbs("meteoroloji", meteoroloji_verbs)
