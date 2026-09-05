import os, sys, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gen_scripts.card_utils import add_and_save_verbs

# 5. epigrafi
epigrafi_verbs = [
    # Kolay (12)
    {"kelime": "taş oymak", "yasakli_kelimeler": ["keski", "çekiç", "mermer", "şekil", "heykel"], "zorluk": "kolay", "aciklama": "Taş veya mermer üzerine aletlerle şekil ve yazı işlemek."},
    {"kelime": "yazıt okumak", "yasakli_kelimeler": ["kitabe", "harf", "tarih", "anıt", "eski"], "zorluk": "kolay", "aciklama": "Taş veya anıt üzerindeki tarihi yazıları çözümlemek."},
    {"kelime": "harf kazımak", "yasakli_kelimeler": ["yazı", "keski", "taş", "metal", "çizmek"], "zorluk": "kolay", "aciklama": "Sert bir yüzeyin üzerine harfleri kazıyarak yazmak."},
    {"kelime": "müzede sergilemek", "yasakli_kelimeler": ["tarihi eser", "vitrin", "ziyaretçi", "kitabe", "stela"], "zorluk": "kolay", "aciklama": "Bulunan tarihi taş eserleri sergi salonunda göstermek."},
    {"kelime": "kitabe incelemek", "yasakli_kelimeler": ["yazıt", "çeviri", "tarih", "bina", "duvar"], "zorluk": "kolay", "aciklama": "Bir yapının girişindeki veya anıttaki yazıyı tetkik etmek."},
    {"kelime": "mezar taşı okumak", "yasakli_kelimeler": ["kabir", "ölüm", "tarih", "isim", "dua"], "zorluk": "kolay", "aciklama": "Mezar üzerindeki kimlik ve tarih yazısını okumak."},
    {"kelime": "tarihi belgelemek", "yasakli_kelimeler": ["kayıt", "arşiv", "yazı", "olay", "geçmiş"], "zorluk": "kolay", "aciklama": "Geçmişte yaşanan olayları yazılı taşlarla kayıt altına almak."},
    {"kelime": "arkeolojik kazı yapmak", "yasakli_kelimeler": ["toprak", "kürek", "fırça", "antik", "buluntu"], "zorluk": "kolay", "aciklama": "Yerin altındaki taş yazıtları ve kalıntıları gün ışığına çıkarmak."},
    {"kelime": "çatlakları onarmak", "yasakli_kelimeler": ["yapıştırıcı", "tamir", "taş", "kırık", "koruma"], "zorluk": "kolay", "aciklama": "Hasar görmüş taş yazıtın kırık parçalarını birleştirmek."},
    {"kelime": "yazıyı fotoğraflamak", "yasakli_kelimeler": ["kamera", "ışık", "belge", "çekim", "arşiv"], "zorluk": "kolay", "aciklama": "Yazıtın net görüntüsünü fotoğraf makinesiyle kaydetmek."},
    {"kelime": "antik kenti gezmek", "yasakli_kelimeler": ["harabe", "sütun", "ziyaret", "roma", "yunan"], "zorluk": "kolay", "aciklama": "Eski çağlardan kalan harabeler arasındaki yazıtları yerinde görmek."},
    {"kelime": "metni tercüme etmek", "yasakli_kelimeler": ["çeviri", "dil", "türkçe", "anlam", "sözlük"], "zorluk": "kolay", "aciklama": "Antik dildeki yazıt metnini günümüz diline aktarmak."},

    # Orta (24)
    {"kelime": "estampaj almak", "yasakli_kelimeler": ["ıslak kağıt", "fırça", "mürekkep", "kabartma", "yazıt"], "zorluk": "orta", "aciklama": "Taş yazıtın üzerine ıslak kağıt ve mürekkep tatbik ederek kopyasını çıkartmak."},
    {"kelime": "stela dikmek", "yasakli_kelimeler": ["dikilitaş", "anıt", "yazıt", "adak", "zafer"], "zorluk": "orta", "aciklama": "Tarihi olay veya anı için taş blok dikip üzerine yazıt kazımak."},
    {"kelime": "harf formlarını tarihlendirmek", "yasakli_kelimeler": ["paleografi", "çağ", "yüzyıl", "yazı stili", "analiz"], "zorluk": "orta", "aciklama": "Yazıdaki harflerin şekil değişimine bakarak dönemi saptamak."},
    {"kelime": "adak yazıtı hazırlamak", "yasakli_kelimeler": ["tanrı", "tapınak", "sunu", "taş", "şükran"], "zorluk": "orta", "aciklama": "Tanrılara sunulan şükran veya adağı taşa yazdırmak."},
    {"kelime": "zafer anıtı inşa etmek", "yasakli_kelimeler": ["savaş", "komutan", "yazıt", "ordu", "kazanmak"], "zorluk": "orta", "aciklama": "Kazanılan savaşı ölümsüzleştirmek için kabartmalı ve yazılı anıt dikmek."},
    {"kelime": "latince metin çözmek", "yasakli_kelimeler": ["roma", "antik", "gramer", "çeviri", "alfabe"], "zorluk": "orta", "aciklama": "Roma dönemine ait Latince taş yazıları çözümlemek."},
    {"kelime": "eski yunanca çevirmek", "yasakli_kelimeler": ["grek", "alfabe", "antik", "filoloji", "yazıt"], "zorluk": "orta", "aciklama": "Grek alfabesiyle yazılmış antik metinleri tercüme etmek."},
    {"kelime": "rekonstrüksiyon yapmak", "yasakli_kelimeler": ["tamamlama", "eksik metin", "tahmin", "bütünleme", "taş"], "zorluk": "orta", "aciklama": "Yazıttaki kırık ve eksik kısımları bağlamdan yola çıkarak tamamlamak."},
    {"kelime": "taş yüzeyini temizlemek", "yasakli_kelimeler": ["yosun", "toz", "fırça", "kimyasal", "okunabilirlik"], "zorluk": "orta", "aciklama": "Yazıtın üzerindeki kir ve yosun tabakasını zarar vermeden arındırmak."},
    {"kelime": "fırdolayı yazı kazımak", "yasakli_kelimeler": ["etrafında", "çevre", "sütun", "dairesel", "taş"], "zorluk": "orta", "aciklama": "Sütun veya kaidenin etrafını dolanacak biçimde yazı yazmak."},
    {"kelime": "imparator unvanı tespit etmek", "yasakli_kelimeler": ["titulatur", "augustus", "caesar", "yıl", "saltanat"], "zorluk": "orta", "aciklama": "Yazıttaki hükümdar lakaplarından yola çıkarak kesin yılı bulmak."},
    {"kelime": "onurlandırma yazıtı dikmek", "yasakli_kelimeler": ["fahri", "meclis", "heykel kaidesi", "vatandaş", "ödül"], "zorluk": "orta", "aciklama": "Kente faydası dokunan bir kişi adına resmi övgü yazıtı koymak."},
    {"kelime": "lahit üzerine yazı yazmak", "yasakli_kelimeler": ["mezar", "mermer", "sanduka", "lanet", "ölü"], "zorluk": "orta", "aciklama": "Mermer mezar sandukasına mevtanın hayatını veya mezar koruma lanetini kazımak."},
    {"kelime": "mil taşı dikmek", "yasakli_kelimeler": ["roma yolu", "mesafe", "milliarium", "yol", "imparator"], "zorluk": "orta", "aciklama": "Roma yollarına merkeze olan mesafeyi belirten silindirik taşlar yerleştirmek."},
    {"kelime": "in situ inceleme yapmak", "yasakli_kelimeler": ["yerinde", "orijinal konum", "kazı", "taşınmamış", "arazi"], "zorluk": "orta", "aciklama": "Yazıtı bulunduğu özgün mimari konumunda incelemek."},
    {"kelime": "taşın cinsini belirlemek", "yasakli_kelimeler": ["mermer", "kireçtaşı", "bazalt", "granit", "maden"], "zorluk": "orta", "aciklama": "Yazıtın yapıldığı taşın jeolojik türünü ve ocağını tespit etmek."},
    {"kelime": "korpus oluşturmak", "yasakli_kelimeler": ["derleme", "katalog", "tüm yazıtlar", "bölge", "kitap"], "zorluk": "orta", "aciklama": "Bir bölgedeki tüm yazıtları bir araya getiren kapsamlı akademik külliyat hazırlamak."},
    {"kelime": "kısaltmaları açmak", "yasakli_kelimeler": ["harf", "sigla", "nokta", "kelime", "anlam"], "zorluk": "orta", "aciklama": "Taştaki yer darlığı sebebiyle yapılmış antik harf kısaltmalarını tamamlamak."},
    {"kelime": "aşınmayı önlemek", "yasakli_kelimeler": ["hava koşulları", "yağmur", "rüzgar", "koruma", "konservasyon"], "zorluk": "orta", "aciklama": "Yazıt yüzeyinin atmosferik şartlarla silinmesini engellemek."},
    {"kelime": "yazı yönünü belirlemek", "yasakli_kelimeler": ["sağdan sola", "soldan sağa", "bustrofedon", "yön", "satır"], "zorluk": "orta", "aciklama": "Antik yazının hangi istikamette aktığını tayin etmek."},
    {"kelime": "3d lazerle taramak", "yasakli_kelimeler": ["dijital", "model", "tarayıcı", "yüzey", "derinlik"], "zorluk": "orta", "aciklama": "Yazıtın mikron düzeyindeki yüzey oyuklarını üç boyutlu tarayıcıyla kaydetmek."},
    {"kelime": "vakıf kitabesi okumak", "yasakli_kelimeler": ["osmanlı", "cami", "çeşme", "sülüs", "şart"], "zorluk": "orta", "aciklama": "Tarihi çeşme veya cami üzerindeki vakfiye yazısını çözmek."},
    {"kelime": "yazıtın kopyasını dökmek", "yasakli_kelimeler": ["alçı", "silikon", "kalıp", "replika", "model"], "zorluk": "orta", "aciklama": "Yazıtın silikon veya alçı kalıbını çıkarıp birebir kopyasını üretmek."},
    {"kelime": "kronoloji oluşturmak", "yasakli_kelimeler": ["tarih sırası", "olay", "hükümdar", "dönem", "sıralama"], "zorluk": "orta", "aciklama": "Yazıtlardaki tarihlerden yararlanarak tarihsel zaman dizini kurmak."},

    # Zor (14)
    {"kelime": "bustrofedon okumak", "yasakli_kelimeler": ["öküz pulluğu", "bir sağdan bir soldan", "yılanvari", "antik grek", "satır"], "zorluk": "zor", "aciklama": "Bir satırı soldan sağa, sonraki satırı sağdan sola giden antik yazı stilini deşifre etmek."},
    {"kelime": "kritik aparat hazırlamak", "yasakli_kelimeler": ["dipnot", "farklı okumalar", "edisyon", "metin tenkidi", "varyant"], "zorluk": "zor", "aciklama": "Yazıtın farklı araştırmacılarca yapılan okuma varyantlarını dipnotta derlemek."},
    {"kelime": "damnatio memoriae uygulamak", "yasakli_kelimeler": ["hatırayı silme", "kazıma", "lanetleme", "imparator adı", "yok etme"], "zorluk": "zor", "aciklama": "Gözden düşen liderin adını yazıtlardan ve anıtlardan kazıyarak sildirmek."},
    {"kelime": "ligatür çözmek", "yasakli_kelimeler": ["birleşik harf", "bağlantı", "kaynaşma", "okuma", "harf"], "zorluk": "zor", "aciklama": "İki veya daha fazla harfin tek bir glifte birleştirildiği şekilleri çözümlemek."},
    {"kelime": "ergatif yapıyı saptamak", "yasakli_kelimeler": ["hurrice", "urartuca", "dilbilgisi", "özne", "ek"], "zorluk": "zor", "aciklama": "Çivi yazılı veya antik yazıtlarda ergatif tümce yapısını gramatikal olarak analiz etmek."},
    {"kelime": "lakunayı restore etmek", "yasakli_kelimeler": ["boşluk", "kırık parça", "kayıp metin", "tamlama", "tahmin"], "zorluk": "zor", "aciklama": "Taştaki kırılma sonucu yok olan metin boşluğunu filolojik olarak doldurmak."},
    {"kelime": "grafem analizi yapmak", "yasakli_kelimeler": ["yazı birimi", "karakter", "harf biçimi", "varyasyon", "fonem"], "zorluk": "zor", "aciklama": "Yazı sistemini oluşturan en küçük harf ve karakter birimlerini incelemek."},
    {"kelime": "paleografik tarihlendirme yapmak", "yasakli_kelimeler": ["yazı tarzı", "yüzyıl", "harf evrimi", "duktus", "çağ"], "zorluk": "zor", "aciklama": "Yazının hat özelliklerine ve duktusuna bakarak dönemsel yaş tespiti yapmak."},
    {"kelime": "prosopografik eşleştirme yapmak", "yasakli_kelimeler": ["şecere", "biyografi", "akrabalık", "soylu", "isim listesi"], "zorluk": "zor", "aciklama": "Yazıtta geçen şahıs isimlerini diğer tarihi kayıtlarla karşılaştırıp soyağacı çıkarmak."},
    {"kelime": "rTI yöntemiyle belgelemek", "yasakli_kelimeler": ["yansıma dönüşümlü görüntüleme", "farklı ışık açıları", "mikro oyuk", "fotoğraf", "dijital"], "zorluk": "zor", "aciklama": "Farklı ışık açılarından çekilen fotoğraflarla silik yazıt detaylarını görünür kılmak."},
    {"kelime": "metrografi uygulamak", "yasakli_kelimeler": ["ölçüm", "harf yüksekliği", "satır aralığı", "milimetre", "oran"], "zorluk": "zor", "aciklama": "Yazıttaki harf yükseklikleri ve satır aralıklarını milimetrik olarak ölçümlemek."},
    {"kelime": "çivi yazısını hecelemek", "yasakli_kelimeler": ["silabik", "kil tablet", "asur", "hitit", "işaret"], "zorluk": "zor", "aciklama": "Taş veya kil üzerindeki hece temelli çivi yazısı gliflerini fonetik olarak okumak."},
    {"kelime": "diplomatik transkripsiyon yapmak", "yasakli_kelimeler": ["birebir aktarım", "orijinal satır", "aynen", "harf harfine", "çeviriyazı"], "zorluk": "zor", "aciklama": "Taştaki metni satır satır ve hiçbir düzeltme yapmadan harfiyen aktarmak."},
    {"kelime": "onomastik çözümleme yapmak", "yasakli_kelimeler": ["özel isim kökeni", "etnik köken", "ad bilimi", "dil", "şahıs"], "zorluk": "zor", "aciklama": "Yazıtta geçen kişi ve yer adlarının kökenini ve etnisitesini saptamak."}
]

# 6. epistemoloji
epistemoloji_verbs = [
    # Kolay (12)
    {"kelime": "düşünmek", "yasakli_kelimeler": ["akıl", "fikir", "zihin", "mantık", "kafa"], "zorluk": "kolay", "aciklama": "Zihinsel süreçleri işletip fikir üretmek."},
    {"kelime": "öğrenmek", "yasakli_kelimeler": ["bilgi", "ders", "kitap", "kavramak", "anlamak"], "zorluk": "kolay", "aciklama": "Yeni bir bilgiyi veya beceriyi zihne yerleştirmek."},
    {"kelime": "anlamak", "yasakli_kelimeler": ["kavramak", "idrak", "bilmek", "çözmek", "mantık"], "zorluk": "kolay", "aciklama": "Bir konunun veya ifadenin anlamını zihinde açık hale getirmek."},
    {"kelime": "araştırmak", "yasakli_kelimeler": ["incelemek", "bilgi", "kaynak", "öğrenmek", "soruşturmak"], "zorluk": "kolay", "aciklama": "Bir gerçeği ortaya çıkarmak için inceleme yapmak."},
    {"kelime": "soru sormak", "yasakli_kelimeler": ["merak", "cevap", "sorgulamak", "öğrenmek", "neden"], "zorluk": "kolay", "aciklama": "Bilinmeyen bir şeyi öğrenmek amacıyla yöneltme yapmak."},
    {"kelime": "şüphe duymak", "yasakli_kelimeler": ["kuşku", "emin olamamak", "tereddüt", "güvenmemek", "gerçek"], "zorluk": "kolay", "aciklama": "Bir bilginin veya durumun doğruluğundan kesin emin olamamak."},
    {"kelime": "inanmak", "yasakli_kelimeler": ["güvenmek", "kabul", "inanç", "doğru", "iman"], "zorluk": "kolay", "aciklama": "Bir önermenin doğru olduğuna güvenip kanaat getirmek."},
    {"kelime": "bilgi edinmek", "yasakli_kelimeler": ["öğrenmek", "okumak", "haber", "kaynak", "veri"], "zorluk": "kolay", "aciklama": "Çevreden veya kaynaklardan yeni malumat toplamak."},
    {"kelime": "akıl yürütmek", "yasakli_kelimeler": ["mantık", "düşünce", "çıkarım", "muhakeme", "fikir"], "zorluk": "kolay", "aciklama": "Öncüllerden hareketle mantıksal bir sonuca varmak."},
    {"kelime": "farkına varmak", "yasakli_kelimeler": ["hissetmek", "idrak", "görmek", "anlamak", "bilinç"], "zorluk": "kolay", "aciklama": "Bir durumun veya nesnenin varlığını zihinde açıkça kavramak."},
    {"kelime": "gözlem yapmak", "yasakli_kelimeler": ["bakmak", "izlemek", "deney", "duyu", "incelemek"], "zorluk": "kolay", "aciklama": "Olayları veya nesneleri duyu organlarıyla dikkatle izlemek."},
    {"kelime": "yanılmak", "yasakli_kelimeler": ["hata", "yanlış", "aldanmak", "doğru değil", "saptırma"], "zorluk": "kolay", "aciklama": "Gerçeğe uymayan hatalı bir yargıya varmak."},

    # Orta (24)
    {"kelime": "sorgulamak", "yasakli_kelimeler": ["eleştiri", "şüphe", "neden", "araştırmak", "temel"], "zorluk": "orta", "aciklama": "Bilgilerin ve iddiaların doğruluğunu derinlemesine incelemek."},
    {"kelime": "kanıt sunmak", "yasakli_kelimeler": ["delil", "ispat", "göstermek", "iddia", "belge"], "zorluk": "orta", "aciklama": "Bir iddianın doğruluğunu gösteren somut deliller ortaya koymak."},
    {"kelime": "gerekçelendirmek", "yasakli_kelimeler": ["temellendirme", "dayanak", "argüman", "sebep", "ispat"], "zorluk": "orta", "aciklama": "Bir inanç veya bilginin neden doğru olduğunu mantıksal dayanakla savunmak."},
    {"kelime": "kavram oluşturmak", "yasakli_kelimeler": ["soyutlama", "zihin", "tanım", "terim", "genelleme"], "zorluk": "orta", "aciklama": "Nesnelerin ortak özelliklerini zihinde soyutlayıp kavrama dönüştürmek."},
    {"kelime": "çürütmek", "yasakli_kelimeler": ["yanlışlamak", "antitez", "argüman", "ispat", "geçersiz"], "zorluk": "orta", "aciklama": "Karşı tarafın öne sürdüğü tezin asılsız olduğunu göstermek."},
    {"kelime": "deneyimlemek", "yasakli_kelimeler": ["tecrübe", "yaşamak", "duyum", "ampirik", "pratik"], "zorluk": "orta", "aciklama": "Bir olayı doğrudan yaşayarak ve duyumsayarak tecrübe etmek."},
    {"kelime": "tümevarım yapmak", "yasakli_kelimeler": ["özelden genele", "tekil", "genelleme", "gözlem", "endüksiyon"], "zorluk": "orta", "aciklama": "Tekil gözlemlerden hareketle genel bir kurala ulaşmak."},
    {"kelime": "tümdengelim yapmak", "yasakli_kelimeler": ["genelden özele", "tümden gelim", "kural", "sonuç", "dedüksiyon"], "zorluk": "orta", "aciklama": "Genel ilkelerden hareketle özel tekil bir duruma dair çıkarım yapmak."},
    {"kelime": "tanımlamak", "yasakli_kelimeler": ["açıklamak", "sınır", "özellik", "kavram", "belirtmek"], "zorluk": "orta", "aciklama": "Bir kavramın temel niteliklerini ve sınırlarını net olarak ortaya koymak."},
    {"kelime": "ayrım yapmak", "yasakli_kelimeler": ["fark", "kategori", "sınıflandırma", "kriter", "ayırmak"], "zorluk": "orta", "aciklama": "İki kavram veya durum arasındaki temel farkı belirginleştirmek."},
    {"kelime": "doğrulamak", "yasakli_kelimeler": ["onay", "gerçek", "ispat", "uygunluk", "tasdik"], "zorluk": "orta", "aciklama": "Bir önermenin gerçeğe uygun olduğunu kanıtlarla onaylamak."},
    {"kelime": "yanlışlamak", "yasakli_kelimeler": ["popper", "hata", "çürütme", "tersini göstermek", "test"], "zorluk": "orta", "aciklama": "Bir iddianın yanlış olduğunu kanıtlayan karşıt örnek bulmak."},
    {"kelime": "idrak etmek", "yasakli_kelimeler": ["kavramak", "anlamak", "zihin", "fark", "bilinç"], "zorluk": "orta", "aciklama": "Bir durumu tüm derinliği ve anlamıyla zihinde kavramak."},
    {"kelime": "sezgisel kavramak", "yasakli_kelimeler": ["sezgi", "akıl dışı", "içgörü", "anında", "aracısız"], "zorluk": "orta", "aciklama": "Akıl yürütme basamaklarına ihtiyaç duymadan doğrudan ve aracısız anlamak."},
    {"kelime": "kanı oluşturmak", "yasakli_kelimeler": ["doxa", "görüş", "inanç", "kanaat", "fikir"], "zorluk": "orta", "aciklama": "Kesin ispata dayanmayan kişisel kanaat ve görüş geliştirmek."},
    {"kelime": "yanılsamayı fark etmek", "yasakli_kelimeler": ["illüzyon", "aldanma", "duyu hatası", "göz yanılması", "gerçek"], "zorluk": "orta", "aciklama": "Duyu organlarının insanı yanılttığı durumu idrak etmek."},
    {"kelime": "diyalektik tartışmak", "yasakli_kelimeler": ["tez", "antitez", "sentez", "sokrat", "karşıtlık"], "zorluk": "orta", "aciklama": "Karşıt argümanları çarpıştırarak daha üst bir hakikate ulaşmaya çalışmak."},
    {"kelime": "ön kabulleri yıkmak", "yasakli_kelimeler": ["önyargı", "varsayım", "dogma", "sorgulama", "şüphe"], "zorluk": "orta", "aciklama": "Sorgulanmadan doğru kabul edilmiş inançları geçersiz kılmak."},
    {"kelime": "dogmalara karşı çıkmak", "yasakli_kelimeler": ["katı inanç", "eleştiri", "özgür düşünce", "kalıp", "otorite"], "zorluk": "orta", "aciklama": "Körü körüne inanılan değişmez kabulleri eleştiriye açmak."},
    {"kelime": "özne-nesne ilişkisi kurmak", "yasakli_kelimeler": ["bilen", "bilinen", "bağlantı", "zihin", "dış dünya"], "zorluk": "orta", "aciklama": "Bilen insan zihni ile bilinen dış nesne arasındaki bağı çözümlemek."},
    {"kelime": "zihinsel model geliştirmek", "yasakli_kelimeler": ["tasarım", "kavrayış", "şema", "teori", "temsil"], "zorluk": "orta", "aciklama": "Gerçekliğin zihindeki işleyiş şemasını ve temsilini oluşturmak."},
    {"kelime": "ampirik veri toplamak", "yasakli_kelimeler": ["deney", "gözlem", "duyusal", "somut", "deneyim"], "zorluk": "orta", "aciklama": "Duyusal deneyim ve somut gözlemlere dayalı bilgi üretmek."},
    {"kelime": "muhakeme yapmak", "yasakli_kelimeler": ["yargı", "akıl", "tartmak", "değerlendirmek", "karar"], "zorluk": "orta", "aciklama": "Olayları ve delilleri akıl terazisinde tartarak sonuca varmak."},
    {"kelime": "kategoriye ayırmak", "yasakli_kelimeler": ["sınıflamak", "tür", "bölüm", "kant", "zihin"], "zorluk": "orta", "aciklama": "Bilgileri ve kavramları zihinsel sınıflara yerleştirmek."},

    # Zor (14)
    {"kelime": "a priori bilgiye ulaşmak", "yasakli_kelimeler": ["deneyim öncesi", "saf akıl", "kant", "deneyden bağımsız", "zorunlu"], "zorluk": "zor", "aciklama": "Duyusal deneyime dayanmayan, doğuştan veya salt akılla bilinen bilgiye erişmek."},
    {"kelime": "a posteriori temellendirmek", "yasakli_kelimeler": ["deneyim sonrası", "ampirik", "duyu", "kant", "gözlem"], "zorluk": "zor", "aciklama": "Bilginin doğruluğunu duyusal tecrübe ve deneyim sonrasına dayandırmak."},
    {"kelime": "epistemik gerekçelendirme yapmak", "yasakli_kelimeler": ["haklılandırılmış", "doğru inanç", "kanıt", "episteme", "dayanak"], "zorluk": "zor", "aciklama": "Bir inancı doğru bilgi (episteme) seviyesine yükseltecek rasyonel kanıt sunmak."},
    {"kelime": "gettier problemini çözmek", "yasakli_kelimeler": ["şans eseri doğru", "üçlü tanım", "karşı örnek", "haklılandırılmış inanç", "bilgi"], "zorluk": "zor", "aciklama": "Gerekçelendirilmiş doğru inancın bilgi için her zaman yeterli olmadığını açıklamak."},
    {"kelime": "epistemolojik kopuş yaşamak", "yasakli_kelimeler": ["bachelard", "althusser", "paradigma değişimi", "kavramsal kırılma", "bilim"], "zorluk": "zor", "aciklama": "Eski düşünce ve bilgi sisteminden köklü ve radikal bir kopuşla ayrılmak."},
    {"kelime": "solipsizmi tartışmak", "yasakli_kelimeler": ["tekbencilik", "sadece benim zihnim", "dış dünya yokluğu", "kuşku", "ben"], "zorluk": "zor", "aciklama": "Yalnızca kendi bilincinin var olduğunun bilinebileceği tezini sorgulamak."},
    {"kelime": "münferit algıları sentetize etmek", "yasakli_kelimeler": ["kant", "sentetik", "duyu verisi", "bütünleştirme", "anlak"], "zorluk": "zor", "aciklama": "Parça parça gelen duyu verilerini anlak kategorileriyle birleştirmek."},
    {"kelime": "koherantist doğruluk aramak", "yasakli_kelimeler": ["bağdaşımcılık", "tutarlılık", "inanç ağı", "sistem", "uyum"], "zorluk": "zor", "aciklama": "Bir bilginin doğruluğunu var olan inançlar bütünüyle çelişmemesinde aramak."},
    {"kelime": "temelciliği savunmak", "yasakli_kelimeler": ["foundationalism", "temel inançlar", "dayanak", "aksiyom", "sarsılmaz"], "zorluk": "zor", "aciklama": "Tüm bilgilerin gerekçelendirmeye muhtaç olmayan sarsılmaz temel inançlara dayandığını savunmak."},
    {"kelime": "fenomenolojik indirgeme yapmak", "yasakli_kelimeler": ["epokhe", "paranteze alma", "husserl", "öz", "yönelimsellik"], "zorluk": "zor", "aciklama": "Dış dünyanın varlığına dair kabulleri paranteze alıp nesnenin saf özüne odaklanmak."},
    {"kelime": "yönelimsellik sergilemek", "yasakli_kelimeler": ["intentionality", "bilincin nesnesi", "brentano", "husserl", "hakkındalık"], "zorluk": "zor", "aciklama": "Bilinç hallerinin daima bir nesneye yönelik ve bir şey hakkında olması."},
    {"kelime": "septisizm geliştirmek", "yasakli_kelimeler": ["kuşkuculuk", "kesin bilginin imkansızlığı", "pyrrhon", "yargıyı askıya alma", "şüphe"], "zorluk": "zor", "aciklama": "Kesin ve mutlak bilgiye ulaşılamayacağını savunarak her türlü yargıdan kaçınmak."},
    {"kelime": "ontolojik temele oturtmak", "yasakli_kelimeler": ["varlık", "bilgi-varlık", "hakikat", "metafizik", "ilişki"], "zorluk": "zor", "aciklama": "Bilgi teorisini varlığın yapısı ve doğasıyla uyumlu bir temele bağlamak."},
    {"kelime": "epistemik adil davranmak", "yasakli_kelimeler": ["epistemik adaletsizlik", "tanıklık", "güvenilirlik", "önyargı", "fricker"], "zorluk": "zor", "aciklama": "Bilgi aktaran kişinin sözüne önyargılardan arınmış adil bir güven payı tanımak."}
]

add_and_save_verbs('epigrafi', epigrafi_verbs)
add_and_save_verbs('epistemoloji', epistemoloji_verbs)
print('P3 done!')
