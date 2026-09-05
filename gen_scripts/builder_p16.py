import os, sys, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gen_scripts.card_utils import add_and_save_verbs

# 31. kampcilik
kampcilik_verbs = [
    # Kolay (12)
    {"kelime": "kamp alanına yerleşmek", "yasakli_kelimeler": ["doğa", "bölge", "eşyaları indirme", "orman", "konaklama"], "zorluk": "kolay", "aciklama": "Kamp yapacağı araziye varıp eşyaları düzenlemek."},
    {"kelime": "kamp ateşi yakmak", "yasakli_kelimeler": ["odun", "çakmak", "ısınmak", "alev", "gece"], "zorluk": "kolay", "aciklama": "Isınmak veya aydınlanmak için açık havada ateş yakmak."},
    {"kelime": "uyku tulumuna girmek", "yasakli_kelimeler": ["fermuar", "sıcak", "çadır içi", "gece", "yatmak"], "zorluk": "kolay", "aciklama": "Gece soğuktan korunmak için tulumun içine yatıp fermuarı çekmek."},
    {"kelime": "mat sermek", "yasakli_kelimeler": ["çadır tabanı", "zemin", "yumuşak", "yalıtım", "uyku"], "zorluk": "kolay", "aciklama": "Yerin soğuğunu ve sertliğini kesmek için çadır içine mat açmak."},
    {"kelime": "odun toplamak", "yasakli_kelimeler": ["çalı", "ağaç dalı", "orman", "ateş için", "kuru"], "zorluk": "kolay", "aciklama": "Ateşi beslemek için ormandan kuru dalları bir araya getirmek."},
    {"kelime": "fener taşımak", "yasakli_kelimeler": ["el feneri", "kafa lambası", "karanlık", "ışık", "gece"], "zorluk": "kolay", "aciklama": "Gece ormanda yolunu bulmak için aydınlatma aracı bulundurmak."},
    {"kelime": "kamp eşyalarını toplamak", "yasakli_kelimeler": ["çanta", "katlamak", "araca yükleme", "kamp sonu", "ayrılma"], "zorluk": "kolay", "aciklama": "Kamp bitiminde tüm araç gereçleri toparlayıp çantaya yerleştirmek."},
    {"kelime": "marşmelov kızartmak", "yasakli_kelimeler": ["tatlı", "çubuk", "ateş üstü", "erimek", "atıştırmalık"], "zorluk": "kolay", "aciklama": "Ateşin üzerinde çubuğa takılı şekerlemeyi karamelize etmek."},
    {"kelime": "matara doldurmak", "yasakli_kelimeler": ["su kabı", "çeşme", "içmek", "yürüyüş", "şişe"], "zorluk": "kolay", "aciklama": "Doğa yürüyüşü öncesi su kabını taze suyla doldurmak."},
    {"kelime": "doğada uyanmak", "yasakli_kelimeler": ["kuş sesi", "sabah", "temiz hava", "çadırdan çıkmak", "güneş"], "zorluk": "kolay", "aciklama": "Sabah çadırın kapısını açıp doğanın içinde güne başlamak."},
    {"kelime": "çöpleri toplamak", "yasakli_kelimeler": ["poşet", "doğayı temiz bırakma", "çevre", "atık", "ayrılma"], "zorluk": "kolay", "aciklama": "Kamptan ayrılırken alanı arkasında hiç çöp bırakmadan temizlemek."},
    {"kelime": "hamak asmak", "yasakli_kelimeler": ["iki ağaç arası", "ip", "sallanmak", "dinlenmek", "keyif"], "zorluk": "kolay", "aciklama": "İki ağacın gövdesine ip bağlayarak sallanan yatak kurmak."},

    # Orta (24)
    {"kelime": "kamp ocağında yemek pişirmek", "yasakli_kelimeler": ["kartuş", "tüp", "tencere", "gaz", "outdoor"], "zorluk": "orta", "aciklama": "Taşınabilir küçük gaz ocağında sıcak yemek hazırlamak."},
    {"kelime": "çadır kazığı çakmak", "yasakli_kelimeler": ["toprak", "gergi ipleri", "rüzgar direnci", "çekiç", "taş"], "zorluk": "orta", "aciklama": "Çadırın gergi iplerini toprağa çakılan metal kazıklara sabitlemek."},
    {"kelime": "su arıtma tableti kullanmak", "yasakli_kelimeler": ["dere suyu", "mikrop kırma", "filtre", "içilebilir su", "klor"], "zorluk": "orta", "aciklama": "Doğal kaynak suyunu dezenfekte etmek için içine arıtma hapı atmak."},
    {"kelime": "çadırın gergi iplerini germek", "yasakli_kelimeler": ["rüzgar", "fırtına", "sıkılaştırma", "ip ayarı", "sağlamlık"], "zorluk": "orta", "aciklama": "Çadırın rüzgarda sallanmaması için iplerini sıkı hale getirmek."},
    {"kelime": "sırt çantası ayarlamak", "yasakli_kelimeler": ["bel kemeri", "omuz askısı", "ağırlık merkezi", "litre", "yük"], "zorluk": "orta", "aciklama": "Büyük yürüyüş çantasının ağırlığını bele bindirecek peron ayarlarını yapmak."},
    {"kelime": "ateşi güvenle söndürmek", "yasakli_kelimeler": ["su dökmek", "toprak örtmek", "köz", "yangın önleme", "soğutma"], "zorluk": "orta", "aciklama": "Ateşin tamamen söndüğünden emin olmak için su döküp toprakla üzerini kapamak."},
    {"kelime": "çakmaktaşı ile kıvılcım çıkarmak", "yasakli_kelimeler": ["magnezyum çubuğu", "kav", "sürtme", "ateş başlatıcı", "kibrit"], "zorluk": "orta", "aciklama": "Magnezyum çubuğunu bıçak sırtıyla sürterek kuru kava kıvılcım fırlatmak."},
    {"kelime": "tente kurmak", "yasakli_kelimeler": ["tarp", "gölgelik", "yağmur barınağı", "ip", "çadır üstü"], "zorluk": "orta", "aciklama": "Yağmurdan ve güneşten korunmak için geniş su geçirmez örtü germek."},
    {"kelime": "yiyecekleri ağaca asmak", "yasakli_kelimeler": ["ayı koruması", "vahşi hayvan", "ip çekme", "yüksek dal", "koku"], "zorluk": "orta", "aciklama": "Vahşi hayvanların yiyeceklere ulaşamaması için erzak torbasını yüksek dala asmak."},
    {"kelime": "düdük çalmak", "yasakli_kelimeler": ["kaybolma", "acil durum", "ses", "üç kısa", "arama kurtarma"], "zorluk": "orta", "aciklama": "Ormanda kaybolunduğunda yerini belli etmek için yüksek sesli düdük öttürmek."},
    {"kelime": "çakı bilemek", "yasakli_kelimeler": ["bıçak", "bileme taşı", "outdoor alet", "keskinleştirme", "ahşap yontma"], "zorluk": "orta", "aciklama": "Kamp çakısının körelen kesici ağzını taşla bilemek."},
    {"kelime": "su geçirmezlik spreyi sıkmak", "yasakli_kelimeler": ["dwr kaplama", "çadır kumaşı", "yağmur testi", "bot", "yalıtım"], "zorluk": "orta", "aciklama": "Çadır ve botun su iticiliğini korumak için koruyucu sprey uygulamak."},
    {"kelime": "kamp yeri seçmek", "yasakli_kelimeler": ["düz zemin", "rüzgar almayan", "su kenarı mesafesi", "ağaç altı tehlikesi", "arazi"], "zorluk": "orta", "aciklama": "Eğim, rüzgar ve sel risklerini gözeterek en güvenli çadır noktasını belirlemek."},
    {"kelime": "termos hazırlamak", "yasakli_kelimeler": ["sıcak çay", "kahve", "yalıtımlı kap", "gece", "ısı koruma"], "zorluk": "orta", "aciklama": "Soğuk gecelerde tüketmek için paslanmaz termosa sıcak içecek doldurmak."},
    {"kelime": "kuru giysi torbası kullanmak", "yasakli_kelimeler": ["dry bag", "su geçirmez çanta", "ıslanma önleme", "yedek kıyafet", "nehir geçişi"], "zorluk": "orta", "aciklama": "Yedek giysileri su geçirmez kuru torba içinde muhafaza etmek."},
    {"kelime": "ilk yardım çantası taşımak", "yasakli_kelimeler": ["sargı bezi", "tentürdiyot", "yara bandı", "ilaç", "acil müdahale"], "zorluk": "orta", "aciklama": "Olası yaralanmalara karşı acil tıbbi kiti her an yanında bulundurmak."},
    {"kelime": "kafa fenerinin pilini değiştirmek", "yasakli_kelimeler": ["led", "eller serbest", "kırmızı ışık modu", "yedek pil", "aydınlatma"], "zorluk": "orta", "aciklama": "Karanlıkta iki elini serbest kullanabilmek için kafa lambasının gücünü tazelemek."},
    {"kelime": "izotermal battaniye açmak", "yasakli_kelimeler": ["acil durum folyosu", "altın gümüş", "vücut ısısı yansıtıcı", "hipotermi", "folyo"], "zorluk": "orta", "aciklama": "Hipotermi riskinde vücut ısısını geri yansıtan ince metalik örtüyü sarmak."},
    {"kelime": "ayakkabıları çadıra almak", "yasakli_kelimeler": ["akrep börtü böcek", "çadır önü bagaj", "çiğ düşmesi", "ıslanma", "bot"], "zorluk": "orta", "aciklama": "Botların içine böcek girmemesi ve çiğden ıslanmaması için çadır içine koymak."},
    {"kelime": "rüzgar siperliği kurmak", "yasakli_kelimeler": ["ocak etrafı", "alüminyum plaka", "alev sönmesi", "verimli pişirme", "rüzgar"], "zorluk": "orta", "aciklama": "Ocağın alevinin rüzgarda sönmemesi için etrafına katlanır panel dizmek."},
    {"kelime": "pusula ile yön bulmak", "yasakli_kelimeler": ["kuzey", "manyetik sapma", "kerteriz", "kaybolma", "harita"], "zorluk": "orta", "aciklama": "Pusulanın manyetik ibresine bakarak gidilecek yönü tayin etmek."},
    {"kelime": "kamp feneri asmak", "yasakli_kelimeler": ["çadır tavan kancası", "dağınık ışık", "lamba", "iç aydınlatma", "karabina"], "zorluk": "orta", "aciklama": "Çadırın tavanındaki kancaya ortam lambasını asmak."},
    {"kelime": "ayak parmaklarını ısıtmak", "yasakli_kelimeler": ["yün çorap", "soğuk", "uyku öncesi", "ısıtıcı ped", "donma önleme"], "zorluk": "orta", "aciklama": "Tulum içine girmeden önce üşüyen ayaklara kalın termal çorap giymek."},
    {"kelime": "ağaç gövdesine basamak yapmak", "yasakli_kelimeler": ["tırmanma", "ip düğümü", "yüksek nokta", "keşif", "doğal merdiven"], "zorluk": "orta", "aciklama": "Çevreye hakim olmak veya malzeme asmak için iplerle ağaca basamak kurmak."},

    # Zor (14)
    {"kelime": "dakota ateş çukuru kazmak", "yasakli_kelimeler": ["gizli ateş", "hava tüneli", "dumansız yanma", "yeraltı ocağı", "taktik kamp"], "zorluk": "zor", "aciklama": "Rüzgardan korunaklı ve sıfır dumanlı yanma sağlayan çift delikli yeraltı ocağı kazmak."},
    {"kelime": "kav hazırlamak", "yasakli_kelimeler": ["char cloth", "karbonize pamuklu bez", "kapalı kutuda yakma", "kıvılcım yakalayıcı", "ateş başlatma"], "zorluk": "zor", "aciklama": "Hava almayan kutuda pamuklu kumaşı kavurup kıvılcımı anında yakalayan kor kumaş üretmek."},
    {"kelime": "yaylı matkapla ateş yakmak", "yasakli_kelimeler": ["bow drill", "sürtünme ateşi", "ahşap mil", "yuva tahtası", "kara duman közü"], "zorluk": "zor", "aciklama": "Ahşap yayı ve mili tahtaya sürterek ilkel sürtünme yöntemiyle köz elde etmek."},
    {"kelime": "prusik düğümü atmak", "yasakli_kelimeler": ["sürtünme bağı", "ana ip üzerinde kaydırma", "tırmanış", "kilitlenme", "kamp kurtarma"], "zorluk": "zor", "aciklama": "Yük bindiğinde ana ipe sımsıkı kilitlenen, boştayken kayan özel kurtarma düğümünü bağlamak."},
    {"kelime": "kar mağarası oymak", "yasakli_kelimeler": ["iglo alternatifi", "kar kütlesi", "sıfır derece yalıtımı", "havalandırma deliği", "kış kampı"], "zorluk": "zor", "aciklama": "Sertleşmiş kar yığınının içini oyup donmaktan kurtaran acil kış barınağı inşa etmek."},
    {"kelime": "yerden yalıtımlı sığınak yapmak", "yasakli_kelimeler": ["debrıs shelter", "çalı çırpı örtüsü", "doğal yalıtım", "yaprak katmanı", "survival"], "zorluk": "zor", "aciklama": "Yere temas etmeyen ve metrelerce yaprakla kaplı doğal hayatta kalma kulübesi yapmak."},
    {"kelime": "yerçekimiyle çalışan su filtresi kurmak", "yasakli_kelimeler": ["hollow fiber", "seramik filtre", "0.1 mikron", "ağaca asılı torba", "bakteri arıtma"], "zorluk": "zor", "aciklama": "Yüksek bir dala asılan torbadan süzülen suyun mikro gözeneklerle arıtılmasını sağlamak."},
    {"kelime": "avcı düğümü bağlamak", "yasakli_kelimeler": ["hunter's bend", "iki ipi birleştirme", "çözülmeyen bağ", "yüksek mukavemet", "perlon"], "zorluk": "zor", "aciklama": "Farklı kalınlıktaki iki ipi ağır yük altında asla kaymayacak şekilde birbirine bağlamak."},
    {"kelime": "kerteriz açısını haritaya uygulamak", "yasakli_kelimeler": ["manyetik sapma düzeltmesi", "üç nokta nirengi", "arazi harita eşleme", "rota çizme", "pusula"], "zorluk": "zor", "aciklama": "Arazideki belirgin zirvelerden alınan pusula kerterizlerini haritaya çizip konumunu bulmak."},
    {"kelime": "kontrollü hipotermi önlemi almak", "yasakli_kelimeler": ["sıcak su şişesi kasıklara", "rüzgar bariyeri", "glikoz takviyesi", "kuru giydirme", "yaşam kurtarma"], "zorluk": "zor", "aciklama": "Aşırı soğukta donma tehlikesi yaşayan kampçının ana damarlarına sıcak kompres uygulamak."},
    {"kelime": "bushcraft tencere askısı yapmak", "yasakli_kelimeler": ["üçayak çatmak", "ahşap çentik", "zincirsiz kanca", "ayarlanabilir yükseklik", "dal"], "zorluk": "zor", "aciklama": "Ateşin üstüne tencere asmak için ormandaki dallardan ayarlanabilir çentikli askı yapmak."},
    {"kelime": "su kaynağı göstergesi bitkileri okumak", "yasakli_kelimeler": ["söğüt ağacı", "kamışlık", "yeşil vaha çizgisi", "yeraltı suyu", "iz sürme"], "zorluk": "zor", "aciklama": "Doğadaki bitki örtüsü türlerine bakarak yüzeye en yakın tatlı su kaynağını tespit etmek."},
    {"kelime": "çadır eteklerine taş yığmak", "yasakli_kelimeler": ["fırtına eteği", "yüksek irtifa", "çadırın havalanmasını önleme", "kar yükü", "baskı"], "zorluk": "zor", "aciklama": "Fırtınalı arazide çadırın altından rüzgar girmemesi için kumaş eteklerini ağır taşlarla gömmek."},
    {"kelime": "biyobozunur kamp sabunu ile yıkanmak", "yasakli_kelimeler": ["su kaynağından 60 metre uzakta", "doğaya zarar vermeyen", "kampanojenik", "arındırma", "ekolojik"], "zorluk": "zor", "aciklama": "Su kaynaklarından en az 60 metre uzakta toprağa dökülecek şekilde çevre dostu sabunla yıkanmak."}
]

add_and_save_verbs('kampcilik', kampcilik_verbs)
add_and_save_verbs('kartografya', kartografya_verbs)
print('P16 done!')
