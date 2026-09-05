import os, sys, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gen_scripts.card_utils import add_and_save_verbs

# 17. futbol
futbol_verbs = [
    # Kolay (12)
    {"kelime": "gol atmak", "yasakli_kelimeler": ["kale", "top", "file", "sevinç", "şut"], "zorluk": "kolay", "aciklama": "Topu rakip kalenin çizgisi içine göndermek."},
    {"kelime": "pas vermek", "yasakli_kelimeler": ["arkadaş", "top", "aktarmak", "ayak", "isabet"], "zorluk": "kolay", "aciklama": "Topu kendi takımındaki oyuncuya doğru göndermek."},
    {"kelime": "şut çekmek", "yasakli_kelimeler": ["vurmak", "kale", "sert", "ayak", "kaleci"], "zorluk": "kolay", "aciklama": "Gol atmak amacıyla kaleye doğru sert top göndermek."},
    {"kelime": "penaltı kullanmak", "yasakli_kelimeler": ["beyaz nokta", "on bir metre", "kaleci", "ceza sahası", "vuruş"], "zorluk": "kolay", "aciklama": "Ceza sahası içi faul sonrası penaltı noktasından vuruş yapmak."},
    {"kelime": "korner atmak", "yasakli_kelimeler": ["köşe vuruşu", "bayrak", "orta", "dışarı çıkmak", "kafa"], "zorluk": "kolay", "aciklama": "Top rakip savunmadan dışarı çıktığında köşe noktasından orta açmak."},
    {"kelime": "kırmızı kart görmek", "yasakli_kelimeler": ["hakem", "oyundan atılmak", "ceza", "faul", "on kişi"], "zorluk": "kolay", "aciklama": "Ağır kural ihlali sonucu hakem tarafından oyundan ihraç edilmek."},
    {"kelime": "sarı kart görmek", "yasakli_kelimeler": ["uyarı", "hakem", "faul", "ceza", "ikinci"], "zorluk": "kolay", "aciklama": "Kural ihlali sebebiyle hakemden resmi uyarı kartı almak."},
    {"kelime": "top sektirmek", "yasakli_kelimeler": ["ayak", "diz", "yere düşürmeme", "beceri", "oyun"], "zorluk": "kolay", "aciklama": "Topu yere değdirmeden ayak veya dizle havada tutmak."},
    {"kelime": "kafa vurmak", "yasakli_kelimeler": ["alın", "hava topu", "orta", "yükselmek", "gol"], "zorluk": "kolay", "aciklama": "Havadan gelen topa alınla müdahale edip yönlendirmek."},
    {"kelime": "kalecilik yapmak", "yasakli_kelimeler": ["eldiven", "kale", "kurtarış", "tutmak", "file"], "zorluk": "kolay", "aciklama": "Kaleyi korumak ve gelen şutları elleriyle önlemek."},
    {"kelime": "ısınma hareketi yapmak", "yasakli_kelimeler": ["maç öncesi", "koşu", "esneme", "sakatlık", "hazırlık"], "zorluk": "kolay", "aciklama": "Maça girmeden önce kasları harekete hazırlamak."},
    {"kelime": "maç kazanmak", "yasakli_kelimeler": ["galibiyet", "skor", "üç puan", "sevinç", "rakip"], "zorluk": "kolay", "aciklama": "Doksan dakika sonunda rakibinden daha fazla gol atıp galip gelmek."},

    # Orta (24)
    {"kelime": "ofsayta düşmek", "yasakli_kelimeler": ["yan hakem", "bayrak", "savunma arkası", "son adam", "düdük"], "zorluk": "orta", "aciklama": "Pas verildiği anda rakip son savunma oyuncusundan daha ilerde kalmak."},
    {"kelime": "çalım atmak", "yasakli_kelimeler": ["dribling", "rakibi geçmek", "bacak arası", "kandırmak", "bilek"], "zorluk": "orta", "aciklama": "Kıvrak vücut ve ayak hareketleriyle rakip oyuncuyu geride bırakmak."},
    {"kelime": "röveşata vurmak", "yasakli_kelimeler": ["havada ters", "akrobatik", "sırtüstü", "vuruş", "gol"], "zorluk": "orta", "aciklama": "Havaya sıçrayıp ters takla atarak havada topa şut çekmek."},
    {"kelime": "baraj kurmak", "yasakli_kelimeler": ["frikik", "serbest vuruş", "yan yana durmak", "savunma", "mesafe"], "zorluk": "orta", "aciklama": "Serbest vuruşta şut açısını kapatmak için savunma oyuncularının yan yana dizilmesi."},
    {"kelime": "top çalmak", "yasakli_kelimeler": ["müdahale", "kapmak", "savunma", "ayak koymak", "tackle"], "zorluk": "orta", "aciklama": "Rakip oyuncunun ayağındaki topu faul yapmadan almak."},
    {"kelime": "orta açmak", "yasakli_kelimeler": ["kanat", "ceza sahası", "havadan", "bek", "gol aramak"], "zorluk": "orta", "aciklama": "Kanatlardan ceza sahasındaki forvete doğru havadan top göndermek."},
    {"kelime": "frikik kullanmak", "yasakli_kelimeler": ["serbest vuruş", "duran top", "baraj", "falso", "doktor"], "zorluk": "orta", "aciklama": "Ceza sahası dışındaki faul sonrası duran toptan direkt kaleye vurmak."},
    {"kelime": "pres yapmak", "yasakli_kelimeler": ["baskı", "rakip yarı saha", "hata yaptırma", "koşmak", "top kapma"], "zorluk": "orta", "aciklama": "Top rakipteyken alan daraltıp sürekli baskı kurarak hataya zorlamak."},
    {"kelime": "kontratağa çıkmak", "yasakli_kelimeler": ["hızlı hücum", "savunma dengesiz", "boş alan", "geçiş oyunu", "koşu"], "zorluk": "orta", "aciklama": "Rakip savunma yerleşmeden ani ve hızlı hücum geliştirmek."},
    {"kelime": "taktik antrenmanı yapmak", "yasakli_kelimeler": ["teknik direktör", "diziliş", "set hücumu", "tahta", "hazırlık"], "zorluk": "orta", "aciklama": "Sahadaki diziliş ve hücum-savunma varyasyonlarını çalışmak."},
    {"kelime": "oyuncu değiştirmek", "yasakli_kelimeler": ["tabela", "kulübe", "kenar", "yedek", "yorgunluk"], "zorluk": "orta", "aciklama": "Sahadaki yorulan oyuncunun yerine kenardaki yedeği oyuna sürmek."},
    {"kelime": "vAR incelemesi yapmak", "yasakli_kelimeler": ["video hakem", "ekran", "izlemek", "pozisyon", "iptal"], "zorluk": "orta", "aciklama": "Tartışmalı pozisyonu saha kenarındaki ekrandan tekrar izlemek."},
    {"kelime": "taç atışı kullanmak", "yasakli_kelimeler": ["çizgi", "iki elle", "baş arkasından", "kenar", "ayaklar yerde"], "zorluk": "orta", "aciklama": "Yan çizgiden çıkan topu iki elle kuralına uygun oyuna sokmak."},
    {"kelime": "bacak arası atmak", "yasakli_kelimeler": ["beşik", "nutmeg", "çalım", "küçük düşürme", "geçmek"], "zorluk": "orta", "aciklama": "Topu rakip oyuncunun iki bacağının arasından geçirip geçmek."},
    {"kelime": "verkaç yapmak", "yasakli_kelimeler": ["duvar pası", "bir iki", "boşa kaçmak", "tek top", "hücum"], "zorluk": "orta", "aciklama": "Arkadaşına tek pas verip hemen savunma arkasına boşa koşmak."},
    {"kelime": "topuk pası vermek", "yasakli_kelimeler": ["şık", "arkaya", "ayak arkası", "beklenmedik", "asist"], "zorluk": "orta", "aciklama": "Ayağın arkasıyla arkadaki arkadaşına şık ve gizli pas atmak."},
    {"kelime": "şampiyonluk kutlamak", "yasakli_kelimeler": ["kupa", "türbin", "tur atmak", "konfeti", "şampiyon"], "zorluk": "orta", "aciklama": "Ligi zirvede bitirip kupayla taraftar önünde kutlama yapmak."},
    {"kelime": "top kontrolü yapmak", "yasakli_kelimeler": ["stop etmek", "göğüs", "ayak içi", "yumuşatmak", "pas"], "zorluk": "orta", "aciklama": "Havadan veya yerden gelen sert topu ayağıyla yumuşatıp kontrol altına almak."},
    {"kelime": "kaptanlık pazubandı takmak", "yasakli_kelimeler": ["lider", "kol", "takım kaptanı", "hakemle diyalog", "pazubent"], "zorluk": "orta", "aciklama": "Takım lideri olarak sahaya pazubent takarak çıkmak."},
    {"kelime": "tribünleri coşturmak", "yasakli_kelimeler": ["taraftar", "tezahürat", "üçlü çektirmek", "moral", "alkış"], "zorluk": "orta", "aciklama": "Gol sevinci veya hareketlerle taraftarı ateşlemek."},
    {"kelime": "asist yapmak", "yasakli_kelimeler": ["gol pası", "servis", "ortalamak", "skor", "katkı"], "zorluk": "orta", "aciklama": "Arkadaşının gol atmasını sağlayan son pası vermek."},
    {"kelime": "kalesini gole kapatmak", "yasakli_kelimeler": ["clean sheet", "gol yememek", "kurtarış", "savunma", "sıfır"], "zorluk": "orta", "aciklama": "Doksan dakikayı kalesinde hiç gol görmeden tamamlamak."},
    {"kelime": "falso vermek", "yasakli_kelimeler": ["kavis", "trivela", "plase", "dönerek gitme", "şut"], "zorluk": "orta", "aciklama": "Topun havada kavis çizerek dönmesini sağlayacak vuruş yapmak."},
    {"kelime": "derbi maçına çıkmak", "yasakli_kelimeler": ["ezeli rakip", "gerginlik", "taraftar", "büyük maç", "şehrin takımları"], "zorluk": "orta", "aciklama": "Aynı şehrin iki büyük ezeli rakibinin karşılaşmasında oynamak."},

    # Zor (14)
    {"kelime": "gegenpressing uygulamak", "yasakli_kelimeler": ["klopp", "karşı pres", "top kaybedildiği an", "şok baskı", "üç saniye"], "zorluk": "zor", "aciklama": "Top kaybedildiği anda derhal 5-6 saniye içinde organize şok baskıyla topu geri kazanmak."},
    {"kelime": "tiki-taka oynamak", "yasakli_kelimeler": ["guardiola", "kısa pas", "topa sahip olma", "barcelona", "üçgenler"], "zorluk": "zor", "aciklama": "Sürekli kısa tek paslar ve üçgenler kurarak rakibi yorup boşluk aramak."},
    {"kelime": "derin oyun kurucu rolü üstlenmek", "yasakli_kelimeler": ["regista", "pirlo", "savunma önü", "uzun pas", "oyun yönlendirme"], "zorluk": "zor", "aciklama": "Stoperlerin hemen önünden oyunu uzun ve isabetli paslarla arkadan yönetmek."},
    {"kelime": "ters ayaklı kanat olarak oynamak", "yasakli_kelimeler": ["inside forward", "içe kat etmek", "sol ayaklı sağ açık", "şut açısı", "robben"], "zorluk": "zor", "aciklama": "Ters ayağının olduğu kanatta oynayıp merkeze kat ederek şut açısı aramak."},
    {"kelime": "ofsayt taktiği uygulamak", "yasakli_kelimeler": ["savunma çizgisi", "aynı anda öne çıkmak", "tuzak", "çizgi defans", "senkronizasyon"], "zorluk": "zor", "aciklama": "Tüm savunma hattının aynı anda öne fırlayarak forveti ofsaytta bırakması."},
    {"kelime": "bek bindirmesi yapmak", "yasakli_kelimeler": ["overlap", "kanattan depar", "çizgiye inme", "orta açma", "hücum katkısı"], "zorluk": "zor", "aciklama": "Savunma bekinin kanat oyuncusunun arkasından fırlayarak hücuma katılması."},
    {"kelime": "panenka penaltısı atmak", "yasakli_kelimeler": ["aşırtma", "kaleciyi yanıltma", "merkeze yavaş", "soğukkanlı", "vuruş"], "zorluk": "zor", "aciklama": "Penaltıda köşeye atlamak yerine kaleciyi yanıltıp merkeze yavaş aşırtma bırakmak."},
    {"kelime": "rabona vuruşu yapmak", "yasakli_kelimeler": ["bacak arkasından çapraz", "gösterişli", "orta açma", "ters ayak", "estetik"], "zorluk": "zor", "aciklama": "Vuruş ayağını destek ayağının arkasından dolandırarak çapraz şut veya orta çıkarmak."},
    {"kelime": "trivela pas atmak", "yasakli_kelimeler": ["quaresma", "ayak dışı", "kavisli", "dış vuruş", "orta"], "zorluk": "zor", "aciklama": "Ayağın dışıyla topa vurarak ters istikamete kavisli pas veya şut göndermek."},
    {"kelime": "sahte dokuz numara oynamak", "yasakli_kelimeler": ["false nine", "orta sahaya çekilme", "stoperi çıkarma", "messi", "forvetsiz"], "zorluk": "zor", "aciklama": "Forvet mevkiinde başlayıp derine inerek rakip stoperleri yerinden sökmek."},
    {"kelime": "catenaccio savunması yapmak", "yasakli_kelimeler": ["italyan ekolü", "katı savunma", "kilit", "libero", "gol yememe"], "zorluk": "zor", "aciklama": "Tüm hatlarla kapanıp sıfır riskli katı savunma zinciri kurmak."},
    {"kelime": "yarım alanları kullanmak", "yasakli_kelimeler": ["half-space", "merkez ve kanat arası", "taktiksel alan", "koridor", "hücum aksı"], "zorluk": "zor", "aciklama": "Sahanın kanat ile merkez arasındaki stratejik ara koridorlarında pozisyon almak."},
    {"kelime": "alan savunması yapmak", "yasakli_kelimeler": ["adam adama karşıtı", "bölge koruma", "kayma", "blok halinde", "alan daraltma"], "zorluk": "zor", "aciklama": "Birebir rakip kovalamak yerine kendi sorumluluk bölgesini kapatmak."},
    {"kelime": "üçüncü bölgede baskı kurmak", "yasakli_kelimeler": ["final third", "rakip ceza sahası çevresi", "yerleşim", "set hücumu", "kuşatma"], "zorluk": "zor", "aciklama": "Rakip kaleye en yakın hücum sahasına tüm takımla yerleşip oyunu yıkmak."}
]

# 18. gastronomi
gastronomi_verbs = [
    # Kolay (12)
    {"kelime": "yemek tatmak", "yasakli_kelimeler": ["lezzet", "damak", "kaşık", "tat", "denemek"], "zorluk": "kolay", "aciklama": "Yemeğin lezzetini ve tuzunu kontrol etmek için azar azar yemek."},
    {"kelime": "soğan doğramak", "yasakli_kelimeler": ["bıçak", "göz yaşarması", "tahta", "küp küp", "kavurmak"], "zorluk": "kolay", "aciklama": "Yemeklik soğanı kesme tahtasında küçük parçalara ayırmak."},
    {"kelime": "menü hazırlamak", "yasakli_kelimeler": ["restoran", "yemek listesi", "fiyat", "öğün", "seçenek"], "zorluk": "kolay", "aciklama": "Sunulacak yemeklerin listesini ve sırasını düzenlemek."},
    {"kelime": "tuz eklemek", "yasakli_kelimeler": ["tuzluk", "lezzet", "serpmek", "tat", "tencere"], "zorluk": "kolay", "aciklama": "Yemeğin tadını dengelemek için içine tuz serpmek."},
    {"kelime": "et pişirmek", "yasakli_kelimeler": ["tava", "ızgara", "kavurma", "kızartmak", "ateş"], "zorluk": "kolay", "aciklama": "Kırmızı veya beyaz eti ısı tatbik ederek yemeye hazır kılmak."},
    {"kelime": "çorba karıştırmak", "yasakli_kelimeler": ["kepçe", "tencere", "dibi tutmamak", "kaynamak", "kaşık"], "zorluk": "kolay", "aciklama": "Tenceredeki çorbanın dibinin tutmaması için kepçeyle döndürmek."},
    {"kelime": "makarna haşlamak", "yasakli_kelimeler": ["kaynar su", "süzgeç", "tuz", "tencere", "sos"], "zorluk": "kolay", "aciklama": "Kuru makarnayı kaynayan tuzlu suda yumuşayana kadar pişirmek."},
    {"kelime": "salata yapmak", "yasakli_kelimeler": ["marul", "domates", "zeytinyağı", "limon", "kase"], "zorluk": "kolay", "aciklama": "Taze yeşillik ve sebzeleri doğrayıp sosla harmanlamak."},
    {"kelime": "servis yapmak", "yasakli_kelimeler": ["garson", "tabak", "masa", "sunum", "müşteri"], "zorluk": "kolay", "aciklama": "Hazırlanan yemekleri konukların masasına sunmak."},
    {"kelime": "bıçak bilemek", "yasakli_kelimeler": ["masat", "keskinleştirmek", "şef bıçağı", "taş", "kesmek"], "zorluk": "kolay", "aciklama": "Körelen mutfak bıçağının ağzını masatla keskin hale getirmek."},
    {"kelime": "tatlı sipariş etmek", "yasakli_kelimeler": ["restoran", "pasta", "garson", "menü", "hesap"], "zorluk": "kolay", "aciklama": "Yemekten sonra ikram edilmek üzere tatlı istemek."},
    {"kelime": "ekmek dilimlemek", "yasakli_kelimeler": ["fırın", "bıçak", "tahta", "somun", "dilim"], "zorluk": "kolay", "aciklama": "Bütün ekmeği ince parçalar halinde kesmek."},

    # Orta (24)
    {"kelime": "tabak sunumu yapmak", "yasakli_kelimeler": ["plater", "estetik", "sos damlatma", "görsellik", "şef"], "zorluk": "orta", "aciklama": "Yemeği tabakta görsel ve sanatsal bir kompozisyonla düzenlemek."},
    {"kelime": "sotelemek", "yasakli_kelimeler": ["yüksek ateş", "tava", "az yağ", "çevirmek", "sebze"], "zorluk": "orta", "aciklama": "Gıdaları az yağda ve yüksek ateşte sürekli tavayı sallayarak pişirmek."},
    {"kelime": "marine etmek", "yasakli_kelimeler": ["sos", "zeytinyağı", "baharat", "bekletmek", "et yumuşatma"], "zorluk": "orta", "aciklama": "Eti lezzetlendirmek ve yumuşatmak için baharatlı yağlı sosta dinlendirmek."},
    {"kelime": "blanşe etmek", "yasakli_kelimeler": ["şoklama", "kaynar su", "buzlu su", "sebze rengi", "kısa süreli"], "zorluk": "orta", "aciklama": "Sebzeleri kısa süre kaynar suya batırıp hemen buzlu suya atarak şoklamak."},
    {"kelime": "karamelize etmek", "yasakli_kelimeler": ["şeker", "kahverengi", "soğan", "yavaş pişirme", "lezzet"], "zorluk": "orta", "aciklama": "Doğal şekerleri kısık ateşte eritip kahverengi zengin aromaya ulaştırmak."},
    {"kelime": "et mühürlemek", "yasakli_kelimeler": ["döküm tava", "yüksek ısı", "suyunu hapsetmek", "cızırdatmak", "biftek"], "zorluk": "orta", "aciklama": "Eti çok sıcak döküm tavada hızla çevirerek suyunu içine hapsetmek."},
    {"kelime": "sos çektirmek", "yasakli_kelimeler": ["kıvam", "buharlaşma", "kısık ateş", "yoğunlaşma", "redüksiyon"], "zorluk": "orta", "aciklama": "Sıvıyı kısık ateşte buharlaştırarak yoğun ve konsantre kıvama getirmek."},
    {"kelime": "benmari usulü eritmek", "yasakli_kelimeler": ["çikolata", "buhar", "su dolu kap", "dolaylı ısı", "yakmamak"], "zorluk": "orta", "aciklama": "Çikolata veya sosu kaynayan suyun buharında oturtulmuş kapta eritmek."},
    {"kelime": "kemik suyu kaynatmak", "yasakli_kelimeler": ["ilik", "saatlerce", "kolajen", "kısık ateş", "stok"], "zorluk": "orta", "aciklama": "İlikli kemikleri kısık ateşte uzun saatler kaynatıp zengin stok elde etmek."},
    {"kelime": "baharat harmanı yapmak", "yasakli_kelimeler": ["havan", "öğütmek", "karışım", "köri", "aroma"], "zorluk": "orta", "aciklama": "Farklı aromatik tohum ve baharatları havanda döverek özel harman üretmek."},
    {"kelime": "degaze etmek", "yasakli_kelimeler": ["tava dibi", "şarap", "et suyu", "lezzet kazıma", "sos yapımı"], "zorluk": "orta", "aciklama": "Tavanın dibine yapışan lezzetli et artıklarını sıvı döküp çözerek sosa katmak."},
    {"kelime": "emülsiyon yapmak", "yasakli_kelimeler": ["mayonez", "çırpmak", "yağ ve su", "bağlayıcı", "yumurta sarısı"], "zorluk": "orta", "aciklama": "Birbirine karışmayan yağ ve suyu bağlayıcıyla homojen sos haline getirmek."},
    {"kelime": "garnitür eklemek", "yasakli_kelimeler": ["yanında sunulan", "püre", "sebze", "tamamlayıcı", "tabak"], "zorluk": "orta", "aciklama": "Ana yemeğin yanına uyumlu sebze veya püre garnitürleri yerleştirmek."},
    {"kelime": "sommelier tavsiyesi almak", "yasakli_kelimeler": ["içecek eşleşmesi", "kadeh", "uzman", "bağ", "tat uyumu"], "zorluk": "orta", "aciklama": "Yemeğin aromasına en uygun içecek seçimini tadım uzmanına danışmak."},
    {"kelime": "michelin yıldızı kazanmak", "yasakli_kelimeler": ["restoran rehberi", "lezzet ödülü", "şef", "prestij", "denetçi"], "zorluk": "orta", "aciklama": "Üstün gastronomi kalitesiyle uluslararası rehberden yıldız ödülü almak."},
    {"kelime": "tadım menüsü sunmak", "yasakli_kelimeler": ["küçük porsiyonlar", "çok çeşitli", "degüstasyon", "sırayla", "şefin seçimi"], "zorluk": "orta", "aciklama": "Şefin özel kreasyonlarını ufak porsiyonlar halinde sırayla tattırmak."},
    {"kelime": "fümelemek", "yasakli_kelimeler": ["is", "duman", "tütsüleme", "somon", "aroma"], "zorluk": "orta", "aciklama": "Gıdaları meşe veya talaş dumanında bekleterek isli aroma kazandırmak."},
    {"kelime": "meyve kabuğu rendelemek", "yasakli_kelimeler": ["zest", "limon", "portakal", "aroma yağı", "rende"], "zorluk": "orta", "aciklama": "Turunçgillerin kabuğundaki uçucu aromatik yağları rendeleyerek sosa katmak."},
    {"kelime": "al dente pişirmek", "yasakli_kelimeler": ["dişe gelen", "makarna", "hafif diri", "fazla yumuşamayan", "italyan"], "zorluk": "orta", "aciklama": "Makarnayı hamurlaştırmadan dişe gelir kıvamda diri bırakmak."},
    {"kelime": "et dinlendirmek", "yasakli_kelimeler": ["dry aged", "kuru dinlendirme", "dolap", "günlerce", "yumuşaklık"], "zorluk": "orta", "aciklama": "Etin kas liflerinin yumuşaması için özel nemli dolapta haftalarca bekletmek."},
    {"kelime": "karaf içine aktarmak", "yasakli_kelimeler": ["havalandırma", "sürahi", "tortu ayırma", "oksijen", "dökmek"], "zorluk": "orta", "aciklama": "İçeceği havalandırmak ve tortusundan ayırmak için cam sürahiye dökmek."},
    {"kelime": "brunoise doğramak", "yasakli_kelimeler": ["minik küpler", "fransız kesim tekniği", "sebze", "bıçak", "milimetrik"], "zorluk": "orta", "aciklama": "Sebzeleri 1-2 milimetrelik minik ve eşit küpler halinde doğramak."},
    {"kelime": "şef ceketi giymek", "yasakli_kelimeler": ["mutfak önlüğü", "beyaz", "üniforma", "aşçı", "restoran"], "zorluk": "orta", "aciklama": "Mutfakta profesyonel hijyen ve prestij gereği aşçı üniformasını kuşanmak."},
    {"kelime": "yerel ürün kullanmak", "yasakli_kelimeler": ["coğrafi işaret", "mevsimsel", "çiftlikten sofraya", "taze", "yöresel"], "zorluk": "orta", "aciklama": "Yemeklerde bulunulan yörenin özgün ve taze malzemelerini tercih etmek."},

    # Zor (14)
    {"kelime": "sous-vide pişirmek", "yasakli_kelimeler": ["vakum poşeti", "hassas su banyosu", "düşük sıcaklık", "termostat", "uzun süre"], "zorluk": "zor", "aciklama": "Vakumlu torbaya konan gıdayı derecesi sabitlenmiş su banyosunda ağır ağır pişirmek."},
    {"kelime": "küreleme tekniği uygulamak", "yasakli_kelimeler": ["sferifikasyon", "sodyum aljinat", "kalsiyum klorür", "havyar benzeri", "moleküler"], "zorluk": "zor", "aciklama": "Moleküler gastronomide sıvıları jelatinimsi ince zarla küre haline getirmek."},
    {"kelime": "sıvı azotla dondurmak", "yasakli_kelimeler": ["eksi 196 derece", "anlık dondurma", "duman", "çıtır dış yüzey", "kriyomutfak"], "zorluk": "zor", "aciklama": "Gıdayı sıvı nitrojen içine daldırarak saniyeler içinde dondurup çıtırlık kazandırmak."},
    {"kelime": "kuliner köpük üretmek", "yasakli_kelimeler": ["sifon", "espuma", "n2o tüpü", "hafif doku", "emülgatör"], "zorluk": "zor", "aciklama": "Sifon ve azot gazı yardımıyla sosları kremsi hafif köpük formuna sokmak."},
    {"kelime": "maillard reaksiyonunu tetiklemek", "yasakli_kelimeler": ["aminoasit şeker", "kararma", "lezzet kabuğu", "kavrulma aroması", "yüksek ısı"], "zorluk": "zor", "aciklama": "Yüksek ısıda protein ve şekerleri reaksiyona sokarak zengin kavruk tat bileşikleri üretmek."},
    {"kelime": "dekonstrüksiyon tabağı tasarlamak", "yasakli_kelimeler": ["yapısöküm", "klasik yemeği parçalama", "farklı formlar", "yeniden birleştirme", "el bulli"], "zorluk": "zor", "aciklama": "Geleneksel bir yemeğin tüm bileşenlerini farklı dokularda ayrı ayrı sunmak."},
    {"kelime": "umami dengesini kurmak", "yasakli_kelimeler": ["beşinci tat", "glutamat", "parmesan", "dashi", "damak derinliği"], "zorluk": "zor", "aciklama": "Glutamat bakımından zengin gıdalarla yemekte derin ve dolgun lezzet yaratmak."},
    {"kelime": "klarifiye tereyağı yapmak", "yasakli_kelimeler": ["ghee", "süt köpüğünü alma", "saf yağ", "yüksek yanma noktası", "eritme"], "zorluk": "zor", "aciklama": "Tereyağını eritip süt katılarını ve suyunu süzerek saf tereyağı elde etmek."},
    {"kelime": "velouté sos bağlamak", "yasakli_kelimeler": ["meyane", "beyaz stok", "beş temel sos", "un tereyağı", "kadife doku"], "zorluk": "zor", "aciklama": "Meyaneyi tavuk veya balık suyuyla açarak kadifemsi temel sos hazırlamak."},
    {"kelime": "damıtma cihazıyla aroma çekmek", "yasakli_kelimeler": ["rotavapor", "döner buharlaştırıcı", "uçucu yağlar", "vakum distilasyonu", "laboratuvar"], "zorluk": "zor", "aciklama": "Vakumlu döner buharlaştırıcı ile bitkilerden saflaştırılmış saf aroma özleri çıkarmak."},
    {"kelime": "fermantasyon odası yönetmek", "yasakli_kelimeler": ["koji küfü", "garum", "kontrollü nem ısı", "noma", "mikrobiyel lezzet"], "zorluk": "zor", "aciklama": "Isı ve nem ayarlı özel odalarda koji veya amino sos fermentasyonu yürütmek."},
    {"kelime": "confit usulü pişirmek", "yasakli_kelimeler": ["kendi yağında", "kısık ateş", "ördek", "ağır ağır", "muhafaza"], "zorluk": "zor", "aciklama": "Eti tamamen kendi yağının içine gömüp çok kısık ateşte saatlerce pişirmek."},
    {"kelime": "lezzet profili haritalamak", "yasakli_kelimeler": ["flavor pairing", "kimyasal bileşen", "aroma molekülleri", "uyumlu tatlar", "analiz"], "zorluk": "zor", "aciklama": "Ortak moleküler bileşiklere sahip sıra dışı gıda eşleşmelerini analiz etmek."},
    {"kelime": "jelleştirme ajanı seçmek", "yasakli_kelimeler": ["agar agar", "gellan sakızı", "pektin", "karragenan", "kıvam artırıcı"], "zorluk": "zor", "aciklama": "Sıvının sıcaklık ve asitliğine en uygun bitkisel jelleştirici tozu belirlemek."}
]

add_and_save_verbs('futbol', futbol_verbs)
add_and_save_verbs('gastronomi', gastronomi_verbs)
print('P9 done!')
