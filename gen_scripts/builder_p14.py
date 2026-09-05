import os, sys, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gen_scripts.card_utils import add_and_save_verbs

# 27. jeoloji
jeoloji_verbs = [
    # Kolay (12)
    {"kelime": "taş toplamak", "yasakli_kelimeler": ["arazi", "kaya", "çakıl", "renkli", "jeolog"], "zorluk": "kolay", "aciklama": "Arazide incelemek veya biriktirmek üzere kayaç parçaları almak."},
    {"kelime": "deprem olmak", "yasakli_kelimeler": ["sarsıntı", "fay", "yer sarsılması", "bina", "şiddet"], "zorluk": "kolay", "aciklama": "Yerkabuğundaki kırılmalar sonucu yerin sarsılması."},
    {"kelime": "yanardağ patlamak", "yasakli_kelimeler": ["volkan", "lav", "kül", "magma", "püskürme"], "zorluk": "kolay", "aciklama": "Yerin altındaki erimiş kayaların ve gazların yeryüzüne fışkırması."},
    {"kelime": "kaya kırmak", "yasakli_kelimeler": ["çekiç", "taş", "parçalamak", "sert", "arazi"], "zorluk": "kolay", "aciklama": "Jeolog çekiciyle kayacın taze iç yüzeyini görmek için kırmak."},
    {"kelime": "fosil bulmak", "yasakli_kelimeler": ["taşlaşmış", "eski canlı", "kemik", "katman", "kazı"], "zorluk": "kolay", "aciklama": "Kayaç katmanları arasında eski çağlara ait canlı kalıntısına rastlamak."},
    {"kelime": "toprak kaymak", "yasakli_kelimeler": ["heyelan", "yamaç", "yağmur", "çamur", "çökme"], "zorluk": "kolay", "aciklama": "Yamaçtaki toprak kütlesinin yerçekimiyle aşağıya sürüklenmesi."},
    {"kelime": "mağara gezmek", "yasakli_kelimeler": ["sarkıt", "dikit", "yeraltı", "karanlık", "kalker"], "zorluk": "kolay", "aciklama": "Kireçtaşının erimesiyle oluşan doğal yeraltı boşluklarını keşfetmek."},
    {"kelime": "maden aramak", "yasakli_kelimeler": ["altın", "bakır", "demir", "yeraltı", "cevher"], "zorluk": "kolay", "aciklama": "Ekonomik değeri olan mineralleri yerkabuğunda araştırmak."},
    {"kelime": "kuyu kazmak", "yasakli_kelimeler": ["su", "derin", "sondaj", "toprak", "pompa"], "zorluk": "kolay", "aciklama": "Yeraltı suyuna veya madene ulaşmak için çukur açmak."},
    {"kelime": "katmanları saymak", "yasakli_kelimeler": ["tabaka", "çökelti", "üst üste", "kaya", "tarih"], "zorluk": "kolay", "aciklama": "Tortul kayaçlardaki ardışık jeolojik tabakaları ayırt etmek."},
    {"kelime": "büyüteçle minerale bakmak", "yasakli_kelimeler": ["mercek", "lup", "kristal", "parıltı", "inceleme"], "zorluk": "kolay", "aciklama": "Kayacın içindeki mineral tanelerini küçük el büyüteciyle incelemek."},
    {"kelime": "toprak örneği almak", "yasakli_kelimeler": ["numune", "poşet", "analiz", "tarla", "zemin"], "zorluk": "kolay", "aciklama": "Laboratuvar tahlili için araziden toprak numunesi toplamak."},

    # Orta (24)
    {"kelime": "fay hattı haritalamak", "yasakli_kelimeler": ["kırık", "diri fay", "deprem riski", "çizgi", "sismoloji"], "zorluk": "orta", "aciklama": "Yerkabuğundaki aktif kırık hatlarının geçtiği yerleri haritaya işlemek."},
    {"kelime": "jeolojik kesit çizmek", "yasakli_kelimeler": ["profil", "yeraltı tabakaları", "düşey görünüm", "senklinal", "antiklinal"], "zorluk": "orta", "aciklama": "Yerin altındaki tabaka dizilimini dikey kesit halinde görselleştirmek."},
    {"kelime": "sondaj yapmak", "yasakli_kelimeler": ["karot", "matkap", "derinlik", "boru", "zemin etüdü"], "zorluk": "orta", "aciklama": "Dönen matkap borularıyla derinlerden silindirik kaya örneği çıkarmak."},
    {"kelime": "karot numunesi almak", "yasakli_kelimeler": ["silindir taş", "sondaj sandığı", "derinlik", "sağlamlık", "analiz"], "zorluk": "orta", "aciklama": "Sondaj kuyusundan çıkarılan silindirik kaya örneğini sandığa dizmek."},
    {"kelime": "pusulayla eğim ölçmek", "yasakli_kelimeler": ["brunton", "tabaka eğimi", "doğrultu", "klinometre", "derece"], "zorluk": "orta", "aciklama": "Jeolog pusulasıyla tabakanın uzanış doğrultusunu ve eğim açısını bulmak."},
    {"kelime": "kayaç tanımlamak", "yasakli_kelimeler": ["magmatik", "tortul", "başkalaşım", "mineraloji", "sınıflandırma"], "zorluk": "orta", "aciklama": "Kayacın doku ve bileşimine bakarak magmatik, sedimanter veya metamorfik olduğunu saptamak."},
    {"kelime": "zemin etüdü hazırlamak", "yasakli_kelimeler": ["inşaat öncesi", "taşıma gücü", "sıvılaşma riski", "rapor", "jeoteknik"], "zorluk": "orta", "aciklama": "Bina yapılmadan önce arsanın zemin sağlamlığını raporlamak."},
    {"kelime": "aşınmayı incelemek", "yasakli_kelimeler": ["erozyon", "rüzgar su", "parçalanma", "vadi", "yüzey"], "zorluk": "orta", "aciklama": "Kayaçların su ve atmosferik şartlarla aşınıp taşınma sürecini tetkik etmek."},
    {"kelime": "radyometrik yaş tayini yapmak", "yasakli_kelimeler": ["karbon 14", "izotop", "uranyum kurşun", "yarılanma ömrü", "milyon yıl"], "zorluk": "orta", "aciklama": "Radyoaktif izotopların bozunma oranından kayacın mutlak yaşını hesaplamak."},
    {"kelime": "metamorfizma geçirmek", "yasakli_kelimeler": ["başkalaşım", "yüksek sıcaklık basınç", "gnays", "mermerleşme", "yapı değişimi"], "zorluk": "orta", "aciklama": "Kayaçların derinlerdeki ısı ve basınç altında mineralojik değişime uğraması."},
    {"kelime": "çökelti biriktirmek", "yasakli_kelimeler": ["sedimantasyon", "göl tabanı", "deniz", "kum çakıl", "katmanlaşma"], "zorluk": "orta", "aciklama": "Akarsuların taşıdığı tortuların göl ve deniz tabanında üst üste yığılması."},
    {"kelime": "magma katılaşmak", "yasakli_kelimeler": ["soğuma", "granit", "bazalt", "plütonizma", "derinlik kayaçları"], "zorluk": "orta", "aciklama": "Erimiş haldeki magmanın yeraltında yavaşça soğuyarak kristalleşmesi."},
    {"kelime": "sertlik testi yapmak", "yasakli_kelimeler": ["mohs ölçeği", "çizme", "elmas", "talk", "mineral"], "zorluk": "orta", "aciklama": "Minerali standart referans taşlarla çizerek Mohs sertlik derecesini bulmak."},
    {"kelime": "hidrojeolojik analiz yapmak", "yasakli_kelimeler": ["akifer", "yeraltı suyu", "kaynak", "debi", "geçirgenlik"], "zorluk": "orta", "aciklama": "Yeraltı suyunun akiferlerdeki hareketini ve debisini incelemek."},
    {"kelime": "levha hareketlerini izlemek", "yasakli_kelimeler": ["plaka tektoniği", "kıtaların kayması", "gps", "yakınlaşma uzaklaşma", "santimetre"], "zorluk": "orta", "aciklama": "Yerkabuğu levhalarının yıllık milimetrik ötelenmelerini takip etmek."},
    {"kelime": "jeotermal kaynak aramak", "yasakli_kelimeler": ["sıcak su", "buhar", "kaplıca", "enerji santrali", "fay"], "zorluk": "orta", "aciklama": "Yerin derinliklerinden gelen yüksek sıcaklıktaki su ve buhar rezervuarlarını bulmak."},
    {"kelime": "asit damlatmak", "yasakli_kelimeler": ["hidroklorik asit", "köpürme", "kalsit", "kalker tespiti", "reaksiyon"], "zorluk": "orta", "aciklama": "Kayaca seyreltik asit damlatıp köpürmesine bakarak kireçtaşı teşhisi koymak."},
    {"kelime": "kıvrımlanma oluşturmak", "yasakli_kelimeler": ["antiklinal", "senklinal", "yan basınç", "dağ oluşumu", "bükülme"], "zorluk": "orta", "aciklama": "Esnek tortul tabakaların yan basınçlarla dalga dalga bükülmesi."},
    {"kelime": "lav akıntısını izlemek", "yasakli_kelimeler": ["akışkanlık", "pahoehoe", "sıcaklık", "krater", "püskürme"], "zorluk": "orta", "aciklama": "Volkandan çıkan erimiş lavın arazi üzerindeki yayılma hızını gözlemek."},
    {"kelime": "sıvılaşma riskini ölçmek", "yasakli_kelimeler": ["deprem anı", "kumlu zemin", "su doygunluğu", "batma", "zemin davranışı"], "zorluk": "orta", "aciklama": "Deprem sarsıntısında suya doygun kumlu zeminin sıvı gibi davranma riskini belirlemek."},
    {"kelime": "tabaka kalınlığını ölçmek", "yasakli_kelimeler": ["metre", "şerit metre", "stratigrafi", "formasyon", "sedimanter"], "zorluk": "orta", "aciklama": "Bir tortul kayaç tabakasının gerçek stratigrafik kalınlığını bulmak."},
    {"kelime": "kaya düşmesini önlemek", "yasakli_kelimeler": ["çelik ağ", "püskürtme beton", "yamaç", "ankraj", "karayolu"], "zorluk": "orta", "aciklama": "Yol kenarındaki dik yamaçlara çelik tel ve ankraj çekerek taş düşmesini engellemek."},
    {"kelime": "jeokimyasal harita çıkarmak", "yasakli_kelimeler": ["element dağılımı", "ağır metal", "toprak tahlili", "anomali", "tenör"], "zorluk": "orta", "aciklama": "Bölgedeki kimyasal elementlerin konsantrasyon haritasını çizmek."},
    {"kelime": "paleocoğrafik ortamı canlandırmak", "yasakli_kelimeler": ["eski deniz", "sığ göl", "fosil kanıtı", "iklim", "milyon yıl önce"], "zorluk": "orta", "aciklama": "Fosil ve tortullardan yola çıkarak bölgenin milyonlarca yıl önceki doğasını tasvir etmek."},

    # Zor (14)
    {"kelime": "polarizan mikroskopta incelemek", "yasakli_kelimeler": ["ince kesit", "çift kırılma", "pleokroizma", "nicol prizması", "mineral tanıma"], "zorluk": "zor", "aciklama": "0.03 mm kalınlığa inceltilmiş kaya kesitini polarize ışık altında analiz etmek."},
    {"kelime": "subdüksiyon zonunu modellemek", "yasakli_kelimeler": ["dalma batma", "okyanusal kabuk", "manto", "hendek", "ada yayı"], "zorluk": "zor", "aciklama": "Yoğun okyanusal levhanın kıtasal levhanın altına dalarak mantoya erimesini modellemek."},
    {"kelime": "orojenez mekanizmasını çözmek", "yasakli_kelimeler": ["dağ oluşumu", "kıtasal çarpışma", "himalayalar", "itilme bindirme fayı", "nap"], "zorluk": "zor", "aciklama": "İki kıtanın çarpışmasıyla tortulların yükselip dev dağ kuşaklarına dönüşmesini açıklamak."},
    {"kelime": "ofiyolit dizilimini saptamak", "yasakli_kelimeler": ["okyanus kabuğu kalıntısı", "peridotit", "gabro", "yastık lav", "karaya bindirme"], "zorluk": "zor", "aciklama": "Karasal alana bindirilmiş antik okyanus tabanı kayaç istifini teşhis etmek."},
    {"kelime": "fasiyes analizi yapmak", "yasakli_kelimeler": ["çökelme ortamı", "lito-fasiyes", "biyo-fasiyes", "çökelti özellikleri", "sedimantoloji"], "zorluk": "zor", "aciklama": "Kayanın doku ve fosil içeriğinden hangi derinlik ve ortamda çökeldiğini saptamak."},
    {"kelime": "nap yapısını belgelemek", "yasakli_kelimeler": ["ötelemeli kütle", "ters fay bindirmesi", "allokton birim", "tektonik sürüklenme", "alp dağları"], "zorluk": "zor", "aciklama": "Kilometrelerce yer değiştirip yabancı tabakaların üzerine oturmuş tektonik kütleyi haritalamak."},
    {"kelime": "p-T evrim eğrisi çıkarmak", "yasakli_kelimeler": ["basınç sıcaklık yolu", "metamorfik fasiyes", "eklojit", "retrograd prograd", "izoterm"], "zorluk": "zor", "aciklama": "Kayacın başkalaşım sürecinde geçtiği sıcaklık ve basınç değişim yolunu hesaplamak."},
    {"kelime": "paleomanyetik kutup terslenmesi bulmak", "yasakli_kelimeler": ["manyetik kalıntı", "okyanus tabanı yayılması", "kuzey güney değişimi", "bazalt şeritleri", "kron"], "zorluk": "zor", "aciklama": "Bazaltlardaki manyetik minerallerin geçmiş kutup terslenmelerine kilitlenişini ölçmek."},
    {"kelime": "boudinage yapısını analiz etmek", "yasakli_kelimeler": ["sosis yapısı", "yetkin tabaka uzaması", "plastik deformasyon", "çekme gerilmesi", "makaslama"], "zorluk": "zor", "aciklama": "Sert tabakanın sünek hamur içinde çekilip sosis dilimleri gibi parçalanmasını incelemek."},
    {"kelime": "sismik yansıma profilini yorumlamak", "yasakli_kelimeler": ["ses dalgaları", "yeraltı tabaka yankısı", "jeofizik hat", "fay tuz domları", "petrol arama"], "zorluk": "zor", "aciklama": "Yere gönderilen ses dalgalarının geri dönüş yankılarından derin yeraltı profilini okumak."},
    {"kelime": "stratigrafik korelasyon yapmak", "yasakli_kelimeler": ["istif eşleme", "kılavuz fosil", "uzak havzalar", "aynı yaş tabakaları", "biyo-stratigrafi"], "zorluk": "zor", "aciklama": "Birbirinden çok uzaktaki iki ayrı arazi kesitinin aynı yaştaki tabakalarını eşleştirmek."},
    {"kelime": "izostazi dengesini hesaplamak", "yasakli_kelimeler": ["kabuk manto dengesi", "airy pratt", "buzul kalkışı", "ağırlık tazmini", "yüzme ilkesi"], "zorluk": "zor", "aciklama": "Yerkabuğu kütlelerinin manto üzerinde hidrostatik dengeyle yüzme prensibini modellemek."},
    {"kelime": "diyajenez sürecini izlemek", "yasakli_kelimeler": ["taşlaşma", "çimentolaşma", "kompaksiyon", "gözeneklilik kaybı", "sedimanter"], "zorluk": "zor", "aciklama": "Gevşek çökeltilerin gömülme esnasında çimentolaşarak sert kayaca dönüşmesini takip etmek."},
    {"kelime": "magmatik farklılaşmayı açıklamak", "yasakli_kelimeler": ["bowen serisi", "kesirli kristallenme", "kalan ergiyik", "asidik bazik", "kristal çökelmesi"], "zorluk": "zor", "aciklama": "Tek bir ana magmadan kristallenme sırasına göre farklı kimyada kayaçlar türemesini izah etmek."}
]

# 28. jeomorfoloji
jeomorfoloji_verbs = [
    # Kolay (12)
    {"kelime": "dağa tırmanmak", "yasakli_kelimeler": ["zirve", "yükseklik", "yürümek", "tepe", "kaya"], "zorluk": "kolay", "aciklama": "Yüksek dağlık yeryüzü şeklinin tepesine doğru çıkmak."},
    {"kelime": "vadi boyunca yürümek", "yasakli_kelimeler": ["dere", "iki dağ arası", "kanyon", "su", "yol"], "zorluk": "kolay", "aciklama": "Akarsuyun aşındırarak açtığı çukur hat boyunca ilerlemek."},
    {"kelime": "nehir akmak", "yasakli_kelimeler": ["ırmak", "su", "deniz", "yatağı", "akıntı"], "zorluk": "kolay", "aciklama": "Tatlı su kütlesinin yatak içinde yerçekimiyle aşağıya akması."},
    {"kelime": "tepeye çıkmak", "yasakli_kelimeler": ["yüksek", "manzara", "tırmanış", "küçük dağ", "zirve"], "zorluk": "kolay", "aciklama": "Çevresine göre hafif yüksek olan yeryüzü kabartısına varmak."},
    {"kelime": "kumsalda yürümek", "yasakli_kelimeler": ["plaj", "deniz kenarı", "kum", "dalga", "kıyı"], "zorluk": "kolay", "aciklama": "Deniz kıyısındaki kumlu düzlükte gezinmek."},
    {"kelime": "şelale izlemek", "yasakli_kelimeler": ["çağlayan", "yüksekten dökülen su", "kayalık", "ses", "akıntı"], "zorluk": "kolay", "aciklama": "Akarsuyun dik kaya basamağından aşağıya dökülüşünü seyretmek."},
    {"kelime": "falezden denize bakmak", "yasakli_kelimeler": ["yalıyar", "dik uçurum", "kıyı", "dalga çarpması", "yüksek"], "zorluk": "kolay", "aciklama": "Kıyıdaki dik kaya uçurumun kenarından denizi izlemek."},
    {"kelime": "ova boyunca sürmek", "yasakli_kelimeler": ["düzlük", "tarla", "yol", "geniş", "araba"], "zorluk": "kolay", "aciklama": "Geniş ve düz alçak arazide yolculuk etmek."},
    {"kelime": "çölde kum tepesi görmek", "yasakli_kelimeler": ["kumul", "kum", "rüzgar", "kurak", "sıcak"], "zorluk": "kolay", "aciklama": "Rüzgarın yığdığı tepecikleri çöl arazisinde gözlemlemek."},
    {"kelime": "göl kenarında durmak", "yasakli_kelimeler": ["durgun su", "kıyı", "manzara", "su birikintisi", "dinlenmek"], "zorluk": "kolay", "aciklama": "Karayla çevrili tatlı veya tuzlu su kütlesinin kıyısında bulunmak."},
    {"kelime": "ada etrafında dolaşmak", "yasakli_kelimeler": ["dört tarafı deniz", "tekne", "tur", "kara parçası", "kıyı"], "zorluk": "kolay", "aciklama": "Her yanı sularla çevrili kara parçasının çevresini gezmek."},
    {"kelime": "boğazdan geçmek", "yasakli_kelimeler": ["gemi", "iki deniz arası", "dar su yolu", "istanbul", "çanakkale"], "zorluk": "kolay", "aciklama": "İki kara arasındaki dar deniz geçidinden karşıya geçmek."},

    # Orta (24)
    {"kelime": "menderes çizmek", "yasakli_kelimeler": ["büküm", "s kıvrımı", "eğimsiz vadi", "akarsu", "salınım"], "zorluk": "orta", "aciklama": "Akarsuyun eğimi azalan tabanda 'S' şeklinde kıvrımlar yaparak akması."},
    {"kelime": "delta oluşturmak", "yasakli_kelimeler": ["alüvyon", "denize döküldüğü yer", "üçgen ova", "akarsu ağzı", "çökelti"], "zorluk": "orta", "aciklama": "Akarsuyun taşıdığı killeri deniz kıyısında biriktirerek üçgen ova kurması."},
    {"kelime": "kanyon yarmak", "yasakli_kelimeler": ["derin vadi", "dik yamaçlar", "akarsu aşındırması", "boğaz", "kaya"], "zorluk": "orta", "aciklama": "Akarsuyun sert kayaç bloklarını derine doğru yararak dik duvarlı vadi açması."},
    {"kelime": "taraça oluşturmak", "yasakli_kelimeler": ["seki", "basamak", "akarsu yatağı", "epirojenez", "eski vadi tabanı"], "zorluk": "orta", "aciklama": "Akarsuyun yeniden canlanarak eski vadi tabanını basamak şeklinde yukarda bırakması."},
    {"kelime": "peribacası aşındırmak", "yasakli_kelimeler": ["kapadokya", "tüf", "bazalt şapka", "yağmur rüzgar", "erozyon"], "zorluk": "orta", "aciklama": "Tüflü arazinin sel suları ve rüzgarla aşınıp konik sütunlara dönüşmesi."},
    {"kelime": "karstik erime gerçekleştirmek", "yasakli_kelimeler": ["kireçtaşı", "lapya", "dolin", "karbondioksitli su", "çözünme"], "zorluk": "orta", "aciklama": "Kalker ve jips gibi kayaçların asidik sularla kimyasal olarak çözünmesi."},
    {"kelime": "kumul hareketi izlemek", "yasakli_kelimeler": ["barkan", "rüzgar yönü", "kum tepesi göçü", "çöl", "ötelenme"], "zorluk": "orta", "aciklama": "Rüzgarın hakim yönüne göre kum tepeciklerinin yer değiştirmesini takip etmek."},
    {"kelime": "buzul vadisi oymak", "yasakli_kelimeler": ["u profilli vadi", "glasyal", "buzul dili", "aşındırma", "yüksek dağ"], "zorluk": "orta", "aciklama": "Aşağı kayan dev buzul kütlesinin vadi tabanını 'U' şeklinde genişletip oyması."},
    {"kelime": "moren yığmak", "yasakli_kelimeler": ["buzul taşı", "moren seti", "buzul biriktirmesi", "kaya döküntüsü", "çökelti"], "zorluk": "orta", "aciklama": "Buzulun sürüklediği köşeli taş ve kayaları eridiği yerde tepe şeklinde biriktirmesi."},
    {"kelime": "tombolo bağlamak", "yasakli_kelimeler": ["saplı ada", "kıyı oku", "adaya bağlanma", "dalga biriktirmesi", "kıstak"], "zorluk": "orta", "aciklama": "Kıyı okunun büyüyerek açıkta duran bir adayı ana karaya bağlaması."},
    {"kelime": "lagün kapatmak", "yasakli_kelimeler": ["deniz kulağı", "kıyı kordonu", "koy ağzı", "gölleşme", "dalga"], "zorluk": "orta", "aciklama": "Koyun önünün dalga birikintisiyle kapanarak denizden ayrılmış göl oluşturması."},
    {"kelime": "dolin oluşturmak", "yasakli_kelimeler": ["karstik çöküntü", "kapalı havza", "kalker", "obruk başlangıcı", "erime çukuru"], "zorluk": "orta", "aciklama": "Kireçtaşlı platolarda erime sonucu tava şeklinde çukurlukların açılması."},
    {"kelime": "obruk çökmesi yaşamak", "yasakli_kelimeler": ["derin kuyu", "yeraltı mağara tavanı", "konya ovası", "aniden çökme", "karstik"], "zorluk": "orta", "aciklama": "Yeraltı mağarasının tavanının çökmesiyle yeryüzünde dev silindirik çukur oluşması."},
    {"kelime": "plato aşındırmak", "yasakli_kelimeler": ["yayla", "akarsularla yarılmış", "yüksek düzlük", "derin vadiler", "aşınım"], "zorluk": "orta", "aciklama": "Yüksek düzlüklerin akarsular tarafından derin vadilerle parçalanması."},
    {"kelime": "alüvyon yelpazesi kurmak", "yasakli_kelimeler": ["dağ eteği", "eğim kırılması", "akarsu birikintisi", "koni", "tortu"], "zorluk": "orta", "aciklama": "Dağdan düzlüğe çıkan derenin hızının kesilmesiyle yelpaze şeklinde kum biriktirmesi."},
    {"kelime": "kıyı aşınmasını ölçmek", "yasakli_kelimeler": ["falez gerilemesi", "dalga darbesi", "abrasyon platformu", "metre", "kayıp"], "zorluk": "orta", "aciklama": "Dalgaların kıyı uçurumlarını geriye doğru aşındırma hızını saptamak."},
    {"kelime": "traverten basamağı oluşturmak", "yasakli_kelimeler": ["pamukkale", "kalsiyum karbonat", "kaynak suyu", "çökelme", "beyaz teras"], "zorluk": "orta", "aciklama": "Kalsiyumlu sıcak suların yüzeyde gazını kaybedip beyaz kalker basamakları örmesi."},
    {"kelime": "dev kazanı oymak", "yasakli_kelimeler": ["şelale altı", "girdap", "taş dönmesi", "silindirik çukur", "aşındırma"], "zorluk": "orta", "aciklama": "Şelalenin düştüğü yerde girdap yapan taşların tabanda yuvarlak derin çukur açması."},
    {"kelime": "sirki buzul gölüne çevirmek", "yasakli_kelimeler": ["buzul yalağı", "dağ zirvesi", "sirk gölü", "erime suyu", "çanak"], "zorluk": "orta", "aciklama": "Buzulun zirvede açtığı çanağın buz eriyince berrak göle dönüşmesi."},
    {"kelime": "boğaz vadi yarmak", "yasakli_kelimeler": ["kluz", "dağ sırasını enine kesme", "akarsu gücü", "dik geçit", "epijenetik"], "zorluk": "orta", "aciklama": "Akarsuyun enine uzanan dağ sırasını dikine yararak koridor açması."},
    {"kelime": "kıyı kordonu uzatmak", "yasakli_kelimeler": ["lido", "kum dili", "kıyı boyu akıntı", "dalga taşıması", "koy"], "zorluk": "orta", "aciklama": "Kıyı akıntılarının taşıdığı kumların açık denize doğru uzayıp set yapması."},
    {"kelime": "tor topoğrafyası sergilemek", "yasakli_kelimeler": ["granit blokları", "fiziksel kimyasal ayrışma", "yuvarlak kayalar", "üst üste", "çatlak sistemi"], "zorluk": "orta", "aciklama": "Granit kütlelerin çatlaklar boyunca ayrışıp üst üste yuvarlak bloklar halinde kalması."},
    {"kelime": "aşınım yüzeyi oluşturmak", "yasakli_kelimeler": ["peneplen", "yontukdüz", "deniz seviyesine yakın", "son evre", "düzleştirme"], "zorluk": "orta", "aciklama": "Milyonlarca yıllık erozyonla tüm engebelerin silinip hafif dalgalı düzlüğe varması."},
    {"kelime": "polye tabanında tarım yapmak", "yasakli_kelimeler": ["gölova", "en büyük karstik çukur", "kırmızı toprak", "terra rossa", "ova"], "zorluk": "orta", "aciklama": "Birbirine bağlanan karstik erime çukurlarının oluşturduğu dev ovada ekim yapmak."},

    # Zor (14)
    {"kelime": "peneplenleşme sürecini incelemek", "yasakli_kelimeler": ["davis coğrafi döngüsü", "gençlik olgunluk yaşlılık", "yontukdüz", "erozyon taban seviyesi", "relyef"], "zorluk": "zor", "aciklama": "Topografyanın jeolojik döngüde taban seviyesine kadar aşınıp yontukdüzleşmesini izlemek."},
    {"kelime": "antedans vadi gelişimini saptamak", "yasakli_kelimeler": ["gömük akarsu", "tektonik yükselme", "akarsuyun önceden varlığı", "yarmavadi", "hız yarışı"], "zorluk": "zor", "aciklama": "Yükselen dağ kütlesini akarsuyun yükselme hızına eşit hızda derine kazarak koruması."},
    {"kelime": "epijenik vadi yarıntısını bulmak", "yasakli_kelimeler": ["farklı tabaka örtüsü", "gömülme", "orijinal yataktan sapma", "sert kayaya saplanma", "aşındırma"], "zorluk": "zor", "aciklama": "Yumuşak örtüde akan nehrin derine indikçe altındaki sert kayaca gömülüp vadi açması."},
    {"kelime": "kapma olayını belgelemek", "yasakli_kelimeler": ["river capture", "geriye aşındırma", "akarsu korsanlığı", "su bölümü çizgisi değişimi", "dirsek"], "zorluk": "zor", "aciklama": "Daha güçlü derenin geriye aşındırmayla komşu derenin sularını kendi yatağına çalması."},
    {"kelime": "biyostazi ve reksistazi dengesini tartmak", "yasakli_kelimeler": ["erhart kuramı", "orman örtüsü ve kimyasal erime", "toprak örtüsü kaybı", "iklimsel jeomorfoloji", "mekanik erozyon"], "zorluk": "zor", "aciklama": "Bitki örtülü kararlı dönem ile kurak erozyonlu dönem arasındaki yeryüzü şekillenme dengesini modellemek."},
    {"kelime": "asimetrik vadi profilini açıklamak", "yasakli_kelimeler": ["coriolis etkisi", "tektonik eğimlenme", "bakı etkisi", "farklı yamaç eğimleri", "yamaç süreçleri"], "zorluk": "zor", "aciklama": "Vadinin iki yamacının bakı, tektonizma veya rüzgar sebebiyle farklı eğimlere sahip olmasını açıklamak."},
    {"kelime": "pediplen düzlüğü haritalamak", "yasakli_kelimeler": ["king modeli", "yamaç gerilemesi", "pediment birleşimi", "kurak yarı kurak", "inselberg"], "zorluk": "zor", "aciklama": "Yamaçların eğimini kaybetmeden paralel gerilemesiyle oluşan geniş düzlükleri haritalamak."},
    {"kelime": "inselberg kalıntısını belirlemek", "yasakli_kelimeler": ["ada tepe", "monadnock", "aşınmadan arta kalan", "sert kaya kütlesi", "düzlük ortası"], "zorluk": "zor", "aciklama": "Düzleşmiş peneplen veya pediplen ortasında tek başına yükselen dirençli tepeyi saptamak."},
    {"kelime": "kriyotürbasyon izi aramak", "yasakli_kelimeler": ["donma çözülme", "periglasiyal", "desenli topraklar", "don kabarması", "tundra"], "zorluk": "zor", "aciklama": "Donma-çözülme döngüsünün toprak katmanlarını altüst edip taş halkaları yapmasını incelemek."},
    {"kelime": "kör vadi yapısını çözmek", "yasakli_kelimeler": ["ponor", "düden", "suyun batması", "aniden biten vadi", "karstik yeraltı drenajı"], "zorluk": "zor", "aciklama": "Yüzeyden akan derenin bir düdenden yerin altına girerek vadisini aniden sonlandırmasını açıklamak."},
    {"kelime": "yardang aşınımını incelemek", "yasakli_kelimeler": ["rüzgar aşındırması", "omurga sırtı", "kurak çöl", "uzunlamasına oluk", "korrazyon"], "zorluk": "zor", "aciklama": "Rüzgarın kum taneleriyle kayaları rüzgar yönüne paralel sivri sırtlar halinde oymasını incelemek."},
    {"kelime": "abrasyon platformunu tarihlendirmek", "yasakli_kelimeler": ["dalga düzlüğü", "deniz seviyesi değişimi", "falez önü", "östatik hareket", "kıyı sekisi"], "zorluk": "zor", "aciklama": "Dalga aşındırmasıyla oluşup deniz çekilince havada kalmış fosil kıyı düzlüklerini tarihlendirmek."},
    {"kelime": "kollüvyal yamaç depolanmasını ölçmek", "yasakli_kelimeler": ["yerçekimi kayması", "yamaç döküntüsü", "talus konisi", "eteğe yığılma", "sedimanter"], "zorluk": "zor", "aciklama": "Yamaçtan kopan köşeli döküntülerin etekte birikme stratigrafisini ve kalınlığını ölçmek."},
    {"kelime": "örgütsel drenaj ağı türetmek", "yasakli_kelimeler": ["horton strahler", "akarsu hiyerarşisi", "dendritik kafesli", "havza morfolojisi", "kol sırası"], "zorluk": "zor", "aciklama": "Havzadaki tüm akarsu kollarını 1'den başlayarak akış hiyerarşisine göre derecelendirmek."}
]

add_and_save_verbs('jeoloji', jeoloji_verbs)
add_and_save_verbs('jeomorfoloji', jeomorfoloji_verbs)
print('P14 done!')
