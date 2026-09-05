import os, sys, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gen_scripts.card_utils import add_and_save_verbs

# 1. ekoloji
ekoloji_verbs = [
    # Kolay (12)
    {"kelime": "ağaç dikmek", "yasakli_kelimeler": ["fidan", "orman", "toprak", "yeşillendirmek", "doğa"], "zorluk": "kolay", "aciklama": "Toprağa yeni bir fidan yerleştirip büyütmek."},
    {"kelime": "çöp toplamak", "yasakli_kelimeler": ["atık", "temizlik", "poşet", "çevre", "süpürmek"], "zorluk": "kolay", "aciklama": "Doğaya veya çevreye atılan atıkları temizlemek."},
    {"kelime": "geri dönüştürmek", "yasakli_kelimeler": ["atık", "plastik", "cam", "kutu", "yeniden"], "zorluk": "kolay", "aciklama": "Kullanılmış maddeleri yeniden işleyerek kullanılabilir hale getirmek."},
    {"kelime": "enerji tasarrufu yapmak", "yasakli_kelimeler": ["elektrik", "lamba", "fatura", "kapatmak", "harcamak"], "zorluk": "kolay", "aciklama": "Enerji kaynaklarını gereksiz tüketmeyip verimli kullanmak."},
    {"kelime": "su tasarrufu yapmak", "yasakli_kelimeler": ["musluk", "damla", "israf", "kapatmak", "içmek"], "zorluk": "kolay", "aciklama": "Suyu idareli ve bilinçli tüketmek."},
    {"kelime": "çevreyi korumak", "yasakli_kelimeler": ["doğa", "temiz", "kirlilik", "orman", "yaşam"], "zorluk": "kolay", "aciklama": "Doğal ortamı kirlenme ve tahribattan korumak."},
    {"kelime": "fidan sulamak", "yasakli_kelimeler": ["ağaç", "su", "büyümek", "hortum", "toprak"], "zorluk": "kolay", "aciklama": "Yeni dikilen küçük ağaçlara su vermek."},
    {"kelime": "orman yangını söndürmek", "yasakli_kelimeler": ["itfaiye", "ağaç", "helikopter", "su", "alev"], "zorluk": "kolay", "aciklama": "Ormanlık alanda çıkan yangına müdahale edip durdurmak."},
    {"kelime": "doğayı sevmek", "yasakli_kelimeler": ["orman", "canlı", "çiçek", "hayvan", "korumak"], "zorluk": "kolay", "aciklama": "Doğal yaşama ve çevreye karşı sevgi ve saygı beslemek."},
    {"kelime": "plastik kullanmamak", "yasakli_kelimeler": ["poşet", "şişe", "naylon", "atık", "çevre"], "zorluk": "kolay", "aciklama": "Doğada zor çözünen plastik ürünlerden kaçınmak."},
    {"kelime": "bisiklete binmek", "yasakli_kelimeler": ["pedal", "tekerlek", "egzoz", "ulaşım", "yakıt"], "zorluk": "kolay", "aciklama": "Egzoz salınımı yapmadan çevre dostu şekilde yolculuk etmek."},
    {"kelime": "toplu taşımaya binmek", "yasakli_kelimeler": ["otobüs", "metro", "araç", "trafik", "karbon"], "zorluk": "kolay", "aciklama": "Kişisel araç yerine ortak taşıtları tercih etmek."},

    # Orta (24)
    {"kelime": "karbon ayak izini azaltmak", "yasakli_kelimeler": ["emisyon", "gaz", "iklim", "tüketim", "salınım"], "zorluk": "orta", "aciklama": "Bireysel faaliyetlerin atmosfere yaydığı sera gazı miktarını düşürmek."},
    {"kelime": "fotosentez yapmak", "yasakli_kelimeler": ["bitki", "güneş", "oksijen", "karbondioksit", "klorofil"], "zorluk": "orta", "aciklama": "Bitkilerin ışık enerjisiyle besin ve oksijen üretmesi."},
    {"kelime": "kompost yapmak", "yasakli_kelimeler": ["organik", "gübre", "atık", "toprak", "çürümek"], "zorluk": "orta", "aciklama": "Mutfak ve bahçe atıklarını organik gübreye dönüştürmek."},
    {"kelime": "biyolojik çeşitliliği korumak", "yasakli_kelimeler": ["tür", "ekosistem", "canlı", "fauna", "flora"], "zorluk": "orta", "aciklama": "Canlı türlerinin ve genetik zenginliğin tükenmesini engellemek."},
    {"kelime": "erozyonu önlemek", "yasakli_kelimeler": ["toprak", "ağaçlandırma", "rüzgar", "aşınma", "sel"], "zorluk": "orta", "aciklama": "Toprağın su veya rüzgarla süpürülüp gitmesini engellemek."},
    {"kelime": "atık ayrıştırmak", "yasakli_kelimeler": ["çöp", "kutu", "plastik", "cam", "kağıt"], "zorluk": "orta", "aciklama": "Geri dönüştürülebilir maddeleri türlerine göre ayırmak."},
    {"kelime": "yenilenebilir enerji üretmek", "yasakli_kelimeler": ["güneş", "rüzgar", "panel", "santral", "temiz"], "zorluk": "orta", "aciklama": "Doğal kaynaklardan tükenmeyen enerji elde etmek."},
    {"kelime": "nesli tükenmek", "yasakli_kelimeler": ["canlı", "hayvan", "son", "tür", "yok olmak"], "zorluk": "orta", "aciklama": "Bir canlı türünün yeryüzünden tamamen silinmesi."},
    {"kelime": "ekosistemi bozmak", "yasakli_kelimeler": ["denge", "zarar", "insan", "doğa", "kirlilik"], "zorluk": "orta", "aciklama": "Doğadaki canlı ve cansız çevre uyumunu tahrip etmek."},
    {"kelime": "habitatı restore etmek", "yasakli_kelimeler": ["onarmak", "doğal", "yaşam alanı", "iyileştirmek", "flora"], "zorluk": "orta", "aciklama": "Tahrip edilmiş doğal yaşam alanını eski haline getirmek."},
    {"kelime": "su ayak izini ölçmek", "yasakli_kelimeler": ["litre", "tüketim", "hesaplamak", "üretim", "israf"], "zorluk": "orta", "aciklama": "Bir ürünün üretiminde harcanan toplam tatlı su miktarını hesaplamak."},
    {"kelime": "sera gazı salmak", "yasakli_kelimeler": ["karbondioksit", "metan", "atmosfer", "küresel ısınma", "fabrika"], "zorluk": "orta", "aciklama": "Atmosfere ısı tutucu gazlar yaymak."},
    {"kelime": "organik tarım yapmak", "yasakli_kelimeler": ["ilaçsız", "gübre", "doğal", "ürün", "sertifika"], "zorluk": "orta", "aciklama": "Kimyasal ilaç ve gübre kullanmadan tarımsal üretim yapmak."},
    {"kelime": "ağaçlandırma yapmak", "yasakli_kelimeler": ["orman", "fidan", "dikim", "erozyon", "yeşil"], "zorluk": "orta", "aciklama": "Boş veya tahrip olmuş arazilere topluca fidan dikmek."},
    {"kelime": "sıfır atık hedeflemek", "yasakli_kelimeler": ["israf", "çöp", "proje", "geri dönüşüm", "tüketim"], "zorluk": "orta", "aciklama": "Hiçbir atığın çöpe gitmediği döngüsel sistemi benimsemek."},
    {"kelime": "ozon tabakasını korumak", "yasakli_kelimeler": ["gaz", "morötesi", "güneş", "kloroflorokarbon", "atmosfer"], "zorluk": "orta", "aciklama": "Güneşin zararlı ışınlarını filtreleyen gaz katmanını korumak."},
    {"kelime": "biyobozunur ürün seçmek", "yasakli_kelimeler": ["plastik", "çözünmek", "çevre dostu", "ambalaj", "doğa"], "zorluk": "orta", "aciklama": "Doğada mikroorganizmalarca kolayca parçalanan maddeleri kullanmak."},
    {"kelime": "sulak alanları korumak", "yasakli_kelimeler": ["göl", "bataklık", "kuş", "ekosistem", "ramsar"], "zorluk": "orta", "aciklama": "Tatlı su ve göçmen kuş barınağı alanları muhafaza etmek."},
    {"kelime": "istilacı türlerle mücadele etmek", "yasakli_kelimeler": ["yerli", "popülasyon", "baskın", "zararlı", "ekosistem"], "zorluk": "orta", "aciklama": "Doğal habitata sonradan gelip yerli türleri tehdit eden canlıları denetlemek."},
    {"kelime": "çevre bilinci aşılamak", "yasakli_kelimeler": ["eğitim", "çocuk", "duyarlılık", "farkındalık", "doğa"], "zorluk": "orta", "aciklama": "Topluma doğayı koruma refleksini öğretmek."},
    {"kelime": "yağmur suyu hasadı yapmak", "yasakli_kelimeler": ["depolamak", "çatı", "tank", "bahçe", "sulama"], "zorluk": "orta", "aciklama": "Çatılardan akan yağmur sularını toplayıp tekrar kullanmak."},
    {"kelime": "yeşil bina tasarlamak", "yasakli_kelimeler": ["enerji", "leed", "yalıtım", "verimlilik", "çevre"], "zorluk": "orta", "aciklama": "Enerji ve su tasarruflu çevre dostu yapılar inşa etmek."},
    {"kelime": "deniz kirliliğini temizlemek", "yasakli_kelimeler": ["müsilaj", "plastik", "tekne", "kıyı", "okyanus"], "zorluk": "orta", "aciklama": "Sulardaki katı ve kimyasal kirliliği arındırmak."},
    {"kelime": "doğal gübre kullanmak", "yasakli_kelimeler": ["kimyasal", "hayvan", "toprak", "verim", "organik"], "zorluk": "orta", "aciklama": "Toprağı sentetik katkı olmadan organik atıklarla beslemek."},

    # Zor (14)
    {"kelime": "ötrofikasyona yol açmak", "yasakli_kelimeler": ["alg", "fosfor", "azot", "oksijensiz", "göl"], "zorluk": "zor", "aciklama": "Sularda aşırı besin maddesi birikimiyle alg patlaması ve oksijensizlik yaratmak."},
    {"kelime": "biyoakümülasyon göstermek", "yasakli_kelimeler": ["ağır metal", "besin zinciri", "birikim", "zehir", "doku"], "zorluk": "zor", "aciklama": "Zehirli maddelerin besin piramidinde üst basamaklara doğru katlanarak birikmesi."},
    {"kelime": "trofik seviyeyi belirlemek", "yasakli_kelimeler": ["besin zinciri", "üretici", "tüketici", "piramit", "enerji"], "zorluk": "zor", "aciklama": "Bir canlının beslenme zincirindeki basamağını saptamak."},
    {"kelime": "fitoremediasyon uygulamak", "yasakli_kelimeler": ["bitki", "toprak", "ağır metal", "arıtma", "temizleme"], "zorluk": "zor", "aciklama": "Kirli toprak ve suların bitkiler yardımıyla biyolojik olarak arındırılması."},
    {"kelime": "ekolojik nişi doldurmak", "yasakli_kelimeler": ["rol", "tür", "habitat", "fonksiyon", "uyum"], "zorluk": "zor", "aciklama": "Bir türün ekosistem içindeki işlevsel görevini icra etmesi."},
    {"kelime": "biyomagnifikasyon oluşturmak", "yasakli_kelimeler": ["zehir", "konsantrasyon", "avcı", "toksik", "piramit"], "zorluk": "zor", "aciklama": "Zararlı kimyasalların besin zincirinin en tepesinde en yüksek derişime ulaşması."},
    {"kelime": "süksesyon geçirmek", "yasakli_kelimeler": ["ardıllık", "değişim", "bitki örtüsü", "orman", "klimaks"], "zorluk": "zor", "aciklama": "Bir alandaki türlerin zaman içinde sırayla birbirinin yerini alması."},
    {"kelime": "klimaks evresine ulaşmak", "yasakli_kelimeler": ["denge", "kararlı", "son aşama", "komünite", "orman"], "zorluk": "zor", "aciklama": "Ekosistemin en olgun ve kararlı son denge durumuna varması."},
    {"kelime": "allokton madde taşımak", "yasakli_kelimeler": ["dış kaynak", "göl", "sediman", "havza", "organik"], "zorluk": "zor", "aciklama": "Ekosisteme dış çevreden giren organik veya inorganik girdileri iletmek."},
    {"kelime": "otokton üretim sağlamak", "yasakli_kelimeler": ["iç kaynak", "primer", "göl", "fotosentez", "ekosistem"], "zorluk": "zor", "aciklama": "Sistem içinde yerel olarak biyokütle ve besin üretmek."},
    {"kelime": "karbon yutağı oluşturmak", "yasakli_kelimeler": ["orman", "turbalık", "okyanus", "depolamak", "emisyon"], "zorluk": "zor", "aciklama": "Atmosferdeki karbondioksiti emip bünyesinde hapseden doğal alan oluşturmak."},
    {"kelime": "çölleşmeyi izlemek", "yasakli_kelimeler": ["kuraklık", "toprak", "uydu", "bozulma", "erozyon"], "zorluk": "zor", "aciklama": "Verimli arazilerin kurak çorak topraklara dönüşüm sürecini takip etmek."},
    {"kelime": "taşıma kapasitesini aşmak", "yasakli_kelimeler": ["popülasyon", "kaynak", "limit", "baskı", "birey"], "zorluk": "zor", "aciklama": "Bir habitattaki nüfusun mevcut kaynakların kaldırabileceği sınırı geçmesi."},
    {"kelime": "ekolojik borçlanmak", "yasakli_kelimeler": ["dünya limiti", "tüketim", "kaynak", "yenilenme", "aşım günü"], "zorluk": "zor", "aciklama": "Dünyanın bir yılda ürettiği doğal kaynakları yıldan önce tüketip gelecekten harcamak."}
]

# 2. ekonometri
ekonometri_verbs = [
    # Kolay (12)
    {"kelime": "veri toplamak", "yasakli_kelimeler": ["anket", "bilgi", "sayı", "analiz", "kaynak"], "zorluk": "kolay", "aciklama": "Araştırma veya analiz için sayısal bilgileri bir araya getirmek."},
    {"kelime": "grafik çizmek", "yasakli_kelimeler": ["eksen", "tablo", "görsel", "çizgi", "eğri"], "zorluk": "kolay", "aciklama": "Verilerin değişimini koordinat düzleminde görselleştirmek."},
    {"kelime": "ortalama hesaplamak", "yasakli_kelimeler": ["toplam", "bölmek", "değer", "aritmetik", "sayı"], "zorluk": "kolay", "aciklama": "Değerlerin toplamını gözlem sayısına bölerek merkezi eğilimi bulmak."},
    {"kelime": "tahmin yapmak", "yasakli_kelimeler": ["gelecek", "öngörü", "model", "fiyat", "beklenti"], "zorluk": "kolay", "aciklama": "Mevcut verilerden yola çıkarak gelecekteki bir değeri kestirmek."},
    {"kelime": "tablo hazırlamak", "yasakli_kelimeler": ["satır", "sütun", "veri", "excel", "düzenlemek"], "zorluk": "kolay", "aciklama": "Sayısal verileri satır ve sütunlar halinde düzenlemek."},
    {"kelime": "yüzde hesaplamak", "yasakli_kelimeler": ["oran", "yüz", "bölmek", "çarpmak", "pay"], "zorluk": "kolay", "aciklama": "Bir miktarın yüze oranla payını tespit etmek."},
    {"kelime": "fiyat karşılaştırmak", "yasakli_kelimeler": ["ürün", "pazar", "ucuz", "pahalı", "oran"], "zorluk": "kolay", "aciklama": "Farklı dönem veya piyasalardaki fiyatları kıyaslamak."},
    {"kelime": "anket yapmak", "yasakli_kelimeler": ["soru", "katılımcı", "cevap", "örneklem", "form"], "zorluk": "kolay", "aciklama": "Kişilere sorular yönelterek veri toplamak."},
    {"kelime": "rapor yazmak", "yasakli_kelimeler": ["sonuç", "analiz", "metin", "sunum", "özet"], "zorluk": "kolay", "aciklama": "Ekonometrik analiz bulgularını yazılı metne dökmek."},
    {"kelime": "trend takip etmek", "yasakli_kelimeler": ["eğilim", "zaman", "grafik", "yükseliş", "düşüş"], "zorluk": "kolay", "aciklama": "Verilerin zaman içerisindeki yönelimini izlemek."},
    {"kelime": "risk ölçmek", "yasakli_kelimeler": ["kayıp", "ihtimal", "oran", "yatırım", "hesaplamak"], "zorluk": "kolay", "aciklama": "Finansal veya ekonomik belirsizlik olasılığını saptamak."},
    {"kelime": "büyüme oranını bulmak", "yasakli_kelimeler": ["ekonomi", "gdp", "artış", "yıl", "yüzde"], "zorluk": "kolay", "aciklama": "Dönemsel ekonomik artış yüzdesini hesaplamak."},

    # Orta (24)
    {"kelime": "regresyon kurmak", "yasakli_kelimeler": ["bağımlı", "bağımsız", "model", "değişken", "katsayı"], "zorluk": "orta", "aciklama": "Değişkenler arasındaki ilişkiyi matematiksel denklemle modellemek."},
    {"kelime": "hipotez test etmek", "yasakli_kelimeler": ["sıfır", "anlamlılık", "p değeri", "kabul", "ret"], "zorluk": "orta", "aciklama": "Bir varsayımın istatistiksel geçerliliğini sınamak."},
    {"kelime": "korelasyon hesaplamak", "yasakli_kelimeler": ["ilişki", "katsayı", "pearson", "yön", "derece"], "zorluk": "orta", "aciklama": "İki değişken arasındaki doğrusal ilişkinin gücünü bulmak."},
    {"kelime": "zaman serisi analizi yapmak", "yasakli_kelimeler": ["dönem", "mevsimsellik", "gecikme", "tahmin", "trend"], "zorluk": "orta", "aciklama": "Kronolojik sırayla dizilmiş verilerin dinamiklerini incelemek."},
    {"kelime": "panel veri modeli kurmak", "yasakli_kelimeler": ["kesit", "zaman", "birey", "sabit etkiler", "rassal"], "zorluk": "orta", "aciklama": "Hem zaman hem birim boyutunu içeren çok boyutlu veri setini analiz etmek."},
    {"kelime": "t-testi uygulamak", "yasakli_kelimeler": ["ortalama", "anlamlılık", "serbestlik", "değer", "istatistik"], "zorluk": "orta", "aciklama": "İki grup ortalaması veya katsayının sıfırdan farklılığını test etmek."},
    {"kelime": "f-testi yapmak", "yasakli_kelimeler": ["varyans", "model", "toplu anlamlılık", "regresyon", "değer"], "zorluk": "orta", "aciklama": "Modelin bütün olarak açıklayıcılığını sınamak."},
    {"kelime": "katsayı yorumlamak", "yasakli_kelimeler": ["beta", "etki", "bağımsız", "değişken", "artış"], "zorluk": "orta", "aciklama": "Bağımsız değişkendeki bir birimlik değişimin etkisini açıklamak."},
    {"kelime": "veriyi normalize etmek", "yasakli_kelimeler": ["ölçek", "standartlaştırma", "aralık", "sıfır", "bir"], "zorluk": "orta", "aciklama": "Farklı ölçekteki verileri ortak bir aralığa getirmek."},
    {"kelime": "örneklem seçmek", "yasakli_kelimeler": ["evren", "temsil", "rassal", "büyüklük", "grup"], "zorluk": "orta", "aciklama": "Ana kütleyi temsil edecek alt grubu belirlemek."},
    {"kelime": "kukla değişken eklemek", "yasakli_kelimeler": ["dummy", "nitel", "sıfır", "bir", "kategori"], "zorluk": "orta", "aciklama": "Niteliksel özellikleri 0 ve 1 kodlarıyla modele dahil etmek."},
    {"kelime": "gecikme uzunluğu belirlemek", "yasakli_kelimeler": ["lag", "akaike", "kriter", "zaman", "model"], "zorluk": "orta", "aciklama": "Zaman serisi modelinde geçmiş dönem etkisinin kaç adım olacağını seçmek."},
    {"kelime": "sapmayı ölçmek", "yasakli_kelimeler": ["standart", "hata", "varyans", "ortalama", "dağılım"], "zorluk": "orta", "aciklama": "Verilerin ortalamadan ne kadar uzaklaştığını tespit etmek."},
    {"kelime": "güven aralığı oluşturmak", "yasakli_kelimeler": ["yüzde", "alt", "üst", "limit", "anlamlılık"], "zorluk": "orta", "aciklama": "Parametrenin belirli bir olasılıkla içinde bulunacağı aralığı belirlemek."},
    {"kelime": "logaritma almak", "yasakli_kelimeler": ["dönüşüm", "esneklik", "doğrusallaştırma", "fonksiyon", "veri"], "zorluk": "orta", "aciklama": "Üstel ilişkileri doğrusal hale getirmek için logaritmik dönüşüm yapmak."},
    {"kelime": "model kalibrasyonu yapmak", "yasakli_kelimeler": ["parametre", "uyarlama", "gerçek veri", "ayar", "denge"], "zorluk": "orta", "aciklama": "Teorik model parametrelerini ampirik verilere göre hassas şekilde ayarlamak."},
    {"kelime": "fark almak", "yasakli_kelimeler": ["durağanlık", "birinci", "seri", "trend", "çıkarma"], "zorluk": "orta", "aciklama": "Seriyi durağanlaştırmak için ardışık dönem değerlerini birbirinden çıkarmak."},
    {"kelime": "esneklik hesaplamak", "yasakli_kelimeler": ["fiyat", "talep", "yüzde", "duyarlılık", "değişim"], "zorluk": "orta", "aciklama": "Bir değişkendeki yüzdelik değişimin diğerine etkisini ölçmek."},
    {"kelime": "tahmin hatasını bulmak", "yasakli_kelimeler": ["artık", "gerçek", "fark", "kalıntı", "model"], "zorluk": "orta", "aciklama": "Modelin öngördüğü değer ile gerçekleşen değer arasındaki farkı hesaplamak."},
    {"kelime": "en küçük kareler yöntemini uygulamak", "yasakli_kelimeler": ["ols", "hata kareleri", "minimizasyon", "doğru", "parametre"], "zorluk": "orta", "aciklama": "Hata kareleri toplamını minimize ederek en uygun regresyon doğrusunu bulmak."},
    {"kelime": "varyans analizi yapmak", "yasakli_kelimeler": ["anova", "grup", "kareler toplamı", "f testi", "fark"], "zorluk": "orta", "aciklama": "Birden çok grup ortalaması arasındaki farkı varyanslar üzerinden incelemek."},
    {"kelime": "p değerini kontrol etmek", "yasakli_kelimeler": ["anlamlılık", "olasılık", "ret", "sıfır hipotezi", "alfa"], "zorluk": "orta", "aciklama": "İstatistiğin anlamlılık düzeyini olasılık değeriyle karşılaştırmak."},
    {"kelime": "simülasyon çalıştırmak", "yasakli_kelimeler": ["monte carlo", "senaryo", "rastgele", "kod", "deneme"], "zorluk": "orta", "aciklama": "Rassal değişkenlerle modelin farklı senaryolardaki davranışını simüle etmek."},
    {"kelime": "yapısal kırılma aramak", "yasakli_kelimeler": ["chow testi", "kriz", "rejim", "parametre değişimi", "dönem"], "zorluk": "orta", "aciklama": "Veri setinde kriz veya politika kaynaklı rejim değişimini tespit etmek."},

    # Zor (14)
    {"kelime": "içselliği gidermek", "yasakli_kelimeler": ["araç değişken", "endojenlik", "hata terimi", "korelasyon", "2sls"], "zorluk": "zor", "aciklama": "Açıklayıcı değişken ile hata terimi arasındaki bağıntıyı ortadan kaldırmak."},
    {"kelime": "koentegrasyon testi yapmak", "yasakli_kelimeler": ["johansen", "engle granger", "uzun dönem", "durağanlık", "ilişki"], "zorluk": "zor", "aciklama": "Durağan olmayan seriler arasındaki uzun vadeli denge ilişkisini sınamak."},
    {"kelime": "otokorelasyonu saptamak", "yasakli_kelimeler": ["durbin watson", "breusch godfrey", "hata terimi", "bağımlılık", "seri"], "zorluk": "zor", "aciklama": "Hata terimlerinin ardışık dönemlerde birbiriyle ilişkili olmasını tespit etmek."},
    {"kelime": "değişen varyansı düzeltmek", "yasakli_kelimeler": ["heteroskedasite", "white", "ağırlıklı", "hata", "standart"], "zorluk": "zor", "aciklama": "Hata terimi varyansının sabit olmaması sorununu gidermek."},
    {"kelime": "çoklu doğrusal bağlantıyı test etmek", "yasakli_kelimeler": ["vif", "multicollinarity", "yüksek korelasyon", "bağımsız", "sapma"], "zorluk": "zor", "aciklama": "Bağımsız değişkenlerin birbirleriyle aşırı ilişkili olup olmadığını incelemek."},
    {"kelime": "vektör otoregresyonu tahmin etmek", "yasakli_kelimeler": ["var modeli", "gecikme", "etki tepki", "simultane", "dinamik"], "zorluk": "zor", "aciklama": "Birden çok zaman serisinin birbirini karşılıklı etkilediği sistemi tahmin etmek."},
    {"kelime": "etki-tepki fonksiyonu türetmek", "yasakli_kelimeler": ["şok", "grafik", "var", "dalgalanma", "yanıt"], "zorluk": "zor", "aciklama": "Bir değişkene gelen tek seferlik şokun diğer değişkenlerdeki zamansal izini çizmek."},
    {"kelime": "varyans ayrıştırması yapmak", "yasakli_kelimeler": ["şok payı", "tahmin hatası", "var", "yüzde", "katkı"], "zorluk": "zor", "aciklama": "Tahmin hatası varyansında her bir şokun yüzde payını hesaplamak."},
    {"kelime": "araç değişken kullanmak", "yasakli_kelimeler": ["iv", "enstrüman", "endojen", "dışsal", "ilişki"], "zorluk": "zor", "aciklama": "İçsel bağımsız değişken yerine dışsal bir değişkeni modele sokmak."},
    {"kelime": "maksimum olabilirlik kestirimi yapmak", "yasakli_kelimeler": ["mle", "log likelihood", "fonksiyon", "parametre", "maksimizasyon"], "zorluk": "zor", "aciklama": "Örneklem verilerinin ortaya çıkma olasılığını en yüksek kılan parametreleri bulmak."},
    {"kelime": "birim kök sınaması yapmak", "yasakli_kelimeler": ["adf", "durağanlık", "phillips perron", "kpss", "seri"], "zorluk": "zor", "aciklama": "Zaman serisinin durağan olup olmadığını istatistiksel olarak test etmek."},
    {"kelime": "genelleştirilmiş momentler yöntemini kullanmak", "yasakli_kelimeler": ["gmm", "ortogonalite", "koşul", "ağırlık matrisi", "iv"], "zorluk": "zor", "aciklama": "Moment koşullarına dayalı parametre kestirim yöntemi uygulamak."},
    {"kelime": "arch testi uygulamak", "yasakli_kelimeler": ["volatilite", "koşullu varyans", "engle", "finans", "kümelenme"], "zorluk": "zor", "aciklama": "Zaman serisinde değişken varyans kümelenmesini test etmek."},
    {"kelime": "granger nedenselliğini araştırmak", "yasakli_kelimeler": ["öncülük", "tahmin", "yön", "gecikme", "sebep"], "zorluk": "zor", "aciklama": "Bir serideki geçmiş değerlerin diğer seriyi tahmin etmede öncülük edip etmediğini sınamak."}
]

add_and_save_verbs('ekoloji', ekoloji_verbs)
add_and_save_verbs('ekonometri', ekonometri_verbs)
print('P1 done!')
