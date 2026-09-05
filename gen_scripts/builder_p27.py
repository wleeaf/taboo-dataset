# -*- coding: utf-8 -*-
from card_utils import add_and_save_verbs

mimarlik_verbs = [
    # Kolay (12)
    {"kelime": "çizmek", "aciklama": "kağıt veya ekranda bina planı ve projesi oluşturmak", "yasakli_kelimeler": ["plan", "proje", "cetvel", "kalem", "tasarım"], "zorluk": "kolay"},
    {"kelime": "tasarlamak", "aciklama": "yeni bir yapının formunu ve mekanlarını zihinde ve projede kurgulamak", "yasakli_kelimeler": ["kurgu", "fikir", "estetik", "bina", "mimar"], "zorluk": "kolay"},
    {"kelime": "inşa etmek", "aciklama": "tasarlanan yapıyı sahada malzeme kullanarak dikmek", "yasakli_kelimeler": ["yapı", "şantiye", "bina", "kurmak", "örme"], "zorluk": "kolay"},
    {"kelime": "ölçmek", "aciklama": "mekan boyutlarını ve mesafeleri metreyle belirlemek", "yasakli_kelimeler": ["metre", "boyut", "uzunluk", "alan", "mesafe"], "zorluk": "kolay"},
    {"kelime": "yıkmak", "aciklama": "eski veya riskli binayı yerle bir etmek", "yasakli_kelimeler": ["dozer", "enkaz", "kentsel dönüşüm", "moloz", "hasar"], "zorluk": "kolay"},
    {"kelime": "onarmak", "aciklama": "hasar gören veya eskiyen yapı elemanlarını tamir etmek", "yasakli_kelimeler": ["tamir", "tadilat", "yenilemek", "hasar", "bakım"], "zorluk": "kolay"},
    {"kelime": "boyamak", "aciklama": "duvar ve tavan yüzeylerine estetik renk katmanı sürmek", "yasakli_kelimeler": ["renk", "fırça", "duvar", "rulo", "tavan"], "zorluk": "kolay"},
    {"kelime": "döşemek", "aciklama": "zemin veya duvara parke, fayans veya seramik yerleştirmek", "yasakli_kelimeler": ["fayans", "parke", "zemin", "kaplama", "seramik"], "zorluk": "kolay"},
    {"kelime": "düzenlemek", "aciklama": "iç mekandaki mobilya ve donatıları işlevsel yerleştirmek", "yasakli_kelimeler": ["iç mimari", "yerleşim", "mobilya", "dekorasyon", "mekan"], "zorluk": "kolay"},
    {"kelime": "maketi yapmak", "aciklama": "binanın küçük ölçekli üç boyutlu fiziksel modelini üretmek", "yasakli_kelimeler": ["maket", "karton", "ölçek", "model", "minyatür"], "zorluk": "kolay"},
    {"kelime": "aydınlatmak", "aciklama": "iç ve dış mekanı doğal veya yapay ışıkla donatmak", "yasakli_kelimeler": ["ışık", "lamba", "avize", "pencere", "armatür"], "zorluk": "kolay"},
    {"kelime": "örneklemek", "aciklama": "tasarım için kullanılacak malzeme numunelerini seçmek", "yasakli_kelimeler": ["numune", "malzeme", "seçim", "katalog", "doku"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "kesit almak", "aciklama": "binayı düşey bir düzlemle kesip iç detaylarını çizmek", "yasakli_kelimeler": ["düşey", "plan", "görünüş", "detay", "çizim"], "zorluk": "orta"},
    {"kelime": "görünüş çizmek", "aciklama": "yapının cephelerinin karşıdan iki boyutlu projeksiyonunu çıkarmak", "yasakli_kelimeler": ["cephe", "ön", "yan", "projeksiyon", "çizim"], "zorluk": "orta"},
    {"kelime": "ruhsat almak", "aciklama": "belediyeden inşaat projesinin uygulanması için yasal izin çıkarmak", "yasakli_kelimeler": ["belediye", "izin", "yasal", "proje", "onay"], "zorluk": "orta"},
    {"kelime": "restorasyon yapmak", "aciklama": "tarihi yapıyı özgün mimarisine sadık kalarak yenilemek", "yasakli_kelimeler": ["tarihi", "anıt", "özgün", "koruma", "eski"], "zorluk": "orta"},
    {"kelime": "revizyon yapmak", "aciklama": "işveren veya yönetmelik talebiyle projede değişiklik yapmak", "yasakli_kelimeler": ["düzeltme", "değişiklik", "güncelleme", "proje", "talep"], "zorluk": "orta"},
    {"kelime": "şantiye denetlemek", "aciklama": "sahadaki yapım sürecinin projeye uygunluğunu kontrol etmek", "yasakli_kelimeler": ["şantiye", "kontrol", "uygunluk", "mühendis", "saha"], "zorluk": "orta"},
    {"kelime": "render almak", "aciklama": "üç boyutlu dijital modelin fotogerçekçi görsel çıktısını oluşturmak", "yasakli_kelimeler": ["3d", "görsel", "kaplama", "ışıklandırma", "yazılım"], "zorluk": "orta"},
    {"kelime": "akustik planlamak", "aciklama": "konser salonu veya odada ses yankılanmasını ve yalıtımını çözmek", "yasakli_kelimeler": ["ses", "yankı", "yalıtım", "panel", "salon"], "zorluk": "orta"},
    {"kelime": "ısı yalıtımı yapmak", "aciklama": "yapı kabuğunu mantolayarak enerji kaybını engellemek", "yasakli_kelimeler": ["mantolama", "strafor", "enerji", "cephe", "sıcaklık"], "zorluk": "orta"},
    {"kelime": "hakediş hazırlamak", "aciklama": "şantiyede tamamlanan imalatların metraj ve bedel tablosunu çıkarmak", "yasakli_kelimeler": ["metraj", "ödeme", "müteahhit", "fatura", "imalat"], "zorluk": "orta"},
    {"kelime": "imar durumunu sorgulamak", "aciklama": "arsanın emsal, çekme mesafesi ve gabari haklarını belediyeden öğrenmek", "yasakli_kelimeler": ["arsa", "emsal", "kaks", "taks", "belediye"], "zorluk": "orta"},
    {"kelime": "perspektif kurmak", "aciklama": "üç boyutlu derinlik algısını kaçış noktalarıyla kağıda aktarmak", "yasakli_kelimeler": ["kaçış noktası", "derinlik", "ufuk çizgisi", "3 boyut", "çizim"], "zorluk": "orta"},
    {"kelime": "statik çözümlemek", "aciklama": "yapının taşıyıcı sistemindeki yük aktarımlarını hesaplamak", "yasakli_kelimeler": ["taşıyıcı", "kolon", "kiriş", "yük", "inşaat mühendisi"], "zorluk": "orta"},
    {"kelime": "kot farkını çözmek", "aciklama": "eğimli arazide kademelendirme ve merdivenlerle seviye bağlamak", "yasakli_kelimeler": ["seviye", "eğim", "arazi", "kademeleme", "istinat"], "zorluk": "orta"},
    {"kelime": "fonksiyon şeması çıkarmak", "aciklama": "mekanlar arası kullanım ve sirkülasyon ilişkilerini baloncuklarla çizmek", "yasakli_kelimeler": ["leke", "şema", "sirkülasyon", "mekan", "ilişki"], "zorluk": "orta"},
    {"kelime": "detay paftası hazırlamak", "aciklama": "pencere, çatı veya döşeme birleşimlerinin 1/5 veya 1/1 ölçekli çizimi", "yasakli_kelimeler": ["ölçek", "pafta", "birleşim", "düğüm noktası", "teknik"], "zorluk": "orta"},
    {"kelime": "asma tavan yapmak", "aciklama": "tesisat borularını gizlemek ve estetik sağlamak için alçıpan tavan kurmak", "yasakli_kelimeler": ["alçıpan", "profil", "gizli ışık", "tesisat", "tavan"], "zorluk": "orta"},
    {"kelime": "sundurma eklemek", "aciklama": "bina girişini yağmurdan korumak için hafif konsol çatı yapmak", "yasakli_kelimeler": ["giriş", "saçak", "konsol", "yağmur", "kapı önü"], "zorluk": "orta"},
    {"kelime": "röleve çıkarmak", "aciklama": "mevcut tarihi yapının birebir ölçülerini alıp mevcut halini çizmek", "yasakli_kelimeler": ["mevcut", "ölçü", "tarihi", "çizim", "kayıt"], "zorluk": "orta"},
    {"kelime": "restitüsyon kurgulamak", "aciklama": "tarihi yapının zamanla yıkılan kısımlarının ilk halini tasarlamak", "yasakli_kelimeler": ["özgün", "ilk hal", "tarihi belge", "dönem", "çizim"], "zorluk": "orta"},
    {"kelime": "yangın kaçışı planlamak", "aciklama": "acil durumlarda tahliye mesafelerini ve yangın merdivenlerini çözmek", "yasakli_kelimeler": ["tahliye", "merdiven", "acil çıkış", "güvenlik", "yönetmelik"], "zorluk": "orta"},
    {"kelime": "peyzaj düzenlemek", "aciklama": "yapı çevresindeki açık alanların yeşil doku ve sert zeminini tasarlamak", "yasakli_kelimeler": ["bahçe", "yeşil alan", "bitki", "çevre", "sert zemin"], "zorluk": "orta"},
    {"kelime": "iskele kurmak", "aciklama": "dış cephe imalatları için geçici metal çalışma platformu inşa etmek", "yasakli_kelimeler": ["cephe", "platform", "şantiye", "yükseklik", "boru"], "zorluk": "orta"},
    {"kelime": "kalıp çakmak", "aciklama": "beton dökülmeden önce ahşap veya çelik sınır panellerini sabitlemek", "yasakli_kelimeler": ["beton", "ahşap", "demir", "döküm", "panel"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "brütalizm uygulamak", "aciklama": "işlenmemiş çıplak beton yüzeyleri ve anıtsal kütleleri öne çıkarmak", "yasakli_kelimeler": ["çıplak beton", "anıt", "akım", "sıvasız", "masif"], "zorluk": "zor"},
    {"kelime": "parametrik tasarlamak", "aciklama": "algoritmik formüller ve yazılımlarla akışkan organik formlar türetmek", "yasakli_kelimeler": ["algoritma", "zaha hadid", "akışkan", "formül", "grasshopper"], "zorluk": "zor"},
    {"kelime": "konsol çıkmak", "aciklama": "alttan destek almadan boşluğa doğru uzanan çıkma döşeme inşa etmek", "yasakli_kelimeler": ["çıkma", "boşluk", "desteksiz", "balkon", "moment"], "zorluk": "zor"},
    {"kelime": "dekonstrüktif parçalamak", "aciklama": "geleneksel dik açılı yapı formunu bozup eğik ve dinamik kütleler kurgulamak", "yasakli_kelimeler": ["parçalama", "eğik", "gehry", "dik açı", "akım"], "zorluk": "zor"},
    {"kelime": "biyoklimatik kurgulamak", "aciklama": "güneş açısı ve hakim rüzgardan pasif yararlanarak sıfır enerjili bina yapmak", "yasakli_kelimeler": ["pasif", "sürdürülebilir", "enerji", "güneş", "doğal havalandırma"], "zorluk": "zor"},
    {"kelime": "tektonik ifade kazandırmak", "aciklama": "yapı malzemesi ve taşıyıcı detaylarının mekansal estetiğe doğrudan yansıması", "yasakli_kelimeler": ["taşıyıcı", "strüktür", "malzeme", "eklem", "estetik"], "zorluk": "zor"},
    {"kelime": "kentsel dokuya entegre etmek", "aciklama": "yeni yapıyı çevresindeki sokak ölçeği ve tarihi siluetle bütünleştirmek", "yasakli_kelimeler": ["siluet", "sokak", "çevre", "ölçek", "morfoloji"], "zorluk": "zor"},
    {"kelime": "modülasyon oluşturmak", "aciklama": "tasarımı tekrar eden standart ızgara veya ölçü birimlerine dayandırmak", "yasakli_kelimeler": ["ızgara", "grid", "tekrar", "birim", "standart"], "zorluk": "zor"},
    {"kelime": "uzay kafes örtmek", "aciklama": "geniş açıklıkları hafif çelik çubukların üç boyutlu düğümleriyle geçmek", "yasakli_kelimeler": ["çelik", "açıklık", "düğüm", "kubbe", "çatı"], "zorluk": "zor"},
    {"kelime": "asma germe membran germek", "aciklama": "çelik halatlar ve gergin kumaş örtülerle geniş stadyum çatıları kurmak", "yasakli_kelimeler": ["halat", "membran", "kumaş", "gergi", "stadyum"], "zorluk": "zor"},
    {"kelime": "derz bırakmak", "aciklama": "sıcaklık genleşmesi ve oturma hareketleri için yapı blokları arasında boşluk payı vermek", "yasakli_kelimeler": ["dilatasyon", "genleşme", "boşluk", "çatlak", "oturma"], "zorluk": "zor"},
    {"kelime": "giydirme cephe asmak", "aciklama": "binanın ana iskeletine yük taşımayan alüminyum ve cam paneller monte etmek", "yasakli_kelimeler": ["cam", "alüminyum", "strüktürel", "ankraj", "dış kabuk"], "zorluk": "zor"},
    {"kelime": "le corbusier modülörünü kullanmak", "aciklama": "insan bedeni oranları ve altın orana dayalı mimari ölçek sistemini uygulamak", "yasakli_kelimeler": ["altın oran", "insan ölçeği", "oransal", "antropometri", "le corbusier"], "zorluk": "zor"},
    {"kelime": "kesme kuvvetini karşılamak", "aciklama": "deprem yatay yüklerine karşı perde betonarme duvarlar yerleştirmek", "yasakli_kelimeler": ["deprem", "perde duvar", "yatay yük", "rijitlik", "betonarme"], "zorluk": "zor"}
]

mitoloji_verbs = [
    # Kolay (12)
    {"kelime": "tapmak", "aciklama": "tanrılara ve kutsal varlıklara ibadet edip saygı göstermek", "yasakli_kelimeler": ["tanrı", "ibadet", "sunak", "dua", "kutsal"], "zorluk": "kolay"},
    {"kelime": "kurban etmek", "aciklama": "tanrıların öfkesini dindirmek veya lütuf almak için sunakta can adamak", "yasakli_kelimeler": ["sunak", "adak", "kesmek", "tanrı", "sunu"], "zorluk": "kolay"},
    {"kelime": "lanetlemek", "aciklama": "bir tanrının ölümlüye veya yaratığa sonsuz ceza vermesi", "yasakli_kelimeler": ["büyü", "ceza", "öfke", "gazap", "kötülük"], "zorluk": "kolay"},
    {"kelime": "kutsamak", "aciklama": "tanrısal güçle birini veya bir yeri koruma altına alıp yüceltmek", "yasakli_kelimeler": ["lütuf", "koruma", "tanrı", "iyilik", "aziz"], "zorluk": "kolay"},
    {"kelime": "yaratmak", "aciklama": "tanrıların evreni, insanı veya dünyayı yoktan var etmesi", "yasakli_kelimeler": ["yoktan", "var etmek", "evren", "insan", "kaos"], "zorluk": "kolay"},
    {"kelime": "cezalandırmak", "aciklama": "kibirli ölümlülere tanrıların ağır bedeller ödetmesi", "yasakli_kelimeler": ["ceza", "gazap", "sisifos", "tarsus", "öç"], "zorluk": "kolay"},
    {"kelime": "dua etmek", "aciklama": "tanrılardan yardım, zafer veya şifa dilemek", "yasakli_kelimeler": ["yakarmak", "dilek", "tapınak", "sunu", "yardım"], "zorluk": "kolay"},
    {"kelime": "dönüşmek", "aciklama": "tanrı veya insanın bir hayvana, ağaca veya yıldıza başkalaşması", "yasakli_kelimeler": ["başkalaşım", "hayvan", "ağaç", "form", "değişim"], "zorluk": "kolay"},
    {"kelime": "savaşmak", "aciklama": "tanrılar, titanlar veya kahramanların efsanevi meydanlarda çarpışması", "yasakli_kelimeler": ["meydan", "çarpışma", "kahraman", "kılıç", "titan"], "zorluk": "kolay"},
    {"kelime": "hükmetmek", "aciklama": "baş tanrının göklere, denizlere veya yeraltına egemen olması", "yasakli_kelimeler": ["egemenlik", "taht", "yönetmek", "güç", "krallık"], "zorluk": "kolay"},
    {"kelime": "kandırmak", "aciklama": "hilebaz tanrı veya kahramanların zekalarıyla rakiplerini aldatması", "yasakli_kelimeler": ["hile", "tuzak", "oyun", "zeka", "loki"], "zorluk": "kolay"},
    {"kelime": "efsaneleşmek", "aciklama": "yapılan kahramanlıkların dilden dile anlatılarak destanlaşması", "yasakli_kelimeler": ["destan", "anlatı", "ölümsüz", "şöhret", "çağ"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "kehanette bulunmak", "aciklama": "kahinlerin tapınakta tanrılardan aldıkları geleceği bildirmesi", "yasakli_kelimeler": ["kahin", "apollon", "delphi", "gelecek", "öngörü"], "zorluk": "orta"},
    {"kelime": "yeraltına inmek", "aciklama": "ölümlü kahramanın hades veya ölüler diyarına yolculuk yapması", "yasakli_kelimeler": ["hades", "ölüler diyarı", "katabasis", "styx", "ruh"], "zorluk": "orta"},
    {"kelime": "öfkesini dindirmek", "aciklama": "gazaba gelen tanrıya adaklar sunarak fırtınayı veya vebayı durdurmak", "yasakli_kelimeler": ["gazap", "adak", "kurban", "af", "hiddet"], "zorluk": "orta"},
    {"kelime": "canavarı katletmek", "aciklama": "kahramanın hidra, minotor veya medusa gibi canavarı öldürmesi", "yasakli_kelimeler": ["hidra", "minotor", "medusa", "kahraman", "öldürmek"], "zorluk": "orta"},
    {"kelime": "ölümsüzlük aramak", "aciklama": "gılgamış gibi kahramanların sonsuz yaşam otunu veya sırrını kovalaması", "yasakli_kelimeler": ["sonsuz yaşam", "gılgamış", "gençlik", "ölüm", "arayış"], "zorluk": "orta"},
    {"kelime": "yıldırım fırlatmak", "aciklama": "zeus veya thor gibi gök tanrılarının şimşek silahını savurması", "yasakli_kelimeler": ["zeus", "thor", "şimşek", "silah", "gök gürültüsü"], "zorluk": "orta"},
    {"kelime": "biçim değiştirmek", "aciklama": "tanrıların insanları aldatmak için kartal, boğa veya altın yağmuru olması", "yasakli_kelimeler": ["şekil", "kılık", "hayvan", "kamuflaj", "tanrısal"], "zorluk": "orta"},
    {"kelime": "adak adamak", "aciklama": "dileğin gerçekleşmesi halinde tapınağa değerli eşya veya hayvan sözü vermek", "yasakli_kelimeler": ["söz", "tapınak", "hediye", "sunak", "şükran"], "zorluk": "orta"},
    {"kelime": "labirentten çıkmak", "aciklama": "theseus'un ariadne'nin ipiyle karmaşık labirentten kurtulması", "yasakli_kelimeler": ["theseus", "ariadne", "ip", "minotor", "çıkış"], "zorluk": "orta"},
    {"kelime": "nehri geçmek", "aciklama": "ölen ruhların kharon'un kayığıyla styx nehrinden karşıya taşınması", "yasakli_kelimeler": ["kharon", "styx", "kayık", "para", "ruh"], "zorluk": "orta"},
    {"kelime": "ateşi çalmak", "aciklama": "prometheus'un olimpos'tan ateşi alıp insanlara hediye etmesi", "yasakli_kelimeler": ["prometheus", "insanlık", "olimpos", "hırsızlık", "kartal"], "zorluk": "orta"},
    {"kelime": "altın postu aramak", "aciklama": "iason ve argonavtların efsanevi kanatlı koç postunu ele geçirme seferi", "yasakli_kelimeler": ["iason", "argonavt", "kholkis", "post", "koç"], "zorluk": "orta"},
    {"kelime": "küllere dönmek", "aciklama": "anka kuşunun ömrü bitince yanıp kendi küllerinden yeniden doğması", "yasakli_kelimeler": ["anka", "simurg", "feniks", "yeniden doğuş", "yanmak"], "zorluk": "orta"},
    {"kelime": "taşa çevirmek", "aciklama": "medusa'nın gözlerine bakan kişiyi anında taş heykele dönüştürmesi", "yasakli_kelimeler": ["medusa", "bakış", "göz", "gorgon", "heykel"], "zorluk": "orta"},
    {"kelime": "elma atmak", "aciklama": "fitne tanrıçası eris'in en güzele yazılı altın elmayı tanrıçaların arasına atması", "yasakli_kelimeler": ["altın elma", "paris", "afrodit", "fitne", "truva"], "zorluk": "orta"},
    {"kelime": "taşı tepeye yuvarlamak", "aciklama": "sisifos'un tepeye çıkardığı kayanın her defasında aşağı yuvarlanması", "yasakli_kelimeler": ["sisifos", "kaya", "tepe", "sonsuz", "ceza"], "zorluk": "orta"},
    {"kelime": "güneşe çok yaklaşmak", "aciklama": "ikaros'un balmumu kanatlarıyla fazla yükselip denize düşmesi", "yasakli_kelimeler": ["ikaros", "balmumu", "kanat", "erimek", "daidalos"], "zorluk": "orta"},
    {"kelime": "kutuyu açmak", "aciklama": "pandora'nın merakına yenilip dünyaya tüm kötülükleri salması", "yasakli_kelimeler": ["pandora", "kötülük", "merak", "umut", "kapak"], "zorluk": "orta"},
    {"kelime": "topuktan vurulmak", "aciklama": "yenilmez aşil'in tek zayıf noktası olan aşil tendonundan oklanması", "yasakli_kelimeler": ["aşil", "ok", "zayıf nokta", "truva", "ölüm"], "zorluk": "orta"},
    {"kelime": "görevleri tamamlamak", "aciklama": "herkül'ün günahlarından arınmak için 12 imkansız görevi bitirmesi", "yasakli_kelimeler": ["herkül", "12 görev", "aslan", "zahmet", "kral"], "zorluk": "orta"},
    {"kelime": "şarap sunmak", "aciklama": "dionisos ayinlerinde tanrıya şarap ve coşku dolu bağbozumu sunusu yapmak", "yasakli_kelimeler": ["dionisos", "kadeh", "sarhoşluk", "ayin", "bağ"], "zorluk": "orta"},
    {"kelime": "gök kubbeyi taşımak", "aciklama": "atlas'ın omuzlarında gökyüzünü taşımaya mahkum edilmesi", "yasakli_kelimeler": ["atlas", "omuz", "gökyüzü", "dünya", "ceza"], "zorluk": "orta"},
    {"kelime": "gölgesine aşık olmak", "aciklama": "narkissos'un sudaki kendi yansımasını görüp eriyerek çiçeğe dönüşmesi", "yasakli_kelimeler": ["narkissos", "yansıma", "su", "çiçek", "kibir"], "zorluk": "orta"},
    {"kelime": "ambrosia ile beslenmek", "aciklama": "tanrıların genç ve ölümsüz kalmak için tanrısal nektar tüketmesi", "yasakli_kelimeler": ["nektar", "ölümsüzlük", "yiyecek", "içecek", "tanrı"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "apoteoz yaşamak", "aciklama": "ölümlü bir kahramanın ölümünden sonra tanrı mertebesine yükseltilmesi", "yasakli_kelimeler": ["tanrılaşma", "yükselme", "ölümlü", "mertebe", "zeus"], "zorluk": "zor"},
    {"kelime": "titanomahi başlatmak", "aciklama": "olimpos tanrılarının yaşlı titan nesline karşı 10 yıllık büyük iktidar savaşı", "yasakli_kelimeler": ["titan", "kronos", "zeus", "savaş", "tartaros"], "zorluk": "zor"},
    {"kelime": "gigantomahide dövüşmek", "aciklama": "tanrıların yeryüzünü tehdit eden devler ırkıyla kanlı savaşı", "yasakli_kelimeler": ["devler", "gaia", "savaş", "olimpos", "herkül"], "zorluk": "zor"},
    {"kelime": "ragnarokta yok olmak", "aciklama": "iskandinav mitolojisinde tanrıların ve dünyanın kıyamet savaşında çökmesi", "yasakli_kelimeler": ["odin", "thor", "kıyamet", "fenrir", "iskandinav"], "zorluk": "zor"},
    {"kelime": "teogoni anlatmak", "aciklama": "tanrıların soy ağacını ve evrenin kökenini şiirsel destanla aktarmak", "yasakli_kelimeler": ["hesiodos", "köken", "soy ağacı", "yaratılış", "destan"], "zorluk": "zor"},
    {"kelime": "psikopomp olmak", "aciklama": "hermes veya anubis gibi tanrıların ölü ruhlara öte dünyada rehberlik etmesi", "yasakli_kelimeler": ["hermes", "anubis", "rehber", "ruh", "öte dünya"], "zorluk": "zor"},
    {"kelime": "hubris sergilemek", "aciklama": "ölümlünün haddini aşıp tanrılara meydan okuyan kibirli cüretkarlığı", "yasakli_kelimeler": ["kibir", "cüret", "nemesis", "meydan okuma", "ceza"], "zorluk": "zor"},
    {"kelime": "nemesisin gazabına uğramak", "aciklama": "aşırı kibir ve adaletsizlik yapanların ilahi intikam tanrıçasıyla ezilmesi", "yasakli_kelimeler": ["intikam", "adalet", "ceza", "tanrıça", "kibir"], "zorluk": "zor"},
    {"kelime": "tartarosa zincirlenmek", "aciklama": "yenilen tanrı veya canavarların yeraltının en derin uçurumuna hapsedilmesi", "yasakli_kelimeler": ["uçurum", "hapis", "yeraltı", "titan", "derinlik"], "zorluk": "zor"},
    {"kelime": "ouroboros gibi dönmek", "aciklama": "kendi kuyruğunu ısıran yılan gibi sonsuz doğum ve yıkım döngüsünü simgelemek", "yasakli_kelimeler": ["yılan", "kuyruk", "sonsuz döngü", "ebediyet", "yenilenme"], "zorluk": "zor"},
    {"kelime": "valhallaya kabul edilmek", "aciklama": "savaşta onurla ölen viking savaşçılarının odin'in cennet sarayına girmesi", "yasakli_kelimeler": ["odin", "viking", "savaşçı", "valkür", "şerefli ölüm"], "zorluk": "zor"},
    {"kelime": "kalbi tüy ile tartılmak", "aciklama": "mısır inancında ölenin kalbinin maat'ın doğruluk tüyüyle terazide ölçülmesi", "yasakli_kelimeler": ["maat", "anubis", "terazi", "tüy", "mısır"], "zorluk": "zor"},
    {"kelime": "lethe suyundan içmek", "aciklama": "yeraltı dünyasındaki unutuş ırmağından içerek geçmiş yaşamı tamamen silmek", "yasakli_kelimeler": ["unutmak", "ırmak", "hafıza", "hades", "yeraltı"], "zorluk": "zor"},
    {"kelime": "yggdrasil dallarında gezinmek", "aciklama": "dokuz diyarı birbirine bağlayan devasa evren ağacında yolculuk etmek", "yasakli_kelimeler": ["dünya ağacı", "dokuz diyar", "iskandinav", "kök", "küllük"], "zorluk": "zor"}
]

if __name__ == "__main__":
    add_and_save_verbs("mimarlik", mimarlik_verbs)
    add_and_save_verbs("mitoloji", mitoloji_verbs)
