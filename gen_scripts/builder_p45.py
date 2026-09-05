# -*- coding: utf-8 -*-
from card_utils import add_and_save_verbs

sinematografi_verbs = [
    # Kolay (12)
    {"kelime": "kamera açmak", "aciklama": "çekim için kameranın güç düğmesine basıp hazır hale getirmek", "yasakli_kelimeler": ["kamera", "açmak", "güç", "çekim", "başlatmak"], "zorluk": "kolay"},
    {"kelime": "odaklamak", "aciklama": "kameranın lensini çevirerek oyuncunun yüzünü netleştirmek", "yasakli_kelimeler": ["netleştirmek", "fokus", "lens", "bulanık", "yüz"], "zorluk": "kolay"},
    {"kelime": "yakınlaşmak", "aciklama": "zoom lensiyle oyuncunun yüz ifadesine doğru optik yaklaşmak", "yasakli_kelimeler": ["zoom in", "yakın çekim", "lens", "ifade", "optik"], "zorluk": "kolay"},
    {"kelime": "uzaklaşmak", "aciklama": "zoom kolunu çevirerek genel mekanı kadraja almak", "yasakli_kelimeler": ["zoom out", "genel plan", "geniş açı", "mekan", "kadraj"], "zorluk": "kolay"},
    {"kelime": "ışık vermek", "aciklama": "karanlık sahnede oyuncunun yüzüne spot ışığı yönlendirmek", "yasakli_kelimeler": ["spot", "aydınlatma", "lamba", "parlatmak", "karanlık"], "zorluk": "kolay"},
    {"kelime": "kadraja almak", "aciklama": "kameranın vizöründen bakarak nesneleri çerçeveye yerleştirmek", "yasakli_kelimeler": ["çerçeve", "vizör", "kompozisyon", "yerleşim", "ekran"], "zorluk": "kolay"},
    {"kelime": "takip etmek", "aciklama": "koşan oyuncunun arkasından veya yanından kamerayla birlikte yürümek", "yasakli_kelimeler": ["yürümek", "koşmak", "takip", "hareket", "kamera"], "zorluk": "kolay"},
    {"kelime": "lens değiştirmek", "aciklama": "geniş açıdan tele lense geçmek için kamera gövdesine yeni cam takmak", "yasakli_kelimeler": ["objektif", "telefoto", "geniş açı", "bayonet", "cam"], "zorluk": "kolay"},
    {"kelime": "kayda girmek", "aciklama": "kırmızı kayıt butonuna basıp dijital karta kareleri yazmaya başlamak", "yasakli_kelimeler": ["rec butonu", "kırmızı", "başlamak", "hafıza kartı", "kare"], "zorluk": "kolay"},
    {"kelime": "üçayak kurmak", "aciklama": "kamerayı sabitlemek için tripod bacaklarını açıp su terazisine oturtmak", "yasakli_kelimeler": ["tripod", "sabitleme", "bacaklar", "su terazisi", "duruş"], "zorluk": "kolay"},
    {"kelime": "vizörden bakmak", "aciklama": "görüntü yönetmeninin gözünü vizör lastiğine dayayıp kompozisyonu izlemesi", "yasakli_kelimeler": ["göz", "vizör lastiği", "kompozisyon", "izleme", "çerçeve"], "zorluk": "kolay"},
    {"kelime": "filtre takmak", "aciklama": "parlak güneşte lensin önüne nd ışık kırıcı cam vida etmek", "yasakli_kelimeler": ["nd filtre", "polarize", "lens önü", "güneş ışığı", "cam"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "pan yapmak", "aciklama": "kamerayı sabit durduğu üçayak üzerinde yatay eksende sağa sola çevirmek", "yasakli_kelimeler": ["yatay çevirme", "sağa sola", "tripod başı", "ufuk ekseni", "panoramik"], "zorluk": "orta"},
    {"kelime": "tilt yapmak", "aciklama": "kamera gövdesini dikey eksende yukarıdan aşağıya veya aşağıdan yukarıya eğmek", "yasakli_kelimeler": ["dikey eğme", "yukarı aşağı", "kamera kafası", "bina boyu", "açı"], "zorluk": "orta"},
    {"kelime": "rack focus atmak", "aciklama": "netliği ön plandaki nesneden arkadaki konuşan karaktere akıcı kaydırmak", "yasakli_kelimeler": ["netlik kaydırma", "odak değişimi", "ön plan arka plan", "follow focus", "bulanıklıktan nete"], "zorluk": "orta"},
    {"kelime": "üç nokta aydınlatma kurmak", "aciklama": "ana ışık, dolgu ışığı ve arka plan kontur ışığını 45 dereceyle yerleştirmek", "yasakli_kelimeler": ["key light", "fill light", "back light", "üçgen", "dolgu ana ışık"], "zorluk": "orta"},
    {"kelime": "diyafram açmak", "aciklama": "f değerini düşürerek arka planı bulanıklaştırıp sığ alan derinliği yakalamak", "yasakli_kelimeler": ["f/1.4", "sığ alan derinliği", "arka plan bulanıklığı", "bokeh", "apertür"], "zorluk": "orta"},
    {"kelime": "shutter açısını ayarlamak", "aciklama": "doğal hareket bulanıklığı için 180 derece enstantane kuralını uygulamak", "yasakli_kelimeler": ["180 derece kuralı", "enstantane", "hareket bulanıklığı", "motion blur", "örtücü"], "zorluk": "orta"},
    {"kelime": "renk sıcaklığı seçmek", "aciklama": "gün ışığı 5600 kelvin veya mum ışığı 3200 kelvin beyaz ayarı yapmak", "yasakli_kelimeler": ["kelvin", "white balance", "5600k", "3200k", "sıcak soğuk ton"], "zorluk": "orta"},
    {"kelime": "jimmy jib uçurmak", "aciklama": "uzun vinç kolunun ucundaki kamerayla havadan süzülerek devasa açılar yakalamak", "yasakli_kelimeler": ["kamera vinci", "uzun kol", "havadan çekim", "ağırlık dengesi", "panoramik vinç"], "zorluk": "orta"},
    {"kelime": "gimbal ile koşmak", "aciklama": "3 eksenli elektronik sabitleyici motorlarla koşarken sarsıntısız görüntü almak", "yasakli_kelimeler": ["ronin", "3 eksenli motor", "sarsıntı önleme", "elektronik sabitleyici", "koşu çekimi"], "zorluk": "orta"},
    {"kelime": "omuz kamerasıyla çekmek", "aciklama": "belgesel veya savaş sahnelerinde el kamerasının dinamik titremesini kullanmak", "yasakli_kelimeler": ["handheld", "el kamerası", "omuzluk rig", "dinamik hareket", "titrek çekim"], "zorluk": "orta"},
    {"kelime": "ışığı difüze etmek", "aciklama": "sert gölgeleri yumuşatmak için spotun önüne ipek tül veya frost filtre germek", "yasakli_kelimeler": ["yumuşatma", "ipek tül", "frost filtre", "sert gölge", "diffuser"], "zorluk": "orta"},
    {"kelime": "yansıtıcı tutmak", "aciklama": "gölgede kalan oyuncu yüzünü aydınlatmak için gümüş veya beyaz reflektör tutmak", "yasakli_kelimeler": ["reflektör", "gümüş beyaz", "gölge doldurma", "güneş yansıtma", "katlanır reflektör"], "zorluk": "orta"},
    {"kelime": "lens flare yakalamak", "aciklama": "güneşi lensin kenarından bilerek kadraja alıp dairesel ışık hüzmeleri saçmak", "yasakli_kelimeler": ["ışık hüzmesi", "güneş parlaması", "lens parlaması", "karşı ışık", "atmosferik"], "zorluk": "orta"},
    {"kelime": "kontur ışığı vermek", "aciklama": "oyuncunun saç ve omuz çizgisini karanlık arka plandan jilet gibi ayırmak", "yasakli_kelimeler": ["rim light", "saç ışığı", "arka ışıltı", "omuz çizgisi", "ayrıştırma"], "zorluk": "orta"},
    {"kelime": "üçte bir kuralına uymak", "aciklama": "kadrajı 9 eşit kareye bölüp ilgi odağını kesişim noktalarına oturtmak", "yasakli_kelimeler": ["rule of thirds", "9 kare", "kesişim noktası", "altın oran", "kompozisyon kuralı"], "zorluk": "orta"},
    {"kelime": "bakış boşluğu bırakmak", "aciklama": "karakterin baktığı yöne doğru kadrajda ferah bir negatif alan payı vermek", "yasakli_kelimeler": ["looking room", "lead room", "bakış yönü", "boşluk payı", "kadraj dengesi"], "zorluk": "orta"},
    {"kelime": "baş boşluğu ayarlamak", "aciklama": "karakterin başının üstü ile çerçevenin üst kenarı arasındaki mesafeyi oranlamak", "yasakli_kelimeler": ["headroom", "üst kenar", "baş üstü boşluğu", "kadraj tavanı", "oran"], "zorluk": "orta"},
    {"kelime": "altın saatte çekmek", "aciklama": "güneşin batışından önceki son bir saatte altın sarısı yumuşak ışığı yakalamak", "yasakli_kelimeler": ["golden hour", "gün batımı", "sarı ışık", "batan güneş", "son saat"], "zorluk": "orta"},
    {"kelime": "mavi saatte yakalamak", "aciklama": "güneş battıktan hemen sonra gökyüzünün masmavi derin tona büründüğü 20 dakika", "yasakli_kelimeler": ["blue hour", "gün batımı sonrası", "alacakaranlık", "gece öncesi", "derin mavi"], "zorluk": "orta"},
    {"kelime": "ağır çekim yapmak", "aciklama": "saniyede 120 veya 240 kare kaydedip patlamayı veya su damlasını yavaşlatmak", "yasakli_kelimeler": ["slow motion", "yüksek fps", "120 kare", "yavaşlatma", "hızlı çekim"], "zorluk": "orta"},
    {"kelime": "timelapse kurmak", "aciklama": "dakikada bir fotoğraf çekip gün boyu bulutların akışını 10 saniyeye sığdırmak", "yasakli_kelimeler": ["zaman atlamalı", "aralıklı çekim", "hızlandırılmış", "bulut akışı", "intervalometre"], "zorluk": "orta"},
    {"kelime": "drone ile süzülmek", "aciklama": "havadan 4k kameralı multikopter ile dağların ve vadilerin üzerinden uçmak", "yasakli_kelimeler": ["hava çekimi", "multikopter", "kuşbakışı", "uçuş", "gimbal kamera"], "zorluk": "orta"},
    {"kelime": "düşük açıdan bakmak", "aciklama": "kamerayı yere koyup yukarı doğru çekerek karakteri devasa ve güçlü göstermek", "yasakli_kelimeler": ["low angle", "yer seviyesi", "aşağıdan yukarı", "güçlü karakter", "heybet"], "zorluk": "orta"},
    {"kelime": "yüksek açıdan ezmek", "aciklama": "kamerayı tepeden aşağı eğip karakteri çaresiz ve küçük hissettirmek", "yasakli_kelimeler": ["high angle", "tepeden çekim", "çaresizlik", "küçük gösterme", "aşağı bakış"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "anamorfik sıkıştırma oranı", "aciklama": "2x optik anamorfoz lensle 4:3 sensör alanına geniş sinemaskop resmi sığdırmak", "yasakli_kelimeler": ["2x sıkıştırma", "optik sıkışma", "anamorfik lens", "sinemaskop", "sensör en boy"], "zorluk": "zor"},
    {"kelime": "dinamik aralığı zorlamak", "aciklama": "arri alexa sensörünün 14+ stop dinamik aralığıyla gölge ve parlak detayları kurtarmak", "yasakli_kelimeler": ["stop sayısı", "arri alexa", "patlayan ışık", "gölge detayı", "enlem toleransı"], "zorluk": "zor"},
    {"kelime": "log profilinde kaydetmek", "aciklama": "post prodüksiyonda maksimum renk esnekliği için kontrastı düzleştirilmiş ham format", "yasakli_kelimeler": ["c-log", "s-log", "logaritmik profil", "soluk ham görüntü", "gamut"], "zorluk": "zor"},
    {"kelime": "dual native iso kullanmak", "aciklama": "gece çekiminde sensörün ikinci yüksek donanımsal iso devresini açıp kumsallığı sıfırlamak", "yasakli_kelimeler": ["çift yerel iso", "donanımsal kazanç", "gren önleme", "gece hassasiyeti", "sensör devresi"], "zorluk": "zor"},
    {"kelime": "zebralarla pozlama kontrolü", "aciklama": "vizördeki yüzde 70 veya 100 çizgili şerit deseniyle patlayan ten tonlarını görmek", "yasakli_kelimeler": ["zebra deseni", "yüzde 70 ten", "aşırı pozlama", "vizör uyarısı", "çizgili alan"], "zorluk": "zor"},
    {"kelime": "false color okumak", "aciklama": "monitördeki pozlama değerlerini mor, pembe ve yeşil renk haritası olarak çözümlemek", "yasakli_kelimeler": ["sahte renk haritası", "ire değerleri", "pembe ten rengi", "monitör pozlama", "pozometre ekranı"], "zorluk": "zor"},
    {"kelime": "anamorfik bokeh üretmek", "aciklama": "silindirik lens elemanlarıyla arka plan ışık noktalarını oval elips şekline sokmak", "yasakli_kelimeler": ["oval ışıklar", "elips bokeh", "silindirik eleman", "streak flare", "sinematik arka plan"], "zorluk": "zor"},
    {"kelime": "t-stop hassasiyetiyle çalışmak", "aciklama": "f-stop yerine lensten cam kaybı sonrası sensöre gerçek ulaşan ışık geçirgenliğini ölçmek", "yasakli_kelimeler": ["t stop", "gerçek ışık geçirgenliği", "f stop farkı", "sinema lensi", "ışık kaybı"], "zorluk": "zor"},
    {"kelime": "pratik ışık kaynakları", "aciklama": "sahne içindeki gerçek masa lambası veya abajuru kompozisyonun ana ışığı yapmak", "yasakli_kelimeler": ["practical light", "kadraj içi lamba", "abajur", "doğal ışık kaynağı", "sahne aydınlatması"], "zorluk": "zor"},
    {"kelime": "chivo lubezki tarzı çekmek", "aciklama": "tamamen doğal gün ışığı ve aşırı geniş açılı 14mm lensle kesintisiz akıcı takip", "yasakli_kelimeler": ["emmanuel lubezki", "doğal ışık kullanımı", "geniş açı takip", "the revenant", "birdman"], "zorluk": "zor"},
    {"kelime": "lut yükleyip izlemek", "aciklama": "monitöre 3d lut tablosu yükleyip soluk log görüntüyü sette son renk haliyle görmek", "yasakli_kelimeler": ["look up table", "3d lut", "monitör rengi", "sette ön izleme", "renk dönüşümü"], "zorluk": "zor"},
    {"kelime": "gobo ile gölge deseni basmak", "aciklama": "ışık kaynağının önüne pencereli veya yapraklı metal şablon koyup duvara desen düşürmek", "yasakli_kelimeler": ["metal şablon", "pencere gölgesi", "gobo", "desenli ışık", "optik projeksiyon"], "zorluk": "zor"},
    {"kelime": "hmi gün ışığı projektörü yakmak", "aciklama": "pencere dışına 18kw devasa metal halide projektör asıp içeri sahte güneş basmak", "yasakli_kelimeler": ["18k hmi", "metal halide", "sahte güneş", "pencere dışı vinç", "yüksek güç"], "zorluk": "zor"},
    {"kelime": "negatif dolgu ile kontrast artırmak", "aciklama": "yüzün gölge tarafına siyah kadife kumaş tutarak ortam sekmelerini emip gölgeyi koyulaştırmak", "yasakli_kelimeler": ["negative fill", "siyah kadife", "ışık emme", "sekme engelleme", "derin gölge"], "zorluk": "zor"}
]

sokaklezzetleri_verbs = [
    # Kolay (12)
    {"kelime": "közlemek", "aciklama": "mısır veya kestaneyi seyyar tezgahtaki kor mangalda pişirmek", "yasakli_kelimeler": ["kor", "mangal", "mısır", "kestane", "ateş"], "zorluk": "kolay"},
    {"kelime": "kızartmak", "aciklama": "kızgın yağ dolu kazanda lokma veya tulumba tatlısını kızartmak", "yasakli_kelimeler": ["yağ", "kazan", "lokma", "tulumba", "çıtır"], "zorluk": "kolay"},
    {"kelime": "haşlamak", "aciklama": "büyük kazanda kaynayan tuzlu suda mısır koçanlarını pişirmek", "yasakli_kelimeler": ["mısır koçanı", "kazan", "tuzlu su", "kaynatmak", "sıcak"], "zorluk": "kolay"},
    {"kelime": "doğramak", "aciklama": "kokoreç tezgahında iki satırla pişmiş bağırsağı tahtada kıymak", "yasakli_kelimeler": ["satır", "kokoreç", "kıymak", "tahta", "bağırsak"], "zorluk": "kolay"},
    {"kelime": "ısırmak", "aciklama": "çıtır sokak simidinden veya sıcacık tosttan büyük bir lokma koparmak", "yasakli_kelimeler": ["lokma", "çıtır simit", "tost", "ağız", "koparmak"], "zorluk": "kolay"},
    {"kelime": "satmak", "aciklama": "seyyar arabayla sokak sokak dolaşıp nohut pilav veya simit satmak", "yasakli_kelimeler": ["seyyar araba", "simitçi", "müşteri", "para", "sokak"], "zorluk": "kolay"},
    {"kelime": "dürmek", "aciklama": "lavaşın içine çiğ köfte veya tantuniyi koyup rulo halinde sarmak", "yasakli_kelimeler": ["dürüm", "lavaş", "çiğ köfte", "tantuni", "rulo"], "zorluk": "kolay"},
    {"kelime": "baharatlamak", "aciklama": "doğranan kokorecin üstüne bol pul biber, kekik ve kimyon serpmek", "yasakli_kelimeler": ["pul biber", "kekik", "kimyon", "tuz", "serpmek"], "zorluk": "kolay"},
    {"kelime": "limon sıkmak", "aciklama": "midye dolmanın veya balık ekmeğin üstüne yarım limonu bastırmak", "yasakli_kelimeler": ["midye dolma", "balık ekmek", "ekşi", "damla", "narenciye"], "zorluk": "kolay"},
    {"kelime": "paketlemek", "aciklama": "kağıt kese kağıdına kestane veya gazete kağıdına balık ekmek sarmak", "yasakli_kelimeler": ["kese kağıdı", "sarmak", "paket", "gazete", "paket servis"], "zorluk": "kolay"},
    {"kelime": "bağırmak", "aciklama": "simitçinin veya kestanecinin sokakta avazı çıktığı kadar tezgahını duyurması", "yasakli_kelimeler": ["seslenmek", "taze simit", "avaz", "çağırmak", "duyuru"], "zorluk": "kolay"},
    {"kelime": "tatmak", "aciklama": "seyyar arabanın önünde ayakta durup sıcak sokak lezzetini denemek", "yasakli_kelimeler": ["denemek", "ayakta yemek", "lezzet", "lezzetli", "açlık"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "şişe takmak", "aciklama": "kuzu bağırsaklarını ve uykuluğu yatay demir şişe kat kat sarmak", "yasakli_kelimeler": ["kokoreç şişi", "uykuluk", "demir mil", "kat kat", "sarma"], "zorluk": "orta"},
    {"kelime": "közde çevirmek", "aciklama": "uzun kokoreç şişini kömür ateşinin önünde kolu çevirerek nar gibi pişirmek", "yasakli_kelimeler": ["kömür ateşi", "çevirme", "kokoreç", "nar gibi", "yağ damlaması"], "zorluk": "orta"},
    {"kelime": "satırla kıymak", "aciklama": "sacdan alınan eti tahta üstünde iki elle çift satırla lokmalık doğramak", "yasakli_kelimeler": ["çift satır", "kıyım", "tahta darbesi", "ritmik ses", "kokoreç"], "zorluk": "orta"},
    {"kelime": "ekmek arasını doldurmak", "aciklama": "yarım somun ekmeğin içini açıp köfte, piyaz ve domatesle tepeleme doldurmak", "yasakli_kelimeler": ["yarım ekmek", "köfte ekmek", "piyaz", "tepeleme", "somun"], "zorluk": "orta"},
    {"kelime": "sacda çevirmek", "aciklama": "ortası çukur mersin tantuni sacında etleri pamuk yağı ve suyla kavurmak", "yasakli_kelimeler": ["tantuni sacı", "mersin", "pamuk yağı", "su serpme", "buhar"], "zorluk": "orta"},
    {"kelime": "şerbete basmak", "aciklama": "kızgın yağdan çıkan sıcak halka tatlısını soğuk şeker şerbetine daldırmak", "yasakli_kelimeler": ["halka tatlısı", "soğuk şerbet", "tatlıcı", "çıtır", "daldırma"], "zorluk": "orta"},
    {"kelime": "çiğ köfte yoğurmak", "aciklama": "tırtıklı bakır tepside esmer bulguru isot ve salçayla saatlerce ezmek", "yasakli_kelimeler": ["bakır tepsi", "isot", "esmer bulgur", "yoğurma", "kol gücü"], "zorluk": "orta"},
    {"kelime": "sıkım yapmak", "aciklama": "yoğrulan çiğ köfteyi avuç içinde sıkarak parmak izli lokmalar dökmek", "yasakli_kelimeler": ["avuç içi", "parmak izi", "sıkma", "marul", "lokma"], "zorluk": "orta"},
    {"kelime": "midye kabuğu açmak", "aciklama": "kapağı tek elle bıçak gibi kırıp içindeki pirinçli dolmayı öne çıkarmak", "yasakli_kelimeler": ["midyeci", "tek el", "kabuk kırma", "pirinçli", "tezgah"], "zorluk": "orta"},
    {"kelime": "nohutlu pilav çekmek", "aciklama": "camlı seyyar arabadan kepçeyle tabağa tereyağlı nohutlu pirinç ve tavuk koymak", "yasakli_kelimeler": ["pilav arabası", "tavuk nohut", "cam tezgah", "kepçe", "karabiber"], "zorluk": "orta"},
    {"kelime": "turşu suyu içmek", "aciklama": "plastik bardaktaki acılı lahana ve salatalık turşusu suyunu diklemek", "yasakli_kelimeler": ["acılı şalgam", "plastik bardak", "lahana turşusu", "sirke limon", "tuzlu ekşi"], "zorluk": "orta"},
    {"kelime": "balık ızgaralamak", "aciklama": "eminönü teknesinde taze palamut veya uskumru filetosunu sac ızgarada pişirmek", "yasakli_kelimeler": ["eminönü teknesi", "uskumru", "fileto", "ızgara", "duman"], "zorluk": "orta"},
    {"kelime": "kestane çizmek", "aciklama": "pişerken patlamaması ve kolay soyulması için kestanenin kabuğuna bıçakla çizik atmak", "yasakli_kelimeler": ["çizik", "kabuk bıçağı", "patlama engeli", "kestaneci", "kış lezzeti"], "zorluk": "orta"},
    {"kelime": "simit tablasını taşımak", "aciklama": "başın üstündeki yuvarlak ahşap tablaya dizili 50 simitle caddelerde yürümek", "yasakli_kelimeler": ["baş üstü", "ahşap tabla", "simitçi", "susam", "denge"], "zorluk": "orta"},
    {"kelime": "boza mayalamak", "aciklama": "darı ve mısır ununu fermente edip kış geceleri leblebi ve tarçınla sunmak", "yasakli_kelimeler": ["darı", "vefa bozası", "tarçın leblebi", "kış gecesi", "sokak satıcısı"], "zorluk": "orta"},
    {"kelime": "kağıt helva basmak", "aciklama": "iki yuvarlak çıtır gofret yaprağı arasına dondurma veya leblebi tozu koymak", "yasakli_kelimeler": ["gofret", "dondurma arası", "çıtır", "yuvarlak", "çocuk lezzeti"], "zorluk": "orta"},
    {"kelime": "macun sarmak", "aciklama": "tepsideki rengarenk osmanlı macunlarını tahta çubuğa burgu gibi sarmak", "yasakli_kelimeler": ["osmanlı macunu", "renkli şifalı", "tahta çubuk", "tepsi", "baharatlı tatlı"], "zorluk": "orta"},
    {"kelime": "ıslak burger buharlamak", "aciklama": "sarımsaklı domates sosuna batırılmış köfteli sandviçi cam buhar kutusunda bekletmek", "yasakli_kelimeler": ["taksim", "buhar kutusu", "sarımsaklı sos", "nemli ekmek", "gece atıştırmalığı"], "zorluk": "orta"},
    {"kelime": "buzlu badem soymak", "aciklama": "büyük buz kalıbı üstünde duran taze tatlı bademlerin kabuğunu sıyırıp ikram etmek", "yasakli_kelimeler": ["buz kalıbı", "taze badem", "kabuk soyma", "meyhane önü", "serin atıştırmalık"], "zorluk": "orta"},
    {"kelime": "kumpir ezmek", "aciklama": "fırınlanmış koca patatesi ortadan yarıp tereyağı ve kaşarla krema gibi ezmek", "yasakli_kelimeler": ["ortaköy", "fırın patates", "kaşar tereyağı", "rus salatası", "malzeme seçimi"], "zorluk": "orta"},
    {"kelime": "gözleme açmak", "aciklama": "yer sofrasında oklavayla yufkayı açıp içine peynir koyup sac üstünde pişirmek", "yasakli_kelimeler": ["sac üstü", "yufka", "oklava", "peynirli ıspanaklı", "köy gözlemesi"], "zorluk": "orta"},
    {"kelime": "şalgam doldurmak", "aciklama": "seyyar arabadan koca cam kavanozdaki mor acılı şalgamı taneleriyle bardağa almak", "yasakli_kelimeler": ["mor havuç", "acılı", "adana usulü", "tane", "kavanoz"], "zorluk": "orta"},
    {"kelime": "tükürük köftesi kızartmak", "aciklama": "maç çıkışında stadyum önündeki dumanaltı seyyar arabada küçük köfteleri çevirmek", "yasakli_kelimeler": ["stadyum önü", "maç çıkışı", "dumanaltı", "ekmek arası köfte", "seyyar ızgara"], "zorluk": "orta"},
    {"kelime": "pamuk şeker sarmak", "aciklama": "dönen sıcak makine haznesinden çıkan şeker ipliklerini tahta çubuğa dolamak", "yasakli_kelimeler": ["şeker ipliği", "pembe bulut", "dönen hazne", "çubuk", "panayır"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "şırdan doldurmak", "aciklama": "geviş getiren hayvanın 4. mide odacığını baharatlı pirinç harcıyla doldurup dikmek", "yasakli_kelimeler": ["adana sokakları", "4. mide", "bağırsak harcı", "kimyonlu", "gece sakatatı"], "zorluk": "zor"},
    {"kelime": "mumbar bağırsağı doldurmak", "aciklama": "koyunun kalın bağırsağını tersyüz edip içi pirinç ve kıymayla harçlayıp haşlamak", "yasakli_kelimeler": ["kalın bağırsak", "tersyüz etme", "sakatat dolması", "baharatlı pirinç", "kazanda haşlama"], "zorluk": "zor"},
    {"kelime": "bici bici buzlamak", "aciklama": "nişasta muhallebisinin üstüne rende buz, gül suyu, pudra şekeri ve şurup dökmek", "yasakli_kelimeler": ["adana tatlısı", "rende buz", "gül suyu", "nişasta karesi", "kırmızı şurup"], "zorluk": "zor"},
    {"kelime": "uykuluk ızgaralamak", "aciklama": "süt kuzusunun timus ve pankreas bezlerini sütlüye ve gerdana göre kömürde pişirmek", "yasakli_kelimeler": ["sütlüce", "timus bezi", "pankreas", "kuzu sakatatı", "yumuşak doku"], "zorluk": "zor"},
    {"kelime": "torik lakerdası dilimlemek", "aciklama": "iri torik balığını takoz kesip omurilik iliğini boşaltarak tuzlu salamurada olgunlaştırmak", "yasakli_kelimeler": ["torik takoz", "omurilik temizleme", "tuzlu salamura", "kırmızı soğan", "balık mezesi"], "zorluk": "zor"},
    {"kelime": "kokoreç sarmak", "aciklama": "içyağı ve çöz yağını şişe doladıktan sonra üstüne yüzlerce metre ince bağırsağı sıkıca örmek", "yasakli_kelimeler": ["çöz yağı", "içyağı", "mumbar bağırsak", "şişe örme", "kasaplık ustalığı"], "zorluk": "zor"},
    {"kelime": "tarihi vefa bozası içmek", "aciklama": "1876'dan kalma mermer dükkanda kalın kıvamlı ekşimsi darı bozasını kadehte kaşıklamak", "yasakli_kelimeler": ["vefa", "1876", "mermer tezgah", "ekşimsi darı", "kadeh"], "zorluk": "zor"},
    {"kelime": "çöp şiş dizmek", "aciklama": "kürdan kalınlığındaki minik ahşap şişlere marine kuzu eti ve kuyruk yağını dizmek", "yasakli_kelimeler": ["selçuk germencik", "minik şiş", "kuyruk yağı", "kürdan boy", "ocakbaşı"], "zorluk": "zor"},
    {"kelime": "çiğ köfteyi tavana fırlatmak", "aciklama": "kıvamını ve yapışkanlığını test etmek için bir parça köfteyi tavana atıp yapışmasını izlemek", "yasakli_kelimeler": ["tavana yapışma", "kıvam testi", "usta şovu", "düşmeme", "yoğurma sonu"], "zorluk": "zor"},
    {"kelime": "kelle söğüş doğramak", "aciklama": "haşlanmış koyun kellesinden beyin, dil, yanak ve göz etini tahtada harmanlamak", "yasakli_kelimeler": ["izmir söğüş", "kelle eti", "beyin dil yanak", "soğuk sakatat", "dürüm içi"], "zorluk": "zor"},
    {"kelime": "pişi kabartmak", "aciklama": "mayalı hamur bezelerini parmakla delip kızgın yağ kazanında altın rengi balon gibi şişirmek", "yasakli_kelimeler": ["mayalı hamur", "balon gibi şişme", "yağda kızartma", "lokma zıttı", "kahvaltılık sokak"], "zorluk": "zor"},
    {"kelime": "nohut mayası tutturmak", "aciklama": "kırılmış kuru nohut ve sıcak suyla geleneksel tatlı maya üreterek sokak çöreği yapmak", "yasakli_kelimeler": ["tatlı maya", "nohut fermantasyonu", "doğal maya", "kumru ekmeği", "gece mayalama"], "zorluk": "zor"},
    {"kelime": "cezerye kazımak", "aciklama": "büyük bakır kazanda havuç, şeker ve cevizle saatlerce pişen karamelize pestili kesmek", "yasakli_kelimeler": ["karamelize havuç", "bakır kazan", "hindistan cevizi", "mersin lokumu", "yoğun tatlı"], "zorluk": "zor"},
    {"kelime": "boyoz fırınlamak", "aciklama": "bol zeytinyağlı mayasız katmerli hamuru yüksek ateşli taş fırında fırınlanmış yumurtayla sunmak", "yasakli_kelimeler": ["izmir lezzeti", "fırınlanmış yumurta", "katmerli hamur", "yağlı çörek", "sefared mutfağı"], "zorluk": "zor"}
]

if __name__ == "__main__":
    add_and_save_verbs("sinematografi", sinematografi_verbs)
    add_and_save_verbs("sokaklezzetleri", sokaklezzetleri_verbs)
