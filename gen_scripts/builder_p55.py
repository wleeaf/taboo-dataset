import sys
from card_utils import add_and_save_verbs

# 1. VOLEYBOL (50 verbs: 12 kolay, 24 orta, 14 zor)
voleybol_verbs = [
    # Kolay (12)
    {
        "kelime": "Servis Atmak",
        "aciklama": "Dip çizginin gerisinden topu filenin üzerinden rakip sahaya göndererek oyunu başlatmak.",
        "yasakli_kelimeler": ["dip çizgi", "file", "başlatmak", "top", "rakip"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Smaç Vurmak",
        "aciklama": "File üzerinde yükselerek havada sert bir vuruşla topu rakip sahaya çivilemek.",
        "yasakli_kelimeler": ["sert", "havada", "file", "vuruş", "sayı"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Blok Yapmak",
        "aciklama": "File önünde sıçrayıp elleri yukarı uzatarak rakibin smaç vuruşunu engellemek.",
        "yasakli_kelimeler": ["file", "engellemek", "eller", "sıçramak", "smaç"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Manşet Almak",
        "aciklama": "İki kolu önde birleştirip gergin tutarak gelen alçak topu karşılamak.",
        "yasakli_kelimeler": ["kol", "birleştirmek", "alçak", "karşılamak", "pas"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Parmak Pası Vermek",
        "aciklama": "Topu parmak uçlarıyla yumuşakça dokunarak smaçöre havaya dikmek.",
        "yasakli_kelimeler": ["parmak", "pasör", "dokunmak", "havaya", "smaçör"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Topu Oyunda Tutmak",
        "aciklama": "Zor pozisyonlarda yere düşmek üzere olan topa vurup ralliyi devam ettirmek.",
        "yasakli_kelimeler": ["düşmek", "ralli", "kurtarmak", "devam", "yer"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Mola Almak",
        "aciklama": "Antrenörün takımı kenara çağırıp taktik vermek için oyunu durdurması.",
        "yasakli_kelimeler": ["antrenör", "taktik", "kenar", "durdurmak", "zaman"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Oyuncu Değiştirmek",
        "aciklama": "Sahadaki yorulan veya taktik gereği çıkan oyuncunun yerine yedek oyuncuyu sokmak.",
        "yasakli_kelimeler": ["tabela", "yedek", "giriş", "çıkış", "kenar"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Fileye Dokunmak",
        "aciklama": "Oyun esnasında vücudun veya formanın fileye temas ederek hata yapması.",
        "yasakli_kelimeler": ["hata", "temas", "düdük", "faul", "ağ"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Sayı Sevinci Yaşamak",
        "aciklama": "Kazanılan puan sonrası takım arkadaşlarının sahada toplanıp sarılması.",
        "yasakli_kelimeler": ["puan", "kutlama", "sarılmak", "sevinç", "alkış"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Dönüş Yapmak",
        "aciklama": "Servis hakkı kazanıldığında sahadaki oyuncuların saat yönünde bir pozisyon kayması.",
        "yasakli_kelimeler": ["saat yönü", "pozisyon", "rotasyon", "kaymak", "altı numara"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Hakemle Konuşmak",
        "aciklama": "Takım kaptanının tartışmalı pozisyonlar hakkında başhakeme soru sorması.",
        "yasakli_kelimeler": ["kaptan", "başhakem", "itiraz", "soru", "kule"],
        "zorluk": "kolay"
    },

    # Orta (24)
    {
        "kelime": "Plase Bırakmak",
        "aciklama": "Smaç vurur gibi yükselip topu rakip sahanın boş bir köşesine parmak ucuyla yumuşakça aşırtmak.",
        "yasakli_kelimeler": ["yumuşak", "aşırtma", "boşluk", "parmak ucu", "kandırmak"],
        "zorluk": "orta"
    },
    {
        "kelime": "Dublaja Girmek",
        "aciklama": "Kendi smaçörünün vuruşu bloktan dönerse topu yere düşmeden kurtarmak için arkasına yanaşmak.",
        "yasakli_kelimeler": ["bloktan dönen", "kurtarma", "arkasına", "yanaşmak", "savunma"],
        "zorluk": "orta"
    },
    {
        "kelime": "Duble Blok Kurmak",
        "aciklama": "File önünde iki oyuncunun yan yana sıçrayarak rakip smaca karşı geniş bir duvar örmesi.",
        "yasakli_kelimeler": ["iki oyuncu", "yan yana", "duvar", "sıçrama", "kapatmak"],
        "zorluk": "orta"
    },
    {
        "kelime": "Üçlü Blok Yapmak",
        "aciklama": "Rakibin en etkili hücumuna karşı üç ön oyuncunun birden havada duvar oluşturması.",
        "yasakli_kelimeler": ["üç oyuncu", "orta oyuncu", "köşe", "duvar", "engelleme"],
        "zorluk": "orta"
    },
    {
        "kelime": "Smaç Servis Kullanmak",
        "aciklama": "Yüksekten atılan topa birkaç adım koşup havada sıçrayarak çok sert ve hızlı servis atmak.",
        "yasakli_kelimeler": ["koşu", "sıçramak", "hızlı", "sert", "havada"],
        "zorluk": "orta"
    },
    {
        "kelime": "Yüzen Servis Atmak",
        "aciklama": "Topa dönmeden, havadaki hava direnciyle sağa sola yalpalanarak gidecek şekilde avuç içiyle vurmak.",
        "yasakli_kelimeler": ["float", "dönmeyen", "yalpalama", "hava direnci", "avuç içi"],
        "zorluk": "orta"
    },
    {
        "kelime": "Libero Değişimi Yapmak",
        "aciklama": "Arka hatta geçen orta oyuncu yerine özel savunma oyuncusunun kuralsız girip çıkması.",
        "yasakli_kelimeler": ["savunma", "farklı forma", "orta oyuncu", "arka hat", "serbest"],
        "zorluk": "orta"
    },
    {
        "kelime": "Görüntülü Değerlendirme İstemek",
        "aciklama": "Çizgiye basma, topun içeri düşmesi veya blok teması için kamera incelemesi talep etmek.",
        "yasakli_kelimeler": ["challenge", "gds", "kamera", "itiraz", "temas"],
        "zorluk": "orta"
    },
    {
        "kelime": "Arka Hattan Hücum Etmek",
        "aciklama": "Üç metre çizgisinin gerisinden sıçrayıp havada çizgiye basmadan smaç vurmak.",
        "yasakli_kelimeler": ["üç metre çizgisi", "geriden", "pipe", "sıçramak", "hücum"],
        "zorluk": "orta"
    },
    {
        "kelime": "Blok Aut Yaptırmak",
        "aciklama": "Smaçörün topu bilerek rakip bloğun parmaklarına çarptırıp saha dışına göndermesi.",
        "yasakli_kelimeler": ["parmak", "çarpma", "dışarı", "akıllı vuruş", "sayı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Dizlikle Sahaya Kaymak",
        "aciklama": "Yere düşen topu kurtarmak için parke zemin üzerinde dizlerinin üstünde kaymak.",
        "yasakli_kelimeler": ["parke", "zemin", "dizlik", "kayma", "kurtarış"],
        "zorluk": "orta"
    },
    {
        "kelime": "Hızlı Hücum Yapmak",
        "aciklama": "Pasörün topu fileye çok yakın ve alçaktan orta oyuncuya sıfır pasla hemen vurdurması.",
        "yasakli_kelimeler": ["kısa pas", "orta oyuncu", "alçak", "sıfır", "ani"],
        "zorluk": "orta"
    },
    {
        "kelime": "Çapraza Vurmak",
        "aciklama": "Smaçörün file üzerinden topu rakip sahanın uzak karşı çapraz köşesine yönlendirmesi.",
        "yasakli_kelimeler": ["çapraz", "köşe", "açı", "uzak köşe", "smaç"],
        "zorluk": "orta"
    },
    {
        "kelime": "Paralele Vurmak",
        "aciklama": "Yan çizgi boyunca, bloğun hemen yanından düz bir hatla smaç indirmek.",
        "yasakli_kelimeler": ["çizgi üstü", "yan çizgi", "düz", "hat", "köşe"],
        "zorluk": "orta"
    },
    {
        "kelime": "Dört Numaradan Hücum Etmek",
        "aciklama": "Ön sol köşe bölgesinden pasörün açtığı yüksek topa smaçörün hücum yapması.",
        "yasakli_kelimeler": ["sol köşe", "bölge", "pas", "açık", "ön hat"],
        "zorluk": "orta"
    },
    {
        "kelime": "İki Numaradan Yükselmek",
        "aciklama": "Ön sağ köşe bölgesinden pasör çaprazının hücum için havaya fırlaması.",
        "yasakli_kelimeler": ["sağ köşe", "pasör çaprazı", "hücum", "bölge", "ön hat"],
        "zorluk": "orta"
    },
    {
        "kelime": "Topu Taşımak",
        "aciklama": "Topa net vurmak yerine elde tutma veya fırlatma hissi vererek teknik kural hatası yapmak.",
        "yasakli_kelimeler": ["tutma", "teknik hata", "hakem", "düdük", "kural"],
        "zorluk": "orta"
    },
    {
        "kelime": "Çift Vuruş Yapmak",
        "aciklama": "Bir oyuncunun topa peş peşe iki defa temas etmesiyle kural ihlali oluşması.",
        "yasakli_kelimeler": ["ihlal", "iki kez", "üst üste", "düdük", "temas"],
        "zorluk": "orta"
    },
    {
        "kelime": "Çizgiye Basmak",
        "aciklama": "Servis atarken veya üç metre hücumunda ayağın sınır çizgisine değmesi.",
        "yasakli_kelimeler": ["ayak", "sınır", "ihlal", "servis anı", "üç metre"],
        "zorluk": "orta"
    },
    {
        "kelime": "Fileye Asılmak",
        "aciklama": "Smaç veya blok sonrası dengesini kaybedip file ağlarına tutunmak.",
        "yasakli_kelimeler": ["tutunmak", "ağ", "denge", "faul", "düşüş"],
        "zorluk": "orta"
    },
    {
        "kelime": "Dört Vuruş Hatası Yapmak",
        "aciklama": "Topu rakip sahaya göndermek için tanınan en fazla üç pas hakkını aşmak.",
        "yasakli_kelimeler": ["üç pas", "aşmak", "takım hatası", "sayı kaybı", "düdük"],
        "zorluk": "orta"
    },
    {
        "kelime": "Göz Teması Kurmak",
        "aciklama": "Pasör ile smaçörün servis atılmadan önce nereye hücum yapılacağını bakışlarla kararlaştırması.",
        "yasakli_kelimeler": ["bakış", "anlaşma", "gizli işaret", "pasör", "hücum planı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Arkadan Pas Atmak",
        "aciklama": "Pasörün vücudu sola dönükken geriye doğru iki numaraya kör pas çıkarması.",
        "yasakli_kelimeler": ["geriye", "ters pas", "iki numara", "pasör", "kör pas"],
        "zorluk": "orta"
    },
    {
        "kelime": "Isınma Alanında Beklemek",
        "aciklama": "Yedek oyuncuların sahanın köşesindeki kare alanda hareket halinde hazır beklemesi.",
        "yasakli_kelimeler": ["yedekler", "kare alan", "köşe", "hazır", "hareket"],
        "zorluk": "orta"
    },

    # Zor (14)
    {
        "kelime": "Pancake Savunması Yapmak",
        "aciklama": "Top tam yere değer değmez elin sırtını parkeye sererek topu sektirip kurtarmak.",
        "yasakli_kelimeler": ["el sırtı", "parke", "kurtarış", "zemin", "avuç tersi"],
        "zorluk": "zor"
    },
    {
        "kelime": "Pipe Hücumu Düzenlemek",
        "aciklama": "Pasörün altı numaradaki arka hat oyuncusuna üç metre gerisinden yüksek hücum pası atması.",
        "yasakli_kelimeler": ["altı numara", "arka hat hücumu", "üç metre gerisi", "orta koridor", "merkez"],
        "zorluk": "zor"
    },
    {
        "kelime": "Tandem Hücum Yapmak",
        "aciklama": "Orta oyuncunun sahte sıçrama yapıp blokçuları çekmesiyle arkasındaki köşe oyuncusunun vurması.",
        "yasakli_kelimeler": ["sahte sıçrama", "kombinasyon", "blok aldatma", "arka arkaya", "hücum"],
        "zorluk": "zor"
    },
    {
        "kelime": "Antene Çarptırmak",
        "aciklama": "Vurulan topun filenin iki ucundaki sınır çubuğuna temas ederek oyun dışı kalması.",
        "yasakli_kelimeler": ["çubuk", "sınır", "file ucu", "out", "temas"],
        "zorluk": "zor"
    },
    {
        "kelime": "Blok Açığını Kapatmak",
        "aciklama": "Orta oyuncunun hızla köşeye kayarak köşe blokçusuyla arasındaki boşluğu sıfırlaması.",
        "yasakli_kelimeler": ["boşluk", "kayma", "orta oyuncu", "sıfırlama", "duvar"],
        "zorluk": "zor"
    },
    {
        "kelime": "Joust Mücadelesi Vermek",
        "aciklama": "File bandının tam üstündeki topa iki rakip oyuncunun aynı anda elleriyle baskı yapması.",
        "yasakli_kelimeler": ["file bandı", "karşılıklı itiş", "aynı anda", "baskı", "üstte"],
        "zorluk": "zor"
    },
    {
        "kelime": "Örme Hücumu Çalıştırmak",
        "aciklama": "İki smaçörün çapraz koşularla yer değiştirip rakip blok organizasyonunu bozması.",
        "yasakli_kelimeler": ["çapraz koşu", "yer değiştirme", "kombinasyon", "taktik", "şaşırtma"],
        "zorluk": "zor"
    },
    {
        "kelime": "Sıfıra Yakın Pas Çıkarmak",
        "aciklama": "Pasörün fileye milimetrik yakınlıkta orta oyuncunun anında vurabileceği dik ve kısa top atması.",
        "yasakli_kelimeler": ["milimetrik", "kısa pas", "orta oyuncu", "ani", "yakın"],
        "zorluk": "zor"
    },
    {
        "kelime": "Pozisyon Boşluğunu Korumak",
        "aciklama": "Dönüş hatası yapmamak için servis atılana kadar herkesin kendi kural alanında durmasını sağlamak.",
        "yasakli_kelimeler": ["rotasyon hatası", "kural alanı", "diziliş", "servis anı", "yerleşme"],
        "zorluk": "zor"
    },
    {
        "kelime": "Taktiksel Servis Yöneltmek",
        "aciklama": "Topu rakibin manşeti en zayıf oyuncusuna veya pasörün kaçış yoluna hedefleyerek atmak.",
        "yasakli_kelimeler": ["zayıf halka", "hedef oyuncu", "manşet zaafı", "kaçış yolu", "strateji"],
        "zorluk": "zor"
    },
    {
        "kelime": "Kayma Adımıyla Bloğa Yetişmek",
        "aciklama": "Orta oyuncunun file boyunca yana doğru hızlı adımlarla köşe smacını kapatmaya koşması.",
        "yasakli_kelimeler": ["yana adım", "orta oyuncu", "file boyunca", "yetişmek", "blok"],
        "zorluk": "zor"
    },
    {
        "kelime": "Blok Üzerinden Aşırtmak",
        "aciklama": "Rakip bloğun boyunu aşacak şekilde kavisli ve derin bir vuruşla arka çizgiye top indirmek.",
        "yasakli_kelimeler": ["kavis", "derin", "arka çizgi", "bloğun üstü", "uzun plase"],
        "zorluk": "zor"
    },
    {
        "kelime": "Savunma Düzenini 6-2 Kurmak",
        "aciklama": "Sahada sürekli üç ön hücumcu bulundurmak için iki pasörlü rotasyon taktiği uygulamak.",
        "yasakli_kelimeler": ["çift pasör", "üç hücumcu", "sistem", "taktik", "rotasyon"],
        "zorluk": "zor"
    },
    {
        "kelime": "Tie-break Setini Yönetmek",
        "aciklama": "2-2 eşitlik sonrası oynanan 15 sayılık final setinde stres ve mola yönetimini idare etmek.",
        "yasakli_kelimeler": ["15 sayı", "beşinci set", "final", "stres", "saha değişimi"],
        "zorluk": "zor"
    }
]

# 2. YAPAYZEKA (50 verbs: 12 kolay, 24 orta, 14 zor)
yapayzeka_verbs = [
    # Kolay (12)
    {
        "kelime": "Model Eğitmek",
        "aciklama": "Yapay zeka algoritmasına veriler sunarak öğrenmesini sağlamak.",
        "yasakli_kelimeler": ["veri", "öğrenmek", "algoritma", "training", "sonuç"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Soru Sormak",
        "aciklama": "ChatGPT veya sohbet botuna prompt girerek yanıt istemek.",
        "yasakli_kelimeler": ["prompt", "chatgpt", "bot", "yanıt", "yazmak"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Metin Üretmek",
        "aciklama": "Büyük dil modelinin verilen talimata uygun makale veya şiir yazması.",
        "yasakli_kelimeler": ["yazmak", "makale", "şiir", "llm", "içerik"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Resim Çizdirmek",
        "aciklama": "Metinsel açıklama girerek difüzyon modeliyle görsel oluşturmak.",
        "yasakli_kelimeler": ["midjourney", "görsel", "çizim", "difüzyon", "fotoğraf"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Yüz Tanımak",
        "aciklama": "Kamera görüntüsündeki insan çehresini tespit edip kimlikle eşleştirmek.",
        "yasakli_kelimeler": ["çehre", "kamera", "kimlik", "güvenlik", "kilit açma"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Ses Tanımak",
        "aciklama": "Mikrofondan gelen konuşma sesini yazıya dönüştürmek (speech-to-text).",
        "yasakli_kelimeler": ["mikrofon", "konuşma", "yazı", "sesli asistan", "transkript"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Çeviri Yapmak",
        "aciklama": "Bir dildeki metni yapay zeka ile başka bir dile otomatik aktarmak.",
        "yasakli_kelimeler": ["dil", "tercüme", "ingilizce", "türkçe", "google çeviri"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Kod Yazdırmak",
        "aciklama": "Yapay zekaya belirli bir işlevi yerine getiren programlama kodu ürettirmek.",
        "yasakli_kelimeler": ["python", "programlama", "yazılım", "fonksiyon", "copilot"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Veri Toplamak",
        "aciklama": "Modelin eğitimi için internetten veya sensörlerden bilgi derlemek.",
        "yasakli_kelimeler": ["bilgi", "dataset", "internet", "derleme", "kaynak"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Öneri Sunmak",
        "aciklama": "Kullanıcının geçmiş zevklerine göre film, müzik veya ürün tavsiye etmek.",
        "yasakli_kelimeler": ["tavsiye", "film", "müzik", "netflix", "algoritma"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Tahmin Yapmak",
        "aciklama": "Geçmiş verilere bakarak gelecekteki hava durumu veya fiyatı öngörmek.",
        "yasakli_kelimeler": ["öngörü", "gelecek", "fiyat", "hava durumu", "istatistik"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Hata Bulmak",
        "aciklama": "Yazılan kod veya metindeki yanlışları yapay zeka yardımıyla tespit etmek.",
        "yasakli_kelimeler": ["yanlış", "bug", "düzeltme", "tespit", "kontrol"],
        "zorluk": "kolay"
    },

    # Orta (24)
    {
        "kelime": "Prompt Yazmak",
        "aciklama": "Yapay zekadan en doğru sonucu almak için detaylı yönerge ve talimat hazırlamak.",
        "yasakli_kelimeler": ["talimat", "yönerge", "mühendislik", "girdi", "bağlam"],
        "zorluk": "orta"
    },
    {
        "kelime": "Fine-Tuning Yapmak",
        "aciklama": "Önceden eğitilmiş bir temel modeli özel bir alana ait veri setiyle ince ayara tabi tutmak.",
        "yasakli_kelimeler": ["ince ayar", "önceden eğitilmiş", "özel veri", "adapte", "ağırlık"],
        "zorluk": "orta"
    },
    {
        "kelime": "Etiketleme Yapmak",
        "aciklama": "Gözetimli öğrenme için verileri 'kedi', 'köpek' gibi kategorik etiketlerle işaretlemek.",
        "yasakli_kelimeler": ["label", "gözetimli", "işaretleme", "kategori", "sınıflandırma"],
        "zorluk": "orta"
    },
    {
        "kelime": "Overfitting Olmak",
        "aciklama": "Modelin eğitim verisini ezberleyip yeni ve görmediği verilerde başarısız olması.",
        "yasakli_kelimeler": ["ezberlemek", "aşırı uyum", "genelleme", "başarısızlık", "eğitim verisi"],
        "zorluk": "orta"
    },
    {
        "kelime": "Halüsinasyon Görmek",
        "aciklama": "Büyük dil modelinin kendinden emin bir şekilde tamamen uydurma ve yanlış bilgi üretmesi.",
        "yasakli_kelimeler": ["uydurma", "yanlış bilgi", "llm", "emin", "gerçek dışı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Vektör Veritabanı Kurmak",
        "aciklama": "Metin ve görsellerin anlamsal embedding değerlerini saklayıp hızlı arama yapmak.",
        "yasakli_kelimeler": ["embedding", "anlamsal", "pinecone", "rag", "benzerlik"],
        "zorluk": "orta"
    },
    {
        "kelime": "RAG Entegre Etmek",
        "aciklama": "Modele harici şirket belgelerinden arama yaptırıp bilgiye dayalı cevap verdirmek.",
        "yasakli_kelimeler": ["retrieval", "belge", "arama", "bilgi getirme", "vektör"],
        "zorluk": "orta"
    },
    {
        "kelime": "GPU Tahsis Etmek",
        "aciklama": "Derin öğrenme eğitim sürecini hızlandırmak için güçlü ekran kartı sunucuları kiralamak.",
        "yasakli_kelimeler": ["ekran kartı", "nvidia", "cuda", "bulut", "sunucu"],
        "zorluk": "orta"
    },
    {
        "kelime": "Ağırlıkları Güncellemek",
        "aciklama": "Geriye yayılım algoritması ile yapay sinir ağındaki düğüm katsayılarını optimize etmek.",
        "yasakli_kelimeler": ["weights", "katsayı", "geriye yayılım", "optimizasyon", "nöron"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kayıp Fonksiyonunu Azaltmak",
        "aciklama": "Modelin tahminleri ile gerçek değerler arasındaki loss farkını minimize etmek.",
        "yasakli_kelimeler": ["loss", "hata payı", "minimize", "hedef", "fonksiyon"],
        "zorluk": "orta"
    },
    {
        "kelime": "Sentetik Veri Üretmek",
        "aciklama": "Yetersiz kalan eğitim verisini artırmak için yapay zekaya yapay veri ürettirmek.",
        "yasakli_kelimeler": ["yapay veri", "çoğaltma", "veri seti", "augmentation", "eğitim"],
        "zorluk": "orta"
    },
    {
        "kelime": "Modeli Sıkıştırmak",
        "aciklama": "Milyarlarca parametrelik modeli kuantizasyonla 4-bit veya 8-bit boyutuna indirgemek.",
        "yasakli_kelimeler": ["kuantizasyon", "küçültmek", "4-bit", "gguf", "ram"],
        "zorluk": "orta"
    },
    {
        "kelime": "Chatbot Konfigüre Etmek",
        "aciklama": "Sistem promptu girerek yapay zekaya belirli bir kişilik ve kurallar tanımlamak.",
        "yasakli_kelimeler": ["sistem promptu", "kişilik", "kural", "rol", "ayar"],
        "zorluk": "orta"
    },
    {
        "kelime": "Segmentasyon Yapmak",
        "aciklama": "Görüntüdeki her bir nesnenin piksellerini ayrı ayrı renklendirip sınırlarını çizmek.",
        "yasakli_kelimeler": ["piksel", "nesne ayırma", "bilgisayarlı görü", "maske", "sınır"],
        "zorluk": "orta"
    },
    {
        "kelime": "Öznitelik Çıkarmak",
        "aciklama": "Ham verideki en ayırt edici ve önemli örüntüleri matematiksel olarak tespit etmek.",
        "yasakli_kelimeler": ["feature extraction", "örüntü", "ayırt edici", "ham veri", "vektör"],
        "zorluk": "orta"
    },
    {
        "kelime": "Gözetimsiz Öğrenmek",
        "aciklama": "Etiketsiz ham veriyi kümeleme algoritmalarıyla kendi kendine gruplandırmak.",
        "yasakli_kelimeler": ["etiketsiz", "kümeleme", "k-means", "gruplama", "kendi kendine"],
        "zorluk": "orta"
    },
    {
        "kelime": "Pekiştirmeli Öğrenmek",
        "aciklama": "Ajanın çevresiyle etkileşime girip ödül ve ceza mekanizmasıyla en iyi stratejiyi bulması.",
        "yasakli_kelimeler": ["ödül", "ceza", "ajan", "reinforcement", "çevre"],
        "zorluk": "orta"
    },
    {
        "kelime": "Ön İşleme Yapmak",
        "aciklama": "Veri setindeki eksik, gürültülü veya hatalı kısımları temizleyip normalize etmek.",
        "yasakli_kelimeler": ["temizleme", "normalizasyon", "gürültü", "eksik veri", "preprocessing"],
        "zorluk": "orta"
    },
    {
        "kelime": "Doğruluk Oranını Ölçmek",
        "aciklama": "Test veri seti üzerinde modelin precision, recall ve accuracy skorlarını hesaplamak.",
        "yasakli_kelimeler": ["accuracy", "precision", "recall", "skor", "test"],
        "zorluk": "orta"
    },
    {
        "kelime": "API Bağlantısı Kurmak",
        "aciklama": "OpenAI veya Anthropic sunucularına JSON isteği göndererek model çıktısı almak.",
        "yasakli_kelimeler": ["openai", "endpoint", "json", "istek", "token"],
        "zorluk": "orta"
    },
    {
        "kelime": "Token Saymak",
        "aciklama": "Girdi ve çıktı metinlerinin model bağlam penceresindeki kelime parçası maliyetini bulmak.",
        "yasakli_kelimeler": ["bağlam penceresi", "maliyet", "parça", "tokenizer", "limit"],
        "zorluk": "orta"
    },
    {
        "kelime": "Çok Modlu Çalışmak",
        "aciklama": "Aynı modelin metin, ses, video ve görseli bir arada anlayıp işleyebilmesi (multimodal).",
        "yasakli_kelimeler": ["multimodal", "görsel", "ses", "video", "metin"],
        "zorluk": "orta"
    },
    {
        "kelime": "Modeli Dağıtmak",
        "aciklama": "Eğitimi biten yapay zeka modelini kullanıcıların erişebileceği canlı sunucuya yüklemek.",
        "yasakli_kelimeler": ["deployment", "canlı", "sunucu", "docker", "bulut"],
        "zorluk": "orta"
    },
    {
        "kelime": "Sıcaklık Ayarı Yapmak",
        "aciklama": "Modelin çıktısındaki yaratıcılık ve rastgelelik seviyesini (temperature) belirlemek.",
        "yasakli_kelimeler": ["temperature", "yaratıcılık", "rastgelelik", "0 ve 1", "çıktı"],
        "zorluk": "orta"
    },

    # Zor (14)
    {
        "kelime": "Dikkat Mekanizması Kurmak",
        "aciklama": "Transformer mimarisinde kelimelerin birbirine göre anlamsal ağırlıklarını (Self-Attention) hesaplamak.",
        "yasakli_kelimeler": ["self attention", "transformer", "ağırlık", "matris", "bağlam"],
        "zorluk": "zor"
    },
    {
        "kelime": "Geriye Yayılım Uygulamak",
        "aciklama": "Zincir kuralı türevi kullanarak çıktı hatasını katmanlar boyunca geriye doğru iletmek.",
        "yasakli_kelimeler": ["backpropagation", "zincir kuralı", "türev", "gradyan", "katman"],
        "zorluk": "zor"
    },
    {
        "kelime": "Gradyan İnişi Yapmak",
        "aciklama": "Kayıp fonksiyonunun eğimini takip ederek parametreleri adım adım minimum noktaya taşımak.",
        "yasakli_kelimeler": ["gradient descent", "öğrenme oranı", "eğim", "minimum", "adam"],
        "zorluk": "zor"
    },
    {
        "kelime": "RLHF Eğitimi Vermek",
        "aciklama": "İnsan geri bildirimiyle ödül modeli eğiterek dil modelini ahlaki ve yardımsever kılmak.",
        "yasakli_kelimeler": ["insan geri bildirimi", "ödül modeli", "hizalama", "pekiştirmeli", "güvenlik"],
        "zorluk": "zor"
    },
    {
        "kelime": "LoRA Adaptörü Eğitmek",
        "aciklama": "Modelin tüm ağırlıklarını dondurup düşük dereceli matrislerle hızlı ve hafif ince ayar yapmak.",
        "yasakli_kelimeler": ["düşük derece", "matris", "dondurmak", "hafif", "peft"],
        "zorluk": "zor"
    },
    {
        "kelime": "Konvolüsyon Filtresi Gezdirmek",
        "aciklama": "CNN modellerinde görselin kenar ve dokularını yakalamak için çekirdek matrisi kaydırmak.",
        "yasakli_kelimeler": ["cnn", "kernel", "matris", "kenar bulma", "filtre"],
        "zorluk": "zor"
    },
    {
        "kelime": "Gürültüden Görsel Üretmek",
        "aciklama": "Difüzyon modellerinde rastgele Gaussian gürültüsünü ters adımlarla net görsele dönüştürmek.",
        "yasakli_kelimeler": ["gaussian", "gürültü giderme", "denoising", "ters difüzyon", "latent"],
        "zorluk": "zor"
    },
    {
        "kelime": "Latent Uzayı Haritalamak",
        "aciklama": "Verilerin çok boyutlu sıkıştırılmış anlamsal temsil manifoldunu analiz etmek.",
        "yasakli_kelimeler": ["latent space", "çok boyutlu", "temsil", "manifold", "sıkıştırma"],
        "zorluk": "zor"
    },
    {
        "kelime": "Gradyan Patlamasını Önlemek",
        "aciklama": "Derin ağlarda katsayıların sonsuza gitmesini engellemek için gradient clipping uygulamak.",
        "yasakli_kelimeler": ["clipping", "sonsuz", "patlama", "nan", "derin ağ"],
        "zorluk": "zor"
    },
    {
        "kelime": "Dropout Uygulamak",
        "aciklama": "Aşırı öğrenmeyi engellemek için eğitim esnasında rastgele nöronları geçici olarak devre dışı bırakmak.",
        "yasakli_kelimeler": ["nöron kapatma", "rastgele", "düzenlileştirme", "ezber engelleme", "olasılık"],
        "zorluk": "zor"
    },
    {
        "kelime": "Mixture of Experts Kurmak",
        "aciklama": "Her bir token için tüm modeli değil yalnızca ilgili uzman alt ağları yönlendiriciyle çalıştırmak.",
        "yasakli_kelimeler": ["moe", "yönlendirici", "uzman ağ", "alt model", "verimlilik"],
        "zorluk": "zor"
    },
    {
        "kelime": "Positional Encoding Eklemek",
        "aciklama": "Transformer modellerine kelimelerin cümle içindeki sıra ve konum bilgisini sinüs dalgalarıyla aktarmak.",
        "yasakli_kelimeler": ["sıra bilgisi", "konum", "sinüs", "vektör", "sırasızlık"],
        "zorluk": "zor"
    },
    {
        "kelime": "Ajanik İş Akışı Tasarlamak",
        "aciklama": "Birden çok LLM ajanının araç kullanarak bir görevi planlayıp kendi kendine tamamlamasını sağlamak.",
        "yasakli_kelimeler": ["agent", "araç kullanımı", "otonom", "planlama", "iş akışı"],
        "zorluk": "zor"
    },
    {
        "kelime": "Zero-Shot Tahmini Almak",
        "aciklama": "Modele daha önce hiç örneğini görmediği bir görevi hiçbir eğitim veya örnek vermeden çözdürmek.",
        "yasakli_kelimeler": ["örneksiz", "önceden görmemiş", "genelleme", "prompt", "few-shot"],
        "zorluk": "zor"
    }
]

if __name__ == "__main__":
    add_and_save_verbs("voleybol", voleybol_verbs)
    add_and_save_verbs("yapayzeka", yapayzeka_verbs)
