import os, sys, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gen_scripts.card_utils import add_and_save_verbs

# 25. immunoloji
immunoloji_verbs = [
    # Kolay (12)
    {"kelime": "bağışıklık kazanmak", "yasakli_kelimeler": ["vücut", "savunma", "hastalık", "güçlenmek", "mikrop"], "zorluk": "kolay", "aciklama": "Vücudun mikroplara karşı dirençli ve korunaklı hale gelmesi."},
    {"kelime": "aşı yaptırmak", "yasakli_kelimeler": ["iğne", "korunma", "doktor", "kol", "hastalanmamak"], "zorluk": "kolay", "aciklama": "Bağışıklık sistemini mikroba karşı önceden eğitmek için aşı olmak."},
    {"kelime": "hastalanmak", "yasakli_kelimeler": ["ateş", "yatak", "virüs", "grip", "zayıf düşmek"], "zorluk": "kolay", "aciklama": "Vücut direncinin kırılmasıyla sağlığın bozulması."},
    {"kelime": "vitamin almak", "yasakli_kelimeler": ["c vitamini", "takviye", "bağışıklık", "meyve", "hap"], "zorluk": "kolay", "aciklama": "Vücut direncini desteklemek için vitamin takviyesi kullanmak."},
    {"kelime": "mikrop kapmak", "yasakli_kelimeler": ["bakteri", "enfeksiyon", "bulaşmak", "yara", "kirli"], "zorluk": "kolay", "aciklama": "Vücuda hastalık yapıcı zararlı organizmaların girmesi."},
    {"kelime": "hapşırmak", "yasakli_kelimeler": ["burun", "alerji", "toz", "çok yaşa", "refleks"], "zorluk": "kolay", "aciklama": "Solunum yolundaki yabancı maddeleri aniden dışarı fırlatmak."},
    {"kelime": "alerji olmak", "yasakli_kelimeler": ["kaşıntı", "kızarıklık", "polen", "toz", "kabarmak"], "zorluk": "kolay", "aciklama": "Zararsız bir maddeye karşı vücudun aşırı tepki vermesi."},
    {"kelime": "şişlik oluşmak", "yasakli_kelimeler": ["ödem", "şişmek", "iltihap", "yara", "darbe"], "zorluk": "kolay", "aciklama": "Dokuda sıvı ve savunma hücrelerinin birikmesiyle kabarıklık meydana gelmesi."},
    {"kelime": "yara kabuk bağlamak", "yasakli_kelimeler": ["iyileşmek", "kan", "deri", "doku", "kapanmak"], "zorluk": "kolay", "aciklama": "Deri hasarının savunma ve pıhtılaşma mekanizmalarıyla onarılması."},
    {"kelime": "ateşi çıkmak", "yasakli_kelimeler": ["sıcaklık", "derece", "hastalık", "yanmak", "savunma"], "zorluk": "kolay", "aciklama": "Vücudun mikroplarla savaşmak için ısısını yükseltmesi."},
    {"kelime": "boğazı şişmek", "yasakli_kelimeler": ["bademcik", "yutkunmak", "iltihap", "ağrı", "lenf"], "zorluk": "kolay", "aciklama": "Boğazdaki lenf dokularının mikropla savaşırken büyümesi."},
    {"kelime": "dinlenmek", "yasakli_kelimeler": ["uyku", "yatak", "vücut toparlanması", "enerji", "iyileşme"], "zorluk": "kolay", "aciklama": "Bağışıklık sisteminin yenilenmesi için uyuyup istirahat etmek."},

    # Orta (24)
    {"kelime": "antikor üretmek", "yasakli_kelimeler": ["plazma hücresi", "savunma proteini", "bağışıklık", "virüs nötralizasyonu", "serum"], "zorluk": "orta", "aciklama": "Yabancı antijenleri etkisiz kılmak için özel protein molekülleri salgılamak."},
    {"kelime": "fagositoz yapmak", "yasakli_kelimeler": ["yutmak", "makrofaj", "mikrop sindirme", "hücresel savunma", "lizozom"], "zorluk": "orta", "aciklama": "Savunma hücrelerinin mikropları içine alarak sindirip yok etmesi."},
    {"kelime": "antijen tanımak", "yasakli_kelimeler": ["yabancı madde", "reseptör", "bağlanma", "t hücresi", "b hücresi"], "zorluk": "orta", "aciklama": "Savunma hücrelerinin vücuda giren yabancı molekülü ayırt etmesi."},
    {"kelime": "lenf bezleri şişmek", "yasakli_kelimeler": ["boyun", "iltihap", "lenfosit çoğalması", "düğüm", "savunma"], "zorluk": "orta", "aciklama": "Enfeksiyon esnasında lenf düğümlerinde hücre üretiminin artmasıyla büyüme olması."},
    {"kelime": "histamin salgılamak", "yasakli_kelimeler": ["mast hücresi", "alerjik tepki", "kılcal damar genişlemesi", "kaşıntı", "ödem"], "zorluk": "orta", "aciklama": "Alerji ve iltihap anında dokuya yangı başlatıcı kimyasal salmak."},
    {"kelime": "sitokin fırtınası yaşamak", "yasakli_kelimeler": ["aşırı bağışıklık yanıtı", "organ hasarı", "covid", "yangı", "iltihap krizi"], "zorluk": "orta", "aciklama": "Bağışıklık sisteminin kontrolsüz biçimde aşırı sitokin salgılayarak vücuda zarar vermesi."},
    {"kelime": "otoimmün reaksiyon vermek", "yasakli_kelimeler": ["kendi dokusuna saldırma", "öz savunma hatası", "lupus", "ms", "hastalık"], "zorluk": "orta", "aciklama": "Bağışıklık sisteminin kendi sağlıklı organ ve dokularını düşman bilip saldırması."},
    {"kelime": "t hücresi olgunlaşmak", "yasakli_kelimeler": ["timus bezi", "lenfosit", "eğitim", "bağışıklık", "hücresel yanıt"], "zorluk": "orta", "aciklama": "T lenfositlerinin timus bezinde antijen tanıma yeteneği kazanması."},
    {"kelime": "b hücresi aktive olmak", "yasakli_kelimeler": ["antikor fabrikası", "kemik iliği", "plazmosit", "bağlanma", "humoral"], "zorluk": "orta", "aciklama": "B lenfositinin antijenle karşılaşıp antikor üretecek forma dönüşmesi."},
    {"kelime": "doğal bağışıklık sergilemek", "yasakli_kelimeler": ["doğuştan gelen", "özgül olmayan", "bariyer", "fagosit", "hızlı yanıt"], "zorluk": "orta", "aciklama": "Vücudun tüm mikroplara karşı doğuştan sahip olduğu ilk savunma hattını devreye sokması."},
    {"kelime": "kazanılmış bağışıklık geliştirmek", "yasakli_kelimeler": ["adaptif", "hafıza hücresi", "özgül yanıt", "zamanla oluşan", "antikor"], "zorluk": "orta", "aciklama": "Geçirilen hastalık veya aşı sonrasında hedefe özel hücresel hafıza kurmak."},
    {"kelime": "iltihaplanma başlatmak", "yasakli_kelimeler": ["enflamasyon", "kızarıklık ısı artışı", "damar geçirgenliği", "ödem", "savunma"], "zorluk": "orta", "aciklama": "Hasarlı bölgeye savunma hücrelerini toplamak için yangı tepkisi başlatmak."},
    {"kelime": "kompleman sistemini aktive etmek", "yasakli_kelimeler": ["protein zinciri", "zar delme kompleksi", "opsonizasyon", "kaskad", "bakteri zarı"], "zorluk": "orta", "aciklama": "Plazmadaki proteinlerin art arda tetiklenerek bakteri zarını delmesi."},
    {"kelime": "hafıza hücresi oluşturmak", "yasakli_kelimeler": ["bellek lenfositi", "ikinci karşılaşma", "hızlı yanıt", "yıllarca yaşama", "bağışıklık"], "zorluk": "orta", "aciklama": "Mikrobun bilgisini saklayıp sonraki enfeksiyonda anında tepki verecek hücreler üretmek."},
    {"kelime": "serolojik test yapmak", "yasakli_kelimeler": ["antikor tespiti", "elisa", "kan serumu", "bağışıklık düzeyi", "titre"], "zorluk": "orta", "aciklama": "Kandaki spesifik antikor miktarını laboratuvarda ölçmek."},
    {"kelime": "anafilaksi geçirmek", "yasakli_kelimeler": ["şok", "soluk borusu tıkanması", "adrenalin iğnesi", "şiddetli alerji", "tansiyon düşmesi"], "zorluk": "orta", "aciklama": "Alerjen maddeye karşı hayatı tehdit eden ani ve şiddetli sistemik reaksiyon yaşamak."},
    {"kelime": "bağışıklık baskılayıcı kullanmak", "yasakli_kelimeler": ["immünsüpresif", "organ nakli", "kortizon", "doku reddi engelleme", "ilaç"], "zorluk": "orta", "aciklama": "Organ reddini önlemek için bağışıklık sistemini ilaçla zayıflatmak."},
    {"kelime": "doku reddi yaşamak", "yasakli_kelimeler": ["organ nakli", "mhc uyumsuzluğu", "yabancı organ", "bağışıklık saldırısı", "greft"], "zorluk": "orta", "aciklama": "Bağışıklık sisteminin nakledilen organı yabancı kabul edip tahrip etmesi."},
    {"kelime": "deri prick testi yaptırmak", "yasakli_kelimeler": ["alerji testi", "çizik", "kızarıklık çapı", "alerjen damlatma", "kol"], "zorluk": "orta", "aciklama": "Kola damlatılan alerjenlerle ciltte kabarma oluşup oluşmadığını denetlemek."},
    {"kelime": "makrofajları bölgeye çağırmak", "yasakli_kelimeler": ["kemotaksis", "kimyasal çekim", "göç", "dokuda devriye", "yutucu hücre"], "zorluk": "orta", "aciklama": "Enfeksiyon bölgesinden salınan kimyasallarla yutucu hücreleri olay yerine çekmek."},
    {"kelime": "doğal katil hücreleri salmak", "yasakli_kelimeler": ["nk hücresi", "kanserli hücre imhası", "virüslü hücre", "perforin", "sitotoksik"], "zorluk": "orta", "aciklama": "Tümör ve virüsle enfekte hücreleri tespit edip doğrudan imha etmek."},
    {"kelime": "opsonizasyon gerçekleştirmek", "yasakli_kelimeler": ["antikorla işaretleme", "kolay yutulma", "fagositoz kolaylaştırma", "bakteri kaplama", "etiketleme"], "zorluk": "orta", "aciklama": "Mikrobun etrafını antikorla kaplayarak makrofajların onu kolayca yutmasını sağlamak."},
    {"kelime": "kan grubu uyuşmazlığını saptamak", "yasakli_kelimeler": ["aglütinasyon", "çökelme", "rh uygunsuzluğu", "eritrosit", "kan nakli"], "zorluk": "orta", "aciklama": "Yanlış kan verildiğinde antikorların eritrositleri çöktürdüğünü görmek."},
    {"kelime": "mukozal bariyeri korumak", "yasakli_kelimeler": ["iga antikoru", "bağırsak zarı", "solunum yolu", "fiziksel engel", "koruma"], "zorluk": "orta", "aciklama": "Ağız, burun ve bağırsak yüzeyindeki koruyucu sıvı tabakasını güçlü tutmak."},

    # Zor (14)
    {"kelime": "mHC molekülü ile sunum yapmak", "yasakli_kelimeler": ["majör histo-uyumluluk kompleksi", "antijen sunan hücre", "dendritik", "tcr bağlanması", "peptit"], "zorluk": "zor", "aciklama": "İşlenen antijen peptitlerini hücre yüzeyindeki MHC oluğuna yerleştirip T hücresine sunmak."},
    {"kelime": "v(D)J rekombinasyonu yapmak", "yasakli_kelimeler": ["somatik çeşitlilik", "rag1 rag2", "antikor çeşitliliği", "gen segmenti birleşimi", "lenfosit"], "zorluk": "zor", "aciklama": "Lenfosit olgunlaşmasında gen parçalarını rastgele birleştirerek sınırsız antikor çeşitliliği üretmek."},
    {"kelime": "klonal seleksiyondan geçmek", "yasakli_kelimeler": ["burnet teorisi", "özgül lenfosit çoğalması", "seçilim", "antijene bağlanan klon", "proliferasyon"], "zorluk": "zor", "aciklama": "Yalnızca giren antijene tam uyan tek bir lenfosit klonunun çoğalarak ordu kurması."},
    {"kelime": "merkezi tolerans geliştirmek", "yasakli_kelimeler": ["negatif seleksiyon", "kendi antijenine saldıranı yok etme", "apoptoz", "timus", "otoimmünite önleme"], "zorluk": "zor", "aciklama": "Timusta vücudun kendi dokusuna tepki veren T hücrelerini programlı ölümle yok etmek."},
    {"kelime": "sitotoksik t lenfosit ile delmek", "yasakli_kelimeler": ["cd8+", "perforin granzim", "hedef hücre apoptozu", "virüslü hücre", "lizis"], "zorluk": "zor", "aciklama": "CD8+ T hücresinin perforin ve granzim salgılayarak enfekte hücreyi delip öldürmesi."},
    {"kelime": "izotip değişimi gerçekleştirmek", "yasakli_kelimeler": ["class switching", "igm den igg ye geçiş", "sabit bölge değişimi", "yardımcı t hücresi", "sitokin"], "zorluk": "zor", "aciklama": "B hücresinin antijen özgüllüğünü koruyarak IgM antikorundan IgG veya IgE üretimine geçmesi."},
    {"kelime": "membran atak kompleksi kurmak", "yasakli_kelimeler": ["mac", "c5b c6 c7 c8 c9", "ozmotik lizis", "bakteri zarı deliği", "kompleman son aşama"], "zorluk": "zor", "aciklama": "Kompleman proteinlerinin bakteri zarı üzerinde gözenek açarak mikrobu patlatması."},
    {"kelime": "somatik hipermutasyon geçirmek", "yasakli_kelimeler": ["germinatif merkez", "afinite olgunlaşması", "yüksek bağlanma gücü", "nokta mutasyonu", "aid enzimi"], "zorluk": "zor", "aciklama": "B hücrelerinin antikor bağlama bölgesinde nokta mutasyonları geçirerek antijene tutunma gücünü artırması."},
    {"kelime": "düzenleyici t hücresi ile baskılamak", "yasakli_kelimeler": ["treg", "foxp3", "immün yanıtı sonlandırma", "tolerans", "aşırı yangıyı önleme"], "zorluk": "zor", "aciklama": "Foxp3+ Treg hücreleriyle savaş bittikten sonra bağışıklık tepkisini susturup dokuyu korumak."},
    {"kelime": "antijen sunan hücreyi olgunlaştırmak", "yasakli_kelimeler": ["dendritik hücre", "toll-like reseptör", "kostimülatör b7", "cd28", "lenf noduna göç"], "zorluk": "zor", "aciklama": "Dendritik hücrenin mikrobu alıp lenf düğümüne giderek naif T hücrelerini uyarması."},
    {"kelime": "immün kontrol noktası inhibitörü vermek", "yasakli_kelimeler": ["pd-1", "ctla-4", "kanser immünoterapisi", "frenleri kaldırma", "t hücresi aktivasyonu"], "zorluk": "zor", "aciklama": "Kanser hücrelerinin bağışıklığı frenleyen mekanizmasını antikor ilaçlarla devre dışı bırakmak."},
    {"kelime": "toll benzeri reseptörle bağlanmak", "yasakli_kelimeler": ["tlr", "pamp tanıma", "doğal bağışıklık sinyali", "nf-kb aktivasyonu", "lipopolisakkarit"], "zorluk": "zor", "aciklama": "Patojenlerin korunmuş ortak moleküler yapılarını hücre yüzeyindeki TLR reseptörleriyle saptamak."},
    {"kelime": "kemokin gradyanını takip etmek", "yasakli_kelimeler": ["lökosit ekstravazasyonu", "endotelden geçiş", "diapedez", "selektin integrin", "iltihap odağı"], "zorluk": "zor", "aciklama": "Akyuvarların kan damarından dokuya geçip yoğunluk farkına göre iltihap odağına sızması."},
    {"kelime": "çapraz sunum gerçekleştirmek", "yasakli_kelimeler": ["cross-presentation", "ekstrasellüler antijen", "mhc sınıf 1 e yükleme", "cd8 t hücresi uyarımı", "dendritik hücre"], "zorluk": "zor", "aciklama": "Hücre dışından alınan yabancı antijenin istisnai olarak MHC-I molekülüne yüklenip sunulması."}
]

# 26. internethayati
internethayati_verbs = [
    # Kolay (12)
    {"kelime": "internete bağlanmak", "yasakli_kelimeler": ["wifi", "ağ", "çevrimiçi", "şifre", "modem"], "zorluk": "kolay", "aciklama": "Cihazı kablosuz veya kablolu ağ üzerinden internete eriştirmek."},
    {"kelime": "arama yapmak", "yasakli_kelimeler": ["google", "motor", "yazmak", "bulmak", "kelime"], "zorluk": "kolay", "aciklama": "Arama motoruna kelime girerek web sitelerini listelemek."},
    {"kelime": "mesaj göndermek", "yasakli_kelimeler": ["whatsapp", "sohbet", "yazmak", "chat", "arkadaş"], "zorluk": "kolay", "aciklama": "Çevrimiçi sohbet uygulamasıyla metin iletmek."},
    {"kelime": "video izlemek", "yasakli_kelimeler": ["youtube", "oynatmak", "ekran", "izleme", "klip"], "zorluk": "kolay", "aciklama": "İnternet üzerindeki video platformlarından içerik seyretmek."},
    {"kelime": "dosya indirmek", "yasakli_kelimeler": ["download", "bilgisayar", "yüklemek", "kaydetmek", "link"], "zorluk": "kolay", "aciklama": "İnternetteki bir belge veya programı cihaza kaydetmek."},
    {"kelime": "e-posta yollamak", "yasakli_kelimeler": ["mail", "gmail", "adres", "gönder", "ileti"], "zorluk": "kolay", "aciklama": "Elektronik posta kutusundan dijital mektup göndermek."},
    {"kelime": "şifre belirlemek", "yasakli_kelimeler": ["parola", "güvenlik", "giriş", "harf sayı", "hesap"], "zorluk": "kolay", "aciklama": "İnternet hesabına giriş için gizli parola oluşturmak."},
    {"kelime": "fotoğraf yüklemek", "yasakli_kelimeler": ["paylaşmak", "upload", "galeri", "resim", "profil"], "zorluk": "kolay", "aciklama": "Cihazdaki görseli internet sitesine veya profile aktarmak."},
    {"kelime": "beğeni butonuna basmak", "yasakli_kelimeler": ["like", "kalp", "tıklamak", "post", "sosyal medya"], "zorluk": "kolay", "aciklama": "Paylaşılan içeriği beğendiğini göstermek için butona dokunmak."},
    {"kelime": "sayfayı yenilemek", "yasakli_kelimeler": ["refresh", "f5", "güncellemek", "tarayıcı", "yeniden yükleme"], "zorluk": "kolay", "aciklama": "Web sayfasının en güncel halini ekrana tekrar çağırmak."},
    {"kelime": "bağlantıya tıklamak", "yasakli_kelimeler": ["link", "url", "fare", "siteye gitmek", "mavi yazı"], "zorluk": "kolay", "aciklama": "Metindeki köprüye dokunarak hedef web sayfasına gitmek."},
    {"kelime": "online alışveriş yapmak", "yasakli_kelimeler": ["sepet", "kredi kartı", "sipariş", "kargo", "satın almak"], "zorluk": "kolay", "aciklama": "İnternet sitelerinden ürün beğenip sipariş vermek."},

    # Orta (24)
    {"kelime": "canlı yayın açmak", "yasakli_kelimeler": ["stream", "takipçi", "kamera", "twitch", "izleyici"], "zorluk": "orta", "aciklama": "İnternet üzerinden anlık görüntülü yayın gerçekleştirmek."},
    {"kelime": "tarayıcı geçmişini silmek", "yasakli_kelimeler": ["chrome", "çerezler", "gizlilik", "temizleme", "ziyaret edilen siteler"], "zorluk": "orta", "aciklama": "Girilen internet sitelerinin bıraktığı izleri tarayıcıdan temizlemek."},
    {"kelime": "vPN kullanmak", "yasakli_kelimeler": ["sanal özel ağ", "ip gizleme", "yasaklı site", "konum değiştirme", "şifreli bağlantı"], "zorluk": "orta", "aciklama": "İnternet trafiğini başka bir ülke sunucusu üzerinden şifreleyerek aktarmak."},
    {"kelime": "modemi yeniden başlatmak", "yasakli_kelimeler": ["reset", "kapatıp açmak", "internet yavaşlığı", "ışıklar", "bağlantı kopması"], "zorluk": "orta", "aciklama": "İnternet kesintisini gidermek için yönlendirici cihazın fişini çekip takmak."},
    {"kelime": "buluta yedeklemek", "yasakli_kelimeler": ["cloud", "drive", "saklama", "senkronizasyon", "depolama"], "zorluk": "orta", "aciklama": "Önemli dosyaları internetteki güvenli sunucularda depolamak."},
    {"kelime": "iki adımlı doğrulama kurmak", "yasakli_kelimeler": ["2fa", "sms kodu", "güvenlik", "authenticator", "ekstra koruma"], "zorluk": "orta", "aciklama": "Hesap güvenliği için şifreye ek olarak telefona gelen onay kodunu zorunlu kılmak."},
    {"kelime": "reklam engelleyici kurmak", "yasakli_kelimeler": ["adblock", "pop-up", "tarayıcı eklentisi", "kapatma", "banner"], "zorluk": "orta", "aciklama": "Web sitelerindeki rahatsız edici reklamları gizleyen eklenti yüklemek."},
    {"kelime": "çerezleri kabul etmek", "yasakli_kelimeler": ["cookie", "kvkk", "onay", "site ayarları", "pop-up bildirim"], "zorluk": "orta", "aciklama": "Web sitesinin tarayıcıya küçük veri dosyaları kaydetmesine izin vermek."},
    {"kelime": "takipçi kasmak", "yasakli_kelimeler": ["hesap büyütme", "beğeni", "etkileşim", "abone", "sosyal medya"], "zorluk": "orta", "aciklama": "Sosyal medya profilindeki takipçi sayısını artırmak için uğraşmak."},
    {"kelime": "hesabı dondurmak", "yasakli_kelimeler": ["geçici kapatma", "mola", "profil", "askıya alma", "çıkış"], "zorluk": "orta", "aciklama": "Sosyal medya hesabını silmeden geçici olarak erişime kapatmak."},
    {"kelime": "ekran görüntüsü almak", "yasakli_kelimeler": ["screenshot", "ss", "yakalamak", "kayıt", "resim çekme"], "zorluk": "orta", "aciklama": "O an ekranda görünen görüntüyü resim dosyası olarak kaydetmek."},
    {"kelime": "spam kutusunu kontrol etmek", "yasakli_kelimeler": ["önemsiz posta", "filtre", "kayıp mail", "doğrulama linki", "istenmeyen"], "zorluk": "orta", "aciklama": "Gelmesi beklenen e-postanın filtreye takılıp takılmadığına bakmak."},
    {"kelime": "influencer olmak", "yasakli_kelimeler": ["içerik üreticisi", "iş birliği", "tanıtım", "marka", "takipçi kitlesi"], "zorluk": "orta", "aciklama": "Sosyal medyada yüksek kitleye ulaşıp ürün ve yaşam tarzı tanıtmak."},
    {"kelime": "trend topic olmak", "yasakli_kelimeler": ["tt", "gündem", "hashtag", "twitter", "en çok konuşulan"], "zorluk": "orta", "aciklama": "Bir konunun veya etiketin internette en çok konuşulanlar listesine girmesi."},
    {"kelime": "gizli sekme açmak", "yasakli_kelimeler": ["incognito", "geçmiş tutmama", "özel pencere", "çerezsiz", "tarayıcı"], "zorluk": "orta", "aciklama": "Geçmişi ve form bilgilerini kaydetmeyen geçici tarayıcı sayfası başlatmak."},
    {"kelime": "link kısaltmak", "yasakli_kelimeler": ["bitly", "uzun url", "küçültme", "tıklama takibi", "paylaşım"], "zorluk": "orta", "aciklama": "Uzun web adresini birkaç karakterlik kısa bağlantıya dönüştürmek."},
    {"kelime": "podcast dinlemek", "yasakli_kelimeler": ["ses kaydı", "spotify", "bölüm", "kulaklık", "söyleşi"], "zorluk": "orta", "aciklama": "İnternette yayınlanan tematik sesli sohbet programlarını dinlemek."},
    {"kelime": "hız testi yapmak", "yasakli_kelimeler": ["speedtest", "mbps", "ping", "download upload", "ölçüm"], "zorluk": "orta", "aciklama": "İnternet bağlantısının indirme ve yükleme süratini ölçmek."},
    {"kelime": "bildirimleri kapatmak", "yasakli_kelimeler": ["sessize alma", "rahatsız etmeyin", "uyarı", "odaklanma", "mesaj sesi"], "zorluk": "orta", "aciklama": "Cihaza gelen uygulama ve site uyarı mesajlarını durdurmak."},
    {"kelime": "profil fotoğrafı güncellemek", "yasakli_kelimeler": ["avatar", "yeni resim", "değiştirme", "yükleme", "hesap"], "zorluk": "orta", "aciklama": "Sosyal ağdaki ana tanıtıcı görseli yenisiyle değiştirmek."},
    {"kelime": "trollere aldırmamak", "yasakli_kelimeler": ["kışkırtıcı yorum", "kavga çıkarma", "görmezden gelme", "cevap vermeme", "bloklama"], "zorluk": "orta", "aciklama": "İnternette insanları bilerek kışkırtan hesaplara prim vermemek."},
    {"kelime": "çevrimdışı moda almak", "yasakli_kelimeler": ["uçak modu", "internetsiz", "bağlantı kesme", "offline", "erişilemez"], "zorluk": "orta", "aciklama": "Cihazın tüm internet ve ağ iletişimini geçici olarak kapatmak."},
    {"kelime": "yorum sabitlemek", "yasakli_kelimeler": ["pinlemek", "en üstte tutma", "post sahibi", "öne çıkarma", "başlık"], "zorluk": "orta", "aciklama": "Paylaşımın altına gelen önemli bir yorumu en üst sıraya tutturmak."},
    {"kelime": "çevrimiçi toplantıya katılmak", "yasakli_kelimeler": ["zoom", "teams", "kamera mikrofon", "uzaktan çalışma", "görüşme"], "zorluk": "orta", "aciklama": "İnternet üzerinden görüntülü ve sesli iş toplantısında bulunmak."},

    # Zor (14)
    {"kelime": "dNS ayarlarını değiştirmek", "yasakli_kelimeler": ["alan adı sunucusu", "1.1.1.1 8.8.8.8", "ip çözümleme", "erişim engeli", "ağ bağdaştırıcısı"], "zorluk": "zor", "aciklama": "Web adreslerini IP'ye çeviren sunucu adreslerini manuel olarak güncellemek."},
    {"kelime": "dDoS saldırısı savuşturmak", "yasakli_kelimeler": ["dağıtık hizmet engelleme", "cloudflare", "aşırı trafik yükü", "botnet", "sunucu çökmesi"], "zorluk": "zor", "aciklama": "Sunucuya yönlendirilen yapay trafik selini güvenlik duvarıyla filtrelemek."},
    {"kelime": "tor ağına bağlanmak", "yasakli_kelimeler": ["dark web", "onion yönlendirme", "anonimlik", "katmanlı şifreleme", "özel tarayıcı"], "zorluk": "zor", "aciklama": "İnternet trafiğini dünya genelindeki gönüllü düğümlerden kat kat şifreleyerek geçirmek."},
    {"kelime": "statik iP tahsis etmek", "yasakli_kelimeler": ["sabit adres", "dinamik olmayan", "port açma", "sunucu barındırma", "iss"], "zorluk": "zor", "aciklama": "İnternet servis sağlayıcıdan değişmeyen sabit bir internet protokol adresi almak."},
    {"kelime": "sSL sertifikası yüklemek", "yasakli_kelimeler": ["https", "yeşil kilit", "tls şifreleme", "güvenli bağlantı", "let's encrypt"], "zorluk": "zor", "aciklama": "Web sitesi ile kullanıcı arasındaki veri transferini şifreleyen güvenlik sertifikası kurmak."},
    {"kelime": "phishing tuzağını deşifre etmek", "yasakli_kelimeler": ["oltalama", "sahte web sitesi", "şifre çalma", "dolandırıcılık", "benzer url"], "zorluk": "zor", "aciklama": "Banka veya resmi kurumu taklit eden sahte e-posta ve web arayüzlerini yakalamak."},
    {"kelime": "port yönlendirmesi yapmak", "yasakli_kelimeler": ["port forwarding", "modem arayüzü", "yerel ip", "tcp udp", "sunucu dışa açma"], "zorluk": "zor", "aciklama": "Dışarıdan gelen belirli port isteklerini yerel ağdaki spesifik cihaza aktarmak."},
    {"kelime": "dijital ayak izini silmek", "yasakli_kelimeler": ["unutulma hakkı", "veri tabanları", "eski kayıtlar", "gizlilik", "izleri temizleme"], "zorluk": "zor", "aciklama": "Yıllar boyunca internet sitelerinde ve veri tabanlarında bırakılan kişisel bilgileri sildirmek."},
    {"kelime": "algoritmik yankı odasından çıkmak", "yasakli_kelimeler": ["echo chamber", "filtre balonu", "aynı fikirler", "kişiselleştirilmiş besleme", "tarafsızlık"], "zorluk": "zor", "aciklama": "Kişiyi sadece kendi görüşündeki içeriklerle çevreleyen platform algoritmasını kırmak."},
    {"kelime": "traceroute ile paket izlemek", "yasakli_kelimeler": ["ağ gecikmesi", "atlama noktaları", "hop sayısı", "ping kaybı", "yönlendirici yolu"], "zorluk": "zor", "aciklama": "Bilgi paketinin hedef sunucuya ulaşana kadar hangi router düğümlerinden geçtiğini izlemek."},
    {"kelime": "p2P dosya paylaşmak", "yasakli_kelimeler": ["torrent", "peer to peer", "seeder leecher", "merkezi sunucusuz", "parça indirme"], "zorluk": "zor", "aciklama": "Dosyaları merkezi sunucu olmadan doğrudan kullanıcıların kendi cihazları arasında aktarmak."},
    {"kelime": "uRL injection açığını kapatmak", "yasakli_kelimeler": ["web güvenliği", "kod enjeksiyonu", "parametre filtreleme", "siber güvenlik", "istismar"], "zorluk": "zor", "aciklama": "Web adres çubuğundaki parametrelerden kaynaklanan zararlı kod çalıştırma açıklarını yamamak."},
    {"kelime": "firewall kuralları yazmak", "yasakli_kelimeler": ["güvenlik duvarı", "gelen giden trafik", "ip engelleme", "paket filtreleme", "kural listesi"], "zorluk": "zor", "aciklama": "Ağa giren ve çıkan veri paketlerini denetleyecek güvenlik kurallarını tanımlamak."},
    {"kelime": "uçtan uca şifrelemeyi doğrulamak", "yasakli_kelimeler": ["end-to-end", "güvenlik anahtarı", "üçüncü şahıs okuyamaz", "sinyal protokolü", "qr kod eşleşmesi"], "zorluk": "zor", "aciklama": "Mesajlaşmada şifre çözme anahtarının yalnızca gönderici ve alıcıda olduğunu doğrulamak."}
]

add_and_save_verbs('immunoloji', immunoloji_verbs)
add_and_save_verbs('internethayati', internethayati_verbs)
print('P13 done!')
