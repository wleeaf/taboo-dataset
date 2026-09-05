# -*- coding: utf-8 -*-
from card_utils import add_and_save_verbs

mevsimler_verbs = [
    # Kolay (12)
    {"kelime": "yaprak dökmek", "aciklama": "ağaçların sonbaharda sararan yapraklarını bırakması", "yasakli_kelimeler": ["sonbahar", "ağaç", "sarı", "düşmek", "güz"], "zorluk": "kolay"},
    {"kelime": "çiçek açmak", "aciklama": "bitkilerin ilkbaharda renkli tomurcuklarını patlatması", "yasakli_kelimeler": ["ilkbahar", "bahar", "tomurcuk", "renk", "dal"], "zorluk": "kolay"},
    {"kelime": "kar yağmak", "aciklama": "kış mevsiminde beyaz tanelerin yere inmesi", "yasakli_kelimeler": ["kış", "beyaz", "soğuk", "tane", "yağış"], "zorluk": "kolay"},
    {"kelime": "güneşlenmek", "aciklama": "yazın sıcak havada sahilde güneş ışığı almak", "yasakli_kelimeler": ["yaz", "güneş", "kumsal", "bronzlaşmak", "sıcak"], "zorluk": "kolay"},
    {"kelime": "yüzmek", "aciklama": "yaz aylarında serinlemek için denize veya havuza girmek", "yasakli_kelimeler": ["deniz", "havuz", "yaz", "serinlemek", "su"], "zorluk": "kolay"},
    {"kelime": "üşümek", "aciklama": "kışın soğuk hava sebebiyle titremek", "yasakli_kelimeler": ["soğuk", "kış", "titremek", "mont", "donmak"], "zorluk": "kolay"},
    {"kelime": "terlemek", "aciklama": "yaz sıcağında vücudun su atması", "yasakli_kelimeler": ["yaz", "sıcak", "su", "bunaltı", "hararet"], "zorluk": "kolay"},
    {"kelime": "hasat etmek", "aciklama": "yaz sonu veya sonbaharda olgunlaşan ekinleri toplamak", "yasakli_kelimeler": ["ekin", "tarla", "toplamak", "ürün", "buğday"], "zorluk": "kolay"},
    {"kelime": "budamak", "aciklama": "kış sonunda ağaçların kuru dallarını kesip gençleştirmek", "yasakli_kelimeler": ["dal", "ağaç", "makas", "kesmek", "bahçe"], "zorluk": "kolay"},
    {"kelime": "fidan dikmek", "aciklama": "ilkbaharda toprağa yeni genç ağaç yerleştirmek", "yasakli_kelimeler": ["toprak", "ağaç", "bahar", "dikim", "bahçe"], "zorluk": "kolay"},
    {"kelime": "soba yakmak", "aciklama": "kış aylarında evi ısıtmak için odun kömür tutuşturmak", "yasakli_kelimeler": ["kış", "odun", "kömür", "ısınmak", "ateş"], "zorluk": "kolay"},
    {"kelime": "serinlemek", "aciklama": "yaz sıcağında gölgeye geçip veya soğuk içecekle ferahlamak", "yasakli_kelimeler": ["sıcak", "gölge", "ferahlamak", "yaz", "soğuk"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "kış uykusuna yatmak", "aciklama": "ayı ve bazı hayvanların kışı uyuyarak geçirmesi", "yasakli_kelimeler": ["ayı", "uyku", "kış", "mağara", "hayvan"], "zorluk": "orta"},
    {"kelime": "göç etmek", "aciklama": "kuşların sonbaharda sıcak güney ülkelerine uçması", "yasakli_kelimeler": ["kuş", "sıcak", "güney", "uçmak", "sonbahar"], "zorluk": "orta"},
    {"kelime": "yeşermek", "aciklama": "baharın gelmesiyle kırların ve ağaçların taze yeşil renge bürünmesi", "yasakli_kelimeler": ["bahar", "yeşil", "çimen", "doğa", "canlanmak"], "zorluk": "orta"},
    {"kelime": "sararmak", "aciklama": "sonbaharda yeşil yaprakların sarı ve kızıla dönmesi", "yasakli_kelimeler": ["sonbahar", "yaprak", "sarı", "solmak", "ağaç"], "zorluk": "orta"},
    {"kelime": "cemre düşmek", "aciklama": "bahar öncesi havaya, suya ve toprağa sıcaklık inmesi", "yasakli_kelimeler": ["hava", "su", "toprak", "bahar", "sıcaklık"], "zorluk": "orta"},
    {"kelime": "ekin ekmek", "aciklama": "sonbaharda tohumları tarlaya serpip toprağa gömmek", "yasakli_kelimeler": ["tohum", "tarla", "çiftçi", "buğday", "toprak"], "zorluk": "orta"},
    {"kelime": "bağ bozumu yapmak", "aciklama": "sonbaharda üzüm bağlarındaki olgun salkımları toplamak", "yasakli_kelimeler": ["üzüm", "bağ", "sonbahar", "salkım", "pekmez"], "zorluk": "orta"},
    {"kelime": "tohum saçmak", "aciklama": "bahar aylarında toprağa yeni bitki tohumları serpmek", "yasakli_kelimeler": ["tohum", "bahçe", "ekim", "toprak", "serpmek"], "zorluk": "orta"},
    {"kelime": "buz tutmak", "aciklama": "dondurucu kış soğuğunda göl ve derelerin yüzeyinin sertleşmesi", "yasakli_kelimeler": ["buz", "göl", "dere", "kış", "don"], "zorluk": "orta"},
    {"kelime": "kardan adam yapmak", "aciklama": "kışın yağan taze karları yuvarlayıp figür oluşturmak", "yasakli_kelimeler": ["kar", "havuç", "kömür", "figür", "çocuk"], "zorluk": "orta"},
    {"kelime": "kayak yapmak", "aciklama": "kış sezonunda dağlardaki karlı pistlerden aşağı kaymak", "yasakli_kelimeler": ["pist", "kar", "dağ", "kış", "kayak"], "zorluk": "orta"},
    {"kelime": "turşu kurmak", "aciklama": "sonbaharda kış için sebzeleri kavanozda tuzlu suya basmak", "yasakli_kelimeler": ["kavanoz", "sirke", "tuz", "sebze", "kış"], "zorluk": "orta"},
    {"kelime": "salça kaynatmak", "aciklama": "yaz sonunda domates ve biberleri kaynatıp kışlık hazırlamak", "yasakli_kelimeler": ["domates", "biber", "kazan", "kışlık", "yaz"], "zorluk": "orta"},
    {"kelime": "yün örmek", "aciklama": "kış ayları gelmeden kazak, atkı ve bere hazırlamak", "yasakli_kelimeler": ["şiş", "ip", "atkı", "bere", "kazak"], "zorluk": "orta"},
    {"kelime": "tarhana sermek", "aciklama": "yaz sıcağında yoğurtlu hamuru bezler üzerine yayıp kurutmak", "yasakli_kelimeler": ["güneş", "kurutmak", "bez", "çorba", "kışlık"], "zorluk": "orta"},
    {"kelime": "gardırop yenilemek", "aciklama": "mevsim geçişinde yazlık ve kışlık kıyafetleri değiştirmek", "yasakli_kelimeler": ["yazlık", "kışlık", "dolap", "kıyafet", "geçiş"], "zorluk": "orta"},
    {"kelime": "güneşten yanmak", "aciklama": "yaz sıcağında uzun süre kalarak ciltte kızarıklık ve acı oluşması", "yasakli_kelimeler": ["kızarıklık", "cilt", "bronz", "güneş kremi", "acı"], "zorluk": "orta"},
    {"kelime": "zemheri yaşamak", "aciklama": "kışın en şiddetli ve dondurucu kırk gününü geçirmek", "yasakli_kelimeler": ["karakış", "ayaz", "ocak", "dondurucu", "soğuk"], "zorluk": "orta"},
    {"kelime": "hıdırellez kutlamak", "aciklama": "baharın gelişini ve tabiatın uyanışını mayıs başında karşılamak", "yasakli_kelimeler": ["bahar", "mayıs", "ateş", "dilek", "şenlik"], "zorluk": "orta"},
    {"kelime": "pastırma yazı yaşamak", "aciklama": "kasım ayında birkaç gün süren beklenmedik sıcak hava dönemi", "yasakli_kelimeler": ["kasım", "sonbahar", "sıcak", "güneş", "kısa"], "zorluk": "orta"},
    {"kelime": "don vurmak", "aciklama": "baharda erken açan meyve çiçeklerinin gece ayazında yanması", "yasakli_kelimeler": ["meyve", "çiçek", "ayaz", "soğuk", "ürün"], "zorluk": "orta"},
    {"kelime": "çiy birikmek", "aciklama": "bahar ve yaz sabahları nemin otlar üstünde damlalaşması", "yasakli_kelimeler": ["sabah", "damla", "ot", "nem", "yaprak"], "zorluk": "orta"},
    {"kelime": "kırkikindi yağmak", "aciklama": "ilkbahar sonu öğleden sonraları düzenli yağan konvektif yağmurlar", "yasakli_kelimeler": ["ikindi", "ilkbahar", "sağanak", "yağmur", "anadolu"], "zorluk": "orta"},
    {"kelime": "kuraklık çekmek", "aciklama": "yaz aylarında hiç yağmur yağmaması sebebiyle su sıkıntısı yaşamak", "yasakli_kelimeler": ["yağmur", "su", "baraj", "kıtlık", "tarla"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "ekinoks yaşanmak", "aciklama": "gece ve gündüz sürelerinin eşitlendiği mevsimsel dönüm noktası", "yasakli_kelimeler": ["gece", "gündüz", "eşitlik", "mart", "eylül"], "zorluk": "zor"},
    {"kelime": "gün dönümü olmak", "aciklama": "güneş ışınlarının dönencelere dik gelip en uzun veya kısa günün oluşması", "yasakli_kelimeler": ["solstis", "21 haziran", "21 aralık", "en uzun", "gündüz"], "zorluk": "zor"},
    {"kelime": "fotoperiyodizmi hissetmek", "aciklama": "bitkilerin gün ışığı süresine göre çiçeklenme zamanını ayarlaması", "yasakli_kelimeler": ["ışık", "süre", "biyolojik saat", "çiçeklenme", "gün"], "zorluk": "zor"},
    {"kelime": "fenolojik gözlem yapmak", "aciklama": "canlıların mevsimsel iklim olaylarına göre gelişim evrelerini kaydetmek", "yasakli_kelimeler": ["evre", "yapraklanma", "iklim", "periyot", "takvim"], "zorluk": "zor"},
    {"kelime": "vernalizasyon geçirmek", "aciklama": "tohumun çiçek açabilmesi için kış soğuğuna maruz kalma ihtiyacı", "yasakli_kelimeler": ["soğuklama", "tohum", "kış", "çiçeklenme", "buğday"], "zorluk": "zor"},
    {"kelime": "diyapoz durumuna girmek", "aciklama": "böceklerin olumsuz kış koşullarında metabolizmasını duraklatması", "yasakli_kelimeler": ["böcek", "kışlama", "durgunluk", "metabolizma", "larva"], "zorluk": "zor"},
    {"kelime": "estivasyon yapmak", "aciklama": "bazı hayvanların aşırı yaz sıcağı ve kuraklığında yaz uykusuna yatması", "yasakli_kelimeler": ["yaz uykusu", "kuraklık", "sıcak", "çöl", "salyangoz"], "zorluk": "zor"},
    {"kelime": "yaprak dökmeyi tetiklemek", "aciklama": "azalan gün ışığıyla absisik asit salgılayıp yaprak sapını zayıflatmak", "yasakli_kelimeler": ["absisik asit", "hormon", "sonbahar", "hücre", "kopma"], "zorluk": "zor"},
    {"kelime": "çığ riski oluşmak", "aciklama": "ilkbaharda ısınan havanın dik yamaçlardaki kar tabakasını kaydırması", "yasakli_kelimeler": ["yamaç", "kar kütlesi", "kayma", "dağ", "tehlike"], "zorluk": "zor"},
    {"kelime": "termal şok geçirmek", "aciklama": "canlının mevsimin ani sıcaklık dalgalanmalarına uyum sağlayamaması", "yasakli_kelimeler": ["ani", "ısı değişimi", "stres", "bitki", "don"], "zorluk": "zor"},
    {"kelime": "albedo etkisi değişmek", "aciklama": "kar örtüsünün erimesiyle yeryüzünün güneş ışığını yansıtma oranının düşmesi", "yasakli_kelimeler": ["yansıma", "kar", "güneş", "yüzey", "erime"], "zorluk": "zor"},
    {"kelime": "muson döngüsüne girmek", "aciklama": "kara ve denizlerin mevsimsel ısınma farkıyla yön değiştiren dev rüzgarlar", "yasakli_kelimeler": ["hint", "yaz", "yağmur", "rüzgar", "kıta"], "zorluk": "zor"},
    {"kelime": "klorofil sentezini durdurmak", "aciklama": "sonbaharda soğuyan havayla bitkilerin yeşil pigment üretimini kesmesi", "yasakli_kelimeler": ["yeşil", "pigment", "fotosentez", "karotenoid", "yaprak"], "zorluk": "zor"},
    {"kelime": "tabakalaşma çözülmek", "aciklama": "ilkbahar ve sonbaharda göl sularının sıcaklık farkıyla alt-üst karışması", "yasakli_kelimeler": ["göl", "termoklin", "karışım", "su", "yoğunluk"], "zorluk": "zor"}
]

mikrobiyoloji_verbs = [
    # Kolay (12)
    {"kelime": "üremek", "aciklama": "bakterilerin besiyerinde bölünerek sayıca çoğalması", "yasakli_kelimeler": ["çoğalmak", "bakteri", "bölünmek", "hücre", "sayı"], "zorluk": "kolay"},
    {"kelime": "bulaşmak", "aciklama": "mikrobun bir kişiden veya eşyadan diğerine geçmesi", "yasakli_kelimeler": ["enfeksiyon", "hasta", "temas", "geçmek", "mikrop"], "zorluk": "kolay"},
    {"kelime": "incelemek", "aciklama": "mikroskop altında mikroorganizmaları gözlemlemek", "yasakli_kelimeler": ["mikroskop", "mercek", "gözlem", "bakteri", "büyütmek"], "zorluk": "kolay"},
    {"kelime": "mayalamak", "aciklama": "maya mantarlarıyla hamur veya sütü fermente etmek", "yasakli_kelimeler": ["maya", "yoğurt", "hamur", "fermantasyon", "mantar"], "zorluk": "kolay"},
    {"kelime": "boyamak", "aciklama": "bakterileri mikroskopta ayırt etmek için özel kimyasal damlatmak", "yasakli_kelimeler": ["gram", "renk", "mikroskop", "lam", "metilen mavisi"], "zorluk": "kolay"},
    {"kelime": "ekim yapmak", "aciklama": "öze yardımıyla petrideki agara mikroorganizma yaymak", "yasakli_kelimeler": ["öze", "petri", "agar", "besiyeri", "yaymak"], "zorluk": "kolay"},
    {"kelime": "steril etmek", "aciklama": "ortamdaki tüm canlı mikropları ve sporları yok etmek", "yasakli_kelimeler": ["otoklav", "arıtmak", "mikrop", "temiz", "yok etmek"], "zorluk": "kolay"},
    {"kelime": "dezenfekte etmek", "aciklama": "cansız yüzeylerdeki hastalık yapıcı mikropları kimyasalla temizlemek", "yasakli_kelimeler": ["alkol", "yüzey", "çamaşır suyu", "temizlik", "mikrop"], "zorluk": "kolay"},
    {"kelime": "hastalandırmak", "aciklama": "patojen mikrobun vücuda girip hastalık tablosu oluşturması", "yasakli_kelimeler": ["patojen", "enfeksiyon", "semptom", "ateş", "mikrop"], "zorluk": "kolay"},
    {"kelime": "küflenmek", "aciklama": "nemli gıdalar üzerinde küf mantarı sporlarının kolonileşmesi", "yasakli_kelimeler": ["ekmek", "mantar", "spor", "yeşil", "bozulmak"], "zorluk": "kolay"},
    {"kelime": "bölünmek", "aciklama": "tek bir bakteri hücresinin ikiye ayrılarak çoğalması", "yasakli_kelimeler": ["ikiye", "çoğalma", "bakteri", "hücre", "fisyon"], "zorluk": "kolay"},
    {"kelime": "ayırt etmek", "aciklama": "morfolojik ve biyokimyasal özelliklerine göre bakteri türünü bulmak", "yasakli_kelimeler": ["tanımlamak", "tür", "teşhis", "cins", "fark"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "koloni oluşturmak", "aciklama": "agar yüzeyinde tek bir hücreden gözle görülür bakteri topluluğu oluşması", "yasakli_kelimeler": ["agar", "petri", "topluluk", "üreme", "popülasyon"], "zorluk": "orta"},
    {"kelime": "inkübe etmek", "aciklama": "mikrop ekili petrileri etüvde belirli sıcaklıkta bekletmek", "yasakli_kelimeler": ["etüv", "sıcaklık", "37 derece", "bekletmek", "üreme"], "zorluk": "orta"},
    {"kelime": "pastörize etmek", "aciklama": "sütü belirli sıcaklığa kadar ısıtıp hızla soğutarak patojenleri öldürmek", "yasakli_kelimeler": ["süt", "ısıtma", "patojen", "soğutma", "besin"], "zorluk": "orta"},
    {"kelime": "otoklavlamak", "aciklama": "basınçlı buhar altında 121 derecede aletleri ve besiyerlerini sterilize etmek", "yasakli_kelimeler": ["buhar", "basınç", "121 derece", "sterilizasyon", "cihaz"], "zorluk": "orta"},
    {"kelime": "antibiyotik duyarlılık testi", "aciklama": "bakterinin hangi ilaca karşı hassas olduğunu diskerle belirlemek", "yasakli_kelimeler": ["antibiyogram", "disk", "direnç", "zon", "ilaç"], "zorluk": "orta"},
    {"kelime": "spor oluşturmak", "aciklama": "bakterinin olumsuz çevre koşullarına karşı dayanıklı kılıf yapması", "yasakli_kelimeler": ["endospor", "dayanıklı", "kapsül", "kurtulma", "basil"], "zorluk": "orta"},
    {"kelime": "fermente etmek", "aciklama": "oksijensiz ortamda şekeri alkol veya aside dönüştürmek", "yasakli_kelimeler": ["oksijensiz", "asit", "alkol", "glikoliz", "maya"], "zorluk": "orta"},
    {"kelime": "biyofilm oluşturmak", "aciklama": "bakterilerin yüzeylere yapışarak sümüksü koruyucu tabaka kurması", "yasakli_kelimeler": ["kateter", "tabaka", "yapışma", "koruma", "matriks"], "zorluk": "orta"},
    {"kelime": "direnç kazanmak", "aciklama": "bakterilerin mutasyon veya plazmitle antibiyotiklerden etkilenmez olması", "yasakli_kelimeler": ["rezistans", "antibiyotik", "gen", "mutasyon", "etkisiz"], "zorluk": "orta"},
    {"kelime": "fagosite edilmek", "aciklama": "akyuvar hücreleri tarafından mikrobun yutularak sindirilmesi", "yasakli_kelimeler": ["akyuvar", "makrofaj", "yutmak", "sindirmek", "bağışıklık"], "zorluk": "orta"},
    {"kelime": "toksin salgılamak", "aciklama": "bakterinin dokulara zarar veren zehirli proteinler üretmesi", "yasakli_kelimeler": ["zehir", "ekzotoksin", "endotoksin", "protein", "zarar"], "zorluk": "orta"},
    {"kelime": "hemoliz yapmak", "aciklama": "kanlı agardaki kırmızı kan hücrelerini parçalayıp rengini açmak", "yasakli_kelimeler": ["kanlı agar", "eritrosit", "alfa", "beta", "parçalamak"], "zorluk": "orta"},
    {"kelime": "santrifüjlemek", "aciklama": "tüpteki bakteri süspansiyonunu yüksek devirde çevirip çöktürmek", "yasakli_kelimeler": ["devir", "çökelti", "tüp", "süpernatant", "dönme"], "zorluk": "orta"},
    {"kelime": "plazmit aktarmak", "aciklama": "bakteriler arasında halkasal DNA parçası transfer etmek", "yasakli_kelimeler": ["halkasal", "dna", "transfer", "konjugasyon", "vektör"], "zorluk": "orta"},
    {"kelime": "besiyeri hazırlamak", "aciklama": "mikropların beslenmesi için gerekli amino asit ve agar karışımını eritmek", "yasakli_kelimeler": ["broth", "besin", "toz", "su", "otoklav"], "zorluk": "orta"},
    {"kelime": "virülans artmak", "aciklama": "bir patojenin hastalık yapabilme yeteneğinin ve şiddetinin yükselmesi", "yasakli_kelimeler": ["patojenite", "şiddet", "hastalık", "kapsül", "yetenek"], "zorluk": "orta"},
    {"kelime": "serolojik test yapmak", "aciklama": "kandaki antikor ve antijen birleşmesini lamda gözlemlemek", "yasakli_kelimeler": ["antikor", "antijen", "aglütinasyon", "elisa", "serum"], "zorluk": "orta"},
    {"kelime": "lam-lamel arası yapmak", "aciklama": "sıvı mikrop damlasını iki ince cam arasına koyup mikroskoba sürmek", "yasakli_kelimeler": ["cam", "damla", "inceleme", "preparat", "mikroskop"], "zorluk": "orta"},
    {"kelime": "kriyoprezervasyon yapmak", "aciklama": "saf bakteri kültürlerini gliserolle eksi 80 derecede dondurup saklamak", "yasakli_kelimeler": ["dondurucu", "eksi 80", "gliserol", "saklama", "kültür"], "zorluk": "orta"},
    {"kelime": "virüs konakçıya tutunmak", "aciklama": "viral reseptörlerin hedef hücre zarına kilitlenmesi", "yasakli_kelimeler": ["reseptör", "bağlanma", "hücre zarı", "enfeksiyon", "kapsid"], "zorluk": "orta"},
    {"kelime": "filtre etmek", "aciklama": "ısıya duyarlı sıvıları 0.22 mikronluk membran filtreden süzmek", "yasakli_kelimeler": ["membran", "0.22 mikron", "süzmek", "steril", "gözenek"], "zorluk": "orta"},
    {"kelime": "kapsül sentezlemek", "aciklama": "bakterinin fagositozdan kaçmak için dışına polisakkarit zırh örmesi", "yasakli_kelimeler": ["polisakkarit", "zırh", "koruma", "fagositoz", "tabaka"], "zorluk": "orta"},
    {"kelime": "gaz kromatografisiyle analiz", "aciklama": "bakteri hücre duvarı yağ asitlerini ayrıştırıp teşhis koymak", "yasakli_kelimeler": ["yağ asidi", "kromatografi", "cihaz", "analiz", "pik"], "zorluk": "orta"},
    {"kelime": "saf kültür elde etmek", "aciklama": "karışık mikrop örneğinden tek bir türe ait izolat yakalamak", "yasakli_kelimeler": ["izolat", "tek", "saf", "koloni", "ayırma"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "konjugasyon yapmak", "aciklama": "iki bakterinin seks pilusu ile köprü kurup genetik materyal aktarması", "yasakli_kelimeler": ["pilus", "köprü", "plazmit", "yatay gen", "aktarım"], "zorluk": "zor"},
    {"kelime": "transformasyon geçirmek", "aciklama": "bakterinin ortamda serbest duran çıplak DNA parçasını içine alması", "yasakli_kelimeler": ["çıplak dna", "kompetan", "ortam", "alım", "rekombinasyon"], "zorluk": "zor"},
    {"kelime": "transdüksiyon olmak", "aciklama": "bakteriyofaj virüsü aracılığıyla bir bakteriden diğerine gen taşınması", "yasakli_kelimeler": ["bakteriyofaj", "faj", "virüs", "aracı", "gen transferi"], "zorluk": "zor"},
    {"kelime": "litik döngüye girmek", "aciklama": "faj virüsünün bakteri içinde çoğalıp hücreyi patlatarak dışarı çıkması", "yasakli_kelimeler": ["lizis", "patlama", "virüs", "kapsid", "çoğalma"], "zorluk": "zor"},
    {"kelime": "lizojenik faza geçmek", "aciklama": "viral genomun bakteri kromozomuna entegre olup profaj olarak uyuması", "yasakli_kelimeler": ["profaj", "entegrasyon", "kromozom", "sessiz", "genom"], "zorluk": "zor"},
    {"kelime": "kemotaksis göstermek", "aciklama": "kamçılı bakterinin kimyasal besin veya zehir konsantrasyonuna doğru yüzmesi", "yasakli_kelimeler": ["kamçı", "yönelme", "kimyasal", "gradyan", "hareket"], "zorluk": "zor"},
    {"kelime": "quorum sensing yapmak", "aciklama": "bakterilerin sinyal molekülleriyle popülasyon yoğunluğunu algılayıp ortak davranması", "yasakli_kelimeler": ["otoindükleyici", "sinyal", "popülasyon", "yoğunluk", "iletişim"], "zorluk": "zor"},
    {"kelime": "pcr ile amplifiye etmek", "aciklama": "mikroorganizmaya ait spesifik DNA dizisini tüpte milyonlarca kez çoğaltmak", "yasakli_kelimeler": ["polimeraz", "termal", "çoğaltma", "primer", "dna"], "zorluk": "zor"},
    {"kelime": "jel elektroforezi yürütmek", "aciklama": "bakteriyel DNA veya RNA parçalarını elektrik alanında büyüklüğüne göre ayırmak", "yasakli_kelimeler": ["agaroz", "akım", "bant", "elektrik", "boyut"], "zorluk": "zor"},
    {"kelime": "katalaz aktivitesi göstermek", "aciklama": "bakterinin toksik hidrojen peroksiti su ve oksijene parçalayarak köpürmesi", "yasakli_kelimeler": ["hidrojen peroksit", "köpük", "enzim", "oksijen", "gaz"], "zorluk": "zor"},
    {"kelime": "oksidaz reaksiyonu vermek", "aciklama": "sitokrom c oksidaz enzim varlığını reaktif damlatarak lacivert renkle saptamak", "yasakli_kelimeler": ["sitokrom", "solunum", "reaktif", "lacivert", "enzim"], "zorluk": "zor"},
    {"kelime": "fakültatif anaerop yaşamak", "aciklama": "hem oksijenli ortamda hem de oksijensiz ortamda üreyebilmek", "yasakli_kelimeler": ["oksijen", "anaerop", "solunum", "esnek", "üreme"], "zorluk": "zor"},
    {"kelime": "endotoksin şoku tetiklemek", "aciklama": "gram negatif bakterilerin lipopolisakkarit duvarıyla aşırı bağışıklık yanıtı doğurması", "yasakli_kelimeler": ["lipopolisakkarit", "gram negatif", "sepsis", "tansiyon", "şok"], "zorluk": "zor"},
    {"kelime": "beta laktamaz salgılamak", "aciklama": "penisilin ve sefalosporin antibiyotik halkasını kırarak ilacı etkisiz kılmak", "yasakli_kelimeler": ["penisilin", "enzim", "halka", "direnç", "hidroliz"], "zorluk": "zor"}
]

if __name__ == "__main__":
    add_and_save_verbs("mevsimler", mevsimler_verbs)
    add_and_save_verbs("mikrobiyoloji", mikrobiyoloji_verbs)
