import os, sys, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gen_scripts.card_utils import add_and_save_verbs

# 3. enstrumanlar
enstrumanlar_verbs = [
    # Kolay (12)
    {"kelime": "gitar çalmak", "yasakli_kelimeler": ["tel", "pena", "akor", "müzik", "şarkı"], "zorluk": "kolay", "aciklama": "Telli müzik aletinden ses çıkartarak melodi üretmek."},
    {"kelime": "piyano çalmak", "yasakli_kelimeler": ["tuş", "siyah", "beyaz", "kuyruklu", "nota"], "zorluk": "kolay", "aciklama": "Tuşlu çalgının tuşlarına basarak müzik icra etmek."},
    {"kelime": "keman çalmak", "yasakli_kelimeler": ["yay", "tel", "çene", "omuz", "arşe"], "zorluk": "kolay", "aciklama": "Yayla tellere sürtülerek çalınan yaylı çalgıyı seslendirmek."},
    {"kelime": "davul çalmak", "yasakli_kelimeler": ["baget", "ritim", "vurmak", "tokmak", "bateri"], "zorluk": "kolay", "aciklama": "Vurmalı çalgının derisine baget veya tokmakla vurarak ritim tutmak."},
    {"kelime": "flüt çalmak", "yasakli_kelimeler": ["üflemek", "delik", "nefes", "müzik", "yan"], "zorluk": "kolay", "aciklama": "Üflemeli çalgının deliklerini parmaklarla kapatıp açarak ses çıkarmak."},
    {"kelime": "bağlama çalmak", "yasakli_kelimeler": ["saz", "mızrap", "türkü", "tel", "perde"], "zorluk": "kolay", "aciklama": "Geleneksel Türk halk müziği telli çalgısını icra etmek."},
    {"kelime": "akort etmek", "yasakli_kelimeler": ["düzenlemek", "tel", "ayar", "ses", "kulak"], "zorluk": "kolay", "aciklama": "Çalgının tellerini doğru ses frekansına getirmek."},
    {"kelime": "şarkı söylemek", "yasakli_kelimeler": ["ses", "vokal", "melodi", "söz", "beste"], "zorluk": "kolay", "aciklama": "Ses tellerini kullanarak melodik eser seslendirmek."},
    {"kelime": "nota okumak", "yasakli_kelimeler": ["porte", "sol anahtarı", "kağıt", "müzik", "işaret"], "zorluk": "kolay", "aciklama": "Porte üzerindeki müzik işaretlerini deşifre etmek."},
    {"kelime": "ritim tutmak", "yasakli_kelimeler": ["tempo", "el çırpmak", "vuruş", "metronom", "hız"], "zorluk": "kolay", "aciklama": "Müziğin vuruş temposuna düzenli olarak eşlik etmek."},
    {"kelime": "zil çalmak", "yasakli_kelimeler": ["metal", "çarpışmak", "parmak", "ses", "bateri"], "zorluk": "kolay", "aciklama": "Metal perküsyon aletlerini birbirine vurarak ses çıkarmak."},
    {"kelime": "mızıka çalmak", "yasakli_kelimeler": ["üflemek", "içine çekmek", "küçük", "ağız", "cep"], "zorluk": "kolay", "aciklama": "Ağızla hava üfleyip çekerek çalınan küçük çalgıyı seslendirmek."},

    # Orta (24)
    {"kelime": "arşe çekmek", "yasakli_kelimeler": ["yay", "keman", "tel", "sürtmek", "viyola"], "zorluk": "orta", "aciklama": "Yaylı çalgı yayını tellerin üzerinden kaydırmak."},
    {"kelime": "tel değiştirmek", "yasakli_kelimeler": ["kopmak", "gitar", "keman", "yenilemek", "burgu"], "zorluk": "orta", "aciklama": "Eski veya kopan enstrüman telinin yerine yenisini takmak."},
    {"kelime": "pena kullanmak", "yasakli_kelimeler": ["mızrap", "plastik", "gitar", "vurmak", "tel"], "zorluk": "orta", "aciklama": "Telleri titreştirmek için küçük plastik alet kullanmak."},
    {"kelime": "nefes kontrolü yapmak", "yasakli_kelimeler": ["diyafram", "üflemek", "flüt", "trompet", "ciğer"], "zorluk": "orta", "aciklama": "Üflemeli çalgılarda havayı dengeli ve uzun süreli vermek."},
    {"kelime": "metronom eşliğinde çalmak", "yasakli_kelimeler": ["tempo", "tık tık", "hız", "ölçü", "cihaz"], "zorluk": "orta", "aciklama": "Sabit vuruş veren cihazın temposuna uyarak prova yapmak."},
    {"kelime": "pedala basmak", "yasakli_kelimeler": ["piyano", "ayak", "uzatmak", "yankı", "sustain"], "zorluk": "orta", "aciklama": "Piyanoda sesin tınlama süresini uzatmak için ayak mekanizmasını kullanmak."},
    {"kelime": "akor basmak", "yasakli_kelimeler": ["klavye", "parmak", "armoni", "gitar", "birlikte"], "zorluk": "orta", "aciklama": "Aynı anda birden fazla sese basarak armoni oluşturmak."},
    {"kelime": "solo atmak", "yasakli_kelimeler": ["tek başına", "melodi", "gitar", "doğaçlama", "sahne"], "zorluk": "orta", "aciklama": "Müzik parçasının ortasında tek başına virtüözce çalmak."},
    {"kelime": "çello çalmak", "yasakli_kelimeler": ["viyolonsel", "bacak arası", "büyük", "yay", "bas"], "zorluk": "orta", "aciklama": "Bacaklar arasında tutulan büyük yaylı çalgıyı çalmak."},
    {"kelime": "klarnet çalmak", "yasakli_kelimeler": ["kamış", "üflemeli", "bek", "siyah", "hüsnü"], "zorluk": "orta", "aciklama": "Tek kamışlı ağızlığı olan nefesli enstrümanı icra etmek."},
    {"kelime": "trompet çalmak", "yasakli_kelimeler": ["bakır", "piston", "üflemek", "parlak", "caz"], "zorluk": "orta", "aciklama": "Pistonlu pirinç nefesli çalgıyı çalmak."},
    {"kelime": "kanun çalmak", "yasakli_kelimeler": ["mızrap", "yüksük", "mandal", "türk müziği", "sehpa"], "zorluk": "orta", "aciklama": "Yüksük ve mızraplarla telleri tınlatılan yatay Türk müziği çalgısını icra etmek."},
    {"kelime": "ney üflemek", "yasakli_kelimeler": ["kamış", "tasavvuf", "başpare", "mevlevi", "ses"], "zorluk": "orta", "aciklama": "Kargı kamışından yapılan geleneksel tasavvuf çalgısından ses çıkarmak."},
    {"kelime": "ud çalmak", "yasakli_kelimeler": ["göğüs", "mızrap", "perdesiz", "türk müziği", "tekne"], "zorluk": "orta", "aciklama": "Perdesiz, bombeli gövdeli telli çalgıyı icra etmek."},
    {"kelime": "darbuka çalmak", "yasakli_kelimeler": ["ritim", "düm", "tek", "koltuk altı", "perküsyon"], "zorluk": "orta", "aciklama": "Koltuk altında tutulan kadeh formundaki ritim aletini çalmak."},
    {"kelime": "bateri çalmak", "yasakli_kelimeler": ["davul seti", "zil", "baget", "trampet", "pedal"], "zorluk": "orta", "aciklama": "Farklı boyutlardaki davul ve zillerden oluşan vurmalı seti çalmak."},
    {"kelime": "gam çalışmak", "yasakli_kelimeler": ["dizi", "egzersiz", "parmak", "nota", "hızlanmak"], "zorluk": "orta", "aciklama": "Belirli bir tonun notalarını sırayla inip çıkarak parmak pratiği yapmak."},
    {"kelime": "doğaçlama yapmak", "yasakli_kelimeler": ["emprovizasyon", "nota olmadan", "içinden geldiği gibi", "caz", "anlık"], "zorluk": "orta", "aciklama": "Yazılı notaya bağlı kalmadan anında ezgi üretmek."},
    {"kelime": "orkestrada çalmak", "yasakli_kelimeler": ["şef", "senfoni", "birlikte", "grup", "filarmoni"], "zorluk": "orta", "aciklama": "Büyük müzik topluluğunun bir üyesi olarak uyum içinde çalmak."},
    {"kelime": "reçine sürmek", "yasakli_kelimeler": ["arşe", "keman", "yay", "toz", "tutunma"], "zorluk": "orta", "aciklama": "Keman yayının tele iyi tutunması için özel reçine taşını yaya sürmek."},
    {"kelime": "tremolo yapmak", "yasakli_kelimeler": ["titretmek", "hızlı vuruş", "tel", "mandolin", "tekrar"], "zorluk": "orta", "aciklama": "Aynı notayı çok hızlı ve kesintisiz şekilde ardışık tınlatmak."},
    {"kelime": "parmak açmak", "yasakli_kelimeler": ["esneklik", "egzersiz", "klavye", "perde", "çalışma"], "zorluk": "orta", "aciklama": "Enstrümanda geniş basışlar yapabilmek için el kaslarını esnetmek."},
    {"kelime": "mandal ayarlamak", "yasakli_kelimeler": ["kanun", "koma", "makam", "çevirmek", "tel"], "zorluk": "orta", "aciklama": "Kanun çalgısında telin boyunu küçük mandallarla değiştirip komaları ayarlamak."},
    {"kelime": "susturucu takmak", "yasakli_kelimeler": ["surdin", "ses azaltmak", "keman", "trompet", "kısık"], "zorluk": "orta", "aciklama": "Enstrümanın ses şiddetini ve tınısını kısmak için aparat takmak."},

    # Zor (14)
    {"kelime": "vibrato yapmak", "yasakli_kelimeler": ["dalgalanma", "parmak sallamak", "perde", "ton", "titreşim"], "zorluk": "zor", "aciklama": "Basılan notanın perdesini hafifçe salındırarak sese zenginlik katmak."},
    {"kelime": "legato çalmak", "yasakli_kelimeler": ["bağlı", "kesintisiz", "yumuşak", "akıcı", "nota"], "zorluk": "zor", "aciklama": "Notaları birbirine pürüzsüz ve kesintisiz bağlayarak icra etmek."},
    {"kelime": "staccato çalmak", "yasakli_kelimeler": ["kesik", "nokta", "kısa", "zıplatmak", "ayrık"], "zorluk": "zor", "aciklama": "Notaları kısa, kesik ve birbirinden net ayrılarak seslendirmek."},
    {"kelime": "pizzicato yapmak", "yasakli_kelimeler": ["parmakla çekmek", "yay bırakmak", "keman", "tel", "çimdiklemek"], "zorluk": "zor", "aciklama": "Yaylı çalgılarda yayı bırakıp teli parmakla çekerek ses çıkartmak."},
    {"kelime": "glissando yapmak", "yasakli_kelimeler": ["kaydırmak", "aralıksız", "tuş", "tel", "ses geçişi"], "zorluk": "zor", "aciklama": "Bir notadan diğerine aradaki tüm seslerden kayarak geçmek."},
    {"kelime": "arpej çalmak", "yasakli_kelimeler": ["kırık akor", "sırayla", "tel", "akor", "pena"], "zorluk": "zor", "aciklama": "Bir akorun seslerini aynı anda değil sırayla peş peşe çalmak."},
    {"kelime": "dairesel nefes almak", "yasakli_kelimeler": ["kesintisiz", "yanak", "burun", "üflemek", "didyiridu"], "zorluk": "zor", "aciklama": "Nefesli çalgıyı üflerken aynı anda burundan nefes alarak sesi hiç kesmemek."},
    {"kelime": "çift dil tekniği uygulamak", "yasakli_kelimeler": ["flüt", "trompet", "hızlı artikülasyon", "tu ku", "dil"], "zorluk": "zor", "aciklama": "Nefesli çalgılarda 't-k-t-k' heceleriyle çok hızlı nota artikülasyonu yapmak."},
    {"kelime": "harmonik ses çıkartmak", "yasakli_kelimeler": ["doğal", "yapay", "flajole", "hafif dokunmak", "tel"], "zorluk": "zor", "aciklama": "Tele tam basmadan boğum noktasına hafifçe dokunarak çan benzeri tiz ses üretmek."},
    {"kelime": "kamış yontmak", "yasakli_kelimeler": ["obua", "klarnet", "bıçak", "ayar", "ağızlık"], "zorluk": "zor", "aciklama": "Üflemeli çalgı kamışını tınısını ayarlamak için özel bıçakla inceltmek."},
    {"kelime": "portamento yapmak", "yasakli_kelimeler": ["yumuşak kayma", "ses", "vokal", "keman", "bağlantı"], "zorluk": "zor", "aciklama": "Bir perdeden diğer perdeye kesintisiz yumuşak bir ton geçişiyle kaymak."},
    {"kelime": "sul ponticello çalmak", "yasakli_kelimeler": ["köprü", "eşik", "keman", "yay", "cızırtılı"], "zorluk": "zor", "aciklama": "Yayı kemanın eşiğine çok yakın çekerek madeni ve ince bir tını elde etmek."},
    {"kelime": "col legno vurmak", "yasakli_kelimeler": ["yayın tahtası", "tel", "keman", "perküsif", "arşe"], "zorluk": "zor", "aciklama": "Yayın kılları yerine tahta kısmıyla tele vurarak perküsif ses elde etmek."},
    {"kelime": "rubato uygulamak", "yasakli_kelimeler": ["tempo çalmak", "serbest hız", "chopin", "yavaşlama", "hızlanma"], "zorluk": "zor", "aciklama": "Katı metronom ritmini esnetip ifadeye göre yavaşlayıp hızlanarak çalmak."}
]

# 4. epidemiyoloji
epidemiyoloji_verbs = [
    # Kolay (12)
    {"kelime": "aşı olmak", "yasakli_kelimeler": ["iğne", "koruma", "hastalık", "bağışıklık", "hemşire"], "zorluk": "kolay", "aciklama": "Bulaşıcı hastalıklara karşı bağışıklık kazanmak için aşı yaptırmak."},
    {"kelime": "maske takmak", "yasakli_kelimeler": ["ağız", "burun", "virüs", "korona", "korunmak"], "zorluk": "kolay", "aciklama": "Havadaki damlacıklardan korunmak için yüzü kapatmak."},
    {"kelime": "elleri yıkamak", "yasakli_kelimeler": ["sabun", "su", "hijyen", "mikrop", "temizlik"], "zorluk": "kolay", "aciklama": "Mikropları uzaklaştırmak için elleri sabunla arındırmak."},
    {"kelime": "karantinaya girmek", "yasakli_kelimeler": ["ev", "tecrit", "bulaş", "kalmak", "çıkmamak"], "zorluk": "kolay", "aciklama": "Bulaşma riskine karşı belirli süre insanlardan izole yaşamak."},
    {"kelime": "hastalık kapmak", "yasakli_kelimeler": ["bulaşmak", "virüs", "ateş", "hasta", "mikrop"], "zorluk": "kolay", "aciklama": "Bir enfeksiyon etkenini vücuduna alıp rahatsızlanmak."},
    {"kelime": "ateş ölçmek", "yasakli_kelimeler": ["derece", "termometre", "sıcaklık", "hastalık", "alın"], "zorluk": "kolay", "aciklama": "Vücut ısısının yüksekliğini tespit etmek."},
    {"kelime": "test yaptırmak", "yasakli_kelimeler": ["pcr", "sürüntü", "sonuç", "pozitif", "negatif"], "zorluk": "kolay", "aciklama": "Vücutta enfeksiyon olup olmadığını laboratuvarda baktırmak."},
    {"kelime": "mesafe korumak", "yasakli_kelimeler": ["sosyal", "uzak durmak", "kalabalık", "yaklaşmamak", "metre"], "zorluk": "kolay", "aciklama": "Bulaşma riskini azaltmak için insanlarla araya fiziksel mesafe koymak."},
    {"kelime": "ilaç kullanmak", "yasakli_kelimeler": ["hap", "şurup", "tedavi", "doktor", "iyileşmek"], "zorluk": "kolay", "aciklama": "Hastalığı tedavi etmek için hekimin verdiği ilaçları almak."},
    {"kelime": "dezenfektan sürmek", "yasakli_kelimeler": ["alkol", "jel", "el", "temizlemek", "mikrop"], "zorluk": "kolay", "aciklama": "Mikroorganizmaları öldüren solüsyonu el veya yüzeye uygulamak."},
    {"kelime": "iyileşmek", "yasakli_kelimeler": ["sağlık", "hastalık", "şifa", "toparlanmak", "düzelmek"], "zorluk": "kolay", "aciklama": "Hastalık durumundan kurtulup eski sağlıklı haline dönmek."},
    {"kelime": "semptom göstermek", "yasakli_kelimeler": ["belirti", "öksürük", "ateş", "hasta", "ağrı"], "zorluk": "kolay", "aciklama": "Hastalığa işaret eden fiziksel belirtiler ortaya koymak."},

    # Orta (24)
    {"kelime": "filyasyon yapmak", "yasakli_kelimeler": ["temaslı", "takip", "zincir", "ekip", "tarama"], "zorluk": "orta", "aciklama": "Bulaşıcı hastalıklı kişinin temas ettiği kimseleri sahada tespit etmek."},
    {"kelime": "sürveyans yürütmek", "yasakli_kelimeler": ["izleme", "veri", "salgın", "sağlık bakanlığı", "raporlama"], "zorluk": "orta", "aciklama": "Halk sağlığını tehdit eden hastalıkların verilerini sistematik olarak toplamak ve izlemek."},
    {"kelime": "temaslı taramak", "yasakli_kelimeler": ["filyasyon", "izolasyon", "hasta", "kişi", "tespit"], "zorluk": "orta", "aciklama": "Enfekte bireyle yan yana gelmiş insanları bulup incelemek."},
    {"kelime": "vaka sayısını bildirmek", "yasakli_kelimeler": ["rapor", "istatistik", "günlük", "tablo", "hasta"], "zorluk": "orta", "aciklama": "Tespit edilen yeni hasta sayılarını resmi makamlara iletmek."},
    {"kelime": "salgını kontrol altına almak", "yasakli_kelimeler": ["pandemi", "tedbir", "kısıtlama", "düşüş", "önleme"], "zorluk": "orta", "aciklama": "Hastalığın yayılma hızını tedbirlerle durdurmak."},
    {"kelime": "izolasyon uygulamak", "yasakli_kelimeler": ["tecrit", "ayrı", "oda", "hastane", "bulaştırmamak"], "zorluk": "orta", "aciklama": "Enfekte olmuş hastayı sağlıklı insanlardan fiziksel olarak ayırmak."},
    {"kelime": "sürü bağışıklığı kazanmak", "yasakli_kelimeler": ["toplum", "aşı", "antikor", "yüzde", "korunma"], "zorluk": "orta", "aciklama": "Toplumun büyük kısmının bağışıklık kazanmasıyla yayılımın durması."},
    {"kelime": "epidemiyolojik harita çıkarmak", "yasakli_kelimeler": ["coğrafi", "küme", "bölge", "risk", "yayılım"], "zorluk": "orta", "aciklama": "Hastalık vakalarının coğrafi dağılımını harita üzerinde göstermek."},
    {"kelime": "hijyen kurallarına uymak", "yasakli_kelimeler": ["temizlik", "kural", "sağlık", "uyarı", "dezenfeksiyon"], "zorluk": "orta", "aciklama": "Hastalık bulaşmasını önleyen temizlik protokollerini uygulamak."},
    {"kelime": "damlacık yoluyla bulaşmak", "yasakli_kelimeler": ["öksürük", "hapşırık", "hava", "partikül", "solunum"], "zorluk": "orta", "aciklama": "Ağız ve burundan çıkan mikro taneciklerle havadan yayılmak."},
    {"kelime": "kuluçka süresini beklemek", "yasakli_kelimeler": ["inkübasyon", "gün", "belirti", "gelişme", "virüs"], "zorluk": "orta", "aciklama": "Mikrobun vücuda girmesiyle ilk semptomun çıkması arasındaki süreyi gözlemek."},
    {"kelime": "seyahat kısıtlaması getirmek", "yasakli_kelimeler": ["yasak", "uçuş", "sınır", "ülke", "kapatmak"], "zorluk": "orta", "aciklama": "Virüsün bölgeler veya ülkeler arası taşınmasını engellemek için dolaşımı durdurmak."},
    {"kelime": "ölüm oranını hesaplamak", "yasakli_kelimeler": ["mortalite", "vefat", "vaka", "yüzde", "istatistik"], "zorluk": "orta", "aciklama": "Hastalığa yakalananların kaçının yaşamını yitirdiğini oranlamak."},
    {"kelime": "toplu tarama yapmak", "yasakli_kelimeler": ["test", "popülasyon", "kitlesel", "okul", "işyeri"], "zorluk": "orta", "aciklama": "Büyük insan gruplarına aynı anda tarama testi uygulamak."},
    {"kelime": "kaynağı tespit etmek", "yasakli_kelimeler": ["sıfır hasta", "köken", "başlangıç", "odak", "virüs"], "zorluk": "orta", "aciklama": "Salgının çıkış noktasını ve ilk bulaş yerini saptamak."},
    {"kelime": "sağlık protokolü yayımlamak", "yasakli_kelimeler": ["rehber", "yönerge", "bakanlık", "kurallar", "hastane"], "zorluk": "orta", "aciklama": "Tedavi ve izolasyon süreçlerini standartlaştıran kılavuz çıkarmak."},
    {"kelime": "numune almak", "yasakli_kelimeler": ["örnek", "çubuk", "boğaz", "burun", "tüp"], "zorluk": "orta", "aciklama": "Laboratuvar incelemesi için hastadan biyolojik sürüntü toplamak."},
    {"kelime": "risk grubu belirlemek", "yasakli_kelimeler": ["kronik", "yaşlı", "hassas", "kategori", "öncelik"], "zorluk": "orta", "aciklama": "Hastalığın ağır seyretme olasılığı yüksek olan kesimleri sınıflandırmak."},
    {"kelime": "antikor seviyesini ölçmek", "yasakli_kelimeler": ["kan", "bağışıklık", "seroloji", "titre", "titer"], "zorluk": "orta", "aciklama": "Kanda hastalığa karşı oluşmuş savunma proteinlerinin miktarını test etmek."},
    {"kelime": "halk sağlığı uyarısı yapmak", "yasakli_kelimeler": ["anons", "tehlike", "bildiri", "toplum", "alarm"], "zorluk": "orta", "aciklama": "Toplumu tehdit eden sağlık riskine karşı kamuoyunu bilgilendirmek."},
    {"kelime": "klinik deneme yürütmek", "yasakli_kelimeler": ["faz", "insan", "ilaç", "deney", "aşı"], "zorluk": "orta", "aciklama": "Yeni geliştirilen tıbbi ürünün insanlardaki etkinliğini ve güvenliğini test etmek."},
    {"kelime": "pik noktasını görmek", "yasakli_kelimeler": ["zirve", "tepe", "düşüş", "en yüksek", "vaka"], "zorluk": "orta", "aciklama": "Salgın eğrisinin en yüksek hasta sayısına ulaşıp gerilemeye başlaması."},
    {"kelime": "aşı pasaportu sorgulamak", "yasakli_kelimeler": ["belge", "kod", "giriş", "kontrol", "doz"], "zorluk": "orta", "aciklama": "Kişilerin aşılanma durumunu belge üzerinden doğrulamak."},
    {"kelime": "sağlık sistemini korumak", "yasakli_kelimeler": ["kapasite", "yoğun bakım", "yatak", "çöküş", "hastane"], "zorluk": "orta", "aciklama": "Hastanelerin hasta yükü altında çökmesini engellemek."},

    # Zor (14)
    {"kelime": "üreme katsayısını hesaplamak", "yasakli_kelimeler": ["r sıfır", "bulaş oranı", "sayı", "salgın dinamiği", "bulaştırma"], "zorluk": "zor", "aciklama": "Enfekte bir kişinin hastalığı ortalama kaç kişiye bulaştırdığını hesaplamak."},
    {"kelime": "insidans hızını bulmak", "yasakli_kelimeler": ["yeni vaka", "nüfus", "zaman", "oran", "hastalık"], "zorluk": "zor", "aciklama": "Belirli bir dönemde toplumda ortaya çıkan yeni vaka sıklığını hesaplamak."},
    {"kelime": "prevalansı saptamak", "yasakli_kelimeler": ["mevcut vaka", "toplam", "nokta", "dönem", "yaygınlık"], "zorluk": "zor", "aciklama": "Belirli bir anda toplumdaki toplam (eski ve yeni) hasta oranını belirlemek."},
    {"kelime": "atak hızını belirlemek", "yasakli_kelimeler": ["besin zehirlenmesi", "risk altındaki nüfus", "yüzde", "akut salgın", "oran"], "zorluk": "zor", "aciklama": "Sınırlı bir toplulukta etkene maruz kalanlar arasındaki hastalanma oranını bulmak."},
    {"kelime": "morbiditeyi değerlendirmek", "yasakli_kelimeler": ["hastalanma", "sağlık durumu", "istatistik", "nüfus", "rapor"], "zorluk": "zor", "aciklama": "Toplumda hastalığın görülme ve yayılma sıklığını analiz etmek."},
    {"kelime": "kohort çalışması yürütmek", "yasakli_kelimeler": ["izlem", "maruziyet", "prospektif", "risk", "grup"], "zorluk": "zor", "aciklama": "Bir etkene maruz kalan ve kalmayan grupları zaman içinde ileriye dönük izlemek."},
    {"kelime": "vaka-kontrol araştırması yapmak", "yasakli_kelimeler": ["retrospektif", "geçmiş", "odds ratio", "hasta", "sağlıklı"], "zorluk": "zor", "aciklama": "Hastalar ile sağlıklı bireylerin geçmiş maruziyetlerini geriye dönük karşılaştırmak."},
    {"kelime": "kesitsel analiz uygulamak", "yasakli_kelimeler": ["anlık", "nokta prevalans", "fotoğraf", "anket", "zaman"], "zorluk": "zor", "aciklama": "Belirli tek bir zaman kesitinde hastalık ve etken ilişkisini incelemek."},
    {"kelime": "endemik durumu saptamak", "yasakli_kelimeler": ["bölgesel", "sürekli", "olağan", "yerel", "seviye"], "zorluk": "zor", "aciklama": "Hastalığın belirli bir coğrafyada sürekli ve alışılmış düzeyde var olduğunu belirlemek."},
    {"kelime": "pandemi ilan etmek", "yasakli_kelimeler": ["küresel", "who", "kıtalararası", "dünya sağlık örgütü", "salgın"], "zorluk": "zor", "aciklama": "Salgının kıtalararası küresel boyuta ulaştığını resmen duyurmak."},
    {"kelime": "zoonotik geçişi kanıtlamak", "yasakli_kelimeler": ["hayvandan insana", "tür atlama", "virüs", "konak", "enfeksiyon"], "zorluk": "zor", "aciklama": "Patojenin hayvandan insana sıçradığını bilimsel olarak göstermek."},
    {"kelime": "karıştırıcı faktörü düzeltmek", "yasakli_kelimeler": ["confounding", "tabakalama", "sapma", "ilişki", "regresyon"], "zorluk": "zor", "aciklama": "Sonucu yanıltıcı şekilde etkileyen üçüncü değişkenin etkisini analizden arındırmak."},
    {"kelime": "göreceli riski hesaplamak", "yasakli_kelimeler": ["relative risk", "oran", "maruz", "kohort", "ihtimal"], "zorluk": "zor", "aciklama": "Risk faktörüne maruz kalanların kalmayanlara göre hastalanma katını bulmak."},
    {"kelime": "epidemik eğri çizmek", "yasakli_kelimeler": ["zamana göre vaka", "histogram", "salgın tipi", "ortak kaynak", "grafik"], "zorluk": "zor", "aciklama": "Vakaların başlangıç tarihlerine göre zamansal grafiğini çıkartıp salgın tipini saptamak."}
]

add_and_save_verbs('enstrumanlar', enstrumanlar_verbs)
add_and_save_verbs('epidemiyoloji', epidemiyoloji_verbs)
print('P2 done!')
