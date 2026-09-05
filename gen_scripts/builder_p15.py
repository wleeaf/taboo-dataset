import os, sys, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gen_scripts.card_utils import add_and_save_verbs

# 29. kahve
kahve_verbs = [
    # Kolay (12)
    {"kelime": "kahve içmek", "yasakli_kelimeler": ["fincan", "sıcak", "sabah", "kafein", "yudum"], "zorluk": "kolay", "aciklama": "Hazırlanan sıcak kahve içeceğini yudumlamak."},
    {"kelime": "kahve pişirmek", "yasakli_kelimeler": ["cezve", "türk kahvesi", "ocak", "köpük", "ateş"], "zorluk": "kolay", "aciklama": "Cezvede su ve kahveyi kaynatarak içecek hazırlamak."},
    {"kelime": "şeker eklemek", "yasakli_kelimeler": ["tatlı", "küp", "kaşık", "karıştırmak", "orta"], "zorluk": "kolay", "aciklama": "Acılığı kırmak için kahveye şeker ilave etmek."},
    {"kelime": "kahve çekirdeği öğütmek", "yasakli_kelimeler": ["değirmen", "toz", "çekmek", "tane", "makine"], "zorluk": "kolay", "aciklama": "Kavrulmuş sert çekirdekleri değirmende toz haline getirmek."},
    {"kelime": "köpük yapmak", "yasakli_kelimeler": ["kabarmak", "türk kahvesi", "fincan üstü", "cezve", "krema"], "zorluk": "kolay", "aciklama": "Kahvenin üzerinde zengin köpük tabakası oluşturmak."},
    {"kelime": "fincana dökmek", "yasakli_kelimeler": ["doldurmak", "servis", "kulp", "tabak", "dökmek"], "zorluk": "kolay", "aciklama": "Cezvedeki veya demlikteki kahveyi fincana aktarmak."},
    {"kelime": "lokum ikram etmek", "yasakli_kelimeler": ["tatlı", "yanında", "su", "türk kahvesi", "küçük"], "zorluk": "kolay", "aciklama": "Kahve servisinin yanında geleneksel lokum sunmak."},
    {"kelime": "süt katmak", "yasakli_kelimeler": ["latte", "beyaz", "yumuşatmak", "sıcak", "dökmek"], "zorluk": "kolay", "aciklama": "Kahvenin sertliğini kırmak için içine ılık süt ilave etmek."},
    {"kelime": "kahve koklamak", "yasakli_kelimeler": ["aroma", "güzel koku", "çekirdek", "burun", "taze"], "zorluk": "kolay", "aciklama": "Taze çekilmiş veya demlenmiş kahvenin kokusunu içine çekmek."},
    {"kelime": "soğuk kahve içmek", "yasakli_kelimeler": ["buz", "yaz", "frappe", "ferahlatıcı", "pipet"], "zorluk": "kolay", "aciklama": "Buzla soğutulmuş kahveyi sıcak havalarda tüketmek."},
    {"kelime": "kahvehaneye gitmek", "yasakli_kelimeler": ["kıraathane", "oyun", "çay", "arkadaş", "oturmak"], "zorluk": "kolay", "aciklama": "Geleneksel kahve ve sohbet mekanına uğramak."},
    {"kelime": "filtre kağıdı koymak", "yasakli_kelimeler": ["damlatıcı", "beyaz kağıt", "huni", "kahve makinesi", "yerleştirmek"], "zorluk": "kolay", "aciklama": "Demleme aparatının içine süzücü filtre kağıdını oturtmak."},

    # Orta (24)
    {"kelime": "espresso çekmek", "yasakli_kelimeler": ["basınç", "portafiltre", "bar makinesi", "kısa sert", "shot"], "zorluk": "orta", "aciklama": "Yüksek basınçlı makinede 9 bar kuvvetle yoğun espresso damlatmak."},
    {"kelime": "süt köpürtmek", "yasakli_kelimeler": ["buhar çubuğu", "pitcher", "mikro köpük", "latte art", "krema kıvamı"], "zorluk": "orta", "aciklama": "Buhar çubuğuyla sütün içine hava vererek pürüzsüz mikro köpük yapmak."},
    {"kelime": "tamping yapmak", "yasakli_kelimeler": ["tamper", "sıkıştırmak", "portafiltre", "düzleme", "baskı"], "zorluk": "orta", "aciklama": "Kaşıktaki öğütülmüş kahveyi düzgünce sıkıştırıp düzleştirmek."},
    {"kelime": "latte art yapmak", "yasakli_kelimeler": ["kalp deseni", "lale", "süt dökme", "fincan üzeri", "desen"], "zorluk": "orta", "aciklama": "Köpürtülmüş sütü döküş açısıyla kahve yüzeyine desenler çizmek."},
    {"kelime": "french press ile demlemek", "yasakli_kelimeler": ["piston", "kalın öğütüm", "süzgeç", "dört dakika", "cam hazne"], "zorluk": "orta", "aciklama": "Kalın çekilmiş kahveyi cam haznede bekletip pistonla süzmek."},
    {"kelime": "v60 ile demlemek", "yasakli_kelimeler": ["pour over", "spiral döküş", "hario", "koni", "damlatıcı"], "zorluk": "orta", "aciklama": "Koni şeklindeki filtre tutucuya sıcak suyu dairesel hareketlerle dökmek."},
    {"kelime": "kahve çekirdeği kavurmak", "yasakli_kelimeler": ["roasting", "tambur", "yeşil çekirdek", "first crack", "kahverengi"], "zorluk": "orta", "aciklama": "Yeşil ham kahve tanelerini kavurma makinesinde uygun dereceye getirmek."},
    {"kelime": "aeropress kullanmak", "yasakli_kelimeler": ["hava basıncı", "silindir", "şırınga benzeri", "hızlı demleme", "ters yöntem"], "zorluk": "orta", "aciklama": "Hava basıncıyla çalışan silindirik aparatla manuel kahve demlemek."},
    {"kelime": "cold brew demlemek", "yasakli_kelimeler": ["soğuk demleme", "12 saat", "buzdolabı", "düşük asidite", "sürahi"], "zorluk": "orta", "aciklama": "Kahveyi soğuk suda en az 12 saat boyunca bekleterek demini almak."},
    {"kelime": "cupping yapmak", "yasakli_kelimeler": ["kahve tadımı", "höpürdeterek içme", "koku puanlama", "kaşık", "degüstasyon"], "zorluk": "orta", "aciklama": "Farklı çekirdeklerin aromatik profilini standart tadım protokolüyle test etmek."},
    {"kelime": "mokapot ile ocakta yapmak", "yasakli_kelimeler": ["italyan cezvesi", "alt hazne su", "buhar basıncı", "brikka", "ocak üstü"], "zorluk": "orta", "aciklama": "Alt haznedeki suyun buhar basıncıyla yukarı süzüldüğü ocak üstü aparatla demlemek."},
    {"kelime": "öğütüm derecesini ayarlamak", "yasakli_kelimeler": ["klik", "ince kalın", "değirmen dişi", "demleme yöntemi", "mikron"], "zorluk": "orta", "aciklama": "Demleme yöntemine göre değirmenin öğütme kalınlığını seçmek."},
    {"kelime": "chemex ile demlemek", "yasakli_kelimeler": ["kum saati", "kalın filtre", "ahşap kulp", "berrak kahve", "cam gövde"], "zorluk": "orta", "aciklama": "Özel kalın filtreli kum saati formundaki cam kapta berrak kahve süzmek."},
    {"kelime": "kahve telvesini dökmek", "yasakli_kelimeler": ["çöp", "kullanılmış posa", "knock box", "dipte kalan", "temizleme"], "zorluk": "orta", "aciklama": "Demleme sonrası kalan kahve posasını atık kutusuna boşaltmak."},
    {"kelime": "su sıcaklığını ölçmek", "yasakli_kelimeler": ["derece", "termometre", "92 96 santigrat", "kaynar su dökülmez", "kettle"], "zorluk": "orta", "aciklama": "Kahveyi yakmamak için demleme suyunun ısısını 92-96 dereceye ayarlamak."},
    {"kelime": "kahve orantısını tartmak", "yasakli_kelimeler": ["brew ratio", "hassas terazi", "1 e 16", "gram", "zamanlayıcı"], "zorluk": "orta", "aciklama": "Kahve ile su miktarını hassas terazi üzerinde gramaj olarak oranlamak."},
    {"kelime": "syphon ile demlemek", "yasakli_kelimeler": ["vakumlu", "ispirto ocağı", "iki cam küre", "laboratuvar", "basınç farkı"], "zorluk": "orta", "aciklama": "Vakum ve ısı basıncıyla çalışan çift cam hazneli düzenekte kahve demlemek."},
    {"kelime": "kahve çekirdeği seçmek", "yasakli_kelimeler": ["arabica", "robusta", "single origin", "yükseklik", "etiket"], "zorluk": "orta", "aciklama": "Damak tadına ve demleme türüne en uygun kökenli çekirdeği belirlemek."},
    {"kelime": "barista eğitimi almak", "yasakli_kelimeler": ["kurs", "sertifika", "kahve sanatı", "makine bakımı", "hizmet"], "zorluk": "orta", "aciklama": "Profesyonel kahve hazırlama ve sunum tekniklerini öğrenmek."},
    {"kelime": "su kalitesini denetlemek", "yasakli_kelimeler": ["ppm", "tds", "arıtma", "mineralli su", "lezzet etkisi"], "zorluk": "orta", "aciklama": "Kahvenin çözünmesini doğrudan etkileyen suyun mineral değerini ölçmek."},
    {"kelime": "yeşil çekirdeği ayıklamak", "yasakli_kelimeler": ["kusurlu çekirdek", "defekt", "kavurma öncesi", "ayırma", "kalite"], "zorluk": "orta", "aciklama": "Kavurma öncesinde kırık ve bozuk yeşil taneleri el ile ayıklamak."},
    {"kelime": "kahveye buz eklemek", "yasakli_kelimeler": ["soğutma", "küp buz", "shaker", "iced latte", "bardak"], "zorluk": "orta", "aciklama": "Sıcak demlenen kahveyi soğuk içeceğe dönüştürmek için bardağa buz koymak."},
    {"kelime": "türk kahvesi fincanı kapatmak", "yasakli_kelimeler": ["fal için", "tabağa ters çevirme", "soğuma", "telvenin akması", "niyet"], "zorluk": "orta", "aciklama": "Fal bakmak amacıyla kahve fincanını tabağın üzerine ters kapatmak."},
    {"kelime": "kahveyi vakumlu saklamak", "yasakli_kelimeler": ["tazelik", "oksijenle temas", "kapak", "valf", "bayatlama önleme"], "zorluk": "orta", "aciklama": "Çekirdeklerin bayatlamaması için havası alınmış kapaklı kapta muhafaza etmek."},

    # Zor (14)
    {"kelime": "pre-infusion uygulamak", "yasakli_kelimeler": ["ön demleme", "blooming", "gaz salınımı", "kahve yatağı ıslatma", "karbondioksit"], "zorluk": "zor", "aciklama": "Kahve yatağını az suyla ıslatıp hapsolmuş karbondioksit gazının salınmasını sağlamak."},
    {"kelime": "kanalizasyonu önlemek", "yasakli_kelimeler": ["channeling", "wdt aleti", "su kanalı", "eşit akış", "portafiltre boşluğu"], "zorluk": "zor", "aciklama": "Suyun kahve yatağında delik açıp homojensiz akmasını iğneli dağıtıcıyla engellemek."},
    {"kelime": "ekstraksiyon verimini hesaplamak", "yasakli_kelimeler": ["extraction yield", "yüzde 18-22", "çözünen katı madde", "tds refraktometre", "aşırı az"], "zorluk": "zor", "aciklama": "Kahve çekirdeğinden suya geçen çözünmüş madde oranını refraktometre ile ölçmek."},
    {"kelime": "refraktometre ile tDS ölçmek", "yasakli_kelimeler": ["toplam çözünmüş katılar", "optik sensör", "brix", "damla", "yoğunluk"], "zorluk": "zor", "aciklama": "Kahve sıvısındaki toplam çözünmüş madde yüzdesini optik cihazla tespit etmek."},
    {"kelime": "kavurma profilini takip etmek", "yasakli_kelimeler": ["ror", "rate of rise", "cropster", "sıcaklık artış hızı", "kavurma grafiği"], "zorluk": "zor", "aciklama": "Kavurma esnasında çekirdek sıcaklık artış hızını grafik yazılımından anlık izlemek."},
    {"kelime": "anaerobik fermantasyon yapmak", "yasakli_kelimeler": ["oksijensiz tank", "kahve meyvesi", "karbondioksit maserasyonu", "fermente tatlar", "özel işlem"], "zorluk": "zor", "aciklama": "Kahve kirazlarını oksijensiz kapalı tanklarda bekleterek yoğun meyvemsi tatlar üretmek."},
    {"kelime": "bal işleme yöntemini seçmek", "yasakli_kelimeler": ["honey process", "müsilajlı kurutma", "yellow red black honey", "tatlılık", "afrika yatağı"], "zorluk": "zor", "aciklama": "Meyve etinin bir kısmını çekirdeğin üstünde bırakarak güneşte kurutma tekniğini uygulamak."},
    {"kelime": "wDT iğneleme yapmak", "yasakli_kelimeler": ["weiss distribution technique", "topaklanma kırma", "akapunktur iğnesi", "eşit dağılım", "puck hazırlığı"], "zorluk": "zor", "aciklama": "Portafiltredeki öğütülmüş kahve topaklarını ince çelik iğnelerle dağıtarak homojenleştirmek."},
    {"kelime": "aşırı ekstraksiyondan kaçınmak", "yasakli_kelimeler": ["over-extraction", "acı yanık tat", "kuruluk", "fazla çözünme", "uzun akış"], "zorluk": "zor", "aciklama": "Kahvenin gereğinden fazla çözünerek acı ve kurutucu bileşiklerin bardağa geçmesini engellemek."},
    {"kelime": "eksik ekstraksiyonu düzeltmek", "yasakli_kelimeler": ["under-extraction", "ekşi tatsız", "hızlı akış", "yetersiz temas", "öğütüm inceltme"], "zorluk": "zor", "aciklama": "Kahvenin yetersiz çözünmesiyle oluşan çiğ ekşi tadı öğütümü incelterek gidermek."},
    {"kelime": "akış profilini ayarlamak", "yasakli_kelimeler": ["flow profiling", "değişken debi", "pedallı makine", "basınç eğrisi", "slayer"], "zorluk": "zor", "aciklama": "Espresso akışı boyunca su debisini ve basıncını anlık değiştirerek ekstraksiyonu yönetmek."},
    {"kelime": "degassing süresini beklemek", "yasakli_kelimeler": ["gaz salınımı", "kavurma sonrası dinlenme", "karbondioksit", "1-2 hafta", "tazelik"], "zorluk": "zor", "aciklama": "Yeni kavrulan çekirdeğin içindeki sıkışmış CO2 gazını atması için birkaç gün beklemek."},
    {"kelime": "kahve çarkını kullanmak", "yasakli_kelimeler": ["scaa aroma tekerleği", "tat notaları", "çiçeksilik", "narenciye", "tat duyusu"], "zorluk": "zor", "aciklama": "Tadımdaki aromaları tanımlamak için uluslararası lezzet çarkı terminolojisinden yararlanmak."},
    {"kelime": "titanyum dişli değirmen takmak", "yasakli_kelimeler": ["burr seti", "düz konik dişli", "partikül homojenliği", "ısınma önleme", "öğütücü"], "zorluk": "zor", "aciklama": "Değirmene mikro partikül tutarlılığı sağlayan titanyum kaplamalı dişli takımı yerleştirmek."}
]

# 30. kaligrafi
kaligrafi_verbs = [
    # Kolay (12)
    {"kelime": "güzel yazı yazmak", "yasakli_kelimeler": ["harf", "kalem", "defter", "estetik", "çizmek"], "zorluk": "kolay", "aciklama": "Harfleri özenli ve estetik kurallara göre kağıda dökmek."},
    {"kelime": "mürekkep doldurmak", "yasakli_kelimeler": ["dolma kalem", "hokka", "damlalık", "kartuş", "siyah"], "zorluk": "kolay", "aciklama": "Kalemin haznesini veya hokkayı taze mürekkeple takviye etmek."},
    {"kelime": "kesik uçlu kalem kullanmak", "yasakli_kelimeler": ["uç", "metal", "açılı", "çizgi kalınlığı", "yazı"], "zorluk": "kolay", "aciklama": "Geniş ve dar çizgiler çizebilen eğik uçlu kalemle yazmak."},
    {"kelime": "harf çizmek", "yasakli_kelimeler": ["alfabe", "şekil", "büyük küçük", "karakter", "yazmak"], "zorluk": "kolay", "aciklama": "Alfabedeki karakterleri kağıt üzerine estetikçe çizmek."},
    {"kelime": "kağıda imza atmak", "yasakli_kelimeler": ["ad soyad", "kalem", "şık", "imzalamak", "çizgi"], "zorluk": "kolay", "aciklama": "Kendi ismini kaligrafik zarif bir kıvrımla kağıda yazmak."},
    {"kelime": "cetvelle çizgi çekmek", "yasakli_kelimeler": ["kılavuz satır", "kurşun kalem", "düz", "hizalama", "ölçüm"], "zorluk": "kolay", "aciklama": "Yazının düzgün akması için kağıda rehber satır çizgileri çekmek."},
    {"kelime": "davetiye yazmak", "yasakli_kelimeler": ["düğün", "isim", "zarf", "özel yazı", "kart"], "zorluk": "kolay", "aciklama": "Düğün ve etkinlik kartlarının üzerine şık el yazısıyla isimleri yazmak."},
    {"kelime": "yazıyı kurutmak", "yasakli_kelimeler": ["ıslak mürekkep", "beklemek", "dağılmaması", "kurutma kağıdı", "üflemek"], "zorluk": "kolay", "aciklama": "Taze yazılan mürekkebin dağılmadan kuruması için beklemek."},
    {"kelime": "uç temizlemek", "yasakli_kelimeler": ["bez", "kurumuş mürekkep", "su", "metal uç", "tıkanma"], "zorluk": "kolay", "aciklama": "Kalemin metal ucunda biriken kurumuş mürekkep artıklarını silmek."},
    {"kelime": "tablo çerçeveletmek", "yasakli_kelimeler": ["cam", "ahşap", "duvar", "asılı", "hat eseri"], "zorluk": "kolay", "aciklama": "Tamamlanan güzel yazı eserini korumak için çerçeve içine aldırmak."},
    {"kelime": "kalem ucu değiştirmek", "yasakli_kelimeler": ["nib", "metal", "takıp çıkarmak", "sap", "farklı kalınlık"], "zorluk": "kolay", "aciklama": "Yazı sapına farklı kalınlıkta yeni bir metal uç takmak."},
    {"kelime": "nokta koymak", "yasakli_kelimeler": ["ölçü", "harf", "kalem ucu", "işaret", "tamamlama"], "zorluk": "kolay", "aciklama": "Harflerin üzerine veya ölçü kılavuzuna kalem ucuyla nokta basmak."},

    # Orta (24)
    {"kelime": "kılavuz çizgileri çizmek", "yasakli_kelimeler": ["rehber satır", "eğim açısı", "x yüksekliği", "taban çizgisi", "kurşun kalem"], "zorluk": "orta", "aciklama": "Harf boylarını ve eğimini eşitlemek için sayfaya kılavuz ızgara çizmek."},
    {"kelime": "kalem açısını korumak", "yasakli_kelimeler": ["45 derece", "tutuş", "sabit açı", "kalın ince çizgi", "bilek"], "zorluk": "orta", "aciklama": "Yazı boyunca kalemin kağıda olan açısını bozmadan sabit tutmak."},
    {"kelime": "kamış kalem yontmak", "yasakli_kelimeler": ["kalemtraş bıçağı", "makta", "kamış", "yarık açma", "hat sanatı"], "zorluk": "orta", "aciklama": "Kargı kamışını özel bıçakla kesip ucuna mürekkep yarığı açmak."},
    {"kelime": "aharli kağıt hazırlamak", "yasakli_kelimeler": ["yumurta akı", "nişasta", "mühre", "pürüzsüz yüzey", "mürekkep emmeyen"], "zorluk": "orta", "aciklama": "Kağıdı mürekkebi dağıtmayacak ve düzeltmeye imkan verecek ahar sıvısıyla kaplamak."},
    {"kelime": "mührelemek", "yasakli_kelimeler": ["akik taşı", "parlatma", "düzleştirme", "ahar", "kağıt ezme"], "zorluk": "orta", "aciklama": "Aharlı kağıdı akik taşından mühreyle ovarak cam gibi pürüzsüz ve parlak yapmak."},
    {"kelime": "is mürekkebi yapmak", "yasakli_kelimeler": ["lamba isi", "arap zamkı", "havan", "dövme", "geleneksel"], "zorluk": "orta", "aciklama": "Kandil isini arap zamkıyla saatlerce döverek geleneksel siyah mürekkep üretmek."},
    {"kelime": "lika yerleştirmek", "yasakli_kelimeler": ["hokka içi", "ham ipek", "mürekkep tutucu", "akmayı önleme", "kalem batırma"], "zorluk": "orta", "aciklama": "Hokkanın içine kaleme dengeli mürekkep vermesi için ham ipek lifleri koymak."},
    {"kelime": "copperplate stili yazmak", "yasakli_kelimeler": ["esnek uç", "baskı uygulayarak kalınlaşan", "italik kıvrım", "ingiliz el yazısı", "zarif"], "zorluk": "orta", "aciklama": "Esnek sivri uçla basınca göre kalınlaşıp incelen zarif İngiliz yazı stilini yazmak."},
    {"kelime": "gotik yazı yazmak", "yasakli_kelimeler": ["fraktur", "textura", "sert köşeli", "orta çağ", "kesik uç"], "zorluk": "orta", "aciklama": "Ortaçağ elyazmalarına özgü köşeli ve kalın gotik karakterleri çizmek."},
    {"kelime": "fırça kaligrafi yapmak", "yasakli_kelimeler": ["brush pen", "esnek fırça uç", "modern kaligrafi", "baskı kontrolü", "renkli"], "zorluk": "orta", "aciklama": "Esnek fırça uçlu kalemle serbest ve akıcı modern harfler üretmek."},
    {"kelime": "italik el yazısı çalışmak", "yasakli_kelimeler": ["eğik", "chancery", "rönesans", "zarif", "kesik uç"], "zorluk": "orta", "aciklama": "Rönesans döneminin eğimli ve akıcı italik hümanist yazısını çalışmak."},
    {"kelime": "harf aralığını dengelemek", "yasakli_kelimeler": ["kerning", "boşluk dengesi", "okunabilirlik", "optik aralık", "uyum"], "zorluk": "orta", "aciklama": "Yanyana gelen harflerin arasındaki negatif boşlukları göz kararıyla eşitlemek."},
    {"kelime": "flourish kıvrımları eklemek", "yasakli_kelimeler": ["süsleme", "kuyruk uzatma", "zarif döngüler", "harf süsü", "estetik"], "zorluk": "orta", "aciklama": "Harf başlarına ve kuyruklarına estetik hava katan oval süsleme kıvrımları çizmek."},
    {"kelime": "altın varak yapıştırmak", "yasakli_kelimeler": ["tezhip", "yaldız", "parşömen", "ezme altın", "parlama"], "zorluk": "orta", "aciklama": "Yazının belirli baş harflerini veya kenarlarını gerçek altın yaprakla süslemek."},
    {"kelime": "tezhip ile süslemek", "yasakli_kelimeler": ["müzehhip", "kenar süsü", "çiçek motifleri", "altınlama", "klasik sanat"], "zorluk": "orta", "aciklama": "Yazı levhasının etrafını geleneksel minyatür ve altın süsleme motifleriyle bezemek."},
    {"kelime": "parşömen üzerine yazmak", "yasakli_kelimeler": ["deri", "dana derisi", "kadim", "elyazması", "dayanıklı"], "zorluk": "orta", "aciklama": "Özel işlenmiş hayvan derisinden yapılma dayanıklı parşömene yazı dökmek."},
    {"kelime": "baskı kuvvetini ayarlamak", "yasakli_kelimeler": ["el ağırlığı", "ince çizgi", "kalın çizgi", "esnek uç", "hassasiyet"], "zorluk": "orta", "aciklama": "Kalemin ucuna uygulanan el basıncını çizgi genişliğine göre kontrol etmek."},
    {"kelime": "sayfa mizanpajı yapmak", "yasakli_kelimeler": ["kenar boşlukları", "yerleşim", "kompozisyon", "metin bloğu", "düzen"], "zorluk": "orta", "aciklama": "Metnin sayfadaki konumunu ve kenar boşluklarını altın orana göre planlamak."},
    {"kelime": "makta üzerinde kalem kesmek", "yasakli_kelimeler": ["kemik altlık", "fildişi", "çat sesi", "keski açısı", "kamış"], "zorluk": "orta", "aciklama": "Kemik veya sedef altlık üzerine kamış ucu koyup bıçakla çıtlatarak kesmek."},
    {"kelime": "yazı meşki yapmak", "yasakli_kelimeler": ["hoca", "pratik", "örnek yazı", "taklit", "ödev"], "zorluk": "orta", "aciklama": "Ustanın yazdığı örnek harfleri defalarca kopya ederek pratik yapmak."},
    {"kelime": "paralel kalem kullanmak", "yasakli_kelimeler": ["pilot parallel", "çift plaka", "keskin hat", "mürekkep akışı", "modern"], "zorluk": "orta", "aciklama": "İki paralel metal plaka arasından mürekkep akıtan modern kaligrafi kalemini kullanmak."},
    {"kelime": "opak guaj boya kullanmak", "yasakli_kelimeler": ["kapatıcı", "renkli yazı", "suyla açma", "beyaz mürekkep", "koyu kağıt"], "zorluk": "orta", "aciklama": "Koyu renkli kağıtlara yazmak için kıvamlı guaj boyayı fırçayla kaleme doldurmak."},
    {"kelime": "monogram tasarlamak", "yasakli_kelimeler": ["iç içe harfler", "baş harfler", "arma", "logo", "kişisel mühür"], "zorluk": "orta", "aciklama": "İki veya üç harfi birbirine sanatsal şekilde kaynaştırarak kişisel amblem çizmek."},
    {"kelime": "eğim tahtası kullanmak", "yasakli_kelimeler": ["yazı masası", "eğimli sehpa", "duruş", "göz hizası", "kol açısı"], "zorluk": "orta", "aciklama": "Bileği ve boynu yormamak için eğimli yazı tablası üzerinde çalışmak."},

    # Zor (14)
    {"kelime": "sülüs ve nesih kaidelerine uymak", "yasakli_kelimeler": ["nokta hesabı", "harf anatomisi", "hüsn-i hat", "elif boyu", "şevkefendi"], "zorluk": "zor", "aciklama": "Harfleri kamış ucunun nokta ölçülerine dayalı katı klasik hat kurallarıyla yazmak."},
    {"kelime": "spencerian el yazısı icra etmek", "yasakli_kelimeler": ["amerikan tarzı", "oval ritim", "kuş kanadı hafifliği", "ince çizgiler", "akıcı el"], "zorluk": "zor", "aciklama": "19. yüzyıl Amerikan iş dünyasının hafif oval ve son derece akıcı yazı stilini yazmak."},
    {"kelime": "gilding tekniğiyle altın varak kabartmak", "yasakli_kelimeler": ["gesso tabanı", "kabartma harf", "akik mühre", "nefesle nemlendirme", "ortaçağ tezhibi"], "zorluk": "zor", "aciklama": "Özel gesso macunuyla kabartılan harfe altın varak yapıştırıp akik taşıyla ayna gibi parlatmak."},
    {"kelime": "uncial alfabesiyle yazmak", "yasakli_kelimeler": ["büyük yuvarlak harfler", "erken hristiyanlık", "latince elyazması", "tek sıra", "4. yüzyıl"], "zorluk": "zor", "aciklama": "Erken Ortaçağ'a özgü tamamen yuvarlak hatlı büyük Latin harfleriyle metin dökmek."},
    {"kelime": "icazetname almak", "yasakli_kelimeler": ["hattatlık diploması", "üstat imzası", "yazı icazeti", "yıllar süren eğitim", "meşk tamamlama"], "zorluk": "zor", "aciklama": "Hat sanatında ustasından kendi eserine imza atabilme yetkisi veren icazetnamesini almak."},
    {"kelime": "rotunda yazı stilini uygulamak", "yasakli_kelimeler": ["italyan gotiği", "yuvarlatılmış köşeler", "karolinj etkisi", "kitap yazısı", "geniş harfler"], "zorluk": "zor", "aciklama": "Kuzey gotiğine göre daha yuvarlak ve ferah olan İtalyan gotik stilini çizmek."},
    {"kelime": "oturan ve uzanan çizgileri dengelemek", "yasakli_kelimeler": ["ascender descender", "üst uzantı", "alt uzantı", "x yüksekliği dengesi", "satır ritmi"], "zorluk": "zor", "aciklama": "Harflerin yukarı uzanan boyunları ile aşağı sarkan kuyruklarının ritmik dengesini kurmak."},
    {"kelime": "karolenj miniskülünü yeniden üretmek", "yasakli_kelimeler": ["şarlman reformu", "küçük harfler", "okunaklı", "9. yüzyıl", "ortaçağ standart yazısı"], "zorluk": "zor", "aciklama": "Tüm Avrupa'ya standart getirmiş olan net ve yuvarlak küçük harf alfabesini yazmak."},
    {"kelime": "istif yapmak", "yasakli_kelimeler": ["harfleri üst üste dizme", "kompozisyon", "hat levhası", "geometrik uyum", "okuma sırası"], "zorluk": "zor", "aciklama": "Uzun bir ibareyi belirli bir geometrik formun içine harfleri üst üste bindirerek istiflemek."},
    {"kelime": "celî sülüs ile anıtsal yazmak", "yasakli_kelimeler": ["iri hat", "cami kubbesi", "geniş kamış", "uzaktan okunan", "mimari yazı"], "zorluk": "zor", "aciklama": "Mimari binaların kubbelerine ve kapılarına konacak devasa kalınlıkta hat yazmak."},
    {"kelime": "kolofan sayfası eklemek", "yasakli_kelimeler": ["müstensih kaydı", "kitabın son sözü", "tarih ve imza", "yazmanın sonu", "şükür duası"], "zorluk": "zor", "aciklama": "El yazması kitabın sonuna eseri yazan hattatın adını ve bitiş tarihini bildiren kayıt düşmek."},
    {"kelime": "minyatür fırçasıyla tahrir çekmek", "yasakli_kelimeler": ["samur kıl", "kontur çizgisi", "siyah ince hat", "motif çerçeveleme", "tezhip"], "zorluk": "zor", "aciklama": "Altın motiflerin etrafına tek bir samur kılı kalınlığında jilet gibi siyah sınır çizgisi çekmek."},
    {"kelime": "kat'ı sanatı ile harf oymak", "yasakli_kelimeler": ["kağıt oyma", "oymacılık", "ince neşter", "harfi kağıttan kesip çıkarma", "geleneksel sanat"], "zorluk": "zor", "aciklama": "Yazılmış harfleri kağıttan kılcal neşterle oyup çıkararak başka bir zemine yapıştırmak."},
    {"kelime": "rubrikasyon uygulamak", "yasakli_kelimeler": ["kırmızı başlıklar", "bölüm başı", "elyazması süsü", "vurgulama", "vermilion mürekkebi"], "zorluk": "zor", "aciklama": "Metin içindeki önemli bölüm başlarını ve ilk harfleri kırmızı mürekkeple vurgulamak."}
]

add_and_save_verbs('kahve', kahve_verbs)
add_and_save_verbs('kaligrafi', kaligrafi_verbs)
print('P15 done!')
