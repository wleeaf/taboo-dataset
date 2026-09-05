import os, sys, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gen_scripts.card_utils import add_and_save_verbs

# 23. hukuk
hukuk_verbs = [
    # Kolay (12)
    {"kelime": "dava açmak", "yasakli_kelimeler": ["mahkeme", "avukat", "dilekçe", "hakim", "hakkını aramak"], "zorluk": "kolay", "aciklama": "Bir anlaşmazlığı çözmesi için mahkemeye resmi başvuru yapmak."},
    {"kelime": "savunma yapmak", "yasakli_kelimeler": ["avukat", "sanık", "hakim", "iddia", "suçsuzluk"], "zorluk": "kolay", "aciklama": "Yöneltilen suçlama veya iddiaya karşı kendini savunmak."},
    {"kelime": "şahitlik yapmak", "yasakli_kelimeler": ["tanık", "gördüğünü anlatmak", "yemin", "mahkeme", "ifade"], "zorluk": "kolay", "aciklama": "Olay anında gördüklerini veya bildiklerini mahkemede anlatmak."},
    {"kelime": "sözleşme imzalamak", "yasakli_kelimeler": ["kontrat", "madde", "anlaşma", "taraflar", "kalem"], "zorluk": "kolay", "aciklama": "İki taraf arasındaki hukuki şartları kabul edip imzalamak."},
    {"kelime": "itiraz etmek", "yasakli_kelimeler": ["kabul etmemek", "karar", "haksızlık", "hakim", "söz hakkı"], "zorluk": "kolay", "aciklama": "Verilen bir kararın veya beyanın geçersizliğini öne sürmek."},
    {"kelime": "ceza vermek", "yasakli_kelimeler": ["hakim", "hapis", "para", "mahkeme", "suç"], "zorluk": "kolay", "aciklama": "Suç işlediği sabit görülen kişiye yaptırım uygulamak."},
    {"kelime": "ifade vermek", "yasakli_kelimeler": ["karakol", "savcı", "anlatmak", "soru", "tutanak"], "zorluk": "kolay", "aciklama": "Polis veya savcının sorularına resmi tutanakla cevap vermek."},
    {"kelime": "boşanmak", "yasakli_kelimeler": ["evlilik", "ayrılmak", "nafaka", "mahkeme", "eş"], "zorluk": "kolay", "aciklama": "Evlilik birliğini mahkeme kararıyla hukuken sonlandırmak."},
    {"kelime": "avukat tutmak", "yasakli_kelimeler": ["vekalet", "savunma", "hukukçu", "dava", "ücret"], "zorluk": "kolay", "aciklama": "Hukuki süreçte kendini temsil etmesi için hukukçuyla anlaşmak."},
    {"kelime": "kanunlara uymak", "yasakli_kelimeler": ["kural", "yasa", "vatandaş", "ceza", "düzen"], "zorluk": "kolay", "aciklama": "Devletin koyduğu yasal kurallara riayet etmek."},
    {"kelime": "tazminat istemek", "yasakli_kelimeler": ["zarar", "para", "mağdur", "ödetmek", "dava"], "zorluk": "kolay", "aciklama": "Uğranılan maddi veya manevi zararın karşılanmasını talep etmek."},
    {"kelime": "şikayetçi olmak", "yasakli_kelimeler": ["suç duyurusu", "dilekçe", "karakol", "mağdur", "başvuru"], "zorluk": "kolay", "aciklama": "Kendisine haksızlık yapan kişinin cezalandırılmasını istemek."},

    # Orta (24)
    {"kelime": "temyize başvurmak", "yasakli_kelimeler": ["yargıtay", "üst mahkeme", "karar bozma", "istinaf", "hukuki inceleme"], "zorluk": "orta", "aciklama": "Yerel mahkemenin verdiği kararı denetlenmesi için Yargıtay'a taşımak."},
    {"kelime": "beraat etmek", "yasakli_kelimeler": ["suçsuz bulunmak", "aklanmak", "hapis yok", "karar", "tahliye"], "zorluk": "orta", "aciklama": "Yargılama sonucunda suçsuzluğu kanıtlanıp cezadan kurtulmak."},
    {"kelime": "haciz koydurmak", "yasakli_kelimeler": ["icra", "borç", "mal varlığı", "memur", "alacak"], "zorluk": "orta", "aciklama": "Borcunu ödemeyen kişinin mal varlığına resmi yoldan el koydurmak."},
    {"kelime": "ihtiyati tedbir istemek", "yasakli_kelimeler": ["dava sonuna kadar", "mal kaçırma önleme", "geçici koruma", "hakim", "güvence"], "zorluk": "orta", "aciklama": "Dava sürerken hakkın kaybolmaması için mahkemeden geçici koruma kararı almak."},
    {"kelime": "vekaletname çıkarmak", "yasakli_kelimeler": ["noter", "yetki verme", "avukat", "resmi belge", "temsil"], "zorluk": "orta", "aciklama": "Kişinin kendisini temsil etmesi için noterde vekalet belgesi düzenletmesi."},
    {"kelime": "bilirkişi raporu istemek", "yasakli_kelimeler": ["uzman görüşü", "teknik inceleme", "hakim", "tespit", "dosya"], "zorluk": "orta", "aciklama": "Uzmanlık gerektiren konularda heyetten teknik değerlendirme talep etmek."},
    {"kelime": "arabuluculuğa gitmek", "yasakli_kelimeler": ["mahkemesiz anlaşma", "uzlaşma", "taraflar", "dava şartı", "masada çözme"], "zorluk": "orta", "aciklama": "Uyuşmazlığı dava açmadan tarafsız arabulucu huzurunda uzlaşarak çözmek."},
    {"kelime": "delil toplamak", "yasakli_kelimeler": ["ispat", "kamera kaydı", "belge", "tanık", "mahkemeye sunma"], "zorluk": "orta", "aciklama": "İddiayı kanıtlayacak somut evrak ve şahitleri bir araya getirmek."},
    {"kelime": "zaman aşımına uğramak", "yasakli_kelimeler": ["süre dolması", "dava hakkı kaybı", "yıl", "düşme", "kanuni müddet"], "zorluk": "orta", "aciklama": "Kanunun tanıdığı yasal sürenin dolması sebebiyle hakkın talep edilemez hale gelmesi."},
    {"kelime": "kefaletle serbest kalmak", "yasakli_kelimeler": ["teminat akçesi", "tahliye", "tutuksuz yargılanma", "para yatırma", "adli kontrol"], "zorluk": "orta", "aciklama": "Belirli bir teminat yatırarak tutuklu halden serbest bırakılmak."},
    {"kelime": "kamu davası açmak", "yasakli_kelimeler": ["cumhuriyet savcısı", "iddianame", "toplum adına", "suç", "ağır ceza"], "zorluk": "orta", "aciklama": "Savcının toplum adına suç işleyen sanığa karşı dava ikame etmesi."},
    {"kelime": "miras reddetmek", "yasakli_kelimeler": ["borçlu tereke", "sulh hukuk", "mirasçı", "üç ay", "kabul etmeme"], "zorluk": "orta", "aciklama": "Vefat eden kişinin borçları sebebiyle mirasını yasal olarak reddetmek."},
    {"kelime": "ihtarname çekmek", "yasakli_kelimeler": ["noter", "uyarı", "süre verme", "borç", "resmi tebligat"], "zorluk": "orta", "aciklama": "Karşı tarafa edimini yerine getirmesi için noterden resmi bildirim yollamak."},
    {"kelime": "adli kontrol şartı getirmek", "yasakli_kelimeler": ["imza atma", "yurt dışı çıkış yasağı", "tutuklama alternatifi", "karakol", "hakim"], "zorluk": "orta", "aciklama": "Şüpheliyi tutuklamadan düzenli imza ve seyahat yasağıyla denetim altına almak."},
    {"kelime": "tahliye kararı vermek", "yasakli_kelimeler": ["cezaevi", "salıverilme", "serbest kalma", "koğuş", "tutukluluk"], "zorluk": "orta", "aciklama": "Cezaevindeki tutuklunun serbest bırakılmasına hükmetmek."},
    {"kelime": "mütekabiliyet ilkesi uygulamak", "yasakli_kelimeler": ["karşılıklılık", "uluslararası hukuk", "aynı muamele", "iki devlet", "diplomasi"], "zorluk": "orta", "aciklama": "Bir devlete kendi vatandaşlarına gösterdiği hukuki muamelenin aynısını tatbik etmek."},
    {"kelime": "hükmün açıklanmasını geri bırakmak", "yasakli_kelimeler": ["hagb", "beş yıl denetim", "ceza erteleme", "sabıkaya işlememe", "şartlı"], "zorluk": "orta", "aciklama": "Verilen cezanın denetim süresi boyunca suç işlenmemesi kaydıyla askıda tutulması."},
    {"kelime": "keşif yapmak", "yasakli_kelimeler": ["olay yeri inceleme", "hakim", "bilirkişi", "arazi", "yerinde tespit"], "zorluk": "orta", "aciklama": "Mahkeme heyetinin uyuşmazlık konusunu yerinde bizzat incelemesi."},
    {"kelime": "nafaka bağlamak", "yasakli_kelimeler": ["aylık ödeme", "boşanma", "çocuk", "tedbir", "yoksulluk"], "zorluk": "orta", "aciklama": "Boşanma sonrası yoksulluğa düşen eşe veya çocuğa aylık ödeme kararı vermek."},
    {"kelime": "iddianame düzenlemek", "yasakli_kelimeler": ["savcı", "sevk maddesi", "suçlama", "mahkeme kabulü", "ceza istemi"], "zorluk": "orta", "aciklama": "Savcının topladığı delillerle sanığın cezalandırılmasını istediği resmi metni yazmak."},
    {"kelime": "istinaf incelemesine göndermek", "yasakli_kelimeler": ["bölge adliye mahkemesi", "ara derece", "itiraz", "karar", "yeniden duruşma"], "zorluk": "orta", "aciklama": "İlk derece mahkemesi kararını hem usul hem esas yönünden üst mahkemeye taşımak."},
    {"kelime": "fesih bildiriminde bulunmak", "yasakli_kelimeler": ["işten çıkarma", "sözleşme sonlandırma", "ihbar süresi", "tek taraflı", "istifa"], "zorluk": "orta", "aciklama": "İş veya kira sözleşmesini tek taraflı irade beyanıyla bitirmek."},
    {"kelime": "sulh olmak", "yasakli_kelimeler": ["anlaşmak", "barışmak", "davadan feragat", "orta yol", "karşılıklı ödün"], "zorluk": "orta", "aciklama": "Dava konusundaki anlaşmazlığı karşılıklı ödünlerle mahkemede tatlıya bağlamak."},
    {"kelime": "duruşma zaptı yazdırmak", "yasakli_kelimeler": ["katip", "tutanak", "hakim", "yaz kızım", "beyan"], "zorluk": "orta", "aciklama": "Duruşmada söylenenleri hakimin ağzından katibe zapta geçirtmek."},

    # Zor (14)
    {"kelime": "içtihadı birleştirme kararı almak", "yasakli_kelimeler": ["yargıtay genel kurulu", "bağlayıcı", "farklı daire kararları", "hukuk birliği", "emsal"], "zorluk": "zor", "aciklama": "Farklı mahkeme dairelerinin çelişkili kararlarını tek bir bağlayıcı ilkeyle birleştirmek."},
    {"kelime": "lex retro non agit kuralını gözetmek", "yasakli_kelimeler": ["kanunların geriye yürümezliği", "ceza hukuku", "aleyhe kanun", "geçmişe etki etmeme", "anayasal ilke"], "zorluk": "zor", "aciklama": "Ceza yasalarının yürürlüğe girdiği tarihten önceki fiillere aleyhte uygulanamayacağı ilkesine uymak."},
    {"kelime": "görevi kötüye kullanmayı saptamak", "yasakli_kelimeler": ["kamu görevlisi", "nüfuz ticareti", "haksız menfaat", "tck 257", "zarar"], "zorluk": "zor", "aciklama": "Memurun yetkilerini kanuna aykırı kullanarak kamuyu zarara uğrattığını kanıtlamak."},
    {"kelime": "iyiniyet karinesine dayanmak", "yasakli_kelimeler": ["türk medeni kanunu m.3", "aslolan iyiniyettir", "hak kazanımı", "hukuki güvence", "bilmeme"], "zorluk": "zor", "aciklama": "Bir hakkın kazanılmasında kişinin aksi ispatlanana kadar dürüst ve habersiz olduğunu savunmak."},
    {"kelime": "sebepsiz zenginleşmeyi kanıtlamak", "yasakli_kelimeler": ["haklı bir sebep olmaksızın", "mal varlığı artışı", "iade talebi", "borçlar kanunu", "fakirleşme"], "zorluk": "zor", "aciklama": "Bir kimsenin başkası aleyhine geçerli hukuki sebep olmadan mal edinmesini ispatlamak."},
    {"kelime": "tenkis davası açmak", "yasakli_kelimeler": ["saklı pay", "miras bırakanın tasarrufu", "indirim", "vasiyetname aşımı", "mirasçı hakkı"], "zorluk": "zor", "aciklama": "Saklı paylı mirasçıların hakkını çiğneyen bağış ve vasiyetlerin geri alınmasını istemek."},
    {"kelime": "muris muvazaasını ispatlamak", "yasakli_kelimeler": ["mirastan mal kaçırma", "sahte satış", "bağış gizleme", "tapu iptali", "mirasçı"], "zorluk": "zor", "aciklama": "Miras bırakanın malını diğer çocuklardan kaçırmak için kağıt üzerinde satmış gibi yaptığını belgelemek."},
    {"kelime": "kanun yararına bozma istemek", "yasakli_kelimeler": ["adalet bakanlığı", "kesinleşmiş karar", "yargıtay başsavcısı", "sanık lehine", "olağanüstü kanun yolu"], "zorluk": "zor", "aciklama": "Kesinleşmiş hükümdeki hukuka aykırılığı gidermek için olağanüstü temyize başvurmak."},
    {"kelime": "ceza ehliyetini raporlamak", "yasakli_kelimeler": ["akıl sağlığı", "adli tıp kurumu", "fiilin hukuki anlam ve sonuçları", "tck 32", "vesayet"], "zorluk": "zor", "aciklama": "Sanığın suç anında eylemlerinin idrak ve irade yeteneğine sahip olup olmadığını rapor etmek."},
    {"kelime": "külli halefiyet tesis etmek", "yasakli_kelimeler": ["terekenin intikali", "tüm hak ve borçlar", "kendiliğinden geçiş", "mirasçılık", "evrensel intikal"], "zorluk": "zor", "aciklama": "Ölenin tüm hak ve borçlarının bir bütün olarak doğrudan mirasçılara intikal etmesi."},
    {"kelime": "def'i hakkını ileri sürmek", "yasakli_kelimeler": ["itiraz karşıtı", "borcu kabul edip ifadan kaçınma", "zamanaşımı def'i", "hak kullanımı", "mahkeme"], "zorluk": "zor", "aciklama": "Borcun varlığını inkar etmeksizin özel bir sebebe dayanarak ödemekten kaçınma hakkını kullanmak."},
    {"kelime": "gabin iddiasında bulunmak", "yasakli_kelimeler": ["aşırı yararlanma", "açık orantısızlık", "zor durumda kalma", "deneyimsizlik", "sözleşmeyi iptal"], "zorluk": "zor", "aciklama": "Karşı tarafın zor durumundan faydalanarak aşırı fahiş edim farkı yarattığını iddia etmek."},
    {"kelime": "tüzel kişilik perdesini aralamak", "yasakli_kelimeler": ["şirket ortakları", "sorumluluktan kaçma", "mal ayrılığı istisnası", "şahsi sorumluluk", "alacaklı"], "zorluk": "zor", "aciklama": "Şirket tüzel kişiliğinin arkasına saklanarak borç kaçıran ortağın şahsi malına ulaşmak."},
    {"kelime": "mücbir sebep bildirmek", "yasakli_kelimeler": ["force majeure", "öngörülemez olay", "deprem savaş", "sorumluluktan kurtulma", "edim imkansızlığı"], "zorluk": "zor", "aciklama": "İradesi dışındaki olağanüstü felaketler sebebiyle taahhüdünü yerine getiremediğini belgelemek."}
]

# 24. iktisat
iktisat_verbs = [
    # Kolay (12)
    {"kelime": "para harcamak", "yasakli_kelimeler": ["satın almak", "tüketim", "ödeme", "cüzdan", "masraf"], "zorluk": "kolay", "aciklama": "Mal veya hizmet almak için eldeki paradan ödemede bulunmak."},
    {"kelime": "para biriktirmek", "yasakli_kelimeler": ["tasarruf", "kumbara", "banka", "birikim", "gelecek"], "zorluk": "kolay", "aciklama": "Gelirin harcanmayan kısmını kenara ayırıp saklamak."},
    {"kelime": "vergi ödemek", "yasakli_kelimeler": ["devlet", "kdv", "gelir", "maliye", "fatura"], "zorluk": "kolay", "aciklama": "Kamu giderlerine katılmak için devlete yasal pay vermek."},
    {"kelime": "fiyat belirlemek", "yasakli_kelimeler": ["etiket", "satış", "ücret", "zam", "maliyet"], "zorluk": "kolay", "aciklama": "Satılacak malın kaç liradan verileceğini tespit etmek."},
    {"kelime": "borç almak", "yasakli_kelimeler": ["kredi", "banka", "arkadaş", "geri ödemek", "para"], "zorluk": "kolay", "aciklama": "Geri vermek üzere başkasından veya bankadan para temin etmek."},
    {"kelime": "yatırım yapmak", "yasakli_kelimeler": ["altın", "arsa", "hisse", "kazanç", "sermaye"], "zorluk": "kolay", "aciklama": "Gelecekte değer kazanması amacıyla parasını bir varlığa yatırmak."},
    {"kelime": "üretim yapmak", "yasakli_kelimeler": ["fabrika", "mal", "işçi", "hammadde", "piyasa"], "zorluk": "kolay", "aciklama": "İhtiyaçları karşılamak üzere mal veya hizmet meydana getirmek."},
    {"kelime": "ithalat yapmak", "yasakli_kelimeler": ["dış alım", "yabancı ülke", "gümrük", "döviz", "getirtmek"], "zorluk": "kolay", "aciklama": "Yabancı ülkelerden mal ve hizmet satın alıp ülkeye getirmek."},
    {"kelime": "ihracat yapmak", "yasakli_kelimeler": ["dış satım", "yurt dışı", "göndermek", "döviz kazanmak", "mal"], "zorluk": "kolay", "aciklama": "Ülkede üretilen malları yabancı ülkelere satmak."},
    {"kelime": "indirim yapmak", "yasakli_kelimeler": ["ucuzluk", "fiyat kırmak", "kampanya", "yüzde", "satış"], "zorluk": "kolay", "aciklama": "Ürünün satış fiyatını geçici olarak düşürmek."},
    {"kelime": "pazarlık etmek", "yasakli_kelimeler": ["fiyat düşürme", "anlaşma", "çarşı", "indirim", "satıcı"], "zorluk": "kolay", "aciklama": "Alışverişte daha uygun bir fiyata anlaşmak için satıcıyla konuşmak."},
    {"kelime": "kar etmek", "yasakli_kelimeler": ["kazanç", "gelir gider farkı", "ticaret", "artı", "para kazanmak"], "zorluk": "kolay", "aciklama": "Maliyetinin üzerinde satış yaparak kazanç sağlamak."},

    # Orta (24)
    {"kelime": "faiz oranını artırmak", "yasakli_kelimeler": ["merkez bankası", "politika faizi", "enflasyon", "sıkılaşma", "kredi maliyeti"], "zorluk": "orta", "aciklama": "Merkez bankasının piyasa borçlanma faizini yükseltmesi."},
    {"kelime": "enflasyonu düşürmek", "yasakli_kelimeler": ["fiyat artışları", "alım gücü", "dezenflasyon", "para politikası", "tüfe"], "zorluk": "orta", "aciklama": "Genel fiyat seviyesindeki yükseliş hızını kontrol altına almak."},
    {"kelime": "arz talep dengesi kurmak", "yasakli_kelimeler": ["piyasa dengesi", "denge fiyatı", "tüketici", "üretici", "kesişim"], "zorluk": "orta", "aciklama": "Piyasadaki mal arzı ile tüketici talebinin eşitlendiği fiyatı bulmak."},
    {"kelime": "bütçe açığını kapatmak", "yasakli_kelimeler": ["gelir gider dengesizliği", "borçlanma", "tasarruf", "hazine", "maliye"], "zorluk": "orta", "aciklama": "Devlet harcamalarının gelirleri aştığı farkı telafi etmek."},
    {"kelime": "para basmak", "yasakli_kelimeler": ["emisyon", "darphane", "likidite", "banknot", "merkez bankası"], "zorluk": "orta", "aciklama": "Piyasaya yeni kağıt para veya madeni para sürmek."},
    {"kelime": "cari açık vermek", "yasakli_kelimeler": ["ithalat ihracat farkı", "döviz çıkışı", "dış ticaret", "açık", "ödeme dengesi"], "zorluk": "orta", "aciklama": "Bir ülkenin dış dünyadan aldıklarının sattıklarından fazla olması."},
    {"kelime": "özelleştirme yapmak", "yasakli_kelimeler": ["kit", "kamu malı", "özel sektör", "satış", "devletten devir"], "zorluk": "orta", "aciklama": "Devlete ait kamu iktisadi kuruluşlarını özel sektöre devretmek."},
    {"kelime": "alım gücünü artırmak", "yasakli_kelimeler": ["refah", "maaş zammı", "fiyat ucuzluğu", "sepet", "reel gelir"], "zorluk": "orta", "aciklama": "Bireylerin paralarıyla daha fazla mal ve hizmet alabilmesini sağlamak."},
    {"kelime": "devalüasyon yapmak", "yasakli_kelimeler": ["milli para", "değer kaybı", "döviz kuru", "sabit kur", "hükümet"], "zorluk": "orta", "aciklama": "Ulusal paranın yabancı para birimleri karşısındaki resmi değerini düşürmek."},
    {"kelime": "gayrisafi yurtiçi hasılayı hesaplamak", "yasakli_kelimeler": ["gsyh", "milli gelir", "toplam üretim", "bir yıl", "katma değer"], "zorluk": "orta", "aciklama": "Ülke sınırları içinde bir yılda üretilen tüm nihai mal ve hizmetlerin toplam değerini bulmak."},
    {"kelime": "teşvik paketi açıklamak", "yasakli_kelimeler": ["vergi indirimi", "hibe", "yatırımcı", "sektör", "destek"], "zorluk": "orta", "aciklama": "Ekonomik canlanma için belirli sektörlere mali destek sunmak."},
    {"kelime": "istihdam yaratmak", "yasakli_kelimeler": ["iş imkanı", "işsizlik", "çalışan", "yeni iş yeri", "personel"], "zorluk": "orta", "aciklama": "İşsiz kişilere yeni çalışma ve gelir alanları açmak."},
    {"kelime": "fırsat maliyetini hesaplamak", "yasakli_kelimeler": ["alternatif maliyet", "vazgeçilen seçenek", "seçim", "ikinci en iyi", "karar"], "zorluk": "orta", "aciklama": "Bir tercihi yaparken vazgeçilen en iyi ikinci seçeneğin değerini tartmak."},
    {"kelime": "monopol olmak", "yasakli_kelimeler": ["tekel", "tek satıcı", "rekabetsiz", "fiyat belirleyici", "piyasa hakimiyeti"], "zorluk": "orta", "aciklama": "Bir piyasada rakipsiz tek üretici veya satıcı konumuna gelmek."},
    {"kelime": "marjinal faydayı ölçmek", "yasakli_kelimeler": ["ek birim", "tüketim tatmini", "azalan fayda", "son ürün", "katkı"], "zorluk": "orta", "aciklama": "Bir maldan tüketilen her ek birimin sağladığı ilave tatmini hesaplamak."},
    {"kelime": "küresel krizi yönetmek", "yasakli_kelimeler": ["resesyon", "durgunluk", "likidite sıkışması", "kurtarma paketi", "piyasa çöküşü"], "zorluk": "orta", "aciklama": "Dünya çapındaki finansal daralmanın yerel ekonomiye etkilerini bertaraf etmek."},
    {"kelime": "sermaye birikimi sağlamak", "yasakli_kelimeler": ["yatırım", "fon", "büyüme", "makine teçhizat", "tasarruf"], "zorluk": "orta", "aciklama": "Gelecek yatırımlar için gerekli olan fiziki ve finansal sermayeyi büyütmek."},
    {"kelime": "vergi matrahını belirlemek", "yasakli_kelimeler": ["vergiye tabi tutar", "kazanç", "oran", "muafiyet", "beyanname"], "zorluk": "orta", "aciklama": "Üzerinden vergi hesaplanacak net kazanç miktarını tespit etmek."},
    {"kelime": "taban fiyat belirlemek", "yasakli_kelimeler": ["çiftçi koruma", "asgari ücret", "piyasa müdahalesi", "en düşük fiyat", "tarım"], "zorluk": "orta", "aciklama": "Üreticiyi korumak için devletin bir mala uygulanabilecek en alt fiyatı koyması."},
    {"kelime": "tavan fiyat koymak", "yasakli_kelimeler": ["tüketici koruma", "karaborsa riski", "en yüksek fiyat", "fahiş fiyat engeli", "müdahale"], "zorluk": "orta", "aciklama": "Tüketiciyi korumak amacıyla bir malın satılabileceği en yüksek yasal sınırı çekmek."},
    {"kelime": "tüketici güvenini ölçmek", "yasakli_kelimeler": ["endeks", "harcama eğilimi", "anket", "beklenti", "ekonomik gidişat"], "zorluk": "orta", "aciklama": "Halkın ekonomik gidişata olan iyimserlik veya karamsarlık düzeyini anketle belirlemek."},
    {"kelime": "damping yapmak", "yasakli_kelimeler": ["maliyetin altına satış", "haksız rekabet", "dış pazar", "rakibi batırma", "ucuz ihracat"], "zorluk": "orta", "aciklama": "Dış piyasada rakipleri yok etmek için malı kendi maliyetinin bile altına satmak."},
    {"kelime": "resesyona girmek", "yasakli_kelimeler": ["ekonomik küçülme", "iki çeyrek üst üste", "durgunluk", "negatif büyüme", "üretim düşüşü"], "zorluk": "orta", "aciklama": "Ekonominin üst üste iki çeyrek daralarak durgunluğa saplanması."},
    {"kelime": "katma değer üretmek", "yasakli_kelimeler": ["yüksek teknoloji", "ham madde işleme", "nitelikli ürün", "fiyat farkı", "zenginleşme"], "zorluk": "orta", "aciklama": "Girdileri işleyip bilgi ve teknoloji katarak çok daha değerli son ürün ortaya koymak."},

    # Zor (14)
    {"kelime": "stagflasyonla mücadele etmek", "yasakli_kelimeler": ["durgunluk ve enflasyon", "aynı anda işsizlik", "para politikası açmazı", "şok", "üretim düşüşü"], "zorluk": "zor", "aciklama": "Aynı anda hem yüksek enflasyon hem de ekonomik durgunluk ve işsizliği yenmeye çalışmak."},
    {"kelime": "kantitatif gevşeme uygulamak", "yasakli_kelimeler": ["quantitative easing", "tahvil alımı", "bilanço büyütme", "piyasaya para sürme", "fed"], "zorluk": "zor", "aciklama": "Merkez bankasının finansal varlıklar satın alarak piyasaya doğrudan devasa likidite vermesi."},
    {"kelime": "gini katsayısını hesaplamak", "yasakli_kelimeler": ["lorenz eğrisi", "gelir adaletsizliği", "sıfır bir aralığı", "dağılım", "toplum"], "zorluk": "zor", "aciklama": "Bir ülkedeki gelir dağılımı eşitsizliğini 0 ile 1 arasındaki katsayıyla matematiksel ölçmek."},
    {"kelime": "phillips eğrisini yorumlamak", "yasakli_kelimeler": ["enflasyon işsizlik ödünleşimi", "kısa dönem", "ters orantı", "ücret artışı", "makroekonomi"], "zorluk": "zor", "aciklama": "İşsizlik ile enflasyon arasındaki ters yönlü takas ilişkisini analiz etmek."},
    {"kelime": "likidite tuzağına düşmek", "yasakli_kelimeler": ["keynes", "sıfır faiz", "para politikasının etkisizliği", "tahvil talebi", "para biriktirme"], "zorluk": "zor", "aciklama": "Faizler sıfıra indiğinde para arzı artırılsa dahi harcama yapılmayıp paranın yastık altına gitmesi."},
    {"kelime": "pareto optimumuna ulaşmak", "yasakli_kelimeler": ["hiç kimseyi kötüleştirmeden", "etkin refah", "kaynak dağılımı", "iktisadi denge", "verimlilik"], "zorluk": "zor", "aciklama": "Birinin durumunu kötüleştirmeden başkasının durumunun iyileştirilemeyeceği en etkin refah durumuna varmak."},
    {"kelime": "is-LM dengesi türetmek", "yasakli_kelimeler": ["mal piyasası para piyasası", "faiz hasıla", "kesişim", "maliye para politikası", "hicks"], "zorluk": "zor", "aciklama": "Mal piyasası ile para piyasasının eşanlı dengesini faiz ve milli gelir ekseninde kurmak."},
    {"kelime": "dışlama etkisini ölçmek", "yasakli_kelimeler": ["crowding out", "kamu borçlanması", "faiz artışı", "özel yatırımların düşmesi", "bütçe harcaması"], "zorluk": "zor", "aciklama": "Devlet harcamalarının faizleri yükselterek özel sektör yatırımlarını piyasadan kovmasını saptamak."},
    {"kelime": "pigou etkisini açıklamak", "yasakli_kelimeler": ["reel balans", "fiyat düşüşü", "servet artışı", "tüketim canlanması", "klasik model"], "zorluk": "zor", "aciklama": "Fiyatlar düştüğünde elde tutulan nakdin reel değerinin artarak tüketimi canlandırmasını izah etmek."},
    {"kelime": "laffer eğrisi analizi yapmak", "yasakli_kelimeler": ["vergi oranı", "vergi geliri", "çan eğrisi", "optimum oran", "araz kesintisi"], "zorluk": "zor", "aciklama": "Aşırı yüksek vergi oranlarının ekonomik faaliyeti baltalayarak vergi gelirlerini düşürdüğünü modellemek."},
    {"kelime": "mundell-Fleming modelini işletmek", "yasakli_kelimeler": ["açık ekonomi", "sermaye hareketliliği", "sabit esnek kur", "üçlü imkansızlık", "politika etkinliği"], "zorluk": "zor", "aciklama": "Açık bir ekonomide sermaye serbestisi ve kur rejimine göre para ve maliye politikalarının gücünü tartmak."},
    {"kelime": "solow büyüme modelini kurmak", "yasakli_kelimeler": ["sermaye birikimi", "teknolojik gelişme", "durağan durum", "nüfus artışı", "neoklasik"], "zorluk": "zor", "aciklama": "Uzun dönemli ekonomik büyümenin sermaye, işgücü ve teknolojik ilerleme bileşenlerini formüle etmek."},
    {"kelime": "moral hazard riskini yönetmek", "yasakli_kelimeler": ["ahlaki tehlike", "asimetrik bilgi", "sigortalanınca pervasızlaşma", "kurtarma beklentisi", "risk alma"], "zorluk": "zor", "aciklama": "Kurtarılacağını veya sigortalı olduğunu bilen aktörlerin aşırı risk alma eğilimini engellemek."},
    {"kelime": "tahvil getiri eğrisi tersine dönmek", "yasakli_kelimeler": ["yield curve inversion", "kısa vadeli faiz uzun vadeliyi geçme", "resesyon habercisi", "hazine bonosu", "piyasa paniği"], "zorluk": "zor", "aciklama": "Kısa vadeli tahvil faizlerinin uzun vadeli faizlerin üzerine çıkarak resesyon sinyali vermesi."}
]

add_and_save_verbs('hukuk', hukuk_verbs)
add_and_save_verbs('iktisat', iktisat_verbs)
print('P12 done!')
