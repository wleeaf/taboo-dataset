# -*- coding: utf-8 -*-
from card_utils import add_and_save_verbs

saatcilik_verbs = [
    # Kolay (12)
    {"kelime": "kurmak", "aciklama": "mekanik saatin tepe kolunu çevirip zembereği sıkıştırmak", "yasakli_kelimeler": ["tepe", "zemberek", "mekanik", "çevirmek", "çalıştırmak"], "zorluk": "kolay"},
    {"kelime": "ayarlamak", "aciklama": "saatin akrep ve yelkovanını doğru zamana getirmek", "yasakli_kelimeler": ["akrep", "yelkovan", "zaman", "doğru saat", "ayar"], "zorluk": "kolay"},
    {"kelime": "tamir etmek", "aciklama": "durmuş veya bozulan saatin içini açıp onarmak", "yasakli_kelimeler": ["onarım", "saatçi", "bozuk", "çalışmayan", "usta"], "zorluk": "kolay"},
    {"kelime": "koluna takmak", "aciklama": "deri veya metal kordonu bileğe sarıp tokayı kapatmak", "yasakli_kelimeler": ["bilek", "kordon", "kayış", "toka", "kol"], "zorluk": "kolay"},
    {"kelime": "pil değiştirmek", "aciklama": "pilli kuvars saatin arka kapağını açıp yeni düğme pil takmak", "yasakli_kelimeler": ["kuvars", "düğme pil", "arka kapak", "bitmiş", "yenilemek"], "zorluk": "kolay"},
    {"kelime": "parlatmak", "aciklama": "çelik kasa ve cam üzerindeki çizikleri macunla ovalayıp silmek", "yasakli_kelimeler": ["polisaj", "çizik", "cam", "kasa", "cila"], "zorluk": "kolay"},
    {"kelime": "temizlemek", "aciklama": "tozlanan saat dişlilerini özel benzin banyosunda arındırmak", "yasakli_kelimeler": ["toz", "benzin", "arındırma", "yıkama", "kir"], "zorluk": "kolay"},
    {"kelime": "yağlamak", "aciklama": "dönen çark millerine iğne ucuyla mikro damla yağ damlatmak", "yasakli_kelimeler": ["mikro yağ", "damla", "çark mili", "sürtünme", "yağdanlık"], "zorluk": "kolay"},
    {"kelime": "tıkırdamak", "aciklama": "maşanın çarka her vuruşunda saatin tik tak sesi çıkarması", "yasakli_kelimeler": ["tik tak", "ses", "maşa", "çark", "işleyiş"], "zorluk": "kolay"},
    {"kelime": "ileri gitmek", "aciklama": "saatin ayarının bozulup gerçek zamandan daha hızlı çalışması", "yasakli_kelimeler": ["hızlı", "zaman", "ayar bozukluğu", "kaç dakika", "hata"], "zorluk": "kolay"},
    {"kelime": "geri kalmak", "aciklama": "saatin sürtünme veya zayıf pille zamandan yavaş ilerlemesi", "yasakli_kelimeler": ["yavaş", "zaman", "geç kalma", "duraksama", "pil zayıf"], "zorluk": "kolay"},
    {"kelime": "büyüteçle bakmak", "aciklama": "saatçi lupuyla gözün önüne büyüteç takıp minik vidaları görmek", "yasakli_kelimeler": ["lup", "gözlük", "büyüteç", "vida", "yakından"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "balans çarkı ayarlamak", "aciklama": "saatin kalbi olan balans yayının salınım frekansını regüle etmek", "yasakli_kelimeler": ["balans yayı", "salınım", "frekans", "regülatör", "kalp"], "zorluk": "orta"},
    {"kelime": "zemberek sarmak", "aciklama": "ana tambur içindeki çelik yayın gerilerek enerji depolamasını sağlamak", "yasakli_kelimeler": ["tambur", "çelik yay", "enerji deposu", "kurma kolu", "sıkışma"], "zorluk": "orta"},
    {"kelime": "maşa değiştirmek", "aciklama": "kaçış çarkının dişlerini tutan yakut paletli manivelayı yenilemek", "yasakli_kelimeler": ["kaçış çarkı", "yakut palet", "escapement", "manivela", "tıkırtı"], "zorluk": "orta"},
    {"kelime": "kronometreyi sıfırlamak", "aciklama": "üstteki basma butonuyla saniye ibresini tam on ikiye fırlatmak", "yasakli_kelimeler": ["kronograf", "buton", "sıfırlama", "12 konumu", "saniye kolu"], "zorluk": "orta"},
    {"kelime": "kordon baklası sökmek", "aciklama": "bileğe bol gelen metal bileziğin pimini çıkarıp kısaltmak", "yasakli_kelimeler": ["bakla", "pim", "bilezik", "kısaltma", "çekiç"], "zorluk": "orta"},
    {"kelime": "su geçirmezlik testi", "aciklama": "basınçlı hava veya su tankında kasanın kaç bar basınca dayandığını ölçmek", "yasakli_kelimeler": ["bar", "atm", "basınç odası", "su sızdırma", "conta"], "zorluk": "orta"},
    {"kelime": "cımbızla tutmak", "aciklama": "antimanyetik ince uçlu saatçi cımbızıyla mikro vidaları taşımak", "yasakli_kelimeler": ["antimanyetik", "ince uç", "cımbız", "mikro vida", "tutuş"], "zorluk": "orta"},
    {"kelime": "conta değiştirmek", "aciklama": "arka kapak ve tepe etrafındaki yıpranmış kauçuk o-ringi yenilemek", "yasakli_kelimeler": ["o-ring", "kauçuk", "su yalıtımı", "arka kapak", "sızdırmazlık"], "zorluk": "orta"},
    {"kelime": "yakut yatak yerleştirmek", "aciklama": "çark millerinin sürtünmesini sıfırlamak için sentetik yakut taş çakmak", "yasakli_kelimeler": ["jewel", "sentetik yakut", "sürtünmesiz yatak", "çark mili", "taş sayısı"], "zorluk": "orta"},
    {"kelime": "timegrapher ile dinlemek", "aciklama": "mikrofonlu test cihazıyla saatin günlük kaç saniye saptığını ekrandan okumak", "yasakli_kelimeler": ["vuruş hatası", "günlük sapma", "genlik", "cihaz", "ölçüm"], "zorluk": "orta"},
    {"kelime": "otomatik rotor dönmek", "aciklama": "bilek hareket ettikçe yarım ay şeklindeki ağır metal rotorun zembereği kurması", "yasakli_kelimeler": ["rotor", "yarım ay", "bilek hareketi", "otomatik mekanizma", "ağırlık"], "zorluk": "orta"},
    {"kelime": "kasa açmak", "aciklama": "vidalı arka kapağı jaxa açacağı ile tırnaklarına oturtup çevirmek", "yasakli_kelimeler": ["jaxa anahtarı", "vidalı kapak", "arka kapak", "tırnak", "açıcı"], "zorluk": "orta"},
    {"kelime": "kadran basmak", "aciklama": "saat yüzeyine tampon baskı makinesiyle rakamları ve yazıları hakketmek", "yasakli_kelimeler": ["tampon baskı", "saat yüzü", "rakamlar", "indeks", "mine"], "zorluk": "orta"},
    {"kelime": "fosfor sürmek", "aciklama": "karanlıkta parlaması için ibrelerin üzerine superluminova boyası uygulamak", "yasakli_kelimeler": ["superluminova", "karanlıkta parlama", "ibre", "gece görünürlüğü", "lüminesans"], "zorluk": "orta"},
    {"kelime": "antimanyetik kafeslemek", "aciklama": "mekanizmayı manyetik alanlardan korumak için yumuşak demir kalkan içine almak", "yasakli_kelimeler": ["yumuşak demir", "manyetik kalkan", "gauss", "koruma kafesi", "sapma önleme"], "zorluk": "orta"},
    {"kelime": "safir cam takmak", "aciklama": "elmas hariç hiçbir şeyin çizemediği 9 mohs sertliğindeki kristal camı preslemek", "yasakli_kelimeler": ["çizilmez", "safir kristal", "mohs 9", "pres", "yansıma önleyici"], "zorluk": "orta"},
    {"kelime": "tarih diski atlamak", "aciklama": "gece tam 12'de takvim çarkının dönüp penceredeki günü bir ileri atması", "yasakli_kelimeler": ["takvim", "tarih penceresi", "gece yarısı", "gün değişimi", "çark"], "zorluk": "orta"},
    {"kelime": "bezeli döndürmek", "aciklama": "dalgıç saatinin kadran dışındaki tek yönlü döner halkasını dakikaya hizalamak", "yasakli_kelimeler": ["döner halka", "dalgıç bezele", "tek yönlü", "tıklama", "tüp süresi"], "zorluk": "orta"},
    {"kelime": "güç rezervini ölçmek", "aciklama": "tam kurulan mekanik saatin kaç saat boyunca durmadan çalışacağını saymak", "yasakli_kelimeler": ["power reserve", "40 saat", "çalışma süresi", "zemberek boşalması", "gösterge"], "zorluk": "orta"},
    {"kelime": "demanyetize etmek", "aciklama": "mıknatıslanan saati bobinli demanyetizör cihazından geçirip manyetizmasını silmek", "yasakli_kelimeler": ["mıknatıslanma", "demanyetizör", "bobin", "hızlı koşma", "silme"], "zorluk": "orta"},
    {"kelime": "akrep yelkovan basmak", "aciklama": "ibreleri milin üstüne el aletiyle birbirine sürtmeyecek paralellikte oturtmak", "yasakli_kelimeler": ["ibre takma", "paralellik", "mil", "el aleti", "oturtma"], "zorluk": "orta"},
    {"kelime": "iskelet mekanizma oymak", "aciklama": "ana plakayı ve köprüleri oyup saatin içindeki çarkların çalışmasını görünür kılmak", "yasakli_kelimeler": ["skeleton", "oyma", "şeffaf kadran", "köprü", "görünür çarklar"], "zorluk": "orta"},
    {"kelime": "mine fırınlamak", "aciklama": "kadran üzerine toz cam sürüp 800 derecelik fırında emaye pişirmek", "yasakli_kelimeler": ["emaye", "grand feu", "800 derece", "fırın", "cam tozu"], "zorluk": "orta"},
    {"kelime": "kurma kolu çekmek", "aciklama": "tepeyi birinci veya ikinci kademeye çekip tarihi ya da saati ayarlamak", "yasakli_kelimeler": ["kademe", "tepe çekme", "ayar modu", "tık sesi", "kol"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "tourbillon kafesi döndürmek", "aciklama": "yerçekiminin balans yayına yaptığı hatayı sıfırlamak için tüm maşayı dakikada 1 tur çevirmek", "yasakli_kelimeler": ["breguet", "yerçekimi dengeleme", "dönen kafes", "yüksek komplikasyon", "dakikada bir tur"], "zorluk": "zor"},
    {"kelime": "perpetual calendar kurmak", "aciklama": "artık yılları, 30-31 çeken ayları ve şubatın 28-29 çekmesini 2100 yılına kadar hatasız hesaplamak", "yasakli_kelimeler": ["ebedi takvim", "artık yıl", "şubat 29", "2100 yılı", "kam sistemi"], "zorluk": "zor"},
    {"kelime": "minute repeater çaldırmak", "aciklama": "saatin yanındaki sürgüyü çekince minik çekiçlerin gong tellerine vurup saati dakika dakika çalması", "yasakli_kelimeler": ["dakika tekrarlayıcı", "gong telleri", "çekiçler", "zil sesi", "sesli komplikasyon"], "zorluk": "zor"},
    {"kelime": "côtes de genève süslemek", "aciklama": "mekanizma köprüleri üzerine ahşap fırça ile dalgalı cenevre şeritleri deseni basmak", "yasakli_kelimeler": ["cenevre şeritleri", "köprü deseni", "dalgalı hat", "finisaj", "haut horlogerie"], "zorluk": "zor"},
    {"kelime": "anglage pahı kırmak", "aciklama": "çelik köprülerin keskin kenarlarını elmas eğeyle 45 derece açıyla ayna gibi parlatmak", "yasakli_kelimeler": ["pah kırma", "ayna polisaj", "45 derece kenar", "el işçiliği", "eğe"], "zorluk": "zor"},
    {"kelime": "perlage dairesi basmak", "aciklama": "ana plaka zeminine dönen aşındırıcı çubukla birbirinin üstüne binen inci daireleri basmak", "yasakli_kelimeler": ["inci deseni", "dairesel desen", "ana plaka", "finisaj", "süsleme"], "zorluk": "zor"},
    {"kelime": "silisyum zemberek takmak", "aciklama": "manyetizmadan ve ısı değişiminden hiç etkilenmeyen silikon kılcal yay takmak", "yasakli_kelimeler": ["silisyum yay", "silikon spiral", "antimanyetik kılcal", "isokronizm", "yüksek teknoloji"], "zorluk": "zor"},
    {"kelime": "guilloché motifi oymak", "aciklama": "rose engine tezgahında elle çevrilerek kadrana geometrik dalga desenleri kazımak", "yasakli_kelimeler": ["rose engine", "geometrik oyma", "kadrana desen", "breguet deseni", "el tornası"], "zorluk": "zor"},
    {"kelime": "sütun çarkı entegre etmek", "aciklama": "lüks kronograflarda buton basışını yumuşacık ve kusursuz kılan kule biçimli çark", "yasakli_kelimeler": ["column wheel", "sütun çarkı", "kronograf mekanizması", "yumuşak buton", "kule çark"], "zorluk": "zor"},
    {"kelime": "koaksiyel eşapman kurmak", "aciklama": "george daniels'ın icat ettiği, sürtünmeyi ve yağ ihtiyacını neredeyse sıfırlayan çift çarklı maşa", "yasakli_kelimeler": ["co-axial", "george daniels", "omega", "yağsız maşa", "radyal darbe"], "zorluk": "zor"},
    {"kelime": "denklem zamanı göstermek", "aciklama": "gerçek güneş saati ile kolumuzdaki ortalama zaman arasındaki 15 dakikalık farkı hesaplamak", "yasakli_kelimeler": ["equation of time", "güneş saati farkı", "analemma", "astronomik komplikasyon", "gerçek zaman"], "zorluk": "zor"},
    {"kelime": "ay fazı diski çevirmek", "aciklama": "59 dişli çarkla hilalden dolunaya 29.5 günlük ay döngüsünü kadranda altın ayla gezdirmek", "yasakli_kelimeler": ["moonphase", "29.5 gün", "dolunay", "59 diş", "gece göğü"], "zorluk": "zor"},
    {"kelime": "yay salınım genliği ölçmek", "aciklama": "balans çarkının her iki yana dönerken yaptığı açısal genliği 280-310 derece arasına ayarlamak", "yasakli_kelimeler": ["amplitude", "açısal genlik", "280 derece", "balans dönüşü", "saat sağlığı"], "zorluk": "zor"},
    {"kelime": "cenevre mührü almak", "aciklama": "mekanizmanın 12 zorlu estetik ve teknik kalite kuralını geçip resmi cenevre arması kazanması", "yasakli_kelimeler": ["geneva seal", "poinçon de genève", "kanton mührü", "en yüksek kalite", "12 kriter"], "zorluk": "zor"}
]

saglikliyasam_verbs = [
    # Kolay (12)
    {"kelime": "spor yapmak", "aciklama": "vücudu zinde ve sağlıklı tutmak için düzenli egzersiz yapmak", "yasakli_kelimeler": ["egzersiz", "zindelik", "hareket", "fitness", "antrenman"], "zorluk": "kolay"},
    {"kelime": "koşmak", "aciklama": "parkta veya koşu bandında tempolu adımlarla ter atmak", "yasakli_kelimeler": ["koşu bandı", "park", "tempo", "adım", "ter"], "zorluk": "kolay"},
    {"kelime": "yürümek", "aciklama": "her gün 10 bin adım hedefine ulaşmak için tempolu yürüyüş yapmak", "yasakli_kelimeler": ["10 bin adım", "yürüyüş", "adım", "tempolu", "hedef"], "zorluk": "kolay"},
    {"kelime": "su içmek", "aciklama": "vücudun nem dengesi için günde en az iki litre su tüketmek", "yasakli_kelimeler": ["iki litre", "bardak", "tüketim", "susuzluk", "hidrasyon"], "zorluk": "kolay"},
    {"kelime": "uyumak", "aciklama": "hücre yenilenmesi için her gece düzenli 8 saat uyku çekmek", "yasakli_kelimeler": ["8 saat", "gece", "yatak", "dinlenme", "kaliteli uyku"], "zorluk": "kolay"},
    {"kelime": "beslenmek", "aciklama": "taze sebze, meyve ve protein ağırlıklı temiz gıdalar tüketmek", "yasakli_kelimeler": ["sebze", "meyve", "protein", "temiz gıda", "öğün"], "zorluk": "kolay"},
    {"kelime": "kilo vermek", "aciklama": "kalori açığı oluşturarak fazla yağları yakıp hafiflemek", "yasakli_kelimeler": ["zayıflamak", "yağ yakımı", "kalori açığı", "tartı", "hafifleme"], "zorluk": "kolay"},
    {"kelime": "esnemek", "aciklama": "spordan önce ve sonra kasları gerip esneklik kazandırmak", "yasakli_kelimeler": ["stretching", "germe", "kas", "esneklik", "açma"], "zorluk": "kolay"},
    {"kelime": "nefes almak", "aciklama": "stres anında burnundan derin diyafram nefesi çekmek", "yasakli_kelimeler": ["derin nefes", "burun", "diyafram", "oksijen", "akciğer"], "zorluk": "kolay"},
    {"kelime": "dinlenmek", "aciklama": "ağır iş veya antrenman sonrası uzanıp vücudu toparlamak", "yasakli_kelimeler": ["uzanmak", "mola", "toparlanma", "yorgunluk", "rahatlama"], "zorluk": "kolay"},
    {"kelime": "güneşlenmek", "aciklama": "doğal d vitamini sentezlemek için sabah güneşinde 15 dakika durmak", "yasakli_kelimeler": ["d vitamini", "güneş ışığı", "sabah", "sentez", "kemik"], "zorluk": "kolay"},
    {"kelime": "tartılmak", "aciklama": "sabah aç karnına dijital basküle çıkıp vücut ağırlığını kontrol etmek", "yasakli_kelimeler": ["baskül", "terazi", "aç karnına", "kilo kontrolü", "ağırlık"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "diyet yapmak", "aciklama": "şeker ve hamur işini kesip diyetisyen listesine harfiyen uymak", "yasakli_kelimeler": ["diyetisyen", "şeker", "hamur işi", "liste", "kalori"], "zorluk": "orta"},
    {"kelime": "ağırlık kaldırmak", "aciklama": "salonda dambıl ve halterle kas kütlesini artırıcı kuvvet çalışmak", "yasakli_kelimeler": ["halter", "dambıl", "kas kütlesi", "kuvvet", "set"], "zorluk": "orta"},
    {"kelime": "kardiyo yapmak", "aciklama": "kürek çekme, bisiklet veya ip atlamayla kalp atım hızını yükseltmek", "yasakli_kelimeler": ["kalp atımı", "bisiklet", "ip atlama", "kürek", "nabız"], "zorluk": "orta"},
    {"kelime": "şekeri kesmek", "aciklama": "işlenmiş beyaz şekeri ve gazlı içecekleri beslenmeden tamamen çıkarmak", "yasakli_kelimeler": ["beyaz şeker", "tatlı", "gazlı içecek", "işlenmiş", "çıkarma"], "zorluk": "orta"},
    {"kelime": "aralıklı oruç tutmak", "aciklama": "günün 16 saati aç kalıp sadece 8 saatlik pencerede yemek yemek", "yasakli_kelimeler": ["16/8", "açlık penceresi", "intermittent fasting", "otofaji", "oruç"], "zorluk": "orta"},
    {"kelime": "yoga yapmak", "aciklama": "mat üstünde asana duruşları ve nefesle zihin-beden dengesi kurmak", "yasakli_kelimeler": ["asana", "mat", "esneklik", "namaste", "meditasyon"], "zorluk": "orta"},
    {"kelime": "meditasyon yapmak", "aciklama": "sessizce oturup zihni boşaltarak içsel dinginlik ve odaklanma yakalamak", "yasakli_kelimeler": ["zihin boşaltma", "dinginlik", "odaklanma", "sessizlik", "nefes"], "zorluk": "orta"},
    {"kelime": "pilatese gitmek", "aciklama": "reformer aletinde yay direnciyle karın ve omurga kaslarını güçlendirmek", "yasakli_kelimeler": ["reformer", "core bölgesi", "omurga", "yay direnci", "karın"], "zorluk": "orta"},
    {"kelime": "detoks yapmak", "aciklama": "yeşil sebze suları ve antioksidan içeceklerle vücudu toksinlerden arındırmak", "yasakli_kelimeler": ["toksin arınma", "yeşil meyve suyu", "smoothie", "antioksidan", "arındırma"], "zorluk": "orta"},
    {"kelime": "probiyotik tüketmek", "aciklama": "bağırsak florasını güçlendirmek için kefir ve ev yapımı turşu yemek", "yasakli_kelimeler": ["kefir", "bağırsak florası", "mikrobiyota", "yararlı bakteri", "ev turşusu"], "zorluk": "orta"},
    {"kelime": "omega 3 almak", "aciklama": "beyin ve damar sağlığı için haftada iki gün balık veya balık yağı kapsülü tüketmek", "yasakli_kelimeler": ["balık yağı", "epa dha", "kapsül", "somon", "damar sağlığı"], "zorluk": "orta"},
    {"kelime": "kolajen kullanmak", "aciklama": "cilt elastikiyeti ve eklem kıkırdağı için hidrolize peptit tozu içmek", "yasakli_kelimeler": ["peptit", "cilt elastikiyeti", "eklem kıkırdağı", "tip 1 tip 3", "toz"], "zorluk": "orta"},
    {"kelime": "nabız ölçmek", "aciklama": "akıllı saat veya göğüs bandıyla dakikadaki kalp vuruş sayısını takip etmek", "yasakli_kelimeler": ["akıllı saat", "bpm", "kalp atışı", "göğüs bandı", "takip"], "zorluk": "orta"},
    {"kelime": "soğuk duş almak", "aciklama": "uyanır uyanmaz buz gibi suyun altına girip kan dolaşımını ve bağışıklığı tetiklemek", "yasakli_kelimeler": ["wim hof", "buz gibi su", "dolaşım", "şok", "bağışıklık"], "zorluk": "orta"},
    {"kelime": "saunaya girmek", "aciklama": "yüksek sıcaklıktaki ahşap odada yoğun terleyerek gözenekleri açmak", "yasakli_kelimeler": ["ahşap oda", "buhar odası", "terleme", "gözenek", "sıcaklık"], "zorluk": "orta"},
    {"kelime": "foam roller ile masaj", "aciklama": "spordan sonra sert sünger silindiri bacak kaslarının altında yuvarlayıp fasyayı açmak", "yasakli_kelimeler": ["sünger silindir", "fasya", "kas düğümü", "tetik nokta", "masaj"], "zorluk": "orta"},
    {"kelime": "kalori saymak", "aciklama": "mobil uygulamaya gün boyu yenen tüm yiyeceklerin gramını ve enerjisini girmek", "yasakli_kelimeler": ["myfitnesspal", "günlük kalori", "makro hesabı", "enerji", "uygulama"], "zorluk": "orta"},
    {"kelime": "şişkinlik hissetmek", "aciklama": "laktoz veya gluten intoleransı sebebiyle yemekten sonra midede gaz toplanması", "yasakli_kelimeler": ["gaz", "ödem", "intolerans", "gluten", "laktoz"], "zorluk": "orta"},
    {"kelime": "postür düzeltmek", "aciklama": "masa başında kambur durmamak için omuzları geriye alıp dik oturmak", "yasakli_kelimeler": ["duruş bozukluğu", "kamburluk", "dik oturma", "omurga sağlığı", "omuzlar geride"], "zorluk": "orta"},
    {"kelime": "kan tahlili yaptırmak", "aciklama": "yılda bir check-up için kolesterol, şeker ve vitamin seviyelerine baktırmak", "yasakli_kelimeler": ["check up", "kolesterol", "kan şekeri", "vitamin", "laboratuvar"], "zorluk": "orta"},
    {"kelime": "sigarayı bırakmak", "aciklama": "tütün ürünlerini tamamen terk ederek akciğer kapasitesini geri kazanmak", "yasakli_kelimeler": ["tütün", "bırakma", "akciğer temizliği", "nikotin", "sağlık"], "zorluk": "orta"},
    {"kelime": "yeşil çay demlemek", "aciklama": "antioksidan zengini yaprakları sıcak suda bekletip metabolizmayı hızlandırmak", "yasakli_kelimeler": ["metabolizma", "antioksidan", "kateşin", "bitki çayı", "demlik"], "zorluk": "orta"},
    {"kelime": "kemik suyuna çorba içmek", "aciklama": "ilikli kemikleri 12 saat kısık ateşte kaynatıp kolajen zengini şifa suyu yapmak", "yasakli_kelimeler": ["ilikli kemik", "şifa", "kaynatma", "kolajen", "bağışıklık"], "zorluk": "orta"},
    {"kelime": "makro besinleri dengelemek", "aciklama": "öğündeki karbonhidrat, protein ve sağlıklı yağ oranlarını hedefe göre ayarlamak", "yasakli_kelimeler": ["karbonhidrat", "protein", "yağ", "oran", "beslenme dengesi"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "otofajiyi tetiklemek", "aciklama": "uzun süreli açlıkla hücrelerin kendi içindeki hasarlı proteinleri yiyip yenilenmesi", "yasakli_kelimeler": ["hücresel temizlik", "açlık", "yoshinori ohsumi", "hasarlı organel", "yenilenme"], "zorluk": "zor"},
    {"kelime": "ketojenez durumuna girmek", "aciklama": "karbonhidratsız beslenmeyle karaciğerin yağları parçalayıp keton cisimciği üretmesi", "yasakli_kelimeler": ["ketozis", "keton", "karaciğer", "yağ yakma", "karbonhidratsız"], "zorluk": "zor"},
    {"kelime": "vo2 max değerini yükseltmek", "aciklama": "maksimal egzersiz anında kasların kandan kullanabildiği en yüksek oksijen hacmi", "yasakli_kelimeler": ["maksimal oksijen", "kardiyovasküler kapasite", "dayanıklılık", "ml/kg/dk", "aerobik güç"], "zorluk": "zor"},
    {"kelime": "kalp hızı değişkenliği ölçmek", "aciklama": "ardışık kalp atımları arasındaki milisaniye farklarından otonom sinir toparlanmasını izlemek", "yasakli_kelimeler": ["hrv", "milisaniye", "parasempatik tonus", "toparlanma", "stres seviyesi"], "zorluk": "zor"},
    {"kelime": "epigenetik saati gençleştirmek", "aciklama": "yaşam tarzı, egzersiz ve uykuyla dna metilasyon yaşını geriye çekmek", "yasakli_kelimeler": ["dna metilasyonu", "horvath saati", "biyolojik yaş", "gen ifadesi", "uzun ömür"], "zorluk": "zor"},
    {"kelime": "glisemik indeksi kontrol etmek", "aciklama": "besinlerin kan şekerini yükseltme hızına göre düşük glisemik karbonhidrat seçmek", "yasakli_kelimeler": ["kan şekeri sıçraması", "insülin direnci", "yavaş sindirim", "glisemik yük", "şeker eğrisi"], "zorluk": "zor"},
    {"kelime": "mitokondriyal biyogenez", "aciklama": "yüksek yoğunluklu aralıklı antrenmanla hücrelerdeki enerji santrali sayısını çoğaltmak", "yasakli_kelimeler": ["mitokondri sayısı", "hiit antrenmanı", "enerji santrali", "pgc-1alpha", "hücresel solunum"], "zorluk": "zor"},
    {"kelime": "sirkadiyen ritmi senkronize etmek", "aciklama": "sabah ilk ışık ve melatonin salınımıyla vücudun 24 saatlik biyolojik saatini hizalamak", "yasakli_kelimeler": ["melatonin", "biyolojik saat", "sabah güneşi", "24 saat", "uyku döngüsü"], "zorluk": "zor"},
    {"kelime": "laktat eşiğini ötelemek", "aciklama": "kanda laktik asit birikiminin patladığı egzersiz yoğunluğunu antrenmanla yukarı taşımak", "yasakli_kelimeler": ["laktik asit", "yanma hissi", "anaerobik eşik", "yorgunluk sınırı", "tempo"], "zorluk": "zor"},
    {"kelime": "telomer kısalmasını yavaşlatmak", "aciklama": "kromozom uçlarındaki koruyucu telomer başlıklarını sağlıklı yaşamla korumak", "yasakli_kelimeler": ["kromozom ucu", "telomeraz", "hücresel yaşlanma", "ömür", "genetik koruma"], "zorluk": "zor"},
    {"kelime": "soğuk şok proteinleri salgılamak", "aciklama": "buz banyosuna girerek rbm3 gibi nöron koruyucu şok proteinlerini aktifleştirmek", "yasakli_kelimeler": ["buz banyosu", "rbm3", "soğuk maruziyeti", "hücresel koruma", "kahverengi yağ"], "zorluk": "zor"},
    {"kelime": "ısı şok proteinleri üretmek", "aciklama": "80 derece saunada bekleyerek hsp70 ile yanlış katlanmış proteinleri onarmak", "yasakli_kelimeler": ["hsp", "sauna etkisi", "protein katlanması", "hücresel stres", "80 derece"], "zorluk": "zor"},
    {"kelime": "bazal metabolizma hızı hesabı", "aciklama": "vücudun tam istirahat halindeyken sadece hayatta kalmak için yaktığı minimum kalori", "yasakli_kelimeler": ["bmh", "istirahat kalorisi", "harris benedict", "yağsız kütle", "minimum enerji"], "zorluk": "zor"},
    {"kelime": "hipertrofi uyarımı sağlamak", "aciklama": "mekanik gerilim ve metabolik stresle kas liflerinde protein sentezini maksimize etmek", "yasakli_kelimeler": ["mekanik gerilim", "kas lifi kalınlaşması", "protein sentezi", "mTOR", "mikro yırtık"], "zorluk": "zor"}
]

if __name__ == "__main__":
    add_and_save_verbs("saatcilik", saatcilik_verbs)
    add_and_save_verbs("saglikliyasam", saglikliyasam_verbs)
