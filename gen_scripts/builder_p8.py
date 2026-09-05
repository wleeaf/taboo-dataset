import os, sys, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gen_scripts.card_utils import add_and_save_verbs

# 15. filateli
filateli_verbs = [
    # Kolay (12)
    {"kelime": "pul yapıştırmak", "yasakli_kelimeler": ["zarf", "mektup", "posta", "yalamak", "göndermek"], "zorluk": "kolay", "aciklama": "Posta ücretini ödemek için zarfın köşesine pul tutturmak."},
    {"kelime": "mektup göndermek", "yasakli_kelimeler": ["zarf", "posta kutusu", "adres", "haberleşme", "yazmak"], "zorluk": "kolay", "aciklama": "Yazılan mektubu postaya vermek."},
    {"kelime": "pul koleksiyonu yapmak", "yasakli_kelimeler": ["biriktirmek", "albüm", "hobi", "çeşit", "filatelist"], "zorluk": "kolay", "aciklama": "Farklı dönem ve ülkelere ait pulları düzenli olarak biriktirmek."},
    {"kelime": "zarf açmak", "yasakli_kelimeler": ["mektup", "yırtmak", "kağıt", "posta", "içinden"], "zorluk": "kolay", "aciklama": "Gelen postayı okumak için zarfın kapağını açmak."},
    {"kelime": "büyüteçle bakmak", "yasakli_kelimeler": ["mercek", "büyütmek", "detay", "incelemek", "küçük"], "zorluk": "kolay", "aciklama": "Pulun üzerindeki ince ayrıntıları büyüteç yardımıyla görmek."},
    {"kelime": "damga basmak", "yasakli_kelimeler": ["mühür", "tarih", "postane", "mürekkep", "iptal"], "zorluk": "kolay", "aciklama": "Pulun tekrar kullanılmaması için üzerine mürekkepli tarih mühürü vurmak."},
    {"kelime": "albüme yerleştirmek", "yasakli_kelimeler": ["defter", "şeffaf cep", "koleksiyon", "dizmek", "sayfa"], "zorluk": "kolay", "aciklama": "Yeni edinilen pulu koleksiyon albümünün yuvasına koymak."},
    {"kelime": "pul satın almak", "yasakli_kelimeler": ["ptt", "postane", "ücret", "para", "hediyelik"], "zorluk": "kolay", "aciklama": "Postaneden veya satıcıdan pul temin etmek."},
    {"kelime": "pul takas etmek", "yasakli_kelimeler": ["değiş tokuş", "koleksiyoncu", "vermek", "almak", "eksik"], "zorluk": "kolay", "aciklama": "Koleksiyondaki fazla pulları diğer koleksiyonerlerle değiştirmek."},
    {"kelime": "zarfı yalamak", "yasakli_kelimeler": ["tükürük", "yapışkan", "kapatmak", "ıslatmak", "dil"], "zorluk": "kolay", "aciklama": "Zarfın tutkallı kısmını ıslatarak kapağı kapatmak."},
    {"kelime": "postaneye gitmek", "yasakli_kelimeler": ["ptt", "gişe", "gönderi", "koli", "sıra"], "zorluk": "kolay", "aciklama": "Posta işlemleri için resmi şubeye uğramak."},
    {"kelime": "pul hediye etmek", "yasakli_kelimeler": ["vermek", "arkadaş", "koleksiyon", "albüm", "sürpriz"], "zorluk": "kolay", "aciklama": "Bir başka meraklıya pul armağan etmek."},

    # Orta (24)
    {"kelime": "cımbızla tutmak", "yasakli_kelimeler": ["pens", "parmak izi", "pul maşası", "zarar vermeme", "koleksiyon"], "zorluk": "orta", "aciklama": "Pula el sürmeden özel filateli maşasıyla temas etmek."},
    {"kelime": "dantel ölçmek", "yasakli_kelimeler": ["perforasyon", "diş", "odontometre", "sayı", "kenar"], "zorluk": "orta", "aciklama": "Pulun kenar dişlerinin sıklığını özel cetvelle ölçmek."},
    {"kelime": "damgalı pul ayırmak", "yasakli_kelimeler": ["kullanılmış", "mühürlü", "temiz", "damgasız", "tasnif"], "zorluk": "orta", "aciklama": "Mühür görmüş pulları kullanılmamışlardan ayırt etmek."},
    {"kelime": "ilk gün zarfı saklamak", "yasakli_kelimeler": ["fdc", "özel damga", "emisyon", "tarih", "koleksiyon"], "zorluk": "orta", "aciklama": "Pulun çıktığı ilk gün basılan özel mühürlü zarfı arşivlemek."},
    {"kelime": "pul kataloğu taramak", "yasakli_kelimeler": ["michel", "scott", "ysequence", "fiyat", "numara"], "zorluk": "orta", "aciklama": "Pulun değerini ve basım yılını uluslararası katalogdan bulmak."},
    {"kelime": "havala kağıdı kullanmak", "yasakli_kelimeler": ["kuşe", "montaj", "şeffaf bant", "fildişi", "albüm"], "zorluk": "orta", "aciklama": "Pulu albüm sayfasına hasarsız sabitlemek için şeffaf cep kullanmak."},
    {"kelime": "baskı hatası aramak", "yasakli_kelimeler": ["varyete", "renk kayması", "değerli", "kusur", "nadir"], "zorluk": "orta", "aciklama": "Matbaa basımı sırasında meydana gelen nadir hataları tespit etmek."},
    {"kelime": "tematik koleksiyon yapmak", "yasakli_kelimeler": ["konu", "kuşlar", "uzay", "çiçek", "olimpiyat"], "zorluk": "orta", "aciklama": "Yalnızca belirli bir temaya ait pulları bir araya getirmek."},
    {"kelime": "filigran kontrolü yapmak", "yasakli_kelimeler": ["filigranskop", "kağıt içi desen", "ışık", "benzin", "güvenlik"], "zorluk": "orta", "aciklama": "Kağıdın hamurundaki gizli güvenlik işaretini sıvı veya ışıkla görmek."},
    {"kelime": "antiyeli kart toplamak", "yasakli_kelimeler": ["baskılı pul", "kartpostal", "posta kartı", "resmi", "değer"], "zorluk": "orta", "aciklama": "Üzerinde matbaa basımı pul bulunan resmi kartpostalları derlemek."},
    {"kelime": "damgasız pul saklamak", "yasakli_kelimeler": ["darphane hali", "mint", "orijinal zamk", "kullanılmamış", "kusursuz"], "zorluk": "orta", "aciklama": "Hiç kullanılmamış, zamkı bozulmamış pulları korumak."},
    {"kelime": "pul müzayedesine katılmak", "yasakli_kelimeler": ["açık artırma", "pey", "nadir parça", "satış", "fiyat"], "zorluk": "orta", "aciklama": "Değerli ve nadir pulların satıldığı açık artırmaya girmek."},
    {"kelime": "emisyon yılını bulmak", "yasakli_kelimeler": ["tedavül", "çıkış", "baskı", "tarih", "dönem"], "zorluk": "orta", "aciklama": "Pulun tedavüle çıktığı resmi yılı tespit etmek."},
    {"kelime": "sürşarj basmak", "yasakli_kelimeler": ["ek yazı", "fiyat değişimi", "matbaa", "yeni değer", "iptal"], "zorluk": "orta", "aciklama": "Mevcut pulun üzerine yeni fiyat veya amaç bildiren ek yazı basmak."},
    {"kelime": "kağıttan pul sökmek", "yasakli_kelimeler": ["ılık su", "banyo", "ayırma", "kurutma", "zamk eritme"], "zorluk": "orta", "aciklama": "Zarfın üzerindeki kullanılmış pulu ılık suda bekleterek kağıttan ayırmak."},
    {"kelime": "kurutma presine koymak", "yasakli_kelimeler": ["kurutma kağıdı", "düzleştirme", "ıslak", "ağırlık", "kırışıklık"], "zorluk": "orta", "aciklama": "Yıkanan ıslak pulları kurutma yaprakları arasında düzleştirmek."},
    {"kelime": "özel gün damgası vurdurmak", "yasakli_kelimeler": ["anma", "yıldönümü", "posta", "hatıra", "şube"], "zorluk": "orta", "aciklama": "Belirli tarihi günler için üretilen özel mühürü zarfa bastırmak."},
    {"kelime": "blok pul biriktirmek", "yasakli_kelimeler": ["dörtlü", "tabaka", "ayrılmamış", "marj", "kenar"], "zorluk": "orta", "aciklama": "Birbirinden koparılmamış dörtlü veya çoklu pul gruplarını toplamak."},
    {"kelime": "nadirliği derecelendirmek", "yasakli_kelimeler": ["kıymet", "popülasyon", "bulunurluk", "derece", "katalog"], "zorluk": "orta", "aciklama": "Pulun piyasada ne kadar az bulunduğunu ve değerini ölçmek."},
    {"kelime": "zamk durumunu incelemek", "yasakli_kelimeler": ["arkası", "orijinal", "yapışkan", "leke", "menteşe izi"], "zorluk": "orta", "aciklama": "Pulun arkasındaki orijinal yapışkan tabakanın durumuna bakmak."},
    {"kelime": "baskı tirajını öğrenmek", "yasakli_kelimeler": ["adet", "sayı", "basım", "kaç tane", "istatistik"], "zorluk": "orta", "aciklama": "O pul serisinden toplam kaç adet basıldığını araştırmak."},
    {"kelime": "marj genişliğini kontrol etmek", "yasakli_kelimeler": ["kenar boşluğu", "dantelsiz", "simetri", "çerçeve", "kağıt"], "zorluk": "orta", "aciklama": "Pul resminin kenar boşluklarına olan simetrisini denetlemek."},
    {"kelime": "seriyi tamamlamak", "yasakli_kelimeler": ["eksik pul", "koleksiyon", "bütün", "tam takım", "set"], "zorluk": "orta", "aciklama": "Bir emisyona ait tüm nominal değerdeki pulları edinip seti bitirmek."},
    {"kelime": "filateli derneğine üye olmak", "yasakli_kelimeler": ["kulüp", "cemiyet", "bülten", "topluluk", "koleksiyoner"], "zorluk": "orta", "aciklama": "Pul koleksiyoncularının kurduğu resmi cemiyete katılmak."},

    # Zor (14)
    {"kelime": "odontometre ile diş saymak", "yasakli_kelimeler": ["perforasyon cetveli", "2 santimetre", "diş adedi", "ölçüm", "hassas"], "zorluk": "zor", "aciklama": "Pul kenarındaki 2 santimetreye düşen diş sayısını hassas ölçekle saymak."},
    {"kelime": "ters filigran tespit etmek", "yasakli_kelimeler": ["hata", "ayna görüntüsü", "güvenlik deseni", "ters baskı", "kıymetli"], "zorluk": "zor", "aciklama": "Kağıttaki filigranın ters veya yan durduğunu belirleyip nadir varyantı bulmak."},
    {"kelime": "tête-bêche çiftini bulmak", "yasakli_kelimeler": ["ters yüz pul", "baş başa", "bitişik", "tabaka hatası", "nadir"], "zorluk": "zor", "aciklama": "Tabakada birbirine göre ters yönde basılmış bitişik pul çiftini yakalamak."},
    {"kelime": "sahte sürşarjı ayırt etmek", "yasakli_kelimeler": ["sahtecilik", "mürekkep testi", "font", "ekspertiz", "taklit"], "zorluk": "zor", "aciklama": "Pula sonradan haksız kazanç için vurulan sahte ek yazıyı mikroskopla saptamak."},
    {"kelime": "gravür tekniğini incelemek", "yasakli_kelimeler": ["çelik kalıp", "intaglio", "oyma", "kabartma mürekkep", "matbaa"], "zorluk": "zor", "aciklama": "Çelik kalıba elle kazınarak yapılan yüksek kaliteli baskı tekniğini incelemek."},
    {"kelime": "saç çizgisi çatlağı yakalamak", "yasakli_kelimeler": ["hairline", "klişe çatlağı", "plaka hatası", "çizgi", "büyüteç"], "zorluk": "zor", "aciklama": "Baskı plakasındaki ince çatlağın pula yansıttığı kılcal çizgiyi keşfetmek."},
    {"kelime": "fantezi damgayı belgelemek", "yasakli_kelimeler": ["özel şekilli", "tren", "gemi", "posta tarihi", "nadir mühür"], "zorluk": "zor", "aciklama": "Demiryolu veya gemi postalarında kullanılan sıra dışı mühür izlerini arşivlemek."},
    {"kelime": "orijinal zamk testi yapmak", "yasakli_kelimeler": ["regummed", "sahte zamk", "morötesi", "parlaklık", "orijinallik"], "zorluk": "zor", "aciklama": "Pulun arkasındaki yapışkanın fabrikasyon mu yoksa sonradan mı sürüldüğünü test etmek."},
    {"kelime": "ekspertiz sertifikası çıkartmak", "yasakli_kelimeler": ["filatelik bilirkişi", "orijinallik belgesi", "onay", "mühür", "uzman raporu"], "zorluk": "zor", "aciklama": "Çok değerli bir pulun orijinalliğini yetkili filateli eksperine onaylatmak."},
    {"kelime": "posta tarihi araştırması yapmak", "yasakli_kelimeler": ["posta güzergahı", "posta tarifesi", "sansür damgası", "eski mektup", "tarihsel belge"], "zorluk": "zor", "aciklama": "Zarf üzerindeki damga, pul ve mühürlerden hareketle posta rotasını ve dönem tarifesini kanıtlamak."},
    {"kelime": "guilloché desenini incelemek", "yasakli_kelimeler": ["karmaşık geometri", "sahtecilik önleme", "çizgiler", "motor deseni", "kalıp"], "zorluk": "zor", "aciklama": "Pul arka planındaki sahteciliği önleyen karmaşık geometrik eğrileri tetkik etmek."},
    {"kelime": "baskı klişesini yeniden kurmak", "yasakli_kelimeler": ["plakalandırma", "plater", "tabakadaki konum", "varyete eşleme", "rekonstrüksiyon"], "zorluk": "zor", "aciklama": "Münferit pulların hatalarından yola çıkarak tüm tabakanın dizilim şemasını çıkarmak."},
    {"kelime": "aerofilatelik belge toplamak", "yasakli_kelimeler": ["uçak postası", "zeplin mektubu", "hava yolu", "özel sürşarj", "ilk uçuş"], "zorluk": "zor", "aciklama": "İlk uçak ve zeplin seferleriyle taşınmış özel damgalı havacılık postalarını derlemek."},
    {"kelime": "dantelsiz kenar payı ölçmek", "yasakli_kelimeler": ["imperforate", "makas payı", "dört kenar genişliği", "milimetre", "nadir baskı"], "zorluk": "zor", "aciklama": "Dişsiz basılmış klasik pullarda komşu pul izi içermeyen kenar payını milimetrik ölçmek."}
]

# 16. fotografcilik
fotografcilik_verbs = [
    # Kolay (12)
    {"kelime": "fotoğraf çekmek", "yasakli_kelimeler": ["kamera", "poz", "resim", "basmak", "makine"], "zorluk": "kolay", "aciklama": "Kamera ile bir anın görüntüsünü kaydetmek."},
    {"kelime": "deklanşöre basmak", "yasakli_kelimeler": ["düğme", "çekim", "fotoğraf makinesi", "parmak", "ses"], "zorluk": "kolay", "aciklama": "Fotoğraf çekmek için makinenin çekim butonuna basmak."},
    {"kelime": "odaklanmak", "yasakli_kelimeler": ["netlik", "bulanık", "focus", "mercek", "göz"], "zorluk": "kolay", "aciklama": "Çekilecek nesneyi vizörde netleştirmek."},
    {"kelime": "flaş patlatmak", "yasakli_kelimeler": ["ışık", "karanlık", "parlama", "gece", "aydınlatma"], "zorluk": "kolay", "aciklama": "Karanlık ortamda anlık güçlü yapay ışık vermek."},
    {"kelime": "selfie çekilmek", "yasakli_kelimeler": ["özçekim", "ön kamera", "telefon", "yüz", "kol uzatmak"], "zorluk": "kolay", "aciklama": "Kişinin kendi görüntüsünü ön kamerayla kaydetmesi."},
    {"kelime": "yakınlaştırmak", "yasakli_kelimeler": ["zoom", "uzak", "lens", "büyütmek", "yakın"], "zorluk": "kolay", "aciklama": "Lens mekanizmasıyla uzaktaki nesneyi çerçeveye yaklaştırmak."},
    {"kelime": "albüm yapmak", "yasakli_kelimeler": ["baskı", "sayfa", "fotoğraf dizmek", "anı", "hatıra"], "zorluk": "kolay", "aciklama": "Basılan fotoğrafları sayfalı deftere yerleştirmek."},
    {"kelime": "poz vermek", "yasakli_kelimeler": ["duruş", "gülümsemek", "kamera", "bakmak", "model"], "zorluk": "kolay", "aciklama": "Fotoğraf makinesinin karşısında belirli bir duruş sergilemek."},
    {"kelime": "fotoğrafı silmek", "yasakli_kelimeler": ["çöp kutusu", "kötü çıkmak", "hafıza kartı", "kaldırmak", "beğenmemek"], "zorluk": "kolay", "aciklama": "İstenmeyen veya kötü çıkmış kareyi hafızadan kaldırmak."},
    {"kelime": "lens kapağını açmak", "yasakli_kelimeler": ["objektif", "koruma", "plastik", "çıkarmak", "cam"], "zorluk": "kolay", "aciklama": "Çekim öncesi merceği örten koruyucu kapağı çıkartmak."},
    {"kelime": "gülümsemek", "yasakli_kelimeler": ["peynir", "mutlu", "surat", "yüz", "poz"], "zorluk": "kolay", "aciklama": "Fotoğraf karesinde neşeli bir ifadeyle görünmek."},
    {"kelime": "manzara çekmek", "yasakli_kelimeler": ["doğa", "dağ", "deniz", "güneş", "geniş açı"], "zorluk": "kolay", "aciklama": "Doğal veya kentsel geniş çevre manzarasını fotoğraflamak."},

    # Orta (24)
    {"kelime": "diyaframı ayarlamak", "yasakli_kelimeler": ["f değeri", "ışık girişi", "alan derinliği", "açıklık", "bıçak"], "zorluk": "orta", "aciklama": "Objektiften geçen ışık miktarını ve netlik derinliğini f değeriyle düzenlemek."},
    {"kelime": "enstantane hızını seçmek", "yasakli_kelimeler": ["perde hızı", "shutter", "hareket dondurma", "saniye", "pozlama süresi"], "zorluk": "orta", "aciklama": "Perdenin ne kadar süre açık kalacağını belirlemek."},
    {"kelime": "iSO değerini yükseltmek", "yasakli_kelimeler": ["gren", "kumlanma", "ışık hassasiyeti", "sensör", "karanlık"], "zorluk": "orta", "aciklama": "Düşük ışıkta sensörün ışık duyarlılığını artırmak."},
    {"kelime": "tripod kurmak", "yasakli_kelimeler": ["üçayak", "sabitlemek", "titreme", "uzun pozlama", "bacak"], "zorluk": "orta", "aciklama": "Kamerayı sarsıntısız tutmak için üç ayaklı sehpaya monte etmek."},
    {"kelime": "filtre takmak", "yasakli_kelimeler": ["nd filtre", "polarize", "uv", "lens önü", "cam"], "zorluk": "orta", "aciklama": "Objektifin önüne ışığı düzenleyen veya yansımayı kesen cam aparat takmak."},
    {"kelime": "beyaz ayarı yapmak", "yasakli_kelimeler": ["white balance", "renk sıcaklığı", "kelvin", "sarı", "mavi ton"], "zorluk": "orta", "aciklama": "Ortam ışığının renk tonunu dengeleyerek beyazı tam beyaz göstermek."},
    {"kelime": "rAW formatında çekmek", "yasakli_kelimeler": ["ham veri", "jpeg", "kalite", "düzenleme", "büyük dosya"], "zorluk": "orta", "aciklama": "Sensörün yakaladığı tüm ışık bilgisini sıkıştırmadan kaydetmek."},
    {"kelime": "kadraj oluşturmak", "yasakli_kelimeler": ["kompozisyon", "çerçeve", "üçler kuralı", "yerleşim", "vizör"], "zorluk": "orta", "aciklama": "Görüntüye girecek ögeleri estetik kurallara göre çerçeveye dizmek."},
    {"kelime": "arka planı bulanıklaştırmak", "yasakli_kelimeler": ["bokeh", "açık diyafram", "portre", "netlik derinliği", "ayrılma"], "zorluk": "orta", "aciklama": "Konuyu öne çıkarmak için arka kısmı flulaştırmak."},
    {"kelime": "uzun pozlama yapmak", "yasakli_kelimeler": ["ışık izi", "gece", "şelale ipeksi", "saniyelerce", "tripod"], "zorluk": "orta", "aciklama": "Perdeyi saniyelerce açık tutarak hareket eden ışıkların izini kaydetmek."},
    {"kelime": "reflektör tutmak", "yasakli_kelimeler": ["gölge doldurma", "gümüş", "altın", "yansıtıcı", "asistan"], "zorluk": "orta", "aciklama": "Doğal ışığı modelin yüzündeki gölgeli kısımlara yansıtmak."},
    {"kelime": "portre çekmek", "yasakli_kelimeler": ["yüz", "insan", "model", "85mm", "ifade"], "zorluk": "orta", "aciklama": "Bir kişinin yüz ifadesini ve karakterini vurgulayan kare yakalamak."},
    {"kelime": "altın saati yakalamak", "yasakli_kelimeler": ["gün batımı", "gün doğumu", "sıcak ışık", "golden hour", "güneş"], "zorluk": "orta", "aciklama": "Güneşin doğuş veya batış anındaki yumuşak ve sıcak ışıktan yararlanmak."},
    {"kelime": "makro çekim yapmak", "yasakli_kelimeler": ["böcek", "çiçek detayı", "birebir büyütme", "yakın", "mercek"], "zorluk": "orta", "aciklama": "Küçük nesneleri gerçek boyutunda veya daha büyük detayla fotoğraflamak."},
    {"kelime": "paning yapmak", "yasakli_kelimeler": ["kaydırma", "hareketli nesne", "arka plan çizgili", "araba", "hız hissi"], "zorluk": "orta", "aciklama": "Hareket eden nesneyi kamerayla takip ederek dinamik hız hissi vermek."},
    {"kelime": "silüet oluşturmak", "yasakli_kelimeler": ["ters ışık", "kara şekil", "gün batımı", "kontur", "aydınlık fon"], "zorluk": "orta", "aciklama": "Öndeki objeyi tamamen karanlık gölge halinde kadraja almak."},
    {"kelime": "fotoğraf düzenlemek", "yasakli_kelimeler": ["photoshop", "lightroom", "rötuş", "kontrast", "renk ayarı"], "zorluk": "orta", "aciklama": "Dijital fotoğrafı yazılımlar aracılığıyla estetik olarak işlemek."},
    {"kelime": "ışıkölçerle ölçüm yapmak", "yasakli_kelimeler": ["pozometre", "lux", "pozlama", "stüdyo", "cihaz"], "zorluk": "orta", "aciklama": "Ortama düşen veya nesneden yansıyan ışık miktarını cihazla ölçmek."},
    {"kelime": "film banyo etmek", "yasakli_kelimeler": ["karanlık oda", "kimyasal", "geliştirici", "fiksaj", "negatif"], "zorluk": "orta", "aciklama": "Analog filmi kimyasal banyolardan geçirerek görünür kılmak."},
    {"kelime": "hafıza kartını biçimlendirmek", "yasakli_kelimeler": ["format atmak", "sd kart", "silme", "temizleme", "kamera"], "zorluk": "orta", "aciklama": "Hafıza kartını kameraya uygun dosya sistemine formatlamak."},
    {"kelime": "seri çekim moduna almak", "yasakli_kelimeler": ["burst", "fps", "ardışık", "spor", "aksiyon"], "zorluk": "orta", "aciklama": "Deklanşöre basılı tutulduğunda saniyede çok sayıda kare çekmek."},
    {"kelime": "üçler kuralını uygulamak", "yasakli_kelimeler": ["kılavuz çizgileri", "kesişim noktaları", "kompozisyon", "kadraj", "üçe bölme"], "zorluk": "orta", "aciklama": "Kadrajı 9 eşit parçaya bölüp ana konuyu kesişim noktalarına koymak."},
    {"kelime": "vizörden bakmak", "yasakli_kelimeler": ["bakarç", "göz", "çerçeve", "ekran", "odak"], "zorluk": "orta", "aciklama": "Kameranın optik veya elektronik göz bakaçından konuyu izlemek."},
    {"kelime": "objektif değiştirmek", "yasakli_kelimeler": ["lens", "bayonet", "çıkarıp takmak", "geniş açı", "telefoto"], "zorluk": "orta", "aciklama": "Çekim açısına uygun yeni bir lensi gövdeye takmak."},

    # Zor (14)
    {"kelime": "hiperfokal mesafeye odaklamak", "yasakli_kelimeler": ["sonsuz netlik", "alan derinliği maksimizasyonu", "manzara", "diyafram", "hesaplama"], "zorluk": "zor", "aciklama": "Kadrajın önünden sonsuza kadar her yerin net olacağı odak noktasını seçmek."},
    {"kelime": "fokus istifleme yapmak", "yasakli_kelimeler": ["focus stacking", "farklı odak noktaları", "birleştirme", "makro", "tam netlik"], "zorluk": "zor", "aciklama": "Farklı noktalara odaklanmış kareleri yazılımla birleştirip derin netlik elde etmek."},
    {"kelime": "histogram okumak", "yasakli_kelimeler": ["tonal dağılım", "patlayan beyazlar", "gölgeler", "grafik", "doğru pozlama"], "zorluk": "zor", "aciklama": "Işığın ton dağılımını gösteren grafikten pozlama hatalarını analiz etmek."},
    {"kelime": "tilt-shift lens kullanmak", "yasakli_kelimeler": ["perspektif düzeltme", "minyatür etkisi", "eğme kaydırma", "mimari çekim", "optik eksen"], "zorluk": "zor", "aciklama": "Objektifin açısını gövdeden bağımsız eğip kaydırarak perspektif kaçmalarını önlemek."},
    {"kelime": "hSS modunda flaş senkronlamak", "yasakli_kelimeler": ["yüksek hız senkronizasyonu", "1/8000 saniye", "gün ışığında açık diyafram", "perde", "strobist"], "zorluk": "zor", "aciklama": "Mekanik perde hızının üzerindeki enstantanelerde flaşı darbe darbe çaktırmak."},
    {"kelime": "bölge sistemini uygulamak", "yasakli_kelimeler": ["zone system", "ansel adams", "on bir ton bölgesi", "saf siyah beyaz", "kontrast"], "zorluk": "zor", "aciklama": "Kareden alınacak tonları 0'dan 10'a kadar ton basamaklarına göre pozlamak."},
    {"kelime": "astronomi takibiyle çekmek", "yasakli_kelimeler": ["star tracker", "yıldız izi olmaması", "dünyanın dönüşü", "samanyolu", "motorlu kundak"], "zorluk": "zor", "aciklama": "Dünyanın dönüşünü kompanse eden motorlu kundakla derin uzay fotoğrafı çekmek."},
    {"kelime": "kromatik aberasyonu düzeltmek", "yasakli_kelimeler": ["renk saçılması", "mor yeşil kenar", "mercek kırılması", "yazılım", "optik hata"], "zorluk": "zor", "aciklama": "Farklı dalga boylarındaki ışığın mercekte odaklanamamasından doğan renk saçılmasını gidermek."},
    {"kelime": "etTR tekniğiyle pozlamak", "yasakli_kelimeler": ["sağa yaslama", "expose to the right", "sinyal gürültü oranı", "maksimum dinamik aralık", "sensör"], "zorluk": "zor", "aciklama": "Histogramı patlatmadan sağa yanaştırarak sensörden en temiz ve zengin veriyi almak."},
    {"kelime": "anamorfik lens ile çekmek", "yasakli_kelimeler": ["sinematik oran", "oval bokeh", "mavi parlama", "sıkıştırma", "2.39:1"], "zorluk": "zor", "aciklama": "Görüntüyü yatayda optik olarak sıkıştırıp sinematik geniş format elde etmek."},
    {"kelime": "karanlık oda baskısı basmak", "yasakli_kelimeler": ["agrandizör", "baryta kağıdı", "kırmızı ışık", "kimyasal tekne", "kontakt"], "zorluk": "zor", "aciklama": "Agrandizör ile negatif filmi duyarlı fotoğraf kağıdına optik olarak basmak."},
    {"kelime": "diffraksiyon sınırını gözetmek", "yasakli_kelimeler": ["f/22 yumuşama", "ışık bükülmesi", "aşırı kısık diyafram", "netlik kaybı", "airy diski"], "zorluk": "zor", "aciklama": "Diyaframı aşırı kısmanın yarattığı ışık bükülmesi kaynaklı bulanıklaşmayı engellemek."},
    {"kelime": "sensör tozu temizlemek", "yasakli_kelimeler": ["swab", "izopropil alkol", "leke", "sensör yüzeyi", "hava pompası"], "zorluk": "zor", "aciklama": "Kamera sensörü üzerindeki mikro toz zerrelerini özel temizleme çubuğuyla silmek."},
    {"kelime": "kalibre edilmiş monitörde işlemek", "yasakli_kelimeler": ["kolorimetre", "icc profili", "srgb adobergb", "renk doğruluğu", "ekran"], "zorluk": "zor", "aciklama": "Baskı ve ekran renk uyumunu sağlamak için ekranı donanımsal cihazla kalibre etmek."}
]

add_and_save_verbs('filateli', filateli_verbs)
add_and_save_verbs('fotografcilik', fotografcilik_verbs)
print('P8 done!')
