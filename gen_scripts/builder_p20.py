import os, sys, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gen_scripts.card_utils import add_and_save_verbs

# 39. kutlamalar
kutlamalar_verbs = [
    # Kolay (12)
    {"kelime": "pasta kesmek", "yasakli_kelimeler": ["doğum günü", "bıçak", "dilim", "mum", "kutlama"], "zorluk": "kolay", "aciklama": "Kutlama pastasını bıçakla dilimleyip ikram etmek."},
    {"kelime": "mum üflemek", "yasakli_kelimeler": ["doğum günü pastası", "dilek tutmak", "söndürmek", "yaş", "nefes"], "zorluk": "kolay", "aciklama": "Pastanın üzerindeki yanan mumları bir nefeste söndürmek."},
    {"kelime": "hediye paketi açmak", "yasakli_kelimeler": ["kutu", "kurdele", "sürpriz", "yırtmak", "sevinç"], "zorluk": "kolay", "aciklama": "Kendisine verilen hediyenin süs kağıdını yırtıp içindekini görmek."},
    {"kelime": "balon şişirmek", "yasakli_kelimeler": ["nefes", "renkli", "parti süsü", "patlamak", "hava"], "zorluk": "kolay", "aciklama": "Kutlama mekanı için renkli balonları hava üfleyerek büyütmek."},
    {"kelime": "şarkı söylemek", "yasakli_kelimeler": ["iyi ki doğdun", "müzik", "hep bir ağızdan", "melodi", "parti"], "zorluk": "kolay", "aciklama": "Kutlanan kişi için neşeyle hep bir ağızdan kutlama şarkısı okumak."},
    {"kelime": "sarılmak", "yasakli_kelimeler": ["kucaklaşmak", "tebrik", "bayram", "sevgi", "kollarını açmak"], "zorluk": "kolay", "aciklama": "Kutlama anında sevdiklerine kollarını dolayıp kucaklaşmak."},
    {"kelime": "alkışlamak", "yasakli_kelimeler": ["el çırpmak", "tebrik", "coşku", "kutlamak", "ses"], "zorluk": "kolay", "aciklama": "Başarıyı veya özel anı kutlamak için ellerini birbirine vurmak."},
    {"kelime": "parti vermek", "yasakli_kelimeler": ["arkadaşlar", "eğlence", "ev", "müzik", "davet"], "zorluk": "kolay", "aciklama": "Kutlama yapmak için arkadaşlarını eğlenceli bir organizasyona çağırmak."},
    {"kelime": "kadeh kaldırmak", "yasakli_kelimeler": ["şerefe", "tost", "içecek", "kutlama", "bardak tokuşturma"], "zorluk": "kolay", "aciklama": "Birinin veya olayın şerefine içecek bardağını havaya kaldırmak."},
    {"kelime": "konfeti patlatmak", "yasakli_kelimeler": ["renkli kağıtlar", "sürpriz", "havaya fırlatma", "parti", "patlama sesi"], "zorluk": "kolay", "aciklama": "Kutlama anında havaya renkli parlak kağıt parçaları saçmak."},
    {"kelime": "dans etmek", "yasakli_kelimeler": ["müzik", "oynamak", "halay", "eğlence", "ritim"], "zorluk": "kolay", "aciklama": "Kutlamanın neşesiyle müzik eşliğinde oynamak."},
    {"kelime": "fotoğraf çektirmek", "yasakli_kelimeler": ["anı", "poz", "hatıra", "kamera", "toplu resim"], "zorluk": "kolay", "aciklama": "Özel kutlama anını ölümsüzleştirmek için hatıra fotoğrafı çekilmek."},

    # Orta (24)
    {"kelime": "dilek tutmak", "yasakli_kelimeler": ["mum üflerken", "içinden geçirme", "gerçekleşmesi", "dua", "niyet"], "zorluk": "orta", "aciklama": "Mumları üflemeden önce gerçekleşmesini istediği arzuyu içinden geçirmek."},
    {"kelime": "havai fişek fırlatmak", "yasakli_kelimeler": ["gökyüzü", "renkli patlama", "gece", "kutlama", "fişek"], "zorluk": "orta", "aciklama": "Büyük kutlamalarda gökyüzünde ışık ve patlama şöleni sergilemek."},
    {"kelime": "bayramlaşmak", "yasakli_kelimeler": ["el öpmek", "ziyaret", "şeker", "akraba", "bayram tebriği"], "zorluk": "orta", "aciklama": "Dini veya milli bayramda akraba ve dostlarla tebrikleşip el sıkışmak."},
    {"kelime": "sürpriz parti hazırlamak", "yasakli_kelimeler": ["gizlice", "haber vermeden", "ışıkları kapatma", "sürpriz", "organizasyon"], "zorluk": "orta", "aciklama": "Kişiden habersizce arkadaşlarını toplayıp mekan hazırlığı yapmak."},
    {"kelime": "şampanya patlatmak", "yasakli_kelimeler": ["mantar fırlaması", "köpük", "kutlama", "şişe", "zafer"], "zorluk": "orta", "aciklama": "Büyük bir başarı veya kutlamada gazlı içeceğin mantarını coşkuyla fırlatmak."},
    {"kelime": "el öpmek", "yasakli_kelimeler": ["büyükler", "alna koymak", "bayram harçlığı", "saygı", "dede nine"], "zorluk": "orta", "aciklama": "Bayramda saygı göstergesi olarak aile büyüklerinin elini öpüp alnına koymak."},
    {"kelime": "harçlık vermek", "yasakli_kelimeler": ["bayram parası", "çocuklar", "mendil", "sevindirmek", "hediye"], "zorluk": "orta", "aciklama": "Bayramda el öpen çocuklara sevinmeleri için nakit para vermek."},
    {"kelime": "yıldönümü kutlamak", "yasakli_kelimeler": ["evlilik", "yıl", "romantik", "özel gün", "tarih"], "zorluk": "orta", "aciklama": "Evlilik veya önemli bir olayın her yıl aynı tarihteki tekrarını anmak."},
    {"kelime": "mekanı süslemek", "yasakli_kelimeler": ["flama", "süsler", "ışıklandırma", "dekorasyon", "parti hazırlığı"], "zorluk": "orta", "aciklama": "Kutlamanın yapılacağı odayı veya salonu temaya uygun donatmak."},
    {"kelime": "tebrik kartı yollamak", "yasakli_kelimeler": ["yeni yıl", "posta", "güzel dilekler", "mesaj", "zarf"], "zorluk": "orta", "aciklama": "Uzakta yaşayan tanıdıklarına özel gün tebriklerini yazılı kartla iletmek."},
    {"kelime": "geri sayım yapmak", "yasakli_kelimeler": ["yılbaşı", "on dokuz sekiz", "gece yarısı", "saat 12", "yeni yıl"], "zorluk": "orta", "aciklama": "Yılbaşı gecesi son on saniyeyi hep bir ağızdan geriye doğru saymak."},
    {"kelime": "mezuniyet kepi fırlatmak", "yasakli_kelimeler": ["üniversite", "tören", "havaya atma", "cübbe", "diploma"], "zorluk": "orta", "aciklama": "Okul bitirme töreninde mezuniyet şapkasını coşkuyla göğe fırlatmak."},
    {"kelime": "bebek partisi düzenlemek", "yasakli_kelimeler": ["baby shower", "doğum öncesi", "hediyeleşme", "anne adayı", "pasta"], "zorluk": "orta", "aciklama": "Doğacak bebeği ve anneyi kutlamak için doğum öncesi eğlence yapmak."},
    {"kelime": "kına yakmak", "yasakli_kelimeler": ["kına gecesi", "avuç içi", "gelin ağlatma", "türkü", "kırmızı tülbent"], "zorluk": "orta", "aciklama": "Düğün öncesi gelinin ve konukların avuçlarına geleneksel kına sürmek."},
    {"kelime": "ziyafet vermek", "yasakli_kelimeler": ["büyük sofra", "yemekli davet", "donatılmış masa", "ağırlamak", "ikram"], "zorluk": "orta", "aciklama": "Misafirlere zengin ve çok çeşitli yemeklerden oluşan görkemli sofra kurmak."},
    {"kelime": "altın takmak", "yasakli_kelimeler": ["düğün takısı", "çeyrek altın", "gelin damat", "kurdele", "hediye"], "zorluk": "orta", "aciklama": "Evlenen çifte destek olmak için yakalarına çeyrek veya tam altın iğnelemek."},
    {"kelime": "açılış kurdelesi kesmek", "yasakli_kelimeler": ["makas", "yeni dükkan", "kırmızı kurdele", "tören", "protokol"], "zorluk": "orta", "aciklama": "Yeni bir tesisin veya mağazanın resmi açılışında sembolik bandı kesmek."},
    {"kelime": "kürsüde konuşma yapmak", "yasakli_kelimeler": ["teşekkür konuşması", "mikrofon", "davetliler", "kutlama", "hitap"], "zorluk": "orta", "aciklama": "Kutlama gecesinde sahneye çıkıp davetlilere teşekkür hitabında bulunmak."},
    {"kelime": "nişan yüzüğü takmak", "yasakli_kelimeler": ["kırmızı kurdele", "yüzük", "alyans", "makas kesmiyor", "sözleşme"], "zorluk": "orta", "aciklama": "Evlilik yolundaki ilk adımda çiftlerin parmağına kurdeleli yüzük takmak."},
    {"kelime": "şampiyonluk turu atmak", "yasakli_kelimeler": ["otobüs üstü", "kupa", "bayrak", "taraftar", "şehir"], "zorluk": "orta", "aciklama": "Kazanılan kupa sonrasında üstü açık otobüsle şehri turlayıp kutlamak."},
    {"kelime": "fener alayına katılmak", "yasakli_kelimeler": ["meşale", "yürüyüş", "bayrak", "gece", "milli bayram"], "zorluk": "orta", "aciklama": "Milli bayram akşamında ellerde meşaleler ve bayraklarla caddede yürümek."},
    {"kelime": "gözyaşlarına hakim olamamak", "yasakli_kelimeler": ["mutluluk gözyaşı", "duygulanmak", "özel an", "ağlamak", "sevinç"], "zorluk": "orta", "aciklama": "Kutlamadaki yoğun duygu ve sevinç anında mutluluktan ağlamak."},
    {"kelime": "kutlama mesajı yayınlamak", "yasakli_kelimeler": ["sosyal medya", "resmi bildiri", "tebrik", "yazılı", "kamuoyu"], "zorluk": "orta", "aciklama": "Önemli gün vesilesiyle tebrik içerikli resmi veya dijital metin paylaşmak."},
    {"kelime": "anı defterine yazmak", "yasakli_kelimeler": ["dilekler", "kalem", "özel defter", "gelin damat", "hatıra"], "zorluk": "orta", "aciklama": "Düğün veya kutlama salonunun girişindeki hatıra defterine iyi dilekleri not etmek."},

    # Zor (14)
    {"kelime": "piñata patlatmak", "yasakli_kelimeler": ["göz bağı", "sopa ile vurma", "şekerleme dökülmesi", "meksika geleneği", "figür"], "zorluk": "zor", "aciklama": "Gözleri bağlıyken tavana asılı şeker dolu karton figüre sopayla vurup parçalamak."},
    {"kelime": "potlaç töreni düzenlemek", "yasakli_kelimeler": ["kızılderili şöleni", "mal mülk dağıtma", "statü kazanma", "armağan ekonomisi", "antropolojik kutlama"], "zorluk": "zor", "aciklama": "Kabile şefinin saygınlık kazanmak için tüm servetini konuklara dağıttığı şöleni yapmak."},
    {"kelime": "karnaval kortejinde geçit yapmak", "yasakli_kelimeler": ["rio karnavalı", "alegorik araba", "tüy kostümler", "samba", "sokak geçidi"], "zorluk": "zor", "aciklama": "Görkemli süslenmiş devasa araçların üstünde binlerce dansçıyla caddede yürümek."},
    {"kelime": "kutlama serenadı yapmak", "yasakli_kelimeler": ["pencere altı", "gitarla şarkı", "romantik kutlama", "sevgiliye müzik", "gece"], "zorluk": "zor", "aciklama": "Özel günde sevgilinin penceresinin altına gidip enstrüman eşliğinde şarkı söylemek."},
    {"kelime": "şeref kütüğü çakmak", "yasakli_kelimeler": ["okul birincisi", "mezuniyet anıtı", "pirinç plaka", "tören", "çekiç"], "zorluk": "zor", "aciklama": "Dönem birincisi olarak adının yazılı olduğu madeni plakayı törenle kütüğe çakmak."},
    {"kelime": "su fıskiyesi selamı vermek", "yasakli_kelimeler": ["su takı", "itfaiye aracı", "ilk uçuş inişi", "uçak karşılama", "havacılık kutlaması"], "zorluk": "zor", "aciklama": "İlk veya son uçuşunu yapan uçağı pistte iki itfaiye aracının su püskürterek selamlaması."},
    {"kelime": "bar mitzvah töreni icra etmek", "yasakli_kelimeler": ["13 yaş", "yahudi ergenlik", "tevrat okuma", "tören", "yetişkinliğe adım"], "zorluk": "zor", "aciklama": "Yahudi gençlerinin yetişkinliğe geçişini dini merasim ve büyük partiyle kutlamak."},
    {"kelime": "quinceañera balosu vermek", "yasakli_kelimeler": ["15 yaş kutlaması", "latin amerika", "prenses elbisesi", "topuklu ayakkabı giyme", "vals"], "zorluk": "zor", "aciklama": "Latin kültüründe kız çocuklarının 15. yaş gününü görkemli balo ve dansla kutlamak."},
    {"kelime": "saturnalia ritüeli yaşatmak", "yasakli_kelimeler": ["antik roma", "rollerin değişimi", "kölelerin efendi olması", "kış gündönümü", "şenlik"], "zorluk": "zor", "aciklama": "Antik Roma'daki efendilerle kölelerin yer değiştirdiği kış bayramı havasını canlandırmak."},
    {"kelime": "şampanya kulesi doldurmak", "yasakli_kelimeler": ["üst üste kadehler", "piramit", "en üstten dökme", "taşarak dolma", "lüks kutlama"], "zorluk": "zor", "aciklama": "Piramit şeklinde dizilmiş yüzlerce kadehi en üstten dökülen içecekle sırayla doldurmak."},
    {"kelime": "hıdırellez ateşi üstünden atlamak", "yasakli_kelimeler": ["bahar bayramı", "dilek dileme", "alevden atlama", "6 mayıs", "bereket"], "zorluk": "zor", "aciklama": "Baharın gelişini kutlamak için yakılan ateşin üzerinden sağlık dileğiyle atlamak."},
    {"kelime": "alegorik maske takmak", "yasakli_kelimeler": ["venedik karnavalı", "gizem", "porselen mask", "tarihi kostüm", "kıyafet balosu"], "zorluk": "zor", "aciklama": "Venedik tarzı maskeli baloda kimliğini gizleyen süslü porselen maske taşımak."},
    {"kelime": "holika dahan ateşi yakmak", "yasakli_kelimeler": ["holi festivali", "renkler bayramı", "kötülüğün yanması", "hint kültürü", "odun yığını"], "zorluk": "zor", "aciklama": "Holi festivalinin arifesinde kötülüğün yenilgisini simgeleyen kutsal ateşi tutuşturmak."},
    {"kelime": "kurban kesim duası okumak", "yasakli_kelimeler": ["bayram kurbanı", "tekbir getirme", "ibadet ve kutlama", "paylaşım", "gelenek"], "zorluk": "zor", "aciklama": "Bayram sabahı adanan kurbanın başında tekbir getirip dualar okumak."}
]

# 40. kutugoyunlari
kutugoyunlari_verbs = [
    # Kolay (12)
    {"kelime": "zarları masaya yuvarlamak", "yasakli_kelimeler": ["noktalar", "altı", "masa", "şans", "fırlatmak"], "zorluk": "kolay", "aciklama": "Küp şeklindeki oyun taşını masaya yuvarlamak."},
    {"kelime": "piyon ilerletmek", "yasakli_kelimeler": ["kare", "adım", "tahta", "oynatmak", "figür"], "zorluk": "kolay", "aciklama": "Kendi karakter taşını zar kadar kare ileri taşımak."},
    {"kelime": "kart çekmek", "yasakli_kelimeler": ["deste", "el", "sıra", "görev", "kapalı"], "zorluk": "kolay", "aciklama": "Masadaki destenin en üstünden yeni oyun kartı almak."},
    {"kelime": "sıra beklemek", "yasakli_kelimeler": ["arkadaş", "tur", "hamle", "oyuncu", "zaman"], "zorluk": "kolay", "aciklama": "Diğer oyuncuların hamlesini bitirmesini sabırla beklemek."},
    {"kelime": "puan toplamak", "yasakli_kelimeler": ["skor", "kazanmak", "yıldız", "artı", "zafer"], "zorluk": "kolay", "aciklama": "Oyun içindeki görevleri tamamlayıp skor hanesine puan yazdırmak."},
    {"kelime": "kutuyu açmak", "yasakli_kelimeler": ["kapak", "kutu oyunu", "kurulum", "parçalar", "yeni oyun"], "zorluk": "kolay", "aciklama": "Oyuna başlamak için masanın ortasındaki kutunun kapağını kaldırmak."},
    {"kelime": "tahtayı sermek", "yasakli_kelimeler": ["mukavva", "harita", "kareler", "masa üstü", "açmak"], "zorluk": "kolay", "aciklama": "Katlanmış sert mukavva oyun alanını masaya düzgünce açmak."},
    {"kelime": "oyunu kazanmak", "yasakli_kelimeler": ["birinci olmak", "zafer", "en yüksek puan", "şampiyon", "bitiş"], "zorluk": "kolay", "aciklama": "Kuralları başarıyla tamamlayıp oyunu rakiplerinden önde bitirmek."},
    {"kelime": "hile yapmamak", "yasakli_kelimeler": ["dürüstlük", "kurala uymak", "aldatmamak", "gizlice", "adil"], "zorluk": "kolay", "aciklama": "Oyun kurallarına sadık kalıp haksız kazançtan kaçınmak."},
    {"kelime": "kartları karıştırmak", "yasakli_kelimeler": ["deste", "shuffle", "rastgele", "kesmek", "el"], "zorluk": "kolay", "aciklama": "Kartların sırasını bozup rastgele hale getirmek."},
    {"kelime": "hamle yapmak", "yasakli_kelimeler": ["hareket", "sıra sende", "oynamak", "strateji", "adım"], "zorluk": "kolay", "aciklama": "Sırası geldiğinde oyun mekanizmasına uygun hareketini gerçekleştirmek."},
    {"kelime": "parçaları kutuya dizmek", "yasakli_kelimeler": ["toplamak", "torba", "oyun sonu", "kaldırmak", "düzen"], "zorluk": "kolay", "aciklama": "Oyun bittiğinde piyon ve kartları kutusundaki gözlere yerleştirmek."},

    # Orta (24)
    {"kelime": "kural kitapçığını okumak", "yasakli_kelimeler": ["manual", "yönergeler", "oyun kuralları", "öğrenmek", "nasıl oynanır"], "zorluk": "orta", "aciklama": "Oyuna başlamadan önce içinden çıkan talimat kitapçığını incelemek."},
    {"kelime": "deste inşa etmek", "yasakli_kelimeler": ["deck building", "kart satın alma", "sinerji", "dominion", "kombinasyon"], "zorluk": "orta", "aciklama": "Oyun aktıkça güçlü kartları destesine ekleyip kendi destesini geliştirmek."},
    {"kelime": "işçi yerleştirmek", "yasakli_kelimeler": ["worker placement", "meeple", "aksiyon alanı", "kaynak toplama", "bloke etme"], "zorluk": "orta", "aciklama": "Piyonunu tahtadaki sınırlı eylem alanlarına koyarak kaynak veya hak kazanmak."},
    {"kelime": "kaynak yönetimi yapmak", "yasakli_kelimeler": ["odun taş tahıl", "harcama", "depolama", "üretim", "verimlilik"], "zorluk": "orta", "aciklama": "Toplanan sınırlı hammadde ve paraları en verimli şekilde kullanmak."},
    {"kelime": "meeple koymak", "yasakli_kelimeler": ["ahşap adam figürü", "carcassonne", "yol kale tarlaya yerleştirme", "puan", "piyon"], "zorluk": "orta", "aciklama": "Ahşap insan figürünü karonun üzerine koyarak orayı sahiplenmek."},
    {"kelime": "karo yerleştirmek", "yasakli_kelimeler": ["tile placement", "harita genişletme", "yol ve şehir eşleme", "kare parça", "masa"], "zorluk": "orta", "aciklama": "Kare karton parçayı kenarları uyumlu olacak şekilde masadaki haritaya eklemek."},
    {"kelime": "blöf yapmak", "yasakli_kelimeler": ["kandırma", "elini saklama", "yalan söyleme", "rol yapma", "poker yüzü"], "zorluk": "orta", "aciklama": "Rakipleri yanıltmak için elindeki kartlar hakkında yalan beyanda bulunmak."},
    {"kelime": "gizli rolünü saklamak", "yasakli_kelimeler": ["social deduction", "hain", "vampir köylü", "kimlik", "ihanet"], "zorluk": "orta", "aciklama": "Oyun başında kapalı verilen hain veya ajan kimliğini kimseye belli etmemek."},
    {"kelime": "zar havuzunu yönetmek", "yasakli_kelimeler": ["dice drafting", "zar seçme", "yeniden atma hakkı", "kombinasyon", "şans kontrolü"], "zorluk": "orta", "aciklama": "Masaya atılan zarlar arasından stratejisine en uygun olanları seçip kullanmak."},
    {"kelime": "pazarlık masasına oturmak", "yasakli_kelimeler": ["catan", "takas", "koyun verip odun alma", "anlaşma", "ticaret"], "zorluk": "orta", "aciklama": "Eksik kaynaklarını tamamlamak için rakipleriyle takas müzakeresi yapmak."},
    {"kelime": "alan kontrolü sağlamak", "yasakli_kelimeler": ["area control", "çoğunluk", "bölge hakimiyeti", "savaş", "puan kazanma"], "zorluk": "orta", "aciklama": "Tahtadaki belirli bir bölgeye en çok askeri koyup oranın puanını toplamak."},
    {"kelime": "ortaklaşa mücadele etmek", "yasakli_kelimeler": ["co-op", "oyuna karşı birlik", "pandemic", "birlikte kazanma kaybetme", "dayanışma"], "zorluk": "orta", "aciklama": "Birbirine rakip olmak yerine tüm oyuncularla birlikte oyun sistemine karşı oynamak."},
    {"kelime": "görev kartını gizli tutmak", "yasakli_kelimeler": ["gizli hedef", "oyun sonu puanı", "hedef kartı", "göstermemek", "strateji"], "zorluk": "orta", "aciklama": "Oyun sonunda ekstra puan getirecek özel görevi rakiplerden gizlemek."},
    {"kelime": "minyatür boyamak", "yasakli_kelimeler": ["plastik figür", "warhammer", "akrilik fırça", "hobi", "detay"], "zorluk": "orta", "aciklama": "Kutu oyunundaki plastik karakter minyatürlerini boyalarla canlandırmak."},
    {"kelime": "monopoly parası dağıtmak", "yasakli_kelimeler": ["bankacı", "kağıt para", "başlangıç sermayesi", "dağıtım", "kasa"], "zorluk": "orta", "aciklama": "Oyun başlamadan önce kasa görevlisi olarak herkese başlangıç parasını saymak."},
    {"kelime": "kumar oynamamak", "yasakli_kelimeler": ["bahis", "şans kontrolü", "risk alma", "taktik", "zar"], "zorluk": "orta", "aciklama": "Körlemesine şansa güvenmek yerine hesaplanmış risklerle ilerlemek."},
    {"kelime": "tur sırasını belirlemek", "yasakli_kelimeler": ["turn order", "en yüksek zar", "saat yönü", "inisiyatif", "başlangıç oyuncusu"], "zorluk": "orta", "aciklama": "Kimin önce oynayacağını zarla veya kuraldaki kriterle belirlemek."},
    {"kelime": "kart kılıfı takmak", "yasakli_kelimeler": ["sleeve", "şeffaf koruyucu", "yıpranma önleme", "kart", "koleksiyon"], "zorluk": "orta", "aciklama": "Kartların kenarlarının soyulmaması için üzerlerine şeffaf koruyucu poşet geçirmek."},
    {"kelime": "puan tablosuna yazmak", "yasakli_kelimeler": ["skor kağıdı", "kalem", "toplama", "kategori", "oyun sonu"], "zorluk": "orta", "aciklama": "Oyun sonunda her kategoriden kazanılan puanları skor kağıdına işlemek."},
    {"kelime": "engelleme hamlesi yapmak", "yasakli_kelimeler": ["bloklama", "rakibin yolunu kesme", "alanı kapatma", "sabote", "taktik"], "zorluk": "orta", "aciklama": "Rakibin kazanmasını veya puan almasını önlemek için önüne set çekmek."},
    {"kelime": "kart elini optimize etmek", "yasakli_kelimeler": ["hand management", "kart kombosu", "en iyi sıra", "etkili kullanım", "tasarruf"], "zorluk": "orta", "aciklama": "Elindeki sınırlı kartları en yüksek faydayı verecek sırayla oynamak."},
    {"kelime": "kampanya modunda oynamak", "yasakli_kelimeler": ["legacy", "bölüm bölüm ilerleme", "kalıcı değişim", "hikaye", "senaryo"], "zorluk": "orta", "aciklama": "Oyunun her oturumunda bir önceki kararların taşındığı hikaye modunu oynamak."},
    {"kelime": "otoma destesi yönetmek", "yasakli_kelimeler": ["tek kişilik oyun", "yapay zeka kartları", "solo mod", "bot rakip", "sanal oyuncu"], "zorluk": "orta", "aciklama": "Tek başına oynarken sanal yapay zeka rakibinin hamle kartlarını çekip işletmek."},
    {"kelime": "kum saatiyle süre tutmak", "yasakli_kelimeler": ["zaman baskısı", "hızlı düşünme", "akan kum", "süre bitimi", "stres"], "zorluk": "orta", "aciklama": "Hamle süresini kısıtlamak için masadaki küçük kum saatini ters çevirmek."},

    # Zor (14)
    {"kelime": "engine building motoru kurmak", "yasakli_kelimeler": ["kart makinesi", "kartların birbirini tetiklemesi", "katlanarak artan güç", "zincirleme reaksiyon", "terraforming mars"], "zorluk": "zor", "aciklama": "Her tur birbirini besleyen ve katlanarak devasa kaynak üreten kart motoru inşa etmek."},
    {"kelime": "legacy oyununda bileşen yırtmak", "yasakli_kelimeler": ["kalıcı hasar", "kart imhası", "kutuya etiket yapıştırma", "tek seferlik deneyim", "pandemi legacy"], "zorluk": "zor", "aciklama": "Geri dönüşü olmayan Legacy oyununda talimat gereği kartı yırtıp panoya kalıcı etiket yapıştırmak."},
    {"kelime": "simültan aksiyon seçimi yapmak", "yasakli_kelimeler": ["aynı anda kart açma", "gizli seçim", "zihin okuma", "7 wonders", "hızlı tur"], "zorluk": "zor", "aciklama": "Tüm oyuncuların aynı anda gizlice seçtiği kartı masaya eşzamanlı açması."},
    {"kelime": "drafting mekanizması işletmek", "yasakli_kelimeler": ["kart seçip kalanı yana verme", "el döndürme", "en iyi kartı alma", "sola pas", "kart havuzu"], "zorluk": "zor", "aciklama": "Gelen kart destesinden en iyisini alıp kalanını yanındaki oyuncuya devretmek."},
    {"kelime": "rondel üzerinde ilerlemek", "yasakli_kelimeler": ["dairesel aksiyon çarkı", "adım maliyeti", "mac gerdts", "çark hamlesi", "eylem seçimi"], "zorluk": "zor", "aciklama": "Dairesel tekerlek üzerindeki eylemler arasında belirli adım kısıtlarıyla ilerleyip hamle seçmek."},
    {"kelime": "action point allowance harcamak", "yasakli_kelimeler": ["aksiyon puanı sistemi", "5 puanı bölüştürme", "hareket maliyeti", "hamle optimizasyonu", "puan kotası"], "zorluk": "zor", "aciklama": "Tur başında verilen 4-5 aksiyon puanını hareket ve eylemler arasında matematiksel paylaştırmak."},
    {"kelime": "modular board dizilimi oluşturmak", "yasakli_kelimeler": ["her oyunda değişen harita", "rastgele altıgenler", "farklı kurulum", "tekrar oynanabilirlik", "hex"], "zorluk": "zor", "aciklama": "Her oyun öncesinde tahtanın altıgen parçalarını rastgele dizerek benzersiz harita kurmak."},
    {"kelime": "asimetrik güçleri dengelemek", "yasakli_kelimeler": ["root", "her ırkın farklı kuralı", "benzersiz oynanış", "farklı kazanma şartı", "fraksiyon"], "zorluk": "zor", "aciklama": "Her fraksiyonun bambaşka kurallarla ve farklı hedeflerle oynadığı asimetrik yapıyı yönetmek."},
    {"kelime": "push-your-luck riskini hesaplamak", "yasakli_kelimeler": ["şansını zorlama", "açgözlülük cezası", "patlama riski", "durma noktası", "quacks"], "zorluk": "zor", "aciklama": "Daha çok ödül için torbadan taş çekmeye devam edip patlama riskini matematiksel tartmak."},
    {"kelime": "hidden movement izini sürmek", "yasakli_kelimeler": ["gizli hareket", "fury of dracula", "arkada gizlice dolaşma", "avcıların koordinasyonu", "iz bulma"], "zorluk": "zor", "aciklama": "Tahtada görünmeden gizlice haritada dolaşan tek bir oyuncunun ayak izlerini avcılarla sürmek."},
    {"kelime": "pazar talebini manipüle etmek", "yasakli_kelimeler": ["arz talep eğrisi", "brass", "hammadde fiyatı artırma", "piyasa boşaltma", "ekonomik oyun"], "zorluk": "zor", "aciklama": "Merkezi pazardan toplu mal çekip kaynak fiyatını rakiplerin alamayacağı kadar tırmandırmak."},
    {"kelime": "tableau building kombinasyonu kurmak", "yasakli_kelimeler": ["önündeki kart ızgarası", "wingspan", "habitat eşleşmesi", "puan motoru", "kart sinerjisi"], "zorluk": "zor", "aciklama": "Önündeki panoya kartları matris şeklinde yerleştirip aralarındaki sinerjilerden puan üretmek."},
    {"kelime": "tehdit seviyesini kontrol altında tutmak", "yasakli_kelimeler": ["threat track", "felaket eşiği", "canavar uyanışı", "arkham horror", "kaybetme koşulu"], "zorluk": "zor", "aciklama": "Her tur yükselen felaket göstergesini görevler tamamlayarak patlama sınırının altında tutmak."},
    {"kelime": "kral yapıcı durumuna düşmemek", "yasakli_kelimeler": ["kingmaker", "kendisi kazanamazken birini kazandırma", "etik oyunculuk", "tarafsız hamle", "üçüncü oyuncu"], "zorluk": "zor", "aciklama": "Kendisinin kazanma şansı kalmadığında yaptığı hamleyle bilerek bir rakibini şampiyon yapmaktan kaçınmak."}
]

add_and_save_verbs('kutlamalar', kutlamalar_verbs)
add_and_save_verbs('kutugoyunlari', kutugoyunlari_verbs)
print('P20 done!')
