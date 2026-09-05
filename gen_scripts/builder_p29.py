# -*- coding: utf-8 -*-
from card_utils import add_and_save_verbs

motor_sporlari_verbs = [
    # Kolay (12)
    {"kelime": "hızlanmak", "aciklama": "gaza basarak yarış aracının süratini artırmak", "yasakli_kelimeler": ["gaz", "sürat", "araç", "pedal", "basmak"], "zorluk": "kolay"},
    {"kelime": "fren yapmak", "aciklama": "viraja girmeden önce fren pedalına basıp yavaşlamak", "yasakli_kelimeler": ["pedal", "yavaşlamak", "viraj", "balata", "durmak"], "zorluk": "kolay"},
    {"kelime": "viraj almak", "aciklama": "pistteki kıvrımlı dönüşleri çizgiyi koruyarak dönmek", "yasakli_kelimeler": ["dönüş", "pist", "apeks", "direksiyon", "kıvrım"], "zorluk": "kolay"},
    {"kelime": "sollamak", "aciklama": "öndeki rakip yarış aracını geçerek pozisyon kazanmak", "yasakli_kelimeler": ["geçmek", "rakip", "atak", "pozisyon", "öndeki"], "zorluk": "kolay"},
    {"kelime": "kaymak", "aciklama": "aracın tekerleklerinin yol tutuşunu kaybedip yana kayması", "yasakli_kelimeler": ["spin", "lastik", "tutuş", "ıslak", "yanlama"], "zorluk": "kolay"},
    {"kelime": "kaza yapmak", "aciklama": "bariyerlere veya başka bir araca hızla çarpmak", "yasakli_kelimeler": ["çarpmak", "bariyer", "hasar", "araç", "enkaz"], "zorluk": "kolay"},
    {"kelime": "vites değiştirmek", "aciklama": "devir yükselince kulakçık veya vites koluyla oranı yükseltmek", "yasakli_kelimeler": ["devir", "kulakçık", "kol", "şanzıman", "debriyaj"], "zorluk": "kolay"},
    {"kelime": "kask takmak", "aciklama": "yarış öncesi başı korumak için vizörlü kask giymek", "yasakli_kelimeler": ["baş", "güvenlik", "vizör", "koruma", "giymek"], "zorluk": "kolay"},
    {"kelime": "yakıt almak", "aciklama": "pit stop sırasında depoya hızlıca yakıt doldurmak", "yasakli_kelimeler": ["pit", "benzin", "depo", "pompa", "dolum"], "zorluk": "kolay"},
    {"kelime": "lastik değiştirmek", "aciklama": "aşınan tekerlekleri pit ekibiyle saniyeler içinde yenilemek", "yasakli_kelimeler": ["pit", "tekerlek", "aşınma", "ekip", "saniye"], "zorluk": "kolay"},
    {"kelime": "tur bindirmek", "aciklama": "yavaş giden arkadaki araca tam bir tur fark atmak", "yasakli_kelimeler": ["tur", "fark", "arkadaki", "mavi bayrak", "geçmek"], "zorluk": "kolay"},
    {"kelime": "şampiyon olmak", "aciklama": "sezon sonunda en çok puanı toplayıp kupayı kaldırmak", "yasakli_kelimeler": ["kupa", "puan", "sezon", "birinci", "zafer"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "pit stop yapmak", "aciklama": "aracı pite sokup lastik ve kanat ayarı yaptırmak", "yasakli_kelimeler": ["pit alanı", "mekaniker", "servis", "lastik", "duraklama"], "zorluk": "orta"},
    {"kelime": "pole pozisyonu almak", "aciklama": "sıralama turlarında en hızlı turu atarak yarışa en önde başlamak", "yasakli_kelimeler": ["sıralama", "en hızlı", "ilk cep", "başlangıç", "turlar"], "zorluk": "orta"},
    {"kelime": "apeksi yakalamak", "aciklama": "virajın en iç tepe noktasına basarak en ideal çizgide dönmek", "yasakli_kelimeler": ["viraj içi", "çizgi", "tepe noktası", "bordür", "ideal"], "zorluk": "orta"},
    {"kelime": "drs açmak", "aciklama": "düzlükte arka kanadı açıp hava direncini kırarak hızlanmak", "yasakli_kelimeler": ["arka kanat", "düzlük", "fark", "hava direnci", "atak"], "zorluk": "orta"},
    {"kelime": "pist dışına taşmak", "aciklama": "frenajı kaçırarak çakıl havuzuna veya kaçış alanına çıkmak", "yasakli_kelimeler": ["çakıl havuzu", "kaçış alanı", "frenaj", "asfalt dışı", "taşma"], "zorluk": "orta"},
    {"kelime": "lastik ısıtmak", "aciklama": "formasyon turunda aracı sağa sola zikzak yaptırarak hamuru ısıtmak", "yasakli_kelimeler": ["hamur", "zikzak", "formasyon", "tutuş", "sıcaklık"], "zorluk": "orta"},
    {"kelime": "kerblere çıkmak", "aciklama": "viraj kenarlarındaki kırmızı beyaz tırtıklı yükseltilere basmak", "yasakli_kelimeler": ["bordür", "tırtık", "kırmızı beyaz", "kenar", "basmak"], "zorluk": "orta"},
    {"kelime": "aero paketi güncellemek", "aciklama": "aracın kanat ve taban aerodinami parçalarını yenilemek", "yasakli_kelimeler": ["aerodinamik", "kanat", "taban", "rüzgar tüneli", "parça"], "zorluk": "orta"},
    {"kelime": "güvenlik aracı girmek", "aciklama": "kaza sonrası pist temizlenirken araçların arkasında dizilmek", "yasakli_kelimeler": ["safety car", "kaza", "sarı bayrak", "lider", "yavaşlama"], "zorluk": "orta"},
    {"kelime": "telemetri okumak", "aciklama": "araçtaki yüzlerce sensörden gelen hız ve gaz verilerini incelemek", "yasakli_kelimeler": ["sensör", "veri", "grafik", "mühendis", "analiz"], "zorluk": "orta"},
    {"kelime": "undercut yapmak", "aciklama": "rakibinden bir tur önce pite girip taze lastikle öne geçmek", "yasakli_kelimeler": ["erken pit", "strateji", "taze lastik", "rakip", "geçiş"], "zorluk": "orta"},
    {"kelime": "overcut denemek", "aciklama": "rakip pite girdiğinde pistte temiz havada kalarak avantaj yakalamak", "yasakli_kelimeler": ["geç pit", "pistte kalmak", "temiz hava", "strateji", "avantaj"], "zorluk": "orta"},
    {"kelime": "lastik ufalanması", "aciklama": "lastik yüzeyinde küçük kauçuk parçacıklarının kopup tutuşu bozması", "yasakli_kelimeler": ["graining", "kauçuk", "aşınma", "tutuş", "kayma"], "zorluk": "orta"},
    {"kelime": "lastik kabarması", "aciklama": "aşırı sıcaklıktan lastik tabanında hava kabarcıkları patlaması", "yasakli_kelimeler": ["blistering", "kabarcık", "aşırı ısı", "taban", "hasar"], "zorluk": "orta"},
    {"kelime": "podyuma çıkmak", "aciklama": "yarışı ilk üçte bitirip şampanya patlatmak", "yasakli_kelimeler": ["ilk üç", "kürsü", "şampanya", "üçüncü", "ikinci"], "zorluk": "orta"},
    {"kelime": "ceza puanı almak", "aciklama": "pist sınırlarını ihlal ettiği veya temas yarattığı için komiserlerden ceza yemek", "yasakli_kelimeler": ["komiser", "süre cezası", "ihlal", "temas", "hakem"], "zorluk": "orta"},
    {"kelime": "start almak", "aciklama": "kırmızı ışıkların sönmesiyle gaza basıp yarışa fırlamak", "yasakli_kelimeler": ["ışıklar", "kalkış", "başlangıç", "debriyaj", "kırmızı"], "zorluk": "orta"},
    {"kelime": "telsizden konuşmak", "aciklama": "yarış mühendisiyle strateji ve araç durumu hakkında iletişim kurmak", "yasakli_kelimeler": ["radyo", "mühendis", "strateji", "iletişim", "pilot"], "zorluk": "orta"},
    {"kelime": "arkadan kaymak", "aciklama": "viraj ortasında arka tekerleklerin çekişi kaybetmesi", "yasakli_kelimeler": ["oversteer", "arka", "kopma", "direksiyon", "kontra"], "zorluk": "orta"},
    {"kelime": "önden kaymak", "aciklama": "virajı dönerken ön tekerleklerin dönemeyip düz kayması", "yasakli_kelimeler": ["understeer", "ön lastik", "dönememek", "burun", "kayma"], "zorluk": "orta"},
    {"kelime": "kontra vermek", "aciklama": "arka kaydığında direksiyonu kayılan yöne çevirip aracı toplamak", "yasakli_kelimeler": ["direksiyon", "toplamak", "ters yön", "kayma", "refleks"], "zorluk": "orta"},
    {"kelime": "drift yapmak", "aciklama": "virajı kontrollü şekilde aracı yan kaydırarak dönmek", "yasakli_kelimeler": ["yanlama", "duman", "el freni", "kaydırma", "şov"], "zorluk": "orta"},
    {"kelime": "motor patlatmak", "aciklama": "aşırı devir veya hararet sonucu motor bloğunun duman atarak iflas etmesi", "yasakli_kelimeler": ["hararet", "duman", "yağ", "iflas", "yarış dışı"], "zorluk": "orta"},
    {"kelime": "ko-pilot dinlemek", "aciklama": "rallide sağ koltuktaki yardımcının okuduğu viraj notlarını uygulamak", "yasakli_kelimeler": ["ralli", "yol notu", "sağ koltuk", "navigatör", "viraj derecesi"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "downforce üretmek", "aciklama": "kanatlar ve difüzörle aracı yere bastıran aerodinamik kuvvet sağlamak", "yasakli_kelimeler": ["yere basma", "difüzör", "aerodinami", "kanat", "vakum"], "zorluk": "zor"},
    {"kelime": "porpoising yaşamak", "aciklama": "zemin etkili araçların düzlükte dalgalanarak zıplaması olayı", "yasakli_kelimeler": ["dalgalanma", "zıplama", "zemin etkisi", "taban", "aerodinamik"], "zorluk": "zor"},
    {"kelime": "ers bataryasını doldurmak", "aciklama": "frenleme anındaki kinetik enerjiyi elektrik bataryasına geri depolamak", "yasakli_kelimeler": ["hibrit", "enerji geri kazanım", "mguk", "batarya", "elektrik"], "zorluk": "zor"},
    {"kelime": "apeks geç kalmak", "aciklama": "viraj çizgisine geç girip çıkışta daha erken gaza oturmayı hedeflemek", "yasakli_kelimeler": ["late apex", "çıkış hızı", "viraj", "gecikme", "çizgi"], "zorluk": "zor"},
    {"kelime": "trail braking uygulamak", "aciklama": "frenlemeyi virajın tam apeksine kadar kademeli azaltarak sürdürmek", "yasakli_kelimeler": ["fren", "viraj içi", "kademeli", "ağırlık transferi", "teknik"], "zorluk": "zor"},
    {"kelime": "heel and toe yapmak", "aciklama": "vites düşürürken sağ ayağın ucuyla frene basıp topuğuyla ara gazı vermek", "yasakli_kelimeler": ["topuk burun", "ara gaz", "vites düşürme", "senkromeç", "pedal"], "zorluk": "zor"},
    {"kelime": "slipstream yakalamak", "aciklama": "öndeki aracın arkasında açtığı alçak basınçlı hava koridoruna girmek", "yasakli_kelimeler": ["hava koridoru", "alçak basınç", "çekim", "düzlük", "arkasına sığınma"], "zorluk": "zor"},
    {"kelime": "kirli havada kalmak", "aciklama": "öndeki aracın arkasındaki türbülanslı havanın ön kanat tutuşunu bozması", "yasakli_kelimeler": ["türbülans", "tutuş kaybı", "öndeki araç", "downforce", "ısınma"], "zorluk": "zor"},
    {"kelime": "difransiyel kilidini ayarlamak", "aciklama": "viraj giriş ve çıkışında sol-sağ tekerlek tork dağılımını değiştirmek", "yasakli_kelimeler": ["tork", "kilit", "çekiş", "tekerlek farkı", "ayarlama"], "zorluk": "zor"},
    {"kelime": "fren dengesini öne almak", "aciklama": "direksiyon üstünden ön ve arka tekerleklere giden hidrolik basıncı kaydırmak", "yasakli_kelimeler": ["brake bias", "hidrolik", "ön arka", "balata", "oran"], "zorluk": "zor"},
    {"kelime": "akua-planing yaşamak", "aciklama": "aşırı yağmurda su tabakasının lastiğin zeminle temasını tamamen kesmesi", "yasakli_kelimeler": ["su tabakası", "yağmur", "yüzme", "kontrol kaybı", "tutuş"], "zorluk": "zor"},
    {"kelime": "halo sayesinde kurtulmak", "aciklama": "kokpit üstündeki titanyum koruma barının baş bölgesini darbeden koruması", "yasakli_kelimeler": ["titanyum", "koruma barı", "kokpit", "kaza", "darbe"], "zorluk": "zor"},
    {"kelime": "lastik delaminasyonu", "aciklama": "aşırı santrifüj kuvveti veya yapısal hatayla lastik sırtının janttan ayrılması", "yasakli_kelimeler": ["ayrılma", "sırt", "patlama", "jant", "kuvvet"], "zorluk": "zor"},
    {"kelime": "parc fermé kurallarına uymak", "aciklama": "sıralama sonrası yarış araçlarının kapalı parka alınıp mekanik müdahalenin yasaklanması", "yasakli_kelimeler": ["kapalı park", "müdahale yasağı", "kontrol", "ayar", "fia"], "zorluk": "zor"}
]

mutfakekipmanlari_verbs = [
    # Kolay (12)
    {"kelime": "doğramak", "aciklama": "bıçak ve kesme tahtası kullanarak sebzeleri küçük parçalara bölmek", "yasakli_kelimeler": ["bıçak", "kesme tahtası", "sebze", "parça", "küçük"], "zorluk": "kolay"},
    {"kelime": "karıştırmak", "aciklama": "kaşık veya spatula ile tenceredeki yemeği harmanlamak", "yasakli_kelimeler": ["kaşık", "spatula", "tencere", "harman", "döndürmek"], "zorluk": "kolay"},
    {"kelime": "pişirmek", "aciklama": "tencere veya tavayı ocağa koyup yiyeceği ısı etkisiyle hazır hale getirmek", "yasakli_kelimeler": ["ocak", "tencere", "tava", "ısı", "yemek"], "zorluk": "kolay"},
    {"kelime": "kızartmak", "aciklama": "tavadaki kızgın yağda patates veya köfteyi nar gibi yapmak", "yasakli_kelimeler": ["tava", "yağ", "patates", "kızgın", "köfte"], "zorluk": "kolay"},
    {"kelime": "fırınlamak", "aciklama": "tepsiye dizilen börek veya eti fırına sürüp pişirmek", "yasakli_kelimeler": ["fırın", "tepsi", "derece", "börek", "pişirme"], "zorluk": "kolay"},
    {"kelime": "rendelemek", "aciklama": "peynir veya havucu rendenin keskin deliklerine sürtüp inceltmek", "yasakli_kelimeler": ["rende", "peynir", "havuç", "sürtmek", "delik"], "zorluk": "kolay"},
    {"kelime": "çırpmak", "aciklama": "çırpma teli veya mikserle yumurtayı köpürtmek", "yasakli_kelimeler": ["mikser", "tel", "yumurta", "köpük", "kase"], "zorluk": "kolay"},
    {"kelime": "süzmek", "aciklama": "haşlanan makarnanın suyunu süzgeç yardımıyla dökmek", "yasakli_kelimeler": ["süzgeç", "makarna", "su", "ayırmak", "lavabo"], "zorluk": "kolay"},
    {"kelime": "kaynatmak", "aciklama": "çaydanlık veya kettle ile suyu yüz dereceye ulaştırmak", "yasakli_kelimeler": ["kettle", "çaydanlık", "su", "kaynar", "derece"], "zorluk": "kolay"},
    {"kelime": "bulaşık yıkamak", "aciklama": "kullanılan tava, tabak ve çatalları deterjanla temizlemek", "yasakli_kelimeler": ["makine", "deterjan", "sünger", "lavabo", "tabak"], "zorluk": "kolay"},
    {"kelime": "ezmek", "aciklama": "patates ezeceği ile haşlanmış patatesleri püre haline getirmek", "yasakli_kelimeler": ["püre", "patates", "ezici", "baskı", "ezme"], "zorluk": "kolay"},
    {"kelime": "soyutmak", "aciklama": "sebze soyacağı ile salatalık veya elmanın kabuğunu sıyırmak", "yasakli_kelimeler": ["soyacak", "kabuk", "salatalık", "elma", "sıyırmak"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "blenderdan geçirmek", "aciklama": "çorbayı veya meyveleri döner bıçaklı haznede pürüzsüz sıvı yapmak", "yasakli_kelimeler": ["blender", "pürüzsüz", "çorba", "bıçak", "motor"], "zorluk": "orta"},
    {"kelime": "bıçak bilemek", "aciklama": "masat veya bileme taşı kullanarak kör bıçağın ağzını keskinleştirmek", "yasakli_kelimeler": ["masat", "bileme taşı", "kör", "keskin", "ağız"], "zorluk": "orta"},
    {"kelime": "hamur yoğurmak", "aciklama": "stand mikseri kancasıyla un ve suyu kıvama gelene kadar çevirmek", "yasakli_kelimeler": ["stand mikser", "kanca", "un", "kıvam", "ekmek"], "zorluk": "orta"},
    {"kelime": "vakumlamak", "aciklama": "gıdayı poşete koyup vakum makinesiyle içindeki havayı tamamen çekmek", "yasakli_kelimeler": ["vakum makinesi", "poşet", "hava", "saklama", "sous vide"], "zorluk": "orta"},
    {"kelime": "tartmak", "aciklama": "hassas dijital mutfak terazisi ile malzemelerin gramajını ölçmek", "yasakli_kelimeler": ["terazi", "gram", "ölçü", "dijital", "dara"], "zorluk": "orta"},
    {"kelime": "buzdolabında soğutmak", "aciklama": "hazırlanan tatlıyı buzdolabına kaldırıp kıvam almasını sağlamak", "yasakli_kelimeler": ["buzdolabı", "soğuk", "tatlı", "dinlendirmek", "raf"], "zorluk": "orta"},
    {"kelime": "kahve öğütmek", "aciklama": "kahve değirmeninde çekirdekleri espresso veya filtre için çekmek", "yasakli_kelimeler": ["değirmen", "çekirdek", "öğütücü", "espresso", "toz"], "zorluk": "orta"},
    {"kelime": "düdüklüde pişirmek", "aciklama": "basınçlı düdüklü tencere kullanarak kuru bakliyatları hızla haşlamak", "yasakli_kelimeler": ["düdüklü tencere", "basınç", "buhar", "kuru fasulye", "hızlı"], "zorluk": "orta"},
    {"kelime": "un elemek", "aciklama": "un eleği kullanarak unu topaklarından ve yabancı maddelerden arındırmak", "yasakli_kelimeler": ["elek", "un", "topak", "havalandırmak", "kek"], "zorluk": "orta"},
    {"kelime": "merdane ile açmak", "aciklama": "ahşap merdane veya oklava ile hamuru masada inceltip yaymak", "yasakli_kelimeler": ["oklava", "merdane", "hamur", "açmak", "yufka"], "zorluk": "orta"},
    {"kelime": "döküm tavayı mühürlemek", "aciklama": "ağır döküm demir tavayı kızdırıp etin suyunu içine hapsetmek", "yasakli_kelimeler": ["döküm tava", "demir", "et", "kızgın", "mühürleme"], "zorluk": "orta"},
    {"kelime": "narenciye sıkmak", "aciklama": "portakal veya limonu narenciye sıkacağına bastırıp suyunu çıkarmak", "yasakli_kelimeler": ["sıkacak", "portakal", "limon", "meyve suyu", "posa"], "zorluk": "orta"},
    {"kelime": "tost basmak", "aciklama": "ekmek arasına kaşar koyup sıcak tost makinesinde preslemek", "yasakli_kelimeler": ["tost makinesi", "ekmek", "kaşar", "pres", "sıcak ızgara"], "zorluk": "orta"},
    {"kelime": "waffle pişirmek", "aciklama": "kare desenli döküm waffle makinesinde hamuru altın sarısı pişirmek", "yasakli_kelimeler": ["waffle makinesi", "desen", "hamur", "kare", "tatlı"], "zorluk": "orta"},
    {"kelime": "sarımsak ezmek", "aciklama": "sarımsak presine diş sarımsak koyup sıkarak püre yapmak", "yasakli_kelimeler": ["sarımsak presi", "diş", "sıkmak", "ezici", "püre"], "zorluk": "orta"},
    {"kelime": "konserve açmak", "aciklama": "konserve açacağı ile metal kutunun kapağını çepeçevre kesmek", "yasakli_kelimeler": ["açacak", "teneke", "kapak", "kutu", "metal"], "zorluk": "orta"},
    {"kelime": "et termometresi batırmak", "aciklama": "fırındaki rostunun iç sıcaklığını metal probla kontrol etmek", "yasakli_kelimeler": ["termometre", "prob", "iç sıcaklık", "derece", "et"], "zorluk": "orta"},
    {"kelime": "yağlı kağıt sermek", "aciklama": "tepsiye yapışmayı önlemek için pişirme kağıdı yaymak", "yasakli_kelimeler": ["pişirme kağıdı", "tepsi", "yapışmaz", "parşömen", "fırın"], "zorluk": "orta"},
    {"kelime": "fırça ile yağlamak", "aciklama": "silikon mutfak fırçasıyla böreğin üstüne yumurta sarısı sürmek", "yasakli_kelimeler": ["silikon fırça", "yumurta sarısı", "sürmek", "yağ", "parlak"], "zorluk": "orta"},
    {"kelime": "et dövmek", "aciklama": "tırtıklı et döveceği ile bifteği vurarak yumuşatıp inceltmek", "yasakli_kelimeler": ["et döveceği", "tokmak", "biftek", "vurmak", "inceltmek"], "zorluk": "orta"},
    {"kelime": "buz kırmak", "aciklama": "güçlü buz kırma bıçağıyla küp buzları kokteyller için parçalamak", "yasakli_kelimeler": ["küp buz", "parçalamak", "kokteyl", "hazne", "bıçak"], "zorluk": "orta"},
    {"kelime": "hava fritözünde pişirmek", "aciklama": "airfryer sepetinde sıcak hava sirkülasyonuyla az yağlı çıtır kızartmak", "yasakli_kelimeler": ["airfryer", "sıcak hava", "sepet", "çıtır", "az yağ"], "zorluk": "orta"},
    {"kelime": "mandolinle dilimlemek", "aciklama": "mandolin rendenin ayarlı bıçağında patatesleri yaprak gibi kesmek", "yasakli_kelimeler": ["mandolin", "yaprak", "dilim", "bıçak", "cips"], "zorluk": "orta"},
    {"kelime": "patates soymak", "aciklama": "kabuk soyma aletiyle patatesin dış kabuğunu hızlıca soymak", "yasakli_kelimeler": ["soyacak", "patates", "kabuk", "bıçak", "zemin"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "sous vide pişirmek", "aciklama": "vakumlu poşetteki eti sabit dereceli su banyosunda saatlerce pişirmek", "yasakli_kelimeler": ["su banyosu", "düşük sıcaklık", "vakum", "termal sirkülatör", "hassas"], "zorluk": "zor"},
    {"kelime": "seasoning yapmak", "aciklama": "döküm tavaya bitkisel yağ sürüp yüksek ısıda fırınlayarak polimer tabaka oluşturmak", "yasakli_kelimeler": ["döküm demir", "yağlama", "fırınlama", "polimerizasyon", "yapışmaz katman"], "zorluk": "zor"},
    {"kelime": "pürmüz alevi vermek", "aciklama": "gazlı mutfak pürmüzüyle krem karamelin üstündeki şekeri karamelize etmek", "yasakli_kelimeler": ["pürmüz", "alev", "karamelize", "şeker", "creme brulee"], "zorluk": "zor"},
    {"kelime": "chinois ile süzmek", "aciklama": "koni biçimli çok ince delikli fransız süzgecinden sosu pürüzsüz geçirmek", "yasakli_kelimeler": ["koni süzgeç", "ince delik", "fransız", "sos", "berrak"], "zorluk": "zor"},
    {"kelime": "bain-marie eritmek", "aciklama": "çikolatayı tenceredeki kaynar suyun üstüne oturtulan kasede buharla eritmek", "yasakli_kelimeler": ["benmari", "çikolata", "buhar", "kase", "dolaylı ısı"], "zorluk": "zor"},
    {"kelime": "sifon ile köpürtmek", "aciklama": "azot protoksit tüplü krema sifonu ile moleküler espumalar sıkmak", "yasakli_kelimeler": ["sifon", "azot tüpü", "espuma", "krema", "köpük"], "zorluk": "zor"},
    {"kelime": "bıçak taşında çapak almak", "aciklama": "japon su taşında bilenen bıçağın ağzında oluşan mikro metal fazlalığını temizlemek", "yasakli_kelimeler": ["su taşı", "japon bıçağı", "mikro", "masat", "ağız"], "zorluk": "zor"},
    {"kelime": "salamandra fırına atmak", "aciklama": "üstten yoğun radyant ısı veren açık endüstriyel fırında yemek üstünü gratine etmek", "yasakli_kelimeler": ["salamandra", "gratin", "üst ısıtıcı", "endüstriyel", "eritmek"], "zorluk": "zor"},
    {"kelime": "refraktometre ile ölçmek", "aciklama": "optik cihazla reçel veya şerbetin brix şeker yoğunluğunu okumak", "yasakli_kelimeler": ["brix", "şeker oranı", "optik", "kırılma indisi", "reçel"], "zorluk": "zor"},
    {"kelime": "pasta çemberini ayarlamak", "aciklama": "ayarlanabilir paslanmaz çelik çemberle pandispanya katlarını sıkıştırmak", "yasakli_kelimeler": ["çember", "pandispanya", "kalıp", "ayarlı", "pasta"], "zorluk": "zor"},
    {"kelime": "pacojet ile pürelemek", "aciklama": "donmuş blok halindeki malzemeleri mikro bıçakla mikron düzeyinde dondurmaya çevirmek", "yasakli_kelimeler": ["pacojet", "donmuş blok", "mikro kesim", "dondurma", "püre"], "zorluk": "zor"},
    {"kelime": "termomiks ile pişirmek", "aciklama": "aynı anda hem tartan, hem doğrayan hem de ısıtarak karıştıran akıllı robotta yapmak", "yasakli_kelimeler": ["thermomix", "robot", "akıllı", "tartma", "indüksiyon"], "zorluk": "zor"},
    {"kelime": "krema torbası sıkmak", "aciklama": "ucuna duy takılmış sıkma torbasıyla pastaya estetik şekilli ganaj bırakmak", "yasakli_kelimeler": ["duy", "sıkma torbası", "ganaj", "dekor", "krema"], "zorluk": "zor"},
    {"kelime": "dehidrate etmek", "aciklama": "gıda kurutucuda düşük ısıda meyve ve sebzelerin nemini günlerce uçurmak", "yasakli_kelimeler": ["kurutucu", "nem", "meyve cipsi", "dehidratör", "düşük ısı"], "zorluk": "zor"}
]

if __name__ == "__main__":
    add_and_save_verbs("motor_sporlari", motor_sporlari_verbs)
    add_and_save_verbs("mutfakekipmanlari", mutfakekipmanlari_verbs)
