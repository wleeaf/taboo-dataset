import sys
from card_utils import add_and_save_verbs

# 1. TURKMUTFAGI (50 verbs: 12 kolay, 24 orta, 14 zor)
turkmutfagi_verbs = [
    # Kolay (12)
    {
        "kelime": "Çorba Kaynatmak",
        "aciklama": "Mercimek, tarhana veya yayla çorbasını tencerede pişirmek.",
        "yasakli_kelimeler": ["mercimek", "tarhana", "tencere", "sıcak", "kaşık"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Kebap Pişirmek",
        "aciklama": "Şişe dizilmiş etleri mangal kömürünün ateşinde közlemek.",
        "yasakli_kelimeler": ["mangal", "şiş", "et", "adana", "urfa"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Börek Açmak",
        "aciklama": "Hamuru incecik açıp peynirli veya kıymalı harçla tepside fırınlamak.",
        "yasakli_kelimeler": ["hamur", "yufka", "peynir", "kıyma", "fırın"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Pilav Demlemek",
        "aciklama": "Suyunu çeken pirinç pilavının üzerine havlu koyup dinlenmeye bırakmak.",
        "yasakli_kelimeler": ["pirinç", "tereyağı", "dinlendirmek", "tane tane", "su"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Dolma Doldurmak",
        "aciklama": "Biber veya patlıcanların içini pirinçli harçla doldurmak.",
        "yasakli_kelimeler": ["biber", "patlıcan", "harç", "pirinç", "tencere"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Sarma Sarmak",
        "aciklama": "Asma yaprağı veya lahana içine harç koyup incecik rulo yapmak.",
        "yasakli_kelimeler": ["asma yaprağı", "zeytinyağlı", "lahana", "rulo", "ince"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Köfte Yoğurmak",
        "aciklama": "Kıyma, soğan, ekmek içi ve baharatları el ile iyice karıştırmak.",
        "yasakli_kelimeler": ["kıyma", "soğan", "baharat", "el", "şekil"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Hamur Açmak",
        "aciklama": "Oklava veya merdane kullanarak hamuru yufka haline getirmek.",
        "yasakli_kelimeler": ["oklava", "merdane", "un", "yufka", "ince"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Salata Yapmak",
        "aciklama": "Domates, salatalık, yeşillik doğrayıp zeytinyağı ve limonla soslamak.",
        "yasakli_kelimeler": ["domates", "salatalık", "zeytinyağı", "limon", "çoban"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Ayran Çalkalamak",
        "aciklama": "Yoğurt, su ve tuzu karıştırıp köpüklü soğuk içecek hazırlamak.",
        "yasakli_kelimeler": ["yoğurt", "su", "tuz", "köpük", "içecek"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Yumurta Kırmak",
        "aciklama": "Tavaya veya menemene kabuğunu kırarak yumurta eklemek.",
        "yasakli_kelimeler": ["menemen", "tava", "kabuk", "sarısı", "beyazı"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Turşu Kurmak",
        "aciklama": "Salatalık, lahana veya biberleri sirkeli ve tuzlu suyla kavanoza basmak.",
        "yasakli_kelimeler": ["sirke", "tuzlu su", "kavanoz", "lahana", "ekşi"],
        "zorluk": "kolay"
    },

    # Orta (24)
    {
        "kelime": "Soğan Pembeleştirmek",
        "aciklama": "Yemek başlangıcında ince kıyılmış soğanları yağda rengi dönene kadar kavurmak.",
        "yasakli_kelimeler": ["yağ", "kavurmak", "kıyılmış", "renk", "başlangıç"],
        "zorluk": "orta"
    },
    {
        "kelime": "Salça Kavurmak",
        "aciklama": "Domates veya biber salçasının kokusu çıkana kadar yağda pişirmek.",
        "yasakli_kelimeler": ["domates salçası", "biber salçası", "koku", "yağ", "tencere"],
        "zorluk": "orta"
    },
    {
        "kelime": "Patlıcan Közlemek",
        "aciklama": "Patlıcanı ocak ateşinde veya fırında kabuğu yanana kadar yumuşatmak.",
        "yasakli_kelimeler": ["ocak", "ateş", "kabuk", "hünkarbeğendi", "ali nazik"],
        "zorluk": "orta"
    },
    {
        "kelime": "Tereyağı Yakmak",
        "aciklama": "Mantı veya çorbaların üzerine gezdirmek için pul biberli tereyağını tavada kızdırmak.",
        "yasakli_kelimeler": ["mantı", "pul biber", "tava", "sos", "kızdırmak"],
        "zorluk": "orta"
    },
    {
        "kelime": "Şerbet Kaynatmak",
        "aciklama": "Baklava veya kadayıf için su, şeker ve limon suyunu kıvam alana kadar kaynatmak.",
        "yasakli_kelimeler": ["şeker", "su", "limon", "baklava", "tatlı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Şerbet Dökmek",
        "aciklama": "Fırından çıkan sıcak tepsi tatlısına ılık şerbeti eşit olarak gezdirmek.",
        "yasakli_kelimeler": ["tatlı", "gezdirmek", "çekmek", "sıcak", "tepsi"],
        "zorluk": "orta"
    },
    {
        "kelime": "Yoğurt Mayalamak",
        "aciklama": "Ilık süte maya ekleyip üzerini bezle sararak pıhtılaşmaya bırakmak.",
        "yasakli_kelimeler": ["süt", "maya", "ılık", "tencere", "sarmak"],
        "zorluk": "orta"
    },
    {
        "kelime": "Mantı Kapatmak",
        "aciklama": "Kıymalı kare hamur parçalarını dört köşesinden birleştirerek bohça yapmak.",
        "yasakli_kelimeler": ["kayseri", "bohça", "kare", "kıyma", "hamur"],
        "zorluk": "orta"
    },
    {
        "kelime": "Tarhana Yoğurmak",
        "aciklama": "Yoğurt, domates, biber ve un karışımını fermente edip kurutmaya hazırlamak.",
        "yasakli_kelimeler": ["fermente", "un", "domates", "kurutmak", "kışlık"],
        "zorluk": "orta"
    },
    {
        "kelime": "Güvece Koymak",
        "aciklama": "Et ve sebzeleri toprak kapta fırına vererek ağır ağır pişirmek.",
        "yasakli_kelimeler": ["toprak kap", "fırın", "ağır ateş", "kuru fasulye", "et"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kavurma Yapmak",
        "aciklama": "Kurban etini kendi yağı ve tuzuyla tencerede suyunu çekene kadar pişirmek.",
        "yasakli_kelimeler": ["kurban", "kendi yağı", "kışlık", "dana", "kuzu"],
        "zorluk": "orta"
    },
    {
        "kelime": "Sulu Yemek Pişirmek",
        "aciklama": "Tencerede et, sebze, salça ve suyla kıvamlı ev yemeği hazırlamak.",
        "yasakli_kelimeler": ["tencere", "ev yemeği", "ekmek banmak", "sebze", "salçalı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Tandırda Pişirmek",
        "aciklama": "Kuzu etini veya ekmeği toprağa gömülü kuyu fırınının sıcaklığında nar gibi kızartmak.",
        "yasakli_kelimeler": ["kuyu", "kuzu", "fırın", "kızartmak", "lavaş"],
        "zorluk": "orta"
    },
    {
        "kelime": "Lokum Dökmek",
        "aciklama": "Şeker, nişasta ve aromaları kazanda kaynatıp tepsilere dökerek soğutmak.",
        "yasakli_kelimeler": ["nişasta", "şeker", "pudra şekeri", "kazan", "fıstık"],
        "zorluk": "orta"
    },
    {
        "kelime": "Cacık Yapmak",
        "aciklama": "Yoğurdu suyla inceltip içine doğranmış salatalık, sarımsak ve nane eklemek.",
        "yasakli_kelimeler": ["yoğurt", "salatalık", "sarımsak", "nane", "soğuk"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kısır Yoğurmak",
        "aciklama": "İnce bulguru sıcak suyla ıslatıp salça, nar ekşisi ve yeşilliklerle yoğurmak.",
        "yasakli_kelimeler": ["ince bulgur", "nar ekşisi", "yeşillik", "salça", "çay saati"],
        "zorluk": "orta"
    },
    {
        "kelime": "İç Harç Hazırlamak",
        "aciklama": "Börek, poğaça veya dolma içine konulacak malzemeleri karıştırmak.",
        "yasakli_kelimeler": ["dolma", "börek", "malzeme", "karışım", "kıyma"],
        "zorluk": "orta"
    },
    {
        "kelime": "Et Marine Etmek",
        "aciklama": "Eti yumuşatmak ve lezzetlendirmek için zeytinyağı, soğan suyu ve kekikte bekletmek.",
        "yasakli_kelimeler": ["kekik", "soğan suyu", "bekletmek", "yumuşatmak", "terbiye"],
        "zorluk": "orta"
    },
    {
        "kelime": "Baklava Tepsisi Dizmek",
        "aciklama": "Kırk kat ince yufkanın arasına ceviz veya fıstık serperek kat kat yerleştirmek.",
        "yasakli_kelimeler": ["fıstık", "ceviz", "yufka", "kat kat", "tepsi"],
        "zorluk": "orta"
    },
    {
        "kelime": "Meyhane Pilavı Yapmak",
        "aciklama": "Bulguru bol domates, biber ve soğanla salçalı pişirmek.",
        "yasakli_kelimeler": ["bulgur", "domates", "biber", "salçalı", "tencere"],
        "zorluk": "orta"
    },
    {
        "kelime": "Gözleme Pişirmek",
        "aciklama": "İnce açılmış yufka içine harç koyup sac üzerinde arkalı önlü kızartmak.",
        "yasakli_kelimeler": ["sac", "yufka", "ıspanaklı", "peynirli", "kızartmak"],
        "zorluk": "orta"
    },
    {
        "kelime": "Piyaz Yapmak",
        "aciklama": "Haşlanmış kuru fasulyeyi soğan, maydanoz, sumak ve tahinle karıştırmak.",
        "yasakli_kelimeler": ["kuru fasulye", "köfte yanı", "sumak", "tahin", "soğan"],
        "zorluk": "orta"
    },
    {
        "kelime": "Helva Kavurmak",
        "aciklama": "Un veya irmiği tereyağında kokusu çıkana kadar kavurup sıcak şerbetle buluşturmak.",
        "yasakli_kelimeler": ["un", "irmik", "tereyağı", "şerbet", "kandil"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kelle Paça Kaynatmak",
        "aciklama": "Sakatatları sarımsak, sirke ve terbiye ile saatlerce kısık ateşte pişirmek.",
        "yasakli_kelimeler": ["sakatat", "sarımsak", "sirke", "çorba", "terbiye"],
        "zorluk": "orta"
    },

    # Zor (14)
    {
        "kelime": "Terbiye Bağlamak",
        "aciklama": "Yumurta sarısı ve limon suyunu çorbanın sıcak suyuyla ılıtıp kesilmeden tencereye yedirmek.",
        "yasakli_kelimeler": ["yumurta sarısı", "limon suyu", "kesilmek", "ılıtmak", "düğün çorbası"],
        "zorluk": "zor"
    },
    {
        "kelime": "İçli Köfte Oymak",
        "aciklama": "Dış bulgur hamurunu parmak hareketiyle inceltip içini kıymalı harçla doldurarak kapatmak.",
        "yasakli_kelimeler": ["bulgur kabuğu", "parmak", "inceltmek", "cevizli kıyma", "şekil vermek"],
        "zorluk": "zor"
    },
    {
        "kelime": "Beşamel Sos Yapmak",
        "aciklama": "Tereyağında kavrulan una süt ekleyip çırparak muskatlı pürüzsüz kıvam elde etmek.",
        "yasakli_kelimeler": ["un kavurma", "süt", "muskat", "hünkarbeğendi", "çırpmak"],
        "zorluk": "zor"
    },
    {
        "kelime": "Hünkarbeğendi Hazırlamak",
        "aciklama": "Közlenmiş patlıcanlı beşamel sosu yatağına lokum gibi pişmiş kuzu eti döşemek.",
        "yasakli_kelimeler": ["patlıcan beğendi", "kuzu tas kebabı", "osmanlı", "saray", "yatak"],
        "zorluk": "zor"
    },
    {
        "kelime": "Baklava Yufkası Açmak",
        "aciklama": "Nişasta yardımıyla arkasından gazete okunacak şeffaflıkta mikron inceliğinde hamur açmak.",
        "yasakli_kelimeler": ["nişasta", "şeffaf", "tül gibi", "oklava", "incelik"],
        "zorluk": "zor"
    },
    {
        "kelime": "Zırhtan Geçirmek",
        "aciklama": "Kebap etini makinaya koymadan iki kulplu hilal bıçakla elde kıymak.",
        "yasakli_kelimeler": ["zırh bıçağı", "kuyruk yağı", "kebap eti", "kıymak", "satır"],
        "zorluk": "zor"
    },
    {
        "kelime": "Kelle Söğüş Yapmak",
        "aciklama": "Haşlanmış koyun kellesinin dil, beyin ve yanak etlerini baharatlayıp dürüme sarmak.",
        "yasakli_kelimeler": ["beyin", "yanak", "dil", "izmir", "dürüm"],
        "zorluk": "zor"
    },
    {
        "kelime": "Kokoreç Sarmak",
        "aciklama": "Şiş üzerine önce kuzu uykuluğu sonra metrelerce ince bağırsağı sıkıca dolamak.",
        "yasakli_kelimeler": ["bağırsak", "uykuluk", "şiş", "mangal", "kollamak"],
        "zorluk": "zor"
    },
    {
        "kelime": "Kazandibi Yakmak",
        "aciklama": "Muhallebinin altını pudra şekeri serpilmiş tepside kontrollü şekilde karamelize etmek.",
        "yasakli_kelimeler": ["karamelize", "tepsi altı", "muhallebi", "yanık lezzet", "pudra şekeri"],
        "zorluk": "zor"
    },
    {
        "kelime": "Aşure Bağlamak",
        "aciklama": "Kırk çeşit bakliyat, tahıl ve kuru meyveyi süt ve şekerle uyum içinde kıvamlandırmak.",
        "yasakli_kelimeler": ["buğday", "nohut", "incir", "nar", "muharrem"],
        "zorluk": "zor"
    },
    {
        "kelime": "Küşleme Ayıklamak",
        "aciklama": "Koyunun omurgasından çıkan sinirsiz ve en yumuşak bonfile parçasını çıkarmak.",
        "yasakli_kelimeler": ["sinirsiz", "koyun bonfile", "antep", "yumuşak et", "kebap"],
        "zorluk": "zor"
    },
    {
        "kelime": "Çiğ Köfte Yoğurmak",
        "aciklama": "Esmer bulgur, isot ve eti buzlu leğende saatlerce yoğurarak pişirmek.",
        "yasakli_kelimeler": ["isot", "leğen", "esmer bulgur", "urfa", "etsiz"],
        "zorluk": "zor"
    },
    {
        "kelime": "Zeytinyağlı Çektirmek",
        "aciklama": "Enginar veya kerevizi portakal suyu, zeytinyağı ve şekerle kısık ateşte suyunu çektirmek.",
        "yasakli_kelimeler": ["enginar", "kısık ateş", "portakal suyu", "soğuk servis", "şeker"],
        "zorluk": "zor"
    },
    {
        "kelime": "Sütlaç Fırınlamak",
        "aciklama": "Toprak güveçlerdeki sütlacın üstünü fırının üst ızgarasında nar gibi yakmak.",
        "yasakli_kelimeler": ["fırın sütlaç", "toprak kase", "üst ızgara", "yanık yüzey", "pirinç"],
        "zorluk": "zor"
    }
]

# 2. ULASIM (50 verbs: 12 kolay, 24 orta, 14 zor)
ulasim_verbs = [
    # Kolay (12)
    {
        "kelime": "Otobüse Binmek",
        "aciklama": "Toplu taşıma aracına duraktan adım atıp kart basmak.",
        "yasakli_kelimeler": ["durak", "kart", "yolcu", "şoför", "inmek"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Taksiye Binmek",
        "aciklama": "Yoldan taksi çevirip istenen adrese gitmek.",
        "yasakli_kelimeler": ["şoför", "taksimetre", "sarı", "adres", "durak"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Metroya Binmek",
        "aciklama": "Yeraltı raylı taşıma hattını kullanarak istasyonlar arasında seyahat etmek.",
        "yasakli_kelimeler": ["istasyon", "ray", "yeraltı", "tren", "turnike"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Uçağa Binmek",
        "aciklama": "Havalimanında biniş kapısından geçip uçağa oturmak.",
        "yasakli_kelimeler": ["havalimanı", "boarding", "kapı", "koltuk", "uçuş"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Vapura Binmek",
        "aciklama": "İskeleden şehir hatları deniz motoru veya gemisine binmek.",
        "yasakli_kelimeler": ["iskele", "deniz", "gemi", "martı", "boğaz"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Bisiklet Sürmek",
        "aciklama": "İki tekerlekli pedalsız/pedallı taşıtla yolda ilerlemek.",
        "yasakli_kelimeler": ["pedal", "tekerlek", "gidon", "kask", "yol"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Bilet Almak",
        "aciklama": "Seyahat edebilmek için gişeden veya internetten geçiş hakkı edinmek.",
        "yasakli_kelimeler": ["gişe", "kart", "ücret", "koltuk", "rezervasyon"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Durakta Beklemek",
        "aciklama": "Gelecek otobüs veya minibüs için kaldırım kenarındaki durakta beklemek.",
        "yasakli_kelimeler": ["otobüs", "minibüs", "kaldırım", "yolcu", "vakit"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Yol Tarifi Almak",
        "aciklama": "Bilinmeyen bir yere giderken navigasyondan veya birinden yön sormak.",
        "yasakli_kelimeler": ["navigasyon", "adres", "sormak", "harita", "yön"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Gaza Basmak",
        "aciklama": "Aracın hızlanması için ayak pedalına kuvvet uygulamak.",
        "yasakli_kelimeler": ["pedal", "hız", "motor", "ayak", "ivme"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Frene Basmak",
        "aciklama": "Hareket halindeki aracı durdurmak veya yavaşlatmak için pedala basmak.",
        "yasakli_kelimeler": ["durdurmak", "yavaşlamak", "pedal", "balata", "araç"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Direksiyon Çevirmek",
        "aciklama": "Aracın tekerleklerine yön vererek dönüş yapmak.",
        "yasakli_kelimeler": ["dönüş", "sağ", "sol", "simit", "yönlendirmek"],
        "zorluk": "kolay"
    },

    # Orta (24)
    {
        "kelime": "Aktarma Yapmak",
        "aciklama": "Bir toplu taşıma hattından inip diğerine geçiş yaparak yola devam etmek.",
        "yasakli_kelimeler": ["hat", "inmek", "geçiş", "indirim", "istasyon"],
        "zorluk": "orta"
    },
    {
        "kelime": "Turnikeden Geçmek",
        "aciklama": "İstanbulkart veya bilet okutarak istasyon giriş bariyerini açmak.",
        "yasakli_kelimeler": ["kart", "okutmak", "bariyer", "geçiş", "istasyon"],
        "zorluk": "orta"
    },
    {
        "kelime": "Trafiğe Takılmak",
        "aciklama": "Yoldaki yoğun araç kalabalığı sebebiyle dur-kalk ilerlemek.",
        "yasakli_kelimeler": ["yoğunluk", "dur kalk", "sıkışıklık", "kilit", "zaman kaybı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Navigasyon Kurmak",
        "aciklama": "Gidilecek rota ve canlı trafik durumunu görmek için GPS uygulamasını açmak.",
        "yasakli_kelimeler": ["gps", "rota", "harita", "canlı trafik", "uygulama"],
        "zorluk": "orta"
    },
    {
        "kelime": "Şerit Değiştirmek",
        "aciklama": "Otoyolda sinyal vererek yanındaki trafik şeridine geçiş yapmak.",
        "yasakli_kelimeler": ["sinyal", "ayna", "otoyol", "geçiş", "çizgi"],
        "zorluk": "orta"
    },
    {
        "kelime": "Sinyal Vermek",
        "aciklama": "Dönüş veya şerit değişimi öncesinde yanıp sönen ikaz ışığını yakmak.",
        "yasakli_kelimeler": ["kol", "ışık", "sağ", "sol", "ikaz"],
        "zorluk": "orta"
    },
    {
        "kelime": "Geri Park Etmek",
        "aciklama": "Aracı iki araç arasındaki boşluğa geri vitese takarak yerleştirmek.",
        "yasakli_kelimeler": ["geri vites", "kaldırım", "ayna", "iki araç arası", "boşluk"],
        "zorluk": "orta"
    },
    {
        "kelime": "Akbil Doldurmak",
        "aciklama": "Toplu ulaşım kartına biletmatik veya internetten bakiye yüklemek.",
        "yasakli_kelimeler": ["bakiye", "yüklemek", "biletmatik", "para", "ulaşım kartı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Check-in Yapmak",
        "aciklama": "Uçuş öncesinde bilet ve koltuk numarasını onaylatıp biniş kartı almak.",
        "yasakli_kelimeler": ["koltuk", "uçuş", "biniş kartı", "onay", "kontuar"],
        "zorluk": "orta"
    },
    {
        "kelime": "Bavul Teslim Etmek",
        "aciklama": "Havalimanında ağır valizleri uçağın kargo bölümüne verilmek üzere kontuara bırakmak.",
        "yasakli_kelimeler": ["valiz", "bagaj", "kontuar", "kargo", "tartı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Hız Sabitleyiciyi Açmak",
        "aciklama": "Uzun yolda aracın hızını belirli bir kilometrede sabit tutan cruise controlü çalıştırmak.",
        "yasakli_kelimeler": ["cruise control", "uzun yol", "sabit", "km/h", "otoban"],
        "zorluk": "orta"
    },
    {
        "kelime": "Korna Çalmak",
        "aciklama": "Trafikteki diğer sürücüleri veya yayaları uyarmak için sesli ikaz vermek.",
        "yasakli_kelimeler": ["ses", "uyarı", "direksiyon", "gürültü", "ikaz"],
        "zorluk": "orta"
    },
    {
        "kelime": "Emniyet Kemeri Takmak",
        "aciklama": "Kaza anında güvenliği sağlamak için koltuk kemerini tokaya kilitlemek.",
        "yasakli_kelimeler": ["kaza", "güvenlik", "koltuk", "kilit", "toka"],
        "zorluk": "orta"
    },
    {
        "kelime": "Geçiş Ücreti Ödemek",
        "aciklama": "Köprü ve otoyollardan geçerken HGS veya OGS sisteminden ücret ödemek.",
        "yasakli_kelimeler": ["hgs", "ogs", "köprü", "otoyol", "gişe"],
        "zorluk": "orta"
    },
    {
        "kelime": "Yolcu İndirmek",
        "aciklama": "Aracı sağa çekip içindeki yolcunun inmesine izin vermek.",
        "yasakli_kelimeler": ["sağa çekmek", "kapı", "durmak", "taksi", "minibüs"],
        "zorluk": "orta"
    },
    {
        "kelime": "Yakıt Almak",
        "aciklama": "Benzinlikte aracın deposunu benzin, mazot veya LPG ile doldurmak.",
        "yasakli_kelimeler": ["benzin", "mazot", "pompa", "istasyon", "depo"],
        "zorluk": "orta"
    },
    {
        "kelime": "Taksi Çevirmek",
        "aciklama": "Yolda el kaldırarak boş taksiyi durdurmak.",
        "yasakli_kelimeler": ["el kaldırmak", "sarı", "durdurmak", "boş", "yol kenarı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Vites Değiştirmek",
        "aciklama": "Aracın motor devrine göre debriyaja basıp kolu uygun dişliye geçirmek.",
        "yasakli_kelimeler": ["debriyaj", "kol", "dişli", "motor devri", "manuel"],
        "zorluk": "orta"
    },
    {
        "kelime": "Rötar Yapmak",
        "aciklama": "Uçak veya trenin planlanan saatten daha geç hareket etmesi.",
        "yasakli_kelimeler": ["gecikme", "saat", "uçuş", "bekleme", "iptal"],
        "zorluk": "orta"
    },
    {
        "kelime": "İskeleden Palamar Çözmek",
        "aciklama": "Vapur veya teknenin hareket etmesi için bağlama halatlarını serbest bırakmak.",
        "yasakli_kelimeler": ["halat", "tekne", "vapur", "bağlantı", "deniz"],
        "zorluk": "orta"
    },
    {
        "kelime": "Valiz Bandından Almak",
        "aciklama": "Uçaktan indikten sonra bagaj teslim salonunda dönen konveyörden bavulunu almak.",
        "yasakli_kelimeler": ["konveyör", "bagaj", "teslim", "dönen bant", "havalimanı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Dörtlüleri Yakmak",
        "aciklama": "Acil durumlarda veya kısa duraklamalarda dört flaşörü birden çalıştırmak.",
        "yasakli_kelimeler": ["flaşör", "acil", "arıza", "duraklama", "ikaz"],
        "zorluk": "orta"
    },
    {
        "kelime": "Otostop Çekmek",
        "aciklama": "Yol kenarında başparmak kaldırarak geçen araçlardan ücretsiz ulaşım istemek.",
        "yasakli_kelimeler": ["başparmak", "ücretsiz", "yol kenarı", "araç", "seyahat"],
        "zorluk": "orta"
    },
    {
        "kelime": "Raydan Gitmek",
        "aciklama": "Tren, tramvay veya metronun demiryolu hattı üzerinde ilerlemesi.",
        "yasakli_kelimeler": ["demiryolu", "makas", "tren", "tramvay", "lokomotif"],
        "zorluk": "orta"
    },

    # Zor (14)
    {
        "kelime": "Uçuş Planı Dosyalamak",
        "aciklama": "Pilotun kalkış öncesi rota, irtifa, yedek meydan ve yakıt bilgilerini kuleye bildirmesi.",
        "yasakli_kelimeler": ["pilot", "irtifa", "hava trafik kontrol", "rota", "meydan"],
        "zorluk": "zor"
    },
    {
        "kelime": "Slot Sırası Beklemek",
        "aciklama": "Yoğun havalimanlarında kalkış veya iniş için hava trafik kontrolünden tahsis edilen zaman aralığını beklemek.",
        "yasakli_kelimeler": ["havaalanı", "pist", "kalkış sırası", "atc", "zaman aralığı"],
        "zorluk": "zor"
    },
    {
        "kelime": "Makas Değiştirmek",
        "aciklama": "Demiryolunda trenin bir ray hattından diğerine yönlenmesini sağlayan mekanizmayı işletmek.",
        "yasakli_kelimeler": ["ray", "tren", "hat", "yönlendirme", "demiryolu"],
        "zorluk": "zor"
    },
    {
        "kelime": "ILS Yaklaşması Yapmak",
        "aciklama": "Uçağın sisli veya gece koşullarında pist başına aletli iniş sistemi radyo sinyalleriyle alçalması.",
        "yasakli_kelimeler": ["aletli iniş", "pist", "sis", "alçalma", "glideslope"],
        "zorluk": "zor"
    },
    {
        "kelime": "Palamar Bağlamak",
        "aciklama": "Büyük gemi ve feribotları liman babalarına çelik halatlarla sabitlemek.",
        "yasakli_kelimeler": ["halat", "liman babası", "feribot", "sabitlemek", "rıhtım"],
        "zorluk": "zor"
    },
    {
        "kelime": "Diferansiyel Kilitlemek",
        "aciklama": "Arazi araçlarında çamura veya kara saplanınca her iki tekerleğe eşit tork aktarmak.",
        "yasakli_kelimeler": ["4x4", "off-road", "tork", "çekiş", "saplanmak"],
        "zorluk": "zor"
    },
    {
        "kelime": "Sinyalizasyon Kurmak",
        "aciklama": "Demiryolu ve otoyol güvenliği için otomatik tren durdurma ve elektronik ışık sistemini entegre etmek.",
        "yasakli_kelimeler": ["elektronik", "otomatik tren koruma", "ışık", "emniyet", "blok"],
        "zorluk": "zor"
    },
    {
        "kelime": "Geniş Gövdeli Uçak İndirmek",
        "aciklama": "Çift koridorlu ve yüzlerce yolcu taşıyan dev yolcu uçağını piste teker koydurmak.",
        "yasakli_kelimeler": ["kıtalararası", "boeing 777", "airbus a350", "pist", "teker koyma"],
        "zorluk": "zor"
    },
    {
        "kelime": "Kombine Taşımacılık Yapmak",
        "aciklama": "Yük konteynerlerini gemi, tren ve tır arasında yükü açmadan aktararak taşımak (intermodal).",
        "yasakli_kelimeler": ["intermodal", "konteyner", "tır", "tren", "aktarma limanı"],
        "zorluk": "zor"
    },
    {
        "kelime": "Takograf Kontrolü Yapmak",
        "aciklama": "Kamyon ve otobüs şoförlerinin sürüş süresi ve hız limitlerini kaydeden cihazı denetlemek.",
        "yasakli_kelimeler": ["cihaz", "sürüş süresi", "şoför dinlenmesi", "kamyon", "polis"],
        "zorluk": "zor"
    },
    {
        "kelime": "Metrobüs Hattını İşletmek",
        "aciklama": "Ayrılmış özel şeritte yüksek yolcu kapasitesiyle çalışan lastik tekerlekli toplu taşıma sistemini yönetmek.",
        "yasakli_kelimeler": ["özel şerit", "yoğunluk", "e-5", "kapasite", "durak"],
        "zorluk": "zor"
    },
    {
        "kelime": "Kılavuz Kaptan Almak",
        "aciklama": "Boğaz ve liman geçişlerinde gemiyi dar sularda emniyetle sevk etmek için yerel uzman kaptanı gemiye çıkarmak.",
        "yasakli_kelimeler": ["boğaz", "dar su", "liman", "uzman", "çarmıh"],
        "zorluk": "zor"
    },
    {
        "kelime": "Taksimetre Kalibre Etmek",
        "aciklama": "Mesafe ve zamana göre ücret hesaplayan cihazın yasal ölçüm ayarlarını mühürlemek.",
        "yasakli_kelimeler": ["ücret", "mesafe", "mühür", "kalibrasyon", "ayar"],
        "zorluk": "zor"
    },
    {
        "kelime": "Trafik Sirkülasyonunu Modellemek",
        "aciklama": "Şehir içi kavşak ve anayollardaki araç akışını bilgisayar simülasyonlarıyla optimize etmek.",
        "yasakli_kelimeler": ["simülasyon", "araç akışı", "kavşak", "optimizasyon", "darboğaz"],
        "zorluk": "zor"
    }
]

if __name__ == "__main__":
    add_and_save_verbs("turkmutfagi", turkmutfagi_verbs)
    add_and_save_verbs("ulasim", ulasim_verbs)
