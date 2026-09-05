# -*- coding: utf-8 -*-
from card_utils import add_and_save_verbs

noroloji_verbs = [
    # Kolay (12)
    {"kelime": "hissetmek", "aciklama": "sinir uçları aracılığıyla dokunma, sıcaklık veya acıyı algılamak", "yasakli_kelimeler": ["dokunma", "acı", "sinir", "sıcaklık", "duyu"], "zorluk": "kolay"},
    {"kelime": "hatırlamak", "aciklama": "beyindeki hafıza merkezinden eski bilgileri geri çağırmak", "yasakli_kelimeler": ["hafıza", "bellek", "eski", "akıl", "unutmak"], "zorluk": "kolay"},
    {"kelime": "unutmak", "aciklama": "beyindeki anıların veya bilgilerin zihinden silinmesi", "yasakli_kelimeler": ["hafıza", "hatırlamamak", "silinmek", "akıl", "bellek"], "zorluk": "kolay"},
    {"kelime": "titremek", "aciklama": "ellerin veya vücudun istemsizce ritmik sallanması", "yasakli_kelimeler": ["el", "sallanmak", "parkinson", "istemsiz", "titreme"], "zorluk": "kolay"},
    {"kelime": "uyumak", "aciklama": "beynin dinlenmeye çekildiği bilinç kapalılığı hali", "yasakli_kelimeler": ["dinlenmek", "yatak", "rüya", "gece", "uyanmak"], "zorluk": "kolay"},
    {"kelime": "uyanmak", "aciklama": "uyku halinden çıkıp bilincin yeniden yerine gelmesi", "yasakli_kelimeler": ["uyku", "sabah", "bilinç", "göz açmak", "kalkmak"], "zorluk": "kolay"},
    {"kelime": "bayılmak", "aciklama": "beyne giden kanın anlık azalmasıyla geçici şuur kaybı yaşamak", "yasakli_kelimeler": ["şuur", "kendinden geçmek", "tansiyon", "düşmek", "geçici"], "zorluk": "kolay"},
    {"kelime": "düşünmek", "aciklama": "beyin korteksinde fikirler ve kavramlar arasında bağ kurmak", "yasakli_kelimeler": ["akıl", "fikir", "zihin", "korteks", "mantık"], "zorluk": "kolay"},
    {"kelime": "öğrenmek", "aciklama": "yeni nöronal bağlantılar kurarak yeni bilgi ve beceri edinmek", "yasakli_kelimeler": ["bilgi", "beceri", "hafıza", "ders", "kavramak"], "zorluk": "kolay"},
    {"kelime": "hareket etmek", "aciklama": "beyinden gelen motor sinyallerle kasları çalıştırmak", "yasakli_kelimeler": ["kas", "motor", "yürümek", "sinyal", "kol"], "zorluk": "kolay"},
    {"kelime": "baş ağrımak", "aciklama": "kafa bölgesindeki damar veya sinir hassasiyetiyle zonklama hissetmek", "yasakli_kelimeler": ["migren", "zonklama", "kafa", "ağrı", "şakak"], "zorluk": "kolay"},
    {"kelime": "göz kırpmak", "aciklama": "kornea refleksiyle göz kapaklarını istemsizce veya bilinçli kapatıp açmak", "yasakli_kelimeler": ["refleks", "göz kapağı", "kapatmak", "kapak", "anlık"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "eeg çekmek", "aciklama": "kafa derisine elektrotlar bağlayarak beynin elektriksel aktivitesini kaydetmek", "yasakli_kelimeler": ["elektrot", "beyin dalgası", "elektrik", "grafi", "nöbet"], "zorluk": "orta"},
    {"kelime": "emg yapmak", "aciklama": "iğne elektrotla kasların ve periferik sinirlerin iletimini ölçmek", "yasakli_kelimeler": ["kas", "iğne", "sinir iletimi", "elektrot", "ölçüm"], "zorluk": "orta"},
    {"kelime": "refleks muayenesi yapmak", "aciklama": "refleks çekici ile dize vurup patella refleksini kontrol etmek", "yasakli_kelimeler": ["refleks çekici", "patella", "diz kapağı", "vurmak", "yanıt"], "zorluk": "orta"},
    {"kelime": "nöbet geçirmek", "aciklama": "beyindeki kontrolsüz elektriksel fırtına sonucu sara krizi yaşamak", "yasakli_kelimeler": ["epilepsi", "sara", "kasılma", "kriz", "şuur"], "zorluk": "orta"},
    {"kelime": "felç geçirmek", "aciklama": "beyin damarı tıkanması veya kanamasıyla vücut yarısının tutmaması", "yasakli_kelimeler": ["inme", "tıkanma", "kanama", "hareketsizlik", "damar"], "zorluk": "orta"},
    {"kelime": "sinir iletmek", "aciklama": "aksiyon potansiyelinin akson boyunca sinapsa doğru akması", "yasakli_kelimeler": ["akson", "aksiyon potansiyeli", "sinaps", "elektrik", "iletim"], "zorluk": "orta"},
    {"kelime": "lomber ponksiyon yapmak", "aciklama": "bel omurları arasından iğneyle girip beyin omurilik sıvısı almak", "yasakli_kelimeler": ["bos", "bel", "iğne", "sıvı", "menenjit"], "zorluk": "orta"},
    {"kelime": "nörotransmitter salgılamak", "aciklama": "sinaps boşluğuna dopamin veya serotonin gibi kimyasal ulaklar bırakmak", "yasakli_kelimeler": ["dopamin", "serotonin", "sinaps", "kimyasal", "salgı"], "zorluk": "orta"},
    {"kelime": "uyuşmak", "aciklama": "baskı gören veya hasarlanan duyusal sinir bölgesinde karıncalanma hissi", "yasakli_kelimeler": ["karıncalanma", "hissizlik", "baskı", "iğnelenme", "bacak"], "zorluk": "orta"},
    {"kelime": "denge kaybetmek", "aciklama": "beyincik veya iç kulak vestibüler sisteminin bozulmasıyla sendelemek", "yasakli_kelimeler": ["beyincik", "vertigo", "sendelemek", "düşme", "vestibüler"], "zorluk": "orta"},
    {"kelime": "komaya girmek", "aciklama": "dış uyaranlara hiçbir yanıt vermeyen derin ve uzun bilinçsizlik evresi", "yasakli_kelimeler": ["derin bilinçsizlik", "uyanmama", "yoğun bakım", "glasgow", "uyaran"], "zorluk": "orta"},
    {"kelime": "miyelin kılıfı soymak", "aciklama": "bağışıklık hücrelerinin sinir etrafındaki yağlı yalıtım katmanına saldırması", "yasakli_kelimeler": ["ms", "multipl skleroz", "demiyelinizasyon", "yalıtım", "hasar"], "zorluk": "orta"},
    {"kelime": "konuşma yetisini yitirmek", "aciklama": "beyindeki broca veya wernicke alanı hasarıyla afazi tablosuna girmek", "yasakli_kelimeler": ["afazi", "broca", "wernicke", "lisan", "anlayamama"], "zorluk": "orta"},
    {"kelime": "hafıza kaybı yaşamak", "aciklama": "hipokampus hasarı sonucu geçmişi veya yakın zamanı hatırlayamamak", "yasakli_kelimeler": ["amnezi", "hipokampus", "yakın hafıza", "anı", "kayıp"], "zorluk": "orta"},
    {"kelime": "kraniyal sinirleri test etmek", "aciklama": "kafa çiftlerinin görme, koku ve yüz mimik fonksiyonlarını muayene etmek", "yasakli_kelimeler": ["kafa çiftleri", "12 çift", "mimik", "koku", "göz hareketi"], "zorluk": "orta"},
    {"kelime": "babinski refleksi aramak", "aciklama": "ayak tabanı çizildiğinde başparmağın yukarı kalkmasını gözlemlemek", "yasakli_kelimeler": ["ayak tabanı", "başparmak", "üst motor nöron", "piramidal", "çizme"], "zorluk": "orta"},
    {"kelime": "migren atağı yaşamak", "aciklama": "ışık ve ses hassasiyetiyle tek taraflı şiddetli zonklayıcı baş ağrısı çekmek", "yasakli_kelimeler": ["fotofobi", "aura", "tek taraflı", "zonklama", "bulantı"], "zorluk": "orta"},
    {"kelime": "kas atması olmak", "aciklama": "deri altındaki kas liflerinin tek tük istemsizce seğirmesi", "yasakli_kelimeler": ["fasikülasyon", "seğirme", "kas lifi", "istemsiz", "als"], "zorluk": "orta"},
    {"kelime": "felç açılmak", "aciklama": "trombolitik ilaçla pıhtı eritildikten sonra felçli uzvun hareket kazanması", "yasakli_kelimeler": ["tpa", "pıhtı eritme", "inme", "hareket", "iyileşme"], "zorluk": "orta"},
    {"kelime": "spastisite gelişmek", "aciklama": "beyin veya omurilik hasarı sonrası kaslarda sürekli sert kasılma hali", "yasakli_kelimeler": ["kas sertliği", "katılık", "kasılma", "tonus", "omurilik"], "zorluk": "orta"},
    {"kelime": "halüsinasyon görmek", "aciklama": "dış ortamda olmayan ses veya görüntüleri beyinde gerçek gibi algılamak", "yasakli_kelimeler": ["sanrı", "olmayan ses", "görüntü", "algı", "hayal"], "zorluk": "orta"},
    {"kelime": "nörogenez gerçekleşmek", "aciklama": "yetişkin beyninin hipokampus bölgesinde yeni nöronların üretilmesi", "yasakli_kelimeler": ["yeni nöron", "üretim", "kök hücre", "hipokampus", "beyin"], "zorluk": "orta"},
    {"kelime": "kan-beyin bariyerini geçmek", "aciklama": "moleküllerin kılcal damar endotelini aşıp beyin dokusuna sızması", "yasakli_kelimeler": ["bariyer", "endotel", "geçiş", "astrosit", "ilaç"], "zorluk": "orta"},
    {"kelime": "derin tendon refleksi almak", "aciklama": "kas kirişine çekiçle vurularak omurilik seviyesindeki arkı değerlendirmek", "yasakli_kelimeler": ["tendon", "kiriş", "ark", "omurilik", "yanıt"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "sinaptik plastisite kurmak", "aciklama": "öğrenmeyle nöronlar arasındaki sinapsların güçlenmesi ve yeniden yapılanması", "yasakli_kelimeler": ["plastisite", "ltp", "uzun süreli potansiyalizasyon", "güçlenme", "bağlantı"], "zorluk": "zor"},
    {"kelime": "aksiyon potansiyeli üretmek", "aciklama": "sodyum potasyum pompası ve voltaj kapılı kanallarla zar voltajını tersine çevirmek", "yasakli_kelimeler": ["sodyum", "potasyum", "depolarizasyon", "voltaj", "zar"], "zorluk": "zor"},
    {"kelime": "salto iletimi yapmak", "aciklama": "elektrik sinyalinin ranvier boğumlarından atlayarak çok hızlı ilerlemesi", "yasakli_kelimeler": ["ranvier boğumu", "atlamalı iletim", "miyelin", "hız", "akson"], "zorluk": "zor"},
    {"kelime": "ekstrapiramidal belirti vermek", "aciklama": "bazal ganglion devrelerinin bozulmasıyla bradikinezi ve rijidite doğması", "yasakli_kelimeler": ["bazal ganglion", "rijidite", "bradikinezi", "substantia nigra", "parkinson"], "zorluk": "zor"},
    {"kelime": "fasiyal paralizi yaşamak", "aciklama": "yedinci kraniyal sinirin iltihabıyla yüzün bir yarısının tamamen sarkması", "yasakli_kelimeler": ["bell paralizisi", "7. sinir", "yüz felci", "asimetri", "göz kapatamama"], "zorluk": "zor"},
    {"kelime": "nörodejenerasyona uğramak", "aciklama": "tau veya amiloid plakları birikerek nöronların kademeli ölmesi", "yasakli_kelimeler": ["alzheimer", "amiloid", "tau proteini", "nöron ölümü", "kademeli"], "zorluk": "zor"},
    {"kelime": "status epileptikusa girmek", "aciklama": "aralıksız 5 dakikadan uzun süren ve durdurulamayan ölümcül sara nöbeti", "yasakli_kelimeler": ["aralıksız nöbet", "acil", "durmayan kriz", "yoğun bakım", "ilaç direnci"], "zorluk": "zor"},
    {"kelime": "derin beyin stimülasyonu", "aciklama": "subtalamik çekirdeğe elektrot implantı yerleştirip elektriksel uyarı vermek", "yasakli_kelimeler": ["dbs", "beyin pili", "subtalamik", "implant", "parkinson"], "zorluk": "zor"},
    {"kelime": "intrakraniyal basınç artmak", "aciklama": "kafa tası içinde ödem veya kanama sebebiyle beyne binen basıncın fırlaması", "yasakli_kelimeler": ["kibas", "kafa içi basınç", "ödem", "herniasyon", "papilödem"], "zorluk": "zor"},
    {"kelime": "herniyasyona uğramak", "aciklama": "yüksek basınç altındaki beyin dokusunun foramen magnumdan aşağı fıtıklaşması", "yasakli_kelimeler": ["fıtıklaşma", "foramen magnum", "tonsil", "solunum durması", "bası"], "zorluk": "zor"},
    {"kelime": "somatotopik haritalamak", "aciklama": "motor ve duyu korteksinde vücut bölgelerinin homunkulus düzeninde yerleşimi", "yasakli_kelimeler": ["homunkulus", "motor korteks", "harita", "penfield", "temsil"], "zorluk": "zor"},
    {"kelime": "otonom disrefleksi tetiklemek", "aciklama": "omurilik hasarlı hastada ağrılı uyaranın kontrolsüz hipertansiyon fırtınası yapması", "yasakli_kelimeler": ["sempatik fırtına", "hipertansiyon", "omurilik hasarı", "bradikardi", "acil"], "zorluk": "zor"},
    {"kelime": "aksonal rejenerasyon denemek", "aciklama": "kesilen periferik sinir lifinin schwann hücreleri kılavuzluğunda uzaması", "yasakli_kelimeler": ["schwann", "periferik sinir", "büyüme konisi", "iyileşme", "yenilenme"], "zorluk": "zor"},
    {"kelime": "glial skar oluşturmak", "aciklama": "merkezi sinir sistemi yaralanmasında astrositlerin hasar bölgesini sert dokuyla kapatması", "yasakli_kelimeler": ["astrosit", "skar", "reaktif gliozis", "bariyer", "iyileşme engeli"], "zorluk": "zor"}
]

numizmatik_verbs = [
    # Kolay (12)
    {"kelime": "para basmak", "aciklama": "darphanede madeni sikke veya banknot üretmek", "yasakli_kelimeler": ["darphane", "madeni", "sikke", "üretim", "para"], "zorluk": "kolay"},
    {"kelime": "koleksiyon yapmak", "aciklama": "farklı dönem ve ülkelere ait madeni paraları biriktirmek", "yasakli_kelimeler": ["biriktirmek", "koleksiyoner", "albüm", "parça", "hobi"], "zorluk": "kolay"},
    {"kelime": "harcamak", "aciklama": "mal ve hizmet satın almak için eldeki parayı vermek", "yasakli_kelimeler": ["satın almak", "ödeme", "alışveriş", "tüketmek", "para"], "zorluk": "kolay"},
    {"kelime": "biriktirmek", "aciklama": "paraları kumbarada veya kasada saklayıp çoğaltmak", "yasakli_kelimeler": ["kumbara", "kasa", "tasarruf", "saklamak", "çoğaltmak"], "zorluk": "kolay"},
    {"kelime": "incelemek", "aciklama": "büyüteçle sikkenin üstündeki yazı ve kabartmaları gözlemlemek", "yasakli_kelimeler": ["büyüteç", "yazı", "kabartma", "detay", "gözlem"], "zorluk": "kolay"},
    {"kelime": "temizlemek", "aciklama": "topraktan çıkan madeni paranın kirini zarar vermeden arındırmak", "yasakli_kelimeler": ["kir", "arındırmak", "yıkamak", "solüsyon", "fırça"], "zorluk": "kolay"},
    {"kelime": "bozdurmak", "aciklama": "büyük değerli banknotu daha küçük bozuk paralara çevirmek", "yasakli_kelimeler": ["tüm", "bozukluk", "küçük", "çevirmek", "para üstü"], "zorluk": "kolay"},
    {"kelime": "saklamak", "aciklama": "değerli sikkeleri koruyucu şeffaf kapsüllere veya albüme koymak", "yasakli_kelimeler": ["kapsül", "albüm", "koruma", "şeffaf", "kutu"], "zorluk": "kolay"},
    {"kelime": "satın almak", "aciklama": "müzayededen nadir bir tarihi sikkeyi bedelini ödeyip edinmek", "yasakli_kelimeler": ["müzayede", "bedel", "nadir", "edinmek", "ödeme"], "zorluk": "kolay"},
    {"kelime": "değiş tokuş etmek", "aciklama": "koleksiyonerler arasında çift olan paraları takas yapmak", "yasakli_kelimeler": ["takas", "koleksiyoner", "çift", "vermek", "almak"], "zorluk": "kolay"},
    {"kelime": "tartmak", "aciklama": "hassas teraziyle madeni paranın gramını virgülden sonra ölçmek", "yasakli_kelimeler": ["terazi", "gram", "hassas", "ağırlık", "ölçüm"], "zorluk": "kolay"},
    {"kelime": "sergilemek", "aciklama": "müzede tarihi sikkeleri cam vitrin arkasında halka açmak", "yasakli_kelimeler": ["müze", "vitrin", "cam", "ziyaretçi", "göstermek"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "sikke darbetmek", "aciklama": "örs üzerindeki kalıba çekiçle vurarak metale kabartma basmak", "yasakli_kelimeler": ["darphane", "kalıp", "çekiç", "örs", "kabartma"], "zorluk": "orta"},
    {"kelime": "patina oluşturmak", "aciklama": "bronz ve gümüş sikkelerin havayla temas ederek yüzeyinde asil oksit tabakası yapması", "yasakli_kelimeler": ["patin", "yeşil", "oksit", "asil", "zaman"], "zorluk": "orta"},
    {"kelime": "kondisyon derecelendirmek", "aciklama": "paranın aşınma durumuna göre çil, çok temiz gibi not vermek", "yasakli_kelimeler": ["çil", "derece", "aşınma", "grading", "not"], "zorluk": "orta"},
    {"kelime": "müzayedeye çıkarmak", "aciklama": "nadir antik parayı açık artırma salonunda satışa sunmak", "yasakli_kelimeler": ["açık artırma", "salon", "satış", "pey", "katalog"], "zorluk": "orta"},
    {"kelime": "leydi okumak", "aciklama": "antik sikke çevresindeki lejant yazılarını ve imparator adını çözmek", "yasakli_kelimeler": ["lejant", "yazı", "imparator", "grekçe", "latince"], "zorluk": "orta"},
    {"kelime": "sahtesini ayırt etmek", "aciklama": "döküm veya modern presle yapılan sahte sikkeyi orijinalden ayırmak", "yasakli_kelimeler": ["sahte", "orijinal", "taklit", "döküm", "ayırma"], "zorluk": "orta"},
    {"kelime": "katalog taramak", "aciklama": "paranın referans numarasını krause veya rsc kataloglarında bulmak", "yasakli_kelimeler": ["krause", "referans", "numara", "kitap", "arama"], "zorluk": "orta"},
    {"kelime": "hazine bulmak", "aciklama": "toprak altında çömlek içinde toplu halde gömülmüş sikke definesi keşfetmek", "yasakli_kelimeler": ["define", "çömlek", "gömü", "toplu", "keşif"], "zorluk": "orta"},
    {"kelime": "hatıra parası basmak", "aciklama": "önemli bir tarihi olay veya şahsiyet anısına sınırlı sayıda özel sikke üretmek", "yasakli_kelimeler": ["hatıra", "anma", "sınırlı sayı", "özel basım", "gümüş"], "zorluk": "orta"},
    {"kelime": "ayarını ölçmek", "aciklama": "altın veya gümüş sikkenin saflık derecesini mihenk taşıyla saptamak", "yasakli_kelimeler": ["mihenk taşı", "ayar", "saflık", "karat", "gümüş"], "zorluk": "orta"},
    {"kelime": "kapsüllemek", "aciklama": "derecelendirme şirketi tarafından parayı kırılmaz plastik kutuya mühürlemek", "yasakli_kelimeler": ["slabbing", "ngc", "pcgs", "mühürlü", "plastik"], "zorluk": "orta"},
    {"kelime": "tarihlendirmek", "aciklama": "sikkenin üstündeki hükümdar yılı ve darp yeri işaretinden basım yılını bulmak", "yasakli_kelimeler": ["yıl", "dönem", "hicri", "miladi", "tespit"], "zorluk": "orta"},
    {"kelime": "kenar yazısı incelemek", "aciklama": "madeni paranın tırtıklı veya yazılı yan yüzeyini kontrol etmek", "yasakli_kelimeler": ["tırtık", "yan yüzey", "yazı", "bordür", "kenar"], "zorluk": "orta"},
    {"kelime": "emisyon çıkarmak", "aciklama": "merkez bankasının yeni tertip kağıt paraları piyasaya sürmesi", "yasakli_kelimeler": ["tertip", "merkez bankası", "kağıt para", "tedavül", "piyasa"], "zorluk": "orta"},
    {"kelime": "tedavülden kaldırmak", "aciklama": "geçerliliği biten eski banknotları ve paraları piyasadan çekmek", "yasakli_kelimeler": ["çekmek", "geçersiz", "iptal", "banka", "eski"], "zorluk": "orta"},
    {"kelime": "darphane işareti aramak", "aciklama": "sikkenin nerede basıldığını gösteren küçük harf veya sembolü okumak", "yasakli_kelimeler": ["mintmark", "harf", "sembol", "şehir", "basım yeri"], "zorluk": "orta"},
    {"kelime": "filigran kontrol etmek", "aciklama": "banknotu ışığa tutarak içindeki gizli resmi doğrulamak", "yasakli_kelimeler": ["ışık", "gizli resim", "kağıt", "güvenlik", "doğrulama"], "zorluk": "orta"},
    {"kelime": "manyetik şerit okumak", "aciklama": "kağıt paranın içindeki güvenlik şeridini mor ışıkta denetlemek", "yasakli_kelimeler": ["mor ışık", "uv", "güvenlik şeridi", "sahtecilik", "denetim"], "zorluk": "orta"},
    {"kelime": "overstrike incelemek", "aciklama": "eski bir sikkenin düzeltilip üstüne yeni hükümdarın kalıbının basılması", "yasakli_kelimeler": ["çift baskı", "üst üste", "eski sikke", "yeniden", "kalıp"], "zorluk": "orta"},
    {"kelime": "hata payı aramak", "aciklama": "üretim sırasında kalıbın kaymasıyla basılan değerli hatalı basımı bulmak", "yasakli_kelimeler": ["hatalı basım", "kayma", "çift vuruş", "error", "değerli"], "zorluk": "orta"},
    {"kelime": "kesik sikke ayırmak", "aciklama": "tarihte kenarlarından gümüş tırtıklanmış hileli paraları tespit etmek", "yasakli_kelimeler": ["kırpma", "tıraşlama", "gümüş çalma", "kenar", "eksik gram"], "zorluk": "orta"},
    {"kelime": "delikli para saklamak", "aciklama": "ortası delik osmanlı veya çin madeni paralarını kordona dizmek", "yasakli_kelimeler": ["delik", "ortası", "çin", "dizi", "kordon"], "zorluk": "orta"},
    {"kelime": "madalyon toplayıcılığı", "aciklama": "resmi para olmayan askeri veya sivil anı madalyalarını biriktirmek", "yasakli_kelimeler": ["madalya", "anı", "nişan", "askeri", "toplamak"], "zorluk": "orta"},
    {"kelime": "korozyonu durdurmak", "aciklama": "tuzlu topraktan çıkan sikkeyi kimyasal banyoyla bronz hastalığından kurtarmak", "yasakli_kelimeler": ["bronz hastalığı", "klorür", "koruma", "kimyasal", "yeşil toz"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "nümismatik tipoloji kurmak", "aciklama": "sikkeleri hükümdar, portre stili, ağırlık standardı ve ikonografisine göre dizmek", "yasakli_kelimeler": ["tipoloji", "kronoloji", "sınıflama", "ikonografi", "standart"], "zorluk": "zor"},
    {"kelime": "die-link analizi yapmak", "aciklama": "aynı ön yüz kalıbıyla basılmış farklı arka yüz sikkelerini eşleştirip kronoloji çıkarmak", "yasakli_kelimeler": ["kalıp bağı", "ön yüz", "arka yüz", "eşleştirme", "kronoloji"], "zorluk": "zor"},
    {"kelime": "kontrmark vurmak", "aciklama": "tedavüldeki yabancı sikkeye geçerlilik veya değer değişimi için küçük mühür basmak", "yasakli_kelimeler": ["mühür", "karşı baskı", "damga", "geçerlilik", "yabancı"], "zorluk": "zor"},
    {"kelime": "brakteat incelemek", "aciklama": "orta çağda incecik gümüş sacın tek yüzüne kabartma basılmış hafif sikkeleri araştırmak", "yasakli_kelimeler": ["tek yüz", "ince sac", "orta çağ", "gümüş", "kabartma"], "zorluk": "zor"},
    {"kelime": "devalüasyona uğratmak", "aciklama": "hükümdarın hazine sıkıntısında sikkenin içindeki saf gümüş oranını düşürmesi", "yasakli_kelimeler": ["tağşiş", "saf metal", "ayar düşürme", "enflasyon", "hazine"], "zorluk": "zor"},
    {"kelime": "elektrum ayrıştırmak", "aciklama": "lidya'nın ilk bastığı doğal altın-gümüş alaşımı sikkelerin metal oranını analiz etmek", "yasakli_kelimeler": ["lidya", "doğal alaşım", "altın gümüş", "paktolos", "ilk para"], "zorluk": "zor"},
    {"kelime": "incuse desen basmak", "aciklama": "arka yüzde dışa kabartma yerine içe çökük geometrik kalıp izi bırakmak", "yasakli_kelimeler": ["içe çökük", "çukur", "geometrik", "arka yüz", "erken antik"], "zorluk": "zor"},
    {"kelime": "kameo kontrastı vermek", "aciklama": "proof baskı sikkede figürü mat kumlu, zemini ise ayna gibi parlak üretmek", "yasakli_kelimeler": ["proof", "ayna zemin", "mat figür", "kontrast", "özel basım"], "zorluk": "zor"},
    {"kelime": "skifate formu vermek", "aciklama": "bizans döneminde çanak veya kase şeklinde içbükey bükük sikke basmak", "yasakli_kelimeler": ["içbükey", "çanak sikke", "bizans", "kase", "form"], "zorluk": "zor"},
    {"kelime": "xrf spektrometresi tutmak", "aciklama": "x ışını floresansı ile sikkeye zarar vermeden yüzde metal alaşımını ölçmek", "yasakli_kelimeler": ["xrf", "alaşım", "tahribatsız", "x ışını", "yüzde"], "zorluk": "zor"},
    {"kelime": "notafili uzmanlığı yapmak", "aciklama": "madeni paralar yerine sadece tarihi kağıt para ve tahvilleri araştırmak", "yasakli_kelimeler": ["kağıt para", "tahvil", "banknot", "uzman", "belge"], "zorluk": "zor"},
    {"kelime": "parola sikkesi basmak", "aciklama": "kuşatma altındaki şehirde acil ihtiyaç için kurşun veya deriden jeton para dökmek", "yasakli_kelimeler": ["kuşatma parası", "obsidional", "acil para", "jeton", "kurşun"], "zorluk": "zor"},
    {"kelime": "spintria yorumlamak", "aciklama": "antik roma genelevlerinde veya hamamlarında jeton olarak kullanılan erotik sikkeleri incelemek", "yasakli_kelimeler": ["roma", "jeton", "genelev", "erotik", "hamam"], "zorluk": "zor"},
    {"kelime": "klip para kesmek", "aciklama": "yuvarlak sac yerine kare veya dikdörtgen plakalardan kesilen acil durum sikkeleri", "yasakli_kelimeler": ["kare sikke", "dikdörtgen", "klippe", "acil basım", "kesim"], "zorluk": "zor"}
]

if __name__ == "__main__":
    add_and_save_verbs("noroloji", noroloji_verbs)
    add_and_save_verbs("numizmatik", numizmatik_verbs)
