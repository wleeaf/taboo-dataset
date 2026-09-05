# -*- coding: utf-8 -*-
from card_utils import add_and_save_verbs

telekomunikasyon_verbs = [
    # Kolay (12)
    {"kelime": "aramak", "aciklama": "telefondan numarayı tuşlayıp karşı tarafın çalmasını sağlamak", "yasakli_kelimeler": ["telefon", "numara", "çağrı", "alo", "tuşlamak"], "zorluk": "kolay"},
    {"kelime": "mesaj göndermek", "aciklama": "sms veya sohbet uygulamasından metin iletmek", "yasakli_kelimeler": ["sms", "metin", "iletmek", "yazmak", "telefon"], "zorluk": "kolay"},
    {"kelime": "konuşmak", "aciklama": "ahizeyi veya kulaklığı takıp karşıdaki kişiyle sesli iletişim kurmak", "yasakli_kelimeler": ["ses", "ahize", "kulaklık", "iletişim", "sohbet"], "zorluk": "kolay"},
    {"kelime": "bağlanmak", "aciklama": "telefon veya bilgisayarla kablosuz wifi veya mobil internet ağına girmek", "yasakli_kelimeler": ["wifi", "internet", "ağ", "mobil", "erişim"], "zorluk": "kolay"},
    {"kelime": "çekmek", "aciklama": "telefonun baz istasyonundan güçlü radyo sinyali alması", "yasakli_kelimeler": ["şebeke", "sinyal", "baz istasyonu", "diş", "kapsama"], "zorluk": "kolay"},
    {"kelime": "kesilmek", "aciklama": "tünelde veya dağda telefon sinyalinin aniden kaybolup çağrının düşmesi", "yasakli_kelimeler": ["kopmak", "düşmek", "sinyal yok", "hat", "tünel"], "zorluk": "kolay"},
    {"kelime": "şarj etmek", "aciklama": "telefonun pilini şarj aletiyle prize takıp doldurmak", "yasakli_kelimeler": ["priz", "kablo", "batarya", "pil", "doldurmak"], "zorluk": "kolay"},
    {"kelime": "indirmek", "aciklama": "internet bağlantısıyla dosyayı veya videoyu telefona çekmek", "yasakli_kelimeler": ["download", "dosya", "video", "veri", "kaydetmek"], "zorluk": "kolay"},
    {"kelime": "yüklemek", "aciklama": "telefondaki fotoğrafı veya belgeyi sunucuya göndermek", "yasakli_kelimeler": ["upload", "göndermek", "sunucu", "fotoğraf", "bulut"], "zorluk": "kolay"},
    {"kelime": "tuşlamak", "aciklama": "telefon ekranında veya klavyesinde rakamlara basmak", "yasakli_kelimeler": ["rakam", "ekran", "klavye", "basmak", "numara"], "zorluk": "kolay"},
    {"kelime": "kapatmak", "aciklama": "konuşma bitince kırmızı butona basıp hattı sonlandırmak", "yasakli_kelimeler": ["sonlandırmak", "kırmızı buton", "ahize", "bitirmek", "çağrı"], "zorluk": "kolay"},
    {"kelime": "yönlendirmek", "aciklama": "ulaşılamayan telefonu başka bir numaraya aktarmak", "yasakli_kelimeler": ["aktarma", "başka numara", "meşgul", "ulaşılamıyor", "çağrı yönlendirme"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "baz istasyonu dikmek", "aciklama": "tepelere veya çatıya mobil haberleşme anten kuleleri monte etmek", "yasakli_kelimeler": ["anten kulesi", "mobil anten", "çatı", "şebeke yayılımı", "direk"], "zorluk": "orta"},
    {"kelime": "fiber kablo çekmek", "aciklama": "sokakları kazıp yer altına ışık hızında cam optik internet hatları döşemek", "yasakli_kelimeler": ["fiber optik", "yer altı kazısı", "cam kablo", "hızlı internet", "altyapı"], "zorluk": "orta"},
    {"kelime": "sim kart takmak", "aciklama": "operatörün verdiği mikro çipli kartı telefonun tepsisine yerleştirmek", "yasakli_kelimeler": ["sim kart", "çip", "operatör", "iğne", "tepsi"], "zorluk": "orta"},
    {"kelime": "roaming açmak", "aciklama": "yurt dışına çıkınca hattın yabancı operatör şebekesine bağlanmasını sağlamak", "yasakli_kelimeler": ["yurt dışı", "uluslararası dolaşım", "yabancı operatör", "tarife", "şebeke geçişi"], "zorluk": "orta"},
    {"kelime": "modem resetlemek", "aciklama": "interneti kopan modemin arkasındaki minik düğmeye iğneyle basıp sıfırlamak", "yasakli_kelimeler": ["modem", "sıfırlama", "yeniden başlatma", "kopma", "arkadaki delik"], "zorluk": "orta"},
    {"kelime": "hız testi yapmak", "aciklama": "speedtest sitesinden indirme ve yükleme megabit hızını ölçmek", "yasakli_kelimeler": ["speedtest", "megabit", "download hızı", "upload hızı", "ping"], "zorluk": "orta"},
    {"kelime": "ping süresi ölçmek", "aciklama": "bilgisayardan sunucuya gönderilen sinyalin milisaniye cinsinden gecikmesini bulmak", "yasakli_kelimeler": ["gecikme", "milisaniye", "ms", "lag", "sunucu yanıtı"], "zorluk": "orta"},
    {"kelime": "uyduya sinyal göndermek", "aciklama": "yer istasyonundaki çanak antenle uzaydaki haberleşme uydusuna veri yollamak", "yasakli_kelimeler": ["türksat", "çanak anten", "uzay", "haberleşme uydusu", "uplink"], "zorluk": "orta"},
    {"kelime": "santralde hat bağlamak", "aciklama": "gelen telefon çağrısını dahili numara santralinden ilgili masaya aktarmak", "yasakli_kelimeler": ["dahili hat", "telefon santrali", "operatör masası", "aktarma", "pabx"], "zorluk": "orta"},
    {"kelime": "ip adresi atamak", "aciklama": "dhcp sunucusuyla ağa yeni katılan telefona otomatik yerel ip vermek", "yasakli_kelimeler": ["dhcp", "yerel ip", "otomatik atama", "ağ adresi", "yönlendirici"], "zorluk": "orta"},
    {"kelime": "frekans bandı tahsis etmek", "aciklama": "devlet kurumunun 5g veya radyo yayını için operatörlere megaherz bandı ihale etmesi", "yasakli_kelimeler": ["btk", "spektrum", "ihale", "megaherz", "radyo bandı"], "zorluk": "orta"},
    {"kelime": "kapsama alanı haritalamak", "aciklama": "şehirdeki sinyal gücünü sokak sokak test aracıyla gezip haritaya işlemek", "yasakli_kelimeler": ["drive test", "sinyal gücü", "kapsama", "harita", "ölçüm aracı"], "zorluk": "orta"},
    {"kelime": "kablo eki yapmak", "aciklama": "kopan bakır veya fiber kablo uçlarını özel kaynak makinesiyle kaynatmak", "yasakli_kelimeler": ["fiber füzyon ek", "kaynak makinesi", "kopuk kablo", "ek kutusu", "birleştirme"], "zorluk": "orta"},
    {"kelime": "hotspot paylaşmak", "aciklama": "telefonun mobil internetini kablosuz ağ açarak yanındaki bilgisayara dağıtmak", "yasakli_kelimeler": ["kişisel erişim noktası", "mobil veri paylaşımı", "tethering", "kablosuz dağıtım", "wifi açma"], "zorluk": "orta"},
    {"kelime": "voip ile aramak", "aciklama": "telefon hattı yerine internet protokolü üzerinden sesli arama yapmak", "yasakli_kelimeler": ["internet üzerinden ses", "skype", "whatsapp arama", "sip protokolü", "dijital ses"], "zorluk": "orta"},
    {"kelime": "dijital abone hattı kurmak", "aciklama": "eski bakır telefon hatlarından yüksek hızlı adsl ve vdsl internet geçirmek", "yasakli_kelimeler": ["adsl", "vdsl", "bakır hat", "splitter", "ev interneti"], "zorluk": "orta"},
    {"kelime": "bant genişliği artırmak", "aciklama": "şebekedeki veri taşıma kapasitesini gigabit seviyesine yükseltmek", "yasakli_kelimeler": ["bandwidth", "kapasite", "veri trafiği", "gigabit", "hız artışı"], "zorluk": "orta"},
    {"kelime": "yönlendirici yapılandırmak", "aciklama": "router cihazına girip port yönlendirme ve nat kurallarını ayarlamak", "yasakli_kelimeler": ["router", "port açma", "nat kuralı", "arayüz", "yönlendirme"], "zorluk": "orta"},
    {"kelime": "numara taşımak", "aciklama": "kendi telefon numarasını değiştirmeden başka bir operatör şirketine geçmek", "yasakli_kelimeler": ["operatör değişikliği", "aynı numara", "taşıma", "tarife geçişi", "sim değişimi"], "zorluk": "orta"},
    {"kelime": "telsiz mandallamak", "aciklama": "polis veya güvenlik telsizinin yanındaki ptt butonuna basıp konuşmak", "yasakli_kelimeler": ["ptt butonu", "anons", "bas konuş", "polis telsizi", "kanal"], "zorluk": "orta"},
    {"kelime": "paket kaybı yaşamak", "aciklama": "ağ yoğunluğundan gönderilen veri paketlerinin hedefe ulaşamadan silinmesi", "yasakli_kelimeler": ["packet loss", "takılma", "kopma", "ağ yoğunluğu", "ulaşamayan veri"], "zorluk": "orta"},
    {"kelime": "kriptolu telsiz kullanmak", "aciklama": "askeri operasyonda dinlenmeyi önlemek için frekans atlamalı şifreli haberleşmek", "yasakli_kelimeler": ["şifreli haberleşme", "frekans atlama", "dinleme engeli", "askeri telsiz", "aseksan"], "zorluk": "orta"},
    {"kelime": "tarife yenilemek", "aciklama": "taahhüt süresi biten faturasız veya faturalı hat için yeni dakika paketi seçmek", "yasakli_kelimeler": ["taahhüt", "dakika sms internet", "fatura", "paket", "sözleşme"], "zorluk": "orta"},
    {"kelime": "çağrı merkezine bağlanmak", "aciklama": "müşteri hizmetlerini arayıp telesekreter menüsünden temsilciye ulaşmak", "yasakli_kelimeler": ["müşteri hizmetleri", "telesekreter", "temsilci", "sıra bekleme", "sesli yanıt"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "mimo anten hüzmeleme yapmak", "aciklama": "5g baz istasyonunda 64 antenle radyo dalgalarını doğrudan kullanıcının telefonuna odaklamak", "yasakli_kelimeler": ["massive mimo", "beamforming", "hüzme oluşturma", "64x64 anten", "5g baz istasyonu"], "zorluk": "zor"},
    {"kelime": "ofdm modülasyonu uygulamak", "aciklama": "geniş bandı birbirine dik yüzlerce alt taşıyıcı frekansa bölerek veri basmak", "yasakli_kelimeler": ["dik frekans bölmeli", "alt taşıyıcı", "spektrum verimi", "lte modülasyonu", "qam"], "zorluk": "zor"},
    {"kelime": "handover gerçekleştirmek", "aciklama": "hızla giden trende telefonun kesintisiz bir baz istasyonundan diğerine devrolması", "yasakli_kelimeler": ["el değiştirme", "kesintisiz devir", "baz istasyonu geçişi", "hücre transferi", "şebeke aktarımı"], "zorluk": "zor"},
    {"kelime": "qam konstelasyonu çözmek", "aciklama": "hem genlik hem faz kaymasıyla tek sembolde 8 veya 10 bit veri taşıyan sinyali işlemek", "yasakli_kelimeler": ["1024 qam", "takımyıldız diyagramı", "faz ve genlik", "sembol hızı", "modülasyon"], "zorluk": "zor"},
    {"kelime": "dwdm dalga boyu çoğullama", "aciklama": "tek bir fiber kıl içinden farklı renklerde 80 ayrı lazer dalga boyunu aynı anda iletmek", "yasakli_kelimeler": ["yoğun dalga boyu", "tek kıl fiber", "terabit hız", "lazer taşıyıcı", "optik çoğullama"], "zorluk": "zor"},
    {"kelime": "network slicing kurgulamak", "aciklama": "tek bir 5g fiziksel şebekesini otonom araçlar ve fabrikalar için sanal bağımsız dilimlere bölmek", "yasakli_kelimeler": ["ağ dilimleme", "5g sanallaştırma", "düşük gecikme", "özelleşmiş hat", "servis kalitesi"], "zorluk": "zor"},
    {"kelime": "otdr ile fiber kırığı bulmak", "aciklama": "kabloya lazer darbesi yollayıp geri yansıyan ışıktan kırığın kaçıncı kilometrede olduğunu metreyle saptamak", "yasakli_kelimeler": ["optik zaman alanı", "yansıma ölçer", "kırık tespiti", "mesafe hesabı", "arıza bulma"], "zorluk": "zor"},
    {"kelime": "oran mimarisini sanallaştırmak", "aciklama": "baz istasyonlarının radyo donanımlarını açık kaynaklı yazılım tabanlı buluta taşımak", "yasakli_kelimeler": ["open ran", "vran", "yazılım tanımlı radyo", "donanım bağımsız", "bulut baz istasyonu"], "zorluk": "zor"},
    {"kelime": "ss7 güvenlik açığı sömürmek", "aciklama": "küresel telekomünikasyon yönlendirme protokolündeki zayıflıkla sms onay kodlarını araya girip çalmak", "yasakli_kelimeler": ["sinyalizasyon sistemi 7", "sms ele geçirme", "hücresel protokol", "küresel açık", "konum takibi"], "zorluk": "zor"},
    {"kelime": "core network paket yönlendirme", "aciklama": "mobil şebekenin çekirdek sunucularında upf ve amf fonksiyonlarıyla kullanıcı oturumu yönetmek", "yasakli_kelimeler": ["5g core", "upf", "amf", "paket çekirdeği", "epc"], "zorluk": "zor"},
    {"kelime": "doppler kaymasını telafi etmek", "aciklama": "hızlı tren veya alçak irtifa uydusunda hareket sebebiyle kayan radyo frekansını dijital düzeltmek", "yasakli_kelimeler": ["doppler etkisi", "frekans kayması", "yüksek hız", "leo uyduları", "taşıyıcı telafisi"], "zorluk": "zor"},
    {"kelime": "snr sinyal gürültü oranı", "aciklama": "alıcıya ulaşan faydalı sinyal gücünün termal gürültüye oranını desibel cinsinden optimize etmek", "yasakli_kelimeler": ["signal to noise", "gürültü tabanı", "desibel", "kanal kapasitesi", "shannon teoremi"], "zorluk": "zor"},
    {"kelime": "e-band milimetrik dalga atmak", "aciklama": "baz istasyonları arasına fiber çekilemeyen yerlerde 80 ghz radyo linkle 10 gigabit basmak", "yasakli_kelimeler": ["milimetrik dalga", "80 ghz", "e band", "kablosuz omurga", "radyolink"], "zorluk": "zor"},
    {"kelime": "urllc standardını tutturmak", "aciklama": "endüstriyel robotlar ve cerrahi için 1 milisaniyenin altında ultra güvenilir düşük gecikme sağlamak", "yasakli_kelimeler": ["1 milisaniye", "ultra güvenilir", "düşük gecikme", "5g endüstri", "otonom kontrol"], "zorluk": "zor"}
]

temizlik_verbs = [
    # Kolay (12)
    {"kelime": "süpürmek", "aciklama": "süpürgeyle yerdeki toz ve kırıntıları faraşa toplamak", "yasakli_kelimeler": ["süpürge", "toz", "kırıntı", "faraş", "zemin"], "zorluk": "kolay"},
    {"kelime": "paspaslamak", "aciklama": "ıslak ve deterjanlı viledayla yer karolarını silip parlatmak", "yasakli_kelimeler": ["vileda", "ıslak", "kova", "fayans", "silmek"], "zorluk": "kolay"},
    {"kelime": "toz almak", "aciklama": "nemli mikro fiber bezle mobilya ve sehpa üzerindeki tozları silmek", "yasakli_kelimeler": ["mikrofiber bez", "nemli", "sehpa", "mobilya", "toz"], "zorluk": "kolay"},
    {"kelime": "yıkamak", "aciklama": "kirli çamaşırları veya bulaşıkları deterjan ve suyla arındırmak", "yasakli_kelimeler": ["deterjan", "su", "çamaşır", "bulaşık", "makine"], "zorluk": "kolay"},
    {"kelime": "durulamak", "aciklama": "sabunlanan yüzeyi veya tabağı temiz bol suyla köpükten arındırmak", "yasakli_kelimeler": ["bol su", "köpük", "arındırma", "sabun", "akıtmak"], "zorluk": "kolay"},
    {"kelime": "kurulamak", "aciklama": "yıkanan bardak veya elleri kuru havluyla silip nemini almak", "yasakli_kelimeler": ["havlu", "ıslak", "nem", "bez", "bardak"], "zorluk": "kolay"},
    {"kelime": "ovmak", "aciklama": "yanmış tencereyi tel ve cif ile bastırarak ovup lekeyi çıkarmak", "yasakli_kelimeler": ["bulaşık teli", "cif", "bastırmak", "tencere", "leke"], "zorluk": "kolay"},
    {"kelime": "parlatmak", "aciklama": "camları camsil ve gazete kağıdıyla iz bırakmadan silip pırıl pırıl yapmak", "yasakli_kelimeler": ["camsil", "cam", "gazete", "pırıl pırıl", "izsiz"], "zorluk": "kolay"},
    {"kelime": "havalandırmak", "aciklama": "odanın pencerelerini açıp içeri temiz hava girmesini sağlamak", "yasakli_kelimeler": ["pencere", "temiz hava", "açmak", "koku", "oda"], "zorluk": "kolay"},
    {"kelime": "çöp atmak", "aciklama": "dolan çöp torbasını bağlayıp sokaktaki konteynere götürmek", "yasakli_kelimeler": ["çöp torbası", "konteynır", "bağlamak", "atık", "kovası"], "zorluk": "kolay"},
    {"kelime": "fırçalamak", "aciklama": "lavabo veya banyo derzlerini sert kıllı fırçayla fırçalayıp temizlemek", "yasakli_kelimeler": ["sert fırça", "lavabo", "derz", "banyo", "kir"], "zorluk": "kolay"},
    {"kelime": "köpürtmek", "aciklama": "sünger üzerine bulaşık deterjanı döküp sıkarak yoğun köpük yapmak", "yasakli_kelimeler": ["sünger", "deterjan", "baloncuk", "köpük", "bulaşık"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "çamaşır suyu dökmek", "aciklama": "klozete yoğun kıvamlı klorlu hijyen sıvısı döküp mikropları öldürmek", "yasakli_kelimeler": ["klor", "hijyen", "klozet", "mikrop kırma", "beyazlatıcı"], "zorluk": "orta"},
    {"kelime": "kireç çözmek", "aciklama": "çaydanlığın tabanında biriken kireç taşını asitli kireç çözücüyle sökmek", "yasakli_kelimeler": ["çaydanlık", "porçöz", "kireç taşı", "asit", "taban"], "zorluk": "orta"},
    {"kelime": "yağ çözücü sıkmak", "aciklama": "ocak üstündeki ve davlumbazdaki yapışkan kurumuş yağları kimyasalla eritmek", "yasakli_kelimeler": ["davlumbaz", "ocak", "kurumuş yağ", "sprey", "eritme"], "zorluk": "orta"},
    {"kelime": "halı yıkamak", "aciklama": "balkonda veya halı yıkama makinesinde bol şampuanla fırçalayıp yıkamak", "yasakli_kelimeler": ["halı şampuanı", "yıkama makinesi", "balkon", "fırça", "kurutma"], "zorluk": "orta"},
    {"kelime": "derz aralarını temizlemek", "aciklama": "banyo fayansları arasındaki kararmış derz dolgularını fırça ve çamaşır suyuyla beyazlatmak", "yasakli_kelimeler": ["fayans arası", "kararma", "derz kalemi", "beyazlatma", "banyo"], "zorluk": "orta"},
    {"kelime": "koltuk silmek", "aciklama": "koltuk kumaşındaki lekeleri arap sabunu ve mikrofiber bezle bastırarak çıkarmak", "yasakli_kelimeler": ["kumaş", "leke çıkarma", "arap sabunu", "döşeme", "silme"], "zorluk": "orta"},
    {"kelime": "leke çıkarmak", "aciklama": "beyaz gömleğe dökülen vişne veya kahve lekesine leke çıkarıcı sprey sıkmak", "yasakli_kelimeler": ["leke çıkarıcı", "kahve lekesi", "vişne", "gömlek", "oksilift"], "zorluk": "orta"},
    {"kelime": "cam çekçeği kullanmak", "aciklama": "köpüklenen pencere camındaki suyu lastik çekçekle yukarıdan aşağıya sıyırmak", "yasakli_kelimeler": ["lastik çekçek", "pencere", "su sıyırma", "iz bırakmadan", "yukarıdan aşağı"], "zorluk": "orta"},
    {"kelime": "perdeleri yıkamak", "aciklama": "tülleri kornişten tek tek söküp makinede hassas programda yıkamak", "yasakli_kelimeler": ["tül perde", "korniş", "hassas program", "düğme", "asma"], "zorluk": "orta"},
    {"kelime": "bulaşık makinesi doldurmak", "aciklama": "kirli tabak, çatal ve tencereleri sepetlere dizip tableti hazneye koymak", "yasakli_kelimeler": ["tablet deterjan", "sepet dizilimi", "tabak çatal", "pervane", "program"], "zorluk": "orta"},
    {"kelime": "çamaşır asmak", "aciklama": "makineden çıkan ıslak kıyafetleri mandallarla balkondaki ipe tutturmak", "yasakli_kelimeler": ["mandal", "çamaşır ipi", "kurutmalık", "balkon", "ıslak çamaşır"], "zorluk": "orta"},
    {"kelime": "baca temizlemek", "aciklama": "şömine veya soba borularındaki kurumları tel süpürgeyle aşağı dökmek", "yasakli_kelimeler": ["kurum", "soba borusu", "şömine", "baca fırçası", "is"], "zorluk": "orta"},
    {"kelime": "dezenfekte etmek", "aciklama": "kapı kollarını ve masaları alkollü solüsyonla silip virüsleri yok etmek", "yasakli_kelimeler": ["alkol bazlı", "kapı kolları", "virüs kırma", "antiseptik", "yüzey"], "zorluk": "orta"},
    {"kelime": "lavabo açmak", "aciklama": "tıkanan mutfak lavabosuna kostik kimyasal döküp üstüne kaynar su boşaltmak", "yasakli_kelimeler": ["lavabo açıcı", "kostik", "kaynar su", "tıkanıklık", "gider"], "zorluk": "orta"},
    {"kelime": "buzdolabı temizlemek", "aciklama": "rafları söküp sirkeli suyla silerek kötü kokuları ve döküntüleri arındırmak", "yasakli_kelimeler": ["sirkeli su", "raf", "kötü koku", "bozuk gıda", "dolap içi"], "zorluk": "orta"},
    {"kelime": "robot süpürge çalıştırmak", "aciklama": "akıllı otonom süpürgenin harita çıkarıp yerdeki tozları kendi kendine çekmesi", "yasakli_kelimeler": ["akıllı süpürge", "otonom", "haritalama", "kendi kendine", "şarj istasyonu"], "zorluk": "orta"},
    {"kelime": "sirke ile silmek", "aciklama": "kimyasal kullanmadan beyaz sirke ve karbonatla doğal hijyen sağlamak", "yasakli_kelimeler": ["beyaz sirke", "karbonat", "doğal temizlik", "kimyasalsız", "kireç"], "zorluk": "orta"},
    {"kelime": "küf temizlemek", "aciklama": "banyo tavanında nemden oluşan siyah küf lekelerine mantar öldürücü sprey sıkmak", "yasakli_kelimeler": ["siyah küf", "banyo tavanı", "mantar ilacı", "nem lekesi", "sprey"], "zorluk": "orta"},
    {"kelime": "pas sökmek", "aciklama": "oksitlenen metal eşyalara pas sökücü sıvı döküp telle ovarak arındırmak", "yasakli_kelimeler": ["pas sökücü", "wd40", "korozyon", "metal tel", "oksit"], "zorluk": "orta"},
    {"kelime": "ütü kirecini temizlemek", "aciklama": "buhar deliklerini tıkayan beyaz kireç parçalarını sirkeli su kaynatarak dökmek", "yasakli_kelimeler": ["buhar delikleri", "ütü kireci", "sirkeli kaynatma", "tıkanma", "taban"], "zorluk": "orta"},
    {"kelime": "gardırop düzenlemek", "aciklama": "dağılan dolap içindeki kazak ve pantolonları yeniden katlayıp askılara dizmek", "yasakli_kelimeler": ["askı", "dolap içi", "düzen", "katlama", "mevsim geçişi"], "zorluk": "orta"},
    {"kelime": "ayakkabı boyamak", "aciklama": "deri kösele ayakkabıyı fırçalayıp vaks sürerek parlatmak", "yasakli_kelimeler": ["ayakkabı boyası", "vaks", "cila fırçası", "parlatma", "kösele"], "zorluk": "orta"},
    {"kelime": "gümüş parlatmak", "aciklama": "kararan antika gümüş kaşık ve tepsileri özel kremle ovarak ayna gibi yapmak", "yasakli_kelimeler": ["kararmış gümüş", "gümüş parlatıcı", "antika tepsi", "ovalama", "krem"], "zorluk": "orta"},
    {"kelime": "fırın içi temizlemek", "aciklama": "fırın tabanına yapışan yanık yağ tabakasını köpük fırın spreyiyle çözmek", "yasakli_kelimeler": ["fırın spreyi", "yanık yağ", "rezistans", "köpük kimyasal", "tepsi"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "otoklavda sterilizasyon", "aciklama": "tıbbi aletleri 134 derece basınçlı doymuş buhar altında tüm mikroplardan arındırmak", "yasakli_kelimeler": ["134 derece", "basınçlı buhar", "tıbbi alet", "spor öldürme", "tam sterilite"], "zorluk": "zor"},
    {"kelime": "ozon gazıyla dezenfekte", "aciklama": "odadaki havalandırmaya ozon jeneratörü bağlayıp tüm virüs ve kokuları moleküler parçalamak", "yasakli_kelimeler": ["ozon jeneratörü", "o3 gazı", "hava sterilizasyonu", "moleküler parçalama", "koku giderme"], "zorluk": "zor"},
    {"kelime": "ultrasonik banyoda yıkamak", "aciklama": "yüksek frekanslı ses dalgalarının sıvı içinde patlattığı mikro kavitasyon kabarcıklarıyla temizlemek", "yasakli_kelimeler": ["kavitasyon", "yüksek frekans", "ses dalgası banyosu", "mikro kabarcık", "hassas alet"], "zorluk": "zor"},
    {"kelime": "hepa filtre ile süpürmek", "aciklama": "0.3 mikron boyutundaki toz ve alerjenleri yüzde 99.97 oranında yakalayan filtreyle çekmek", "yasakli_kelimeler": ["0.3 mikron", "yüzde 99.97", "alerjen tutucu", "hava filtresi", "medikal süpürge"], "zorluk": "zor"},
    {"kelime": "kriyojenik kuru buzla püskürtmek", "aciklama": "eksi 78 derecedeki katı karbondioksit peletlerini basınçlı havayla endüstriyel kalıba çarptırmak", "yasakli_kelimeler": ["kuru buz püskürtme", "eksi 78 derece", "termal şok temizlik", "aşındırmasız", "co2 pelet"], "zorluk": "zor"},
    {"kelime": "buharlı temizlik makinesi", "aciklama": "150 derece kuru buhar püskürterek kimyasal kullanmadan yağları ve akarları eritip yok etmek", "yasakli_kelimeler": ["150 derece", "kuru buhar", "toz akarı", "kimyasalsız temizlik", "buhar basıncı"], "zorluk": "zor"},
    {"kelime": "biyolojik arıtma yapmak", "aciklama": "endüstriyel atık suları aktif çamur havuzundaki aerobik bakterilere yedirip temizlemek", "yasakli_kelimeler": ["aktif çamur", "aerobik bakteri", "atık su arıtma", "biyolojik havuz", "organik yük"], "zorluk": "zor"},
    {"kelime": "temiz oda protokolü uygulamak", "aciklama": "çip üretim tesisinde havadaki partikül sayısını sıfırlamak için hava duşundan geçmek", "yasakli_kelimeler": ["cleanroom", "hava duşu", "partikül kontrolü", "tulum", "iso class"], "zorluk": "zor"},
    {"kelime": "kloramin gazı zehirlenmesinden kaçınmak", "aciklama": "çamaşır suyu ile tuz ruhunu asla karıştırmayarak ölümcül zehirli gaz çıkışını önlemek", "yasakli_kelimeler": ["tuz ruhu", "ölümcül karışım", "zehirli gaz", "klor gazı", "asla karıştırma"], "zorluk": "zor"},
    {"kelime": "asbest dekontaminasyonu", "aciklama": "kentsel dönüşümde kanserojen lifli yalıtım malzemesini negatif basınçlı çadırda vakumlamak", "yasakli_kelimeler": ["kanserojen lif", "negatif basınç", "özel tulum", "yalıtım sökümü", "zararlı atık"], "zorluk": "zor"},
    {"kelime": "yağ tutucu havuzunu vidanjörle çekmek", "aciklama": "restoran giderindeki donmuş atık yağ katmanını periyodik olarak tankerle tahliye etmek", "yasakli_kelimeler": ["yağ kapanı", "vidanjör", "restoran atık yağı", "donmuş tabaka", "tahliye pompası"], "zorluk": "zor"},
    {"kelime": "biyofilm tabakasını kazımak", "aciklama": "su boruları ve diş yüzeyinde bakterilerin kurduğu dirençli polisakkarit kalkanı enzimatik sökmek", "yasakli_kelimeler": ["bakteri matrisi", "polisakkarit tabaka", "enzimatik temizlik", "dirençli katman", "borularda kalkan"], "zorluk": "zor"},
    {"kelime": "hidrofobik seramik kaplamak", "aciklama": "araba kaportasına sıvı cam sürerek su ve kir tutmayan nano koruma kalkanı örmek", "yasakli_kelimeler": ["seramik kaplama", "sıvı cam", "nano koruma", "su itici katman", "araba boyası"], "zorluk": "zor"},
    {"kelime": "endüstriyel zemin cilalama", "aciklama": "avm ve fabrika beton zeminini dev cila makineleriyle elmas pedlerle kristalize parlatmak", "yasakli_kelimeler": ["kristalize cila", "elmas ped", "dev cila makinesi", "mermer parlatma", "polimer cila"], "zorluk": "zor"}
]

if __name__ == "__main__":
    add_and_save_verbs("telekomunikasyon", telekomunikasyon_verbs)
    add_and_save_verbs("temizlik", temizlik_verbs)
