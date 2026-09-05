# -*- coding: utf-8 -*-
from card_utils import add_and_save_verbs

satranc_verbs = [
    # Kolay (12)
    {"kelime": "hamle yapmak", "aciklama": "sırası geldiğinde tahtadaki bir taşı kurallara uygun oynatmak", "yasakli_kelimeler": ["taş", "oynamak", "sıra", "tahta", "kare"], "zorluk": "kolay"},
    {"kelime": "şah çekmek", "aciklama": "rakibin şahını tehdit eden bir kareye taş basmak", "yasakli_kelimeler": ["şah", "tehdit", "saldırı", "kare", "uyarı"], "zorluk": "kolay"},
    {"kelime": "mat etmek", "aciklama": "şahı kaçamayacak ve kurtulamayacak şekilde sıkıştırıp oyunu kazanmak", "yasakli_kelimeler": ["şahmat", "kazanmak", "kaçış yok", "oyun sonu", "zafer"], "zorluk": "kolay"},
    {"kelime": "taş yemek", "aciklama": "rakibin taşının durduğu kareye kendi taşını koyup onu tahtadan almak", "yasakli_kelimeler": ["almak", "kırmak", "tahtadan çıkarma", "rakip taş", "ele geçirme"], "zorluk": "kolay"},
    {"kelime": "rok atmak", "aciklama": "şah ile kaleyi aynı hamlede birbirinin üzerinden atlatıp köşeye gizlemek", "yasakli_kelimeler": ["kale", "şah", "uzun rok", "kısa rok", "güvenlik"], "zorluk": "kolay"},
    {"kelime": "piyon sürmek", "aciklama": "önündeki eri bir veya başlangıçta iki kare ileri itmek", "yasakli_kelimeler": ["piyon", "er", "ileri", "kare", "adım"], "zorluk": "kolay"},
    {"kelime": "berabere kalmak", "aciklama": "oyunun pat veya yetersiz materyalle galip çıkmadan yarım puanla bitmesi", "yasakli_kelimeler": ["pat", "yarım puan", "beraberlik", "galip yok", "anlaşma"], "zorluk": "kolay"},
    {"kelime": "terk etmek", "aciklama": "durumun umutsuz olduğunu görüp şahını devirerek yenilgiyi kabul etmek", "yasakli_kelimeler": ["şahı devirme", "istifa", "yenilgi", "pes etme", "bırakmak"], "zorluk": "kolay"},
    {"kelime": "saate basmak", "aciklama": "hamleyi yaptıktan sonra kendi süresini durdurup rakibin süresini başlatmak", "yasakli_kelimeler": ["satranç saati", "süre", "durdurmak", "zaman", "buton"], "zorluk": "kolay"},
    {"kelime": "taş dizmek", "aciklama": "oyun başlamadan 32 taşı 64 karelik satranç tahtasına yerleştirmek", "yasakli_kelimeler": ["tahta", "64 kare", "32 taş", "başlangıç", "yerleşim"], "zorluk": "kolay"},
    {"kelime": "düşünmek", "aciklama": "hamle yapmadan önce tahtadaki varyantları ve tehditleri zihinde hesaplamak", "yasakli_kelimeler": ["hesap", "varyant", "plan", "zihin", "süre"], "zorluk": "kolay"},
    {"kelime": "vezir çıkmak", "aciklama": "son yataya ulaşan piyonu en güçlü taşa dönüştürmek", "yasakli_kelimeler": ["terfi", "8. yatay", "piyon dönüşümü", "en güçlü", "yeni vezir"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "açmazda bırakmak", "aciklama": "arkasındaki şah veya vezir düşmesin diye aradaki taşın kıpırdayamaması", "yasakli_kelimeler": ["açmaz", "pin", "arkadaki taş", "kıpırdama yasağı", "bağlama"], "zorluk": "orta"},
    {"kelime": "çatal atmak", "aciklama": "at veya piyon ile aynı anda iki değerli rakip taşa birden saldırmak", "yasakli_kelimeler": ["çatal", "fork", "aynı anda", "at hamlesi", "çifte tehdit"], "zorluk": "orta"},
    {"kelime": "şiş takmak", "aciklama": "öndeki değerli taşa saldırıp o kaçınca arkadaki daha az değerli taşı vurmak", "yasakli_kelimeler": ["skewer", "öndeki taş", "arkadaki taş", "kaçış", "hat"], "zorluk": "orta"},
    {"kelime": "feda yapmak", "aciklama": "mat atağı veya pozisyonel üstünlük kazanmak için piyon ya da taşını kurban etmek", "yasakli_kelimeler": ["kurban", "fedakarlık", "vezir fedası", "taktik kazanç", "bırakma"], "zorluk": "orta"},
    {"kelime": "merkezi tutmak", "aciklama": "d4, e4, d5, e5 kritik karelerini piyon ve atlarla kontrol altına almak", "yasakli_kelimeler": ["d4 e4", "merkez kareler", "kontrol", "alan hakimiyeti", "er"], "zorluk": "orta"},
    {"kelime": "geçer piyon yaratmak", "aciklama": "önünde veya komşu sütunlarında kendisini durduracak rakip piyon kalmamış er", "yasakli_kelimeler": ["passed pawn", "durdurulamayan er", "terfi yolu", "serbest piyon", "sütun"], "zorluk": "orta"},
    {"kelime": "açarak şah çekmek", "aciklama": "öndeki taşı kenara çekerek arkadaki kale veya filin gizli hattını açığa vurmak", "yasakli_kelimeler": ["açarak saldırı", "arkadaki taş", "hat açma", "gizli tehdit", "çifte şah"], "zorluk": "orta"},
    {"kelime": "çifte şah çekmek", "aciklama": "aynı anda iki farklı taşla birden şah çekip rakibi sadece şah oynamaya zorlamak", "yasakli_kelimeler": ["iki taş birden", "kapatılamaz", "zorunlu kaçış", "şah hareketi", "taktik"], "zorluk": "orta"},
    {"kelime": "pat yapmak", "aciklama": "şahı tehdit altında olmayan ama kurallara uygun yapacak hiçbir hamlesi kalmayan durum", "yasakli_kelimeler": ["beraberlik", "hamlesiz kalma", "şah tehditsiz", "sıkışma", "pat durumu"], "zorluk": "orta"},
    {"kelime": "açık hat ele geçirmek", "aciklama": "üzerinde hiç piyon bulunmayan dikey sütuna ağır kaleleri yerleştirmek", "yasakli_kelimeler": ["açık sütun", "dikey hat", "kale çiftleme", "inme", "kontrol"], "zorluk": "orta"},
    {"kelime": "kaleleri çiftlemek", "aciklama": "aynı açık sütun üzerine iki kaleyi alt alta dizip batarya kurmak", "yasakli_kelimeler": ["batarya", "iki kale", "açık sütun", "arka arkaya", "güç"], "zorluk": "orta"},
    {"kelime": "fianchetto yapmak", "aciklama": "fili g2 veya b2 karesine koyup çapraz uzun diyagonal boyunca uzatmak", "yasakli_kelimeler": ["uzun çapraz", "b2 g2", "fil yerleşimi", "kanat", "g3 b3"], "zorluk": "orta"},
    {"kelime": "notasyon yazmak", "aciklama": "yapılan her hamleyi satranç kağıdına standart harf ve rakamlarla kaydetmek", "yasakli_kelimeler": ["hamle kağıdı", "cebirsel notasyon", "kayıt", "kalem", "e4 e5"], "zorluk": "orta"},
    {"kelime": "zaman sıkışmasına girmek", "aciklama": "saatte son bir dakikası kalıp hamleleri panikle saniyeler içinde yapmak", "yasakli_kelimeler": ["zeitnot", "son dakika", "panik", "zaman azlığı", "bayrak düşmesi"], "zorluk": "orta"},
    {"kelime": "en passant yapmak", "aciklama": "iki kare fırlayan rakip piyonu sanki bir kare gitmiş gibi çaprazdan geçerken almak", "yasakli_kelimeler": ["geçerken alma", "özel kural", "iki kare fırlama", "çapraz", "piyon"], "zorluk": "orta"},
    {"kelime": "gambit oynamak", "aciklama": "açılışta hızlı gelişim ve alan üstünlüğü için bilerek piyon feda etmek", "yasakli_kelimeler": ["şah gambiti", "vezir gambiti", "açılış fedası", "gelişim", "piyon kurbanı"], "zorluk": "orta"},
    {"kelime": "fil çiftini korumak", "aciklama": "tahtadaki iki filini de elinde tutarak açık oyunda rakip atlara üstünlük kurmak", "yasakli_kelimeler": ["iki fil", "açık konum", "atlara karşı", "çapraz güç", "avantaj"], "zorluk": "orta"},
    {"kelime": "blitz oynamak", "aciklama": "toplam 3 veya 5 dakikalık aşırı hızlı yıldırım satranç temposunda yarışmak", "yasakli_kelimeler": ["yıldırım", "3 dakika", "hızlı tempo", "refleks", "saat"], "zorluk": "orta"},
    {"kelime": "bullet oynamak", "aciklama": "toplam 1 dakikalık kurşun hızında hamle yaparak fareyle yarışmak", "yasakli_kelimeler": ["1 dakika", "kurşun satranç", "aşırı hızlı", "fare hızı", "premove"], "zorluk": "orta"},
    {"kelime": "taktik bulmaca çözmek", "aciklama": "kitaptan veya siteden iki hamlede mat kombinasyonlarını zihinde bulmak", "yasakli_kelimeler": ["puzzle", "kombinezon", "taktik tema", "iki hamlede mat", "antreman"], "zorluk": "orta"},
    {"kelime": "sürekli şah çekmek", "aciklama": "kaybetmekte olan tarafın peş peşe durmaksızın şah çekerek beraberlik koparması", "yasakli_kelimeler": ["perpetual check", "sonsuz şah", "beraberlik kurtarma", "kaçışsız", "tekrar"], "zorluk": "orta"},
    {"kelime": "konumsal baskı kurmak", "aciklama": "taktik numara yapmadan rakibin alanını daraltıp taşlarını felç etmek", "yasakli_kelimeler": ["pozisyonel oyun", "alan daraltma", "felç etme", "karpov stili", "yavaş boğma"], "zorluk": "orta"},
    {"kelime": "şah kanadı hücumu", "aciklama": "tüm taşları rakip şahın rok attığı tarafa yığıp piyon fırtınası koparmak", "yasakli_kelimeler": ["piyon fırtınası", "h4 g4", "rok tarafı", "hücum", "mat atağı"], "zorluk": "orta"},
    {"kelime": "oyun sonuna geçmek", "aciklama": "vezirleri ve hafif taşları kırışarak az taşlı piyon finallerine girmek", "yasakli_kelimeler": ["endgame", "vezir kırışması", "az taş", "final", "şah aktivitesi"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "zugzwang durumuna sokmak", "aciklama": "rakibin yapmak zorunda olduğu her hamlenin kendi konumunu kaçınılmaz batırması", "yasakli_kelimeler": ["hamle zorunluluğu", "zorunlu kötüleşme", "hamle sırası laneti", "oyun sonu", "kıpırdayamama"], "zorluk": "zor"},
    {"kelime": "profilaksi uygulamak", "aciklama": "rakibin planladığı taktik tehdidi henüz başlamadan 3 hamle önceden sezilip önlemek", "yasakli_kelimeler": ["petrosian", "nimzowitsch", "önleyici hamle", "tehdidi sezme", "engelleme"], "zorluk": "zor"},
    {"kelime": "karelerin hakimiyeti", "aciklama": "özellikle beyaz veya siyah renk kompleksindeki zayıflamış karelere yerleşmek", "yasakli_kelimeler": ["renk kompleksi", "zayıf kareler", "renk hakimiyeti", "delik kare", "blokaj"], "zorluk": "zor"},
    {"kelime": "triangülasyon yapmak", "aciklama": "oyun sonunda şahla üçgen çizerek hamle sırasını rakibe verip zugzwang yaratmak", "yasakli_kelimeler": ["üçgen çizme", "şah hamlesi", "hamle sırası devri", "kare kaybetme", "piyon finali"], "zorluk": "zor"},
    {"kelime": "lucena konumunu kurmak", "aciklama": "kale oyun sonlarında köprü kurma tekniğiyle şahı ve geçer piyonu terfiye taşımak", "yasakli_kelimeler": ["köprü kurma", "kale finali", "7. yatay", "geçer piyon", "kazanç tekniği"], "zorluk": "zor"},
    {"kelime": "philidor savunması çekmek", "aciklama": "kale oyun sonlarında 6. yatayda bekleyip şah gelince arkadan sonsuz şahla beraberliği tutmak", "yasakli_kelimeler": ["6. yatay kesme", "arkadan şah", "kale finali beraberlik", "pasif savunma", "beraberlik reçetesi"], "zorluk": "zor"},
    {"kelime": "intermezzo araya sokmak", "aciklama": "beklenen zorunlu alış hamlesinden önce rakibi şok eden beklenmedik ara şah patlatmak", "yasakli_kelimeler": ["ara hamle", "zwischenzug", "beklenmedik", "şok hamle", "öncelik"], "zorluk": "zor"},
    {"kelime": "izole piyonu kuşatmak", "aciklama": "komşu sütunlarında hiçbir koruyucu piyonu olmayan d4 tecrit erini ablukaya almak", "yasakli_kelimeler": ["d4 tecrit", "izole d piyonu", "iqp", "blokaj karesi", "zayıflık"], "zorluk": "zor"},
    {"kelime": "asılı piyonları yarmak", "aciklama": "yan yana duran iki merkez piyonunun ilerlemesini provoke edip zayıflatmak", "yasakli_kelimeler": ["hanging pawns", "yan yana erler", "merkez piyon çifti", "yarma", "hedef"], "zorluk": "zor"},
    {"kelime": "kraliyet çatalı vurmak", "aciklama": "at ile aynı anda hem şaha hem vezire hem de kaleye çatal basıp oyunu bitirmek", "yasakli_kelimeler": ["şah vezir at çatalı", "büyük çatal", "at darbesi", "vezir kaybı", "üçlü saldırı"], "zorluk": "zor"},
    {"kelime": "fianchetto filini kırmak", "aciklama": "rakip şahın önündeki koruyucu g2 filini kendi filiyle değişip şah kanadını soymak", "yasakli_kelimeler": ["bh6", "koruyucu fil kırışması", "karanlık kare zayıflığı", "rok soyma", "h hat matı"], "zorluk": "zor"},
    {"kelime": "motor analizi çalıştırmak", "aciklama": "stockfish yapay zeka motoruyla konumun santipawn cinsinden artı eksi değerlendirmesini almak", "yasakli_kelimeler": ["stockfish", "değerlendirme puanı", "centipawn", "yapay zeka", "derinlik"], "zorluk": "zor"},
    {"kelime": "teori hazırlığı yapmak", "aciklama": "büyükusta seviyesinde açılış veri tabanından 25. hamleye kadar yenilik ezberlemek", "yasakli_kelimeler": ["novelty", "açılış teorisi", "büyükusta", "20 hamle ezber", "chessbase"], "zorluk": "zor"},
    {"kelime": "kare kuralını işletmek", "aciklama": "piyonun terfi karesine olan mesafesiyle zihinsel kare çizip rakip şahın yetişip yetişemeyeceğini bilmek", "yasakli_kelimeler": ["piyon karesi", "geometrik kural", "şah yetişmesi", "oyun sonu hesabı", "sayma"], "zorluk": "zor"}
]

savas_verbs = [
    # Kolay (12)
    {"kelime": "savaşmak", "aciklama": "iki ordunun cephede silahlarla birbiriyle çarpışması", "yasakli_kelimeler": ["çarpışmak", "ordu", "cephe", "silah", "meydan"], "zorluk": "kolay"},
    {"kelime": "saldırmak", "aciklama": "düşman mevzilerine doğru topyekun taarruza geçmek", "yasakli_kelimeler": ["taarruz", "hücum", "ileri", "düşman", "mevzi"], "zorluk": "kolay"},
    {"kelime": "savunmak", "aciklama": "düşman saldırısına karşı siperleri ve vatan toprağını korumak", "yasakli_kelimeler": ["müdafaa", "siper", "korumak", "mevzi", "dayanmak"], "zorluk": "kolay"},
    {"kelime": "ateş etmek", "aciklama": "tüfek veya topla düşman hedeflerine mermi yağdırmak", "yasakli_kelimeler": ["mermi", "tüfek", "top", "tetik", "hedef"], "zorluk": "kolay"},
    {"kelime": "bombalamak", "aciklama": "uçak veya toplarla düşman mevzilerine bomba fırlatmak", "yasakli_kelimeler": ["bomba", "patlama", "uçak", "hava saldırısı", "yıkım"], "zorluk": "kolay"},
    {"kelime": "kaçmak", "aciklama": "bozguna uğrayan askerlerin canını kurtarmak için geri çekilmesi", "yasakli_kelimeler": ["bozgun", "firar", "can havli", "geri çekilme", "terk"], "zorluk": "kolay"},
    {"kelime": "teslim olmak", "aciklama": "beyaz bayrak çekip silahları bırakarak düşmana teslim olmak", "yasakli_kelimeler": ["beyaz bayrak", "silah bırakma", "esir", "yenilgi", "pes"], "zorluk": "kolay"},
    {"kelime": "kazanmak", "aciklama": "düşman ordusunu imha edip meydandan zaferle ayrılmak", "yasakli_kelimeler": ["zafer", "galibiyet", "yenmek", "başarı", "kupa"], "zorluk": "kolay"},
    {"kelime": "kaybetmek", "aciklama": "savaşta ağır kayıplar verip hezimete uğramak", "yasakli_kelimeler": ["hezimet", "yenilgi", "mağlubiyet", "kayıp", "yıkım"], "zorluk": "kolay"},
    {"kelime": "siper kazmak", "aciklama": "mermilerden ve şarapnelden korunmak için toprağı hendek şeklinde oymak", "yasakli_kelimeler": ["hendek", "toprak", "kürek", "korunma", "mevzi"], "zorluk": "kolay"},
    {"kelime": "nöbet tutmak", "aciklama": "karakolda veya sınır boyunda gece tüfek elde uyanık beklemek", "yasakli_kelimeler": ["karakol", "sınır", "gece", "uyanık", "beklemek"], "zorluk": "kolay"},
    {"kelime": "emir vermek", "aciklama": "komutanın askerlerine hücum veya ateş talimatı bildirmesi", "yasakli_kelimeler": ["komutan", "talimat", "hücum emri", "subay", "bildirmek"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "pusu kurmak", "aciklama": "düşman konvoyunun geçeceği vadi boğazında gizlenip aniden saldırmak", "yasakli_kelimeler": ["tuzak", "boğaz", "vadi", "gizlenme", "ani saldırı"], "zorluk": "orta"},
    {"kelime": "kuşatmak", "aciklama": "düşman kalesini veya şehrini çepeçevre sarıp ikmal yollarını kesmek", "yasakli_kelimeler": ["muhasara", "çember", "ikmal kesme", "kale", "abluka"], "zorluk": "orta"},
    {"kelime": "mayın döşemek", "aciklama": "tankların ve piyadelerin geçişini engellemek için toprağa patlayıcı gömmek", "yasakli_kelimeler": ["patlayıcı", "toprak altı", "tuzak", "tank mayını", "patlama"], "zorluk": "orta"},
    {"kelime": "tahkimat yapmak", "aciklama": "mevzileri kum torbaları, beton sığınaklar ve dikenli tellerle güçlendirmek", "yasakli_kelimeler": ["kum torbası", "beton sığınak", "dikenli tel", "güçlendirme", "savunma hattı"], "zorluk": "orta"},
    {"kelime": "ikmal sağlamak", "aciklama": "cephedeki birliklere kamyonlarla mühimmat, yakıt ve erzak ulaştırmak", "yasakli_kelimeler": ["lojistik", "mühimmat", "erzak", "yakıt", "ulaştırma"], "zorluk": "orta"},
    {"kelime": "keşif uçuşu yapmak", "aciklama": "düşman mevzilerini ve radar yerleşimlerini havadan fotoğraflamak", "yasakli_kelimeler": ["hava keşfi", "istihbarat", "fotoğraf", "mevzi tespiti", "dron"], "zorluk": "orta"},
    {"kelime": "esir takası yapmak", "aciklama": "savaş esirlerini tarafsız sınır kapısında karşılıklı değiştirmek", "yasakli_kelimeler": ["savaş esiri", "değişim", "kızılhaç", "sınır kapısı", "takas"], "zorluk": "orta"},
    {"kelime": "ateşkes ilan etmek", "aciklama": "müzakereler sürerken silahları belirli bir tarihe kadar geçici susturmak", "yasakli_kelimeler": ["moratoryum", "geçici barış", "silah bırakma", "müzakere", "tarih"], "zorluk": "orta"},
    {"kelime": "seferberlik ilan etmek", "aciklama": "ülke tehlikeye girince tüm eli silah tutan erkekleri orduya çağırmak", "yasakli_kelimeler": ["askere çağırma", "topyekun", "silah altına", "genel seferberlik", "hazırlık"], "zorluk": "orta"},
    {"kelime": "köprü uçurmak", "aciklama": "düşman tanklarının nehir üzerinden ilerlemesini durdurmak için dinamitle patlatmak", "yasakli_kelimeler": ["dinamit", "patlatma", "nehir köprüsü", "tank engeli", "geri çekilme"], "zorluk": "orta"},
    {"kelime": "cephe yarmak", "aciklama": "tank tümenleriyle düşmanın en zayıf savunma hattını yarıp arkasına sarkmak", "yasakli_kelimeler": ["yarma harekatı", "savunma hattı", "tank tümeni", "derinlik", "arkaya sarkma"], "zorluk": "orta"},
    {"kelime": "çembere almak", "aciklama": "kanatlardan ilerleyerek düşman ordusunu dört bir yandan kuşatıp hapsetmek", "yasakli_kelimeler": ["kuşatma", "kiskaç", "çift kanat", "stalingrad", "kurtulamama"], "zorluk": "orta"},
    {"kelime": "kamuflaj yapmak", "aciklama": "tank ve çadırların üstünü yaprak ve kamuflaj filesiyle örterek gizlemek", "yasakli_kelimeler": ["kamuflaj filesi", "gizleme", "yeşil boya", "yaprak", "görünmez kılma"], "zorluk": "orta"},
    {"kelime": "hava indirme yapmak", "aciklama": "paraşütçü komandoları nakliye uçaklarından düşman hatlarının gerisine atmak", "yasakli_kelimeler": ["paraşütçü", "komando", "düşman gerisi", "uçaktan atlama", "indirme"], "zorluk": "orta"},
    {"kelime": "şarapnel saçılmak", "aciklama": "patlayan top mermisinin çelik gövdesinin binlerce keskin parça halinde dağılması", "yasakli_kelimeler": ["keskin parça", "çelik parçacık", "top mermisi", "yaralanma", "patlama"], "zorluk": "orta"},
    {"kelime": "istihbarat toplamak", "aciklama": "ajanlar ve telsiz dinlemeleriyle düşmanın taarruz planlarını öğrenmek", "yasakli_kelimeler": ["ajan", "telsiz dinleme", "casus", "plan", "öğrenme"], "zorluk": "orta"},
    {"kelime": "telsiz karartması", "aciklama": "baskın öncesi düşman sinyal istihbaratına yakalanmamak için tüm telsizleri kapatmak", "yasakli_kelimeler": ["telsiz yasağı", "sessizlik", "sinyal", "baskın öncesi", "iletişim kesme"], "zorluk": "orta"},
    {"kelime": "imha etmek", "aciklama": "ele geçirilen düşman silah deposunu ve cephaneliğini tamamen havaya uçurmak", "yasakli_kelimeler": ["yok etmek", "cephanelik", "havaya uçurma", "silah deposu", "patlatma"], "zorluk": "orta"},
    {"kelime": "baskın düzenlemek", "aciklama": "gece karanlığında düşman karargahına beklenmedik ani taarruz yapmak", "yasakli_kelimeler": ["gece baskını", "ani saldırı", "karargah", "hazırlıksız", "şafak vakti"], "zorluk": "orta"},
    {"kelime": "taktik geri çekilme", "aciklama": "daha elverişli savunma hatlarına geçmek için düzeni bozmadan ricat etmek", "yasakli_kelimeler": ["ricat", "düzenli çekilme", "elverişli hat", "taktik", "bozulmadan"], "zorluk": "orta"},
    {"kelime": "tank savar ateşi", "aciklama": "roketatar veya güdümlü füzeyle zırhlı düşman tankının zırhını delmek", "yasakli_kelimeler": ["bazuka", "rpg", "kornet", "zırh delme", "roket"], "zorluk": "orta"},
    {"kelime": "keskin nişancı atışı", "aciklama": "dürbünlü tüfekle gizlendiği yerden tek mermiyle düşman subayını vurmak", "yasakli_kelimeler": ["sniper", "dürbünlü tüfek", "tek atış", "subay hedefi", "kamufle"], "zorluk": "orta"},
    {"kelime": "abluka altına almak", "aciklama": "savaş gemileriyle düşman limanlarını kapatıp deniz ticaretini durdurmak", "yasakli_kelimeler": ["deniz ablukası", "liman kapatma", "savaş gemisi", "ticaret engeli", "deniz kuvvetleri"], "zorluk": "orta"},
    {"kelime": "cephe gerisine sızmak", "aciklama": "özel kuvvetler timinin sınır tellerini sessizce aşıp derin sabotaj yapması", "yasakli_kelimeler": ["özel kuvvetler", "sızma", "sabotaj", "derin harekat", "sessizce"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "blitzkrieg uygulamak", "aciklama": "tank, mekanize piyade ve dalış bombardıman uçaklarının eşgüdümüyle yıldırım savaşı", "yasakli_kelimeler": ["yıldırım savaşı", "guderian", "panzer", "stuka", "hızlı yarma"], "zorluk": "zor"},
    {"kelime": "derin harekat doktrini", "aciklama": "tüm düşman savunma derinliğine aynı anda topçu, hava ve zırhlı darbeyle çökme stratejisi", "yasakli_kelimeler": ["tukaçevski", "sovyet doktrini", "tüm derinlik", "operasyonel sanat", "kademeli yarma"], "zorluk": "zor"},
    {"kelime": "yanak kaydırma manevrası", "aciklama": "kendi cephesini sabit tutup düşmanın zayıf açık kanadına süvari ve zırhlılarla sarılmak", "yasakli_kelimeler": ["kanat çevirme", "flank", "açık kanat", "manevra", "kuşatma"], "zorluk": "zor"},
    {"kelime": "hannibal taktiği uygulamak", "aciklama": "merkezi bilerek geri çekip hilal oluşturarak cannae meydan muharebesinde düşmanı yutmak", "yasakli_kelimeler": ["cannae", "hilal taktiği", "merkez çekilmesi", "kanat kapanması", "hannibal"], "zorluk": "zor"},
    {"kelime": "hibrid savaş yürütmek", "aciklama": "konvansiyonel ordu yerine siber saldırı, dezenformasyon ve vekalet güçlerini harmanlamak", "yasakli_kelimeler": ["vekalet savaşı", "siber saldırı", "dezenformasyon", "asimetrik", "gri bölge"], "zorluk": "zor"},
    {"kelime": "c4isr sistemini kurmak", "aciklama": "komuta, kontrol, iletişim, bilgisayar, istihbarat ve gözetleme ağını müşterek bağlamak", "yasakli_kelimeler": ["ağ merkezli harp", "komuta kontrol", "durumsal farkındalık", "müşterek harekat", "dijital harp"], "zorluk": "zor"},
    {"kelime": "bastırıcı karşı batarya ateşi", "aciklama": "karşı topçu radarıyla düşman mermisinin yörüngesini hesaplayıp anında kaynağını vurmak", "yasakli_kelimeler": ["karşı topçu", "yörünge radarı", "topçu düellosu", "anında karşılık", "batarya imhası"], "zorluk": "zor"},
    {"kelime": "sead görevi icra etmek", "aciklama": "hava savunma radarlarını anti-radyasyon füzeleriyle kör edip hava sahasını temizlemek", "yasakli_kelimeler": ["wild weasel", "anti-radyasyon füzesi", "hava savunma bastırma", "radar körletme", "harm füzesi"], "zorluk": "zor"},
    {"kelime": "alan engelleme uygulamak", "aciklama": "gemi savar ve uzun menzilli füzelerle düşmanın deniz veya hava bölgesine girişini yasaklamak", "yasakli_kelimeler": ["a2/ad", "bölgeye erişim engelleme", "füze kalkanı", "giriş yasağı", "katmanlı savunma"], "zorluk": "zor"},
    {"kelime": "eskort jammer ile karıştırmak", "aciklama": "elektronik harp uçağının düşman hava radarlarına parazit ve sahte hedef basması", "yasakli_kelimeler": ["elektronik harp", "chaff flare", "jammer", "parazit yayma", "radar yanıltma"], "zorluk": "zor"},
    {"kelime": "kombine kollar taktiği", "aciklama": "piyade, tank, istihkam ve topçunun birbirinin zaafını örtecek kusursuz senkronizasyonu", "yasakli_kelimeler": ["combined arms", "müşterek taktik", "tank piyade iş birliği", "istihkam", "senkronizasyon"], "zorluk": "zor"},
    {"kelime": "yıpratma savaşına sokmak", "aciklama": "hızlı zafer yerine düşmanın insan ve malzeme kaynaklarını tüketene kadar kanlı yıpratma", "yasakli_kelimeler": ["attrition", "verdun", "kaynak tüketme", "kan kaybettirme", "yıpratma"], "zorluk": "zor"},
    {"kelime": "nükleer caydırıcılık sağlamak", "aciklama": "karşılıklı garantili imha doktriniyle ilk nükleer vuruşu engelleyecek nükleer üçleme kurmak", "yasakli_kelimeler": ["mad doktrini", "nükleer üçleme", "caydırıcılık", "kıtalararası balistik", "garantili imha"], "zorluk": "zor"},
    {"kelime": "loiter mühimmat uçurmak", "aciklama": "kamikaze dronun hedef bölge üzerinde saatlerce süzülüp hedefi görünce intihar dalışı yapması", "yasakli_kelimeler": ["kamikaze dron", "dolaşan mühimmat", "intihar dalışı", "nokta vuruş", "otonom saldırı"], "zorluk": "zor"}
]

if __name__ == "__main__":
    add_and_save_verbs("satranc", satranc_verbs)
    add_and_save_verbs("savas", savas_verbs)
