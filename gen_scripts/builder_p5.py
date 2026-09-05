import os, sys, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gen_scripts.card_utils import add_and_save_verbs

# 9. etnografi
etnografi_verbs = [
    # Kolay (12)
    {"kelime": "gelenekleri öğrenmek", "yasakli_kelimeler": ["adet", "kültür", "görenek", "toplum", "yaşayış"], "zorluk": "kolay", "aciklama": "Bir topluluğun kuşaktan kuşağa aktardığı adetleri tanımak."},
    {"kelime": "köy ziyaret etmek", "yasakli_kelimeler": ["kırsal", "halk", "ev", "gezi", "misafir"], "zorluk": "kolay", "aciklama": "Kırsal yerleşim yerindeki insanların arasına gidip görmek."},
    {"kelime": "masal dinlemek", "yasakli_kelimeler": ["anlatıcı", "yaşlı", "hikaye", "efsane", "sözlü"], "zorluk": "kolay", "aciklama": "Köy veya topluluk büyüklerinin anlattığı halk masallarını işitmek."},
    {"kelime": "yöresel yemek tatmak", "yasakli_kelimeler": ["mutfak", "lezzet", "kültür", "tat", "geleneksel"], "zorluk": "kolay", "aciklama": "Bölgeye özgü geleneksel yemekleri deneyimlemek."},
    {"kelime": "not tutmak", "yasakli_kelimeler": ["defter", "kalem", "yazmak", "kayıt", "gözlem"], "zorluk": "kolay", "aciklama": "Sahada gördüklerini ve duyduklarını deftere kaydetmek."},
    {"kelime": "halk oyunu izlemek", "yasakli_kelimeler": ["halay", "zeybek", "dans", "folklor", "ritim"], "zorluk": "kolay", "aciklama": "Geleneksel halk danslarının icrasını seyretmek."},
    {"kelime": "kilim dokumak", "yasakli_kelimeler": ["tezgah", "motif", "ip", "yün", "halı"], "zorluk": "kolay", "aciklama": "Yöresel tezgahlarda yün iplerle desenli yaygı üretmek."},
    {"kelime": "düğüne katılmak", "yasakli_kelimeler": ["tören", "gelin", "damat", "kutlama", "adet"], "zorluk": "kolay", "aciklama": "Geleneksel evlilik merasiminde bulunup ritüelleri görmek."},
    {"kelime": "halk ozanını dinlemek", "yasakli_kelimeler": ["aşık", "bağlama", "türkü", "saz", "söz"], "zorluk": "kolay", "aciklama": "Geleneksel saz şairlerinin atışmalarını ve türkülerini işitmek."},
    {"kelime": "fotoğraf çekmek", "yasakli_kelimeler": ["kamera", "görüntü", "belge", "insan", "arşiv"], "zorluk": "kolay", "aciklama": "Saha araştırmasındaki kültürel anları görsel olarak kaydetmek."},
    {"kelime": "röportaj yapmak", "yasakli_kelimeler": ["mülakat", "soru", "söyleşi", "kayıt", "konuşmak"], "zorluk": "kolay", "aciklama": "Kaynak kişilerle yüz yüze soru-cevap söyleşisi gerçekleştirmek."},
    {"kelime": "yerel dili anlamak", "yasakli_kelimeler": ["şive", "ağız", "lehçe", "konuşma", "kelime"], "zorluk": "kolay", "aciklama": "Bölge halkının kullandığı yerel ağız ve deyimleri kavramak."},

    # Orta (24)
    {"kelime": "katılımcı gözlem yapmak", "yasakli_kelimeler": ["birlikte yaşamak", "saha", "araştırmacı", "malinowski", "içeriden"], "zorluk": "orta", "aciklama": "Topluluğun içine girip onlarla birlikte yaşayarak gözlemde bulunmak."},
    {"kelime": "saha çalışması yürütmek", "yasakli_kelimeler": ["alan araştırması", "topluluk", "gözlem", "anket", "araştırmacı"], "zorluk": "orta", "aciklama": "Veri toplamak amacıyla bizzat çalışılan coğrafyada bulunmak."},
    {"kelime": "derinlemesine mülakat yapmak", "yasakli_kelimeler": ["nitel görüşme", "kaynak kişi", "yarı yapılandırılmış", "ses kaydı", "soru"], "zorluk": "orta", "aciklama": "Kaynak kişiyle uzun süreli ve detaylı sözlü görüşme yapmak."},
    {"kelime": "sözlü tarih kaydetmek", "yasakli_kelimeler": ["ses alma", "hafıza", "yaşlılar", "tanıklık", "arşiv"], "zorluk": "orta", "aciklama": "Geçmiş olayların tanıklarının anlattıklarını sesli veya görüntülü belgelemek."},
    {"kelime": "kültürel ritüeli belgelemek", "yasakli_kelimeler": ["ayin", "tören", "gelenek", "kurban", "bayram"], "zorluk": "orta", "aciklama": "Topluluk için simgesel değeri olan törensel uygulamaları kayıt altına almak."},
    {"kelime": "akrabalık bağlarını çıkarmak", "yasakli_kelimeler": ["soy", "şecere", "klan", "kabile", "soy ağacı"], "zorluk": "orta", "aciklama": "Topluluktaki hısımlık ve sülale ilişkilerini şematize etmek."},
    {"kelime": "saha günlüğü tutmak", "yasakli_kelimeler": ["not defteri", "günlük", "etnograf", "izlenim", "tarih"], "zorluk": "orta", "aciklama": "Sahadaki her günün olaylarını ve kişisel gözlemlerini günü gününe yazmak."},
    {"kelime": "kültürel görelilik gözetmek", "yasakli_kelimeler": ["yargılamama", "kendi bağlamında", "tarafsız", "değer", "önyargısız"], "zorluk": "orta", "aciklama": "İncelenen kültürü kendi iç dinamikleri ve değerleriyle değerlendirmek."},
    {"kelime": "etnik kökeni araştırmak", "yasakli_kelimeler": ["soy", "halk", "köken", "tarih", "kimlik"], "zorluk": "orta", "aciklama": "Bir topluluğun tarihsel soyunu ve kültürel aidiyetini incelemek."},
    {"kelime": "maddi kültür öğesi toplamak", "yasakli_kelimeler": ["alet", "kıyafet", "eşya", "el sanatı", "müze"], "zorluk": "orta", "aciklama": "Halkın günlük hayatta ürettiği somut araç ve giysileri derlemek."},
    {"kelime": "kaynak kişiyle görüşmek", "yasakli_kelimeler": ["enformatör", "yerel rehber", "bilgi veren", "mülakat", "yaşlı"], "zorluk": "orta", "aciklama": "Kültür hakkında yetkin bilgi sahibi yerel bireyle temas kurmak."},
    {"kelime": "ses kaydı almak", "yasakli_kelimeler": ["diktafon", "mikrofon", "türkü", "masal", "arşiv"], "zorluk": "orta", "aciklama": "Ağıt, türkü veya anlatıları dijital ses kayıt cihazına aktarmak."},
    {"kelime": "yas ritüelini izlemek", "yasakli_kelimeler": ["cenaze", "ağıt", "taziye", "tören", "ölüm"], "zorluk": "orta", "aciklama": "Ölüm sonrası gerçekleştirilen toplumsal ağıt ve merasimleri incelemek."},
    {"kelime": "çeyiz geleneğini incelemek", "yasakli_kelimeler": ["sandık", "nakış", "düğün", "gelin", "hediye"], "zorluk": "orta", "aciklama": "Evlilik öncesi hazırlanan el emeği eşyaların kültürel anlamını analiz etmek."},
    {"kelime": "folklor derlemesi yapmak", "yasakli_kelimeler": ["mani", "atasözü", "bilmece", "derlemek", "halk kültürü"], "zorluk": "orta", "aciklama": "Yöredeki anonim halk edebiyatı ürünlerini bir araya getirmek."},
    {"kelime": "yerli halkla güven kurmak", "yasakli_kelimeler": ["rapor kurma", "samimiyet", "kabul görme", "diyalog", "saha"], "zorluk": "orta", "aciklama": "Araştırma yapılan cemaatin güvenini kazanarak kabul görmek."},
    {"kelime": "geçiş törenlerini incelemek", "yasakli_kelimeler": ["doğum", "sünnet", "evlilik", "ölüm", "aşama"], "zorluk": "orta", "aciklama": "Bireyin hayatındaki kritik dönüm noktalarında icra edilen ayinleri araştırmak."},
    {"kelime": "mitik anlatıları deşifre etmek", "yasakli_kelimeler": ["efsane", "köken miti", "inanç", "sembol", "çözümleme"], "zorluk": "orta", "aciklama": "Halk arasındaki kutsal veya doğaüstü hikayelerin simgesel anlamını çözmek."},
    {"kelime": "üretim tekniklerini kaydetmek", "yasakli_kelimeler": ["zanaat", "çömlek", "dokuma", "demir", "geleneksel"], "zorluk": "orta", "aciklama": "Geleneksel el sanatlarının yapılış aşamalarını aşama aşama kayda geçirmek."},
    {"kelime": "beden dillerini yorumlamak", "yasakli_kelimeler": ["jest", "mimik", "iletişim", "kültür", "davranış"], "zorluk": "orta", "aciklama": "Kültüre özgü selamlaşma ve vücut hareketlerinin manasını çözmek."},
    {"kelime": "kurban törenini gözlemlemek", "yasakli_kelimeler": ["adak", "kesim", "ritüel", "inanç", "paylaşım"], "zorluk": "orta", "aciklama": "Kutsal kabul edilen kurban sunma pratiklerini yerinde incelemek."},
    {"kelime": "büyüsel pratikleri incelemek", "yasakli_kelimeler": ["muska", "nazar", "ocak", "şifa", "ritüel"], "zorluk": "orta", "aciklama": "Halk hekimliği ve batıl inanış uygulamalarını kayıt altına almak."},
    {"kelime": "mekansal kullanım haritalamak", "yasakli_kelimeler": ["köy meydanı", "mahalle", "haremlik selamlık", "mekan", "sosyal alan"], "zorluk": "orta", "aciklama": "Topluluğun kamusal ve özel mekanları nasıl paylaştığını çizmek."},
    {"kelime": "halk takvimini çıkarmak", "yasakli_kelimeler": ["kocakarı soğuğu", "cemre", "hasat zamanı", "mevsim", "gelenek"], "zorluk": "orta", "aciklama": "Doğa olaylarına göre halkın belirlediği geleneksel takvimi derlemek."},

    # Zor (14)
    {"kelime": "yoğun betimleme yapmak", "yasakli_kelimeler": ["thick description", "geertz", "bağlam", "derinlik", "anlam"], "zorluk": "zor", "aciklama": "Bir eylemi sadece fiziksel olarak değil, içinde yer aldığı tüm kültürel bağlamıyla tarif etmek."},
    {"kelime": "emik bakış açısı yakalamak", "yasakli_kelimeler": ["içeriden bakış", "yerlinin gözü", "etik karşıtı", "anlam dünyası", "kültür"], "zorluk": "zor", "aciklama": "Olayları topluluğun kendi üyelerinin kavradığı ve hissettiği pencereden anlamak."},
    {"kelime": "etik perspektiften analiz etmek", "yasakli_kelimeler": ["dışarıdan bakış", "bilimsel kategori", "araştırmacı gözü", "emik karşıtı", "nesnel"], "zorluk": "zor", "aciklama": "Kültürel verileri evrensel bilimsel kavramlar ve dış gözlemci kategorileriyle açıklamak."},
    {"kelime": "otoetnografi yazmak", "yasakli_kelimeler": ["kendi deneyimi", "araştırmacı benliği", "biyografi", "özdüşünümsellik", "anlatı"], "zorluk": "zor", "aciklama": "Araştırmacının kendi kişisel ve kültürel deneyimini etnografik analiz nesnesi yapması."},
    {"kelime": "etnosentrizmden kaçınmak", "yasakli_kelimeler": ["kendi kültürünü üstün görme", "önyargı", "merkezcilik", "kültürel körlük", "tarafsızlık"], "zorluk": "zor", "aciklama": "Diğer kültürleri kendi kültürünün kalıplarıyla yargılamaktan sakınmak."},
    {"kelime": "dijital etnografi yürütmek", "yasakli_kelimeler": ["netnografi", "sanal cemaat", "sosyal medya", "çevrimiçi saha", "internet"], "zorluk": "zor", "aciklama": "İnternet ve sosyal medya topluluklarının kültürel pratiklerini sahada incelemek."},
    {"kelime": "özdüşünümsellik sergilemek", "yasakli_kelimeler": ["refleksivite", "araştırmacı etkisi", "konumsallık", "tarafsızlık", "farkındalık"], "zorluk": "zor", "aciklama": "Araştırmacının kendi cinsiyet, sınıf ve kimliğinin sahaya etkisini eleştirel sorgulaması."},
    {"kelime": "sembolik antropoloji uygulamak", "yasakli_kelimeler": ["geertz", "turner", "simge", "kültürel kod", "yorum"], "zorluk": "zor", "aciklama": "Kültürü insanların dünyayı anlamlandırmak için ördükleri bir semboller ağı olarak yorumlamak."},
    {"kelime": "yapısalcı çözümleme yapmak", "yasakli_kelimeler": ["levi strauss", "ikili karşıtlıklar", "mit yapısı", "akrabalık", "derin yapı"], "zorluk": "zor", "aciklama": "Kültürel unsurların arkasındaki evrensel bilinçdışı zihinsel yapıları ve ikilikleri bulmak."},
    {"kelime": "kültürleşme sürecini izlemek", "yasakli_kelimeler": ["akkültürasyon", "kültür değişimi", "etkileşim", "baskın kültür", "dönüşüm"], "zorluk": "zor", "aciklama": "İki farklı kültürün karşılaşması sonucu ortaya çıkan karşılıklı değişim sürecini izlemek."},
    {"kelime": "hegemonik söylemi sorgulamak", "yasakli_kelimeler": ["gramsci", "güç ilişkileri", "baskı", "sömürgecilik", "temsil"], "zorluk": "zor", "aciklama": "Egemen gücün dili ve kültürel anlatısının topluluk üzerindeki baskısını ifşa etmek."},
    {"kelime": "etnobotanik derleme yapmak", "yasakli_kelimeler": ["şifalı bitki", "halk ilacı", "otlar", "yerel bilgi", "tedavi"], "zorluk": "zor", "aciklama": "Yerel halkın yabani bitkileri tıbbi ve beslenme amaçlı kullanım bilgisini derlemek."},
    {"kelime": "görsel etnografi yöntemi kullanmak", "yasakli_kelimeler": ["antropolojik belgesel", "kamera", "film", "foto-etnografi", "görüntü"], "zorluk": "zor", "aciklama": "Saha araştırmasını fotoğraf ve belgesel sinema teknikleriyle bütünleştirmek."},
    {"kelime": "kabile içi tabuyu çözümlemek", "yasakli_kelimeler": ["yasak", "totem", "dokunulmaz", "kutsal", "korku"], "zorluk": "zor", "aciklama": "Topluluğun çiğnenmesini felaket saydığı kutsal yasakların sosyal işlevini açıklamak."}
]

# 10. evcilhayvanlar
evcilhayvanlar_verbs = [
    # Kolay (12)
    {"kelime": "köpek gezdirmek", "yasakli_kelimeler": ["tasma", "yürüyüş", "park", "dolaşmak", "dışarı"], "zorluk": "kolay", "aciklama": "Köpeği tasmasıyla açık havada dolaştırmak."},
    {"kelime": "kedi sevmek", "yasakli_kelimeler": ["okşamak", "tüy", "mırıldamak", "pati", "kucak"], "zorluk": "kolay", "aciklama": "Kediye el ile şefkat gösterip tüylerini okşamak."},
    {"kelime": "mama vermek", "yasakli_kelimeler": ["kap", "yem", "beslemek", "kuru", "öğün"], "zorluk": "kolay", "aciklama": "Evcil hayvanın kabına yiyecek koymak."},
    {"kelime": "su doldurmak", "yasakli_kelimeler": ["içmek", "kap", "taze", "susuzluk", "kase"], "zorluk": "kolay", "aciklama": "Evcil hayvanın su kabını taze suyla doldurmak."},
    {"kelime": "kum temizlemek", "yasakli_kelimeler": ["kürek", "kedi tuvaleti", "kaka", "kristal", "değiştirmek"], "zorluk": "kolay", "aciklama": "Kedi kumundaki dışkıları kürekle arındırmak."},
    {"kelime": "tüylerini taramak", "yasakli_kelimeler": ["fırça", "dökülmek", "bakım", "tarak", "düğüm"], "zorluk": "kolay", "aciklama": "Hayvanın dökülen tüylerini fırça yardımıyla toplamak."},
    {"kelime": "top atmak", "yasakli_kelimeler": ["oyun", "fırlatmak", "yakalamak", "köpek", "koşmak"], "zorluk": "kolay", "aciklama": "Köpeğin yakalaması için oyun topunu uzağa fırlatmak."},
    {"kelime": "veterinere götürmek", "yasakli_kelimeler": ["doktor", "klinik", "muayene", "hasta", "aşı"], "zorluk": "kolay", "aciklama": "Hayvanı sağlık kontrolü için kliniğe taşımak."},
    {"kelime": "banyo yaptırmak", "yasakli_kelimeler": ["yıkamak", "şampuan", "su", "kurulamak", "köpek"], "zorluk": "kolay", "aciklama": "Kirlenen evcil hayvanı su ve şampuanla yıkamak."},
    {"kelime": "kafesi temizlemek", "yasakli_kelimeler": ["kuş", "hamster", "talaş", "tel", "arındırmak"], "zorluk": "kolay", "aciklama": "Kuş veya kemirgen kafesinin tabanını hijyenik hale getirmek."},
    {"kelime": "ödül maması vermek", "yasakli_kelimeler": ["ödül", "bisküvi", "eğitim", "aferin", "lezzet"], "zorluk": "kolay", "aciklama": "Doğru bir davranış yaptığında hayvana lezzetli ödül vermek."},
    {"kelime": "pati uzatmak", "yasakli_kelimeler": ["el sıkışmak", "komut", "köpek", "ayak", "selam"], "zorluk": "kolay", "aciklama": "Köpeğin sahibinin eline ayağını koyması."},

    # Orta (24)
    {"kelime": "tuvalet eğitimi vermek", "yasakli_kelimeler": ["ped", "çiş", "öğretmek", "dışarı", "kural"], "zorluk": "orta", "aciklama": "Yavru köpeğe ihtiyacını doğru yere yapmasını öğretmek."},
    {"kelime": "tasma takmak", "yasakli_kelimeler": ["kayış", "boyun", "göğüs tasması", "bağlamak", "güvenlik"], "zorluk": "orta", "aciklama": "Dışarı çıkmadan önce hayvanın boynuna veya göğsüne aparat geçirmek."},
    {"kelime": "tırmalama tahtası almak", "yasakli_kelimeler": ["kedi", "tırnak", "koltuk", "törpü", "ip"], "zorluk": "orta", "aciklama": "Kedinin tırnaklarını bilemesi ve mobilyalara zarar vermemesi için aparat sağlamak."},
    {"kelime": "pire damlası damlatmak", "yasakli_kelimeler": ["kene", "ense", "parazit", "ilaç", "dış parazit"], "zorluk": "orta", "aciklama": "Ense bölgesine parazitleri engelleyici tıbbi solüsyon uygulamak."},
    {"kelime": "aşı takvimini takip etmek", "yasakli_kelimeler": ["kuduz", "karma", "veteriner", "kart", "tarih"], "zorluk": "orta", "aciklama": "Hayvanın dönemsel aşılarının zamanını geciktirmeden yaptırmak."},
    {"kelime": "tırnak kesmek", "yasakli_kelimeler": ["makas", "pati", "uzamak", "damar", "kısaltmak"], "zorluk": "orta", "aciklama": "Pati tırnaklarını kanatmadan uygun boyda budamak."},
    {"kelime": "mikroçip taktırmak", "yasakli_kelimeler": ["deri altı", "kimlik", "kayıp", "kayıt", "veteriner"], "zorluk": "orta", "aciklama": "Deri altına kimlik ve sahip bilgilerini içeren elektronik çip taktırmak."},
    {"kelime": "kısırlaştırmak", "yasakli_kelimeler": ["operasyon", "üreme", "ameliyat", "anestezi", "çiftleşme"], "zorluk": "orta", "aciklama": "Hayvanın üreme yeteneğini cerrahi müdahaleyle sonlandırmak."},
    {"kelime": "temel itaat eğitimi vermek", "yasakli_kelimeler": ["otur", "kalk", "bekle", "komut", "köpek"], "zorluk": "orta", "aciklama": "Köpeğe 'otur', 'yat', 'gel' gibi temel yönlendirmeleri öğretmek."},
    {"kelime": "taşıma çantasına koymak", "yasakli_kelimeler": ["box", "fermuar", "yolculuk", "kedi", "veteriner"], "zorluk": "orta", "aciklama": "Seyahat veya klinik için hayvanı güvenli taşıma kafesine almak."},
    {"kelime": "yaş mama ikram etmek", "yasakli_kelimeler": ["konserve", "püre", "soslu", "lezzetli", "açmak"], "zorluk": "orta", "aciklama": "Kuru mamaya ek olarak konserve lezzetli yemek vermek."},
    {"kelime": "kulak temizliği yapmak", "yasakli_kelimeler": ["kir", "solüsyon", "pamuk", "enfeksiyon", "koku"], "zorluk": "orta", "aciklama": "Kulak kepçesi ve kanalındaki kirleri özel losyonla arındırmak."},
    {"kelime": "diş fırçalamak", "yasakli_kelimeler": ["macun", "tartar", "ağız kokusu", "diş eti", "bakım"], "zorluk": "orta", "aciklama": "Ağızda plak ve tartar oluşumunu önlemek için dişleri temizlemek."},
    {"kelime": "kilo takibi yapmak", "yasakli_kelimeler": ["tartı", "obezite", "diyet", "gram", "sağlık"], "zorluk": "orta", "aciklama": "Hayvanın aşırı kilo almasını önlemek için tartım yapmak."},
    {"kelime": "akvaryum suyunu değiştirmek", "yasakli_kelimeler": ["balık", "filtre", "dip çekimi", "klor", "temizlik"], "zorluk": "orta", "aciklama": "Akvaryumdaki kirlenmiş suyun bir kısmını taze dinlenmiş suyla yenilemek."},
    {"kelime": "kuş tüneği yerleştirmek", "yasakli_kelimeler": ["tahta", "kafes", "ayak", "muhabbet kuşu", "tünemek"], "zorluk": "orta", "aciklama": "Kuşun rahat konabilmesi için kafese ahşap çubuk takmak."},
    {"kelime": "oyuncak almak", "yasakli_kelimeler": ["peluş", "sesli", "kemirme", "fare", "oyun"], "zorluk": "orta", "aciklama": "Evcil hayvanın can sıkıntısını giderecek nesneler temin etmek."},
    {"kelime": "sahiplenmek", "yasakli_kelimeler": ["barınak", "satın alma", "yuva", "evlat", "bakmak"], "zorluk": "orta", "aciklama": "Barınaktan veya sokaktan bir hayvanı eve alıp bakımını üstlenmek."},
    {"kelime": "tasmasını gevşetmek", "yasakli_kelimeler": ["sıkmak", "boyun", "rahatlatmak", "nefes", "ayar"], "zorluk": "orta", "aciklama": "Boynu sıkan tasma bandını iki parmak girecek şekilde bollaştırmak."},
    {"kelime": "kemirme kemiği vermek", "yasakli_kelimeler": ["pres", "diş", "köpek", "oyalanmak", "kalsiyum"], "zorluk": "orta", "aciklama": "Köpeğin dişlerini kaşıması ve oyalanması için pres kemik vermek."},
    {"kelime": "kedi nanesi koklatmak", "yasakli_kelimeler": ["catnip", "neşe", "ot", "oyun", "uyarıcı"], "zorluk": "orta", "aciklama": "Kediyi neşelendiren ve rahatlatan aromatik otu denetmek."},
    {"kelime": "sosyalleştirmek", "yasakli_kelimeler": ["diğer köpekler", "insanlar", "korku", "alıştırmak", "park"], "zorluk": "orta", "aciklama": "Yavruyu farklı insan ve hayvanlara alıştırarak hırçınlaşmasını önlemek."},
    {"kelime": "tüy yumağı önleyici macun vermek", "yasakli_kelimeler": ["malt", "kedi", "kusma", "mide", "sindirim"], "zorluk": "orta", "aciklama": "Yalanırken yutulan tüylerin bağırsaktan atılmasını sağlayan macun yedirmek."},
    {"kelime": "göz çapağını silmek", "yasakli_kelimeler": ["pamuk", "akıntı", "gözyaşı", "ılık su", "temizleme"], "zorluk": "orta", "aciklama": "Göz kenarında biriken kurumuş salgıları nazikçe temizlemek."},

    # Zor (14)
    {"kelime": "klikır ile koşullandırmak", "yasakli_kelimeler": ["clicker", "pozitif pekiştirme", "ses", "ödül", "işaret"], "zorluk": "zor", "aciklama": "Mekanik klik sesiyle doğru davranışı işaretleyip ödülle pekiştirmek."},
    {"kelime": "tahılsız diyete geçirmek", "yasakli_kelimeler": ["grain free", "alerji", "yüksek protein", "karbonhidrat", "mama"], "zorluk": "zor", "aciklama": "Sindirim veya deri hassasiyeti olan hayvana tahıl içermeyen mama seçmek."},
    {"kelime": "iç parazit hapı yutturmak", "yasakli_kelimeler": ["tenya", "kurt", "boğaz", "hap", "üç ayda bir"], "zorluk": "zor", "aciklama": "Bağırsak kurtlarını dökmek için hapı hayvanın boğazına yerleştirip yutturmak."},
    {"kelime": "feromon difüzörü takmak", "yasakli_kelimeler": ["feliway", "adaptil", "stres", "koku", "sakinleştirici"], "zorluk": "zor", "aciklama": "Sentetik sakinleştirici koku yayan elektrikli cihazla stresi azaltmak."},
    {"kelime": "ayrılık kaygısını rehabilite etmek", "yasakli_kelimeler": ["yalnız kalamama", "havlama", "kapı tırmalama", "anksiyete", "davranış"], "zorluk": "zor", "aciklama": "Evde yalnız bırakıldığında panikleyen hayvanın kaygı düzeyini terapilerle düşürmek."},
    {"kelime": "deri kazıntısı örneği aldırmak", "yasakli_kelimeler": ["uyuz", "mantar", "mikroskop", "kaşıntı", "biyopsi"], "zorluk": "zor", "aciklama": "Deri lezyonunun mikroskobik teşhisi için cerrahi bisturiyle kazıntı aldırmak."},
    {"kelime": "barf diyeti hazırlamak", "yasakli_kelimeler": ["çiğ besleme", "kemikli et", "organ", "doğal", "dondurucu"], "zorluk": "zor", "aciklama": "Evcil hayvana çiğ et, kemik ve sebzeden oluşan ev yapımı taze rasyon hazırlamak."},
    {"kelime": "kaynak koruma saldırganlığını çözmek", "yasakli_kelimeler": ["mama kıskanma", "hırlama", "ısırık", "oyuncak", "desensitizasyon"], "zorluk": "zor", "aciklama": "Köpeğin mama veya oyuncağı sahibinden kıskanıp hırlama refleksini kırmak."},
    {"kelime": "ileri düzey çeviklik eğitimi yaptırmak", "yasakli_kelimeler": ["agility", "parkur", "tünel", "slalom", "engel atlama"], "zorluk": "zor", "aciklama": "Köpeği engeller, tüneller ve slalom çubuklarından oluşan parkurda yarıştırmak."},
    {"kelime": "hipoalerjenik bakım uygulamak", "yasakli_kelimeler": ["alerjen", "özel şampuan", "tüy dökülmesi", "dermatit", "reaksiyon"], "zorluk": "zor", "aciklama": "Alerjik reaksiyonlara yatkın hayvanın deri bariyerini özel medikal ürünlerle onarmak."},
    {"kelime": "anal kese boşalttırmak", "yasakli_kelimeler": ["veteriner", "kızaklama", "iltihap", "koku bezi", "rektal"], "zorluk": "zor", "aciklama": "Tıkanan anüs yanı koku bezlerinin biriken salgısını hekime sıktırmak."},
    {"kelime": "hedef çubuk ile yönlendirmek", "yasakli_kelimeler": ["target stick", "burun dokundurma", "pozitif eğitim", "yön", "komut"], "zorluk": "zor", "aciklama": "Köpeğin burnunu hedef aparatına dokundurarak belirli rotalara yönelmesini sağlamak."},
    {"kelime": "serum fizyolojik ile göz yıkamak", "yasakli_kelimeler": ["konjonktivit", "tuzlu su", "damla", "göz temizliği", "steril"], "zorluk": "zor", "aciklama": "Göz enfeksiyonunda steril tuzlu suyla göz yüzeyini yıkayıp arındırmak."},
    {"kelime": "postoperatif yakalık takmak", "yasakli_kelimeler": ["elizabeth tasması", "huni", "dikiş yalama", "yara", "koruma"], "zorluk": "zor", "aciklama": "Ameliyat dikişlerini yalamaması için hayvanın kafasına koni şeklinde huni takmak."}
]

add_and_save_verbs('etnografi', etnografi_verbs)
add_and_save_verbs('evcilhayvanlar', evcilhayvanlar_verbs)
print('P5 done!')
