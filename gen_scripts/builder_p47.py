# -*- coding: utf-8 -*-
from card_utils import add_and_save_verbs

tatlilar_verbs = [
    # Kolay (12)
    {"kelime": "şerbet dökmek", "aciklama": "fırından çıkan sıcak baklavanın üstüne ılık şeker şerbeti gezdirmek", "yasakli_kelimeler": ["baklava", "şeker", "kaynatmak", "sıcak", "tatlı"], "zorluk": "kolay"},
    {"kelime": "fırınlamak", "aciklama": "fırın sütlacı güveç kaplarında üstü kızarana kadar pişirmek", "yasakli_kelimeler": ["fırın", "sütlaç", "güveç", "kızarmak", "pişirme"], "zorluk": "kolay"},
    {"kelime": "karıştırmak", "aciklama": "tenceredeki pudingi veya muhallebiyi dibi tutmasın diye tahta kaşıkla çevirmek", "yasakli_kelimeler": ["muhallebi", "puding", "dibi tutmak", "tencere", "kaşık"], "zorluk": "kolay"},
    {"kelime": "çırpmak", "aciklama": "pasta kremasını veya yumurta akını mikserle köpük köpük yapmak", "yasakli_kelimeler": ["mikser", "krema", "yumurta akı", "köpük", "kase"], "zorluk": "kolay"},
    {"kelime": "süslemek", "aciklama": "pastanın üstüne çilek, fıstık tozu veya çikolata parçaları dizmek", "yasakli_kelimeler": ["pasta", "çilek", "antep fıstığı", "dekor", "çikolata"], "zorluk": "kolay"},
    {"kelime": "dilimlemek", "aciklama": "büyük tepsi böreğini veya pastayı bıçakla porsiyonlara ayırmak", "yasakli_kelimeler": ["bıçak", "porsiyon", "kesmek", "tepsi", "pasta"], "zorluk": "kolay"},
    {"kelime": "soğutmak", "aciklama": "pişen irmik helvasını veya kazandibini buzdolabına kaldırıp dinlendirmek", "yasakli_kelimeler": ["buzdolabı", "dinlendirmek", "kazandibi", "helva", "soğuk"], "zorluk": "kolay"},
    {"kelime": "eritmek", "aciklama": "çikolatayı benmari usulü sıcak su buharında sıvı hale getirmek", "yasakli_kelimeler": ["çikolata", "benmari", "sıvı", "buhar", "ısı"], "zorluk": "kolay"},
    {"kelime": "yoğurmak", "aciklama": "un kurabiyesi veya şekerpare için tereyağlı tatlı hamuru hazırlamak", "yasakli_kelimeler": ["şekerpare", "hamur", "tereyağı", "kurabiye", "un"], "zorluk": "kolay"},
    {"kelime": "kızartmak", "aciklama": "tulumba veya lokma hamurunu bol kızgın yağda nar gibi kızartmak", "yasakli_kelimeler": ["tulumba", "lokma", "yağ", "kızgın", "çıtır"], "zorluk": "kolay"},
    {"kelime": "ikram etmek", "aciklama": "bayramda veya misafirlere tabakta lezzetli tatlı sunmak", "yasakli_kelimeler": ["misafir", "sunum", "tabak", "bayram", "çatalla"], "zorluk": "kolay"},
    {"kelime": "tatmak", "aciklama": "yapılan tatlının şeker ve vanilya dengesini kaşık ucuyla kontrol etmek", "yasakli_kelimeler": ["lezzet", "şeker oranı", "denemek", "kaşık", "lezzetli"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "yufka açmak", "aciklama": "baklava için nişastayla tül gibi arkası görünen ince hamur açmak", "yasakli_kelimeler": ["tül gibi", "oklava", "nişasta", "baklava yufkası", "şeffaf"], "zorluk": "orta"},
    {"kelime": "karamelize etmek", "aciklama": "toz şekeri tavada yakarak altın sarısı sıvı karamele dönüştürmek", "yasakli_kelimeler": ["şeker eritme", "altın sarısı", "yanık şeker", "karamel", "tava"], "zorluk": "orta"},
    {"kelime": "dibi tutturmak", "aciklama": "kazandibinin tepsisini ocakta çevirerek altını kontrollü şekilde yakmak", "yasakli_kelimeler": ["kazandibi", "yanık taban", "ocakta çevirme", "pudra şekeri", "karamelize lezzet"], "zorluk": "orta"},
    {"kelime": "kakaoya bulamak", "aciklama": "truf çikolata toplarını acı kakao tozu dolu kasede yuvarlamak", "yasakli_kelimeler": ["truffle", "kakao tozu", "yuvarlama", "çikolata topu", "kaplama"], "zorluk": "orta"},
    {"kelime": "krema torbası kullanmak", "aciklama": "profiterol veya eklerin içine duy takılı torbayla pastacı kreması basmak", "yasakli_kelimeler": ["sıkma torbası", "profiterol", "ekler", "pastacı kreması", "duy"], "zorluk": "orta"},
    {"kelime": "şantiyi köpürtmek", "aciklama": "soğuk süt ile krem şanti tozunu yüksek devirde hacimce kabartmak", "yasakli_kelimeler": ["krem şanti", "soğuk süt", "kabartma", "yüksek devir", "beyaz köpük"], "zorluk": "orta"},
    {"kelime": "kadayif tel tel ayırmak", "aciklama": "künefe tepsisine dizmeden önce çiğ kadayıfı elle havalandırıp yağlamak", "yasakli_kelimeler": ["künefe", "tel kadayıf", "havalandırma", "tereyağıyla ovma", "ayırma"], "zorluk": "orta"},
    {"kelime": "peynir uzatmak", "aciklama": "sıcak künefeyi çatalla kaldırırken ortasındaki tuzsuz peynirin sünmesi", "yasakli_kelimeler": ["künefe peyniri", "sünme", "antakya", "sıcak şerbet", "uzama"], "zorluk": "orta"},
    {"kelime": "jöle dondurmak", "aciklama": "meyveli tartın üzerine parlak ve şeffaf jelatin sos döküp sertleştirmek", "yasakli_kelimeler": ["tart", "jelatin", "meyve kaplama", "parlak katman", "kıvam"], "zorluk": "orta"},
    {"kelime": "fıstık serpmek", "aciklama": "şerbetli tatlıların üstüne canlı yeşil toz antep fıstığı yaymak", "yasakli_kelimeler": ["antep fıstığı", "yeşil toz", "süsleme", "serpiştirme", "baklava üstü"], "zorluk": "orta"},
    {"kelime": "hindistan cevizi dökmek", "aciklama": "ıslak kekin veya revaninin üzerine beyaz rendelenmiş hindistan cevizi serpmek", "yasakli_kelimeler": ["revani", "ıslak kek", "beyaz rende", "süsleme", "hindistan cevizi"], "zorluk": "orta"},
    {"kelime": "damla sakızı dövmek", "aciklama": "sakızlı muhallebiye koku vermesi için sakız damlalarını havanda ezmek", "yasakli_kelimeler": ["havan", "sakızlı muhallebi", "aroma", "koku", "sakız adası"], "zorluk": "orta"},
    {"kelime": "un kavurmak", "aciklama": "helva tenceresinde unu tereyağıyla kokusu çıkıp rengi dönene kadar kavurmak", "yasakli_kelimeler": ["un helvası", "tereyağı", "kavurma", "koku", "kahverengi"], "zorluk": "orta"},
    {"kelime": "irmik pembeleştirmek", "aciklama": "çam fıstığı ve irmiği kısık ateşte sürekli karıştırarak kavurmak", "yasakli_kelimeler": ["irmik helvası", "çam fıstığı", "kısık ateş", "pembeleşme", "kavurma"], "zorluk": "orta"},
    {"kelime": "kıvam tutturmak", "aciklama": "şerbetin veya reçelin tırnak üstüne damlatıldığında dağılmayacak koyuluğa gelmesi", "yasakli_kelimeler": ["koyu şerbet", "damla testi", "reçel kıvamı", "koyuluk", "kaynama süresi"], "zorluk": "orta"},
    {"kelime": "dondurma dövmek", "aciklama": "maraş dondurmasını keçi sütü ve saleple kancada çekip uzatmak", "yasakli_kelimeler": ["maraş dondurması", "salep", "keçi sütü", "kancada dövme", "uzama"], "zorluk": "orta"},
    {"kelime": "pandispanya kabartmak", "aciklama": "yaş pasta için yumurtaları şekerle 10 dakika çırparak puf sünger kek yapmak", "yasakli_kelimeler": ["sünger kek", "yaş pasta keki", "kabarma", "puf puf", "fırın"], "zorluk": "orta"},
    {"kelime": "ganaj hazırlamak", "aciklama": "sıcak sıvı krema içine bitter çikolata kırıp pürüzsüz parlak sos yapmak", "yasakli_kelimeler": ["ganache", "bitter çikolata", "sıcak krema", "pasta sosu", "parlak"], "zorluk": "orta"},
    {"kelime": "şeker hamuru kaplamak", "aciklama": "doğum günü pastasını renkli elastik şeker hamuruyla pürüzsüz örtmek", "yasakli_kelimeler": ["fondant", "şeker hamuru", "figür", "doğum günü pastası", "ütüleme"], "zorluk": "orta"},
    {"kelime": "pudra şekeri elemek", "aciklama": "lokumların veya elmalı kurabiyelerin üstüne minik elekle beyaz toz serpmek", "yasakli_kelimeler": ["elmalı kurabiye", "lokum", "küçük elek", "beyaz toz", "toz şeker"], "zorluk": "orta"},
    {"kelime": "güllaç yaprağı ıslatmak", "aciklama": "ramazanda mısır nişastalı kuru güllaç yapraklarını ılık şekerli sütle yumuşatmak", "yasakli_kelimeler": ["ramazan tatlısı", "ılık süt", "nişasta yaprağı", "ceviz içi", "nar tanesi"], "zorluk": "orta"},
    {"kelime": "aşure kaynatmak", "aciklama": "buğday, nohut, fasulye, incir ve kuru kayısıyı koca kazanda pişirip süslemek", "yasakli_kelimeler": ["muharrem ayı", "buğday nohut", "kuru meyveler", "nar tarçın", "kazan"], "zorluk": "orta"},
    {"kelime": "trileçe sosu dökmek", "aciklama": "üç farklı sütten yapılan ıslak keki buzdolabında bekletip üstüne karamel yaymak", "yasakli_kelimeler": ["üç süt", "balkan tatlısı", "ıslak sünger", "karamel sos", "soğuk tatlı"], "zorluk": "orta"},
    {"kelime": "kabak tatlısı kireçlemek", "aciklama": "balkabağı dilimlerini kireç suyunda bekleterek dışını çıtır içini lokum yapmak", "yasakli_kelimeler": ["kireç suyu", "çıtır kabak", "tahin ceviz", "balkabağı", "sert kabuk"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "çikolatayı tempere etmek", "aciklama": "eritilmiş çikolatayı mermer tezgahta 28-31 dereceye soğutup parlak ve çıtır kılmak", "yasakli_kelimeler": ["temperleme", "mermer tezgah", "kristalizasyon", "termometre", "parlak kırılma"], "zorluk": "zor"},
    {"kelime": "makaron eteği kabartmak", "aciklama": "badem unlu bezeyi fırında tabanında karakteristik dantel eteği oluşturarak pişirmek", "yasakli_kelimeler": ["macaron", "dantel etek", "badem unu", "kurutma tepsisi", "fransız tatlısı"], "zorluk": "zor"},
    {"kelime": "parfe dondurmak", "aciklama": "yumurta sarısı sabayonu ve çırpılmış kremayı kalıba döküp eksi 18 derecede dondurmak", "yasakli_kelimeler": ["parfait", "sabayon", "donmuş tatlı", "kalıp", "yarı donuk"], "zorluk": "zor"},
    {"kelime": "şeker üflemek", "aciklama": "izomaltoz veya şekeri 160 derecede eritip pompayla içi boş cam küre heykeller şişirmek", "yasakli_kelimeler": ["izomalt", "şişirme pompa", "cam şeker", "şeker heykeli", "yüksek ısı"], "zorluk": "zor"},
    {"kelime": "krokan kırmak", "aciklama": "fındık veya bademleri karamelize şekere gömüp soğuduktan sonra sert plakayı parçalamak", "yasakli_kelimeler": ["krokant", "karamelize fındık", "sert plaka", "çıtır şeker", "pasta içi"], "zorluk": "zor"},
    {"kelime": "mille-feuille katlamak", "aciklama": "tereyağını milföy hamuruna yedirip tur vererek bin yaprak katmanı oluşturmak", "yasakli_kelimeler": ["milföy", "bin yaprak", "tur verme", "tereyağı bloğu", "fransız katmanı"], "zorluk": "zor"},
    {"kelime": "ayva tatlısına çekirdek koymak", "aciklama": "doğal kırmızı rengi ve jöle kıvamını yakalamak için tencereye ayva çekirdekleri atmak", "yasakli_kelimeler": ["doğal kırmızı", "çekirdek jölesi", "kaymak", "kısık ateş", "renk verme"], "zorluk": "zor"},
    {"kelime": "souffle kabartmak", "aciklama": "fırında pişen çikolatalı sufle kabının kenarından yukarı 3 parmak dikine yükselmesi", "yasakli_kelimeler": ["souffle", "akışkan iç", "fırından yükselme", "sönmeden servis", "ramekin"], "zorluk": "zor"},
    {"kelime": "tulumba şerbeti soğutmak", "aciklama": "çıtır tulumbanın yumuşamaması için kaynar hamuru buz gibi yoğun şerbete şoklamak", "yasakli_kelimeler": ["termal şoklama", "soğuk şerbet", "çıtır kalma", "yumuşamama", "yoğun kıvam"], "zorluk": "zor"},
    {"kelime": "pate a choux pişirmek", "aciklama": "tereyağı ve unu tencerede kavurup yumurtaları tek tek yedirerek şu hamuru yapmak", "yasakli_kelimeler": ["choux hamuru", "tencerede pişirme", "ekler bazı", "boşluklu iç", "yumurta yedirme"], "zorluk": "zor"},
    {"kelime": "ayna astar glazür dökmek", "aciklama": "jelatin, yoğunlaştırılmış süt ve çikolatalı sosu donmuş mousse pastaya ayna gibi dökmek", "yasakli_kelimeler": ["mirror glaze", "ayna sır", "yansıma", "donmuş mousse", "jelatinli parıltı"], "zorluk": "zor"},
    {"kelime": "krem brule pürmüzlemek", "aciklama": "vanilyalı fırın muhallebisinin üstündeki toz şekeri alev pürmüzüyle çıtır kabuk yapmak", "yasakli_kelimeler": ["crème brûlée", "pürmüz alevi", "çıtır şeker kabuğu", "kaşıkla kırma", "vanilya tanesi"], "zorluk": "zor"},
    {"kelime": "lokum kazanında bağlamak", "aciklama": "nişasta, şeker ve sitrik asidi açık kazanda saatlerce kürekle çevirip jelleştirmek", "yasakli_kelimeler": ["lokumculuk", "açık kazan", "nişasta bağı", "kürekle çevirme", "ağdalı kıvam"], "zorluk": "zor"},
    {"kelime": "cannoli kabuğu sarmak", "aciklama": "şaraplı sert hamuru metal borulara sarıp yağda kızartarak çıtır silindir boru yapmak", "yasakli_kelimeler": ["sicilya tatlısı", "metal boru kalıp", "ricotta dolgusu", "çıtır silindir", "kızartma"], "zorluk": "zor"}
]

tekstil_verbs = [
    # Kolay (12)
    {"kelime": "dokumak", "aciklama": "tezgahta atkı ve çözgü ipliklerini birbirine geçirip kumaş üretmek", "yasakli_kelimeler": ["tezgah", "iplik", "kumaş", "atkı", "çözgü"], "zorluk": "kolay"},
    {"kelime": "dikmek", "aciklama": "kesilen kumaş parçalarını dikiş makinesiyle birleştirip elbise yapmak", "yasakli_kelimeler": ["iğne", "iplik", "dikiş makinesi", "kumaş", "elbise"], "zorluk": "kolay"},
    {"kelime": "kesmek", "aciklama": "kumaşı makasla veya motorlu kesim bıçağıyla kalıba göre kesmek", "yasakli_kelimeler": ["makas", "kumaş", "kalıp", "parça", "biçmek"], "zorluk": "kolay"},
    {"kelime": "boyamak", "aciklama": "ham kumaşı veya ipliği boya kazanına sokup renklendirmek", "yasakli_kelimeler": ["renk", "boyahane", "kazan", "kumaş", "iplik"], "zorluk": "kolay"},
    {"kelime": "örmek", "aciklama": "şiş veya triko makinesiyle iplikten kazak veya süveter yapmak", "yasakli_kelimeler": ["triko", "şiş", "kazak", "ilmek", "iplik"], "zorluk": "kolay"},
    {"kelime": "ütülemek", "aciklama": "üretilen konfeksiyon ürünlerini sanayi ütüsüyle düzeltip pürüzsüz yapmak", "yasakli_kelimeler": ["sanayi ütüsü", "buhar", "kırışık", "düzeltme", "paskaraya"], "zorluk": "kolay"},
    {"kelime": "katlamak", "aciklama": "dikilip ütülenen tişörtleri jelatin poşete koymadan önce katlamak", "yasakli_kelimeler": ["düzgün", "poşetleme", "tişört", "bükme", "kolileme"], "zorluk": "kolay"},
    {"kelime": "paketlemek", "aciklama": "hazır giyim ürünlerini jelatinleyip ihracat kolilerine yerleştirmek", "yasakli_kelimeler": ["koli", "ihracat", "jelatin", "poşet", "sevkiyat"], "zorluk": "kolay"},
    {"kelime": "sarmak", "aciklama": "iplik fabrikasında üretilen pamuk iplerini büyük bobinlere dolamak", "yasakli_kelimeler": ["bobin", "makara", "dolama", "iplik", "pamuk"], "zorluk": "kolay"},
    {"kelime": "ölçmek", "aciklama": "kumaşın enini, boyunu ve gramajını metreyle ve teraziyle denetlemek", "yasakli_kelimeler": ["metre", "gramaj", "en boy", "kumaş", "kontrol"], "zorluk": "kolay"},
    {"kelime": "yırtmak", "aciklama": "kumaş topunun kenarını makasla çentip elle boydan boya ayırmak", "yasakli_kelimeler": ["ayırmak", "koparmak", "kumaş topu", "elle", "çentik"], "zorluk": "kolay"},
    {"kelime": "temizlemek", "aciklama": "dikim sonrası kumaş üzerindeki dikiş iplik artıklarını makasla kırpmak", "yasakli_kelimeler": ["iplik temizleme", "artık", "kırpma", "küçük makas", "son kontrol"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "çözgü hazırlamak", "aciklama": "dokuma öncesi binlerce ipliği paralel olarak levent silindirine sarmak", "yasakli_kelimeler": ["levent", "paralel iplik", "dokuma hazırlık", "silindir", "bobin sehpasından"], "zorluk": "orta"},
    {"kelime": "mekik atmak", "aciklama": "dokuma tezgahında mekiğin çözgü iplikleri arasından hızla geçip atkı bırakması", "yasakli_kelimeler": ["mekik", "atkı ipliği", "ağızlık", "sağa sola", "tık tak"], "zorluk": "orta"},
    {"kelime": "iplik eğirmek", "aciklama": "ham pamuk veya yün elyafını bükerek ince dayanıklı iplik haline getirmek", "yasakli_kelimeler": ["büküm", "elyaf", "iğ", "pamuk", "iplikhane"], "zorluk": "orta"},
    {"kelime": "ramözden geçirmek", "aciklama": "ıslak kumaşı iğneli zincirlerle gerdirip sıcak hava tünelinde enini sabitlemek", "yasakli_kelimeler": ["kurutma tüneli", "en sabitleme", "iğneli zincir", "apre", "ramöz"], "zorluk": "orta"},
    {"kelime": "sanforize etmek", "aciklama": "kumaşın yıkandığında çekmesini önlemek için kauçuk blanketle önceden çektirmek", "yasakli_kelimeler": ["çekmezlik", "boyutsal kararlılık", "yıkama payı", "blanket", "mekanik apre"], "zorluk": "orta"},
    {"kelime": "jakar kartı okutmak", "aciklama": "kendinden kabartmalı desenli kumaş için jakar kafesindeki iğneleri programlamak", "yasakli_kelimeler": ["jakarlı dokuma", "kendinden desenli", "iğne seçimi", "döşemelik kumaş", "tezgah"], "zorluk": "orta"},
    {"kelime": "baskı yapmak", "aciklama": "rotasyon veya dijital baskı makinesiyle kumaş yüzeyine desenli boya basmak", "yasakli_kelimeler": ["rotasyon baskı", "dijital kumaş baskısı", "şablon", "renkli desen", "fikse"], "zorluk": "orta"},
    {"kelime": "kumaş topu açmak", "aciklama": "kesim masasına 50 kat kumaşı serici makineyle üst üste sermek", "yasakli_kelimeler": ["serim masası", "pastal", "kumaş katı", "otomatik serici", "kesim öncesi"], "zorluk": "orta"},
    {"kelime": "pastal çizmek", "aciklama": "kumaş firesini sıfırlamak için giysi kalıplarını en verimli şekilde bilgisayarda dizmek", "yasakli_kelimeler": ["fire engelleme", "kalıp yerleşimi", "verimlilik", "marker", "kesim planı"], "zorluk": "orta"},
    {"kelime": "overlok dikmek", "aciklama": "kumaş kenarlarının iplik atıp sökülmemesi için 4 iplikli bıçaklı dikiş geçmek", "yasakli_kelimeler": ["sökülme önleme", "kenar dikişi", "bıçaklı makine", "4 iplik", "kumaş kenarı"], "zorluk": "orta"},
    {"kelime": "reçme çekmek", "aciklama": "tişört etek ve kol uçlarına çift iğneli esnek reçme dikişi vurmak", "yasakli_kelimeler": ["çift iğne", "etek ucu", "esnek dikiş", "tişört kolu", "örgü kumaş"], "zorluk": "orta"},
    {"kelime": "ilik açmak", "aciklama": "otomatik ilik makinesinde ceket ve gömlek kumaşını kesip etrafını sarmak", "yasakli_kelimeler": ["düğme iliği", "gözlü ilik", "otomatik makine", "gömlek önü", "kesme"], "zorluk": "orta"},
    {"kelime": "düğme dikmek", "aciklama": "ayaklı düğme dikme otomatıyla saniyeler içinde düğmeyi kumaşa çakmak", "yasakli_kelimeler": ["düğme otomatı", "iplik düğüm", "kıyafet", "hızlı dikim", "çakma"], "zorluk": "orta"},
    {"kelime": "tela yapıştırmak", "aciklama": "yaka ve manşetlerin dik durması için pres makinesinde ısıyla yapışkan astar basmak", "yasakli_kelimeler": ["yapışkan tela", "sıcak pres", "yaka sertleştirme", "manşet", "eriyen astar"], "zorluk": "orta"},
    {"kelime": "lazerle kesmek", "aciklama": "sentetik kumaşları kenarları sökülmesin diye yüksek güçlü lazer ışınıyla yakarak kesmek", "yasakli_kelimeler": ["lazer başlığı", "yakıcı kesim", "sökülmez kenar", "otomasyon", "sentetik"], "zorluk": "orta"},
    {"kelime": "penye iplik üretmek", "aciklama": "tarama makinesinde kısa pamuk liflerini ayıklayıp sadece en uzun ve kaliteli lifleri bükmek", "yasakli_kelimeler": ["tarama makinesi", "combing", "uzun pamuk lifi", "kaliteli penye", "karde zıttı"], "zorluk": "orta"},
    {"kelime": "karde iplik bükmek", "aciklama": "taranmamış standart pamuk elyafından daha pütürlü ve ucuz iplik üretmek", "yasakli_kelimeler": ["taranmamış", "kısa lifler", "standart pamuk", "pütürlü", "ucuz iplik"], "zorluk": "orta"},
    {"kelime": "elyaf harmanlamak", "aciklama": "balyalar halindeki farklı kalite pamuk ve polyester elyaflarını homojen karıştırmak", "yasakli_kelimeler": ["balya", "harman hallaç", "polyester pamuk", "karışım", "elyaf açma"], "zorluk": "orta"},
    {"kelime": "fitil çekmek", "aciklama": "tarak şeridini çekme makinesinde inceltip büküme hazır fitil makaralarına sarmak", "yasakli_kelimeler": ["çekme makinesi", "inceltme", "şerit", "fitil makarası", "cer makinesi"], "zorluk": "orta"},
    {"kelime": "fikse etmek", "aciklama": "boyanmış ve basılmış kumaşı yüksek sıcaklıklı doymuş buhar kazanında sabitlemek", "yasakli_kelimeler": ["buhar fiksajı", "boya sabitleme", "yıkama haslığı", "doymuş buhar", "kazan"], "zorluk": "orta"},
    {"kelime": "kumaş kalite kontrol", "aciklama": "ışıklı kontrol masasından metrelerce akan kumaştaki dokuma hatalarını işaretlemek", "yasakli_kelimeler": ["ışıklı masa", "dokuma hatası", "iplik kopuğu", "kumaş metresi", "etiketleme"], "zorluk": "orta"},
    {"kelime": "hidrofilize etmek", "aciklama": "ham pamuklu kumaşın üzerindeki doğal yağları arındırıp su emicilik kazandırmak", "yasakli_kelimeler": ["su emicilik", "havlu kumaş", "yağ arındırma", "kaynatma", "ön terbiye"], "zorluk": "orta"},
    {"kelime": "şardon çekmek", "aciklama": "dönen tel fırçalarla kumaş yüzeyindeki lifleri kaldırıp polar yumuşaklığı vermek", "yasakli_kelimeler": ["tüylendirme", "polar kumaş", "tel fırça", "şardonlama", "yumuşak yüzey"], "zorluk": "orta"},
    {"kelime": "boncuklanma testi yapmak", "aciklama": "martindale cihazında kumaşı sürterek yüzeyde tiftik ve tüylenme oluşumunu ölçmek", "yasakli_kelimeler": ["pilling", "tüylenme", "martindale", "sürtünme direnci", "tiftik"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "merserize işlemi uygulamak", "aciklama": "pamuk ipliğini gergin haldeyken kostik soda banyosuna sokup ipeksi parlaklık vermek", "yasakli_kelimeler": ["sodyum hidroksit", "kostik soda", "ipeksi parlaklık", "mukavemet artışı", "pamuk parlaklığı"], "zorluk": "zor"},
    {"kelime": "ring iplik eğirmek", "aciklama": "kopça ve bilezik sistemiyle fitili yüksek devirde döndürerek en mukavim ipliği bükmek", "yasakli_kelimeler": ["kopça bilezik", "yüksek mukavemet", "ring iplikçiliği", "iğ devri", "kaliteli büküm"], "zorluk": "zor"},
    {"kelime": "open-end rotor ipliği", "aciklama": "hava akımıyla açılan elyafları dönen yüksek hızlı rotorda merkezkaçla iplik yapmak", "yasakli_kelimeler": ["rotor iplik", "merkezkaç", "hızlı üretim", "hacimli iplik", "open end"], "zorluk": "zor"},
    {"kelime": "air-jet dokuma atmak", "aciklama": "yüksek basınçlı hava jeti püskürterek atkı ipliğini dakikada 1000 metre hızla karşıya fırlatmak", "yasakli_kelimeler": ["hava jeti", "yüksek hızlı dokuma", "dakikada 1000 metre", "kompresörlü atkı", "mekiksiz"], "zorluk": "zor"},
    {"kelime": "süprem kumaş örmek", "aciklama": "yuvarlak örme makinesinde tek plaka iğnelerle esnek ve ince tişört kumaşı üretmek", "yasakli_kelimeler": ["single jersey", "yuvarlak örme", "tek plaka", "tişört kumaşı", "ön yüz düz"], "zorluk": "zor"},
    {"kelime": "interlok örme yapmak", "aciklama": "çift plaka iğnelerin karşılıklı kilitlenmesiyle her iki yüzü de aynı pürüzsüz kumaş dokumak", "yasakli_kelimeler": ["çift plaka", "interlock", "ön arka aynı", "kalın örme", "kilitli ilmek"], "zorluk": "zor"},
    {"kelime": "yakma işlemi yapmak", "aciklama": "kumaşın yüzeyinden fırlayan tüyleri gaz alevinin üzerinden jet hızıyla geçirip yakmak", "yasakli_kelimeler": ["gazzeleme", "singeing", "tüy yakma", "gaz alevi", "pürüzsüz yüzey"], "zorluk": "zor"},
    {"kelime": "antistatik apre vermek", "aciklama": "sentetik kumaşların elektriklenmesini ve tozu çekmesini kimyasal kaplamayla önlemek", "yasakli_kelimeler": ["statik elektrik önleme", "kimyasal apre", "toz tutmaz", "sentetik lif", "iletken tabaka"], "zorluk": "zor"},
    {"kelime": "su itici florokarbon kaplamak", "aciklama": "kumaş liflerinin etrafına teflon benzeri nano bariyer kurup suyun damlalaşmasını sağlamak", "yasakli_kelimeler": ["su itici apre", "florokarbon", "dwr", "yağmur damlası", "ıslanmaz kumaş"], "zorluk": "zor"},
    {"kelime": "denye ve dtex hesaplamak", "aciklama": "9000 veya 10000 metre ipliğin gram ağırlığını ölçerek iplik inceliğini saptamak", "yasakli_kelimeler": ["iplik numarası", "9000 metre", "dtex", "iplik kalınlığı", "numaralandırma"], "zorluk": "zor"},
    {"kelime": "yıkama haslığı ölçmek", "aciklama": "boyalı kumaşın standart yıkama testinde beyaz beze ne kadar boya kustuğunu gri skalayla puanlamak", "yasakli_kelimeler": ["renk haslığı", "boya kusması", "gri skala", "yıkama testi", "lekeleme"], "zorluk": "zor"},
    {"kelime": "süblimasyon transferi basmak", "aciklama": "ısı ve basınçla katı mürekkebi doğrudan gaz fazına geçirip polyester liflerine hapsetmek", "yasakli_kelimeler": ["transfer baskı", "katıdan gaza", "polyester kumaş", "ısı presi", "kalıcı baskı"], "zorluk": "zor"},
    {"kelime": "kumaş gramajı tartmak", "aciklama": "dairesel numune kesiciyle tam 100 cm2 kumaş kesip hassas terazide g/m2 bulmak", "yasakli_kelimeler": ["gsm", "dairesel kesici", "100 cm2", "metrekare ağırlığı", "kumaş tartımı"], "zorluk": "zor"},
    {"kelime": "örme may dönmesini çözmek", "aciklama": "yuvarlak örme kumaşta yıkama sonrası yan dikişlerin öne doğru kaymasını engellemek", "yasakli_kelimeler": ["may dönmesi", "spirallik", "yan dikiş kayması", "büküm dengesizliği", "örme hatası"], "zorluk": "zor"}
]

if __name__ == "__main__":
    add_and_save_verbs("tatlilar", tatlilar_verbs)
    add_and_save_verbs("tekstil", tekstil_verbs)
