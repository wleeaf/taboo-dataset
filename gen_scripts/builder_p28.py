# -*- coding: utf-8 -*-
from card_utils import add_and_save_verbs

moda_verbs = [
    # Kolay (12)
    {"kelime": "giymek", "aciklama": "kıyafet veya ayakkabıyı üzerine geçirmek", "yasakli_kelimeler": ["elbise", "üzerine", "pantolon", "kıyafet", "takmak"], "zorluk": "kolay"},
    {"kelime": "çıkarmak", "aciklama": "üzerindeki elbiseyi veya ayakkabıyı soyunmak", "yasakli_kelimeler": ["soyunmak", "üst", "elbise", "kıyafet", "çıkış"], "zorluk": "kolay"},
    {"kelime": "dikmek", "aciklama": "iğne iplik veya dikiş makinesiyle kumaşı birleştirmek", "yasakli_kelimeler": ["iğne", "iplik", "makine", "kumaş", "terzi"], "zorluk": "kolay"},
    {"kelime": "ütülemek", "aciklama": "kırışık kıyafetleri sıcak ütüyle düzeltmek", "yasakli_kelimeler": ["ütü", "kırışık", "buhar", "sıcak", "düzeltmek"], "zorluk": "kolay"},
    {"kelime": "kombinlemek", "aciklama": "farklı parça kıyafetleri renk ve tarz olarak uydurmak", "yasakli_kelimeler": ["uyum", "tarz", "kıyafet", "parça", "renk"], "zorluk": "kolay"},
    {"kelime": "denemek", "aciklama": "mağazada kıyafetin bedene uyup uymadığına kabinde bakmak", "yasakli_kelimeler": ["kabin", "beden", "prova", "mağaza", "üst"], "zorluk": "kolay"},
    {"kelime": "katlamak", "aciklama": "kıyafetleri dolaba yerleştirmek için büküp düzeltmek", "yasakli_kelimeler": ["dolap", "düzgün", "bükmek", "kırışmak", "raf"], "zorluk": "kolay"},
    {"kelime": "düğmelemek", "aciklama": "gömlek veya ceketin düğmelerini iliklerine geçirmek", "yasakli_kelimeler": ["düğme", "ilik", "gömlek", "ceket", "kapatmak"], "zorluk": "kolay"},
    {"kelime": "fermuar çekmek", "aciklama": "pantolon veya montun fermuarını kapatmak", "yasakli_kelimeler": ["fermuar", "mont", "pantolon", "kapatmak", "diş"], "zorluk": "kolay"},
    {"kelime": "aksesuar takmak", "aciklama": "kombini tamamlamak için kolye, kemer veya şapka takmak", "yasakli_kelimeler": ["kolye", "kemer", "şapka", "küpe", "tamamlamak"], "zorluk": "kolay"},
    {"kelime": "tarz yaratmak", "aciklama": "kendine özgü giyim stili ve imaj oluşturmak", "yasakli_kelimeler": ["stil", "imaj", "özgün", "giyim", "moda"], "zorluk": "kolay"},
    {"kelime": "trend olmak", "aciklama": "bir giyim tarzının veya parçanın dönemde çok popülerleşmesi", "yasakli_kelimeler": ["popüler", "moda", "akım", "herkes", "dönem"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "defileye çıkmak", "aciklama": "mankenin podyumda tasarım kıyafetleri sergileyerek yürümesi", "yasakli_kelimeler": ["podyum", "manken", "yürümek", "tasarım", "koleksiyon"], "zorluk": "orta"},
    {"kelime": "prova yapmak", "aciklama": "terzinin özel dikim kıyafeti müşteri üzerinde ölçüp ayarlaması", "yasakli_kelimeler": ["terzi", "özel dikim", "ölçü", "iğnelemek", "beden"], "zorluk": "orta"},
    {"kelime": "paça boyu almak", "aciklama": "pantolonun uzun gelen paçasını kısaltmak için işaretlemek", "yasakli_kelimeler": ["pantolon", "kısaltmak", "terzi", "boy", "işaret"], "zorluk": "orta"},
    {"kelime": "koleksiyon hazırlamak", "aciklama": "tasarımcının mevsime özel tematik kıyafet serisi üretmesi", "yasakli_kelimeler": ["sezon", "tasarımcı", "tema", "seri", "katalog"], "zorluk": "orta"},
    {"kelime": "desen çizmek", "aciklama": "kumaş üzerine basılacak motif ve figürleri tasarlamak", "yasakli_kelimeler": ["motif", "baskı", "kumaş", "figür", "çizim"], "zorluk": "orta"},
    {"kelime": "renk kartelası seçmek", "aciklama": "koleksiyonda kullanılacak uyumlu renk tonlarını belirlemek", "yasakli_kelimeler": ["kartela", "ton", "palet", "renk", "uyum"], "zorluk": "orta"},
    {"kelime": "overlok çekmek", "aciklama": "kumaş kenarlarının sökülmemesi için özel makineyle sarmak", "yasakli_kelimeler": ["kenar", "sökülmek", "iplik", "makine", "dikiş"], "zorluk": "orta"},
    {"kelime": "pile yapmak", "aciklama": "etek veya perde kumaşına düzenli kat izleri vermek", "yasakli_kelimeler": ["kat", "etek", "kıvrım", "dikiş", "ütü"], "zorluk": "orta"},
    {"kelime": "teyel vurmak", "aciklama": "asıl dikişten önce parçaları geçici iri dikişle tutturmak", "yasakli_kelimeler": ["geçici", "dikiş", "iğne", "iplik", "prova"], "zorluk": "orta"},
    {"kelime": "kloş kesmek", "aciklama": "etek veya elbiseyi dairesel formda genişleyerek dökümlü biçmek", "yasakli_kelimeler": ["etek", "dairesel", "dökümlü", "geniş", "kesim"], "zorluk": "orta"},
    {"kelime": "astar dikmek", "aciklama": "ceket veya eteğin iç yüzeyine ince koruyucu kumaş eklemek", "yasakli_kelimeler": ["iç", "ceket", "kaygan", "koruma", "kumaş"], "zorluk": "orta"},
    {"kelime": "kalıp çıkarmak", "aciklama": "kıyafetin parçalarını parşömen kağıdına standart ölçülerde çizmek", "yasakli_kelimeler": ["parşömen", "patron", "ölçü", "kağıt", "kesim"], "zorluk": "orta"},
    {"kelime": "drapaj yapmak", "aciklama": "kumaşı canlı manken veya cansız prova mankeni üstünde şekillendirmek", "yasakli_kelimeler": ["manken", "iğneleme", "katlama", "üzerinde", "form"], "zorluk": "orta"},
    {"kelime": "vitrin düzenlemek", "aciklama": "mağaza vitrinindeki mankenleri sezonun öne çıkan parçalarıyla giydirmek", "yasakli_kelimeler": ["vitrin", "mağaza", "manken", "görsel", "sergilemek"], "zorluk": "orta"},
    {"kelime": "stil danışmanlığı yapmak", "aciklama": "müşterinin vücut tipine ve ten rengine uygun giyim rehberliği vermek", "yasakli_kelimeler": ["stylist", "danışman", "vücut tipi", "imaj", "öneri"], "zorluk": "orta"},
    {"kelime": "vintage avına çıkmak", "aciklama": "geçmiş dönemlere ait özgün ve kaliteli kıyafetleri ikinci elde aramak", "yasakli_kelimeler": ["eski", "ikinci el", "dönem", "retro", "özgün"], "zorluk": "orta"},
    {"kelime": "kot taşlamak", "aciklama": "denim kumaşa eskimiş ve yumuşak efekt vermek için ponza taşıyla yıkamak", "yasakli_kelimeler": ["denim", "kot", "ponza", "yıkama", "efekt"], "zorluk": "orta"},
    {"kelime": "kapsül dolap kurmak", "aciklama": "birbiriyle tam uyumlu az sayıda kaliteli temel parçadan gardırop oluşturmak", "yasakli_kelimeler": ["minimalist", "temel parça", "gardırop", "kombin", "sade"], "zorluk": "orta"},
    {"kelime": "deri işlemek", "aciklama": "doğal deriyi çanta, ceket veya ayakkabı için tabaklayıp dikmek", "yasakli_kelimeler": ["tabaklama", "çanta", "ayakkabı", "kösele", "doğal"], "zorluk": "orta"},
    {"kelime": "yakayı kolalamak", "aciklama": "gömlek yakasının dik ve sert durması için kola sıvısı sürmek", "yasakli_kelimeler": ["gömlek", "sert", "dik", "kola", "ütü"], "zorluk": "orta"},
    {"kelime": "nakış işlemek", "aciklama": "kumaş üzerine renkli sim ve ipliklerle kabartma desenler yapmak", "yasakli_kelimeler": ["kasnak", "sim", "iplik", "desen", "el işi"], "zorluk": "orta"},
    {"kelime": "kordon geçirmek", "aciklama": "kapüşon veya eşofman belindeki tünele bağlama ipi sokmak", "yasakli_kelimeler": ["ip", "kapüşon", "eşofman", "çengelli iğne", "bağcık"], "zorluk": "orta"},
    {"kelime": "potluk yapmak", "aciklama": "kıyafetin bedene oturmayıp belirli yerde çirkin kat ve bolluk yapması", "yasakli_kelimeler": ["bolluk", "kat", "hata", "oturmamak", "kesim"], "zorluk": "orta"},
    {"kelime": "paçayı kıvırmak", "aciklama": "pantolon paçasını stil gereği veya su değmesin diye dışa doğru katlamak", "yasakli_kelimeler": ["pantolon", "katlama", "dış", "stil", "bilek"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "haute couture üretmek", "aciklama": "kişiye özel el işçiliğiyle üretilen lüks ve yüksek terzilik eseri yapmak", "yasakli_kelimeler": ["yüksek terzilik", "lüks", "el işi", "paris", "özel dikim"], "zorluk": "zor"},
    {"kelime": "prêt-à-porter tasarlamak", "aciklama": "standart bedenlerde seri üretime uygun hazır giyim koleksiyonu hazırlamak", "yasakli_kelimeler": ["hazır giyim", "seri üretim", "standart beden", "koleksiyon", "sezon"], "zorluk": "zor"},
    {"kelime": "moodboard oluşturmak", "aciklama": "koleksiyon ilhamını görselleştirmek için fotoğraf, kumaş ve doku panosu yapmak", "yasakli_kelimeler": ["ilham", "kolaj", "pano", "görsel", "konsept"], "zorluk": "zor"},
    {"kelime": "kupları birleştirmek", "aciklama": "bedene tam oturan ceket ve elbiselerde kavisli göğüs ve bel panellerini dikmek", "yasakli_kelimeler": ["kavis", "panel", "beden", "göğüs", "dikiş"], "zorluk": "zor"},
    {"kelime": "sürdürülebilir moda yapmak", "aciklama": "organik kumaşlar ve geri dönüştürülmüş malzemelerle çevre dostu üretmek", "yasakli_kelimeler": ["ekolojik", "organik", "geri dönüşüm", "çevre", "atık"], "zorluk": "zor"},
    {"kelime": "upcycling uygulamak", "aciklama": "eski ve atık kıyafetleri yeniden tasarlayarak daha değerli parçaya dönüştürmek", "yasakli_kelimeler": ["ileri dönüşüm", "eski kıyafet", "dönüştürmek", "atık", "tasarım"], "zorluk": "zor"},
    {"kelime": "illüstrasyon çizmek", "aciklama": "tasarım siluetini stilize insan figürü üzerinde sanatsal çizimle yansıtmak", "yasakli_kelimeler": ["siluet", "figür", "marker", "çizim", "kroki"], "zorluk": "zor"},
    {"kelime": "tela yapıştırmak", "aciklama": "kumaşa tok ve dik duruş kazandırmak için arkasına ısıyla tela preslemek", "yasakli_kelimeler": ["yaka", "pres", "ütü", "sertlik", "yapışkan"], "zorluk": "zor"},
    {"kelime": "biye geçirmek", "aciklama": "kumaş kenarlarını kapatmak için verev kesilmiş ince kumaş şerit dikmek", "yasakli_kelimeler": ["verev", "şerit", "kenar", "kıvırma", "temiz dikiş"], "zorluk": "zor"},
    {"kelime": "jakar dokumak", "aciklama": "desenlerin baskı yerine ipliklerin dokuma tezgahında örülmesiyle oluşması", "yasakli_kelimeler": ["tezgah", "dokuma", "kendinden desenli", "iplik", "kumaş"], "zorluk": "zor"},
    {"kelime": "fast fashiona direnmek", "aciklama": "hızlı ve kalitesiz tüketim yerine uzun ömürlü zamansız tasarımları seçmek", "yasakli_kelimeler": ["hızlı tüketim", "zamansız", "kalite", "yavaş moda", "tek kullanımlık"], "zorluk": "zor"},
    {"kelime": "siluet kurgulamak", "aciklama": "tasarlanan giysinin uzaktan bakıldığında bedende oluşturduğu dış hat formunu belirlemek", "yasakli_kelimeler": ["dış hat", "a kesim", "kum saati", "form", "oran"], "zorluk": "zor"},
    {"kelime": "apre vermek", "aciklama": "dokunmuş kumaşa su geçirmezlik, parlaklık veya yumuşaklık kazandıran son işlem", "yasakli_kelimeler": ["terbiye", "su itici", "son işlem", "parlaklık", "kumaş"], "zorluk": "zor"},
    {"kelime": "pantone rengi eşleştirmek", "aciklama": "tekstilde standart renk kodunu uluslararası renk kataloğundan tutturmak", "yasakli_kelimeler": ["pantone", "kod", "baskı", "ton tutturma", "katalog"], "zorluk": "zor"}
]

monarsi_verbs = [
    # Kolay (12)
    {"kelime": "hükmetmek", "aciklama": "hükümdarın tebaası ve ülkesi üzerinde mutlak otorite kurması", "yasakli_kelimeler": ["otorite", "kral", "yönetmek", "ülke", "güç"], "zorluk": "kolay"},
    {"kelime": "tahta çıkmak", "aciklama": "yeni kral veya padişahın hükümdarlık koltuğuna oturması", "yasakli_kelimeler": ["taht", "cülus", "kral", "taç", "hükümdar"], "zorluk": "kolay"},
    {"kelime": "taç giymek", "aciklama": "hükümdarlık töreninde başına değerli tacın konulması", "yasakli_kelimeler": ["taç", "tören", "kutsama", "kral", "baş"], "zorluk": "kolay"},
    {"kelime": "ferman çıkarmak", "aciklama": "hükümdarın halka ve bürokrasiye yazılı kesin emir bildirmesi", "yasakli_kelimeler": ["emir", "yazılı", "tuğra", "padişah", "hüküm"], "zorluk": "kolay"},
    {"kelime": "vergi toplamak", "aciklama": "saray ve ordu harcamaları için halktan haraç ve vergi almak", "yasakli_kelimeler": ["halk", "hazine", "saray", "ödeme", "ordu"], "zorluk": "kolay"},
    {"kelime": "saray yaptırmak", "aciklama": "hükümdar ve hanedanın yaşaması için görkemli saray inşa ettirmek", "yasakli_kelimeler": ["saray", "inşa", "hanedan", "görkem", "köşk"], "zorluk": "kolay"},
    {"kelime": "fethetmek", "aciklama": "ordunun başına geçip başka krallığın topraklarını ele geçirmek", "yasakli_kelimeler": ["ordu", "toprak", "ele geçirmek", "zafer", "savaş"], "zorluk": "kolay"},
    {"kelime": "affetmek", "aciklama": "hükümdarın cezalı bir mahkumu veya suçluyu bağışlaması", "yasakli_kelimeler": ["bağışlamak", "lütuf", "mahkum", "ceza", "hükümdar"], "zorluk": "kolay"},
    {"kelime": "cezalandırmak", "aciklama": "saraya veya devlete karşı gelenleri zindana veya idama göndermek", "yasakli_kelimeler": ["zindan", "idam", "suç", "isyan", "ceza"], "zorluk": "kolay"},
    {"kelime": "elçi kabul etmek", "aciklama": "yabancı ülkelerin temsilcilerini taht odasında huzura almak", "yasakli_kelimeler": ["elçi", "huzur", "taht odası", "diplomat", "mektup"], "zorluk": "kolay"},
    {"kelime": "sürgün etmek", "aciklama": "tehdit oluşturan soyluyu veya muhalifi ülke dışına sürmek", "yasakli_kelimeler": ["sürmek", "ülke dışı", "muhalif", "kale", "uzaklaştırmak"], "zorluk": "kolay"},
    {"kelime": "miras kalmak", "aciklama": "kral ölünce krallığın ve hazinenin oğluna devrolması", "yasakli_kelimeler": ["veraset", "hazine", "oğul", "baba", "devir"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "tahttan feragat etmek", "aciklama": "kralın kendi isteğiyle hükümdarlık haklarını veliahda bırakması", "yasakli_kelimeler": ["ab游kasyon", "vazgeçmek", "bırakmak", "veliaht", "taht"], "zorluk": "orta"},
    {"kelime": "isyan bastırmak", "aciklama": "halkın veya ordunun çıkardığı ayaklanmayı kılıçla ezmek", "yasakli_kelimeler": ["ayaklanma", "ordu", "bastırma", "isyancı", "kılıç"], "zorluk": "orta"},
    {"kelime": "soyluluk unvanı vermek", "aciklama": "hizmet eden kişiye dük, kont veya şövalyelik payesi bahşetmek", "yasakli_kelimeler": ["dük", "kont", "şövalye", "unvan", "paye"], "zorluk": "orta"},
    {"kelime": "siyasi evlilik yapmak", "aciklama": "iki hanedan arasında ittifak kurmak için prensesle evlenmek", "yasakli_kelimeler": ["hanedan", "prenses", "ittifak", "dünür", "evlilik"], "zorluk": "orta"},
    {"kelime": "sadakat yemini etmek", "aciklama": "derebeylerin ve şövalyelerin kralın önünde diz çöküp bağlılık bildirmesi", "yasakli_kelimeler": ["biat", "diz çökmek", "bağlılık", "feodal", "yemin"], "zorluk": "orta"},
    {"kelime": "veliaht ilan etmek", "aciklama": "kralın kendisinden sonra tahta geçecek çocuğu resmi olarak duyurması", "yasakli_kelimeler": ["varis", "prens", "halef", "taht", "duyuru"], "zorluk": "orta"},
    {"kelime": "saray darbesi yapmak", "aciklama": "muhafızların veya vezirlerin mevcut kralı tahttan zorla indirmesi", "yasakli_kelimeler": ["darbe", "muhafız", "tahttan indirme", "komplo", "saray"], "zorluk": "orta"},
    {"kelime": "cülus bahşişi dağıtmak", "aciklama": "yeni padişah tahta çıktığında yeniçerilere para dağıtması", "yasakli_kelimeler": ["cülus", "bahşiş", "yeniçeri", "altın", "kapıkulu"], "zorluk": "orta"},
    {"kelime": "divan toplamak", "aciklama": "vezirleri ve komutanları toplayıp devlet işlerini müzakere etmek", "yasakli_kelimeler": ["divan", "vezir", "sadrazam", "toplantı", "müzakere"], "zorluk": "orta"},
    {"kelime": "naip atamak", "aciklama": "hükümdar çocuk yaştayken devleti onun adına yönetecek vekil seçmek", "yasakli_kelimeler": ["vekil", "çocuk kral", "yönetim", "regent", "ana kraliçe"], "zorluk": "orta"},
    {"kelime": "para bastırmak", "aciklama": "kendi adına sikke darbettirerek egemenliğini tescil etmek", "yasakli_kelimeler": ["sikke", "darphane", "egemenlik", "altın", "tuğra"], "zorluk": "orta"},
    {"kelime": "hutbe okutmak", "aciklama": "cuma namazında hükümdarın adını anarak meşruiyetini halka duyurmak", "yasakli_kelimeler": ["cami", "meşruiyet", "adına", "hükümdar", "cuma"], "zorluk": "orta"},
    {"kelime": "entrika çevirmek", "aciklama": "saray içinde rakipleri tasfiye etmek için gizli oyunlar kurmak", "yasakli_kelimeler": ["harem", "komplo", "oyun", "tasfiye", "rakip"], "zorluk": "orta"},
    {"kelime": "kral naibi olmak", "aciklama": "hükümdarın yokluğunda veya hastalığında krallık yetkilerini kullanmak", "yasakli_kelimeler": ["vekalet", "yetki", "kral", "yokluk", "saray"], "zorluk": "orta"},
    {"kelime": "iltimas geçmek", "aciklama": "saray kademelerine akraba veya yakınlarını kayırarak yerleştirmek", "yasakli_kelimeler": ["kayırma", "torpil", "akraba", "kadro", "görev"], "zorluk": "orta"},
    {"kelime": "zehirlenmek", "aciklama": "taht kavgası sırasında kralın yemeğine veya içkisine zehir katılması", "yasakli_kelimeler": ["zehir", "kadeh", "suikast", "taht kavgası", "ölüm"], "zorluk": "orta"},
    {"kelime": "biat almak", "aciklama": "devlet ricali ve tebaanın yeni hükümdara bağlılığını kabul etmek", "yasakli_kelimeler": ["bağlılık", "kabul", "rical", "tören", "itaat"], "zorluk": "orta"},
    {"kelime": "saraydan kız almak", "aciklama": "hanedan prensesiyle evlenerek damat unvanı ve saray nüfuzu kazanmak", "yasakli_kelimeler": ["damat", "prenses", "nüfuz", "evlilik", "paşa"], "zorluk": "orta"},
    {"kelime": "zindana attırmak", "aciklama": "güvenilmez bulunan bürokrat veya soyluyu kalenin karanlık odasına kapatmak", "yasakli_kelimeler": ["zindan", "kilit", "kule", "hapis", "muhalif"], "zorluk": "orta"},
    {"kelime": "haraç bağlamak", "aciklama": "yenilen komşu krallığı her yıl düzenli altın ödemeye zorlamak", "yasakli_kelimeler": ["tazminat", "yıllık", "altın", "ödemek", "komşu"], "zorluk": "orta"},
    {"kelime": "fetva istemek", "aciklama": "yapılacak savaş veya idam için şeyhülislamdan dini izin belgesi almak", "yasakli_kelimeler": ["şeyhülislam", "dini izin", "şeriat", "belge", "onay"], "zorluk": "orta"},
    {"kelime": "tuğra çekmek", "aciklama": "ferman ve beratların üstüne hükümdarın özel imzasını hakketmek", "yasakli_kelimeler": ["tuğra", "imza", "nişancı", "mühür", "ferman"], "zorluk": "orta"},
    {"kelime": "muhafız alayı kurmak", "aciklama": "kralın canını korumak için en seçkin birliklerden özel ordu oluşturmak", "yasakli_kelimeler": ["muhafız", "koruma", "seçkin", "birlik", "özel"], "zorluk": "orta"},
    {"kelime": "kapıkulu oluşturmak", "aciklama": "devşirme çocukları yetiştirip doğrudan saraya bağlı ordu kurmak", "yasakli_kelimeler": ["devşirme", "yeniçeri", "ordu", "doğrudan", "saray"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "kut anlayışına inanmak", "aciklama": "hükümdarlık yetkisinin tanrı tarafından verildiğine inanılan eski türk inancı", "yasakli_kelimeler": ["tanrısal", "gök tanrı", "eski türk", "yetki", "hükümdarlık"], "zorluk": "zor"},
    {"kelime": "primogenitür uygulamak", "aciklama": "tahtın ve mirasın doğrudan en büyük erkek çocuğa geçmesi kuralı", "yasakli_kelimeler": ["en büyük oğul", "veraset", "miras", "kural", "hukuk"], "zorluk": "zor"},
    {"kelime": "ekber ve erşed sistemine geçmek", "aciklama": "hanedanın en yaşlı ve en aklı başında üyesinin tahta çıkması kuralı", "yasakli_kelimeler": ["en yaşlı", "akıl", "i. ahmed", "veraset", "hanedan"], "zorluk": "zor"},
    {"kelime": "kardeş katli uygulamak", "aciklama": "devletin bekası ve taht kavgalarını önlemek için şehzadeleri boğdurmak", "yasakli_kelimeler": ["nizam-ı alem", "şehzade", "boğdurmak", "fatih kanunnamesi", "fetva"], "zorluk": "zor"},
    {"kelime": "kralın ilahi hakkını savunmak", "aciklama": "monarkın sadece tanrıya hesap vereceği ve mutlak otorite olduğu doktrini", "yasakli_kelimeler": ["ilahi hak", "mutlakiyet", "absolütizm", "doktrin", "tanrısal"], "zorluk": "zor"},
    {"kelime": "meşrutiyet ilan etmek", "aciklama": "kralın yetkilerini meclis ve anayasa ile sınırlandıran sisteme geçmek", "yasakli_kelimeler": ["anayasa", "parlamento", "meclis", "sınırlandırma", "kanun-i esasi"], "zorluk": "zor"},
    {"kelime": "lèse-majesté ile yargılamak", "aciklama": "hükümdara veya monarşi kurumuna hakaret ve saygısızlık suçundan ceza vermek", "yasakli_kelimeler": ["hakaret", "hükümdar", "vatana ihanet", "suç", "yargılama"], "zorluk": "zor"},
    {"kelime": "interregnum yaşamak", "aciklama": "iki hükümdar arasında tahtın boş kaldığı ve iç savaşların sürdüğü fetret devri", "yasakli_kelimeler": ["fetret", "boşluk", "iç savaş", "taht", "dönem"], "zorluk": "zor"},
    {"kelime": "feodal beyleri tasfiye etmek", "aciklama": "merkezi krallık otoritesini güçlendirmek için yerel derebeylerin gücünü kırmak", "yasakli_kelimeler": ["merkeziyetçilik", "derebeyi", "feodalizm", "güç", "kral"], "zorluk": "zor"},
    {"kelime": "morganatik evlilik yapmak", "aciklama": "hükümdarın soylu olmayan biriyle evlenip çocuklarını taht mirasından men etmesi", "yasakli_kelimeler": ["halktan biri", "miras hakkı", "evlilik", "soylu olmayan", "unvan"], "zorluk": "zor"},
    {"kelime": "karantinaya almak", "aciklama": "şehzadeleri sarayda kafes arkasında gözetim altında tutarak isyanı engellemek", "yasakli_kelimeler": ["kafes sistemi", "şehzade", "tecrit", "saray", "gözetim"], "zorluk": "zor"},
    {"kelime": "magna cartayı imzalamak", "aciklama": "kralın mutlak yetkilerini soylular lehine kısıtlayan tarihi fermanı onaylamak", "yasakli_kelimeler": ["1215", "yurtsuz john", "soylular", "hak", "anayasal"], "zorluk": "zor"},
    {"kelime": "müsadere etmek", "aciklama": "ölen veya azledilen devlet adamının mal varlığına saray hazinesince el koyulması", "yasakli_kelimeler": ["el koyma", "hazine", "azil", "mal varlığı", "paşa"], "zorluk": "zor"},
    {"kelime": "mutlak monarşi kurmak", "aciklama": "tüm yasama, yürütme ve yargı yetkilerini tek bir hükümdarın şahsında toplamak", "yasakli_kelimeler": ["tek adam", "absolütizm", "yetki", "devlet benim", "louis"], "zorluk": "zor"}
]

if __name__ == "__main__":
    add_and_save_verbs("moda", moda_verbs)
    add_and_save_verbs("monarsi", monarsi_verbs)
