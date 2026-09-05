# -*- coding: utf-8 -*-
from card_utils import add_and_save_verbs

paleontoloji_verbs = [
    # Kolay (12)
    {"kelime": "kazmak", "aciklama": "fosil yatağını kürek ve çekiçle açıp kemik aramak", "yasakli_kelimeler": ["kürek", "çekiç", "toprak", "kemik", "kazı"], "zorluk": "kolay"},
    {"kelime": "bulmak", "aciklama": "kayaç katmanları arasında milyonlarca yıllık fosil keşfetmek", "yasakli_kelimeler": ["keşif", "kaya", "fosil", "katman", "kemik"], "zorluk": "kolay"},
    {"kelime": "fırçalamak", "aciklama": "fosilin üstündeki toz ve kumu ince kıllı fırçayla temizlemek", "yasakli_kelimeler": ["fırça", "kum", "toz", "temizlemek", "kemik"], "zorluk": "kolay"},
    {"kelime": "taşlaşmak", "aciklama": "canlı kalıntısının minerallerle dolarak kayaya dönüşmesi", "yasakli_kelimeler": ["mineral", "kaya", "kemik", "fosilleşme", "katılaşma"], "zorluk": "kolay"},
    {"kelime": "incelemek", "aciklama": "büyüteçle dinozor dişinin mine yapısını gözlemlemek", "yasakli_kelimeler": ["büyüteç", "dinozor", "diş", "gözlem", "laboratuvar"], "zorluk": "kolay"},
    {"kelime": "birleştirmek", "aciklama": "kırık fosil parçalarını özel yapıştırıcıyla yan yana getirmek", "yasakli_kelimeler": ["yapıştırıcı", "parça", "iskelet", "kırık", "onarım"], "zorluk": "kolay"},
    {"kelime": "müzede sergilemek", "aciklama": "birleştirilen dinozor iskeletini cam vitrinde halka göstermek", "yasakli_kelimeler": ["müze", "iskelet", "vitrin", "sergi", "halk"], "zorluk": "kolay"},
    {"kelime": "ölçmek", "aciklama": "kumpasla fosil kabuğunun en ve boy boyutlarını almak", "yasakli_kelimeler": ["kumpas", "boyut", "milimetre", "cetvel", "ölçüm"], "zorluk": "kolay"},
    {"kelime": "fotoğraflamak", "aciklama": "kazı alanındaki fosilin yerini ve pozisyonunu kaydetmek", "yasakli_kelimeler": ["kamera", "çekim", "arşiv", "kazı alanı", "görsel"], "zorluk": "kolay"},
    {"kelime": "paketlemek", "aciklama": "kırılgan fosil kemiklerini alçı ceketle sarıp nakle hazırlamak", "yasakli_kelimeler": ["alçı", "sarım", "koruma", "koli", "taşıma"], "zorluk": "kolay"},
    {"kelime": "yok olmak", "aciklama": "dinozor türlerinin göktaşı çarpması sonucu yeryüzünden silinmesi", "yasakli_kelimeler": ["tükenmek", "dinozor", "nesil", "göktaşı", "silinmek"], "zorluk": "kolay"},
    {"kelime": "karşılaştırmak", "aciklama": "bulunan antik kemiği günümüz canlılarının anatomisiyle kıyaslamak", "yasakli_kelimeler": ["kıyas", "anatomi", "günümüz", "kemik", "benzerlik"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "alçı ceket yapmak", "aciklama": "kazılan büyük kemiği dağılmadan taşımak için alçılı bezle kaplamak", "yasakli_kelimeler": ["alçılı bez", "ceket", "nakil", "sertleşme", "koruma"], "zorluk": "orta"},
    {"kelime": "karbon testi yapmak", "aciklama": "karbon 14 izotopunun bozunma hızından fosilin yaşını hesaplamak", "yasakli_kelimeler": ["karbon 14", "izotop", "yaş tayini", "radyometrik", "yıl"], "zorluk": "orta"},
    {"kelime": "ayak izi takip etmek", "aciklama": "taşlaşmış çamur üzerindeki dinozor yürüyüş izlerini incelemek", "yasakli_kelimeler": ["iknofosil", "ayak izi", "adım", "yürüyüş", "çamur"], "zorluk": "orta"},
    {"kelime": "kehribar içinde bulmak", "aciklama": "fosilleşmiş çam reçinesine hapsolmuş 50 milyon yıllık böcek keşfetmek", "yasakli_kelimeler": ["kehribar", "amber", "reçine", "böcek", "şeffaf"], "zorluk": "orta"},
    {"kelime": "diş aşınması incelemek", "aciklama": "otobur veya etobur olduğunu anlamak için diş minesindeki çizikleri saymak", "yasakli_kelimeler": ["etobur", "otobur", "beslenme", "mine", "çizik"], "zorluk": "orta"},
    {"kelime": "koprolit kırmak", "aciklama": "taşlaşmış antik hayvan dışkısını kesip besin artıklarını araştırmak", "yasakli_kelimeler": ["dışkı", "koprolit", "besin", "artık", "analiz"], "zorluk": "orta"},
    {"kelime": "katman stratigrafisi okumak", "aciklama": "jeolojik sediman tabakalarının sıralanışından göreceli yaş bulmak", "yasakli_kelimeler": ["stratigrafi", "tabaka", "göreceli yaş", "çökelme", "jeolojik katman"], "zorluk": "orta"},
    {"kelime": "asitle preparasyon", "aciklama": "kireçtaşı içindeki narin fosili seyreltik asit banyosuyla kayadan çözmek", "yasakli_kelimeler": ["seyreltik asit", "kireçtaşı", "çözme", "preparasyon", "zarar vermeme"], "zorluk": "orta"},
    {"kelime": "mikrofosil ayıklamak", "aciklama": "çamur numunesini mikroskop altında foraminifera kabukları için elemek", "yasakli_kelimeler": ["foraminifera", "mikroskop", "elek", "küçük kabuk", "sediman"], "zorluk": "orta"},
    {"kelime": "polen analizi yapmak", "aciklama": "antik bataklık çökellerindeki polenlerden geçmiş bitki örtüsünü çözmek", "yasakli_kelimeler": ["palinoloji", "polen", "bataklık", "bitki örtüsü", "geçmiş iklim"], "zorluk": "orta"},
    {"kelime": "iskelet rekonstrüksiyonu", "aciklama": "eksik kemikleri anatomik kurallara göre modelleyip tam iskelet ayağa kaldırmak", "yasakli_kelimeler": ["ayağa kaldırma", "eksik kemik", "model", "duruş", "montaj"], "zorluk": "orta"},
    {"kelime": "rehber fosil aramak", "aciklama": "kısa sürede yaşayıp geniş alana yayılan trilobit veya ammonit ile katman tarihlendirmek", "yasakli_kelimeler": ["indeks fosil", "trilobit", "ammonit", "tarihleme", "katman"], "zorluk": "orta"},
    {"kelime": "ct taraması yapmak", "aciklama": "fosilleşmiş kafatasını kırmadan bilgisayarlı tomografiyle beyin boşluğunu çıkarmak", "yasakli_kelimeler": ["tomografi", "x ışını", "3d tarama", "iç yapı", "beyin boşluğu"], "zorluk": "orta"},
    {"kelime": "paleoiklim modellemek", "aciklama": "fosil yaprakların kenar dişliliğinden milyonlarca yıl önceki ortalama sıcaklığı bulmak", "yasakli_kelimeler": ["yaprak kenarı", "geçmiş sıcaklık", "iklim", "klimatoloji", "sıcaklık"], "zorluk": "orta"},
    {"kelime": "ammonit kabuğu kesmek", "aciklama": "spiral deniz kabuğunu enlemesine kesip içindeki bölmeleri ve sedef tabakayı parlatmak", "yasakli_kelimeler": ["spiral", "sedef", "kamera", "bölme", "kesit"], "zorluk": "orta"},
    {"kelime": "permineralize olmak", "aciklama": "kemik hücre boşluklarına silisli yeraltı suyunun sızıp kuvars dolması", "yasakli_kelimeler": ["silis", "boşluk doldurma", "kuvars", "yeraltı suyu", "hücre"], "zorluk": "orta"},
    {"kelime": "havalı matkapla oymak", "aciklama": "pnömatik mikro kalemle sert ana kayayı fosil kemiğin etrafından yontmak", "yasakli_kelimeler": ["pnömatik", "hava kalemi", "yontma", "ana kaya", "titreşim"], "zorluk": "orta"},
    {"kelime": "mumyalaşmış doku bulmak", "aciklama": "permafrost buzulunda donmuş mamut derisi ve et kalıntısına rastlamak", "yasakli_kelimeler": ["mamut", "permafrost", "donmuş", "deri", "et"], "zorluk": "orta"},
    {"kelime": "kalıp ve döküm almak", "aciklama": "orijinal fosilin zarar görmemesi için silikon kalıp çıkarıp epoksi kopyasını dökmek", "yasakli_kelimeler": ["silikon kalıp", "epoksi", "kopya", "replika", "döküm"], "zorluk": "orta"},
    {"kelime": "paleo-çevre canlandırmak", "aciklama": "fosil faunadan hareketle bölgenin göl mü çöl mü olduğunu resmetmek", "yasakli_kelimeler": ["canlandırma", "ortam", "göl", "çöl", "illüstrasyon"], "zorluk": "orta"},
    {"kelime": "kemik iliği incelemek", "aciklama": "dinozor uyluk kemiği kesitindeki osteon ve damar kanallarını mikroskopta aramak", "yasakli_kelimeler": ["osteon", "uyluk kemiği", "damar kanalı", "kemik doku", "kesit"], "zorluk": "orta"},
    {"kelime": "izotop imzası okumak", "aciklama": "diş minesindeki stronsiyum izotoplarından hayvanın hangi vadilerde göç ettiğini bulmak", "yasakli_kelimeler": ["stronsiyum", "göç rotası", "izotop", "diş minesi", "coğrafi köken"], "zorluk": "orta"},
    {"kelime": "biyomanyetostratigrafi", "aciklama": "kayaçlardaki kutup manyetik terslenmelerini fosil katmanlarıyla çakıştırmak", "yasakli_kelimeler": ["manyetik kutup", "terslenme", "kayaç", "tarihleme", "manyetizma"], "zorluk": "orta"},
    {"kelime": "taphonomi çalışmak", "aciklama": "canlının ölüm anından fosilleşip bulunmasına kadar geçen çürüme ve taşınma süreçleri", "yasakli_kelimeler": ["çürüme", "taşınma", "gömülme", "ölüm sonrası", "fosilleşme süreci"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "kambriyen patlamasını araştırmak", "aciklama": "541 milyon yıl önce hayvan filumlarının aniden çeşitlendiği evrimsel sıçramayı incelemek", "yasakli_kelimeler": ["541 milyon", "filum", "burgess shale", "aniden çeşitlenme", "erken hayvan"], "zorluk": "zor"},
    {"kelime": "lagersatte yatağı kazmak", "aciklama": "yumuşak doku ve göz gibi organların kusursuz korunduğu istisnai fosil yataklarında çalışmak", "yasakli_kelimeler": ["istisnai korunum", "yumuşak doku", "solnhofen", "burgess", "kusursuz"], "zorluk": "zor"},
    {"kelime": "kladistik analiz yürütmek", "aciklama": "morfolojik sinapomorfileri matrise döküp en tutumlu evrimsel soy ağacını kurmak", "yasakli_kelimeler": ["soy ağacı", "sinapomorfi", "parsimoni", "filogenetik", "kladogram"], "zorluk": "zor"},
    {"kelime": "k-pg sınırını tespit etmek", "aciklama": "dinozorların yok olduğu tabakadaki küresel iridyum kili zenginleşmesini bulmak", "yasakli_kelimeler": ["iridyum anomalisi", "kretase paleojen", "göktaşı sınırı", "kil tabakası", "chicxulub"], "zorluk": "zor"},
    {"kelime": "kesintili dengeyi savunmak", "aciklama": "türlerin uzun durgunluk dönemlerinden sonra ani hızlı evrimsel türleşmeler geçirdiği teorisi", "yasakli_kelimeler": ["punctuated equilibrium", "gould", "ani türleşme", "morfolojik durağanlık", "stasis"], "zorluk": "zor"},
    {"kelime": "histolojik inceleme yapmak", "aciklama": "fosil kemiği ince dilimleyip polarize ışık altında büyüme çizgilerini saymak", "yasakli_kelimeler": ["kemik histolojisi", "büyüme çizgisi", "polarize ışık", "lag", "ince kesit"], "zorluk": "zor"},
    {"kelime": "antropoid kökeni aramak", "aciklama": "hominid fosillerinin kafatası ve pelvis morfolojisinden iki ayaklılığı kanıtlamak", "yasakli_kelimeler": ["iki ayaklılık", "bipedalizm", "hominid", "lucy", "australopithecus"], "zorluk": "zor"},
    {"kelime": "kitlesel yok oluş modellemek", "aciklama": "permocu büyük yok oluşta deniz türlerinin yüzde 96'sının silinme nedenlerini simüle etmek", "yasakli_kelimeler": ["büyük ölüm", "permiyen triyas", "yüzde 96", "volkanizma", "küresel yok oluş"], "zorluk": "zor"},
    {"kelime": "paleoproteomik dizilemek", "aciklama": "milyonlarca yıllık dinozor kemiğinden geriye kalan kolajen protein dizilerini okumak", "yasakli_kelimeler": ["kolajen", "eski protein", "kütle spektrometresi", "dizileme", "peptit"], "zorluk": "zor"},
    {"kelime": "biyoerozyon izi saptamak", "aciklama": "antik sünger ve kurtların fosil kabuklar üzerinde açtığı mikro oyukları sınıflandırmak", "yasakli_kelimeler": ["oyuk", "delgi izi", "sünger", "parazit", "kabuk aşındırma"], "zorluk": "zor"},
    {"kelime": "ediyakaran faunasını çözmek", "aciklama": "kambriyen öncesi iskeletsiz yaprak ve disk formundaki gizemli canlıları araştırmak", "yasakli_kelimeler": ["ediacaran", "prekambriyen", "iskeletsiz", "disk formu", "gizemli"], "zorluk": "zor"},
    {"kelime": "oksijen izotop stratigrafisi", "aciklama": "foraminifer kabuklarındaki delta 18-o oranından buzul ve buzul arası dönemleri çizmek", "yasakli_kelimeler": ["delta o18", "buzul çağı", "milankovic", "derin deniz karotu", "döngü"], "zorluk": "zor"},
    {"kelime": "biyomekanik sonlu elemanlar", "aciklama": "t-rex çenesinin 3d modeline ısırma kuvveti simülasyonu uygulayıp stresi hesaplamak", "yasakli_kelimeler": ["fea", "ısırma kuvveti", "çene stresi", "simülasyon", "mekanik dayanım"], "zorluk": "zor"},
    {"kelime": "izotopik paleodiyet belirlemek", "aciklama": "karbon 13/12 oranından canlının c3 mü yoksa c4 tipi otlarla mı beslendiğini ayırt etmek", "yasakli_kelimeler": ["c3 c4 bitkileri", "karbon izotopu", "paleodiyet", "beslenme", "oran"], "zorluk": "zor"}
]

patoloji_verbs = [
    # Kolay (12)
    {"kelime": "biyopsi almak", "aciklama": "hastalıklı organdan iğne veya cerrahiyle küçük doku parçası koparmak", "yasakli_kelimeler": ["doku", "parça", "iğne", "cerrahi", "organ"], "zorluk": "kolay"},
    {"kelime": "kesit almak", "aciklama": "parafine gömülü dokudan mikrotomla mikron inceliğinde yaprak kesmek", "yasakli_kelimeler": ["mikrotom", "parafin", "mikron", "bıçak", "yaprak"], "zorluk": "kolay"},
    {"kelime": "boyamak", "aciklama": "şeffaf hücreleri mikroskopta görmek için hematoksilen eozin boyası sürmek", "yasakli_kelimeler": ["hematoksilen", "eozin", "pembe mavi", "renk", "boya"], "zorluk": "kolay"},
    {"kelime": "incelemek", "aciklama": "ışık mikroskobu altında hücre yapısını ve bozulmaları gözlemlemek", "yasakli_kelimeler": ["mikroskop", "hücre", "gözlem", "bozulma", "doktor"], "zorluk": "kolay"},
    {"kelime": "teşhis koymak", "aciklama": "dokudaki kanser veya iltihap varlığını saptayıp raporlamak", "yasakli_kelimeler": ["tanı", "rapor", "kanser", "iltihap", "sonuç"], "zorluk": "kolay"},
    {"kelime": "örnek almak", "aciklama": "vücut sıvılarından veya kistten enjektörle sıvı çekmek", "yasakli_kelimeler": ["enjektör", "sıvı", "kist", "iğne", "çekmek"], "zorluk": "kolay"},
    {"kelime": "dokuyu dondurmak", "aciklama": "ameliyat esnasında hızlı tanı için parçayı anında dondurmak", "yasakli_kelimeler": ["frozen", "ameliyat", "hızlı", "soğuk", "anlık"], "zorluk": "kolay"},
    {"kelime": "smear yapmak", "aciklama": "rahim ağzından fırçayla sürüntü alıp cama yaymak", "yasakli_kelimeler": ["sürüntü", "rahim ağzı", "pap", "cam", "fırça"], "zorluk": "kolay"},
    {"kelime": "otopsi yapmak", "aciklama": "şüpheli ölümün kesin nedenini bulmak için cesedi açıp incelemek", "yasakli_kelimeler": ["ceset", "ölüm nedeni", "adli tıp", "açmak", "morga"], "zorluk": "kolay"},
    {"kelime": "yıpranmak", "aciklama": "kronik hastalık veya sigara sebebiyle dokunun yapısının bozulması", "yasakli_kelimeler": ["kronik", "bozulma", "hasar", "doku", "tahribat"], "zorluk": "kolay"},
    {"kelime": "şişmek", "aciklama": "iltihaplı bölgeye sıvı toplanması sonucu ödem meydana gelmesi", "yasakli_kelimeler": ["ödem", "sıvı toplanması", "iltihap", "büyüme", "iltihabi"], "zorluk": "kolay"},
    {"kelime": "iyileşmek", "aciklama": "hasarlı dokunun nedbe dokusu oluşturarak tamir olması", "yasakli_kelimeler": ["tamir", "nedbe", "skar", "düzelme", "hücre"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "makroskopi yapmak", "aciklama": "ameliyatla çıkarılan tümörün boyutunu, ağırlığını ve rengini gözle kaydetmek", "yasakli_kelimeler": ["gözle muayene", "boyut", "ağırlık", "tümör", "kesi"], "zorluk": "orta"},
    {"kelime": "parafine gömmek", "aciklama": "suyu uçurulan doku parçasını eritilmiş sıcak balmumu kalıbına almak", "yasakli_kelimeler": ["blok", "balmumu", "kaset", "fiksasyon", "kalıp"], "zorluk": "orta"},
    {"kelime": "formaldehitte tespit etmek", "aciklama": "otolizi ve çürümeyi durdurmak için dokuyu yüzde onluk formaline yatırmak", "yasakli_kelimeler": ["formalin", "fiksasyon", "çürüme", "koruma", "yüzde 10"], "zorluk": "orta"},
    {"kelime": "lam-lamel kapatmak", "aciklama": "boyanmış ince doku kesitinin üstüne damla damlatıp lamel yapıştırmak", "yasakli_kelimeler": ["lamel", "entellan", "kapatma", "yapıştırma", "preparat"], "zorluk": "orta"},
    {"kelime": "nekroza uğramak", "aciklama": "kan gitmemesi veya toksin etkisiyle hücrelerin kontrolsüzce ölmesi", "yasakli_kelimeler": ["hücre ölümü", "iskemi", "gangren", "kontrolsüz", "çürüme"], "zorluk": "orta"},
    {"kelime": "apoptoza gitmek", "aciklama": "hasarlı veya yaşlı hücrenin programlı intihar mekanizmasını çalıştırması", "yasakli_kelimeler": ["programlı ölüm", "intihar", "kaspaz", "büzüşme", "dna kırılması"], "zorluk": "orta"},
    {"kelime": "immünohistokimya boyamak", "aciklama": "tümör hücresindeki spesifik proteinleri antikorlarla kahverengi işaretlemek", "yasakli_kelimeler": ["antikor", "antijen", "kahverengi", "ihk", "belirteç"], "zorluk": "orta"},
    {"kelime": "cerrahi sınırı incelemek", "aciklama": "tümörün çıkarılan parçanın kenarlarına ulaşıp ulaşmadığını kontrol etmek", "yasakli_kelimeler": ["temiz sınır", "kenar", "mürekkep", "pozitif sınır", "tümör"], "zorluk": "orta"},
    {"kelime": "frozen section bakmak", "aciklama": "ameliyat sürerken cerraha tümörün iyi mi kötü mü olduğunu 15 dakikada bildirmek", "yasakli_kelimeler": ["ameliyathane", "hızlı tanı", "kriyo", "15 dakika", "cerrah"], "zorluk": "orta"},
    {"kelime": "tümörü evrelemek", "aciklama": "kanser kitlesinin çapını ve lenf bezine yayılımını tnm sistemine göre dizmek", "yasakli_kelimeler": ["tnm", "evre", "boyut", "lenf nodu", "yayılım"], "zorluk": "orta"},
    {"kelime": "derecelendirme yapmak", "aciklama": "tümör hücrelerinin normal dokuya ne kadar benzediğini gleason veya nottingham ile puanlamak", "yasakli_kelimeler": ["grade", "gleason", "farklılaşma", "puan", "agresiflik"], "zorluk": "orta"},
    {"kelime": "metaplazik dönüşüm", "aciklama": "kronik tahrişle bir epitel tipinin başka bir dayanıklı epitel tipine dönüşmesi", "yasakli_kelimeler": ["epitel", "barrett", "dönüşüm", "tahriş", "skuamöz"], "zorluk": "orta"},
    {"kelime": "displazi saptamak", "aciklama": "hücrelerin boyut ve çekirdek yapısındaki kanser öncesi anormal düzensizlik", "yasakli_kelimeler": ["kanser öncüsü", "atipik", "çekirdek", "düzensizlik", "prekanseröz"], "zorluk": "orta"},
    {"kelime": "hipertrofi gelişmek", "aciklama": "iş yükü artan kalp veya iskelet kası hücrelerinin hacimce büyümesi", "yasakli_kelimeler": ["hacim artışı", "kas büyümesi", "kalp", "iş yükü", "bölünmeme"], "zorluk": "orta"},
    {"kelime": "hiperplazi olmak", "aciklama": "hormon veya uyarılmayla dokudaki hücre sayısının anormal çoğalması", "yasakli_kelimeler": ["sayı artışı", "çoğalma", "hormon", "endometrium", "prostat"], "zorluk": "orta"},
    {"kelime": "atrofiye uğramak", "aciklama": "kullanılmama veya damar yetmezliği sebebiyle organın küçülüp körelmesi", "yasakli_kelimeler": ["küçülme", "körelme", "kullanılmama", "hacim kaybı", "zayıflama"], "zorluk": "orta"},
    {"kelime": "granülom oluşturmak", "aciklama": "yabancı cisim veya tüberküloz basili etrafına makrofajların sur örmesi", "yasakli_kelimeler": ["tüberküloz", "dev hücre", "makrofaj", "kazeifikasyon", "iltihap"], "zorluk": "orta"},
    {"kelime": "anjiyogenez tetiklemek", "aciklama": "büyüyen tümörün beslenebilmek için çevreye yeni kılcal damarlar salması", "yasakli_kelimeler": ["yeni damar", "vegf", "tümör beslenmesi", "kılcal", "büyüme"], "zorluk": "orta"},
    {"kelime": "metastaz yapmak", "aciklama": "kanser hücrelerinin lenf veya kan yoluyla uzak organlara sıçraması", "yasakli_kelimeler": ["sıçrama", "uzak organ", "yayılma", "kan damarı", "sekonder"], "zorluk": "orta"},
    {"kelime": "sitopatolojik inceleme", "aciklama": "dokuyu kesmeden sadece serbest hücrelerin morfolojisini incelemek", "yasakli_kelimeler": ["hücre analizi", "iab", "sıvı", "sitoloji", "morfoloji"], "zorluk": "orta"},
    {"kelime": "ödem sıvısı birikmek", "aciklama": "damar geçirgenliğinin artmasıyla intertisiyel boşluğa eksüda veya transüda kaçması", "yasakli_kelimeler": ["eksüda", "transüda", "interstisyel", "şişlik", "geçirgenlik"], "zorluk": "orta"},
    {"kelime": "tromboz oluşmak", "aciklama": "damar içinde kan hücrelerinin ve fibrinin pıhtı tıkacı oluşturması", "yasakli_kelimeler": ["pıhtı", "damar tıkanması", "fibrin", "trombosit", "emboli"], "zorluk": "orta"},
    {"kelime": "mitoz saymak", "aciklama": "yüksek büyütme alanında bölünen hücre figürlerini sayarak proliferasyonu ölçmek", "yasakli_kelimeler": ["bölünme", "mitotik figür", "çoğalma hızı", "büyütme alanı", "agresif"], "zorluk": "orta"},
    {"kelime": "kalsifikasyon çökmek", "aciklama": "ölü veya dejenere doku alanlarına kalsiyum tuzlarının oturup taşlaşması", "yasakli_kelimeler": ["kalsiyum", "taşlaşma", "distrofik", "çökelti", "damar sertliği"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "anaplazi göstermek", "aciklama": "tümör hücrelerinin köken aldığı dokuya benzerliğini tamamen yitirip ilkel kalması", "yasakli_kelimeler": ["farklılaşmama", "ilkel", "yüksek derece", "pleomorfizm", "atipik"], "zorluk": "zor"},
    {"kelime": "in situ karsinom yakalamak", "aciklama": "kanser hücrelerinin bazal membranı henüz delmeyip epitel içinde sınırlı kalması", "yasakli_kelimeler": ["bazal membran", "istila etmemiş", "erken evre", "epitel içi", "karsinoma"], "zorluk": "zor"},
    {"kelime": "desmoplazi indüklemek", "aciklama": "istilacı kanser hücrelerinin çevresinde yoğun ve sert fibröz bağ dokusu stroma yaptırması", "yasakli_kelimeler": ["stroma", "fibröz doku", "sertlik", "tümör çevresi", "fibroblast"], "zorluk": "zor"},
    {"kelime": "perinöral invazyon aramak", "aciklama": "malign hücrelerin mikroskobik sinir kılıflarını sarıp boyunca ilerlemesi", "yasakli_kelimeler": ["sinir kılıfı", "malign", "yayılım", "ilerleme", "kötü prognoz"], "zorluk": "zor"},
    {"kelime": "lenfovasküler invazyon saptamak", "aciklama": "tümör embolilerinin kılcal lenf veya kan damarı lümeninde yüzmesi", "yasakli_kelimeler": ["damar içi", "emboli", "lümen", "metastaz riski", "lenfatik"], "zorluk": "zor"},
    {"kelime": "fish analizi yürütmek", "aciklama": "flüoresan problarla dokuda her2 veya myc gen amplifikasyonunu saptamak", "yasakli_kelimeler": ["flüoresan", "in situ hibridizasyon", "gen çoğalması", "her2", "prob"], "zorluk": "zor"},
    {"kelime": "kazeifikasyon nekrozu görmek", "aciklama": "tüberküloz lezyonunun merkezinde peynirimsi yumuşak doku yıkımı izlemek", "yasakli_kelimeler": ["peynirimsi", "tüberküloz", "nekroz", "verem", "odak"], "zorluk": "zor"},
    {"kelime": "koagülasyon nekrozu gelişmek", "aciklama": "enfarktüs alanında hücre proteinlerinin pıhtılaşıp hayalet hücre çizgileri bırakması", "yasakli_kelimeler": ["hayalet hücre", "enfarktüs", "pıhtılaşma", "iskemi", "şablon"], "zorluk": "zor"},
    {"kelime": "kolikvasyon nekrozu olmak", "aciklama": "beyin enfarktüsü veya apsesinde dokunun litik enzimlerle tamamen sıvılaşması", "yasakli_kelimeler": ["sıvılaşma", "beyin enfarktı", "apse", "erime", "kist"], "zorluk": "zor"},
    {"kelime": "karsinogenezi aydınlatmak", "aciklama": "onkogon mutasyonları ve tümör baskılayıcı p53 gen inaktivasyonu aşamalarını çözmek", "yasakli_kelimeler": ["onkojen", "p53", "mutasyon", "tümör oluşumu", "kanserleşme"], "zorluk": "zor"},
    {"kelime": "epitelyal-mezenkimal geçiş", "aciklama": "sabit epitel kanser hücresinin göç yeteneği kazanıp mezenkimal hareketli faza geçmesi", "yasakli_kelimeler": ["emt", "göç yeteneği", "kadherin", "metastaz", "mezenkimal"], "zorluk": "zor"},
    {"kelime": "psammom cisimciği görmek", "aciklama": "tiroid veya over kanserinde lameller tarzda kalsifiye eşmerkezli yuvarlak yapılar bulmak", "yasakli_kelimeler": ["eşmerkezli", "papiller tiroid", "over", "kalsiyum küresi", "lameller"], "zorluk": "zor"},
    {"kelime": "mikrosatellit instabilitesi", "aciklama": "dna mismatch onarım genlerindeki mutasyonla tekrarlayan dna dizilerinin uzayıp kısalması", "yasakli_kelimeler": ["msi", "dna onarımı", "lynch sendromu", "kolon kanseri", "instabilite"], "zorluk": "zor"},
    {"kelime": "dijital patoloji taraması", "aciklama": "tüm cam lamı yüksek çözünürlüklü otomatik tarayıcıyla devasa dijital görsele aktarmak", "yasakli_kelimeler": ["wsi", "tüm lam tarama", "dijital görsel", "yapay zeka", "uzaktan tanı"], "zorluk": "zor"}
]

if __name__ == "__main__":
    add_and_save_verbs("paleontoloji", paleontoloji_verbs)
    add_and_save_verbs("patoloji", patoloji_verbs)
