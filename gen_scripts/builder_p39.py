# -*- coding: utf-8 -*-
from card_utils import add_and_save_verbs

resim_verbs = [
    # Kolay (12)
    {"kelime": "çizmek", "aciklama": "kurşun kalem veya kömürle kağıt üzerine kontur hatları çekmek", "yasakli_kelimeler": ["kalem", "kağıt", "hat", "desen", "kontur"], "zorluk": "kolay"},
    {"kelime": "boyamak", "aciklama": "fırçayı boyaya batırıp tuvaldeki alanları renklendirmek", "yasakli_kelimeler": ["fırça", "renk", "tuval", "boya", "alan"], "zorluk": "kolay"},
    {"kelime": "karıştırmak", "aciklama": "palet üzerinde ana renkleri harmanlayıp ara tonlar elde etmek", "yasakli_kelimeler": ["palet", "renk", "ton", "harman", "ana renk"], "zorluk": "kolay"},
    {"kelime": "silmek", "aciklama": "hamur silgiyle kağıttaki hatalı kurşun kalem çizgilerini yok etmek", "yasakli_kelimeler": ["silgi", "çizgi", "hata", "kağıt", "temizlemek"], "zorluk": "kolay"},
    {"kelime": "sergilemek", "aciklama": "tamamlanan tabloları sanat galerisinde duvarlara asıp ziyarete açmak", "yasakli_kelimeler": ["galeri", "tablo", "duvar", "sergi", "ziyaretçi"], "zorluk": "kolay"},
    {"kelime": "imzalamak", "aciklama": "tablonun sağ alt köşesine ressamın kendi imzasını atması", "yasakli_kelimeler": ["ressam", "sağ alt", "köşe", "imza", "tablo"], "zorluk": "kolay"},
    {"kelime": "çerçeveletmek", "aciklama": "resmin etrafına ahşap veya yaldızlı çerçeve takıp camlatmak", "yasakli_kelimeler": ["çerçeve", "ahşap", "paspartu", "cam", "kenar"], "zorluk": "kolay"},
    {"kelime": "kurutmak", "aciklama": "yağlı boya tablosunu atölyede günlerce bekletip kurumasını sağlamak", "yasakli_kelimeler": ["bekletmek", "yağlı boya", "atölye", "zaman", "ıslak"], "zorluk": "kolay"},
    {"kelime": "ilham almak", "aciklama": "doğadan veya insan yüzlerinden etkilenip yeni resim fikri bulmak", "yasakli_kelimeler": ["fikir", "doğa", "yaratıcılık", "etkilenmek", "esin"], "zorluk": "kolay"},
    {"kelime": "model olmak", "aciklama": "ressamın karşısına oturup saatlerce kıpırdamadan poz vermek", "yasakli_kelimeler": ["poz vermek", "canlı model", "oturmak", "kıpırdamamak", "ressam"], "zorluk": "kolay"},
    {"kelime": "lekelemek", "aciklama": "fırçadan sıçrayan boya damlalarıyla yüzeyde doku ve iz bırakmak", "yasakli_kelimeler": ["damla", "sıçratma", "iz", "doku", "fırça"], "zorluk": "kolay"},
    {"kelime": "gözlemlemek", "aciklama": "ışığın nesneler üzerindeki düşüşünü ve gölgeleri dikkatle incelemek", "yasakli_kelimeler": ["ışık gölge", "nesne", "bakmak", "incelemek", "dikkat"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "tuval germek", "aciklama": "ham keten bezi ahşap şaseye zımbayla sımsıkı gerdirmek", "yasakli_kelimeler": ["keten bez", "şase", "ahşap çıta", "zımba", "gergi"], "zorluk": "orta"},
    {"kelime": "gesso sürmek", "aciklama": "tuval bezinin boyayı emmesini engellemek için beyaz astar çekmek", "yasakli_kelimeler": ["astar", "beyaz", "astar boyası", "astar çekme", "emilme"], "zorluk": "orta"},
    {"kelime": "şövale kurmak", "aciklama": "üç ayaklı ahşap resim sehpasını atölyeye veya doğaya dikmek", "yasakli_kelimeler": ["sehpa", "üç ayak", "ahşap", "tuval tutucu", "atölye"], "zorluk": "orta"},
    {"kelime": "spatula ile sürmek", "aciklama": "yoğun yağlı boyayı resim bıçağıyla tuvale kalın katmanlar halinde yaymak", "yasakli_kelimeler": ["resim bıçağı", "palet bıçağı", "impasto", "kalın katman", "metal"], "zorluk": "orta"},
    {"kelime": "perspektif kaçışı", "aciklama": "çizgileri ufuk çizgisindeki tek veya çift kaçış noktasına bağlamak", "yasakli_kelimeler": ["kaçış noktası", "ufuk çizgisi", "derinlik", "üç boyut", "çizgisel"], "zorluk": "orta"},
    {"kelime": "verniklemek", "aciklama": "tamamen kuruyan yağlı boya tablosunu koruyucu parlak vernikle cilalamak", "yasakli_kelimeler": ["damar verniği", "cila", "koruyucu katman", "parlaklık", "sararma önleyici"], "zorluk": "orta"},
    {"kelime": "sfumato uygulamak", "aciklama": "da vinci'nin mona lisa'da yaptığı gibi renk sınırlarını duman gibi yumuşatmak", "yasakli_kelimeler": ["da vinci", "dumanlı", "geçiş yumuşatma", "sınır yok etme", "mona lisa"], "zorluk": "orta"},
    {"kelime": "klasik chiaroscuro", "aciklama": "caravaggio gibi sert ışık ve zifiri karanlık gölge kontrastı kurmak", "yasakli_kelimeler": ["ışık gölge", "caravaggio", "sert kontrast", "karanlık zemin", "aydınlatma"], "zorluk": "orta"},
    {"kelime": "kroki almak", "aciklama": "hareket halindeki nesneyi birkaç hızlı çizgi darbesiyle taslaklamak", "yasakli_kelimeler": ["taslak", "hızlı çizim", "birkaç saniye", "eskiz", "çizgi"], "zorluk": "orta"},
    {"kelime": "füzenle gölgelendirmek", "aciklama": "yanık asma dalından yapılan doğal kömür çubukla tonlama yapmak", "yasakli_kelimeler": ["doğal kömür", "asma dalı", "siyah ton", "dağıtma", "parmakla yayma"], "zorluk": "orta"},
    {"kelime": "ebru teknesine boya damlatmak", "aciklama": "kitreli suyun yüzeyine öd katkılı toprak boyaları fırçayla serpmek", "yasakli_kelimeler": ["kitre", "öd", "toprak boya", "tekne", "biz"], "zorluk": "orta"},
    {"kelime": "minyatür işlemek", "aciklama": "osmanlı yazmalarına gölgesiz ve perspektifsiz ince detaylı nakış resim yapmak", "yasakli_kelimeler": ["nakkaş", "gölgesiz", "osmanlı", "ince fırça", "yazma"], "zorluk": "orta"},
    {"kelime": "özgün baskı yapmak", "aciklama": "litografi veya gravür plakasını mürekkepleyip pres makinesinde basmak", "yasakli_kelimeler": ["gravür", "litografi", "pres makinesi", "mürekkep", "plaka"], "zorluk": "orta"},
    {"kelime": "lavi tekniğiyle boyamak", "aciklama": "tek renk çini mürekkebini suyla açarak açıktan koyuya tonlar elde etmek", "yasakli_kelimeler": ["çini mürekkebi", "sulandırma", "tek renk", "ton derecesi", "fırça"], "zorluk": "orta"},
    {"kelime": "glaze katmanı atmak", "aciklama": "alttaki rengi kapatmadan yarı şeffaf yağlı boya tabakasıyla derinlik vermek", "yasakli_kelimeler": ["şeffaf sır", "velatura", "derinlik", "yarı saydam", "katman"], "zorluk": "orta"},
    {"kelime": "akrilik dökmek", "aciklama": "akışkan akrilik boyaları tuvale döküp hücre desenleri oluşturmak", "yasakli_kelimeler": ["pouring", "akışkan boya", "silikon yağı", "hücre efekti", "dökme"], "zorluk": "orta"},
    {"kelime": "guajla matlaştırmak", "aciklama": "kapatıcı ve opak su bazlı guaj boyayla pürüzsüz düz renk yüzeyleri boyamak", "yasakli_kelimeler": ["guaj", "opak", "kapatıcı su bazlı", "mat", "düz renk"], "zorluk": "orta"},
    {"kelime": "fiksatif püskürtmek", "aciklama": "pastel ve karakalem resmin dökülmemesi için üzerine sabitleyici sprey sıkmak", "yasakli_kelimeler": ["sabitleyici sprey", "pastel", "karakalem dökülmesi", "koruma spreyi", "püskürtme"], "zorluk": "orta"},
    {"kelime": "puanlama yapmak", "aciklama": "seurat'nın noktacılık akımında olduğu gibi binlerce renkli noktayı yan yana dizmek", "yasakli_kelimeler": ["noktacılık", "pointilizm", "seurat", "noktalar", "optik karışım"], "zorluk": "orta"},
    {"kelime": "kolaj yapıştırmak", "aciklama": "gazete kupürleri, fotoğraflar ve kumaş parçalarını tuvale yapıştırıp kompozisyon kurmak", "yasakli_kelimeler": ["yapıştırma", "gazete kupürü", "fotoğraf", "kesip yapıştırma", "kübizm"], "zorluk": "orta"},
    {"kelime": "fırça izi bırakmak", "aciklama": "van gogh gibi boyayı kalın sürüp dinamik ve kaba fırça darbelerini görünür kılmak", "yasakli_kelimeler": ["van gogh", "kaba darbe", "dokulu yüzey", "tuş", "ifade"], "zorluk": "orta"},
    {"kelime": "fresk sıvamak", "aciklama": "ıslak kireç sıvalı duvara pigment boyalarla kilise duvar resmi yapmak", "yasakli_kelimeler": ["ıslak kireç", "duvar resmi", "sıva", "kilise", "pigment"], "zorluk": "orta"},
    {"kelime": "tonlama cetveli çıkarmak", "aciklama": "en açıktan en koyu siyaha kadar 9 basamaklı gri değer cetveli hazırlamak", "yasakli_kelimeler": ["gri skalası", "değer skalası", "açık koyu", "basamak", "karakalem"], "zorluk": "orta"},
    {"kelime": "portre oranlamak", "aciklama": "gözlerin, burnun ve ağzın baş yüksekliğine göre oranlarını ölçüp çizmek", "yasakli_kelimeler": ["yüz oranları", "göz burun ağız", "portre çizimi", "üçte bir kuralı", "baş yüksekliği"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "alla prima bitirmek", "aciklama": "yağlı boyayı alt katmanların kurumasını beklemeden tek seansta ıslak üstüne ıslak tamamlamak", "yasakli_kelimeler": ["ıslak üstüne ıslak", "tek seans", "wet on wet", "hızlı boyama", "katmansız"], "zorluk": "zor"},
    {"kelime": "trompe l'oeil aldatmacası", "aciklama": "duvarda öyle gerçekçi pencere veya niş çizmek ki gözün gerçek sanması", "yasakli_kelimeler": ["göz aldatmacası", "üç boyut illüzyonu", "hiperrealizm", "gerçek gibi", "derinlik yanılsaması"], "zorluk": "zor"},
    {"kelime": "enkaustik balmumu eritmek", "aciklama": "antik mısır fayyum portrelerindeki gibi sıcak eritilmiş balmumu ve pigmentle boyamak", "yasakli_kelimeler": ["fayyum portreleri", "eritilmiş balmumu", "sıcak mum", "antik teknik", "mum boyama"], "zorluk": "zor"},
    {"kelime": "grisailles altlığı sermek", "aciklama": "renklere geçmeden önce tüm tabloyu sadece gri-monokrom tonlarla modellemek", "yasakli_kelimeler": ["monokrom altlık", "gri tonlar", "değer modelleme", "klasik atölye", "alt resim"], "zorluk": "zor"},
    {"kelime": "altın varak yapıştırmak", "aciklama": "ikonanın veya tablonun zeminine mikron kalınlığında saf altın yaprakları mühürlemek", "yasakli_kelimeler": ["varak", "saf altın", "mühre", "ikona zemini", "yaprak altın"], "zorluk": "zor"},
    {"kelime": "anamorfik deformasyon", "aciklama": "resmi öyle çarpıtarak çizmek ki sadece belirli açılı aynadan bakınca düzgün görünmesi", "yasakli_kelimeler": ["holbein elçiler", "çarpık perspektif", "açılı bakış", "gizli kafatası", "optik deformasyon"], "zorluk": "zor"},
    {"kelime": "pentimento izi yakalamak", "aciklama": "x ışını altında tablonun altındaki ressamın vazgeçtiği eski çizim katmanlarını bulmak", "yasakli_kelimeler": ["x ışını incelemesi", "ressamın pişmanlığı", "alttaki çizim", "vazgeçilen figür", "tabaka"], "zorluk": "zor"},
    {"kelime": "impasto dokusu yığmak", "aciklama": "boyayı tuval üstüne heykelsi kabartma oluşturacak kadar kalın yığmak", "yasakli_kelimeler": ["kalın yığma", "kabartma boya", "heykelsi", "yoğun katman", "ağır doku"], "zorluk": "zor"},
    {"kelime": "damlatma eylemi yapmak", "aciklama": "pollock gibi boya kutusunu delip yere serili tuvalin üstünde dans ederek gezdirmek", "yasakli_kelimeler": ["action painting", "jackson pollock", "drip", "yer tuvali", "otomatizm"], "zorluk": "zor"},
    {"kelime": "frottage tekniğiyle sürtmek", "aciklama": "max ernst gibi pürüzlü ahşap veya taş zemin üstündeki kağıdı kurşunla karalayıp doku çıkarmak", "yasakli_kelimeler": ["sürtme tekniği", "max ernst", "sürrealizm", "yüzey dokusu", "karalama"], "zorluk": "zor"},
    {"kelime": "grattage ile kazımak", "aciklama": "kurumamış kalın boya katmanlarını jilet veya tarakla kazıyarak alt renkleri çıkarmak", "yasakli_kelimeler": ["kazıma", "jilet", "tarak", "alt katman", "sürrealist doku"], "zorluk": "zor"},
    {"kelime": "sfumato ton geçişi yapmak", "aciklama": "ışık ve gölgenin sınırlarını mikron fırça dokunuşlarıyla tamamen buğulandırmak", "yasakli_kelimeler": ["buğulu geçiş", "kenar yumuşatma", "duman efekti", "leonardo tekniği", "kontursuz"], "zorluk": "zor"},
    {"kelime": "cire perdue bronz dökmek", "aciklama": "ressamın yaptığı balmumu modelin erimesiyle yerine erimiş bronz akıtmak", "yasakli_kelimeler": ["kayıp mum", "bronz döküm", "balmumu model", "döküm kalıbı", "metal heykel"], "zorluk": "zor"},
    {"kelime": "renk alanları boyamak", "aciklama": "mark rothko gibi devasa tuvalleri sadece meditasyonel düz renk bloklarıyla kaplamak", "yasakli_kelimeler": ["color field", "mark rothko", "renk blokları", "meditatif", "büyük monokrom"], "zorluk": "zor"}
]

retorik_verbs = [
    # Kolay (12)
    {"kelime": "konuşmak", "aciklama": "düşüncelerini sesli sözcüklerle dinleyicilere aktarmak", "yasakli_kelimeler": ["söz", "ses", "anlatmak", "dinleyici", "kelime"], "zorluk": "kolay"},
    {"kelime": "ikna etmek", "aciklama": "etkili sözlerle karşı tarafın fikrini ve tutumunu değiştirmek", "yasakli_kelimeler": ["inandırmak", "fikir", "değiştirmek", "karşı taraf", "söz"], "zorluk": "kolay"},
    {"kelime": "savunmak", "aciklama": "kendi tezini ve doğrusunu mantıklı delillerle korumak", "yasakli_kelimeler": ["tez", "delil", "korumak", "iddia", "ispat"], "zorluk": "kolay"},
    {"kelime": "anlatmak", "aciklama": "bir konuyu örnekler ve detaylarla topluluğa açıklamak", "yasakli_kelimeler": ["açıklamak", "örnek", "konu", "topluluk", "bilgi"], "zorluk": "kolay"},
    {"kelime": "tartışmak", "aciklama": "farklı görüşteki iki kişinin bir konu üzerinde karşılıklı konuşması", "yasakli_kelimeler": ["münazara", "karşılıklı", "görüş", "fikir ayrılığı", "tez antitez"], "zorluk": "kolay"},
    {"kelime": "hitap etmek", "aciklama": "kürsüden salondaki kalabalığa doğru seslenmek", "yasakli_kelimeler": ["kürsü", "kalabalık", "seslenmek", "salon", "topluluk"], "zorluk": "kolay"},
    {"kelime": "soru sormak", "aciklama": "dinleyicinin dikkatini çekmek veya bilgi almak için soru yöneltmek", "yasakli_kelimeler": ["soru", "yöneltmek", "cevap", "merak", "dikkat"], "zorluk": "kolay"},
    {"kelime": "vurgulamak", "aciklama": "cümledeki en önemli kelimeyi ses tonunu yükselterek belirtmek", "yasakli_kelimeler": ["ses tonu", "önemli", "altını çizmek", "belirtmek", "kelime"], "zorluk": "kolay"},
    {"kelime": "övmek", "aciklama": "bir kişiyi veya fikri güzel sözlerle yüceltip takdir etmek", "yasakli_kelimeler": ["medhetmek", "takdir", "yüceltmek", "güzel söz", "iltifat"], "zorluk": "kolay"},
    {"kelime": "eleştirmek", "aciklama": "yanlış veya eksik görülen fikirlerin hatalarını yüzüne söylemek", "yasakli_kelimeler": ["tenkit", "hata", "eksik", "kusur", "karşı çıkmak"], "zorluk": "kolay"},
    {"kelime": "etkilemek", "aciklama": "güzel ve coşkulu konuşmayla dinleyicilerin kalbini fethetmek", "yasakli_kelimeler": ["coşku", "kalp", "tesir", "büyülemek", "iz bırakmak"], "zorluk": "kolay"},
    {"kelime": "susturmak", "aciklama": "verdiği ezici cevapla rakibin konuşamayacak hale gelmesi", "yasakli_kelimeler": ["cevap", "rakip", "kapak yapmak", "laf", "ezici"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "hitabet yapmak", "aciklama": "kürsüde vücut dili ve ses tonuyla kitleleri coşturan nutuk atmak", "yasakli_kelimeler": ["oratory", "nutuk", "kitle", "vücut dili", "coşku"], "zorluk": "orta"},
    {"kelime": "metafor kullanmak", "aciklama": "anlatımı güçlendirmek için kavramlar arasında derin benzetmeler kurmak", "yasakli_kelimeler": ["mecaz", "benzetme", "istiare", "kavram", "aktarım"], "zorluk": "orta"},
    {"kelime": "retorik soru sormak", "aciklama": "cevap beklemeksizin dinleyiciyi düşündürmek ve mesajı vurgulamak için sormak", "yasakli_kelimeler": ["cevap beklemeyen", "düşündürme", "soru", "söz sanatı", "istifham"], "zorluk": "orta"},
    {"kelime": "tez çürütmek", "aciklama": "rakibin sunduğu argümanın mantık hatalarını ve zayıflıklarını ispatlamak", "yasakli_kelimeler": ["çürütme", "antitez", "mantık hatası", "argüman", "zayıflık"], "zorluk": "orta"},
    {"kelime": "delil sunmak", "aciklama": "iddiasını kanıtlamak için istatistik, bilimsel rapor veya tanık göstermek", "yasakli_kelimeler": ["kanıt", "istatistik", "ispat", "tanık", "belge"], "zorluk": "orta"},
    {"kelime": "münazara kazanmak", "aciklama": "jüri önündeki fikir yarışmasında savunduğu tezi daha iyi anlatıp galip gelmek", "yasakli_kelimeler": ["jüri", "fikir yarışı", "puan", "hükümet muhalefet", "galibiyet"], "zorluk": "orta"},
    {"kelime": "coşku uyandırmak", "aciklama": "duygusal sözler ve yükselen ses tonuyla salonda alkış tufanı koparmak", "yasakli_kelimeler": ["pathos", "heyecan", "alkış", "duygu seli", "galeyan"], "zorluk": "orta"},
    {"kelime": "söz hakkı almak", "aciklama": "oturum başkanından parmak kaldırarak konuşma sırası talep etmek", "yasakli_kelimeler": ["moderatör", "oturum başkanı", "sıra", "talep", "konuşma izni"], "zorluk": "orta"},
    {"kelime": "diyalektik yürütmek", "aciklama": "tez ve antitez çatışmasından daha üst bir sentez doğruya ulaşmak", "yasakli_kelimeler": ["tez antitez sentez", "hegel", "çatışma", "akıl yürütme", "doğruluk"], "zorluk": "orta"},
    {"kelime": "ironi yapmak", "aciklama": "söylenen sözün tam tersini kastederek ince bir alayla durumu yermek", "yasakli_kelimeler": ["tersini kastetme", "ince alay", "kinaye", "mizah", "alay"], "zorluk": "orta"},
    {"kelime": "abartmak", "aciklama": "mesajın etkisini artırmak için durumu olduğundan bin kat büyük göstermek", "yasakli_kelimeler": ["mübalağa", "hiperbol", "büyütmek", "aşırı", "kat kat"], "zorluk": "orta"},
    {"kelime": "tekrara başvurmak", "aciklama": "cümle başlarında aynı kelimeyi yineleyerek ritmik baskı kurmak", "yasakli_kelimeler": ["anafora", "yineleme", "ritim", "cümle başı", "tekrar"], "zorluk": "orta"},
    {"kelime": "teşhis ve intak yapmak", "aciklama": "cansız nesnelere veya hayvanlara insan kişiliği verip onları konuşturmak", "yasakli_kelimeler": ["kişileştirme", "konuşturma", "fabl", "insan özelliği", "sanat"], "zorluk": "orta"},
    {"kelime": "örnek olay aktarmak", "aciklama": "soyut teorik konuyu somutlaştırmak için yaşanmış kısa bir hikaye anlatmak", "yasakli_kelimeler": ["anektod", "vaka", "yaşanmış hikaye", "kıssa", "somut örnek"], "zorluk": "orta"},
    {"kelime": "sessizliği kullanmak", "aciklama": "vurucu bir cümleden sonra 3 saniye susarak dinleyicinin sindirmesini sağlamak", "yasakli_kelimeler": ["duraklama", "es vermek", "susma", "vurgulu sessizlik", "bekleme"], "zorluk": "orta"},
    {"kelime": "göz teması kurmak", "aciklama": "salondaki dinleyicilerin gözlerinin içine tek tek bakarak samimiyet vermek", "yasakli_kelimeler": ["bakış", "gözün içine", "samimiyet", "güven", "tarama"], "zorluk": "orta"},
    {"kelime": "beden dilini yönetmek", "aciklama": "açık el hareketleri ve dik duruşla kendine güvenen hatip imajı çizmek", "yasakli_kelimeler": ["jest mimik", "el hareketleri", "duruş", "hatip", "özgüven"], "zorluk": "orta"},
    {"kelime": "lafı dolandırmak", "aciklama": "asıl söylenmesi gereken cevabı vermemek için konudan uzak laflar etmek", "yasakli_kelimeler": ["gevelemek", "uzatmak", "konudan sapma", "kaçamak", "cevap vermeme"], "zorluk": "orta"},
    {"kelime": "demagoji yapmak", "aciklama": "halkın duygularını ve önyargılarını sömürerek gerçeği saptırmak", "yasakli_kelimeler": ["halk dalkavukluğu", "önyargı sömürüsü", "popülizm", "saptırma", "duygu istismarı"], "zorluk": "orta"},
    {"kelime": "paradoks öne sürmek", "aciklama": "ilk bakışta çelişkili ve mantıksız görünen ama derin bir gerçek barındıran ifade", "yasakli_kelimeler": ["çelişki", "mantıksız görünen", "ikilem", "derin anlam", "şaşırtma"], "zorluk": "orta"},
    {"kelime": "antitez üretmek", "aciklama": "ortaya atılan bir savın tam zıttı olan karşı savı oluşturmak", "yasakli_kelimeler": ["karşı sav", "zıt fikir", "tez karşıtı", "çelişki", "sentez öncesi"], "zorluk": "orta"},
    {"kelime": "özdeyiş alıntılamak", "aciklama": "sözünün gücünü artırmak için ünlü bir düşünürün vecizesini aktarmak", "yasakli_kelimeler": ["vecize", "aforizma", "düşünür sözü", "alıntı", "otorite"], "zorluk": "orta"},
    {"kelime": "nüans yakalamak", "aciklama": "iki yakın anlamlı kavram arasındaki çok ince anlam farkını ortaya koymak", "yasakli_kelimeler": ["ince fark", "ayrıntı", "anlam farkı", "kavram", "detay"], "zorluk": "orta"},
    {"kelime": "kapanış konuşması yapmak", "aciklama": "tüm anlatılanları özetleyip vurucu bir çağrıyla konuşmayı bitirmek", "yasakli_kelimeler": ["peroration", "özet", "son söz", "çağrı", "bitiriş"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "ethos-pathos-logos dengesi", "aciklama": "aristoteles'in hatibin karakteri, duygu uyandırma ve mantıksal kanıt üçgenini kurmak", "yasakli_kelimeler": ["aristoteles", "karakter güveni", "duygu mantık", "retorik üçgeni", "ikna sanatı"], "zorluk": "zor"},
    {"kelime": "sofist mantığı işletmek", "aciklama": "doğruluktan ziyade kelime oyunları ve göreli argümanlarla her tezi savunabilmek", "yasakli_kelimeler": ["sofizm", "görecelik", "kelime oyunu", "protagoras", "kandırmaca"], "zorluk": "zor"},
    {"kelime": "ad hominem yapmak", "aciklama": "tartışılan fikre cevap vermek yerine doğrudan konuşmacının kişiliğine saldırmak", "yasakli_kelimeler": ["kişiliğe saldırı", "safsata", "fallacy", "konuyu saptırma", "karalama"], "zorluk": "zor"},
    {"kelime": "korkuluk safsatası kurmak", "aciklama": "rakibin argümanını aşırı basitleştirip çarpıtarak kolayca çürütmek", "yasakli_kelimeler": ["straw man", "saman adam", "çarpıtma", "abartılı sav", "safsata"], "zorluk": "zor"},
    {"kelime": "entimem kurgulamak", "aciklama": "öncüllerden birinin herkesçe bilindiği varsayılarak gizlendiği örtük kıyas", "yasakli_kelimeler": ["örtük kıyas", "eksik öncül", "mantık çıkarımı", "varsayım", "kısaltılmış tasım"], "zorluk": "zor"},
    {"kelime": "aporia durumuna düşürmek", "aciklama": "sokratik sorgulamayla karşı tarafı içinden çıkılmaz çözümsüz çelişki çıkmazına sokmak", "yasakli_kelimeler": ["çıkmaz", "çözümsüzlük", "sokrates", "şaşkınlık", "çelişki"], "zorluk": "zor"},
    {"kelime": "maieutik ile doğurtmak", "aciklama": "sokratik yöntemle muhatabın zihnindeki saklı doğru bilgiyi soru sorarak açığa çıkarmak", "yasakli_kelimeler": ["doğurtma sanatı", "sokratik yöntem", "saklı bilgi", "soruyla öğretme", "ebelik"], "zorluk": "zor"},
    {"kelime": "kairosu yakalamak", "aciklama": "sözü söylemek için en doğru, en uygun ve geri dönülmez tarihi anı seçmek", "yasakli_kelimeler": ["uygun zaman", "fırsat anı", "doğru an", "zamanlama", "antik yunan"], "zorluk": "zor"},
    {"kelime": "chiasmus çaprazlaması yapmak", "aciklama": "ilk cümledeki kelime dizilişini ikinci cümlede a-b-b-a şeklinde tersine çevirmek", "yasakli_kelimeler": ["çaprazlama", "abba", "ters çevirme", "söz simetrisi", "figür"], "zorluk": "zor"},
    {"kelime": "kırmızı ringa balığı taktiği", "aciklama": "dikkatleri asıl can alıcı sorundan uzaklaştırmak için alakasız sansasyonel konu atmak", "yasakli_kelimeler": ["red herring", "hedef saptırma", "alakasız konu", "dikkat dağıtma", "safsata"], "zorluk": "zor"},
    {"kelime": "tavuk-yumurta döngüselliği", "aciklama": "iddianın doğruluğunu yine iddia edilen önermeye dayandıran kısır döngü safsatası", "yasakli_kelimeler": ["petitio principii", "kısır döngü", "döngüsel akıl yürütme", "önermeyi kanıtlama", "safsata"], "zorluk": "zor"},
    {"kelime": "oxymoron bağlamak", "aciklama": "birbiriyle tamamen zıt anlamlı iki kelimeyi yan yana getirip sarsıcı derinlik yaratmak", "yasakli_kelimeler": ["zıtlık birleşimi", "yaşayan ölü", "çelişkili ifade", "sessiz çığlık", "edebi sanat"], "zorluk": "zor"},
    {"kelime": "slippery slope argümanı", "aciklama": "küçük bir adımın felaketler zincirine yol açacağını mantıksızca iddia eden kaygan zemin safsatası", "yasakli_kelimeler": ["kaygan zemin", "felaket zinciri", "safsata", "abartılı sonuç", "korku yayma"], "zorluk": "zor"},
    {"kelime": "epistemik cüret sergilemek", "aciklama": "bilgi temeli olmadan mutlak otorite gibi konuşup dinleyiciyi baskılamak", "yasakli_kelimeler": ["bilgi temelsiz", "otoriter dil", "cüret", "baskılama", "dogmatizm"], "zorluk": "zor"}
]

if __name__ == "__main__":
    add_and_save_verbs("resim", resim_verbs)
    add_and_save_verbs("retorik", retorik_verbs)
