# -*- coding: utf-8 -*-
from card_utils import add_and_save_verbs

muzikoloji_verbs = [
    # Kolay (12)
    {"kelime": "bestelemek", "aciklama": "yeni bir müzik eseri ve ezgi yaratmak", "yasakli_kelimeler": ["nota", "ezgi", "şarkı", "besteci", "yaratmak"], "zorluk": "kolay"},
    {"kelime": "dinlemek", "aciklama": "müzikal sesleri ve ritimleri kulak vererek takip etmek", "yasakli_kelimeler": ["kulak", "ses", "şarkı", "ezgi", "işitmek"], "zorluk": "kolay"},
    {"kelime": "çalmak", "aciklama": "bir müzik aletini kullanarak ses üretmek", "yasakli_kelimeler": ["enstrüman", "alet", "piyano", "gitar", "ses"], "zorluk": "kolay"},
    {"kelime": "söylemek", "aciklama": "şarkı sözlerini vokal ve melodiyle seslendirmek", "yasakli_kelimeler": ["şarkı", "vokal", "ses", "söz", "koro"], "zorluk": "kolay"},
    {"kelime": "kaydetmek", "aciklama": "icra edilen müziği stüdyoda ses bandına veya dijitale aktarmak", "yasakli_kelimeler": ["stüdyo", "ses", "mikrofon", "kayıt", "albüm"], "zorluk": "kolay"},
    {"kelime": "notaya almak", "aciklama": "duyulan ezgiyi porte üzerine nota işaretleriyle dökmek", "yasakli_kelimeler": ["porte", "nota", "sol anahtarı", "yazmak", "kağıt"], "zorluk": "kolay"},
    {"kelime": "akort etmek", "aciklama": "çalgı tellerini doğru ses frekansına ayarlamak", "yasakli_kelimeler": ["tel", "düzen", "ses", "kulak", "ton"], "zorluk": "kolay"},
    {"kelime": "ritim tutmak", "aciklama": "müziğin vuruşlarına el veya ayakla eşlik etmek", "yasakli_kelimeler": ["vuruş", "tempo", "el çırpmak", "metronom", "eşlik"], "zorluk": "kolay"},
    {"kelime": "derlemek", "aciklama": "yörelerdeki anonim halk türkülerini köylerden toplayıp kaydetmek", "yasakli_kelimeler": ["türkü", "halk", "anonim", "yöre", "toplamak"], "zorluk": "kolay"},
    {"kelime": "incelemek", "aciklama": "müzik tarihini, makamları veya bestecilerin eserlerini araştırmak", "yasakli_kelimeler": ["araştırma", "analiz", "eser", "tarih", "müzikolog"], "zorluk": "kolay"},
    {"kelime": "sınıflandırmak", "aciklama": "müzik aletlerini telli, üflemeli veya vurmalı olarak gruplamak", "yasakli_kelimeler": ["grup", "telli", "üflemeli", "vurmalı", "tür"], "zorluk": "kolay"},
    {"kelime": "öğretmek", "aciklama": "konservatuvarda nota ve enstrüman dersi vermek", "yasakli_kelimeler": ["konservatuvar", "hoca", "ders", "eğitim", "öğrenci"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "transkripsiyon yapmak", "aciklama": "bir çalgı için yazılmış eseri başka çalgıya uyarlayıp notalamak", "yasakli_kelimeler": ["uyarlama", "notasyon", "çalgı", "düzenleme", "aktarma"], "zorluk": "orta"},
    {"kelime": "partisyon okumak", "aciklama": "tüm orkestra çalgılarının aynı anda çaldığı büyük notayı takip etmek", "yasakli_kelimeler": ["orkestra", "şef", "büyük nota", "takip", "çalgılar"], "zorluk": "orta"},
    {"kelime": "armonize etmek", "aciklama": "tek sesli bir melodiye uyumlu akorlar ve çok seslilik eklemek", "yasakli_kelimeler": ["akor", "çok seslilik", "armoni", "melodi", "uyum"], "zorluk": "orta"},
    {"kelime": "makam tahlili yapmak", "aciklama": "türk müziği eserinin dizi, güçlü ve karar perdelerini incelemek", "yasakli_kelimeler": ["karar sesi", "güçlü", "seyir", "perde", "dizi"], "zorluk": "orta"},
    {"kelime": "seyir takip etmek", "aciklama": "makamın inici mi çıkıcı mı gezindiğini notalarda izlemek", "yasakli_kelimeler": ["inici", "çıkıcı", "gezinme", "ezgi", "makam"], "zorluk": "orta"},
    {"kelime": "arşiv taramak", "aciklama": "eski taş plakları ve nota yazmalarını kütüphanede araştırmak", "yasakli_kelimeler": ["taş plak", "yazma", "kütüphane", "tarihi", "belge"], "zorluk": "orta"},
    {"kelime": "organoloji çalışmak", "aciklama": "müzik aletlerinin tarihsel gelişimini ve yapısını araştırmak", "yasakli_kelimeler": ["çalgı bilimi", "enstrüman", "yapı", "akustik", "tarih"], "zorluk": "orta"},
    {"kelime": "etnomüzikoloji yapmak", "aciklama": "müziği ait olduğu kültürün antropolojik bağlamı içinde incelemek", "yasakli_kelimeler": ["kültür", "antropoloji", "saha araştırması", "toplum", "gelenek"], "zorluk": "orta"},
    {"kelime": "solfej yapmak", "aciklama": "notaları isimleri, ses yükseklikleri ve süreleriyle okumak", "yasakli_kelimeler": ["bona", "süre", "ses yüksekliği", "okuma", "kulak eğitimi"], "zorluk": "orta"},
    {"kelime": "dikte yazmak", "aciklama": "piyanodan çalınan melodiyi sadece duyarak anında notaya dökmek", "yasakli_kelimeler": ["işitme", "duyma", "anında", "yazmak", "kulak"], "zorluk": "orta"},
    {"kelime": "analiz etmek", "aciklama": "senfoninin form yapısını ve tema gelişimini çözümlemek", "yasakli_kelimeler": ["form", "sonat", "tema", "yapı", "çözümleme"], "zorluk": "orta"},
    {"kelime": "polifoni kurgulamak", "aciklama": "birbirinden bağımsız melodik hatları aynı anda örmek", "yasakli_kelimeler": ["çok seslilik", "kontrpuan", "melodi hattı", "bağımsız", "kanon"], "zorluk": "orta"},
    {"kelime": "ses frekansı ölçmek", "aciklama": "herz cinsinden diyapazon veya cihazla perde frekansını bulmak", "yasakli_kelimeler": ["hertz", "diyapazon", "440", "frekans", "titreşim"], "zorluk": "orta"},
    {"kelime": "modülasyon yapmak", "aciklama": "parçanın ortasında bir tondan veya makamdan diğerine geçmek", "yasakli_kelimeler": ["ton değiştirme", "geçiş", "makam", "tonalite", "akor"], "zorluk": "orta"},
    {"kelime": "usul vurmak", "aciklama": "türk müziğinde dizlere ellerle vurarak ritmik kalıbı icra etmek", "yasakli_kelimeler": ["düm tek", "diz", "ritim", "kudüm", "kalıp"], "zorluk": "orta"},
    {"kelime": "arpej basmak", "aciklama": "akorun seslerini aynı anda değil sırayla tek tek çalmak", "yasakli_kelimeler": ["akor", "sırayla", "kırık akor", "gitar", "piyano"], "zorluk": "orta"},
    {"kelime": "koroya eşlik etmek", "aciklama": "piyano veya orkestrayla çok sesli koroyu desteklemek", "yasakli_kelimeler": ["koro", "eşlik", "soprano", "korrepetitör", "ses"], "zorluk": "orta"},
    {"kelime": "orkestrasyon yazmak", "aciklama": "piyano taslağını yaylılar, üflemeliler ve vurmalılara paylaştırmak", "yasakli_kelimeler": ["çalgılama", "yaylılar", "şef", "parti", "paylaştırma"], "zorluk": "orta"},
    {"kelime": "kadans yapmak", "aciklama": "müzik cümlesinin sonundaki bitiş akor dizilimini bağlamak", "yasakli_kelimeler": ["bitiş", "cümle sonu", "çözülme", "akor dizilimi", "tam kadans"], "zorluk": "orta"},
    {"kelime": "kontrpuan yazmak", "aciklama": "nota notaya kuralına göre yatay çok sesli örgü oluşturmak", "yasakli_kelimeler": ["füg", "yatay", "nota karşı nota", "bach", "kural"], "zorluk": "orta"},
    {"kelime": "doğaçlama yapmak", "aciklama": "önceden yazılmış nota olmadan o an içinden geldiğince çalmak", "yasakli_kelimeler": ["emprovizasyon", "taksim", "caz", "o anda", "içten"], "zorluk": "orta"},
    {"kelime": "tınıyı ayırt etmek", "aciklama": "aynı notayı çalan flüt ile kemanın ses rengini kulağıyla tanımak", "yasakli_kelimeler": ["ses rengi", "flüt", "keman", "harmonik", "karakter"], "zorluk": "orta"},
    {"kelime": "güfte yazmak", "aciklama": "beste yapılmak üzere şiir formunda şarkı sözü kaleme almak", "yasakli_kelimeler": ["söz", "şarkı", "şiir", "bestekar", "vezin"], "zorluk": "orta"},
    {"kelime": "dinamikleri belirtmek", "aciklama": "notanın altına forte, piyano veya kreşendo işaretleri koymak", "yasakli_kelimeler": ["forte", "piyano", "crescendo", "gürlük", "ses seviyesi"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "paleografi okumak", "aciklama": "orta çağ neuma notalarını veya eski elyazması müzik metinlerini çözmek", "yasakli_kelimeler": ["neuma", "eski yazı", "elyazması", "orta çağ", "çözümleme"], "zorluk": "zor"},
    {"kelime": "mikrotonalite uygulamak", "aciklama": "yarım sesten daha küçük koma aralıklarını kullanarak müzik üretmek", "yasakli_kelimeler": ["koma", "çeyrek ses", "aralık", "türk müziği", "bölüntü"], "zorluk": "zor"},
    {"kelime": "dodekafoni bestelemek", "aciklama": "schoenberg'in 12 ton dizisi sistemine göre atonal eser yazmak", "yasakli_kelimeler": ["12 ton", "schoenberg", "atonal", "seri", "tonsuz"], "zorluk": "zor"},
    {"kelime": "spektral müzik analizi", "aciklama": "sesin akustik dalga boyu ve harmonik tayfını bilgisayarla incelemek", "yasakli_kelimeler": ["tayf", "harmonik", "frekans grafiği", "akustik", "bilgisayar"], "zorluk": "zor"},
    {"kelime": "kantus firmus kurmak", "aciklama": "orta çağ polifonisinde eserin temeli olan değişmez sabit ezgiyi yerleştirmek", "yasakli_kelimeler": ["sabit ezgi", "temel melodi", "orta çağ", "polifoni", "rönesans"], "zorluk": "zor"},
    {"kelime": "akustik empedansı hesaplamak", "aciklama": "çalgı borusundaki hava sütununun ses dalgasına gösterdiği direnci ölçmek", "yasakli_kelimeler": ["hava sütunu", "direnç", "dalga", "çalgı yapımı", "rezonans"], "zorluk": "zor"},
    {"kelime": "diyatonik modları türetmek", "aciklama": "doryen, frigyen veya lidyen gibi kilise modlarını kurmak", "yasakli_kelimeler": ["kilise modu", "doryen", "frigyen", "lidyen", "gam"], "zorluk": "zor"},
    {"kelime": "aleatorik kurgu yapmak", "aciklama": "müzik akışında bazı bölümleri icracının rastlantısal seçimine bırakmak", "yasakli_kelimeler": ["rastlantısal", "şans", "john cage", "çağdaş", "belirsizlik"], "zorluk": "zor"},
    {"kelime": "monodi geliştirmek", "aciklama": "erken barokta tek sesli vokal hattına continuo akor eşliği yazmak", "yasakli_kelimeler": ["basso continuo", "barok", "tek ses", "vokal", "erken"], "zorluk": "zor"},
    {"kelime": "izoritmik motet örmek", "aciklama": "ars nova döneminde ritmik kalıp talea ile melodi color'u eşleştirmek", "yasakli_kelimeler": ["talea", "color", "ars nova", "motet", "orta çağ"], "zorluk": "zor"},
    {"kelime": "akustik tını analizi yapmak", "aciklama": "çalgının üst tonlar dizisindeki formant bölgelerini grafikle çıkarmak", "yasakli_kelimeler": ["formant", "üst tonlar", "spektrogram", "tını", "harmonik"], "zorluk": "zor"},
    {"kelime": "hermeneutik yorumlamak", "aciklama": "bestecinin müzikal şifrelerini ve metafizik anlam dünyasını felsefi okumak", "yasakli_kelimeler": ["yorumbilim", "felsefe", "anlam", "metafor", "bağlam"], "zorluk": "zor"},
    {"kelime": "tonaliteyi askıya almak", "aciklama": "kromatizm ve disonans akorlarla eserin merkez ton hissini yok etmek", "yasakli_kelimeler": ["atonal", "kromatik", "disonans", "merkez", "çözülmeme"], "zorluk": "zor"},
    {"kelime": "entonomatoloji çalışmak", "aciklama": "yöresel halk müziği türlerinin ve terimlerinin etimolojisini araştırmak", "yasakli_kelimeler": ["terim", "etimoloji", "halk müziği", "dilbilim", "köken"], "zorluk": "zor"}
]

nanoteknoloji_verbs = [
    # Kolay (12)
    {"kelime": "küçültmek", "aciklama": "malzemeleri nanometre ölçeğine kadar boyutça ufaltmak", "yasakli_kelimeler": ["ufaltmak", "boyut", "ölçek", "nano", "mikro"], "zorluk": "kolay"},
    {"kelime": "sentezlemek", "aciklama": "laboratuvarda nano boyutta yeni kimyasal partiküller üretmek", "yasakli_kelimeler": ["üretmek", "kimyasal", "laboratuvar", "partikül", "reaksiyon"], "zorluk": "kolay"},
    {"kelime": "büyütmek", "aciklama": "elektron mikroskobuyla nano yapıları milyonlarca kat görünür kılmak", "yasakli_kelimeler": ["mikroskop", "görsel", "milyon kat", "mercek", "görüntü"], "zorluk": "kolay"},
    {"kelime": "kaplamak", "aciklama": "yüzeyleri su itici nano film tabakasıyla örtmek", "yasakli_kelimeler": ["film", "tabaka", "su itici", "örtmek", "yüzey"], "zorluk": "kolay"},
    {"kelime": "incelemek", "aciklama": "nano malzemelerin atomik dizilimini cihazlarla gözlemlemek", "yasakli_kelimeler": ["atom", "cihaz", "gözlem", "yapı", "analiz"], "zorluk": "kolay"},
    {"kelime": "taşımak", "aciklama": "ilaç moleküllerini nano kapsüllerle doğrudan kanserli hücreye iletmek", "yasakli_kelimeler": ["ilaç", "kapsül", "kanser", "hücre", "hedef"], "zorluk": "kolay"},
    {"kelime": "karıştırmak", "aciklama": "polimer içine karbon nanotüp ekleyip homojen dağıtmak", "yasakli_kelimeler": ["polimer", "dağılım", "kompozit", "nanotüp", "homojen"], "zorluk": "kolay"},
    {"kelime": "ölçmek", "aciklama": "üretilen parçacıkların nanometre cinsinden çapını hesaplamak", "yasakli_kelimeler": ["çap", "nanometre", "boyut", "ölçüm", "cihaz"], "zorluk": "kolay"},
    {"kelime": "saflaştırmak", "aciklama": "sentez sonrası nano partikülleri kimyasal kalıntılardan arındırmak", "yasakli_kelimeler": ["arınma", "kalıntı", "saf", "temizleme", "filtre"], "zorluk": "kolay"},
    {"kelime": "üretmek", "aciklama": "endüstriyel ölçekte grafen veya nano gümüş imal etmek", "yasakli_kelimeler": ["grafen", "gümüş", "imalat", "endüstri", "madde"], "zorluk": "kolay"},
    {"kelime": "entegre etmek", "aciklama": "nano sensörleri mikroçip devrelerinin içine yerleştirmek", "yasakli_kelimeler": ["çip", "devre", "sensör", "elektronik", "yerleşim"], "zorluk": "kolay"},
    {"kelime": "test etmek", "aciklama": "nano kompozit malzemenin kırılma ve iletkenlik dayanımını denemek", "yasakli_kelimeler": ["dayanım", "iletkenlik", "mukavemet", "deney", "kırılma"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "kendi kendine birleşmek", "aciklama": "moleküllerin dış müdahale olmadan kendiliğinden düzenli nano desen kurması", "yasakli_kelimeler": ["self assembly", "kendiliğinden", "düzen", "molekül", "termodinamik"], "zorluk": "orta"},
    {"kelime": "fonksiyonelleştirmek", "aciklama": "nanotüp yüzeyine hedef hücreyi tanıyan kimyasal gruplar bağlamak", "yasakli_kelimeler": ["bağlama", "grup", "yüzey modifikasyonu", "ligand", "hedefleme"], "zorluk": "orta"},
    {"kelime": "sol-jel yapmak", "aciklama": "sıvı çözeltiyi jel fazına geçirip fırınlayarak nano seramik üretmek", "yasakli_kelimeler": ["çözelti", "jel", "fırınlama", "seramik", "hidroliz"], "zorluk": "orta"},
    {"kelime": "buhar fazında büyütmek", "aciklama": "gaz halindeki öncülleri sıcak yüzeyde reaksiyona sokup nano tel büyütmek", "yasakli_kelimeler": ["cvd", "gaz", "buhar", "yüzey", "büyütme"], "zorluk": "orta"},
    {"kelime": "litografi ile işlemek", "aciklama": "ışık veya elektron demetiyle silikon tabakaya nanometrik kanallar oymak", "yasakli_kelimeler": ["silikon", "oyma", "elektron demeti", "maske", "çip"], "zorluk": "orta"},
    {"kelime": "nanotüp sarmak", "aciklama": "tek atom kalınlığındaki grafen tabakasını silindirik tüp haline getirmek", "yasakli_kelimeler": ["grafen", "silindir", "karbon", "tek atom", "tüp"], "zorluk": "orta"},
    {"kelime": "hidrofobik kılmak", "aciklama": "lotus çiçeği etkisi yaratan nano pürüzlerle yüzeyi su tutmaz yapmak", "yasakli_kelimeler": ["lotus", "su tutmaz", "ıslanmaz", "kontakt açısı", "damla"], "zorluk": "orta"},
    {"kelime": "ilaç kapsüllemek", "aciklama": "kemoterapi ilacını lipozom nano küresi içine hapsetmek", "yasakli_kelimeler": ["lipozom", "kemoterapi", "kapsülleme", "salım", "hedefli"], "zorluk": "orta"},
    {"kelime": "yüzey alanını artırmak", "aciklama": "tanecik boyutunu küçülterek birim gram başına düşen temas yüzeyini katlamak", "yasakli_kelimeler": ["alan", "hacim oranı", "reaktivite", "katalizör", "boyut"], "zorluk": "orta"},
    {"kelime": "elektro-eğirme yapmak", "aciklama": "yüksek voltajlı elektrik alanında polimer çözeltisinden nano lif çekmek", "yasakli_kelimeler": ["elektrospinning", "lif", "voltaj", "polimer", "iplik"], "zorluk": "orta"},
    {"kelime": "manyetik yönlendirmek", "aciklama": "dış manyetik alan uygulayarak manyetik nano parçacıkları damarda yürütmek", "yasakli_kelimeler": ["manyetik alan", "demir oksit", "damar", "yönlendirme", "mıknatıs"], "zorluk": "orta"},
    {"kelime": "afm ile taramak", "aciklama": "atomik kuvvet mikroskobunun nano iğnesiyle atomik topoğrafyayı hissetmek", "yasakli_kelimeler": ["afm", "iğne", "topoğrafya", "kuvvet", "konsol"], "zorluk": "orta"},
    {"kelime": "sem ile görüntülemek", "aciklama": "taramalı elektron mikroskobuyla numuneden 3 boyutlu nano görüntü almak", "yasakli_kelimeler": ["sem", "elektron", "taramalı", "görüntü", "vakum"], "zorluk": "orta"},
    {"kelime": "tem ile kesit almak", "aciklama": "geçirimli elektron mikroskobunda elektronları numunenin içinden geçirmek", "yasakli_kelimeler": ["tem", "geçirimli", "iç yapı", "atomik çözünürlük", "ince kesit"], "zorluk": "orta"},
    {"kelime": "katalizör olarak kullanmak", "aciklama": "nano altın parçacıklarıyla kimyasal reaksiyonun hızını binlerce kat artırmak", "yasakli_kelimeler": ["reaksiyon hızı", "kataliz", "altın", "aktivasyon", "yüzey"], "zorluk": "orta"},
    {"kelime": "kümelenmeyi önlemek", "aciklama": "nano parçacıkların birbirine yapışıp topaklanmasını sürfaktanla engellemek", "yasakli_kelimeler": ["aglomerasyon", "topaklanma", "sürfaktan", "stabilizasyon", "zeta potansiyeli"], "zorluk": "orta"},
    {"kelime": "biyouyumluluk sağlamak", "aciklama": "vücuda verilecek nano malzemenin zehirli etki ve bağışıklık tepkisi vermemesini sağlamak", "yasakli_kelimeler": ["sitotoksisite", "vücut", "bağışıklık", "toksik", "uyum"], "zorluk": "orta"},
    {"kelime": "fototermal etki yaratmak", "aciklama": "kızılötesi lazerle nano altın çubukları ısıtıp tümör hücresini yakmak", "yasakli_kelimeler": ["lazer", "ısıtma", "altın çubuk", "tümör", "ablasyon"], "zorluk": "orta"},
    {"kelime": "nano gözenek delmek", "aciklama": "grafen membran üzerinde tekil dna ipliğinin geçebileceği delik açmak", "yasakli_kelimeler": ["nanopor", "dna dizileme", "membran", "delik", "geçiş"], "zorluk": "orta"},
    {"kelime": "fotokataliz yapmak", "aciklama": "titanyum dioksit nano kaplamanın güneş ışığıyla havadaki kirleticileri parçalaması", "yasakli_kelimeler": ["tio2", "titanyum", "ışık", "parçalama", "kendi kendini temizleyen"], "zorluk": "orta"},
    {"kelime": "kuantum noktası parlatmak", "aciklama": "yarı iletken nano kristalin boyutuna göre farklı saf renklerde ışık yayması", "yasakli_kelimeler": ["quantum dot", "flüoresan", "qled", "yarı iletken", "ışık yayma"], "zorluk": "orta"},
    {"kelime": "kontrollü salım yapmak", "aciklama": "nano kapsülün ilacı ph veya sıcaklık değişimiyle zamana yayarak bırakması", "yasakli_kelimeler": ["salım", "ph duyarlı", "zaman", "bırakma", "kapsül"], "zorluk": "orta"},
    {"kelime": "grafen pulcuk dökmek", "aciklama": "grafit katmanlarını ultrasonik banyoda sıvı fazda soyup tek katmanlara ayırmak", "yasakli_kelimeler": ["grafit", "pulcuk", "ultrasonik", "soyma", "eksfoliasyon"], "zorluk": "orta"},
    {"kelime": "nano jeneratör kurmak", "aciklama": "piezoelektrik çinko oksit nano tellerle vücut hareketinden elektrik üretmek", "yasakli_kelimeler": ["piezoelektrik", "hareket", "elektrik", "çinko oksit", "enerji hasadı"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "atomik katman kaplamak", "aciklama": "yüzeye gaz öncülleriyle her döngüde tam bir atom kalınlığında film sermek", "yasakli_kelimeler": ["ald", "tek atom katmanı", "döngü", "homojen", "öncül"], "zorluk": "zor"},
    {"kelime": "plazmonik rezonans yakalamak", "aciklama": "metal nano parçacık yüzeyindeki serbest elektronların ışıkla ortak salınımı", "yasakli_kelimeler": ["yüzey plazmon", "salınım", "rezonans", "ışık saçılması", "soğurma"], "zorluk": "zor"},
    {"kelime": "kuantum hapsetmesi oluşturmak", "aciklama": "elektron hareketini nano boyuta sıkıştırarak enerji bant aralığını değiştirmek", "yasakli_kelimeler": ["quantum confinement", "bant aralığı", "elektron", "dalga fonksiyonu", "boyut etkisi"], "zorluk": "zor"},
    {"kelime": "dna origami katlamak", "aciklama": "uzun tek iplikli dna zincirini kısa zımba dizileriyle 2 ve 3 boyutlu nano formlara bükmek", "yasakli_kelimeler": ["dna origami", "zımba iplik", "katlama", "nano yapı", "kurgu"], "zorluk": "zor"},
    {"kelime": "moleküler motor çevirmek", "aciklama": "ışık veya kimyasal enerjiyle tek yönde dönen sentetik moleküler çark yapmak", "yasakli_kelimeler": ["moleküler makine", "feringa", "dönme", "çark", "nanorobot"], "zorluk": "zor"},
    {"kelime": "kuantum tünelleme ölçmek", "aciklama": "taramalı tünelleme mikroskobunda iğne ile yüzey arası akan tünelleme akımını izlemek", "yasakli_kelimeler": ["stm", "tünelleme akımı", "iğne ucu", "dalga", "atomik çözünürlük"], "zorluk": "zor"},
    {"kelime": "dipsiz potansiyel kuyusu açmak", "aciklama": "yarı iletken arayüzeylerde 2 boyutlu elektron gazı hapsi oluşturmak", "yasakli_kelimeler": ["potansiyel kuyusu", "2deg", "arayüz", "yarı iletken", "hapsolma"], "zorluk": "zor"},
    {"kelime": "zeta potansiyeli ölçmek", "aciklama": "nano süspansiyondaki partiküllerin kayma düzlemi elektrostatik yükünü saptamak", "yasakli_kelimeler": ["kayma düzlemi", "elektrostatik", "stabilite", "kolloid", "yük"], "zorluk": "zor"},
    {"kelime": "süperparamanyetik faza geçmek", "aciklama": "ferromanyetik parçacıkların nano boyuta inince kalıcı mıknatıslığını yitirmesi", "yasakli_kelimeler": ["mıknatıslanma", "histerezis", "ferromanyetik", "sıcaklık", "manyetik moment"], "zorluk": "zor"},
    {"kelime": "foster rezonans enerji aktarımı", "aciklama": "nano boyuttaki iki florofor arasında ışımasız dipol-dipol enerji transferi", "yasakli_kelimeler": ["fret", "florofor", "ışımasız", "mesafe", "donör akseptör"], "zorluk": "zor"},
    {"kelime": "spin kapısı anahtarlamak", "aciklama": "nano manyetik tünel ekleminde elektron spin yönüne göre direnci değiştirmek", "yasakli_kelimeler": ["spintronik", "spin", "mram", "tünel direnci", "manyetodirenç"], "zorluk": "zor"},
    {"kelime": "kirallik tayini yapmak", "aciklama": "karbon nanotüpün balıksırtı, koltuk veya kiral indeksini (n,m) belirlemek", "yasakli_kelimeler": ["kiral indeks", "armchair", "zigzag", "vektör", "iletkenlik"], "zorluk": "zor"},
    {"kelime": "top-down litografi oymak", "aciklama": "büyük külçe silikondan nano boyuta doğru aşındırarak yonga deseni çıkarmak", "yasakli_kelimeler": ["yukarıdan aşağı", "aşındırma", "yonga", "fotolitografi", "silikon"], "zorluk": "zor"},
    {"kelime": "bottom-up moleküler dizmek", "aciklama": "tek tek atomları ve molekülleri kimyasal çekimle birleştirip üst yapı kurmak", "yasakli_kelimeler": ["aşağıdan yukarı", "kimyasal sentez", "moleküler", "inşa", "kendiliğinden"], "zorluk": "zor"}
]

if __name__ == "__main__":
    add_and_save_verbs("muzikoloji", muzikoloji_verbs)
    add_and_save_verbs("nanoteknoloji", nanoteknoloji_verbs)
