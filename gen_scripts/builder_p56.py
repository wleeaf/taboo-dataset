import sys
from card_utils import add_and_save_verbs

# 1. ZOOLOJI (50 verbs: 12 kolay, 24 orta, 14 zor)
zooloji_verbs = [
    # Kolay (12)
    {
        "kelime": "Hayvan İncelemek",
        "aciklama": "Canlıların anatomik ve biyolojik yapılarını yakından gözlemlemek.",
        "yasakli_kelimeler": ["canlı", "biyoloji", "anatomi", "gözlem", "laboratuvar"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Tür Tanımlamak",
        "aciklama": "Yeni keşfedilen bir canlının özelliklerini belirleyip literatüre kazandırmak.",
        "yasakli_kelimeler": ["yeni", "keşif", "isimlendirme", "özellik", "literatür"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Yumurta Bırakmak",
        "aciklama": "Kuş, sürüngen veya balıkların neslini sürdürmek için yumurtlaması.",
        "yasakli_kelimeler": ["kuş", "balık", "kuluçka", "üreme", "kabuk"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Yavru Bakımı Yapmak",
        "aciklama": "Ebeveyn hayvanın yavrularını beslemesi, temizlemesi ve koruması.",
        "yasakli_kelimeler": ["ebeveyn", "besleme", "büyütme", "koruma", "anne"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Hayvanat Bahçesi Gezmek",
        "aciklama": "Farklı kıtalardan getirilmiş vahşi hayvanları özel kafes ve barınaklarda görmek.",
        "yasakli_kelimeler": ["kafes", "barınak", "vahşi", "ziyaret", "park"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Kuş Halkalamak",
        "aciklama": "Göç rotalarını izlemek için kuşların bacağına numaralı halka takmak.",
        "yasakli_kelimeler": ["halka", "bacak", "göç", "izleme", "numara"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Mikroskopla Bakmak",
        "aciklama": "Hücre ve mikroorganizmaları mercek altında büyüterek incelemek.",
        "yasakli_kelimeler": ["mercek", "büyütmek", "hücre", "lame", "küçük"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Örnek Toplamak",
        "aciklama": "Arazi çalışmasında böcek, kıl veya tüy numunesi derlemek.",
        "yasakli_kelimeler": ["numune", "arazi", "böcek", "kıl", "tüp"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Hayvan Sayımı Yapmak",
        "aciklama": "Belirli bir bölgedeki canlı popülasyonunun sayısını tespit etmek.",
        "yasakli_kelimeler": ["popülasyon", "tespit", "miktar", "envanter", "bölge"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Kafes Temizlemek",
        "aciklama": "Laboratuvar veya bakım merkezindeki hayvan barınaklarının hijyenini sağlamak.",
        "yasakli_kelimeler": ["barınak", "hijyen", "yıkanma", "laboratuvar", "pislik"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Belgesel Çekmek",
        "aciklama": "Vahşi canlıların doğal yaşamını kameralarla kayıt altına almak.",
        "yasakli_kelimeler": ["kamera", "kayıt", "doğal yaşam", "video", "televizyon"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Nesli Tükenmek",
        "aciklama": "Bir hayvan türünün yeryüzündeki tüm bireylerinin ölmesi.",
        "yasakli_kelimeler": ["ölüm", "son birey", "yok olmak", "dinozor", "kırmızı liste"],
        "zorluk": "kolay"
    },

    # Orta (24)
    {
        "kelime": "Sınıflandırma Yapmak",
        "aciklama": "Canlıları alem, şube, sınıf, takım, aile, cins ve tür basamaklarına ayırmak.",
        "yasakli_kelimeler": ["taksonomi", "şube", "alem", "cins", "basamak"],
        "zorluk": "orta"
    },
    {
        "kelime": "Diseksiyon Yapmak",
        "aciklama": "İç organları ve anatomiyi incelemek için ölü hayvan kadavrasını bistüri ile kesip açmak.",
        "yasakli_kelimeler": ["kadavra", "bistüri", "kesmek", "iç organ", "otopsi"],
        "zorluk": "orta"
    },
    {
        "kelime": "Morfolojik Tahlil Yapmak",
        "aciklama": "Canlının dış görünüşü, organ oranları ve iskelet yapısını detaylı ölçmek.",
        "yasakli_kelimeler": ["dış görünüş", "organ", "iskelet", "ölçüm", "yapı"],
        "zorluk": "orta"
    },
    {
        "kelime": "DNA Barkodlama Yapmak",
        "aciklama": "Kısa bir genetik dizilim kullanarak canlının hangi türe ait olduğunu tespit etmek.",
        "yasakli_kelimeler": ["genetik", "dizilim", "sekans", "tür tespiti", "gen"],
        "zorluk": "orta"
    },
    {
        "kelime": "Ekolojik Niş Belirlemek",
        "aciklama": "Bir hayvanın ekosistem içindeki beslenme, barınma ve biyolojik rolünü saptamak.",
        "yasakli_kelimeler": ["ekosistem", "rol", "beslenme", "habitat", "fonksiyon"],
        "zorluk": "orta"
    },
    {
        "kelime": "Metamorfoz Geçirmek",
        "aciklama": "Tırtılın kelebeğe veya iribaşın kurbağaya dönüşmesi gibi başkalaşım yaşamak.",
        "yasakli_kelimeler": ["başkalaşım", "tırtıl", "kelebek", "larva", "krizalit"],
        "zorluk": "orta"
    },
    {
        "kelime": "Fotokapan Kurmak",
        "aciklama": "Yaban hayatını rahatsız etmeden gece ve gündüz hareket sensörlü kameralarla izlemek.",
        "yasakli_kelimeler": ["hareket sensörü", "kamera", "yaban hayatı", "ağaca bağlamak", "gece görüşü"],
        "zorluk": "orta"
    },
    {
        "kelime": "Etoloji İncelemesi Yapmak",
        "aciklama": "Hayvanların doğadaki davranış kalıplarını, sosyal ilişkilerini ve güdülerini araştırmak.",
        "yasakli_kelimeler": ["davranış", "içgüdü", "sosyal", "kalıp", "bilim"],
        "zorluk": "orta"
    },
    {
        "kelime": "Telemetri Takibi Yapmak",
        "aciklama": "Yakalanan vahşi hayvana GPS verici tasma takarak uydu üzerinden hareketini izlemek.",
        "yasakli_kelimeler": ["tasma", "gps", "verici", "uydu", "takip"],
        "zorluk": "orta"
    },
    {
        "kelime": "Fosil Eşleştirmek",
        "aciklama": "Milyonlarca yıllık kemik ve diş kalıntılarını günümüz hayvan anatomisiyle karşılaştırmak.",
        "yasakli_kelimeler": ["kemik", "kalıntı", "paleontoloji", "milyon yıl", "karşılaştırma"],
        "zorluk": "orta"
    },
    {
        "kelime": "Koryon Zarı İncelemek",
        "aciklama": "Embriyoyu saran koruyucu dış yumurta zarının gaz geçirgenliğini analiz etmek.",
        "yasakli_kelimeler": ["embriyo", "yumurta zarı", "koruyucu", "gaz alışverişi", "amniyon"],
        "zorluk": "orta"
    },
    {
        "kelime": "Böcek İğnelemek",
        "aciklama": "Koleksiyon ve müzecilik için böcek örneklerini özel panolara böcek iğnesiyle sabitlemek.",
        "yasakli_kelimeler": ["entomoloji", "koleksiyon", "pano", "iğne", "sabitlemek"],
        "zorluk": "orta"
    },
    {
        "kelime": "Habitatı Haritalamak",
        "aciklama": "Bir hayvan topluluğunun yaşadığı coğrafi sınırları ve bitki örtüsünü CBS ile çizmek.",
        "yasakli_kelimeler": ["coğrafi sınır", "cbs", "yaşam alanı", "bitki örtüsü", "harita"],
        "zorluk": "orta"
    },
    {
        "kelime": "Sürüngenleri İncelemek",
        "aciklama": "Herpetoloji alanında kertenkele, yılan ve kaplumbağaların pullu derisini ve fizyolojisini çalışmak.",
        "yasakli_kelimeler": ["herpetoloji", "yılan", "kertenkele", "pul", "soğukkanlı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Memelileri Sınıflamak",
        "aciklama": "Mammaloji dalında plasentalı, keseliler ve tek delikliler gibi grupları ayrıştırmak.",
        "yasakli_kelimeler": ["mammaloji", "plasenta", "keseli", "süt bezi", "doğuran"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kuş Sesini Spektrogramda İncelemek",
        "aciklama": "Kuş ötüşlerinin frekans ve ses dalga grafiklerini ses analiz programında çözümlemek.",
        "yasakli_kelimeler": ["ötüş", "frekans", "ses dalgası", "grafik", "biyoakustik"],
        "zorluk": "orta"
    },
    {
        "kelime": "Dışkı Analizi Yapmak",
        "aciklama": "Vahşi hayvan dışkısındaki sindirilmemiş tohum ve kemiklerden beslenme rejimini tespit etmek.",
        "yasakli_kelimeler": ["beslenme rejimi", "sindirilmemiş", "kemik", "tohum", "dışkı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Karasal Omurgasızları Toplamak",
        "aciklama": "Toprak altı ve ağaç kabuklarındaki eklembacaklıları pitfall çukur tuzaklarıyla yakalamak.",
        "yasakli_kelimeler": ["tuzak", "çukur", "eklembacaklı", "omurgasız", "toprak"],
        "zorluk": "orta"
    },
    {
        "kelime": "Endemik Türü Korumak",
        "aciklama": "Dünyada yalnızca belirli bir dar coğrafyada yaşayan nadir hayvanı koruma altına almak.",
        "yasakli_kelimeler": ["nadir", "sadece orada", "dar coğrafya", "milli park", "yok olma tehlikesi"],
        "zorluk": "orta"
    },
    {
        "kelime": "Trofik Düzeyi Hesaplamak",
        "aciklama": "Canlının besin ağındaki basamağını (üretici, birincil tüketici, ikincil tüketici) belirlemek.",
        "yasakli_kelimeler": ["besin ağı", "otçul", "etçil", "piramit", "basamak"],
        "zorluk": "orta"
    },
    {
        "kelime": "İkili Adlandırma Yapmak",
        "aciklama": "Linnaeus sistemine göre canlıya Latince Cins ve Epitet isimlerini (Binominal) vermek.",
        "yasakli_kelimeler": ["linnaeus", "binominal", "latince", "cins adı", "homo sapiens"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kemik İskeletini Birleştirmek",
        "aciklama": "Müzede sergilemek üzere temizlenmiş hayvan kemiklerini tellerle anatomik pozisyonda dizmek.",
        "yasakli_kelimeler": ["müze", "iskelet", "tel", "monte etmek", "kemikler"],
        "zorluk": "orta"
    },
    {
        "kelime": "Gen Havuzunu İncelemek",
        "aciklama": "İzole bir popülasyondaki genetik çeşitliliği ve akraba evliliği (inbreeding) oranını ölçmek.",
        "yasakli_kelimeler": ["çeşitlilik", "alel", "akrabalık", "izole", "popülasyon genetiği"],
        "zorluk": "orta"
    },
    {
        "kelime": "Solungaç Solunumu İncelemek",
        "aciklama": "Balık ve suda yaşayan canlıların sudaki çözünmüş oksijeni kana aktarma mekanizmasını çalışmak.",
        "yasakli_kelimeler": ["balık", "oksijen", "kan", "su", "solungaç kapağı"],
        "zorluk": "orta"
    },

    # Zor (14)
    {
        "kelime": "Filogenetik Ağaç Çizmek",
        "aciklama": "Türlerin ortak atalarından günümüze evrimsel akrabalık ve dallanma ilişkilerini modellemek.",
        "yasakli_kelimeler": ["evrim", "kladogram", "ortak ata", "dallanma", "akrabalık"],
        "zorluk": "zor"
    },
    {
        "kelime": "Kladistik Analiz Yapmak",
        "aciklama": "Türemiş karakterler (sinapomorfi) üzerinden organizmaları monofiletik gruplara ayırmak.",
        "yasakli_kelimeler": ["sinapomorfi", "monofiletik", "klad", "türemiş karakter", "ata"],
        "zorluk": "zor"
    },
    {
        "kelime": "Allometrik Büyümeyi Ölçmek",
        "aciklama": "Vücut organlarının genel gövde büyüklüğüne göre farklı oranlarda büyüme hızını hesaplamak.",
        "yasakli_kelimeler": ["büyüme hızı", "oran", "boynuz boyu", "gövde", "farklı oran"],
        "zorluk": "zor"
    },
    {
        "kelime": "Endotermik Regülasyon Sağlamak",
        "aciklama": "Sıcakkanlı hayvanların çevre sıcaklığına bakılmaksızın iç vücut ısısını metabolik olarak sabit tutması.",
        "yasakli_kelimeler": ["sıcakkanlı", "homeostaz", "vücut ısısı", "metabolizma", "sabit"],
        "zorluk": "zor"
    },
    {
        "kelime": "Ektotermik Davranış Sergilemek",
        "aciklama": "Soğukkanlı canlıların vücut ısısını ayarlamak için güneşe çıkıp kayalarda güneşlenmesi.",
        "yasakli_kelimeler": ["soğukkanlı", "güneşlenme", "dış ortam", "kertenkele", "ısı alma"],
        "zorluk": "zor"
    },
    {
        "kelime": "Taksonomik Revizyon Yapmak",
        "aciklama": "Yeni genetik bulgular ışığında önceden tanımlanmış bir cinsi veya türü yeniden adlandırıp ayırmak.",
        "yasakli_kelimeler": ["yeniden sınıflandırma", "genetik bulgu", "sinonim", "ayrılma", "revizyon"],
        "zorluk": "zor"
    },
    {
        "kelime": "Kadavrayı Masere Etmek",
        "aciklama": "İskelet hazırlamak için et dokularını enzimler ve dermestid böcek larvalarıyla temizlemek.",
        "yasakli_kelimeler": ["dermestid böceği", "kemik temizleme", "et arındırma", "maserasyon", "iskelet"],
        "zorluk": "zor"
    },
    {
        "kelime": "Tip Örneğini Belirlemek",
        "aciklama": "Bir türün bilimsel tanımına temel oluşturan müzeye kayıtlı holotip numunesini seçmek.",
        "yasakli_kelimeler": ["holotip", "paratip", "müze kaydı", "orijinal numune", "tanım temeli"],
        "zorluk": "zor"
    },
    {
        "kelime": "Homeobox Genlerini Taramak",
        "aciklama": "Embriyonik gelişimde vücut planı ve organların dizilimini kontrol eden Hox genlerini incelemek.",
        "yasakli_kelimeler": ["hox genleri", "embriyo gelişimi", "vücut planı", "segmentasyon", "evo-devo"],
        "zorluk": "zor"
    },
    {
        "kelime": "Karşıt Akım Değişimi Yapmak",
        "aciklama": "Kutup kuşlarının bacaklarında atardamar ile toplardamarın yan yana geçerek ısı kaybını önlemesi.",
        "yasakli_kelimeler": ["ısı koruma", "atardamar toplardamar", "kutup", "kan akışı", "bacak"],
        "zorluk": "zor"
    },
    {
        "kelime": "Biyocoğrafi Dağılımı Çözümlemek",
        "aciklama": "Türlerin kıtalar üzerindeki dağılımını Wallace Hattı ve tektonik levha hareketleriyle açıklamak.",
        "yasakli_kelimeler": ["wallace hattı", "kıta kayması", "endemizm", "ada biyocoğrafyası", "dağılım"],
        "zorluk": "zor"
    },
    {
        "kelime": "Sölom Boşluğunu İncelemek",
        "aciklama": "Hayvan embriyolojisinde mezodermle çevrili gerçek vücut boşluğunun gelişimini takip etmek.",
        "yasakli_kelimeler": ["vücut boşluğu", "mezoderm", "embriyoloji", "sölomat", "iç organ yatağı"],
        "zorluk": "zor"
    },
    {
        "kelime": "Girişken Türleri İzlemek",
        "aciklama": "Doğal yaşam alanına sonradan giren istilacı türlerin yerli fauna üzerindeki baskısını ölçmek.",
        "yasakli_kelimeler": ["istilacı tür", "yerli fauna", "popülasyon baskısı", "biyoçeşitlilik kaybı", "ekolojik tehdit"],
        "zorluk": "zor"
    },
    {
        "kelime": "Optik Çözünürlüğü Spektrometreyle Ölçmek",
        "aciklama": "Kuşların ve böceklerin ultraviyole ışık dalga boylarını algılama kapasitesini test etmek.",
        "yasakli_kelimeler": ["ultraviyole", "uv görüşü", "dalga boyu", "kuş gözü", "fotoreseptör"],
        "zorluk": "zor"
    }
]

if __name__ == "__main__":
    add_and_save_verbs("zooloji", zooloji_verbs)
