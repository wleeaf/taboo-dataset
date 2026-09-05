import sys
from card_utils import add_and_save_verbs

# 1. VAHSIDOGA (50 verbs: 12 kolay, 24 orta, 14 zor)
vahsidoga_verbs = [
    # Kolay (12)
    {
        "kelime": "Avlanmak",
        "aciklama": "Yırtıcı hayvanın karnını doyurmak için başka bir canlıyı yakalaması.",
        "yasakli_kelimeler": ["yırtıcı", "yakalamak", "av", "beslenmek", "orman"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Kükremek",
        "aciklama": "Aslan veya kaplan gibi büyük kedilerin alan belirlemek için çıkardığı gür ses.",
        "yasakli_kelimeler": ["aslan", "kaplan", "ses", "bağırmak", "korkutmak"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Ulumak",
        "aciklama": "Kurt veya çakalların sürüyle iletişim kurmak için aya karşı çıkardığı uzun ses.",
        "yasakli_kelimeler": ["kurt", "çakal", "dolunay", "ses", "sürü"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Pusuya Yatmak",
        "aciklama": "Avcı hayvanın çalılar arkasında gizlenip avın yaklaşmasını beklemesi.",
        "yasakli_kelimeler": ["gizlenmek", "çalı", "beklemek", "av", "saldırı"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Kaçmak",
        "aciklama": "Otçul bir hayvanın yırtıcı saldırısından canını kurtarmak için hızla uzaklaşması.",
        "yasakli_kelimeler": ["avcı", "korku", "hızlı", "koşmak", "kurtulmak"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Yuva Yapmak",
        "aciklama": "Kuş veya memelilerin yavrularını büyütmek için dal ve yapraklardan barınak kurması.",
        "yasakli_kelimeler": ["barınak", "kuş", "yavru", "dal", "yaprak"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Göç Etmek",
        "aciklama": "Hayvan sürülerinin mevsimsel olarak sıcak bölgelere veya otlaklara yolculuğu.",
        "yasakli_kelimeler": ["mevsim", "yolculuk", "sürü", "kuşlar", "sıcak"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Kış Uykusuna Yatmak",
        "aciklama": "Ayı veya sürüngenlerin soğuk kış aylarını mağarada uyuyarak geçirmesi.",
        "yasakli_kelimeler": ["ayı", "uyku", "kış", "soğuk", "mağara"],
        "zorluk": "kolay"
    },
    {
        "kelime": "İz Sürmek",
        "aciklama": "Avcı hayvanın yerdeki koku ve ayak izlerini takip ederek avını bulması.",
        "yasakli_kelimeler": ["ayak izi", "koku", "takip", "bulmak", "toprak"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Tırmanmak",
        "aciklama": "Leopar veya sincap gibi canlıların ağaç gövdesinde yukarı doğru çıkması.",
        "yasakli_kelimeler": ["ağaç", "pençe", "yukarı", "dal", "leopar"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Saldırmak",
        "aciklama": "Yırtıcının avına doğru hamle yaparak pençe ve dişleriyle etkisiz hale getirmesi.",
        "yasakli_kelimeler": ["hamle", "pençe", "diş", "av", "ısırmak"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Tıslamak",
        "aciklama": "Yılan veya sürüngenlerin tehdit altındayken düşmanı korkutmak için çıkardığı ses.",
        "yasakli_kelimeler": ["yılan", "ses", "tehdit", "korkutmak", "zehir"],
        "zorluk": "kolay"
    },

    # Orta (24)
    {
        "kelime": "Kamuflaj Olmak",
        "aciklama": "Canlının desen ve rengiyle doğal çevreye uyum sağlayarak görünmez hale gelmesi.",
        "yasakli_kelimeler": ["çevre", "renk", "görünmez", "saklanmak", "bukalemun"],
        "zorluk": "orta"
    },
    {
        "kelime": "Sürü Halinde Gezmek",
        "aciklama": "Bizon, antilop veya zebraların yırtıcılara karşı korunmak için toplu hareket etmesi.",
        "yasakli_kelimeler": ["toplu", "antilop", "zebra", "korunma", "birlikte"],
        "zorluk": "orta"
    },
    {
        "kelime": "Bölge İşaretlemek",
        "aciklama": "Büyük etoburların ağaçlara koku bırakarak veya tırmalayarak sınır belirlemesi.",
        "yasakli_kelimeler": ["sınır", "koku", "tırmalamak", "alan", "ağaç"],
        "zorluk": "orta"
    },
    {
        "kelime": "Liderlik Mücadelesi Vermek",
        "aciklama": "Sürüdeki erkek bireylerin alfa konumu için boynuz veya pençeyle dövüşmesi.",
        "yasakli_kelimeler": ["alfa", "erkek", "boynuz", "dövüş", "üstünlük"],
        "zorluk": "orta"
    },
    {
        "kelime": "Zehir Salgılamak",
        "aciklama": "Yılan, akrep veya örümceğin avını felç etmek için toksin enjekte etmesi.",
        "yasakli_kelimeler": ["toksin", "felç", "akrep", "yılan", "ısırmak"],
        "zorluk": "orta"
    },
    {
        "kelime": "Leş Yemek",
        "aciklama": "Sırtlan veya akbabaların diğer avcıların bıraktığı ölü hayvan kalıntılarıyla beslenmesi.",
        "yasakli_kelimeler": ["akbaba", "sırtlan", "ölü hayvan", "kalıntı", "et"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kur Yapmak",
        "aciklama": "Erkek kuşların veya canlıların eş bulmak için renkli danslar ve gösteriler yapması.",
        "yasakli_kelimeler": ["dans", "çiftleşme", "tavus kuşu", "eş", "gösteri"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kabuk Değiştirmek",
        "aciklama": "Büyüyen yılan veya eklembacaklının eskiyen dış derisini/kabuğunu sıyırması.",
        "yasakli_kelimeler": ["deri", "gömlek bırakma", "yılan", "büyüme", "sıyırmak"],
        "zorluk": "orta"
    },
    {
        "kelime": "Otlatmak",
        "aciklama": "Geniş savanalarda otçul hayvanların çimen ve yaprakları tüketmesi.",
        "yasakli_kelimeler": ["savana", "çimen", "otçul", "yaprak", "beslenme"],
        "zorluk": "orta"
    },
    {
        "kelime": "Süzülerek Uçmak",
        "aciklama": "Kartal veya şahinin kanat çırpmadan sıcak hava termallerinde yükselmesi.",
        "yasakli_kelimeler": ["kartal", "kanat çırpmadan", "termal", "hava akımı", "yüksek"],
        "zorluk": "orta"
    },
    {
        "kelime": "Gözcü Dikmek",
        "aciklama": "Mirketlerin veya dağ keçilerinin sürü beslenirken tehlikeye karşı nöbetçi bırakması.",
        "yasakli_kelimeler": ["mirket", "nöbet", "tehlike", "uyarı", "sürü"],
        "zorluk": "orta"
    },
    {
        "kelime": "Tehlike Sinyali Vermek",
        "aciklama": "Avcı gören bir hayvanın ses veya kuyruk hareketiyle tüm grubu uyarması.",
        "yasakli_kelimeler": ["uyarı", "ses", "kuyruk", "kaçış", "grup"],
        "zorluk": "orta"
    },
    {
        "kelime": "Su Başına İnmek",
        "aciklama": "Kurak mevsimde hayvanların su birikintisi veya gölet etrafında toplanması.",
        "yasakli_kelimeler": ["gölet", "kuraklık", "içmek", "toplanma", "nehir"],
        "zorluk": "orta"
    },
    {
        "kelime": "Pençe Bilemek",
        "aciklama": "Kedigillerin tırnaklarını ağaç gövdesine sürterek keskinleştirmesi.",
        "yasakli_kelimeler": ["tırnak", "ağaç gövdesi", "keskin", "sürtmek", "kedi"],
        "zorluk": "orta"
    },
    {
        "kelime": "Tüy Dökmek",
        "aciklama": "Mevsim geçişlerinde hayvanların kışlık veya yazlık kürk/tüy yapısına geçmesi.",
        "yasakli_kelimeler": ["kürk", "mevsim geçişi", "yenilenme", "yazlık", "kışlık"],
        "zorluk": "orta"
    },
    {
        "kelime": "Toprağı Eşelemek",
        "aciklama": "Yaban domuzu veya porsuğun toprak altındaki kök ve kurtçukları aramak için yeri kazması.",
        "yasakli_kelimeler": ["kazmak", "yaban domuzu", "kök", "kurtçuk", "burun"],
        "zorluk": "orta"
    },
    {
        "kelime": "Koku Almak",
        "aciklama": "Rüzgarın getirdiği zerreleri burnuyla koklayarak avın veya avcının yerini sezmek.",
        "yasakli_kelimeler": ["burun", "sezmek", "rüzgar", "avcı", "mesafe"],
        "zorluk": "orta"
    },
    {
        "kelime": "Yavrusunu Korumak",
        "aciklama": "Anne hayvanın yırtıcılara karşı hayatını tehlikeye atarak yavrusunu savunması.",
        "yasakli_kelimeler": ["anne", "savunma", "fedakarlık", "yırtıcı", "içgüdü"],
        "zorluk": "orta"
    },
    {
        "kelime": "Baraj İnşa Etmek",
        "aciklama": "Kunduzların akarsu üzerine dallar ve çamurla su bendi kurması.",
        "yasakli_kelimeler": ["kunduz", "akarsu", "dal", "çamur", "bent"],
        "zorluk": "orta"
    },
    {
        "kelime": "Körfezde Dalış Yapmak",
        "aciklama": "Pelikan veya yalıçapkınının balık yakalamak için havadan suya dik dalması.",
        "yasakli_kelimeler": ["balık", "suya dalış", "havadan", "gaga", "av"],
        "zorluk": "orta"
    },
    {
        "kelime": "Yere Yapışmak",
        "aciklama": "Geyik yavrusunun yırtıcı gördüğünde otların arasında hareketsizce sinmesi.",
        "yasakli_kelimeler": ["sinmek", "hareketsiz", "otlar", "kamuflaj", "yavru"],
        "zorluk": "orta"
    },
    {
        "kelime": "Ot Dolaşmak",
        "aciklama": "Zürafaların uzun boyunlarıyla yüksek akasya ağaçlarının yapraklarını yemesi.",
        "yasakli_kelimeler": ["zürafa", "akasya", "yüksek", "uzun boyun", "yaprak"],
        "zorluk": "orta"
    },
    {
        "kelime": "Çamura Bulanmak",
        "aciklama": "Fil veya su aygırlarının parazitlerden ve güneşten korunmak için çamur banyosu yapması.",
        "yasakli_kelimeler": ["fil", "su aygırı", "parazit", "güneş", "serinleme"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kemik Kırmak",
        "aciklama": "Sırtlanın güçlü çenesiyle avın ilikli kemiklerini parçalaması.",
        "yasakli_kelimeler": ["sırtlan", "çene", "parçalamak", "ilik", "kuvvet"],
        "zorluk": "orta"
    },

    # Zor (14)
    {
        "kelime": "Ekolokasyon Kullanmak",
        "aciklama": "Yarasa veya yunusların yüksek frekanslı ses dalgalarının yankısıyla yön ve av bulması.",
        "yasakli_kelimeler": ["yankı", "ses dalgası", "yarasa", "sonar", "frekans"],
        "zorluk": "zor"
    },
    {
        "kelime": "Miyasis Oluşturmak",
        "aciklama": "Bazı sinek türlerinin vahşi hayvan dokuları içine larva bırakarak parazitlik yapması.",
        "yasakli_kelimeler": ["larva", "sinek", "doku", "parazit", "enfeksiyon"],
        "zorluk": "zor"
    },
    {
        "kelime": "Aposematizm Sergilemek",
        "aciklama": "Zehirli kurbağa veya böceklerin yırtıcıları uyarmak için parlak ve göz alıcı renkler taşıması.",
        "yasakli_kelimeler": ["uyarıcı renk", "zehir", "parlak", "yırtıcı caydırma", "kurbağa"],
        "zorluk": "zor"
    },
    {
        "kelime": "Batesian Taklidi Yapmak",
        "aciklama": "Zararsız bir türün zehirli veya tehlikeli başka bir türün desenlerini kopyalayarak korunması.",
        "yasakli_kelimeler": ["taklit", "mimikri", "zehirli gibi", "kopyalama", "zararsız"],
        "zorluk": "zor"
    },
    {
        "kelime": "Torpor Durumuna Geçmek",
        "aciklama": "Sinek kuşu veya küçük memelilerin geceleri vücut sıcaklığı ve metabolizmasını geçici düşürmesi.",
        "yasakli_kelimeler": ["metabolizma", "kısa kış uykusu", "enerji tasarrufu", "vücut ısısı", "gecelik"],
        "zorluk": "zor"
    },
    {
        "kelime": "Simbiotik Yaşamak",
        "aciklama": "Gergedan ile parazit yiyen kürdan kuşu gibi iki farklı türün karşılıklı fayda içinde yaşaması.",
        "yasakli_kelimeler": ["karşılıklı fayda", "mutualizm", "ortak yaşam", "parazit kuşu", "gergedan"],
        "zorluk": "zor"
    },
    {
        "kelime": "Trofik Kademeyi Değiştirmek",
        "aciklama": "Tepe avcısının ortadan kalkması veya geri gelmesiyle tüm ekosistem dengesinin yeniden şekillenmesi.",
        "yasakli_kelimeler": ["trofik kaskad", "tepe avcısı", "ekosistem dengesi", "kurtlar", "besin zinciri"],
        "zorluk": "zor"
    },
    {
        "kelime": "Biyolüminesans Yaymak",
        "aciklama": "Derin deniz canlılarının veya ateş böceklerinin kimyasal tepkimeyle soğuk ışık üretmesi.",
        "yasakli_kelimeler": ["kimyasal ışık", "ateş böceği", "derin deniz", "lüsiferin", "parlama"],
        "zorluk": "zor"
    },
    {
        "kelime": "Tepkisel Otonomi Yapmak",
        "aciklama": "Kertenkelenin yakalandığında yırtıcıyı şaşırtmak için kuyruğunu kendi isteğiyle koparması.",
        "yasakli_kelimeler": ["kuyruk kopması", "ototomi", "kertenkele", "şaşırtma", "koparmak"],
        "zorluk": "zor"
    },
    {
        "kelime": "Manyetik Alanla Yön Bulmak",
        "aciklama": "Deniz kaplumbağaları veya göçmen kuşların dünyanın manyetik çizgilerini pusula gibi kullanması.",
        "yasakli_kelimeler": ["manyetoreseptör", "dünya manyetik alanı", "pusula", "kaplumbağa", "göç rotası"],
        "zorluk": "zor"
    },
    {
        "kelime": "Thanatosis Numarası Yapmak",
        "aciklama": "Opossum veya yılanların avcının ilgisini kaybetmesi için ölü taklidi yapması.",
        "yasakli_kelimeler": ["ölü taklidi", "hareketsiz kalma", "opossum", "koku salma", "savunma"],
        "zorluk": "zor"
    },
    {
        "kelime": "Feromon İzi Bırakmak",
        "aciklama": "Karıncaların besin kaynağına giden yolu diğer işçilere bildirmek için kimyasal koku bırakması.",
        "yasakli_kelimeler": ["karınca", "kimyasal iz", "besin yolu", "koku sinyali", "koloni"],
        "zorluk": "zor"
    },
    {
        "kelime": "Partenogenezle Üremek",
        "aciklama": "Komodo ejderi veya bazı sürüngenlerin döllenme olmadan yumurtadan yavru çıkarması.",
        "yasakli_kelimeler": ["döllenmesiz", "eşeysiz", "komodo ejderi", "klonlama", "dişi"],
        "zorluk": "zor"
    },
    {
        "kelime": "İmprinting Geliştirmek",
        "aciklama": "Yumurtadan çıkan yavru kazların gördüğü ilk hareketli canlıyı ebeveyni olarak bağlaması.",
        "yasakli_kelimeler": ["bağlanma", "lorenz", "kaz yavrusu", "ilk görülen", "ebeveyn"],
        "zorluk": "zor"
    }
]

# 2. VIDEOOYUNLARI (50 verbs: 12 kolay, 24 orta, 14 zor)
videooyunlari_verbs = [
    # Kolay (12)
    {
        "kelime": "Oyunu Başlatmak",
        "aciklama": "Ana menüden 'Başla' butonuna basarak video oyununa girmek.",
        "yasakli_kelimeler": ["ana menü", "start", "buton", "oyun", "giriş"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Karakter Seçmek",
        "aciklama": "Oyuna başlamadan önce yönetilecek kahramanı veya sınıfı belirlemek.",
        "yasakli_kelimeler": ["kahraman", "sınıf", "seçim", "avatar", "liste"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Tuşlara Basmak",
        "aciklama": "Klavye, gamepad veya fare butonlarına basarak karakteri hareket ettirmek.",
        "yasakli_kelimeler": ["klavye", "gamepad", "kol", "fare", "buton"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Zıplamak",
        "aciklama": "Platform oyunlarında engelleri aşmak için boşluk tuşuna basıp havalanmak.",
        "yasakli_kelimeler": ["boşluk", "space", "engel", "hava", "platform"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Ateş Etmek",
        "aciklama": "Silahlı aksiyon oyunlarında sol tıkla düşman hedeflere mermi sıkmak.",
        "yasakli_kelimeler": ["mermi", "silah", "sol tık", "düşman", "hedef"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Bölüm Geçmek",
        "aciklama": "Mevcut etabın görevlerini tamamlayıp bir sonraki seviyeye ulaşmak.",
        "yasakli_kelimeler": ["seviye", "etap", "level", "tamamlamak", "sonraki"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Can Doldurmak",
        "aciklama": "Sağlık paketi veya iksir kullanarak azalan sağlık barını artırmak.",
        "yasakli_kelimeler": ["sağlık", "hp", "iksir", "medkit", "bar"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Oyunu Kaydetmek",
        "aciklama": "İlerlemeyi kaybetmemek için kayıt noktasına gelip oyunu save etmek.",
        "yasakli_kelimeler": ["save", "ilerleme", "kayıt noktası", "hafıza", "checkpoint"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Kazanmak",
        "aciklama": "Maçın veya oyunun sonunda rakibi yenerek zafere ulaşmak.",
        "yasakli_kelimeler": ["zafer", "victory", "yenmek", "skor", "şampiyon"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Kaybetmek",
        "aciklama": "Tüm can hakları bitince 'Game Over' ekranıyla karşılaşmak.",
        "yasakli_kelimeler": ["game over", "ölmek", "yenilgi", "can hakkı", "bitmek"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Çevrimiçi Oynamak",
        "aciklama": "İnternet üzerinden diğer gerçek oyuncularla çok oyunculu maç yapmak.",
        "yasakli_kelimeler": ["internet", "multiplayer", "online", "sunucu", "diğer oyuncular"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Kulaklık Takmak",
        "aciklama": "Oyun seslerini ve takım arkadaşlarının sesli sohbetini duymak için kulaklık takmak.",
        "yasakli_kelimeler": ["ses", "mikrofon", "discord", "duymak", "kulak"],
        "zorluk": "kolay"
    },

    # Orta (24)
    {
        "kelime": "Boss Kesmek",
        "aciklama": "Bölüm sonundaki devasa ve güçlü ana düşmanı yenmek.",
        "yasakli_kelimeler": ["bölüm sonu canavarı", "ana düşman", "büyük canavar", "yenmek", "loot"],
        "zorluk": "orta"
    },
    {
        "kelime": "Seviye Atlamak",
        "aciklama": "Yeterli tecrübe puanı (XP) toplayarak karakterin seviyesini bir üst basamağa çıkarmak.",
        "yasakli_kelimeler": ["xp", "tecrübe", "level up", "yetenek puanı", "gelişim"],
        "zorluk": "orta"
    },
    {
        "kelime": "Loot Toplamak",
        "aciklama": "Düşmanlardan düşen veya sandıklardan çıkan ganimet ve eşyaları çantaya almak.",
        "yasakli_kelimeler": ["ganimet", "sandık", "eşya", "düşen", "envanter"],
        "zorluk": "orta"
    },
    {
        "kelime": "Envanter Düzenlemek",
        "aciklama": "Karakterin çantasındaki eşyaları ağırlık veya türe göre organize etmek.",
        "yasakli_kelimeler": ["çanta", "organize", "ağırlık", "slot", "eşyalar"],
        "zorluk": "orta"
    },
    {
        "kelime": "Grup Kurmak",
        "aciklama": "Zindan veya görev için diğer oyuncularla lobi/parti oluşturmak.",
        "yasakli_kelimeler": ["parti", "lobi", "zindan", "arkadaş", "takım"],
        "zorluk": "orta"
    },
    {
        "kelime": "Skill Kullanmak",
        "aciklama": "Karakterin özel büyü veya yetenek tuşuna basarak atağını sergilemek.",
        "yasakli_kelimeler": ["yetenek", "büyü", "cooldown", "mana", "tuş"],
        "zorluk": "orta"
    },
    {
        "kelime": "Respawn Olmak",
        "aciklama": "Öldükten sonra başlangıç veya doğma noktasında yeniden canlanmak.",
        "yasakli_kelimeler": ["yeniden doğmak", "canlanmak", "ölüm", "spawn", "nokta"],
        "zorluk": "orta"
    },
    {
        "kelime": "Haritayı Açmak",
        "aciklama": "Sisli veya keşfedilmemiş açık dünya bölgelerini gezerek mini haritada görünür kılmak.",
        "yasakli_kelimeler": ["mini harita", "açık dünya", "sis", "keşif", "bölge"],
        "zorluk": "orta"
    },
    {
        "kelime": "Karakter Özelleştirmek",
        "aciklama": "Oyun başında kahramanın saç, yüz, zırh ve giysi görünümünü tasarlamak.",
        "yasakli_kelimeler": ["görünüm", "saç", "yüz", "zırh", "kozmetik"],
        "zorluk": "orta"
    },
    {
        "kelime": "FPS Düşüşü Yaşamak",
        "aciklama": "Bilgisayar donanımının yetersizliğiyle ekran saniyelik kare hızının aniden düşüp kasması.",
        "yasakli_kelimeler": ["kare hızı", "kasma", "donma", "ekran kartı", "drop"],
        "zorluk": "orta"
    },
    {
        "kelime": "Ping Yükselmek",
        "aciklama": "İnternet gecikmesi yüzünden oyunda lag oluşması ve komutların geç gitmesi.",
        "yasakli_kelimeler": ["lag", "gecikme", "milisaniye", "internet", "bağlantı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Rank Atlamak",
        "aciklama": "Dereceli rekabetçi maçları kazanarak bronz, gümüş, elmas gibi liglerde yükselmek.",
        "yasakli_kelimeler": ["dereceli", "lig", "elmas", "elo", "rekabetçi"],
        "zorluk": "orta"
    },
    {
        "kelime": "Eşya Üretmek",
        "aciklama": "Toplanan maden ve malzemeleri crafting masasında yeni silahlara dönüştürmek.",
        "yasakli_kelimeler": ["crafting", "üretim masası", "maden", "malzeme", "tarif"],
        "zorluk": "orta"
    },
    {
        "kelime": "Yama İndirmek",
        "aciklama": "Oyundaki hataları düzelten veya yeni içerik getiren güncelleme dosyasını yüklemek.",
        "yasakli_kelimeler": ["patch", "güncelleme", "hata düzeltme", "indirme", "yeni sürüm"],
        "zorluk": "orta"
    },
    {
        "kelime": "Mod Kurmak",
        "aciklama": "Topluluk tarafından üretilen ek içerik veya grafik geliştirme dosyalarını oyuna entegre etmek.",
        "yasakli_kelimeler": ["modifikasyon", "topluluk", "nexus", "grafik modu", "eklenti"],
        "zorluk": "orta"
    },
    {
        "kelime": "Pusu Kurmak",
        "aciklama": "Battle royale oyunlarında güvenli alan çemberinde bekleyip geçen rakipleri avlamak.",
        "yasakli_kelimeler": ["çember", "alan", "battle royale", "beklemek", "camper"],
        "zorluk": "orta"
    },
    {
        "kelime": "Speedrun Yapmak",
        "aciklama": "Bir oyunu glitch veya kestirmeler kullanarak mümkün olan en kısa sürede bitirmeye çalışmak.",
        "yasakli_kelimeler": ["hızlı bitirme", "rekor", "süre", "kestirme", "kronometre"],
        "zorluk": "orta"
    },
    {
        "kelime": "Mikrofon Basmak",
        "aciklama": "Push-to-talk tuşuna basarak takım içi sesli iletişime bilgi vermek.",
        "yasakli_kelimeler": ["push to talk", "sesli sohbet", "iletişim", "info vermek", "konuşmak"],
        "zorluk": "orta"
    },
    {
        "kelime": "Zırh Kuşanmak",
        "aciklama": "Karakterin savunma değerini artırmak için kask, göğüslük ve eldiven takmak.",
        "yasakli_kelimeler": ["kask", "savunma", "göğüslük", "defans", "ekipman"],
        "zorluk": "orta"
    },
    {
        "kelime": "NPC ile Konuşmak",
        "aciklama": "Oyun içi yapay zeka karakterleriyle etkileşime girip görev veya diyalog almak.",
        "yasakli_kelimeler": ["görev veren", "diyalog", "yapay zeka", "etkileşim", "bot"],
        "zorluk": "orta"
    },
    {
        "kelime": "Görev Takip Etmek",
        "aciklama": "Görev günlüğündeki ana ve yan görev hedeflerine doğru harita işaretçisini izlemek.",
        "yasakli_kelimeler": ["quest", "günlük", "işaretçi", "hedef", "yan görev"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kritik Vuruş Yapmak",
        "aciklama": "Düşmanın kafasına veya zayıf noktasına vurarak iki katı hasar (crit) çıkarmak.",
        "yasakli_kelimeler": ["headshot", "hasar", "zayıf nokta", "katı", "crit"],
        "zorluk": "orta"
    },
    {
        "kelime": "Trollük Yapmak",
        "aciklama": "Takım arkadaşlarını bilerek trolleyip oyunu sabote etmek.",
        "yasakli_kelimeler": ["sabotaj", "kasıtlı", "rahatsız etmek", "toxic", "feedlemek"],
        "zorluk": "orta"
    },
    {
        "kelime": "Yayın Açmak",
        "aciklama": "Oynanan video oyununu Twitch veya YouTube üzerinden canlı olarak izleyicilere aktarmak.",
        "yasakli_kelimeler": ["twitch", "youtube", "canlı yayın", "izleyici", "streamer"],
        "zorluk": "orta"
    },

    # Zor (14)
    {
        "kelime": "Hitbox Hesaplamak",
        "aciklama": "Dövüş veya nişancı oyunlarında merminin ve vuruşun isabet ettiği görünmez çarpışma kutularını analiz etmek.",
        "yasakli_kelimeler": ["çarpışma kutusu", "isabet alanı", "piksel", "hasar tespiti", "dövüş"],
        "zorluk": "zor"
    },
    {
        "kelime": "Animasyon İptali Yapmak",
        "aciklama": "Karakterin vuruş sonrası bekleme hareketini başka bir tuşla kesip daha seri saldırı çıkarmak.",
        "yasakli_kelimeler": ["animation cancel", "kesmek", "seri saldırı", "frame", "kombo"],
        "zorluk": "zor"
    },
    {
        "kelime": "Aggro Çekmek",
        "aciklama": "MMO oyunlarında tank sınıfı oyuncunun boss canavarın tüm saldırı odağını üzerine çekmesi.",
        "yasakli_kelimeler": ["tank", "tehdit", "canavar odağı", "taunt", "mmo"],
        "zorluk": "zor"
    },
    {
        "kelime": "Kite Yapmak",
        "aciklama": "Menzilli karakterin düşmana vurup kaçarak aradaki mesafeyi sürekli koruması.",
        "yasakli_kelimeler": ["hit and run", "mesafe koruma", "menzilli", "vur kaç", "ad carry"],
        "zorluk": "zor"
    },
    {
        "kelime": "Gank Atmak",
        "aciklama": "MOBA oyunlarında ormancının beklenmedik anda koridora baskın yapıp rakibi gafil avlaması.",
        "yasakli_kelimeler": ["moba", "koridor", "baskın", "ormancı", "lol"],
        "zorluk": "zor"
    },
    {
        "kelime": "Frameleri Saymak",
        "aciklama": "Dövüş oyunlarında hareketlerin avantaj veya dezavantaj kare sayılarını (frame data) ezberlemek.",
        "yasakli_kelimeler": ["frame data", "avantaj", "dövüş oyunu", "kare sayısı", "bloklama"],
        "zorluk": "zor"
    },
    {
        "kelime": "Build Dizmek",
        "aciklama": "ARPG oyunlarında yetenek ağacı, eşya statları ve pasif bonusları maksimum hasar için optimize etmek.",
        "yasakli_kelimeler": ["yetenek ağacı", "stat", "optimizasyon", "pasif", "meta"],
        "zorluk": "zor"
    },
    {
        "kelime": "Raid Liderliği Yapmak",
        "aciklama": "Kırk kişilik büyük klan zindanında herkesin rol ve mekanik sıralamasını yönetmek.",
        "yasakli_kelimeler": ["klan", "büyük zindan", "mekanik", "komut", "wow"],
        "zorluk": "zor"
    },
    {
        "kelime": "Nerf Yemek",
        "aciklama": "Geliştirici güncellemesiyle aşırı güçlü olan karakter veya silahın değerlerinin düşürülmesi.",
        "yasakli_kelimeler": ["zayıflatma", "güç düşüşü", "dengeleme", "buff", "yama"],
        "zorluk": "zor"
    },
    {
        "kelime": "Buff Almak",
        "aciklama": "Karaktere geçici ekstra güç, hız veya zırh sağlayan büyü ve iksir etkisi yüklenmesi.",
        "yasakli_kelimeler": ["güçlendirme", "geçici etki", "stat artışı", "iksir", "büyü"],
        "zorluk": "zor"
    },
    {
        "kelime": "Glitch Kullanmak",
        "aciklama": "Oyun motorundaki kod veya harita sınır hatalarını kendi lehine kullanarak duvardan geçmek.",
        "yasakli_kelimeler": ["hata", "duvardan geçme", "oyun motoru", "açık", "speedrun"],
        "zorluk": "zor"
    },
    {
        "kelime": "Reroll Atmak",
        "aciklama": "Gacha veya RPG oyunlarında en iyi başlangıç kahramanını veya eşya statını elde etmek için sıfırlamak.",
        "yasakli_kelimeler": ["gacha", "sıfırlama", "zar atma", "yeniden çekme", "stat değişimi"],
        "zorluk": "zor"
    },
    {
        "kelime": "Macro Atamak",
        "aciklama": "Birden çok tuş kombinasyonunu tek bir fare veya klavye tuşuna otomatik sekans olarak kodlamak.",
        "yasakli_kelimeler": ["otomasyon", "tuş kombinasyonu", "yazılım", "tek tuş", "sekans"],
        "zorluk": "zor"
    },
    {
        "kelime": "Metayı Takip Etmek",
        "aciklama": "En son güncellemeyle en güçlü ve en çok kazanma oranına sahip taktik ve şampiyonları oynamak.",
        "yasakli_kelimeler": ["en güçlü", "kazanma oranı", "şampiyon", "taktik", "trend"],
        "zorluk": "zor"
    }
]

if __name__ == "__main__":
    add_and_save_verbs("vahsidoga", vahsidoga_verbs)
    add_and_save_verbs("videooyunlari", videooyunlari_verbs)
