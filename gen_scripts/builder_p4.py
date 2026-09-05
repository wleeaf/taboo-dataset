import os, sys, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gen_scripts.card_utils import add_and_save_verbs

# 7. ergonomi
ergonomi_verbs = [
    # Kolay (12)
    {"kelime": "dik oturmak", "yasakli_kelimeler": ["sırt", "koltuk", "duruş", "omurga", "kambur"], "zorluk": "kolay", "aciklama": "Omurgayı bükmeden düzgün pozisyonda oturmak."},
    {"kelime": "koltuğu ayarlamak", "yasakli_kelimeler": ["yükseklik", "sandalye", "masa", "oturmak", "kolçak"], "zorluk": "kolay", "aciklama": "Çalışma sandalyesinin boyunu ve sırt açısını vücuda göre düzenlemek."},
    {"kelime": "mola vermek", "yasakli_kelimeler": ["dinlenmek", "ara", "çalışmak", "ara vermek", "yorulmak"], "zorluk": "kolay", "aciklama": "Sürekli çalışmaya ara verip bedeni rahatlatmak."},
    {"kelime": "ekran yüksekliğini ayarlamak", "yasakli_kelimeler": ["monitör", "göz hizası", "boyun", "bilgisayar", "bakmak"], "zorluk": "kolay", "aciklama": "Ekranın üst kenarını göz hizasına getirmek."},
    {"kelime": "esneme hareketi yapmak", "yasakli_kelimeler": ["kol", "bacak", "gerinmek", "kas", "rahatlamak"], "zorluk": "kolay", "aciklama": "Kas tutulmalarını önlemek için vücudu esnetmek."},
    {"kelime": "ağır yük kaldırmak", "yasakli_kelimeler": ["bel", "diz", "koli", "taşımak", "ağırlık"], "zorluk": "kolay", "aciklama": "Ağır bir nesneyi yerden yukarı doğru hareket ettirmek."},
    {"kelime": "aydınlatmayı düzenlemek", "yasakli_kelimeler": ["ışık", "lamba", "göz yorulması", "parlama", "masa"], "zorluk": "kolay", "aciklama": "Çalışma ortamındaki ışık seviyesini gözü yormayacak şekle getirmek."},
    {"kelime": "bilek desteği kullanmak", "yasakli_kelimeler": ["klavye", "mousepad", "el", "ağrı", "yumuşak"], "zorluk": "kolay", "aciklama": "Klavye ve fare kullanırken bileği yumuşak pedle desteklemek."},
    {"kelime": "kambur durmamak", "yasakli_kelimeler": ["duruş", "sırt", "eğilmek", "dik", "omurga"], "zorluk": "kolay", "aciklama": "Sırtı eğri ve öne bükük tutmaktan kaçınmak."},
    {"kelime": "ayak desteği koymak", "yasakli_kelimeler": ["tabure", "yer", "bacak", "yükseklik", "dolaşım"], "zorluk": "kolay", "aciklama": "Masa altında ayakların altına eğimli basamak yerleştirmek."},
    {"kelime": "gözleri dinlendirmek", "yasakli_kelimeler": ["ekran", "kapatmak", "uzak", "bakmak", "kırpmak"], "zorluk": "kolay", "aciklama": "Sürekli ekrana bakmaktan yorulan gözleri uzağa bakarak dinlendirmek."},
    {"kelime": "rahat giyinmek", "yasakli_kelimeler": ["kıyafet", "bol", "ayakkabı", "sıkmak", "hareket"], "zorluk": "kolay", "aciklama": "Bedeni sıkmayan, dolaşımı engellemeyen giysiler tercih etmek."},

    # Orta (24)
    {"kelime": "dizleri bükerek yük kaldırmak", "yasakli_kelimeler": ["bel sakatlığı", "squat", "omurga", "ağırlık", "bacak kası"], "zorluk": "orta", "aciklama": "Ağır yükü bele değil bacak kaslarına bindirerek kaldırmak."},
    {"kelime": "bel boşluğunu desteklemek", "yasakli_kelimeler": ["lomber", "yastık", "omurga", "koltuk", "kavis"], "zorluk": "orta", "aciklama": "Belin doğal çukurunu ergonomik destekle doldurmak."},
    {"kelime": "20-20-20 kuralını uygulamak", "yasakli_kelimeler": ["dakika", "saniye", "metre", "göz dinlendirme", "ekran"], "zorluk": "orta", "aciklama": "Her 20 dakikada bir 20 saniye boyunca 20 feet (6 metre) uzağa bakmak."},
    {"kelime": "dikey fare kullanmak", "yasakli_kelimeler": ["ergonomik mouse", "ön kol", "bilek", "pronasyon", "tutuş"], "zorluk": "orta", "aciklama": "Bilek burkulmasını önlemek için el sıkışma pozisyonlu fare kullanmak."},
    {"kelime": "ayakta çalışma masası kullanmak", "yasakli_kelimeler": ["standing desk", "yükseklik ayarı", "hareket", "oturma", "kalori"], "zorluk": "orta", "aciklama": "Gün içinde oturma ve ayakta durma pozisyonlarını dönüştürmek."},
    {"kelime": "tekrarlayan hareketlerden kaçınmak", "yasakli_kelimeler": ["rsi", "sakatlık", "aynı hareket", "bilek", "rotasyon"], "zorluk": "orta", "aciklama": "Sürekli aynı kas grubunu yoran monotoni hareketleri çeşitlendirmek."},
    {"kelime": "ortam gürültüsünü azaltmak", "yasakli_kelimeler": ["desibel", "kulaklık", "akustik", "stres", "odak"], "zorluk": "orta", "aciklama": "Çalışma ortamındaki ses kirliliğini kontrol altına almak."},
    {"kelime": "postür analizi yapmak", "yasakli_kelimeler": ["vücut duruşu", "hizalanma", "omurga", "açı", "değerlendirme"], "zorluk": "orta", "aciklama": "Çalışanın çalışma sırasındaki beden duruş açılarını incelemek."},
    {"kelime": "parlamayı engellemek", "yasakli_kelimeler": ["ekran", "güneş", "yansıma", "mat filtre", "ışık"], "zorluk": "orta", "aciklama": "Ekrana vuran ışık yansımalarını önleyici filtre veya perde kullanmak."},
    {"kelime": "ulaşım mesafesini optimize etmek", "yasakli_kelimeler": ["çalışma alanı", "uzanmak", "kol mesafesi", "masa düzeni", "alet"], "zorluk": "orta", "aciklama": "Sık kullanılan araçları kola en yakın erişim alanına yerleştirmek."},
    {"kelime": "ortam sıcaklığını ayarlamak", "yasakli_kelimeler": ["klima", "terleme", "üşüme", "derece", "konfor"], "zorluk": "orta", "aciklama": "Oda ısısını termal konfor standartlarına getirmek."},
    {"kelime": "titreşimi absorbe etmek", "yasakli_kelimeler": ["vibrasyon", "alet", "eldiven", "makine", "eklem"], "zorluk": "orta", "aciklama": "El aletlerinin yarattığı titreşimin eklemlere geçişini sönümlemek."},
    {"kelime": "hava sirkülasyonu sağlamak", "yasakli_kelimeler": ["havalandırma", "oksijen", "temiz hava", "pencere", "karbondioksit"], "zorluk": "orta", "aciklama": "Kapalı ortamın havasını düzenli tazeleyerek hava kalitesini korumak."},
    {"kelime": "eklem açısını korumak", "yasakli_kelimeler": ["90 derece", "dirsek", "diz", "bilek", "nötr"], "zorluk": "orta", "aciklama": "Eklem ve uzuvları 90 derecelik nötr açıda tutmak."},
    {"kelime": "iş istasyonunu kişiselleştirmek", "yasakli_kelimeler": ["boyut", "boy", "çalışan", "özelleştirme", "ekipman"], "zorluk": "orta", "aciklama": "Masa ve donanımları çalışanın fiziksel ölçülerine göre ayarlamak."},
    {"kelime": "ergonomik klavye seçmek", "yasakli_kelimeler": ["bölünmüş", "split", "eğim", "bilek", "tuş"], "zorluk": "orta", "aciklama": "Doğal kol açısına uyumlu bölünmüş klavyeleri tercih etmek."},
    {"kelime": "yorgunluk seviyesini izlemek", "yasakli_kelimeler": ["tükenmişlik", "dikkat", "performans", "hata", "dinlenme"], "zorluk": "orta", "aciklama": "Çalışanların bedensel ve zihinsel bitkinlik düzeyini takip etmek."},
    {"kelime": "karpal tünel riskini düşürmek", "yasakli_kelimeler": ["sinir sıkışması", "bilek", "uyuşma", "tendon", "ameliyat"], "zorluk": "orta", "aciklama": "Bilek sinirlerinin baskı altında kalmasını engelleyici tedbirler almak."},
    {"kelime": "iş rotasyonu uygulamak", "yasakli_kelimeler": ["görev değişimi", "farklı iş", "monotoni", "kas grubu", "vardiya"], "zorluk": "orta", "aciklama": "Farklı kasları çalıştırmak için çalışanların görev yerini dönüştürmek."},
    {"kelime": "görme alanını düzenlemek", "yasakli_kelimeler": ["bakış açısı", "odak", "göz hareketi", "konumlandırma", "mesafe"], "zorluk": "orta", "aciklama": "Ekran ve belgeleri boyun çevirmeden görülecek alana koymak."},
    {"kelime": "kullanıcı dostu arayüz tasarlamak", "yasakli_kelimeler": ["ui", "yazılım", "bilişsel", "kolay", "erişilebilirlik"], "zorluk": "orta", "aciklama": "Zihinsel eforu azaltan sade ve anlaşılır yazılım arayüzleri oluşturmak."},
    {"kelime": "bel fıtığını önlemek", "yasakli_kelimeler": ["disk", "omurilik", "ağrı", "omurga", "ağır kaldırma"], "zorluk": "orta", "aciklama": "Omurga disklerine binen dengesiz yükleri engelleyerek fıtık riskini kaldırmak."},
    {"kelime": "bilişsel yükü azaltmak", "yasakli_kelimeler": ["zihin", "hafıza", "stres", "karmaşa", "bilgi akışı"], "zorluk": "orta", "aciklama": "Çalışanın aynı anda işlemesi gereken zihinsel bilgi miktarını sadeleştirmek."},
    {"kelime": "kulak koruyucu takmak", "yasakli_kelimeler": ["kulaklık", "tıkaç", "gürültü", "işitme kaybı", "fabrika"], "zorluk": "orta", "aciklama": "Yüksek desibelli sanayi ortamlarında işitme duyusunu korumak."},

    # Zor (14)
    {"kelime": "antropometrik ölçüm almak", "yasakli_kelimeler": ["insan vücudu", "boyutlar", "persentil", "uzuv uzunluğu", "tasarım"], "zorluk": "zor", "aciklama": "Hedef kullanıcı kitlesinin vücut ölçü dağılımlarını bilimsel olarak çıkarmak."},
    {"kelime": "rULA skorunu hesaplamak", "yasakli_kelimeler": ["hızlı üst uzuv değerlendirmesi", "postür", "skor", "biyomekanik", "risk"], "zorluk": "zor", "aciklama": "Üst uzuvların duruşuna bağlı kas-iskelet sistemi riskini puanlamak."},
    {"kelime": "rEBA analizi yapmak", "yasakli_kelimeler": ["tüm vücut", "ergonomi puanı", "postür", "iş güvenliği", "değerlendirme"], "zorluk": "zor", "aciklama": "Tüm vücut duruşunu baz alarak ergonomik risk düzeyini belirlemek."},
    {"kelime": "nIOSH kaldırma denklemini uygulamak", "yasakli_kelimeler": ["tavsiye edilen ağırlık limiti", "kaldırma indeksi", "mesafe", "frekans", "asimetri"], "zorluk": "zor", "aciklama": "Elle kaldırma işlerinde güvenli ağırlık sınırını formülle hesaplamak."},
    {"kelime": "biyomekanik yükü modellemek", "yasakli_kelimeler": ["moment", "l5 s1 omuru", "kuvvet", "vektör", "eklem gerilmesi"], "zorluk": "zor", "aciklama": "İş esnasında kas ve eklemlere binen fiziksel kuvvetleri simüle etmek."},
    {"kelime": "kümülatif travma bozukluğunu saptamak", "yasakli_kelimeler": ["ctd", "kronik mikro hasar", "kas iskelet", "yıpranma", "tendinit"], "zorluk": "zor", "aciklama": "Sürekli tekrarlanan küçük zorlanmaların birikerek oluşturduğu hasarı teşhis etmek."},
    {"kelime": "persentil aralığını belirlemek", "yasakli_kelimeler": ["yüzdelik dilim", "5 ila 95", "popülasyon", "ölçü", "uyum"], "zorluk": "zor", "aciklama": "Tasarımda toplumun yüzde 5'i ile 95'ini kapsayacak ölçü sınırlarını seçmek."},
    {"kelime": "bilişsel ergonomiyi optimize etmek", "yasakli_kelimeler": ["mental iş yükü", "nasa tlx", "hafıza kapasitesi", "karar verme", "arayüz"], "zorluk": "zor", "aciklama": "Operatörün bilgi işleme ve dikkat süreçlerindeki zihinsel zorlanmayı asgariye indirmek."},
    {"kelime": "kas elektromyografisi çekmek", "yasakli_kelimeler": ["emg", "elektrik aktivitesi", "kas yorgunluğu", "elektrot", "sinyal"], "zorluk": "zor", "aciklama": "Kasların çalışma anındaki elektriksel sinyallerini ölçerek yorulma hızını bulmak."},
    {"kelime": "termal konfor indeksi hesaplamak", "yasakli_kelimeler": ["pmv", "ppd", "nem", "radyant sıcaklık", "hava hızı"], "zorluk": "zor", "aciklama": "Ortamın ısısal parametrelerinden yola çıkarak tahmini memnuniyetsizlik oranını bulmak."},
    {"kelime": "nötr beden duruşunu sağlamak", "yasakli_kelimeler": ["minimum gerilim", "omurga doğal eğrisi", "açı", "biyomekanik", "sıfır stres"], "zorluk": "zor", "aciklama": "Kas ve bağların en az gerilim altında olduğu ideal anatomik pozisyonu korumak."},
    {"kelime": "iş-yükü indeksini türetmek", "yasakli_kelimeler": ["strain index", "el bileği", "kuvvet harcama", "frekans", "risk skoru"], "zorluk": "zor", "aciklama": "El ve bilek işlerinde tekrarlı eforun yarattığı zorlanma katsayısını hesaplamak."},
    {"kelime": "luxmetre ile ölçüm yapmak", "yasakli_kelimeler": ["aydınlık düzeyi", "lümen", "ışık şiddeti", "görme konforu", "cihaz"], "zorluk": "zor", "aciklama": "Çalışma masası yüzeyine düşen ışık akısını cihazla ölçmek."},
    {"kelime": "titreşim dozu değerini saptamak", "yasakli_kelimeler": ["vibration dose value", "ivme", "el kol titreşimi", "maruziyet sınırı", "frekans"], "zorluk": "zor", "aciklama": "Çalışanın maruz kaldığı mekanik titreşimin kümülatif dozunu hesaplamak."}
]

# 8. etik
etik_verbs = [
    # Kolay (12)
    {"kelime": "doğruyu söylemek", "yasakli_kelimeler": ["yalan", "dürüst", "gerçek", "aldatmamak", "söz"], "zorluk": "kolay", "aciklama": "Gerçekleri saklamadan dürüstçe ifade etmek."},
    {"kelime": "yardım etmek", "yasakli_kelimeler": ["destek", "iyilik", "ihtiyaç", "el uzatmak", "paylaşmak"], "zorluk": "kolay", "aciklama": "İhtiyacı olan kişiye karşılık beklemeden destek olmak."},
    {"kelime": "yalan söylememek", "yasakli_kelimeler": ["dürüstlük", "aldatmak", "kandırmak", "gerçek", "sahte"], "zorluk": "kolay", "aciklama": "Gerçeğe aykırı söz ve beyandan kaçınmak."},
    {"kelime": "hırsızlık yapmamak", "yasakli_kelimeler": ["çalmak", "hak", "mal", "sahip", "izinsiz"], "zorluk": "kolay", "aciklama": "Başkasına ait bir eşyayı izinsiz almaktan sakınmak."},
    {"kelime": "sözünde durmak", "yasakli_kelimeler": ["vefa", "güven", "söz vermek", "tutmak", "sadakat"], "zorluk": "kolay", "aciklama": "Verilen vaadi ve taahhüdü eksiksiz yerine getirmek."},
    {"kelime": "saygı göstermek", "yasakli_kelimeler": ["hürmet", "büyük", "değer", "kibar", "nezaket"], "zorluk": "kolay", "aciklama": "Başkalarının hak ve varlığına hürmetle yaklaşmak."},
    {"kelime": "adaletli olmak", "yasakli_kelimeler": ["hak", "eşit", "tarafsız", "hukuk", "doğruluk"], "zorluk": "kolay", "aciklama": "Herkese hakkı olanı tarafsızca ve dürüstçe vermek."},
    {"kelime": "özür dilemek", "yasakli_kelimeler": ["hata", "pişman", "af", "bağışlanma", "kusur"], "zorluk": "kolay", "aciklama": "Yapılan bir hatadan ötürü karşı taraftan bağışlanma istemek."},
    {"kelime": "iyilik yapmak", "yasakli_kelimeler": ["güzel", "fayda", "yardım", "karşılıksız", "sevap"], "zorluk": "kolay", "aciklama": "İnsanlara ve canlılara faydalı, güzel davranışta bulunmak."},
    {"kelime": "hakkını savunmak", "yasakli_kelimeler": ["haksızlık", "mücadele", "korumak", "itiraz", "adalet"], "zorluk": "kolay", "aciklama": "Kendisine veya başkasına yapılan haksızlığa karşı durmak."},
    {"kelime": "sır tutmak", "yasakli_kelimeler": ["gizli", "paylaşmamak", "güven", "anlatmamak", "saklamak"], "zorluk": "kolay", "aciklama": "Kendisine emanet edilen gizli bilgiyi başkalarına yaymamak."},
    {"kelime": "kul hakkı yememek", "yasakli_kelimeler": ["adalet", "helal", "haram", "günah", "haksızlık"], "zorluk": "kolay", "aciklama": "Başkalarının emeğine ve hakkına tecavüz etmemek."},

    # Orta (24)
    {"kelime": "vicdan muhasebesi yapmak", "yasakli_kelimeler": ["iç ses", "pişmanlık", "değerlendirme", "doğru yanlış", "hesaplaşma"], "zorluk": "orta", "aciklama": "Davranışlarının ahlaki doğruluğunu kendi iç dünyasında sorgulamak."},
    {"kelime": "empati kurmak", "yasakli_kelimeler": ["kendini yerine koymak", "anlamak", "duygu", "hissiyat", "bakış açısı"], "zorluk": "orta", "aciklama": "Kendini başkasının yerine koyarak onun duygularını anlamaya çalışmak."},
    {"kelime": "çıkar çatışmasını bildirmek", "yasakli_kelimeler": ["tarafsızlık", "menfaat", "şeffaflık", "etik kurul", "beyan"], "zorluk": "orta", "aciklama": "Kişisel menfaatinin göreviyle çeliştiği durumu dürüstçe açıklamak."},
    {"kelime": "etik dışı davranışı ihbar etmek", "yasakli_kelimeler": ["whistleblowing", "şikayet", "yolsuzluk", "rapor", "bildiri"], "zorluk": "orta", "aciklama": "Kurumdaki ahlaksız veya yasadışı uygulamaları yetkililere bildirmek."},
    {"kelime": "özerkliğe saygı duymak", "yasakli_kelimeler": ["otonomi", "özgür irade", "karar", "birey", "müdahale etmeme"], "zorluk": "orta", "aciklama": "Bireyin kendi hayatı hakkında özgürce karar verme hakkını tanımak."},
    {"kelime": "zarar vermeme ilkesini gözetmek", "yasakli_kelimeler": ["primum non nocere", "doktor", "kötülük", "zararsızlık", "koruma"], "zorluk": "orta", "aciklama": "Eylemlerinde öncelikle hiçbir canlıya zarar vermemeyi esas almak."},
    {"kelime": "aydınlatılmış onam almak", "yasakli_kelimeler": ["rıza", "hasta", "bilgilendirme", "imza", "tedavi"], "zorluk": "orta", "aciklama": "Tıbbi veya bilimsel işlem öncesi kişiyi tüm riskler hakkında bilgilendirip rızasını almak."},
    {"kelime": "mesleki sırrı saklamak", "yasakli_kelimeler": ["gizlilik", "avukat", "doktor", "danışan", "etik kod"], "zorluk": "orta", "aciklama": "Meslek icrası sırasında öğrenilen mahrem bilgileri korumak."},
    {"kelime": "intihalden kaçınmak", "yasakli_kelimeler": ["aşırma", "kaynak gösterme", "kopya", "akademik", "alıntı"], "zorluk": "orta", "aciklama": "Başkalarının fikir veya yazılarını kaynak göstermeden sahiplenmemek."},
    {"kelime": "tarafsız karar vermek", "yasakli_kelimeler": ["objektif", "önyargısız", "hakem", "ayrımcılık", "eşitlik"], "zorluk": "orta", "aciklama": "Kişisel sempati veya antipatileri karara karıştırmamak."},
    {"kelime": "ahlaki ikilem yaşamak", "yasakli_kelimeler": ["çıkmaz", "iki seçenek", "zor karar", "değer çatışması", "vicdan"], "zorluk": "orta", "aciklama": "İki ahlaki ilkenin birbiriyle çatıştığı zor bir durum arasında kalmak."},
    {"kelime": "fırsat eşitliği sağlamak", "yasakli_kelimeler": ["ayrımcılık", "liyakat", "adil", "hak", "şans"], "zorluk": "orta", "aciklama": "Tüm bireylere başarı ve gelişim için adil ve eşit imkanlar sunmak."},
    {"kelime": "hayvan refahını gözetmek", "yasakli_kelimeler": ["canlı", "eziyet", "deney", "şefkat", "yaşam hakkı"], "zorluk": "orta", "aciklama": "Hayvanlara acı çektirmemek ve yaşam şartlarını insani tutmak."},
    {"kelime": "şeffaf davranmak", "yasakli_kelimeler": ["açıklık", "gizli olmamak", "hesap verebilirlik", "dürüst", "denetim"], "zorluk": "orta", "aciklama": "Süreçleri ve kararları herkesin görebileceği açık biçimde yürütmek."},
    {"kelime": "sadakat göstermek", "yasakli_kelimeler": ["bağlılık", "vefa", "ihanet etmemek", "güven", "dostluk"], "zorluk": "orta", "aciklama": "İlişkilerinde ve görevinde bağlılık ve doğruluktan ayrılmamak."},
    {"kelime": "liyakat esas almak", "yasakli_kelimeler": ["hak ediş", "yeterlilik", "torpil", "beceri", "atama"], "zorluk": "orta", "aciklama": "Görev dağılımında akrabalık veya tanıdıklık yerine yetkinliği ölçü almak."},
    {"kelime": "rüşveti reddetmek", "yasakli_kelimeler": ["para", "hediye", "yolsuzluk", "teklif", "haram"], "zorluk": "orta", "aciklama": "Haksız kazanç ve nüfuz sağlama amaçlı maddi teklifleri geri çevirmek."},
    {"kelime": "etik kurula başvurmak", "yasakli_kelimeler": ["onay", "araştırma", "komite", "değerlendirme", "proje"], "zorluk": "orta", "aciklama": "Araştırmanın ahlaki uygunluğunu denetletmek için komiteden izin almak."},
    {"kelime": "hakkı teslim etmek", "yasakli_kelimeler": ["takdir", "emek", "itiraf", "övgü", "pay"], "zorluk": "orta", "aciklama": "Bir başarı veya eserdeki gerçek pay sahibinin hakkını açıkça teslim etmek."},
    {"kelime": "ayrımcılık yapmamak", "yasakli_kelimeler": ["ırk", "cinsiyet", "din", "eşitlik", "dışlama"], "zorluk": "orta", "aciklama": "İnsanlara köken, inanç veya cinsiyetlerine göre haksız muamele etmemek."},
    {"kelime": "hesap verebilirlik sergilemek", "yasakli_kelimeler": ["sorumluluk", "açıklama", "denetim", "rapor", "şeffaflık"], "zorluk": "orta", "aciklama": "Aldığı kararların ve harcamaların hesabını topluma vermeye hazır olmak."},
    {"kelime": "insan onurunu yüceltmek", "yasakli_kelimeler": ["haysiyet", "şeref", "değer", "insan hakları", "aşağılamama"], "zorluk": "orta", "aciklama": "Her bireyin doğuştan sahip olduğu şeref ve haysiyete saygı göstermek."},
    {"kelime": "sosyal sorumluluk üstlenmek", "yasakli_kelimeler": ["toplum", "fayda", "proje", "gönüllülük", "yardım"], "zorluk": "orta", "aciklama": "Toplumun refahı ve dezavantajlı grupların kalkınması için sorumluluk almak."},
    {"kelime": "meslek ahlakına uymak", "yasakli_kelimeler": ["deontoloji", "kural", "standart", "dürüstlük", "disiplin"], "zorluk": "orta", "aciklama": "İcra edilen mesleğin evrensel etik ilkelerine sadık kalmak."},

    # Zor (14)
    {"kelime": "kategorik buyruğa uymak", "yasakli_kelimeler": ["kant", "ödev ahlakı", "evrensel yasa", "maksim", "şartsız"], "zorluk": "zor", "aciklama": "Eylemin maksiminin evrensel bir yasa olmasını isteyecek biçimde davranmak."},
    {"kelime": "faydacılık ilkesini uygulamak", "yasakli_kelimeler": ["utilitarianism", "en büyük mutluluk", "bentham", "mill", "çoğunluk"], "zorluk": "zor", "aciklama": "En çok sayıda insana en yüksek fayda ve mutluluğu getiren seçeneği seçmek."},
    {"kelime": "erdam etiğini benimsemek", "yasakli_kelimeler": ["aristoteles", "altın orta", "karakter", "fazilet", "erdem"], "zorluk": "zor", "aciklama": "Ahlaki doğruluğu kurallardan ziyade iyi ve erdemli karakter geliştirmede aramak."},
    {"kelime": "trolley problemini tartışmak", "yasakli_kelimeler": ["tramvay ikilemi", "makas değiştirmek", "bir kişi beş kişi", "feda", "etik çıkmaz"], "zorluk": "zor", "aciklama": "Beş kişiyi kurtarmak için bir kişiyi feda etmenin ahlakiliğini sorgulamak."},
    {"kelime": "deontolojik karar vermek", "yasakli_kelimeler": ["ödev etiği", "sonuçtan bağımsız", "kural", "kant", "görev"], "zorluk": "zor", "aciklama": "Eylemin sonucuna bakılmaksızın sadece ödeve ve kurala uygunluğuna göre hareket etmek."},
    {"kelime": "sonuçsalcılığı savunmak", "yasakli_kelimeler": ["teleoloji", "eylem sonucu", "netice", "iyi", "değerlendirme"], "zorluk": "zor", "aciklama": "Bir eylemin ahlaki değerini yalnızca doğurduğu neticelerle ölçmek."},
    {"kelime": "biyoetik konsültasyon istemek", "yasakli_kelimeler": ["tıbbi etik", "yaşam sonu kararları", "ötenazi", "genetik müdahale", "komite"], "zorluk": "zor", "aciklama": "Karmaşık tıbbi etik vakalarda uzman heyetinden görüş talep etmek."},
    {"kelime": "altın ortayı bulmak", "yasakli_kelimeler": ["mesotes", "aşırılık", "eksiklik", "denge", "aristoteles"], "zorluk": "zor", "aciklama": "İki uç aşırılık arasındaki dengeli ve erdemli orta yolu tutturmak."},
    {"kelime": "ahlaki rölativizmi sorgulamak", "yasakli_kelimeler": ["görecelilik", "kültür", "evrensel ahlak yokluğu", "öznel", "değişken"], "zorluk": "zor", "aciklama": "Ahlaki doğruların toplumlara ve kültürlere göre değiştiği tezini tartışmak."},
    {"kelime": "metaetik analiz yapmak", "yasakli_kelimeler": ["iyinin tanımı", "ahlak felsefesi", "dil", "önerme", "anlam"], "zorluk": "zor", "aciklama": "Ahlaki yargıların ve 'iyi', 'kötü' kavramlarının anlamsal doğasını incelemek."},
    {"kelime": "adli tıp etiğini gözetmek", "yasakli_kelimeler": ["otopsi", "tarafsız rapor", "delil karartmama", "adalet", "mahkeme"], "zorluk": "zor", "aciklama": "Adli rapor tanziminde hiçbir baskı altında kalmadan mutlak bilimsel doğruyu yazmak."},
    {"kelime": "algoritmik yanlılığı önlemek", "yasakli_kelimeler": ["yapay zeka etiği", "bias", "ayrımcı veri", "adalet", "model"], "zorluk": "zor", "aciklama": "Yapay zeka algoritmalarının toplumdaki önyargıları pekiştirmesini engellemek."},
    {"kelime": "çifte etki doktrinini gözetmek", "yasakli_kelimeler": ["aquinas", "öngörülen yan etki", "iyi niyet", "kötü sonuç", "orantılılık"], "zorluk": "zor", "aciklama": "İyi amaçlı bir eylemin kaçınılmaz kötü yan etkisinin ahlaki sınırını tartmak."},
    {"kelime": "evrensel ahlak yasası aramak", "yasakli_kelimeler": ["nesnel etik", "tüm insanlık", "bağlayıcı", "norm", "değer"], "zorluk": "zor", "aciklama": "Zaman ve mekandan bağımsız tüm insanlık için bağlayıcı ilkeleri temellendirmek."}
]

add_and_save_verbs('ergonomi', ergonomi_verbs)
add_and_save_verbs('etik', etik_verbs)
print('P4 done!')
