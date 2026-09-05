# -*- coding: utf-8 -*-
from card_utils import add_and_save_verbs

osinografi_verbs = [
    # Kolay (12)
    {"kelime": "dalgalanmak", "aciklama": "rüzgarın etkisiyle deniz yüzeyinde su tepecikleri oluşması", "yasakli_kelimeler": ["dalga", "deniz", "rüzgar", "su", "yüzey"], "zorluk": "kolay"},
    {"kelime": "akmak", "aciklama": "okyanus sularının belirli bir yönde nehir gibi ilerlemesi", "yasakli_kelimeler": ["akıntı", "su", "okyanus", "yön", "ilerlemek"], "zorluk": "kolay"},
    {"kelime": "dalmak", "aciklama": "araştırma gemisinden tüple veya denizaltıyla derin sulara inmek", "yasakli_kelimeler": ["derin", "su altı", "tüp", "denizaltı", "inmek"], "zorluk": "kolay"},
    {"kelime": "yüzmek", "aciklama": "deniz canlılarının veya insanların su içinde ilerlemesi", "yasakli_kelimeler": ["su", "canlı", "balık", "kulaç", "deniz"], "zorluk": "kolay"},
    {"kelime": "batmak", "aciklama": "ağır nesnelerin veya batık geminin deniz tabanına çökmesi", "yasakli_kelimeler": ["çökmek", "taban", "batık", "derinlik", "su altı"], "zorluk": "kolay"},
    {"kelime": "örnek almak", "aciklama": "deniz tabanından çamur veya farklı derinliklerden su numunesi çekmek", "yasakli_kelimeler": ["numune", "su", "çamur", "şişe", "laboratuvar"], "zorluk": "kolay"},
    {"kelime": "ölçmek", "aciklama": "cihazlarla denizin sıcaklığını, tuzluluğunu ve derinliğini belirlemek", "yasakli_kelimeler": ["sıcaklık", "tuzluluk", "derinlik", "cihaz", "metre"], "zorluk": "kolay"},
    {"kelime": "keşfetmek", "aciklama": "okyanusun keşfedilmemiş derin çukurlarını ve batıklarını bulmak", "yasakli_kelimeler": ["bulmak", "derin çukur", "çukur", "yeni", "batık"], "zorluk": "kolay"},
    {"kelime": "yükselmek", "aciklama": "gelgit etkisiyle deniz suyu seviyesinin kıyıya doğru tırmanması", "yasakli_kelimeler": ["gelgit", "seviye", "su", "kıyı", "tırmanmak"], "zorluk": "kolay"},
    {"kelime": "çekilmek", "aciklama": "cezir vaktinde deniz suyunun açığa doğru gerilemesi", "yasakli_kelimeler": ["cezir", "gelgit", "kıyı", "kumsal", "gerilemek"], "zorluk": "kolay"},
    {"kelime": "donmak", "aciklama": "kutup okyanuslarında suyun eksi derecede buzul katmanına dönüşmesi", "yasakli_kelimeler": ["buzul", "kutup", "soğuk", "buz", "sıfır altı"], "zorluk": "kolay"},
    {"kelime": "buharlaşmak", "aciklama": "tropik okyanus yüzeyindeki sıcak suyun atmosfere nem olarak yükselmesi", "yasakli_kelimeler": ["nem", "atmosfer", "güneş", "su buharı", "sıcak"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "sonarla taramak", "aciklama": "ses dalgaları göndererek deniz tabanının derinlik haritasını çıkarmak", "yasakli_kelimeler": ["sonar", "ses dalgası", "taban", "harita", "eko"], "zorluk": "orta"},
    {"kelime": "upwelling oluşturmak", "aciklama": "kıyı rüzgarlarıyla dipteki soğuk ve besin zengini suların yüzeye fışkırması", "yasakli_kelimeler": ["yükselim", "dip suyu", "besin tuzu", "soğuk", "plankton"], "zorluk": "orta"},
    {"kelime": "downwelling yaşamak", "aciklama": "yüzeydeki yoğun veya rüzgarla biriken suların derinlere doğru batması", "yasakli_kelimeler": ["çökme", "yüzey suyu", "yoğunluk", "derin", "akıntı"], "zorluk": "orta"},
    {"kelime": "tuzluluk ölçmek", "aciklama": "iletkenlik ölçer cihazla binde bir birim cinsinden tuz oranını saptamak", "yasakli_kelimeler": ["salinite", "binde", "iletkenlik", "tuz", "ctd"], "zorluk": "orta"},
    {"kelime": "ctd cihazı indirmek", "aciklama": "vinçle iletkenlik, sıcaklık ve derinlik ölçen sensör kafesini suya salmak", "yasakli_kelimeler": ["ctd", "sensör", "vinç", "rozet", "şişe"], "zorluk": "orta"},
    {"kelime": "plankton süzmek", "aciklama": "özel konik ipek kepçe ağıyla yüzeyden mikroskobik deniz canlısı toplamak", "yasakli_kelimeler": ["fitoplankton", "ipek kepçe", "mikroskobik", "ağ", "zooplankton"], "zorluk": "orta"},
    {"kelime": "mercanköşk resifi haritalamak", "aciklama": "sığ sulardaki canlı mercan kolonilerinin dağılımını uyduyla çizmek", "yasakli_kelimeler": ["mercan", "resif", "koloni", "sığ", "biyoçeşitlilik"], "zorluk": "orta"},
    {"kelime": "dip çamuru karotu almak", "aciklama": "ağır metal boruyu tabana saplayıp katmanlı tortu sütunu çıkarmak", "yasakli_kelimeler": ["karot", "tortu", "sütun", "sediman", "katman"], "zorluk": "orta"},
    {"kelime": "tsunami izlemek", "aciklama": "deniz dibi deprem sensörleriyle dev dalgaların kıyıya hızını hesaplamak", "yasakli_kelimeler": ["deprem", "dev dalga", "kıyı", "erken uyarı", "şamandıra"], "zorluk": "orta"},
    {"kelime": "hidrotermal baca aramak", "aciklama": "okyanus sırtlarında 400 derece mineral püskürten siyah bacaları bulmak", "yasakli_kelimeler": ["kara duman", "baca", "okyanus sırtı", "mineral", "kemosentez"], "zorluk": "orta"},
    {"kelime": "akıntı hızını ölçmek", "aciklama": "akustik doppler akım profilleyici ile farklı su katmanlarının hızını bulmak", "yasakli_kelimeler": ["adcp", "akıntı hızı", "doppler", "knot", "katman"], "zorluk": "orta"},
    {"kelime": "girdap oluşturmak", "aciklama": "ana akıntıdan kopan devasa dairesel su halkalarının enerjiyi taşıması", "yasakli_kelimeler": ["eddy", "dairesel", "girdap", "halka", "enerji"], "zorluk": "orta"},
    {"kelime": "oksijen minimum zonu", "aciklama": "ara derinliklerde organik madde çürümesiyle çözünmüş oksijenin dibe vurması", "yasakli_kelimeler": ["çözünmüş oksijen", "çürüme", "hipoksi", "ölü bölge", "tüketim"], "zorluk": "orta"},
    {"kelime": "derin denizaltı indirmek", "aciklama": "alvin gibi basınca dayanıklı titanyum küreli araçla 6000 metreye inmek", "yasakli_kelimeler": ["alvin", "titanyum küre", "basınç", "insanlı", "derin su"], "zorluk": "orta"},
    {"kelime": "batimetrik harita çizmek", "aciklama": "çok ışınlı iskandil verileriyle okyanus tabanı topoğrafyasını renklendirmek", "yasakli_kelimeler": ["derinlik çizgisi", "topoğrafya", "izobat", "çok ışınlı", "taban"], "zorluk": "orta"},
    {"kelime": "tuz kaması oluşturmak", "aciklama": "nehir ağzında yoğun tuzlu deniz suyunun tatlı suyun altına kama gibi girmesi", "yasakli_kelimeler": ["estuar", "tatlı su", "nehir ağzı", "yoğunluk", "tabakalaşma"], "zorluk": "orta"},
    {"kelime": "şamandıra fırlatmak", "aciklama": "otonom argo şamandıralarını serbest bırakıp 2000 metreye dalıp çıkmasını sağlamak", "yasakli_kelimeler": ["argo şamandırası", "otonom", "profil", "uydu aktarımı", "deniz yüzeyi"], "zorluk": "orta"},
    {"kelime": "biyolüminesans saçmak", "aciklama": "derin deniz balıklarının lusiferin enzimiyle karanlıkta ışık yayması", "yasakli_kelimeler": ["ışık yayma", "lusiferin", "derin deniz", "parlama", "enzim"], "zorluk": "orta"},
    {"kelime": "sediman çökelmek", "aciklama": "nehirlerle gelen kum ve kilin kıta sahanlığında yavaşça tabana oturması", "yasakli_kelimeler": ["tortul", "çökelme", "kıta sahanlığı", "kum", "kil"], "zorluk": "orta"},
    {"kelime": "kıta sahanlığını geçmek", "aciklama": "sığ kıyı şeridinden dik kıta yamacına ve abisal düzlüğe geçiş yapmak", "yasakli_kelimeler": ["kıta yamacı", "sığlık", "abisal", "eğim", "açık deniz"], "zorluk": "orta"},
    {"kelime": "termoklini tespit etmek", "aciklama": "sıcaklığın derinlikle çok hızlı düştüğü ara su tabakasını belirlemek", "yasakli_kelimeler": ["termoklin", "ani düşüş", "sıcaklık katmanı", "soğuk su", "bariyer"], "zorluk": "orta"},
    {"kelime": "haloklini kaydetmek", "aciklama": "tuzluluğun dikey profilde aniden keskin şekilde değiştiği derinliği bulmak", "yasakli_kelimeler": ["tuzluluk sıçraması", "haloklin", "dikey profil", "katman", "değişim"], "zorluk": "orta"},
    {"kelime": "piknoklini aşmak", "aciklama": "su yoğunluğunun hızla arttığı katmanı geçip derin dip sularına ulaşmak", "yasakli_kelimeler": ["yoğunluk katmanı", "piknoklin", "geçiş", "tabakalaşma", "ağır su"], "zorluk": "orta"},
    {"kelime": "deniz buzulu kırıcıyla ilerlemek", "aciklama": "kutup araştırma gemisinin kalın buz kütlelerini yararak rota açması", "yasakli_kelimeler": ["buzkıran", "kutup", "rota", "yarmak", "gemisi"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "termohalin sirkülasyonu sürmek", "aciklama": "sıcaklık ve tuzluluk farklarıyla tüm dünyayı 1000 yılda dolaşan küresel taşıyıcı bant", "yasakli_kelimeler": ["küresel taşıyıcı bant", "yoğunluk farkı", "kuzey atlantik dip suyu", "dolaşım", "derin akıntı"], "zorluk": "zor"},
    {"kelime": "ekman spirali çizmek", "aciklama": "coriolis etkisiyle rüzgarın sürüklediği suyun derinleştikçe spiral şeklinde sapması", "yasakli_kelimeler": ["coriolis", "ekman taşınımı", "spiral", "sapma açısı", "rüzgar sürüklemesi"], "zorluk": "zor"},
    {"kelime": "kalsit kompanzasyon derinliği", "aciklama": "kalsiyum karbonat kabuklarının çözünme hızının çökelme hızına eşitlendiği derinlik", "yasakli_kelimeler": ["ccd", "kalsiyum karbonat", "çözünme", "foraminifera", "asitlik"], "zorluk": "zor"},
    {"kelime": "abisal düzlüğe yerleşmek", "aciklama": "okyanusun 4000-6000 metre derinliğindeki uçsuz bucaksız düz tabanında çalışmak", "yasakli_kelimeler": ["abisal ova", "4000 metre", "derin taban", "pelajik çökelti", "karanlık"], "zorluk": "zor"},
    {"kelime": "hadal zonu araştırmak", "aciklama": "6000 metreden daha derin okyanus çukurlarının aşırı basınçlı dünyasını incelemek", "yasakli_kelimeler": ["mariana çukuru", "hendek", "hadal", "aşırı basınç", "derinlik"], "zorluk": "zor"},
    {"kelime": "turbidite akıntısı tetiklemek", "aciklama": "kıta yamacından aşağı saatte yüz kilometre hızla akan yoğun çamur ve kum çığı", "yasakli_kelimeler": ["sualtı çığı", "çamur akıntısı", "kanyon", "kıta yamacı", "yoğunluk"], "zorluk": "zor"},
    {"kelime": "brunt-vaisala frekansı", "aciklama": "kararlı tabakalaşmış su kolonunda yer değiştiren parselin dikey salınım frekansı", "yasakli_kelimeler": ["kararlılık", "salınım", "tabakalaşma", "yoğunluk gradyanı", "frekans"], "zorluk": "zor"},
    {"kelime": "paleo-osinografi çalışmak", "aciklama": "dip tortularındaki mikrofosillerin izotop oranlarından antik okyanus iklimini çözmek", "yasakli_kelimeler": ["mikrofosil", "oksijen izotopu", "antik okyanus", "jeolojik geçmiş", "sediman"], "zorluk": "zor"},
    {"kelime": "rossby dalgası yaymak", "aciklama": "dünyanın dönüşü ve enlemle değişen coriolis etkisiyle okyanusta batıya yürüyen devasa dalgalar", "yasakli_kelimeler": ["rossby", "gezegensel dalga", "enlem", "batıya göç", "akıntı salınımı"], "zorluk": "zor"},
    {"kelime": "kelvin dalgası ilerlemek", "aciklama": "ekvator boyunca veya kıyıya paralel hapsolarak doğuya doğru ilerleyen okyanus dalgası", "yasakli_kelimeler": ["el nino", "ekvatoral", "kıyı dalgası", "hapsolma", "doğuya ilerleme"], "zorluk": "zor"},
    {"kelime": "metan hidrat çıkarmak", "aciklama": "derin deniz tabanındaki yüksek basınç ve soğukta donmuş yanıcı buz kristallerini incelemek", "yasakli_kelimeler": ["yanıcı buz", "metan gazı", "kristal kafes", "deniz tabanı", "enerji kaynağı"], "zorluk": "zor"},
    {"kelime": "okyanus asitlenmesini ölçmek", "aciklama": "artış gösteren atmosferik co2 emilimiyle okyanus ph seviyesinin düşüşünü saptamak", "yasakli_kelimeler": ["ph düşüşü", "co2 emilimi", "karbonik asit", "kabuk erimesi", "mercan beyazlaması"], "zorluk": "zor"},
    {"kelime": "kemosentez adaptasyonu", "aciklama": "güneş görmeyen hidrotermal yarık canlılarının kükürt bakterileriyle besin üretmesi", "yasakli_kelimeler": ["kükürt", "tüp solucanı", "güneşsiz", "baca", "simbiyotik bakteri"], "zorluk": "zor"},
    {"kelime": "jeostrofik akıntı hesaplamak", "aciklama": "deniz yüzeyi eğiminden doğan basınç gradyanı ile coriolis kuvvetini dengelemek", "yasakli_kelimeler": ["basınç gradyanı", "coriolis dengesi", "dinamik yükseklik", "akıntı hesabı", "izobar"], "zorluk": "zor"}
]

osmanli_verbs = [
    # Kolay (12)
    {"kelime": "fethetmek", "aciklama": "osmanlı ordusuyla bir kaleyi veya şehri kuşatıp sınırlarına katmak", "yasakli_kelimeler": ["kale", "şehir", "ordu", "kuşatma", "sınır"], "zorluk": "kolay"},
    {"kelime": "hükmetmek", "aciklama": "padişahın imparatorluk toprakları ve tebaası üzerinde otorite kurması", "yasakli_kelimeler": ["padişah", "imparatorluk", "otorite", "yönetmek", "saray"], "zorluk": "kolay"},
    {"kelime": "sefer düzenlemek", "aciklama": "batıya veya doğuya doğru yüz binlerce askerle savaşa çıkmak", "yasakli_kelimeler": ["savaş", "ordu", "batı", "doğu", "asker"], "zorluk": "kolay"},
    {"kelime": "saray yaptırmak", "aciklama": "topkapı veya dolmabahçe gibi anıtsal padişah sarayları inşa ettirmek", "yasakli_kelimeler": ["topkapı", "dolmabahçe", "inşa", "padişah", "külliye"], "zorluk": "kolay"},
    {"kelime": "vergi toplamak", "aciklama": "köylü ve tüccardan haraç, cizye ve aşar vergisi tahsil etmek", "yasakli_kelimeler": ["cizye", "aşar", "haraç", "köylü", "hazine"], "zorluk": "kolay"},
    {"kelime": "ferman çıkarmak", "aciklama": "padişahın tuğralı yazılı emirlerini vilayetlere göndermek", "yasakli_kelimeler": ["emir", "tuğra", "yazılı", "vilayet", "buyruk"], "zorluk": "kolay"},
    {"kelime": "kuşatmak", "aciklama": "düşman kalesinin etrafını asker ve toplarla sarıp teslim olmaya zorlamak", "yasakli_kelimeler": ["muhasara", "kale", "top", "sarmak", "asker"], "zorluk": "kolay"},
    {"kelime": "isyan etmek", "aciklama": "yeniçerilerin veya celalilerin devlete karşı ayaklanması", "yasakli_kelimeler": ["ayaklanma", "yeniçeri", "celali", "başkaldırı", "kazan"], "zorluk": "kolay"},
    {"kelime": "vakfetmek", "aciklama": "hanedan veya paşaların mal varlığını cami, medrese ve aşevi için bağışlaması", "yasakli_kelimeler": ["vakıf", "bağış", "cami", "medrese", "aşevi"], "zorluk": "kolay"},
    {"kelime": "tahta geçmek", "aciklama": "şehzadenin cülus töreniyle osmangazi tahtına oturması", "yasakli_kelimeler": ["cülus", "şehzade", "padişah", "taht", "tören"], "zorluk": "kolay"},
    {"kelime": "barış yapmak", "aciklama": "savaş sonunda düşman devletle ahidname imzalayıp sınırları çizmek", "yasakli_kelimeler": ["ahidname", "anlaşma", "savaş sonu", "sınır", "imza"], "zorluk": "kolay"},
    {"kelime": "sadrazam atamak", "aciklama": "padişahın mühr-i hümayunu en güvendiği vezire teslim etmesi", "yasakli_kelimeler": ["mühür", "başvezir", "veziriazam", "görev", "atamak"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "devşirme yapmak", "aciklama": "balkan köylerinden hristiyan çocukları toplayıp acemi ocağına almak", "yasakli_kelimeler": ["acemi ocağı", "hristiyan çocuk", "balkanlar", "yeniçeri", "toplama"], "zorluk": "orta"},
    {"kelime": "tımar dağıtmak", "aciklama": "sipahilere vergi toplama hakkı vererek atlı asker besletmek", "yasakli_kelimeler": ["dirlik", "sipahi", "cebelü", "toprak sistemi", "atlı asker"], "zorluk": "orta"},
    {"kelime": "divan-ı hümayunu toplamak", "aciklama": "topkapı sarayı kubbealtında sadrazam ve vezirlerin toplanıp hüküm vermesi", "yasakli_kelimeler": ["kubbealtı", "sadrazam", "toplantı", "hüküm", "topkapı"], "zorluk": "orta"},
    {"kelime": "kazan kaldırmak", "aciklama": "yeniçerilerin et meydanında isyan başlatarak kazanlarını ters çevirmesi", "yasakli_kelimeler": ["yeniçeri", "et meydanı", "isyan", "kazan", "başkaldırı"], "zorluk": "orta"},
    {"kelime": "kılıç kuşanmak", "aciklama": "eyüp sultan türbesinde yeni padişahın beline osman gazi'nin kılıcını takması", "yasakli_kelimeler": ["eyüp sultan", "türbe", "osman gazi", "merasim", "kılıç alayı"], "zorluk": "orta"},
    {"kelime": "fetva almak", "aciklama": "padişah veya sadrazamın savaşa çıkmadan şeyhülislamdan onay istemesi", "yasakli_kelimeler": ["şeyhülislam", "şeriat", "onay", "dini izin", "savaş izni"], "zorluk": "orta"},
    {"kelime": "sancağa çıkmak", "aciklama": "şehzadenin devlet tecrübesi kazanmak için manisa veya amasya valiliğine gitmesi", "yasakli_kelimeler": ["şehzade", "lala", "manisa", "amasya", "vali"], "zorluk": "orta"},
    {"kelime": "iltizam vermek", "aciklama": "devlet gelirlerinin ihale usulüyle mültezimlere peşin para karşılığı satılması", "yasakli_kelimeler": ["mültezim", "ihale", "peşin", "vergi toplama", "gelir"], "zorluk": "orta"},
    {"kelime": "tuğra çekmek", "aciklama": "nişancının devlet belgelerinin en üstüne padişahın özel imzasını çizmesi", "yasakli_kelimeler": ["nişancı", "imza", "ferman", "hat", "mühür"], "zorluk": "orta"},
    {"kelime": "ulufe dağıtmak", "aciklama": "üç ayda bir saray avlusunda yeniçerilere maaş keselerini teslim etmek", "yasakli_kelimeler": ["maaş", "üç ayda bir", "yeniçeri", "kese", "saray avlusu"], "zorluk": "orta"},
    {"kelime": "akçe bastırmak", "aciklama": "darphanede padişahın adı ve basım yılı yazılı gümüş sikke dökmek", "yasakli_kelimeler": ["gümüş para", "darphane", "sikke", "tedavül", "para"], "zorluk": "orta"},
    {"kelime": "kadı tayin etmek", "aciklama": "kazaya şeriat ve örf hukukunu uygulayacak adli hakim görevlendirmek", "yasakli_kelimeler": ["hakim", "kaza", "mahkeme", "şeriat", "hüküm"], "zorluk": "orta"},
    {"kelime": "kapitülasyon tanımak", "aciklama": "fransa veya ingiltere gibi yabancı tüccarlara gümrük ve ticaret imtiyazı vermek", "yasakli_kelimeler": ["imtiyaz", "ayrıcalık", "ticaret", "gümrük", "yabancı"], "zorluk": "orta"},
    {"kelime": "gaza yapmak", "aciklama": "islam dinini yaymak ve sınırları genişletmek amacıyla gayrimüslimlere karşı savaşmak", "yasakli_kelimeler": ["cihat", "akıncı", "din", "kutsal savaş", "sınır boyu"], "zorluk": "orta"},
    {"kelime": "istimalet uygulamak", "aciklama": "fethedilen yerlerin ahalisine adil davranıp gönüllerini fethetmek", "yasakli_kelimeler": ["hoşgörü", "gönül alma", "balkanlar", "adalet", "ısındırma"], "zorluk": "orta"},
    {"kelime": "iskan ettirmek", "aciklama": "anadolu'daki türkmen aşiretlerini balkanlardaki boş topraklara yerleştirmek", "yasakli_kelimeler": ["türkmen", "yerleştirme", "balkanlar", "göç", "nüfus"], "zorluk": "orta"},
    {"kelime": "kadırga kürek çekmek", "aciklama": "osmanlı donanmasında forsa olarak akdeniz'de küreklere asılmak", "yasakli_kelimeler": ["forsa", "donanma", "akdeniz", "kürek", "deniz savaşı"], "zorluk": "orta"},
    {"kelime": "kaptan-ı derya olmak", "aciklama": "tersane-i amire ve tüm osmanlı donanmasının başkomutanlığına yükselmek", "yasakli_kelimeler": ["donanma", "deniz kuvvetleri", "barbaros", "tersane", "amiral"], "zorluk": "orta"},
    {"kelime": "enderuna öğrenci seçmek", "aciklama": "üstün zekalı devşirme gençleri saray okuluna alıp vezir ve bürokrat yetiştirmek", "yasakli_kelimeler": ["saray okulu", "iç oğlanı", "eğitim", "bürokrat", "topkapı"], "zorluk": "orta"},
    {"kelime": "cizye vergisi almak", "aciklama": "askerlik yapmayan gayrimüslim erkeklerden can güvenliği karşılığı baş vergisi kesmek", "yasakli_kelimeler": ["gayrimüslim", "baş vergisi", "askerlik muafiyeti", "hazine", "vergi"], "zorluk": "orta"},
    {"kelime": "sürre alayı uğurlamak", "aciklama": "her hac mevsiminde mekke ve medine fukarasına istanbul'dan hediye kervanı yollamak", "yasakli_kelimeler": ["mekke medine", "hac", "kervan", "hediye", "saray"], "zorluk": "orta"},
    {"kelime": "millet sistemi kurmak", "aciklama": "tebaayı ırklarına göre değil dini inançlarına göre cemaatler halinde yönetmek", "yasakli_kelimeler": ["din", "cemaat", "ortodoks", "yahudi", "yönetim"], "zorluk": "orta"},
    {"kelime": "kelle istemek", "aciklama": "isyan eden yeniçerilerin saraydan görevli paşanın idamını talep etmesi", "yasakli_kelimeler": ["idam", "isyan", "paşa", "yeniçeri", "saray kapısı"], "zorluk": "orta"},
    {"kelime": "boğdurulmak", "aciklama": "kan dökmek yasak olduğu için hanedan üyesi şehzadenin ipek kementle canına kıyılması", "yasakli_kelimeler": ["ipek kement", "dilsiz cellat", "şehzade", "kan akıtmama", "idam"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "kanunname-i ali osman", "aciklama": "fatih sultan mehmed'in devlet teşkilatı ve kardeş katlini yasal kurallara bağlaması", "yasakli_kelimeler": ["fatih", "kardeş katli", "devlet düzeni", "yasa", "örfi hukuk"], "zorluk": "zor"},
    {"kelime": "nizam-ı alem gütmek", "aciklama": "dünya düzeninin ve osmanlı merkezi otoritesinin bozulmaması için her tedbiri almak", "yasakli_kelimeler": ["dünya düzeni", "merkezi otorite", "devlet bekası", "felsefe", "padişah"], "zorluk": "zor"},
    {"kelime": "vaka-i hayriyeyi gerçekleştirmek", "aciklama": "ii. mahmud'un top ateşiyle yeniçeri ocaklarını dağıtıp kanlı şekilde kaldırması", "yasakli_kelimeler": ["ii. mahmud", "1826", "yeniçeri ocağının kalkması", "top atışı", "asakir-i mansure"], "zorluk": "zor"},
    {"kelime": "malikane sistemine bağlamak", "aciklama": "iltizam arazilerini mültezimlere kaydıhayat şartıyla ömür boyu kiralamak", "yasakli_kelimeler": ["kaydıhayat", "ömür boyu", "mültezim", "vergi kiralama", "18. yüzyıl"], "zorluk": "zor"},
    {"kelime": "sened-i ittifak imzalamak", "aciklama": "padişah ii. mahmud ile anadolu ve rumeli ayanları arasında yetki paylaşımı anlaşması", "yasakli_kelimeler": ["ayanlar", "1808", "ii. mahmud", "alemdarmustafa", "sözleşme"], "zorluk": "zor"},
    {"kelime": "tanzimat fermanı okumak", "aciklama": "gülhane parkı'nda reşid paşa'nın can, mal ve namus güvencesi getiren fermanı okuması", "yasakli_kelimeler": ["gülhane", "mustafa reşid", "1839", "hukuk devleti", "abdülmecid"], "zorluk": "zor"},
    {"kelime": "kanun-i esasiyi yürürlüğe koymak", "aciklama": "1876 yılında türk tarihinin ilk anayasasını ilan edip meclis-i mebusanı açmak", "yasakli_kelimeler": ["ilk anayasa", "1876", "meclis-i mebusan", "mithat paşa", "ii. abdülhamid"], "zorluk": "zor"},
    {"kelime": "düyun-u umumiyeye bağlanmak", "aciklama": "dış borçların ödenememesi sonucu yabancı alacaklıların devlet gelirlerine el koyması", "yasakli_kelimeler": ["dış borç", "alacaklılar", "muharrem kararnamesi", "el koyma", "1881"], "zorluk": "zor"},
    {"kelime": "tahrir defterine kaydetmek", "aciklama": "fethedilen sancağın köy köy nüfus, toprak ve vergi kaynaklarını ayrıntılı yazmak", "yasakli_kelimeler": ["mufassal", "tahrir", "sayım", "nüfus kaydı", "vergi defteri"], "zorluk": "zor"},
    {"kelime": "pençik kanununu uygulamak", "aciklama": "savaşta esir alınan kafir esirlerin beşte birini ordu adına devlete devretmek", "yasakli_kelimeler": ["beşte bir", "esir", "i. murad", "yeniçeri kökeni", "hisse"], "zorluk": "zor"},
    {"kelime": "berat-ı hümayun vermek", "aciklama": "padişahın tayin, muafiyet veya unvan bahşettiğini bildiren resmi tuğralı belge", "yasakli_kelimeler": ["tayin belgesi", "tuğralı", "imtiyaz", "ferman türü", "atama"], "zorluk": "zor"},
    {"kelime": "müsadere kanununu işletmek", "aciklama": "görevden alınan veya vefat eden veziriazamın tüm şahsi servetine sarayca el konulması", "yasakli_kelimeler": ["el koyma", "hazine-i amire", "haksız kazanç", "sadrazam serveti", "mülkiyet engeli"], "zorluk": "zor"},
    {"kelime": "bab-ı ali baskını yapmak", "aciklama": "enver ve talat paşaların hükümet binasını basıp sadrazamı silah zoruyla istifa ettirmesi", "yasakli_kelimeler": ["enver paşa", "ittihat ve terakki", "hükümet darbesi", "1913", "kamil paşa"], "zorluk": "zor"},
    {"kelime": "muhallefat kaydı tutmak", "aciklama": "ölen kişinin geride bıraktığı mirası kadı marifetiyle tereke defterine geçirmek", "yasakli_kelimeler": ["tereke", "miras", "tereke defteri", "kadı", "kalan eşya"], "zorluk": "zor"}
]

if __name__ == "__main__":
    add_and_save_verbs("osinografi", osinografi_verbs)
    add_and_save_verbs("osmanli", osmanli_verbs)
