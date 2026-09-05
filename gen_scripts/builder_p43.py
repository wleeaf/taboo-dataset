# -*- coding: utf-8 -*-
from card_utils import add_and_save_verbs

seramik_verbs = [
    # Kolay (12)
    {"kelime": "yoğurmak", "aciklama": "kırmızı veya beyaz kili hava kabarcıklarını çıkarmak için elle yoğurmak", "yasakli_kelimeler": ["kil", "çamur", "hava kabarcığı", "el", "hazırlık"], "zorluk": "kolay"},
    {"kelime": "şekil vermek", "aciklama": "ıslak çamura parmaklarla bastırarak vazo veya kase formu kazandırmak", "yasakli_kelimeler": ["form", "vazo", "kase", "parmak", "çamur"], "zorluk": "kolay"},
    {"kelime": "fırınlamak", "aciklama": "kuruyan seramik ürünleri 1000 derecelik fırına sürüp pişirmek", "yasakli_kelimeler": ["fırın", "pişirme", "derece", "seramik fırını", "ısı"], "zorluk": "kolay"},
    {"kelime": "sır dökmek", "aciklama": "bisküvi pişen ürünün üstüne parlak ve su geçirmez sır tabakası akıtmak", "yasakli_kelimeler": ["sır", "parlak", "su geçirmez", "bisküvi", "kaplama"], "zorluk": "kolay"},
    {"kelime": "boyamak", "aciklama": "seramik boyaları ve fırçayla vazo üzerine desenler çizmek", "yasakli_kelimeler": ["fırça", "desen", "çini boyası", "vazo", "renklendirme"], "zorluk": "kolay"},
    {"kelime": "kurutmak", "aciklama": "şekillendirilen ıslak kil objeyi çatlamasın diye gölgede yavaşça kurutmak", "yasakli_kelimeler": ["gölge", "yavaşça", "çatlama", "ıslak kil", "bekletmek"], "zorluk": "kolay"},
    {"kelime": "kesmek", "aciklama": "misina teliyle çamur bloğundan kalın dilimler ayırmak", "yasakli_kelimeler": ["misina", "tel", "çamur bloğu", "dilim", "ayırmak"], "zorluk": "kolay"},
    {"kelime": "zımparalamak", "aciklama": "bisküvi pişirimi sonrası ürünün altındaki pürüzleri zımparayla düzeltmek", "yasakli_kelimeler": ["pürüz", "zımpara kağıdı", "düzeltme", "taban", "aşındırma"], "zorluk": "kolay"},
    {"kelime": "döndürmek", "aciklama": "ayakla veya elektrikle dönen torna tablasında çamura form vermek", "yasakli_kelimeler": ["torna", "tabla", "dönüş", "çömlek", "ayak"], "zorluk": "kolay"},
    {"kelime": "delmek", "aciklama": "saksının altından fazla su aksın diye çamurken delik açmak", "yasakli_kelimeler": ["delik", "saksı", "drenaj", "açmak", "su tahliyesi"], "zorluk": "kolay"},
    {"kelime": "yapıştırmak", "aciklama": "çamur çamuru tutsun diye kulp ve gövde arasına balçık sürüp tutturmak", "yasakli_kelimeler": ["balçık", "kulp", "tutturmak", "çentik", "ekleme"], "zorluk": "kolay"},
    {"kelime": "parlatmak", "aciklama": "deri sertliğindeki kilin yüzeyini pürüzsüz taşla ovarak parlatmak", "yasakli_kelimeler": ["perdah", "taş", "ovalama", "deri sertliği", "pürüzsüz"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "çömlekçi tornasında çekmek", "aciklama": "dönen tabladaki kil kütlesini merkezleyip ellerle yukarı doğru silindir çekmek", "yasakli_kelimeler": ["merkezleme", "silindir", "torna", "çömlek", "yukarı çekme"], "zorluk": "orta"},
    {"kelime": "sucuk tekniğiyle örmek", "aciklama": "kili rulo halinde silindir sucuklar yapıp üst üste dizerek vazo duvarı örmek", "yasakli_kelimeler": ["coiling", "rulo", "sucuk", "katman", "üst üste"], "zorluk": "orta"},
    {"kelime": "plaka açmak", "aciklama": "merdane ve kılavuz çıtalarla kili düz bir hamur plakası şeklinde yaymak", "yasakli_kelimeler": ["slab", "merdane", "kılavuz çıta", "düz levha", "plaka"], "zorluk": "orta"},
    {"kelime": "çentiklemek", "aciklama": "iki kuru kil parçayı birleştirmeden önce yüzeyleri tarakla çizip balçıklamak", "yasakli_kelimeler": ["score and slip", "çizmek", "tarak", "pürüzlendirme", "balçık"], "zorluk": "orta"},
    {"kelime": "bisküvi pişirimi yapmak", "aciklama": "kuruyan ham kili ilk kez 950 derecede fırınlayıp gözenekli sert seramik yapmak", "yasakli_kelimeler": ["ilk pişirim", "950 derece", "gözenekli", "sırlama öncesi", "bisküvi"], "zorluk": "orta"},
    {"kelime": "sır daldırmak", "aciklama": "bisküvi kaseyi maşayla tutup sıvı sır leğenine batırıp çıkarmak", "yasakli_kelimeler": ["daldırma", "maşa", "leğen", "sıvı sır", "kaplama"], "zorluk": "orta"},
    {"kelime": "sır tabancasıyla püskürtmek", "aciklama": "kompresörlü boya tabancasıyla heykelsi seramiklere homojen sır püskürtmek", "yasakli_kelimeler": ["püskürtme", "kompresör", "tabanca", "homojen katman", "kabinde sır"], "zorluk": "orta"},
    {"kelime": "deri sertliğine getirmek", "aciklama": "kilin nemini kaybedip kesilebilir ve oyulabilir peynir sertliğine ulaşması", "yasakli_kelimeler": ["leather hard", "peynir sertliği", "oyma kıvamı", "nem kaybı", "traşlama"], "zorluk": "orta"},
    {"kelime": "dip traşlamak", "aciklama": "tornada kuruyan kasenin altını ters çevirip oygu aletleriyle dip halkası açmak", "yasakli_kelimeler": ["trimming", "dip halkası", "oygu aleti", "ters çevirme", "fazlalık alma"], "zorluk": "orta"},
    {"kelime": "alçı kalıp dökmek", "aciklama": "modelin etrafına sıvı alçı döküp döküm çamuru için emici negatif kalıp üretmek", "yasakli_kelimeler": ["alçı", "negatif kalıp", "döküm", "model", "emici"], "zorluk": "orta"},
    {"kelime": "döküm çamuru boşaltmak", "aciklama": "alçı kalıba sıvı slip döküp et payı oluştuktan sonra fazlasını geri akıtmak", "yasakli_kelimeler": ["slip casting", "sıvı çamur", "et payı", "kalıptan dökme", "akıtma"], "zorluk": "orta"},
    {"kelime": "çini tahriri çekmek", "aciklama": "samur fırça ve siyah tahrir boyasıyla karo üstündeki lale motiflerinin sınırını çizmek", "yasakli_kelimeler": ["tahrir", "samur fırça", "siyah kontur", "lale motifi", "iznik çinisi"], "zorluk": "orta"},
    {"kelime": "engob uygulamak", "aciklama": "ham kile renk vermek için üstüne renklendirilmiş astar çamuru sürmek", "yasakli_kelimeler": ["engobe", "renkli astar", "pişmemiş kil", "sıvı astar", "kaplama"], "zorluk": "orta"},
    {"kelime": "sgraffito kazımak", "aciklama": "engop sürülmüş yüzeyi sivri uçla kazıyarak alttaki kilin kontrast rengini çıkarmak", "yasakli_kelimeler": ["kazıma sanatı", "kontrast", "sivri uç", "alt renk", "desen kazıma"], "zorluk": "orta"},
    {"kelime": "krakle çatlağı oluşturmak", "aciklama": "sır ile kilin genleşme farkından faydalanarak sırda dekoratif kılcal çatlaklar yapmak", "yasakli_kelimeler": ["çatlak sır", "kılcal", "genleşme farkı", "dekoratif çatlak", "efekt"], "zorluk": "orta"},
    {"kelime": "fırın dizmek", "aciklama": "fırın raflarını ve sütunlarını yerleştirip ürünleri birbirine değmeyecek şekilde dizmek", "yasakli_kelimeler": ["fırın rafı", "kordiyerit plaka", "sütun", "raf dizilimi", "değmeme"], "zorluk": "orta"},
    {"kelime": "sır akması yaşamak", "aciklama": "aşırı sıcaklıkta eriyen sırın ürünün tabanından fırın plakasına damlayıp yapışması", "yasakli_kelimeler": ["akma", "plakaya yapışma", "aşırı ısı", "damlama", "sır hatası"], "zorluk": "orta"},
    {"kelime": "şamot karıştırmak", "aciklama": "kile önceden pişirilip öğütülmüş gözenekli seramik kırığı katarak fırında çatlamayı önlemek", "yasakli_kelimeler": ["grog", "pişmiş kil tozu", "büyük heykel", "çatlama önleme", "doku"], "zorluk": "orta"},
    {"kelime": "moka difüzyonu damlatmak", "aciklama": "ıslak engob üstüne asitli tütün suyu damlatıp ağaç dalı gibi yayılmasını izlemek", "yasakli_kelimeler": ["mocha tea", "ağaç deseni", "tütün suyu", "asit reaksiyonu", "difüzyon"], "zorluk": "orta"},
    {"kelime": "terakota üretmek", "aciklama": "kırmızı topraktan sırsız rustik saksı ve tuğlaları düşük ısıda pişirmek", "yasakli_kelimeler": ["kırmızı kil", "sırsız", "rustik", "saksı", "fırınlama"], "zorluk": "orta"},
    {"kelime": "porselen dökümü yapmak", "aciklama": "kaolin ve kuvarstan oluşan camsı beyaz porselen çamurunu yüksek ısıda eritmek", "yasakli_kelimeler": ["kaolin", "beyaz kil", "1250 derece", "yarı şeffaf", "camsı"], "zorluk": "orta"},
    {"kelime": "çimdikleme yapmak", "aciklama": "kil topunu başparmakla ortadan delip parmak uçlarıyla sıkarak kase oluşturmak", "yasakli_kelimeler": ["pinching", "parmakla sıkma", "küçük kase", "el yapımı", "başparmak"], "zorluk": "orta"},
    {"kelime": "balon patlaması olmak", "aciklama": "yoğururken içeride kalan hava kabarcığının fırında genleşip ürünü patlatması", "yasakli_kelimeler": ["hava boşluğu", "fırında patlama", "parçalanma", "genleşme", "yoğurma hatası"], "zorluk": "orta"},
    {"kelime": "lüster parıltısı vermek", "aciklama": "üçüncü pişirimde metalik altın veya platin tabakayı indirgen atmosferde parlatmak", "yasakli_kelimeler": ["metalik parıltı", "altın yaldız", "3. pişirim", "indirgen atmosfer", "yanardöner"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "raku fırınından çekmek", "aciklama": "1000 derecede kor alev halindeki vazoyu maşayla çıkarıp talaş dolu tenekeye basmak", "yasakli_kelimeler": ["kor kızıl", "talaş dumanı", "maşayla çıkarma", "termal şok", "japon tekniği"], "zorluk": "zor"},
    {"kelime": "kintsugi ile birleştirmek", "aciklama": "kırılan antika kaseyi urushi reçinesi ve saf altın tozu karışımıyla onarmak", "yasakli_kelimeler": ["altın tozu", "urushi", "kusurlu güzellik", "kırık birleştirme", "japon felsefesi"], "zorluk": "zor"},
    {"kelime": "indirgen pişirim yapmak", "aciklama": "fırın bacasını kapatıp oksijeni boğarak bakır oksiti yeşilden kan kırmızısına dönüştürmek", "yasakli_kelimeler": ["oksijen boğma", "redüksiyon", "öküz kanı sırrı", "karbonmonoksit", "flambe"], "zorluk": "zor"},
    {"kelime": "seladon sırrı geliştirmek", "aciklama": "demir oksit katkılı sırrı indirgen fırında pişirip yeşim taşı yeşili elde etmek", "yasakli_kelimeler": ["celadon", "yeşim taşı yeşili", "demir indirgenmesi", "çin seramiği", "yeşil sır"], "zorluk": "zor"},
    {"kelime": "segre konisi erimesi", "aciklama": "fırının ulaştığı gerçek ısı ve zaman kombinasyonunu piramit konilerin bükülmesinden okumak", "yasakli_kelimeler": ["orton konisi", "pirometrik koni", "bükülme açısı", "ısı işi", "fırın gözetleme"], "zorluk": "zor"},
    {"kelime": "kristal sır büyütmek", "aciklama": "çinko silikat sırrını fırın soğurken saatlerce bekletip sır içinde çiçek kristali açtırmak", "yasakli_kelimeler": ["çinko silikat", "kristalizasyon", "çiçek deseni", "kontrollü soğuma", "makrokristal"], "zorluk": "zor"},
    {"kelime": "anagama odun fırını yakmak", "aciklama": "tünel fırını 4 gün boyunca aralıksız odunla besleyip doğal uçucu kül sırrı yaratmak", "yasakli_kelimeler": ["odun fırını", "doğal kül sırrı", "4 gün yakma", "tünel fırın", "yüksek ateş"], "zorluk": "zor"},
    {"kelime": "vitrifikasyona uğramak", "aciklama": "yüksek sıcaklıkta kil içindeki silis ve feldspatın eriyip gözeneksiz cam fazına geçmesi", "yasakli_kelimeler": ["camsılaşma", "gözeneksiz", "feldspat erimesi", "yüksek derece", "su emmeme"], "zorluk": "zor"},
    {"kelime": "tuzlu pişirim yapmak", "aciklama": "1200 derecede fırın gözlerinden sofra tuzu atıp sodyum buharıyla portakal kabuğu sırrı yapmak", "yasakli_kelimeler": ["kaya tuzu", "sodyum buharı", "portakal kabuğu dokusu", "klor gazı", "buharlı sır"], "zorluk": "zor"},
    {"kelime": "saggar içinde gömmek", "aciklama": "ürünü refrakter kutu içine deniz tuzu, bakır tel ve muz kabuğuyla gömüp fırınlamak", "yasakli_kelimeler": ["refrakter kutu", "organik duman", "dumanlama", "kapalı kutu", "renk dumanı"], "zorluk": "zor"},
    {"kelime": "tiksotropik kıvam ayarlamak", "aciklama": "döküm çamurunun çalkalandığında akıcı, beklediğinde jelleşen reolojik dengesini kurmak", "yasakli_kelimeler": ["reoloji", "sodyum silikat", "defokülant", "akışkanlık", "jel kıvamı"], "zorluk": "zor"},
    {"kelime": "tenmoku sırrı pişirmek", "aciklama": "yüksek demirli sırın koni 10'da erimesiyle kase kenarında çay lekesi ve tavşan tüyü efekti alması", "yasakli_kelimeler": ["tavşan tüyü", "demir sırrı", "yağ damlası efekti", "japon çay kasesi", "koni 10"], "zorluk": "zor"},
    {"kelime": "dunting çatlağı yaşamak", "aciklama": "kuvars terslenmesi sırasında fırının çok hızlı soğutulmasıyla gövdenin jilet gibi yarılması", "yasakli_kelimeler": ["kuvars terslenmesi", "hızlı soğuma çatlağı", "termal şok kırılması", "573 derece", "yarılma"], "zorluk": "zor"},
    {"kelime": "refrakter astar çekmek", "aciklama": "fırın raflarını akan sırlardan korumak için alümina hidrat ve kaolin harcıyla boyamak", "yasakli_kelimeler": ["fırın yıkama", "kil astarı", "alümina", "raf koruma", "yapışma engeli"], "zorluk": "zor"}
]

seyahat_verbs = [
    # Kolay (12)
    {"kelime": "gezmek", "aciklama": "yeni bir şehirde sokakları, müzeleri ve meydanları dolaşmak", "yasakli_kelimeler": ["şehir", "sokak", "dolaşmak", "turist", "yeni yer"], "zorluk": "kolay"},
    {"kelime": "çanta toplamak", "aciklama": "yola çıkmadan önce eşyaları sırt çantasına veya valize doldurmak", "yasakli_kelimeler": ["sırt çantası", "eşya", "valiz", "yolculuk", "doldurmak"], "zorluk": "kolay"},
    {"kelime": "bilet almak", "aciklama": "uçak, tren veya otobüs yolculuğu için önceden bilet satın almak", "yasakli_kelimeler": ["uçak", "tren", "otobüs", "satın almak", "koltuk"], "zorluk": "kolay"},
    {"kelime": "otele yerleşmek", "aciklama": "resepsiyonda anahtarı alıp odaya valizleri bırakmak", "yasakli_kelimeler": ["resepsiyon", "oda", "anahtar", "konaklama", "valiz"], "zorluk": "kolay"},
    {"kelime": "fotoğraf çekmek", "aciklama": "tarihi eserlerin ve manzaraların önünde anı kaydetmek", "yasakli_kelimeler": ["kamera", "anı", "manzara", "poz", "hatıra"], "zorluk": "kolay"},
    {"kelime": "uçmak", "aciklama": "havalimanından uçağa binip bulutların üstünden başka ülkeye gitmek", "yasakli_kelimeler": ["uçak", "havalimanı", "havada", "gökyüzü", "ülke"], "zorluk": "kolay"},
    {"kelime": "hediyelik almak", "aciklama": "dönüşte sevdiklerine magnet, lokum veya biblo satın almak", "yasakli_kelimeler": ["magnet", "hatıra", "lokum", "dönüş", "satın alma"], "zorluk": "kolay"},
    {"kelime": "kaybolmak", "aciklama": "yabancı bir kentin ara sokaklarında yolu bulamayıp bakınmak", "yasakli_kelimeler": ["yol", "ara sokak", "yabancı şehir", "harita", "şaşırmak"], "zorluk": "kolay"},
    {"kelime": "yol sormak", "aciklama": "haritayı gösterip yerel halktan meydanın yönünü öğrenmek", "yasakli_kelimeler": ["tarif", "yön", "yerel halk", "harita", "adres"], "zorluk": "kolay"},
    {"kelime": "tatmak", "aciklama": "gidilen ülkenin geleneksel sokak lezzetlerini ve yemeklerini denemek", "yasakli_kelimeler": ["yemek", "lezzet", "denemek", "geleneksel", "mutfak"], "zorluk": "kolay"},
    {"kelime": "yola çıkmak", "aciklama": "sabah erkenden bavulları arabaya yükleyip tatile başlamak", "yasakli_kelimeler": ["başlamak", "araba", "sabah", "yolculuk", "hareket"], "zorluk": "kolay"},
    {"kelime": "dinlenmek", "aciklama": "tüm gün yürüdükten sonra kafede oturup kahve içerek mola vermek", "yasakli_kelimeler": ["mola", "kafe", "yorgunluk", "oturmak", "çay"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "rezervasyon yapmak", "aciklama": "internet üzerinden uçuş ve otel odasını aylar öncesinden ayırtmak", "yasakli_kelimeler": ["ayırtmak", "booking", "erken", "otel", "uçuş"], "zorluk": "orta"},
    {"kelime": "vize başvurusu yapmak", "aciklama": "konsolosluğa evrakları, banka dökümünü ve pasaportu teslim etmek", "yasakli_kelimeler": ["pasaport", "konsolosluk", "evrak", "schengen", "onay"], "zorluk": "orta"},
    {"kelime": "pasaport kontrolünden geçmek", "aciklama": "sınır kapısında polise pasaportu uzatıp giriş damgası vurdurmak", "yasakli_kelimeler": ["sınır kapısı", "damga", "polis", "giriş", "kuyruk"], "zorluk": "orta"},
    {"kelime": "biniş kartı çıkarmak", "aciklama": "havalimanı kioskundan veya telefondan uçağa biniş belgesini barkodla almak", "yasakli_kelimeler": ["boarding pass", "kiosk", "barkod", "uçağa biniş", "belge"], "zorluk": "orta"},
    {"kelime": "bagaj teslim etmek", "aciklama": "büyük valizi tartıya koyup bagaj fişini alarak uçağın altına yollamak", "yasakli_kelimeler": ["valiz", "tartı", "kontuar", "kargo bölümü", "etiket"], "zorluk": "orta"},
    {"kelime": "pansiyonda kalmak", "aciklama": "sahil kasabasında samimi ve uygun fiyatlı aile işletmesinde konaklamak", "yasakli_kelimeler": ["konaklama", "aile işletmesi", "oda kahvaltı", "sahil", "ucuz otel"], "zorluk": "orta"},
    {"kelime": "rehber eşliğinde gezmek", "aciklama": "tur rehberinin anlattığı tarihi hikayeleri kulaklıkla dinleyerek antik kenti dolaşmak", "yasakli_kelimeler": ["tur rehberi", "anlatım", "grup turu", "kulaklık", "antik kent"], "zorluk": "orta"},
    {"kelime": "araba kiralamak", "aciklama": "havalimanındaki rent a car firmasından şehri gezmek için otomobil kiralamak", "yasakli_kelimeler": ["rent a car", "otomobil", "kasko", "sözleşme", "havalimanı"], "zorluk": "orta"},
    {"kelime": "duty free alışverişi", "aciklama": "havalimanının gümrüksüz mağazalarından parfüm ve çikolata almak", "yasakli_kelimeler": ["gümrüksüz", "parfüm", "çikolata", "havalimanı mağazası", "vergisiz"], "zorluk": "orta"},
    {"kelime": "döviz bozdurmak", "aciklama": "yabancı ülkeye varınca döviz bürosunda parayı yerel para birimine çevirmek", "yasakli_kelimeler": ["döviz bürosu", "kur", "yerel para", "euro dolar", "komisyon"], "zorluk": "orta"},
    {"kelime": "rötar yapmak", "aciklama": "uçağın teknik arıza veya hava şartları sebebiyle saatlerce gecikmesi", "yasakli_kelimeler": ["gecikme", "bekleme", "uçuş saati", "kapı", "tehir"], "zorluk": "orta"},
    {"kelime": "aktarma yapmak", "aciklama": "transit havalimanında uçaktan inip ikinci uçağın kapısına koşmak", "yasakli_kelimeler": ["transit", "aktarmalı uçuş", "bağlantı", "ikinci uçak", "kapı"], "zorluk": "orta"},
    {"kelime": "seyahat sigortası yaptırmak", "aciklama": "yurt dışında olası kaza ve hastalık masraflarını karşılayan poliçe almak", "yasakli_kelimeler": ["poliçe", "yurt dışı", "sağlık güvencesi", "kaza", "hastane masrafı"], "zorluk": "orta"},
    {"kelime": "hostelde ranzada yatmak", "aciklama": "sırt çantalı gezginlerin çok kişilik yatakhanelerde ucuza konaklaması", "yasakli_kelimeler": ["yatakhane", "ranza", "sırt çantalı", "ortak oda", "ucuz konaklama"], "zorluk": "orta"},
    {"kelime": "jet lag olmak", "aciklama": "kıtalararası uzun uçuş sonrası saat farkından dolayı gündüz uyuyup gece uyanık kalmak", "yasakli_kelimeler": ["saat farkı", "uyku bozukluğu", "kıtalararası", "zaman dilimi", "sersemlik"], "zorluk": "orta"},
    {"kelime": "ücretsiz araç bulmak", "aciklama": "yol kenarında bekleyerek geçen sürücülere katılmak için el etmek", "yasakli_kelimeler": ["otostopçu", "yolcu alma", "sürücü", "yol kenarı", "el işareti"], "zorluk": "orta"},
    {"kelime": "interrail biletiyle tren", "aciklama": "tek bir tren pasosuyla tüm avrupa ülkelerini raylar üzerinde gezmek", "yasakli_kelimeler": ["tren pasosu", "avrupa turu", "gar", "vagon", "raylar"], "zorluk": "orta"},
    {"kelime": "gezi rotası çizmek", "aciklama": "gün gün gezilecek tarihi noktaları ve müzeleri harita üzerinde sıraya dizmek", "yasakli_kelimeler": ["itinerary", "günlük plan", "harita rotası", "duraklar", "gezi planı"], "zorluk": "orta"},
    {"kelime": "pazarlık etmek", "aciklama": "kapalıçarşı veya doğu pazarlarında hediyelik eşya fiyatını yarıya indirmeye çalışmak", "yasakli_kelimeler": ["fiyat kırma", "pazar", "kapalıçarşı", "indirim isteme", "satıcı"], "zorluk": "orta"},
    {"kelime": "kruvaziyer gemisine binmek", "aciklama": "yüzen otel büyüklüğündeki dev lüks gemiyle ada ada dolaşmak", "yasakli_kelimeler": ["gemi turu", "liman", "ada turu", "kabin", "yüzen otel"], "zorluk": "orta"},
    {"kelime": "sanal tur gezmek", "aciklama": "evden bilgisayar ekranıyla louvre veya piramitleri 360 derece izlemek", "yasakli_kelimeler": ["360 derece", "ekrandan", "müze gezisi", "dijital", "evden"], "zorluk": "orta"},
    {"kelime": "yerel rehber tutmak", "aciklama": "turistlerin bilmediği gizli mekanları keşfetmek için bölgeyi bilen biriyle anlaşmak", "yasakli_kelimeler": ["özel rehber", "gizli mekanlar", "bölge uzmanı", "kişisel tur", "yerel"], "zorluk": "orta"},
    {"kelime": "e-sim yüklemek", "aciklama": "yurt dışında internete girmek için telefona dijital yabancı hat tanımlamak", "yasakli_kelimeler": ["dijital hat", "roaming", "yurt dışı internet", "hücresel veri", "karekod"], "zorluk": "orta"},
    {"kelime": "müze kart çıkarmak", "aciklama": "tüm ören yerlerine sıra beklemeden ücretsiz girmeyi sağlayan kartı almak", "yasakli_kelimeler": ["ören yeri", "sıra beklemeden", "giriş kartı", "kültür bakanlığı", "tarihi yer"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "overbooking mağduru olmak", "aciklama": "havayolunun koltuk sayısından fazla bilet satması yüzünden uçağa alınmamak", "yasakli_kelimeler": ["fazla bilet satışı", "kapıda kalma", "tazminat hakkı", "uçamamak", "yer olmaması"], "zorluk": "zor"},
    {"kelime": "couchsurfing ile misafir olmak", "aciklama": "yerel ev sahiplerinin evinde para vermeden kanepede kalarak kültür paylaşmak", "yasakli_kelimeler": ["ev paylaşımı", "ücretsiz kanepe", "kültür değişimi", "misafirlik", "ev sahibi"], "zorluk": "zor"},
    {"kelime": "vize serbestisi kazanmak", "aciklama": "iki ülke arasındaki anlaşmayla pasaportsuz veya vizesiz seyahat hakkı elde etmek", "yasakli_kelimeler": ["vize muafiyeti", "kapıda vize", "anlaşma", "serbest dolaşım", "sınırsız"], "zorluk": "zor"},
    {"kelime": "aktarmada bagaj kaybetmek", "aciklama": "kısa süreli aktarmada bavulun uçağa yetişemeyip kayıp eşya ofisine başvurmak", "yasakli_kelimeler": ["lost and found", "kayıp valiz", "pir raporu", "bagaj bandı", "yetişmeme"], "zorluk": "zor"},
    {"kelime": "couchsurfingde referans almak", "aciklama": "misafir olduğu ev sahibinden güvenilirlik yorumu ve puanı toplamak", "yasakli_kelimeler": ["misafir yorumu", "puan", "güvenilirlik", "ev sahibi", "profil"], "zorluk": "zor"},
    {"kelime": "karbon ayak izini telafi etmek", "aciklama": "kıtalararası uçuşun yaydığı sera gazı emisyonu karşılığında fidan bağışı yapmak", "yasakli_kelimeler": ["karbon ofset", "fidan bağışı", "uçak emisyonu", "yeşil seyahat", "dengeleme"], "zorluk": "zor"},
    {"kelime": "turist tuzağından kaçınmak", "aciklama": "tarihi merkezlerdeki fahiş fiyatlı kalitesiz mekanları sezilip yerellerin yerine gitmek", "yasakli_kelimeler": ["tourist trap", "fahiş fiyat", "kazıklanma", "kalitesiz restoran", "yerel mekan"], "zorluk": "zor"},
    {"kelime": "tax free iadesi almak", "aciklama": "yurt dışında ödenen katma değer vergisini havalimanı gümrüğünde nakit geri almak", "yasakli_kelimeler": ["kdv iadesi", "gümrük damgası", "fatura iadesi", "global blue", "havalimanı gişesi"], "zorluk": "zor"},
    {"kelime": "mil puanıyla biletlemek", "aciklama": "kredi kartında ve uçuşlarda biriken havayolu millerini bedava uçuşa çevirmek", "yasakli_kelimeler": ["miles and smiles", "ödül bilet", "puan harcama", "statü mili", "bedava uçuş"], "zorluk": "zor"},
    {"kelime": "konsolosluk yardımı istemek", "aciklama": "yurt dışında pasaport çalınması veya gözaltı durumunda büyükelçilikten acil geçici pasaport almak", "yasakli_kelimeler": ["geçici pasaport", "büyükelçilik", "acil durum", "hırsızlık", "vatandaş hakkı"], "zorluk": "zor"},
    {"kelime": "aparthotelde yemek pişirmek", "aciklama": "kendi mutfağı olan stüdyo dairede marketten alışveriş yapıp yemek hazırlamak", "yasakli_kelimeler": ["mutfaklı oda", "stüdyo daire", "kendi yemeği", "market alışverişi", "uzun konaklama"], "zorluk": "zor"},
    {"kelime": "tahliye uçuşuna yetişmek", "aciklama": "savaş veya pandemi sebebiyle ülkeye dönmek için düzenlenen özel kurtarma uçağına binmek", "yasakli_kelimeler": ["özel tahliye", "kurtarma uçuşu", "pandemi dönüşü", "kriz masası", "vatandaş tahliyesi"], "zorluk": "zor"},
    {"kelime": "dijital göçebe olarak çalışmak", "aciklama": "dünyayı gezerken dizüstü bilgisayarla kafelerden uzaktan işini yürütmek", "yasakli_kelimeler": ["digital nomad", "uzaktan çalışma", "remote", "dizüstü", "mekandan bağımsız"], "zorluk": "zor"},
    {"kelime": "kutup ışığı kovalamak", "aciklama": "norveç veya izlanda'da dondurucu gecede aurora borealis dansını görmek için tur yapmak", "yasakli_kelimeler": ["aurora borealis", "kuzey ışıkları", "yeşil ışık", "izlanda", "kutup gecesi"], "zorluk": "zor"}
]

if __name__ == "__main__":
    add_and_save_verbs("seramik", seramik_verbs)
    add_and_save_verbs("seyahat", seyahat_verbs)
