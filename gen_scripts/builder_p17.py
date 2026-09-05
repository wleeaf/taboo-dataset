import os, sys, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gen_scripts.card_utils import add_and_save_verbs

# 33. kimya
kimya_verbs = [
    # Kolay (12)
    {"kelime": "deney yapmak", "yasakli_kelimeler": ["tüp", "laboratuvar", "karışım", "bilim", "reaksiyon"], "zorluk": "kolay", "aciklama": "Kimyasal olayları gözlemlemek için kontrollü test yürütmek."},
    {"kelime": "tüp çalkalamak", "yasakli_kelimeler": ["cam", "sıvı", "karıştırmak", "laboratuvar", "deney tüpü"], "zorluk": "kolay", "aciklama": "Deney tüpündeki sıvıları birbirine karıştırmak için sallamak."},
    {"kelime": "asit dökmek", "yasakli_kelimeler": ["yakıcı", "ph", "sıvı", "tehlike", "damla"], "zorluk": "kolay", "aciklama": "Reaksiyon kabına dikkatlice asidik sıvı ilave etmek."},
    {"kelime": "su kaynatmak", "yasakli_kelimeler": ["100 derece", "buhar", "ocak", "beher", "ısıtmak"], "zorluk": "kolay", "aciklama": "Sıvının sıcaklığını kaynama noktasına ulaştırıp buharlaştırmak."},
    {"kelime": "tuz eritmek", "yasakli_kelimeler": ["çözünmek", "su", "karıştırmak", "şeffaf", "çözelti"], "zorluk": "kolay", "aciklama": "Katı tuzu suyun içinde çözünene kadar karıştırmak."},
    {"kelime": "damlalık kullanmak", "yasakli_kelimeler": ["pipet", "damla damla", "sıvı çekmek", "cam uç", "ekleme"], "zorluk": "kolay", "aciklama": "Sıvıyı azar azar damlatarak kaba aktarmak."},
    {"kelime": "önlük giymek", "yasakli_kelimeler": ["beyaz", "laboratuvar", "koruma", "kıyafet", "leke"], "zorluk": "kolay", "aciklama": "Kimyasal sıçramalardan korunmak için beyaz önlük takmak."},
    {"kelime": "koruyucu gözlük takmak", "yasakli_kelimeler": ["göz", "plastik", "güvenlik", "sıçrama", "laboratuvar"], "zorluk": "kolay", "aciklama": "Gözleri tehlikeli gaz ve kimyasal sıçramalardan korumak."},
    {"kelime": "periyodik tabloya bakmak", "yasakli_kelimeler": ["elementler", "sembol", "mendeleyev", "atom numarası", "çizelge"], "zorluk": "kolay", "aciklama": "Elementlerin sıralandığı kimyasal tabloyu incelemek."},
    {"kelime": "gaz çıkışı izlemek", "yasakli_kelimeler": ["kabarcık", "duman", "köpürme", "reaksiyon", "tüp"], "zorluk": "kolay", "aciklama": "Kimyasal tepkime anında sıvıdan kabarcıklar halinde gaz çıkışını görmek."},
    {"kelime": "hassas terazide tartmak", "yasakli_kelimeler": ["gram", "miligram", "toz", "madde", "ölçüm"], "zorluk": "kolay", "aciklama": "Kimyasal tozu miligram hassasiyetinde tartmak."},
    {"kelime": "renk değişimini gözlemek", "yasakli_kelimeler": ["indikatör", "pembe mavi", "reaksiyon", "fark", "turnusol"], "zorluk": "kolay", "aciklama": "Tepkime sonrasında çözeltinin renginin değişmesini izlemek."},

    # Orta (24)
    {"kelime": "titrasyon yapmak", "yasakli_kelimeler": ["büret", "dönüm noktası", "asit baz", "indikatör", "damla damla"], "zorluk": "orta", "aciklama": "Büret yardımıyla konsantrasyonu bilinmeyen çözeltinin derişimini bulmak."},
    {"kelime": "çökelme oluşturmak", "yasakli_kelimeler": ["presipitasyon", "dipte birikme", "katı tortu", "çözünürlük çarpımı", "bulanıklık"], "zorluk": "orta", "aciklama": "İki çözelti karıştığında çözünmeyen katı maddenin dibe çökmesi."},
    {"kelime": "destilasyon yapmak", "yasakli_kelimeler": ["damıtma", "kaynama noktası farkı", "soğutucu", "buharlaşma", "fraksiyonel"], "zorluk": "orta", "aciklama": "Farklı kaynama noktasına sahip sıvıları buharlaştırıp yoğuşturarak ayırmak."},
    {"kelime": "pH değerini ölçmek", "yasakli_kelimeler": ["asitlik bazlık", "turnusol kağıdı", "0 ile 14", "prob", "hidrojen iyonu"], "zorluk": "orta", "aciklama": "Çözeltinin hidrojen iyonu yoğunluğunu pH metreyle ölçmek."},
    {"kelime": "kristallendirmek", "yasakli_kelimeler": ["aşırı doymuş", "soğuma", "katılaşma", "saflaştırma", "kristal yapısı"], "zorluk": "orta", "aciklama": "Sıcak doymuş çözeltiyi soğutarak saf katı kristaller elde etmek."},
    {"kelime": "katalizör eklemek", "yasakli_kelimeler": ["tepkime hızı", "aktivasyon enerjisi", "tüketilmeden çıkan", "hızlandırıcı", "reaksiyon"], "zorluk": "orta", "aciklama": "Tepkimenin aktivasyon enerjisini düşürerek reaksiyonu hızlandırmak."},
    {"kelime": "çözelti hazırlamak", "yasakli_kelimeler": ["molarite", "balon joje", "çözücü çözünen", "karışım", "hacim"], "zorluk": "orta", "aciklama": "Belirli molaritede homojen sıvı karışım üretmek."},
    {"kelime": "ekzotermik ısı salmak", "yasakli_kelimeler": ["dışarı ısı verme", "sıcaklık artışı", "yanma", "entalpi eksi", "reaksiyon"], "zorluk": "orta", "aciklama": "Tepkime gerçekleşirken çevreye ısı enerjisi yaymak."},
    {"kelime": "endotermik ısı soğurmak", "yasakli_kelimeler": ["çevreden ısı alma", "soğuma", "entalpi artı", "enerji ihtiyacı", "reaksiyon"], "zorluk": "orta", "aciklama": "Tepkimenin yürümesi için dışarıdan ısı absorbe etmek."},
    {"kelime": "süzme işlemi yapmak", "yasakli_kelimeler": ["filtre kağıdı", "huni", "katı sıvı ayırma", "süzüntü", "beher"], "zorluk": "orta", "aciklama": "Sıvı içindeki asılı katı parçacıkları süzgeç kağıdıyla ayırmak."},
    {"kelime": "korozyona uğramak", "yasakli_kelimeler": ["paslanma", "metal aşınması", "oksitlenme", "nem hava", "demir"], "zorluk": "orta", "aciklama": "Metallerin kimyasal çevre etkisiyle oksitlenip aşınması."},
    {"kelime": "tampon çözelti oluşturmak", "yasakli_kelimeler": ["ph sabit tutma", "zayıf asit tuz", "direnç", "baz ekleme", "denge"], "zorluk": "orta", "aciklama": "Asit veya baz eklendiğinde pH değişimine direnen çözelti hazırlamak."},
    {"kelime": "santrifüj etmek", "yasakli_kelimeler": ["hızlı döndürme", "merkezkaç", "tüp", "çöktürme", "ayrıştırma"], "zorluk": "orta", "aciklama": "Yüksek devirde döndürerek yoğunluk farkıyla katıyı çöktürmek."},
    {"kelime": "polimerizasyon başlatmak", "yasakli_kelimeler": ["monomer", "uzun zincir", "plastik", "bağ oluşumu", "makromolekül"], "zorluk": "orta", "aciklama": "Küçük moleküllerin birbirine bağlanarak dev zincirler oluşturmasını sağlamak."},
    {"kelime": "kromatografi uygulamak", "yasakli_kelimeler": ["ince tabaka", "tlc", "hareketli faz", "ayrışma", "renk bantları"], "zorluk": "orta", "aciklama": "Karışımdaki bileşenleri durağan ve hareketli faz yardımıyla ayırmak."},
    {"kelime": "redoks tepkimesi yürütmek", "yasakli_kelimeler": ["yükseltgenme indirgenme", "elektron alışverişi", "anot katot", "pil", "yük"], "zorluk": "orta", "aciklama": "Elektron aktarımıyla gerçekleşen oksidasyon-redüksiyon tepkimesini sağlamak."},
    {"kelime": "eter ekstraksiyonu yapmak", "yasakli_kelimeler": ["ayırma hunisi", "çözücü çekimi", "iki faz", "organik katman", "çalkalama"], "zorluk": "orta", "aciklama": "Organik maddeyi ayırma hunisinde çözücü yardımıyla sulu fazdan çekmek."},
    {"kelime": "manyetik karıştırıcı çalıştırmak", "yasakli_kelimeler": ["balık", "manyetik alan", "beher", "homojen", "ısıtıcı tabla"], "zorluk": "orta", "aciklama": "Manyetik balık kullanarak sıvıyı sürekli ve homojen döndürmek."},
    {"kelime": "çözünürlüğü artırmak", "yasakli_kelimeler": ["sıcaklık", "karıştırma", "basınç", "katı madde", "doygunluk"], "zorluk": "orta", "aciklama": "Sıcaklığı yükselterek bir sıvının çözebileceği madde miktarını artırmak."},
    {"kelime": "kimyasal bağ kurmak", "yasakli_kelimeler": ["kovalent", "iyonik", "elektron paylaşımı", "molekül", "kararlılık"], "zorluk": "orta", "aciklama": "Atomların elektron ortaklaşması veya transferiyle kararlı yapıya geçmesi."},
    {"kelime": "geri soğutucu altında kaynatmak", "yasakli_kelimeler": ["reflüks", "buharlaşan sıvıyı yoğuşturma", "balon", "uzun süreli reaksiyon", "kondenser"], "zorluk": "orta", "aciklama": "Buharlaşan sıvıyı soğutucuda yoğuşturup kaba geri damlatarak kaynatmak."},
    {"kelime": "erime noktasını tayin etmek", "yasakli_kelimeler": ["kapiler tüp", "saflık derecesi", "katıdan sıvıya", "sıcaklık", "cihaz"], "zorluk": "orta", "aciklama": "Katı kimyasalın eridiği sıcaklığı ölçerek saflığını belirlemek."},
    {"kelime": "çekerocakta çalışmak", "yasakli_kelimeler": ["zehirli gaz", "havalandırma", "cam kapak", "emme fanı", "güvenlik"], "zorluk": "orta", "aciklama": "Tehlikeli buhar çıkaran deneyleri fanlı cam kabin içinde yapmak."},
    {"kelime": "mol miktarını hesaplamak", "yasakli_kelimeler": ["avogadro sayısı", "n eşittir m bölü ma", "gram", "kütle", "atom ağırlığı"], "zorluk": "orta", "aciklama": "Maddenin kütlesini mol kütlesine bölerek tanecik miktarını bulmak."},

    # Zor (14)
    {"kelime": "gibbs serbest enerjisini hesaplamak", "yasakli_kelimeler": ["delta g", "spontanlık", "entalpi eksi t delta s", "termodinamik denge", "istemli reaksiyon"], "zorluk": "zor", "aciklama": "Tepkimenin kendiliğinden yürüyüp yürümeyeceğini termodinamik formülle saptamak."},
    {"kelime": "nMR spektrumu çekmek", "yasakli_kelimeler": ["nükleer manyetik rezonans", "kimyasal kayma", "proton 1h", "yapı aydınlatma", "spin"], "zorluk": "zor", "aciklama": "Molekülün üç boyutlu kimyasal yapısını manyetik rezonans sinyalleriyle çözmek."},
    {"kelime": "kızılötesi spektroskopisi yapmak", "yasakli_kelimeler": ["ft-ir", "fonksiyonel gruplar", "bağ titreşimleri", "dalga sayısı", "absorbans"], "zorluk": "zor", "aciklama": "Moleküldeki fonksiyonel grupların bağ titreşim frekanslarını IR ışığıyla saptamak."},
    {"kelime": "le Chatelier ilkesini uygulamak", "yasakli_kelimeler": ["denge kayması", "etkiye tepki", "sıcaklık basınç derişim", "ürünler girenler", "kimyasal denge"], "zorluk": "zor", "aciklama": "Dengedeki sisteme yapılan dış müdahalenin denge yönünü nasıl kaydıracağını belirlemek."},
    {"kelime": "arrhenius denklemini çözmek", "yasakli_kelimeler": ["hız sabiti k", "aktivasyon enerjisi ea", "sıcaklık bağımlılığı", "üstel", "çarpışma teorisi"], "zorluk": "zor", "aciklama": "Sıcaklığın kimyasal reaksiyon hızı üzerindeki etkisini matematiksel modellemek."},
    {"kelime": "sn2 mekanizmasıyla yürümek", "yasakli_kelimeler": ["biyomoleküler nükleofilik sübstitüsyon", "arkadan saldırı", "walden terslenmesi", "tek basamak", "ara ürün yok"], "zorluk": "zor", "aciklama": "Nükleofilin ters taraftan saldırıp tek basamakta konfigürasyon terslenmesiyle bağlanması."},
    {"kelime": "kiral merkez belirlemek", "yasakli_kelimeler": ["asimetrik karbon", "dört farklı grup", "optikçe aktif", "enantiomer", "stereokimya"], "zorluk": "zor", "aciklama": "Karbon atomuna bağlı dört farklı grubu inceleyip kiraliteyi saptamak."},
    {"kelime": "kütle spektrometresi ile tartmak", "yasakli_kelimeler": ["m/z oranı", "moleküler iyon piki", "iyonlaşma", "parçalanma paterni", "izotop dağılımı"], "zorluk": "zor", "aciklama": "Molekülleri iyonlaştırıp kütle/yük oranlarına göre molekül ağırlığını saptamak."},
    {"kelime": "nernst denklemini işletmek", "yasakli_kelimeler": ["pil potansiyeli", "standart dışı koşullar", "iyon konsantrasyonu", "elektrokimya", "voltaj"], "zorluk": "zor", "aciklama": "Standart olmayan derişimlerde elektrokimyasal hücre potansiyelini hesaplamak."},
    {"kelime": "moleküler orbital diyagramı çizmek", "yasakli_kelimeler": ["homo lumo", "bağ yapan bağ karşıtı", "sigma pi", "elektron dizilimi", "kuantum"], "zorluk": "zor", "aciklama": "Atomik orbitallerin örtüşmesiyle oluşan moleküler enerji seviyelerini çizmek."},
    {"kelime": "kristal alan yarılmasını açıklamak", "yasakli_kelimeler": ["d orbitalleri", "oktahedral tetrahedral", "ligand alanı", "renk oluşumu", "kompleks"], "zorluk": "zor", "aciklama": "Geçiş metali komplekslerinde ligandların d orbitallerini farklı enerjilere yarmasını açıklamak."},
    {"kelime": "grignard reaktifi hazırlamak", "yasakli_kelimeler": ["organomagnezyum", "kuru eter", "karbonil saldırısı", "karbon-karbon bağı", "rmgx"], "zorluk": "zor", "aciklama": "Alkil halojenür ile magnezyumu susuz eterde reaksiyona sokarak organometalik reaktif üretmek."},
    {"kelime": "diels-Alder halkalaşması yapmak", "yasakli_kelimeler": ["[4+2] siklooktavasyon", "dien dienofil", "sikloheksen halkası", "perisiklik", "stereospesifik"], "zorluk": "zor", "aciklama": "Konjuge dien ile dienofili ısıtarak altı üyeli sikloheksen halkası sentezlemek."},
    {"kelime": "hPLC ile kromatografik ayırma yapmak", "yasakli_kelimeler": ["yüksek performanslı sıvı kromatografisi", "kolon", "yüksek basınç", "alıkonma zamanı", "pür saflık"], "zorluk": "zor", "aciklama": "Yüksek basınç altında mikron boyutlu dolgulu kolondan geçirerek saf fraksiyonlar toplamak."}
]

# 34. koreografi
koreografi_verbs = [
    # Kolay (12)
    {"kelime": "dans etmek", "yasakli_kelimeler": ["müzik", "ritim", "figür", "adımlar", "oynamak"], "zorluk": "kolay", "aciklama": "Müziğin ritmine uyarak bedensel hareketler sergilemek."},
    {"kelime": "adımları saymak", "yasakli_kelimeler": ["bir iki üç dört", "tempo", "prova", "dansçı", "ritim"], "zorluk": "kolay", "aciklama": "Dans hareketlerini öğrenirken ritim vuruşlarını sesli saymak."},
    {"kelime": "sahneye çıkmak", "yasakli_kelimeler": ["perde", "seyirci", "ışık", "gösteri", "alkış"], "zorluk": "kolay", "aciklama": "Performansı sergilemek için sahne alanına adım atmak."},
    {"kelime": "alkış almak", "yasakli_kelimeler": ["tebrik", "seyirci", "beğeni", "gösteri sonu", "selam"], "zorluk": "kolay", "aciklama": "Başarılı bir dans performansının ardından izleyiciden alkış toplamak."},
    {"kelime": "prova yapmak", "yasakli_kelimeler": ["tekrar", "çalışmak", "stüdyo", "ayna", "hazırlık"], "zorluk": "kolay", "aciklama": "Gösteri öncesi hareketleri aynalı salonda defalarca tekrar etmek."},
    {"kelime": "ritme uymak", "yasakli_kelimeler": ["tempo", "müzik", "kaçırmamak", "vuruş", "senkron"], "zorluk": "kolay", "aciklama": "Vücut hareketlerini çalan müziğin vuruşlarıyla tam eşzamanlı kılmak."},
    {"kelime": "esnemek", "yasakli_kelimeler": ["streching", "bacak açma", "kas", "ısınma", "esneklik"], "zorluk": "kolay", "aciklama": "Dans öncesi kasları uzatıp sakatlanmayı önleyici egzersiz yapmak."},
    {"kelime": "figür sergilemek", "yasakli_kelimeler": ["hareket", "dönüş", "estetik", "gösteri", "jest"], "zorluk": "kolay", "aciklama": "Belirli bir dans tarzına özgü hareket kombinasyonunu sunmak."},
    {"kelime": "dönmek", "yasakli_kelimeler": ["spin", "fırıldak", "piruet", "kendi etrafında", "denge"], "zorluk": "kolay", "aciklama": "Tek veya çift ayak üzerinde kendi ekseni etrafında tur atmak."},
    {"kelime": "zıplamak", "yasakli_kelimeler": ["sıçramak", "havaya", "ayak", "yere basma", "hareket"], "zorluk": "kolay", "aciklama": "Yerden kuvvet alarak iki veya tek ayakla havaya yükselmek."},
    {"kelime": "selam vermek", "yasakli_kelimeler": ["eğilmek", "gösteri sonu", "seyirci", "teşekkür", "alkış"], "zorluk": "kolay", "aciklama": "Performans bitiminde sahne önünde eğilerek izleyiciyi selamlamak."},
    {"kelime": "kostüm giymek", "yasakli_kelimeler": ["kıyafet", "gösteri", "sahne", "renkli", "tütü"], "zorluk": "kolay", "aciklama": "Koreografinin konseptine uygun sahne giysisini kuşanmak."},

    # Orta (24)
    {"kelime": "koreografi yazmak", "yasakli_kelimeler": ["figür tasarlama", "dans adımları", "müzik kurgusu", "sahneleme", "yaratım"], "zorluk": "orta", "aciklama": "Dansın tüm hareket akışını ve sahne düzenini baştan sona tasarlamak."},
    {"kelime": "senkronize olmak", "yasakli_kelimeler": ["aynı anda", "uyum", "toplu dans", "birlikte hareket", "fark olmaması"], "zorluk": "orta", "aciklama": "Gruptaki tüm dansçıların hareketleri birebir aynı anda ve uyumla yapması."},
    {"kelime": "piruet atmak", "yasakli_kelimeler": ["tek ayak üstünde dönüş", "bale", "noktaya odaklanma", "spotting", "denge"], "zorluk": "orta", "aciklama": "Tek ayak parmak ucunda başı sabit noktaya odaklayarak hızlı dönüş yapmak."},
    {"kelime": "sahne trafiğini düzenlemek", "yasakli_kelimeler": ["giriş çıkış", "dansçı akışı", "çarpışma önleme", "alan kullanımı", "mizanpaj"], "zorluk": "orta", "aciklama": "Dansçıların sahneye giriş, konumlanma ve çıkış rotalarını planlamak."},
    {"kelime": "müziği saymak", "yasakli_kelimeler": ["sekizlik sayım", "1-8 ölçü", "ritim analizi", "vuruş eşleme", "koreograf"], "zorluk": "orta", "aciklama": "Müziği 8'lik ölçülere bölerek adımları ölçü basamaklarına yerleştirmek."},
    {"kelime": "doğaçlama dans etmek", "yasakli_kelimeler": ["emprovizasyon", "içinden geldiği gibi", "serbest hareket", "çağdaş dans", "akış"], "zorluk": "orta", "aciklama": "Önceden belirlenmiş kalıplara bağlı kalmadan anlık duyguyla dans etmek."},
    {"kelime": "lift yapmak", "yasakli_kelimeler": ["havaya kaldırma", "partner", "taşıma", "havada asılı", "akrobatik"], "zorluk": "orta", "aciklama": "Partnerini iki elle kavrayıp estetik biçimde havaya kaldırmak."},
    {"kelime": "pas dö dö icra etmek", "yasakli_kelimeler": ["ikili dans", "balerin balet", "partnerlik", "bale", "düet"], "zorluk": "orta", "aciklama": "Klasik balede kadın ve erkek dansçının sergilediği ikili gösteriyi sunmak."},
    {"kelime": "bloklama yapmak", "yasakli_kelimeler": ["sahnede diziliş", "v düzeni", "daire", "dansçı yerleşimi", "formasyon"], "zorluk": "orta", "aciklama": "Dansçıların sahnede geometrik formasyonlar halinde yerleşmesini sağlamak."},
    {"kelime": "kanon tekniği uygulamak", "yasakli_kelimeler": ["dalga hareketi", "sırayla başlama", "ardışık hareket", "gecikmeli tekrar", "grup"], "zorluk": "orta", "aciklama": "Aynı hareketi dansçıların birer saniye arayla dalga halinde başlatması."},
    {"kelime": "spotting yapmak", "yasakli_kelimeler": ["baş savurma", "baş dönmesi önleme", "sabit noktaya bakma", "dönüş tekniği", "göz"], "zorluk": "orta", "aciklama": "Dönerken başın dönmemesi için bakışları karşıdaki tek bir noktaya odaklamak."},
    {"kelime": "beden dilini kullanmak", "yasakli_kelimeler": ["anlatım", "mimik", "jest", "duygu aktarımı", "hikaye"], "zorluk": "orta", "aciklama": "Koreografideki hikaye ve duyguyu jest ve beden hareketleriyle aktarmak."},
    {"kelime": "esneklik kazanmak", "yasakli_kelimeler": ["şpagat", "açma germe", "eklem açıklığı", "antreman", "bacak"], "zorluk": "orta", "aciklama": "Zor figürleri yapabilmek için kas ve bağ dokularının esnekliğini artırmak."},
    {"kelime": "plie yapmak", "yasakli_kelimeler": ["diz bükme", "bale temeli", "topuklar yerde", "yumuşak iniş", "pozisyon"], "zorluk": "orta", "aciklama": "Dizleri yana doğru bükerek gövdeyi esnek biçimde alçaltmak."},
    {"kelime": "temas doğaçlaması yapmak", "yasakli_kelimeler": ["contact improv", "fiziksel temas", "ağırlık paylaşımı", "çağdaş dans", "akış"], "zorluk": "orta", "aciklama": "Partnerlerin sürekli fiziksel temas ve ağırlık aktarımıyla spontane dans etmesi."},
    {"kelime": "müzik kurgusu yapmak", "yasakli_kelimeler": ["parça birleştirme", "mix", "soundtrack", "hızlandırma", "kurgu"], "zorluk": "orta", "aciklama": "Farklı müzikleri koreografinin dramaturjisine göre kesip birleştirmek."},
    {"kelime": "ışık provası yapmak", "yasakli_kelimeler": ["sahne spotu", "renk geçişi", "aydınlatma kurgusu", "teknik prova", "dansçı takibi"], "zorluk": "orta", "aciklama": "Dansçıların sahne ışıkları ve spotlarla olan uyumunu salonda denemek."},
    {"kelime": "enerji seviyesini yükseltmek", "yasakli_kelimeler": ["dinamizm", "patlama", "hızlanma", "sahne aurası", "coşku"], "zorluk": "orta", "aciklama": "Gösterinin doruk noktasında dansçıların fiziksel enerjisini zirveye taşımak."},
    {"kelime": "hizalanmayı kontrol etmek", "yasakli_kelimeler": ["çizgi", "aynı hizada durma", "simetri", "ön arka boşluk", "düzeltme"], "zorluk": "orta", "aciklama": "Grup dansında sıraların ve aralıkların düzgünlüğünü denetlemek."},
    {"kelime": "akrobatik hareket eklemek", "yasakli_kelimeler": ["amuda kalkma", "çember", "havada takla", "zor figür", "esneklik"], "zorluk": "orta", "aciklama": "Koreografinin içine jimnastik ve akrobasi unsurları serpiştirmek."},
    {"kelime": "yer çekimine teslim olmak", "yasakli_kelimeler": ["fall and recovery", "bırakma ve toparlanma", "yere düşüş", "humphrey", "gevşeme"], "zorluk": "orta", "aciklama": "Modern dansta bedeni yerçekimine bırakıp ardından tekrar yükseltmek."},
    {"kelime": "merkez dengesini bulmak", "yasakli_kelimeler": ["core gücü", "karın kasları", "denge", "omurga", "duruş"], "zorluk": "orta", "aciklama": "Dönüş ve sıçramalarda bedenin ağırlık merkezini sağlam tutmak."},
    {"kelime": "izleyiciyi büyülemek", "yasakli_kelimeler": ["hayranlık", "büyüleyici performans", "sahne hakimiyeti", "alkış", "estetik"], "zorluk": "orta", "aciklama": "Kusursuz hareket ve duygu aktarımıyla seyircide hayranlık uyandırmak."},
    {"kelime": "karakter yaratmak", "yasakli_kelimeler": ["rol", "anlatı", "bale temsili", "tiyatral ifade", "dramaturgi"], "zorluk": "orta", "aciklama": "Koreografideki hikayenin kahramanını bedensel ifadeyle canlandırmak."},

    # Zor (14)
    {"kelime": "laban hareket analizini uygulamak", "yasakli_kelimeler": ["labanotasyon", "ağırlık zaman uzam akış", "çaba grafiği", "kinetosfer", "dans notasyonu"], "zorluk": "zor", "aciklama": "Dans hareketlerini Laban'ın dört efor faktörü ve geometrik uzam sistemine göre kodlamak."},
    {"kelime": "labanotasyon ile kaydetmek", "yasakli_kelimeler": ["dans partisyonu", "hareket sembolleri", "dikey porte", "yazılı dans", "arşivleme"], "zorluk": "zor", "aciklama": "Tüm koreografiyi evrensel Laban hareket sembolleriyle kağıda nota gibi dökmek."},
    {"kelime": "kinetosferi haritalamak", "yasakli_kelimeler": ["kişisel hareket alanı", "uzanma mesafesi", "ikosahedron", "beden çevresi küre", "uzamsal"], "zorluk": "zor", "aciklama": "Bedenin yer değiştirmeden uzanabileceği üç boyutlu geometrik hacmi kurgulamak."},
    {"kelime": "kontraktil dinamikleri yönetmek", "yasakli_kelimeler": ["contraction release", "graham tekniği", "pelvis nefes", "merkezden başlayan güç", "kasılma"], "zorluk": "zor", "aciklama": "Martha Graham tekniğindeki karından başlayan nefes kasılması ve gevşemesini yönetmek."},
    {"kelime": "poliritmik koreografi kurmak", "yasakli_kelimeler": ["farklı uzuvlarda farklı ritim", "çapraz tempo", "ayak başka el başka", "karmaşık", "afrika dansı"], "zorluk": "zor", "aciklama": "Bedenin farklı uzuvlarının aynı anda farklı metronomik vuruşlarla dans etmesini sağlamak."},
    {"kelime": "somatik farkındalık oluşturmak", "yasakli_kelimeler": ["feldenkrais", "alexander tekniği", "içsel beden duyumu", "propriosepsiyon", "hareket verimi"], "zorluk": "zor", "aciklama": "Dansçının kendi kas ve iskelet dizilimini içsel beden algısıyla optimize etmesi."},
    {"kelime": "dramaturgik omurga inşa etmek", "yasakli_kelimeler": ["dans tiyatrosu", "pina bausch", "kavramsal kurgu", "anlatı yapısı", "sahne metni"], "zorluk": "zor", "aciklama": "Koreografinin arkasındaki felsefi ve psikolojik anlatı yapısını kurmak."},
    {"kelime": "mekansal rezonans yaratmak", "yasakli_kelimeler": ["mekanla bütünleşme", "akustik ve mimari", "site-specific", "yankı", "hareket diyaloğu"], "zorluk": "zor", "aciklama": "Dansın hareket temposunu icra edildiği mimari mekanın boşluklarıyla rezone etmek."},
    {"kelime": "polifonik dans kurgulamak", "yasakli_kelimeler": ["çok seslilik", "bağımsız hareket hatları", "kontrpuan", "aynı anda farklı partiler", "füg"], "zorluk": "zor", "aciklama": "Müzikteki füg gibi farklı dansçı gruplarının bağımsız hareket çizgilerini iç içe örmek."},
    {"kelime": "yer çekimi merkezini desantralize etmek", "yasakli_kelimeler": ["merkez dışı hareket", "forsythe tekniği", "dengesizlik estetiği", "aşırı bükülme", "açısal"], "zorluk": "zor", "aciklama": "Ağırlık merkezini omurga dışına taşıyarak kontrollü düşme ve sınır çizgileri aramak."},
    {"kelime": "kinestetik empati uyandırmak", "yasakli_kelimeler": ["ayna nöronlar", "seyircide kas hissi", "bedensel rezonans", "izleme deneyimi", "duyu"], "zorluk": "zor", "aciklama": "Dansçının hareket kuvvetinin izleyicinin kaslarında fiziksel bir his gibi yankılanmasını sağlamak."},
    {"kelime": "bütünsel koreoloji uygulamak", "yasakli_kelimeler": ["benesh notasyonu", "hareket bilimi", "antropolojik dans", "yapısal analiz", "teori"], "zorluk": "zor", "aciklama": "Dans hareketlerini sosyolojik, anatomik ve estetik boyutlarıyla akademik tahlile tabi tutmak."},
    {"kelime": "partisyon çıkarmak", "yasakli_kelimeler": ["dans skoru", "saniye saniye döküm", "ışık ses hareket tablosu", "sahne yönetimi", "yazılı plan"], "zorluk": "zor", "aciklama": "Müzik, ışık ve dans adımlarının saniyelik senkron tablosunu çıkarmak."},
    {"kelime": "biyomekanik kuvvet aktarımını optimize etmek", "yasakli_kelimeler": ["kinetik zincir", "tork üretimi", "minimum efor maksimum sıçrama", "eklem sağlığı", "açısal momentum"], "zorluk": "zor", "aciklama": "Yerden alınan reaksiyon kuvvetini eklemlere zarar vermeden maksimum sıçramaya dönüştürmek."}
]

add_and_save_verbs('kimya', kimya_verbs)
add_and_save_verbs('koreografi', koreografi_verbs)
print('P17 done!')
