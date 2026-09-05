# -*- coding: utf-8 -*-
from card_utils import add_and_save_verbs

pazarlama_verbs = [
    # Kolay (12)
    {"kelime": "satmak", "aciklama": "üretilen mal veya hizmeti bedeli karşılığı müşteriye devretmek", "yasakli_kelimeler": ["ürün", "hizmet", "müşteri", "bedel", "para"], "zorluk": "kolay"},
    {"kelime": "reklam yapmak", "aciklama": "ürünü tanıtmak için televizyon, afiş veya internete ilan vermek", "yasakli_kelimeler": ["ilan", "tanıtım", "televizyon", "afiş", "kampanya"], "zorluk": "kolay"},
    {"kelime": "tanıtmak", "aciklama": "yeni çıkan ürünün özelliklerini müşterilere anlatmak", "yasakli_kelimeler": ["anlatmak", "özellik", "lansman", "sunum", "müşteri"], "zorluk": "kolay"},
    {"kelime": "kampanya başlatmak", "aciklama": "satışları artırmak için belirli süreli indirim ve promosyon duyurmak", "yasakli_kelimeler": ["indirim", "promosyon", "duyuru", "satış artırma", "fırsat"], "zorluk": "kolay"},
    {"kelime": "fiyatlandırmak", "aciklama": "ürünün maliyetine ve piyasa durumuna göre satış etiketini belirlemek", "yasakli_kelimeler": ["etiket", "ücret", "maliyet", "piyasa", "belirlemek"], "zorluk": "kolay"},
    {"kelime": "ikna etmek", "aciklama": "kararsız müşteriyi ürünün faydalarına inandırıp satın aldırmak", "yasakli_kelimeler": ["inandırmak", "fayda", "satın alma", "müşteri", "iletişim"], "zorluk": "kolay"},
    {"kelime": "araştırmak", "aciklama": "tüketicilerin ne istediğini ve rakiplerin ne yaptığını incelemek", "yasakli_kelimeler": ["tüketici", "rakip", "pazar araştırması", "istek", "anket"], "zorluk": "kolay"},
    {"kelime": "afiş asmak", "aciklama": "reklam panolarına veya mağaza camlarına görsel duyurular yapıştırmak", "yasakli_kelimeler": ["poster", "pano", "billboard", "yapıştırmak", "görsel"], "zorluk": "kolay"},
    {"kelime": "broşür dağıtmak", "aciklama": "sokakta veya fuarda ürün bilgilerini içeren el ilanlarını dağıtmak", "yasakli_kelimeler": ["el ilanı", "fuar", "kağıt", "dağıtım", "bilgi"], "zorluk": "kolay"},
    {"kelime": "indirim yapmak", "aciklama": "ürün fiyatını yüzde olarak aşağı çekip cazip hale getirmek", "yasakli_kelimeler": ["ucuzluk", "yüzde", "fiyat düşürme", "cazip", "etiket"], "zorluk": "kolay"},
    {"kelime": "markalaşmak", "aciklama": "bir şirketin veya ürünün pazarda güven ve bilinirlik kazanması", "yasakli_kelimeler": ["bilinirlik", "güven", "isim", "logo", "itibar"], "zorluk": "kolay"},
    {"kelime": "müşteri bulmak", "aciklama": "satış potansiyeli olan yeni kişi ve kurumlarla temas kurmak", "yasakli_kelimeler": ["aday", "potansiyel", "temas", "portföy", "ulaşmak"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "hedef kitle belirlemek", "aciklama": "ürünün hitap edeceği yaş, gelir ve cinsiyet grubunu tespit etmek", "yasakli_kelimeler": ["segmentasyon", "yaş grubu", "gelir", "kitle", "tüketici"], "zorluk": "orta"},
    {"kelime": "lansman yapmak", "aciklama": "yeni bir ürünü basın ve davetliler önünde ilk kez sahneye çıkarmak", "yasakli_kelimeler": ["ürün lansmanı", "tanıtım gecesi", "basın", "ilk çıkış", "sahne"], "zorluk": "orta"},
    {"kelime": "dijital reklam vermek", "aciklama": "google ve sosyal medya platformlarında tıklama başı bütçeli reklam açmak", "yasakli_kelimeler": ["google ads", "sosyal medya", "tıklama", "bütçe", "dijital"], "zorluk": "orta"},
    {"kelime": "influencer ile çalışmak", "aciklama": "takipçisi çok olan sosyal medya fenomenine ürün tanıtımı yaptırmak", "yasakli_kelimeler": ["fenomen", "iş birliği", "instagram", "takipçi", "story"], "zorluk": "orta"},
    {"kelime": "anket uygulamak", "aciklama": "müşteri memnuniyetini veya pazar talebini ölçmek için soru sormak", "yasakli_kelimeler": ["soru formu", "memnuniyet", "pazar araştırması", "ölçüm", "cevap"], "zorluk": "orta"},
    {"kelime": "sponsor olmak", "aciklama": "marka bilinirliği için spor veya sanat etkinliklerine maddi destek vermek", "yasakli_kelimeler": ["sponsorluk", "etkinlik", "forma", "maddi destek", "logo"], "zorluk": "orta"},
    {"kelime": "pazar payı artırmak", "aciklama": "sektördeki toplam satış hacmi içindeki şirketin yüzdesini büyütmek", "yasakli_kelimeler": ["pazar payı", "yüzde", "sektör", "rakip", "büyüme"], "zorluk": "orta"},
    {"kelime": "konumlandırma yapmak", "aciklama": "markayı müşterinin zihninde ucuz, lüks veya kaliteli algısıyla yerleştirmek", "yasakli_kelimeler": ["positioning", "algı", "zihin", "lüks", "farklılaşma"], "zorluk": "orta"},
    {"kelime": "sadakat programı kurmak", "aciklama": "sürekli gelen müşterilere puan ve özel avantajlar veren kart sistemi yapmak", "yasakli_kelimeler": ["puan", "sadakat kartı", "avantaj", "sürekli müşteri", "ödül"], "zorluk": "orta"},
    {"kelime": "bülten göndermek", "aciklama": "abone olan müşterilere e-posta ile haftalık kampanya ve içerik yollamak", "yasakli_kelimeler": ["newsletter", "e-posta", "abone", "mailing", "duyuru"], "zorluk": "orta"},
    {"kelime": "rakip analizi yapmak", "aciklama": "pazardaki rakip firmaların fiyat, kalite ve reklam stratejilerini izlemek", "yasakli_kelimeler": ["rakip", "strateji", "kıyaslama", "fiyat karşılaştırma", "benchmark"], "zorluk": "orta"},
    {"kelime": "fuara katılmak", "aciklama": "sektörel ticaret fuarında stant açıp kurumsal ziyaretçiler ağırlamak", "yasakli_kelimeler": ["stant", "sektörel", "ziyaretçi", "kartvizit", "ticaret"], "zorluk": "orta"},
    {"kelime": "yeniden hedeflemek", "aciklama": "web sitesini gezip bir şey almadan çıkan kullanıcının karşısına tekrar reklam çıkarmak", "yasakli_kelimeler": ["retargeting", "çerez", "tekrar reklam", "ziyaretçi", "dönüşüm"], "zorluk": "orta"},
    {"kelime": "amblem tasarlatmak", "aciklama": "grafik tasarımcıya markayı temsil eden özgün logo ve kurumsal kimlik çizdirmek", "yasakli_kelimeler": ["logo", "kurumsal kimlik", "vektör", "grafik", "sembol"], "zorluk": "orta"},
    {"kelime": "slogan bulmak", "aciklama": "akılda kalıcı, vurucu ve markayı özetleyen kısa reklam cümlesi yazmak", "yasakli_kelimeler": ["motto", "akılda kalıcı", "cümle", "metin yazarı", "özet"], "zorluk": "orta"},
    {"kelime": "çapraz satış yapmak", "aciklama": "ayakkabı alan müşteriye bakım spreyi veya çorap da teklif edip satmak", "yasakli_kelimeler": ["cross-sell", "ek ürün", "tamamlayıcı", "teklif", "sepet artırma"], "zorluk": "orta"},
    {"kelime": "üst satış denemek", "aciklama": "müşteriye seçtiği modelin daha donanımlı ve pahalı üst versiyonunu satmak", "yasakli_kelimeler": ["upsell", "üst model", "pahalı", "donanım", "fiyat artırma"], "zorluk": "orta"},
    {"kelime": "katalog bastırmak", "aciklama": "tüm ürün yelpazesini fotoğrafları ve teknik özellikleriyle kuşe kağıda basmak", "yasakli_kelimeler": ["ürün listesi", "kuşe kağıt", "baskı", "fotoğraf", "sayfa"], "zorluk": "orta"},
    {"kelime": "vitrin tasarımı yapmak", "aciklama": "mağaza önünden geçenlerin dikkatini çekecek tematik vitrin dekore etmek", "yasakli_kelimeler": ["görsel mağazacılık", "mannequin", "dekor", "cadde", "dikkat çekme"], "zorluk": "orta"},
    {"kelime": "tüketici içgörüsü yakalamak", "aciklama": "müşterinin dile getirmediği derin psikolojik ihtiyaç ve motivasyonunu keşfetmek", "yasakli_kelimeler": ["insight", "ihtiyaç", "motivasyon", "psikoloji", "derin"], "zorluk": "orta"},
    {"kelime": "basın bülteni dağıtmak", "aciklama": "şirketin yeni başarısını veya ürününü gazete ve haber sitelerine servis etmek", "yasakli_kelimeler": ["pr", "medya", "haber ajansı", "gazeteci", "duyuru"], "zorluk": "orta"},
    {"kelime": "fiyat kırmak", "aciklama": "rakibi pazardan silmek veya stok eritmek için zararına satış yapmak", "yasakli_kelimeler": ["damping", "zararına", "ucuzlatmak", "fiyat savaşı", "stok eritme"], "zorluk": "orta"},
    {"kelime": "viral olmak", "aciklama": "hazırlanan reklam videosunun kullanıcılar tarafından hızla paylaşılıp yayılması", "yasakli_kelimeler": ["paylaşım", "video", "patlama", "hızlı yayılma", "sosyal medya"], "zorluk": "orta"},
    {"kelime": "odak grup toplantısı", "aciklama": "tüketicileri masa etrafında toplayıp yeni ürün prototipini tartıştırmak", "yasakli_kelimeler": ["focus grup", "moderatör", "tartışma", "prototip", "geri bildirim"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "4p karması oluşturmak", "aciklama": "ürün, fiyat, dağıtım ve tutundurma stratejilerini bütünleşik planlamak", "yasakli_kelimeler": ["marketing mix", "ürün fiyat dağıtım", "tutundurma", "kotler", "temel karma"], "zorluk": "zor"},
    {"kelime": "growth hacking uygulamak", "aciklama": "düşük bütçeli yaratıcı yazılım ve pazarlama hileleriyle kullanıcı sayısını katlamak", "yasakli_kelimeler": ["hızlı büyüme", "düşük bütçe", "korsan", "otomasyon", "deney"], "zorluk": "zor"},
    {"kelime": "müşteri yaşam boyu değeri", "aciklama": "bir müşterinin şirketle olan tüm ilişkisi boyunca bırakacağı toplam net karı hesaplamak", "yasakli_kelimeler": ["clv", "ltv", "toplam kar", "ilişki süresi", "metrik"], "zorluk": "zor"},
    {"kelime": "churn oranını düşürmek", "aciklama": "abonelikten çıkan veya rakibe kaçan müşteri kaybı yüzdesini aşağı çekmek", "yasakli_kelimeler": ["müşteri kaybı", "terk", "iptal oranı", "tutundurma", "abonelik"], "zorluk": "zor"},
    {"kelime": "cac optimizasyonu yapmak", "aciklama": "yeni bir müşteri kazanmak için harcanan toplam reklam maliyetini azaltmak", "yasakli_kelimeler": ["müşteri edinme maliyeti", "edinme bedeli", "harcama", "verimlilik", "karlılık"], "zorluk": "zor"},
    {"kelime": "dönüşüm hunisi kurmak", "aciklama": "farkındalıktan satın almaya kadar adım adım müşteri dönüşüm hunisi tasarlamak", "yasakli_kelimeler": ["funnel", "aida", "farkındalık", "satın alma adımı", "kayıp oranı"], "zorluk": "zor"},
    {"kelime": "a/b testi yürütmek", "aciklama": "web sayfası veya reklamın iki farklı varyantını eşzamanlı gösterip tıklamayı kıyaslamak", "yasakli_kelimeler": ["varyant", "split test", "kıyaslama", "tıklama oranı", "istatistik"], "zorluk": "zor"},
    {"kelime": "omnichannel entegrasyon", "aciklama": "fiziksel mağaza, mobil uygulama ve web sitesi alışveriş deneyimini kusursuz bağlamak", "yasakli_kelimeler": ["çok kanallı", "bütünleşik", "mağaza web mobil", "kesintisiz deneyim", "kanal"], "zorluk": "zor"},
    {"kelime": "nps skoru ölçmek", "aciklama": "tavsiye etme eğilimine göre net tavsiye skorunu destekçi ve köstekçilerden çıkarmak", "yasakli_kelimeler": ["net promoter score", "tavsiye", "destekçi", "köstekçi", "0-10 puan"], "zorluk": "zor"},
    {"kelime": "pazarlama otomasyonu kurmak", "aciklama": "kullanıcı hareketlerine göre otomatik tetiklenen kişiselleştirilmiş e-posta ve bildirim kurgulamak", "yasakli_kelimeler": ["otomasyon", "tetikleyici", "hubspot", "kişiselleştirme", "iş akışı"], "zorluk": "zor"},
    {"kelime": "gerilla pazarlama yapmak", "aciklama": "geleneksel olmayan şaşırtıcı ve düşük maliyetli sokak eylemleriyle sansasyon yaratmak", "yasakli_kelimeler": ["alışılmadık", "şaşırtma", "sokak eylemi", "düşük bütçe", "sansasyon"], "zorluk": "zor"},
    {"kelime": "nöropazarlama uygulamak", "aciklama": "reklama bakan tüketicinin beyin dalgalarını ve göz bebek hareketlerini ölçmek", "yasakli_kelimeler": ["eye tracking", "eeg", "bilinçaltı", "beyin tepkisi", "biyometrik"], "zorluk": "zor"},
    {"kelime": "seo stratejisi kurgulamak", "aciklama": "arama motoru sonuç sayfalarında organik olarak ilk sıraya çıkacak içerik mimarisi yapmak", "yasakli_kelimeler": ["arama motoru optimizasyonu", "organik trafik", "anahtar kelime", "backlink", "google sıra"], "zorluk": "zor"},
    {"kelime": "marka denkliği inşa etmek", "aciklama": "ismin tüketici algısındaki finansal ve duygusal toplam değer gücünü yükseltmek", "yasakli_kelimeler": ["brand equity", "finansal değer", "duygusal bağ", "saygınlık", "soyut varlık"], "zorluk": "zor"}
]

pedagoji_verbs = [
    # Kolay (12)
    {"kelime": "eğitmek", "aciklama": "çocuğa bilgi, beceri ve ahlaki değerler kazandırmak", "yasakli_kelimeler": ["öğretmek", "çocuk", "beceri", "ahlak", "bilgi"], "zorluk": "kolay"},
    {"kelime": "öğretmek", "aciklama": "yeni bir konuyu veya kuralı çocuğun anlamasını sağlamak", "yasakli_kelimeler": ["anlatmak", "bilgi", "kural", "kavratmak", "ders"], "zorluk": "kolay"},
    {"kelime": "oynamak", "aciklama": "çocuğun eğlenerek öğrenmesi için oyun kurmak ve katılmak", "yasakli_kelimeler": ["oyun", "oyuncak", "eğlence", "katılmak", "etkinlik"], "zorluk": "kolay"},
    {"kelime": "dinlemek", "aciklama": "çocuğun anlattıklarına göz teması kurarak dikkatle kulak vermek", "yasakli_kelimeler": ["kulak vermek", "göz teması", "anlatılan", "sabır", "çocuk"], "zorluk": "kolay"},
    {"kelime": "ödüllendirmek", "aciklama": "olumlu davranış gösteren çocuğu takdir veya küçük hediyeyle pekiştirmek", "yasakli_kelimeler": ["takdir", "aferin", "hediye", "olumlu", "pekiştireç"], "zorluk": "kolay"},
    {"kelime": "yönlendirmek", "aciklama": "çocuğun ilgi ve yeteneklerine uygun aktivitelere teşvik etmek", "yasakli_kelimeler": ["teşvik", "yetenek", "ilgi", "rehberlik", "aktivite"], "zorluk": "kolay"},
    {"kelime": "sevgi göstermek", "aciklama": "çocuğa sarılarak ve şefkatle yaklaşarak güven hissi vermek", "yasakli_kelimeler": ["şefkat", "sarılmak", "güven", "ilgi", "duygu"], "zorluk": "kolay"},
    {"kelime": "sabretmek", "aciklama": "çocuğun öğrenme ve gelişim sürecinde öfkelenmeden beklemek", "yasakli_kelimeler": ["öfkelenmemek", "beklemek", "anlayış", "sakinlik", "tahammül"], "zorluk": "kolay"},
    {"kelime": "anlamak", "aciklama": "çocuğun korkularını, kaygılarını ve duygusal dünyasını kavramak", "yasakli_kelimeler": ["empati", "korku", "kaygı", "duygu", "kavramak"], "zorluk": "kolay"},
    {"kelime": "masal anlatmak", "aciklama": "hayal gücünü geliştirmek ve ders çıkarmasını sağlamak için hikaye okumak", "yasakli_kelimeler": ["hikaye", "hayal gücü", "kitap", "anlatı", "uyku öncesi"], "zorluk": "kolay"},
    {"kelime": "korumak", "aciklama": "çocuğu fiziksel ve psikolojik tehlikelerden uzak tutmak", "yasakli_kelimeler": ["tehlike", "fiziksel", "psikolojik", "güvenlik", "kollamak"], "zorluk": "kolay"},
    {"kelime": "model olmak", "aciklama": "doğru davranışları bizzat sergileyerek çocuğa örnek oluşturmak", "yasakli_kelimeler": ["örnek", "davranış", "taklit", "sergilemek", "büyükler"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "özgüven aşılamak", "aciklama": "çocuğun kendi kararlarını alabilmesi ve yapabileceğine inanmasını sağlamak", "yasakli_kelimeler": ["özgüven", "cesaret", "başarabilme", "kendi başına", "inanç"], "zorluk": "orta"},
    {"kelime": "sınır koymak", "aciklama": "çocuğa kuralları ve özgürlüğünün nerede bittiğini net şekilde öğretmek", "yasakli_kelimeler": ["kural", "çerçeve", "disiplin", "net", "öğretme"], "zorluk": "orta"},
    {"kelime": "empati kurmak", "aciklama": "olaylara çocuğun gözünden bakarak onun hissettiklerini anlamak", "yasakli_kelimeler": ["çocuk gözü", "his", "duygu paylaşımı", "anlayış", "yaklaşım"], "zorluk": "orta"},
    {"kelime": "öfke nöbetini yönetmek", "aciklama": "çocuğun ağlama ve tepinme krizinde sakin kalarak yatışmasını beklemek", "yasakli_kelimeler": ["tantrum", "kriz", "ağlama", "tepinme", "sakinleşme"], "zorluk": "orta"},
    {"kelime": "tuvalet eğitimi vermek", "aciklama": "bezin bırakılıp lazımlık veya klozete yapma alışkanlığını kazandırmak", "yasakli_kelimeler": ["lazımlık", "bez", "klozet", "çiş", "alışkanlık"], "zorluk": "orta"},
    {"kelime": "akran iletişimini desteklemek", "aciklama": "parkta veya kreşte diğer çocuklarla paylaşma ve sıra bekleme pratiği yaptırmak", "yasakli_kelimeler": ["paylaşma", "kreş", "arkadaş", "sıra bekleme", "sosyalleşme"], "zorluk": "orta"},
    {"kelime": "ince motor geliştirmek", "aciklama": "makas kesme, hamur yoğurma ve boncuk dizmeyle parmak kaslarını güçlendirmek", "yasakli_kelimeler": ["parmak kası", "makas", "oyun hamuru", "boncuk", "el becerisi"], "zorluk": "orta"},
    {"kelime": "kaba motor çalıştırmak", "aciklama": "koşma, zıplama ve tırmanma oyunlarıyla büyük kas koordinasyonunu artırmak", "yasakli_kelimeler": ["büyük kas", "koşma", "zıplama", "tırmanma", "denge"], "zorluk": "orta"},
    {"kelime": "montessori uygulamak", "aciklama": "çocuğun kendi hızında ve ilgi duyduğu ahşap materyallerle bağımsız öğrenmesi", "yasakli_kelimeler": ["maria montessori", "ahşap materyal", "bağımsızlık", "kendi hızı", "özgür seçim"], "zorluk": "orta"},
    {"kelime": "waldorf yaklaşımı izlemek", "aciklama": "doğal malzemeler, masallar ve sanatsal ritimlerle çocuğu bütüncül yetiştirmek", "yasakli_kelimeler": ["rudolf steiner", "doğal", "sanat", "bütüncül", "ritim"], "zorluk": "orta"},
    {"kelime": "reggio emilia modeli", "aciklama": "çocuğun yüz dili olduğunu savunarak proje tabanlı çevre etkileşimi kurmak", "yasakli_kelimeler": ["yüz dil", "atölye", "çevre", "proje", "keşif"], "zorluk": "orta"},
    {"kelime": "olumlu pekiştirmek", "aciklama": "istenilen davranış sergilendiğinde hemen takdir ederek davranışın kalıcılığını sağlamak", "yasakli_kelimeler": ["pekiştireç", "övgü", "davranışçı", "ödül", "sıklık"], "zorluk": "orta"},
    {"kelime": "gelişim takibi yapmak", "aciklama": "boy, kilo, dil ve sosyal becerilerin persentil tablosundaki yerini izlemek", "yasakli_kelimeler": ["persentil", "yaş basamağı", "dil gelişimi", "milestone", "tablo"], "zorluk": "orta"},
    {"kelime": "sorumluluk vermek", "aciklama": "odasını toplama, sofrayı kurma veya çiçeği sulama gibi küçük görevler teslim etmek", "yasakli_kelimeler": ["görev", "oda toplama", "özbakım", "ev işi", "sorumluluk bilinci"], "zorluk": "orta"},
    {"kelime": "ekran süresini sınırlamak", "aciklama": "tablet, telefon ve televizyon karşısında geçirilen zamanı kontrol altında tutmak", "yasakli_kelimeler": ["tablet", "telefon", "televizyon", "mavi ışık", "dijital detoks"], "zorluk": "orta"},
    {"kelime": "uyku rutini oluşturmak", "aciklama": "her gece aynı saatte ılık banyo, pijama ve kitap okuma döngüsü kurmak", "yasakli_kelimeler": ["uyku saati", "banyo", "kitap okuma", "düzen", "yatak"], "zorluk": "orta"},
    {"kelime": "kardeş kıskançlığını çözmek", "aciklama": "yeni doğan bebekle büyük çocuk arasındaki sevgi dengesini korumak", "yasakli_kelimeler": ["yeni bebek", "kıskançlık", "büyük çocuk", "ilgi bölünmesi", "denge"], "zorluk": "orta"},
    {"kelime": "dil gelişimini desteklemek", "aciklama": "çocukla sürekli konuşarak, sorular sorarak kelime dağarcığını zenginleştirmek", "yasakli_kelimeler": ["kelime haznesi", "konuşma", "telaffuz", "soru sorma", "artikülasyon"], "zorluk": "orta"},
    {"kelime": "duyusal oyun kurmak", "aciklama": "su, kum, pirinç veya tıraş köpüğüyle duyuları uyaran havuzlar hazırlamak", "yasakli_kelimeler": ["duyu havuzu", "dokunma", "tıraş köpüğü", "kum", "keşif"], "zorluk": "orta"},
    {"kelime": "özbakım becerisi kazandırmak", "aciklama": "ayakkabısını giyme, dişini fırçalama ve montunu iliklemeyi öğretmek", "yasakli_kelimeler": ["kendi giyinme", "diş fırçalama", "fermuar", "bağımsız", "temizlik"], "zorluk": "orta"},
    {"kelime": "ayrılık kaygısını yatıştırmak", "aciklama": "kreşe başlarken anneden kopmakta zorlanan çocuğa güvenli veda etmek", "yasakli_kelimeler": ["kreş başlangıcı", "güvenli bağlanma", "anne bağı", "ağlama", "veda"], "zorluk": "orta"},
    {"kelime": "etkin dinleme yapmak", "aciklama": "sözünü kesmeden, söylediklerini tekrar ederek anlaşıldığını hissettirmek", "yasakli_kelimeler": ["söz kesmeme", "anlaşıldım", "tekrar", "göz hizası", "iletişim"], "zorluk": "orta"},
    {"kelime": "koşulsuz kabul etmek", "aciklama": "çocuğu başarısından veya hatalarından bağımsız olarak olduğu gibi sevmek", "yasakli_kelimeler": ["şartsız sevgi", "olduğu gibi", "kabul", "hata", "değerlilik"], "zorluk": "orta"},
    {"kelime": "ben dili kullanmak", "aciklama": "suçlayıcı sen dili yerine davranışın üzerindeki etkisini ifade etmek", "yasakli_kelimeler": ["suçlamama", "ifade", "iletişim tekniği", "duygu anlatımı", "sen dili"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "yakınsak gelişim alanını işletmek", "aciklama": "vygotsky'nin çocuğun tek başına yapamadığı ama yetişkin desteğiyle başardığı alan", "yasakli_kelimeler": ["zpd", "vygotsky", "iskele kurma", "scaffolding", "potansiyel"], "zorluk": "zor"},
    {"kelime": "bilişsel evreleri çözümlemek", "aciklama": "piaget'nin duyusal-motor, işlem öncesi ve somut işlemler basamaklarını izlemek", "yasakli_kelimeler": ["piaget", "duyusal motor", "işlem öncesi", "somut işlemler", "korunum"], "zorluk": "zor"},
    {"kelime": "güvenli bağlanma kurmak", "aciklama": "bowlby ve ainsworth'ün bebek ile anne arasındaki tutarlı güven bağını inşa etmek", "yasakli_kelimeler": ["john bowlby", "ainsworth", "yabancı durum", "tutarlı tepki", "bağlanma stili"], "zorluk": "zor"},
    {"kelime": "psikososyal krizleri aşmak", "aciklama": "erikson'un temel güvene karşı güvensizlik ve özerkliğe karşı kuşku evreleri", "yasakli_kelimeler": ["erik erikson", "özerklik", "temel güven", "kimlik", "evrim"], "zorluk": "zor"},
    {"kelime": "çoklu zeka alanlarını beslemek", "aciklama": "gardner'ın müzikal, kinestetik, uzamsal ve mantıksal zeka kuramını uygulamak", "yasakli_kelimeler": ["howard gardner", "kinestetik", "uzamsal", "müzikal", "8 zeka"], "zorluk": "zor"},
    {"kelime": "ahlaki muhakemeyi geliştirmek", "aciklama": "kohlberg'in gelenek öncesi, geleneksel ve ötesi ahlak evrelerinde basamak atlatmak", "yasakli_kelimeler": ["kohlberg", "heinz ikilemi", "ahlak gelişimi", "geleneksel", "yargı"], "zorluk": "zor"},
    {"kelime": "davranış modifikasyonu yapmak", "aciklama": "uygulamalı davranış analizi ile otizmli veya gelişimsel gecikmeli çocuğa beceri kazandırmak", "yasakli_kelimeler": ["aba", "ayrık denemeler", "edimsel koşullanma", "skinner", "söndürme"], "zorluk": "zor"},
    {"kelime": "duyu bütünleme terapisi", "aciklama": "vestibüler ve propriyoseptif duyusal girdileri salıncak ve parkurda düzenlemek", "yasakli_kelimeler": ["propriyoseptif", "vestibüler", "jean ayres", "salıncak", "duyu bütünleme"], "zorluk": "zor"},
    {"kelime": "sosyal öğrenmeyi modellemek", "aciklama": "bandura'nın bobo doll deneyindeki gibi gözlem ve taklitle öğrenmeyi kurgulamak", "yasakli_kelimeler": ["albert bandura", "bobo doll", "gözlem", "taklit", "dolaylı pekiştirme"], "zorluk": "zor"},
    {"kelime": "metakognitif düşünceyi açmak", "aciklama": "çocuğa kendi düşünme süreçlerinin ve nasıl öğrendiğinin farkındalığını kazandırmak", "yasakli_kelimeler": ["üstbiliş", "öğrenmeyi öğrenme", "öz düzenleme", "farkındalık", "düşünme"], "zorluk": "zor"},
    {"kelime": "transaksiyonel analiz yapmak", "aciklama": "ebeveyn, yetişkin ve çocuk ego durumları arasındaki iletişim çatışmalarını çözmek", "yasakli_kelimeler": ["eric berne", "ego durumları", "ebeveyn yetişkin çocuk", "temas iletisi", "analiz"], "zorluk": "zor"},
    {"kelime": "özerkliği desteklemek", "aciklama": "öz belirleme kuramı uyarınca çocuğun içsel motivasyonunu ve yetkinliğini beslemek", "yasakli_kelimeler": ["öz belirleme", "içsel motivasyon", "yetkinlik", "özerklik desteği", "deci ryan"], "zorluk": "zor"},
    {"kelime": "ekolojik sistem analizi", "aciklama": "bronfenbrenner'ın mikro, mezo, ekzo ve makro sistemlerinin çocuk gelişimine etkisi", "yasakli_kelimeler": ["bronfenbrenner", "mikrosistem", "çevre katmanları", "mezosistem", "bağlam"], "zorluk": "zor"},
    {"kelime": "bibliyoterapi uygulamak", "aciklama": "çocuğun travma veya korkusunu özel seçilmiş hikaye kitaplarındaki karakterlerle sağaltmak", "yasakli_kelimeler": ["sağaltım", "kitapla terapi", "karakter özdeşimi", "katarsis", "travma"], "zorluk": "zor"}
]

if __name__ == "__main__":
    add_and_save_verbs("pazarlama", pazarlama_verbs)
    add_and_save_verbs("pedagoji", pedagoji_verbs)
