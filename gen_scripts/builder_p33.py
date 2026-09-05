# -*- coding: utf-8 -*-
from card_utils import add_and_save_verbs

optik_verbs = [
    # Kolay (12)
    {"kelime": "yansıtmak", "aciklama": "ışık ışınının ayna gibi pürüzsüz yüzeye çarpıp geri dönmesi", "yasakli_kelimeler": ["ayna", "ışık", "çarpmak", "dönmek", "yüzey"], "zorluk": "kolay"},
    {"kelime": "kırmak", "aciklama": "ışığın bir saydam ortamdan diğerine geçerken yön değiştirmesi", "yasakli_kelimeler": ["saydam", "ortam", "ışık", "açı", "yön"], "zorluk": "kolay"},
    {"kelime": "odaklamak", "aciklama": "mercek yardımıyla ışık ışınlarını tek bir noktada toplamak", "yasakli_kelimeler": ["mercek", "odak noktası", "toplamak", "ışın", "nokta"], "zorluk": "kolay"},
    {"kelime": "büyütmek", "aciklama": "büyüteç veya mikroskopla küçük nesnelerin görüntüsünü iri göstermek", "yasakli_kelimeler": ["büyüteç", "mikroskop", "görüntü", "iri", "mercek"], "zorluk": "kolay"},
    {"kelime": "küçültmek", "aciklama": "kalın kenarlı mercekle cismin görüntüsünü daha ufak hale getirmek", "yasakli_kelimeler": ["ufak", "mercek", "görüntü", "boyut", "kalın kenarlı"], "zorluk": "kolay"},
    {"kelime": "aydınlatmak", "aciklama": "karanlık odaya veya cisme ışık kaynağı yönlendirip görünür kılmak", "yasakli_kelimeler": ["ışık", "fener", "lamba", "karanlık", "görünür"], "zorluk": "kolay"},
    {"kelime": "gözlük takmak", "aciklama": "görme kusurunu düzeltmek için burun üstüne camlı çerçeve koymak", "yasakli_kelimeler": ["çerçeve", "cam", "numara", "göz", "kusur"], "zorluk": "kolay"},
    {"kelime": "gözlemlemek", "aciklama": "teleskopla gece gökyüzündeki yıldızları ve gezegenleri izlemek", "yasakli_kelimeler": ["teleskop", "yıldız", "gökyüzü", "izlemek", "bakmak"], "zorluk": "kolay"},
    {"kelime": "parlamak", "aciklama": "yüzeyin üzerine düşen ışıkla ışıltılı ve parlak görünmesi", "yasakli_kelimeler": ["ışıltı", "parlak", "parıltı", "yüzey", "ışık"], "zorluk": "kolay"},
    {"kelime": "gölge düşürmek", "aciklama": "opak cismin ışığın önüne geçerek arkasında karanlık alan yaratması", "yasakli_kelimeler": ["opak", "karanlık", "ışık engeli", "siluet", "arka"], "zorluk": "kolay"},
    {"kelime": "renklere ayırmak", "aciklama": "cam prizmadan geçen beyaz ışığı gökkuşağı tayfına bölmek", "yasakli_kelimeler": ["prizma", "tayf", "gökkuşağı", "kırmızı mor", "beyaz ışık"], "zorluk": "kolay"},
    {"kelime": "filtrelemek", "aciklama": "renkli cam filtre ile belirli dalga boyundaki ışıkları süzmek", "yasakli_kelimeler": ["süzmek", "polarize", "cam", "filtre", "dalga"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "tam yansıma yapmak", "aciklama": "ışığın sınır açısından büyük açıyla gelip tamamen aynı ortama dönmesi", "yasakli_kelimeler": ["sınır açısı", "fiber optik", "kırılma", "ortam", "açı"], "zorluk": "orta"},
    {"kelime": "polarize etmek", "aciklama": "farklı yönlerde titreşen ışık dalgalarını tek bir düzlemde titreştirmek", "yasakli_kelimeler": ["polarizasyon", "düzlem", "titreşim", "güneş gözlüğü", "filtre"], "zorluk": "orta"},
    {"kelime": "kırınım oluşturmak", "aciklama": "ışık dalgasının dar bir yarıktan geçerken bükülüp dairesel yayılması", "yasakli_kelimeler": ["yarık", "bükülme", "difraksiyon", "dalga", "engel"], "zorluk": "orta"},
    {"kelime": "girişim deseni kurmak", "aciklama": "iki koherent ışık dalgasının üst üste binerek aydınlık ve karanlık saçaklar yapması", "yasakli_kelimeler": ["aydınlık karanlık", "saçak", "çift yarık", "young", "dalga"], "zorluk": "orta"},
    {"kelime": "lazer üretmek", "aciklama": "uyarılmış ışıma ile aynı fazlı ve tek renkli yoğun ışık demeti çıkarmak", "yasakli_kelimeler": ["lazer", "aynı faz", "monokromatik", "ışıma", "yoğun"], "zorluk": "orta"},
    {"kelime": "diyoptri hesaplamak", "aciklama": "merceğin odak uzaklığının tersini alarak kırma gücünü bulmak", "yasakli_kelimeler": ["odak uzaklığı", "kırma gücü", "numara", "metre", "mercek"], "zorluk": "orta"},
    {"kelime": "mercek temizlemek", "aciklama": "mikroskop veya kamera camını mikro fiber bez ve solüsyonla silmek", "yasakli_kelimeler": ["mikrofiber", "solüsyon", "toz", "kamera", "çizik"], "zorluk": "orta"},
    {"kelime": "kontakt lens takmak", "aciklama": "kornea yüzeyine doğrudan ince şeffaf polimer mercek yerleştirmek", "yasakli_kelimeler": ["kornea", "lens", "solüsyon", "göz", "şeffaf"], "zorluk": "orta"},
    {"kelime": "ışık soğurmak", "aciklama": "koyu renkli maddenin üzerine düşen foton enerjisini emip ısıya çevirmesi", "yasakli_kelimeler": ["absorbsiyon", "emilim", "foton", "siyah", "enerji"], "zorluk": "orta"},
    {"kelime": "dispersiyon yaşamak", "aciklama": "farklı frekanstaki renklerin cam içinde farklı hızlarla kırılarak dağılması", "yasakli_kelimeler": ["dağılma", "frekans", "hız farkı", "prizma", "kırılma indisi"], "zorluk": "orta"},
    {"kelime": "netlik ayarı yapmak", "aciklama": "objektifin odak bileziğini çevirerek görüntüyü keskinleştirmek", "yasakli_kelimeler": ["fokus", "keskinlik", "bilezik", "objektif", "bulanıklık"], "zorluk": "orta"},
    {"kelime": "paralaks hatası yapmak", "aciklama": "gözün bakış açısı değiştiğinde nesnenin konumunun kaymış görünmesi", "yasakli_kelimeler": ["bakış açısı", "konum kayması", "ölçüm", "hata", "açı"], "zorluk": "orta"},
    {"kelime": "diyafram kısmak", "aciklama": "objektif içindeki metal yaprakları daraltıp içeri giren ışığı azaltmak", "yasakli_kelimeler": ["f değeri", "alan derinliği", "ışık miktarı", "yaprak", "apertür"], "zorluk": "orta"},
    {"kelime": "sanal görüntü oluşturmak", "aciklama": "ışınların uzantılarının kesişmesiyle düz aynanın arkasında görüntü doğması", "yasakli_kelimeler": ["düz ayna", "uzantı", "zahiri", "ayna arkası", "kesişim"], "zorluk": "orta"},
    {"kelime": "gerçek görüntü düşürmek", "aciklama": "ışınların bizzat kendilerinin kesişip perde üzerinde ters görüntü yapması", "yasakli_kelimeler": ["perde", "ters", "ışın kesişimi", "çukur ayna", "odak"], "zorluk": "orta"},
    {"kelime": "fiberle veri iletmek", "aciklama": "cam kablo içindeki tam yansımalarla ışık hızında dijital sinyal taşımak", "yasakli_kelimeler": ["fiber optik", "cam kablo", "sinyal", "internet", "ışık hızı"], "zorluk": "orta"},
    {"kelime": "küresel aberasyon oluşmak", "aciklama": "mercek kenarından geçen ışınların merkezden geçenlerle aynı noktada odaklanamaması", "yasakli_kelimeler": ["aberasyon", "kusur", "kenar", "odak sapması", "bulanıklık"], "zorluk": "orta"},
    {"kelime": "renk sapması yaşamak", "aciklama": "merceğin farklı renkleri farklı noktalarda odaklayıp kenarlarda gökkuşağı yapması", "yasakli_kelimeler": ["kromatik", "gökkuşağı kenar", "odak farkı", "mercek", "mor saçak"], "zorluk": "orta"},
    {"kelime": "spektrometre ile ölçmek", "aciklama": "ışık kaynağının hangi dalga boylarında ne kadar enerji yaydığını grafiğe dökmek", "yasakli_kelimeler": ["dalga boyu", "spektrum", "nanometre", "cihaz", "grafik"], "zorluk": "orta"},
    {"kelime": "hologram basmak", "aciklama": "lazer ışınlarının girişimiyle 3 boyutlu derinlikli optik görüntü kaydetmek", "yasakli_kelimeler": ["3 boyut", "derinlik", "lazer", "girişim", "kayıt"], "zorluk": "orta"},
    {"kelime": "kollimatörden geçirmek", "aciklama": "dağınık çıkan ışık ışınlarını birbirine paralel düzgün demete dönüştürmek", "yasakli_kelimeler": ["paralel demet", "dağınık", "yarık", "düzleştirme", "ışın"], "zorluk": "orta"},
    {"kelime": "antirefle kaplamak", "aciklama": "gözlük camına ince dielektrik tabaka sürerek parlamayı ve yansımayı sıfırlamak", "yasakli_kelimeler": ["yansıma önleyici", "kaplama", "cam", "yeşil parlama", "parlama"], "zorluk": "orta"},
    {"kelime": "astigmat düzeltmek", "aciklama": "silindirik mercek kullanarak korneadaki eğrilik farkını dengelemek", "yasakli_kelimeler": ["silindirik", "kornea eğriliği", "aks", "görme kusuru", "torik"], "zorluk": "orta"},
    {"kelime": "lümen ölçmek", "aciklama": "fotometre cihazıyla bir ampulün yaydığı toplam görünür ışık akısını hesaplamak", "yasakli_kelimeler": ["ışık akısı", "lüks", "fotometre", "ampul", "kandela"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "snell yasasını uygulamak", "aciklama": "kırılma indisleri ve gelme açılarının sinüsleri arasındaki bağıntıyı çözmek", "yasakli_kelimeler": ["sinüs", "kırılma indisi", "n1 n2", "gelme açısı", "formül"], "zorluk": "zor"},
    {"kelime": "brewster açısını bulmak", "aciklama": "yansıyan ışığın tamamen çizgisel polarize olduğu özel gelme açısını hesaplamak", "yasakli_kelimeler": ["kutup açısı", "tam polarizasyon", "tanjant", "yansıma", "kırılma"], "zorluk": "zor"},
    {"kelime": "çift kırılma göstermek", "aciklama": "kalsit kristalinin içine giren ışığı iki farklı kırılma indisiyle iki ayrı ışına bölmesi", "yasakli_kelimeler": ["birefringence", "kalsit", "olağan ışın", "kristal", "anizotropik"], "zorluk": "zor"},
    {"kelime": "fresnel katsayısı çıkarmak", "aciklama": "dielektrik arayüzeyde s ve p polarizasyonlu ışığın yansıma ve iletim oranlarını bulmak", "yasakli_kelimeler": ["s polarizasyon", "p polarizasyon", "arayüz", "yansıma katsayısı", "denklem"], "zorluk": "zor"},
    {"kelime": "fourier optiği işlemek", "aciklama": "merceklerin odak düzleminde optik görüntünün iki boyutlu uzamsal frekans fourier dönüşümü", "yasakli_kelimeler": ["uzamsal frekans", "fourier dönüşümü", "odak düzlemi", "optik filtreleme", "kırınım"], "zorluk": "zor"},
    {"kelime": "sayısal açıklık hesaplamak", "aciklama": "mikroskop objektifinin ortam kırma indisi ve ışık toplama yarı açısının sinüsünü çarpmak", "yasakli_kelimeler": ["numerical aperture", "na", "çözünürlük", "sinüs alfa", "objektif"], "zorluk": "zor"},
    {"kelime": "abbé sınırını aşmak", "aciklama": "süper çözünürlüklü flüoresan mikroskopisiyle kırınım sınırının altına inmek", "yasakli_kelimeler": ["kırınım sınırı", "sted", "süper çözünürlük", "flüoresan", "dalga boyu yarısı"], "zorluk": "zor"},
    {"kelime": "metamateryalle bükmek", "aciklama": "negatif kırılma indisine sahip yapay yapılarla ışığı cismin etrafından dolaştırmak", "yasakli_kelimeler": ["negatif indis", "görünmezlik pelerini", "yapay malzeme", "bükme", "ters kırılma"], "zorluk": "zor"},
    {"kelime": "evanescent dalga yakalamak", "aciklama": "tam yansıma arayüzeyinin hemen ötesinde eksponansiyel sönen kaybolan dalga alanı", "yasakli_kelimeler": ["sönen dalga", "arayüzey", "üstel", "eksponansiyel", "yakın alan"], "zorluk": "zor"},
    {"kelime": "optik cımbızla tutmak", "aciklama": "odaklanmış lazer demetinin foton momentum kuvvetiyle tekil bakteriyi havada asılı tutmak", "yasakli_kelimeler": ["lazer", "foton momentumu", "yakalama", "mikro parçacık", "arthur ashkin"], "zorluk": "zor"},
    {"kelime": "faz farkını girişimle ölçmek", "aciklama": "iki koherent ışık kolunun birleşimindeki faz kaymasını girişimölçerle bulmak", "yasakli_kelimeler": ["faz kayması", "girişimölçer", "koherent", "dalga", "ışın ayırıcı"], "zorluk": "zor"},
    {"kelime": "akromatik dublet birleştirmek", "aciklama": "crown ve flint camından yapılmış iki zıt merceği yapıştırıp renk sapmasını sıfırlamak", "yasakli_kelimeler": ["crown", "flint", "yapıştırma", "renk hatası", "düzeltme"], "zorluk": "zor"},
    {"kelime": "akusto-optik modülasyon", "aciklama": "kristal içine verilen ultrasonik ses dalgalarıyla ışığın yönünü ve şiddetini değiştirmek", "yasakli_kelimeler": ["ultrasonik", "kristal", "ses dalgası", "modülatör", "bragg"], "zorluk": "zor"},
    {"kelime": "pockels hücresi anahtarlamak", "aciklama": "elektrik alan uygulandığında kristalin çift kırıcılığını değiştirerek hızlı optik kapı açmak", "yasakli_kelimeler": ["elektro-optik", "kristal", "anahtarlama", "voltaj", "q-switch"], "zorluk": "zor"}
]

orman_verbs = [
    # Kolay (12)
    {"kelime": "ağaç dikmek", "aciklama": "ormanlık alana genç fidanları toprağa gömüp can suyu vermek", "yasakli_kelimeler": ["fidan", "toprak", "ağaçlandırma", "yeşil", "dikim"], "zorluk": "kolay"},
    {"kelime": "ağaç kesmek", "aciklama": "motorlu testereyle olgunlaşmış veya işaretli ağacı devirmek", "yasakli_kelimeler": ["motorlu testere", "devirmek", "odun", "balta", "kütük"], "zorluk": "kolay"},
    {"kelime": "yürüyüş yapmak", "aciklama": "orman patikalarında kuş sesleri eşliğinde doğa yürüyüşü yapmak", "yasakli_kelimeler": ["trekking", "patika", "doğa", "temiz hava", "ağaçlar"], "zorluk": "kolay"},
    {"kelime": "kamp kurmak", "aciklama": "ormanda ağaçlar arasına çadır açıp geceyi geçirmek", "yasakli_kelimeler": ["çadır", "kamp", "uyku tulumu", "gece", "ateş"], "zorluk": "kolay"},
    {"kelime": "mantar toplamak", "aciklama": "yağmur sonrası nemli ağaç diplerindeki yenebilir mantarları sepete koymak", "yasakli_kelimeler": ["mantar", "sepet", "yağmur", "dip", "zehirli"], "zorluk": "kolay"},
    {"kelime": "odun toplamak", "aciklama": "yerdeki kuru dal parçalarını yakacak için bir araya getirmek", "yasakli_kelimeler": ["kuru dal", "çalı", "yakacak", "yer", "ateş"], "zorluk": "kolay"},
    {"kelime": "kuş gözlemek", "aciklama": "dürbünle ağaç dallarındaki yabani kuş türlerini takip etmek", "yasakli_kelimeler": ["dürbün", "ağaç dalı", "yabani", "tür", "izlemek"], "zorluk": "kolay"},
    {"kelime": "yangın söndürmek", "aciklama": "ağaçları saran alevleri arazöz veya helikopterle su dökerek durdurmak", "yasakli_kelimeler": ["alev", "itfaiye", "su", "helikopter", "duman"], "zorluk": "kolay"},
    {"kelime": "ormanı korumak", "aciklama": "kaçak kesim ve kaçak avcılığa karşı koruma tedbiri almak", "yasakli_kelimeler": ["kaçak kesim", "muhafaza", "avcı", "tedbir", "bekçi"], "zorluk": "kolay"},
    {"kelime": "oksijen üretmek", "aciklama": "ağaçların fotosentezle karbondioksiti alıp havaya temiz oksijen salması", "yasakli_kelimeler": ["fotosentez", "temiz hava", "yaprak", "karbondioksit", "salım"], "zorluk": "kolay"},
    {"kelime": "yaprak dökmek", "aciklama": "geniş yapraklı orman ağaçlarının sonbaharda yapraklarını boşaltması", "yasakli_kelimeler": ["sonbahar", "sararma", "düşmek", "meşe", "güz"], "zorluk": "kolay"},
    {"kelime": "yeşermek", "aciklama": "baharın gelmesiyle kuru ağaç dallarının taze filizlerle kaplanması", "yasakli_kelimeler": ["bahar", "filiz", "taze", "canlanmak", "yapraklanma"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "damgalama yapmak", "aciklama": "orman mühendisinin kesilecek veya korunacak ağaç gövdesine kırmızı işaret vurması", "yasakli_kelimeler": ["kırmızı boya", "çekiç", "işaret", "mühendis", "kesim izni"], "zorluk": "orta"},
    {"kelime": "yangın emniyet şeridi açmak", "aciklama": "alevlerin sıçramasını önlemek için orman blokları arasında çıplak toprak koridor sürmek", "yasakli_kelimeler": ["şerit", "koridor", "dozer", "sıçrama", "toprak"], "zorluk": "orta"},
    {"kelime": "kozalak toplamak", "aciklama": "fidanlıklarda tohum üretmek için kızılçam veya karaçam kozalaklarını hasat etmek", "yasakli_kelimeler": ["çam", "tohum", "fidanlık", "ağaç", "hasat"], "zorluk": "orta"},
    {"kelime": "seyreltme yapmak", "aciklama": "sık orman dokusunda zayıf ağaçları kesip sağlıklı olanlara ışık ve alan açmak", "yasakli_kelimeler": ["bakım", "aralama", "sık", "ışık", "alan"], "zorluk": "orta"},
    {"kelime": "ağaç kabuğu soymak", "aciklama": "kesilen tomrukların kabuk böceği istilasını önlemek için dış kabuğunu sıyırmak", "yasakli_kelimeler": ["tomruk", "kabuk böceği", "sıyırmak", "zararlı", "ahşap"], "zorluk": "orta"},
    {"kelime": "istiflemek", "aciklama": "kesilip boylanan kütükleri orman deposunda düzenli piramitler halinde dizmek", "yasakli_kelimeler": ["kütük", "depo", "dizmek", "piramit", "odun"], "zorluk": "orta"},
    {"kelime": "reçine akıtmak", "aciklama": "çam ağacı gövdesine v şeklinde çizik atıp tenekelere sakız toplamak", "yasakli_kelimeler": ["çam sakızı", "çizik", "teneke", "akıntı", "yapışkan"], "zorluk": "orta"},
    {"kelime": "yangın gözetleme kulesi", "aciklama": "yüksek dağ tepesindeki kuleden duman çıkışlarını dürbün ve telsizle izlemek", "yasakli_kelimeler": ["kule", "duman", "telsiz", "gözetleme", "tepe"], "zorluk": "orta"},
    {"kelime": "fidan aşılamak", "aciklama": "yabani orman fidanına kültür meyvesi veya aşılı göz kaynaştırmak", "yasakli_kelimeler": ["aşılama", "göz", "yabani", "meyve", "kaynaşma"], "zorluk": "orta"},
    {"kelime": "erozyonu önlemek", "aciklama": "ağaç köklerinin toprağı tutarak yağmur sularıyla kaymasını engellemek", "yasakli_kelimeler": ["toprak kayması", "kök", "yamaç", "sel", "tutunma"], "zorluk": "orta"},
    {"kelime": "fotokapan kurmak", "aciklama": "yaban hayatı ve kaçakçıları görüntülemek için ağaç gövdesine hareket sensörlü kamera takmak", "yasakli_kelimeler": ["sensörlü kamera", "yaban hayatı", "ayı", "kurt", "ağaç gövdesi"], "zorluk": "orta"},
    {"kelime": "kayın ormanında gezmek", "aciklama": "karadeniz dağlarındaki dev gövdeli kayın ağaçları altında yürümek", "yasakli_kelimeler": ["kayın", "karadeniz", "geniş yaprak", "gövde", "yayla"], "zorluk": "orta"},
    {"kelime": "talaş çıkarmak", "aciklama": "hızar makinesinde odunlar biçilirken etrafa ahşap tozları saçılması", "yasakli_kelimeler": ["hızar", "testere", "ahşap tozu", "marangoz", "odun"], "zorluk": "orta"},
    {"kelime": "orman yolu açmak", "aciklama": "yangın ve nakliyat araçlarının ulaşabilmesi için dozerle patika yarmak", "yasakli_kelimeler": ["dozer", "nakliyat", "ulaşım", "yangın aracı", "yol"], "zorluk": "orta"},
    {"kelime": "böcek zararlısıyla mücadele", "aciklama": "ağaçları kurutan çam kese tırtıllarına karşı biyolojik veya kimyasal önlem almak", "yasakli_kelimeler": ["çam kese tırtılı", "parazit", "biyolojik", "kuruma", "zararlı"], "zorluk": "orta"},
    {"kelime": "orman muhafaza devriyesi", "aciklama": "silahlı orman koruma memurlarının arazi araçlarıyla bölgeyi turlaması", "yasakli_kelimeler": ["muhafaza memuru", "devriye", "arazi aracı", "kaçakçılık", "denetim"], "zorluk": "orta"},
    {"kelime": "yaş halkası saymak", "aciklama": "kesilen ağaç gövdesindeki enine dairesel halkalardan yaşını hesaplamak", "yasakli_kelimeler": ["halka", "gövde kesiti", "ağaç yaşı", "daire", "yıllık"], "zorluk": "orta"},
    {"kelime": "orman vasfını kaybetmek", "aciklama": "tahrip olan alanın resmi kayıtlarda orman statüsünden çıkarılması", "yasakli_kelimeler": ["2b", "statü", "tahribat", "resmi kayıt", "vasıf"], "zorluk": "orta"},
    {"kelime": "doğal gençleştirme yapmak", "aciklama": "mevcut yaşlı ağaçların tohum dökmesiyle yeni neslin kendi kendine büyümesi", "yasakli_kelimeler": ["gençlik", "tohum dökümü", "kendiliğinden", "orman bakımı", "yaşlı ağaç"], "zorluk": "orta"},
    {"kelime": "yaprak gübresi oluşmak", "aciklama": "orman tabanındaki kuru yaprakların çürüyerek humuslu zengin toprak yapması", "yasakli_kelimeler": ["humus", "çürüme", "orman tabanı", "zengin toprak", "organik"], "zorluk": "orta"},
    {"kelime": "balta girmemiş orman", "aciklama": "insan elinin ve baltasının hiç değmediği bakir balta girmemiş vahşi koru", "yasakli_kelimeler": ["bakir", "balta", "insan eli", "vahşi", "değmemiş"], "zorluk": "orta"},
    {"kelime": "sürgün vermek", "aciklama": "kesilen ağaç kütüğünden veya kökünden yeni taze tırnak dalların fışkırması", "yasakli_kelimeler": ["taze filiz", "kütük", "kök", "fışkırma", "büyüme"], "zorluk": "orta"},
    {"kelime": "meşe palamudu saçılmak", "aciklama": "sonbaharda koca meşe ağaçlarından toprağa sert kabuklu tohumların dökülmesi", "yasakli_kelimeler": ["palamut", "meşe", "sincap", "tohum", "dökülmek"], "zorluk": "orta"},
    {"kelime": "çam iğnesi süpürmek", "aciklama": "yangın riski oluşturan yerdeki kuru çam pürlerini temizlemek", "yasakli_kelimeler": ["çam pürü", "iğne yaprak", "temizlik", "yangın riski", "taban"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "silvikültür uygulamak", "aciklama": "ormanların planlı yetiştirilmesi, bakımı, gençleştirilmesi ve korunması bilimi", "yasakli_kelimeler": ["orman yetiştirme", "bakım", "gençleştirme", "orman amenajmanı", "bilim"], "zorluk": "zor"},
    {"kelime": "amenajman planı yapmak", "aciklama": "ormanın 10-20 yıllık dönemde ne kadar odun üreteceği ve nasıl kesileceğini haritalamak", "yasakli_kelimeler": ["envanter", "yıllık artım", "kesim planı", "eta", "harita"], "zorluk": "zor"},
    {"kelime": "klimaks vejetasyona ulaşmak", "aciklama": "orman ekosisteminin tür çeşitliliği ve biyokütle olarak en kararlı nihai evreye gelmesi", "yasakli_kelimeler": ["nihai evre", "süksesyon", "kararlı", "ekosistem", "biyokütle"], "zorluk": "zor"},
    {"kelime": "dendrokronolojik tarihleme", "aciklama": "ağaç gövdesindeki yıllık yaş halkalarının genişlik deseninden geçmiş iklimi okumak", "yasakli_kelimeler": ["yaş halkası", "geçmiş iklim", "tarihleme", "genişlik", "desen"], "zorluk": "zor"},
    {"kelime": "eta hesabı çıkarmak", "aciklama": "orman amenajmanında ormanın yıllık büyüme miktarını aşmayacak yasal kesim hacmi", "yasakli_kelimeler": ["kesim hacmi", "yıllık artım", "metreküp", "yasal sınır", "orman geliri"], "zorluk": "zor"},
    {"kelime": "bonitet tayini yapmak", "aciklama": "orman arazisinin toprak ve iklim açısından ağaç yetiştirme verim sınıfını belirlemek", "yasakli_kelimeler": ["verim sınıfı", "toprak kalitesi", "ağaç boyu", "saha", "kalite"], "zorluk": "zor"},
    {"kelime": "fitososyolojik etüt yapmak", "aciklama": "orman tabanındaki bitki birliklerinin ve floristik kompozisyonun sosyolojisini incelemek", "yasakli_kelimeler": ["bitki birliği", "braun-blanquet", "flora", "kompozisyon", "vejetasyon"], "zorluk": "zor"},
    {"kelime": "karbon yutağı olmak", "aciklama": "atmosferik karbondioksiti devasa biyokütlesinde ve orman toprağında hapsedip depolamak", "yasakli_kelimeler": ["karbon tutumu", "biyokütle", "sera gazı", "depolama", "küresel ısınma"], "zorluk": "zor"},
    {"kelime": "taç kapalılığını ölçmek", "aciklama": "orman örtüsünde ağaç tepelerinin gökyüzünü kapatma oranını yüzdeyle saptamak", "yasakli_kelimeler": ["kapalılık", "tepe tacı", "yüzde", "gökyüzü", "örtü"], "zorluk": "zor"},
    {"kelime": "ekoton kuşağı oluşturmak", "aciklama": "orman ile çayır veya göl arasındaki zengin geçiş zonunda tür çeşitliliği barındırmak", "yasakli_kelimeler": ["geçiş zonu", "kenar etkisi", "çayır", "çeşitlilik", "sınır"], "zorluk": "zor"},
    {"kelime": "miko-rizal ağ kurmak", "aciklama": "orman ağaçlarının köklerinde mantar hifleriyle birbirine besin ve sinyal aktaran dev yeraltı ağı", "yasakli_kelimeler": ["mantar kök", "wood wide web", "simbiyoz", "hif", "yeraltı iletişimi"], "zorluk": "zor"},
    {"kelime": "kalburlama yapmak", "aciklama": "orman tohumlarının çimlenme kabiliyetini artırmak için laboratuvarda saflaştırmak", "yasakli_kelimeler": ["tohum", "çimlenme", "laboratuvar", "saflık", "fidanlık"], "zorluk": "zor"},
    {"kelime": "kök sürgünüyle yayılmak", "aciklama": "kavak veya kızılağacın toprağın altından uzanan köklerinden yüzlerce yeni gövde çıkarması", "yasakli_kelimeler": ["klon", "kavak", "yeraltı kökü", "klonal", "vejetatif"], "zorluk": "zor"},
    {"kelime": "defolyasyona maruz kalmak", "aciklama": "istilacı tırtılların veya asit yağmurunun tüm ağaç yapraklarını tamamen dökmesi", "yasakli_kelimeler": ["yapraksızlaşma", "tırtıl istilası", "asit yağmuru", "tahribat", "kuruma"], "zorluk": "zor"}
]

if __name__ == "__main__":
    add_and_save_verbs("optik", optik_verbs)
    add_and_save_verbs("orman", orman_verbs)
