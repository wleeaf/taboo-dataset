import os, sys, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gen_scripts.card_utils import add_and_save_verbs

kutugoyunlari_verbs = [
    # Kolay (12)
    {"kelime": "zarları masaya yuvarlamak", "yasakli_kelimeler": ["noktalar", "altı", "masa", "şans", "fırlatmak"], "zorluk": "kolay", "aciklama": "Küp şeklindeki oyun taşını masaya yuvarlamak."},
    {"kelime": "piyon ilerletmek", "yasakli_kelimeler": ["kare", "adım", "tahta", "oynatmak", "figür"], "zorluk": "kolay", "aciklama": "Kendi karakter taşını zar kadar kare ileri taşımak."},
    {"kelime": "kart çekmek", "yasakli_kelimeler": ["deste", "el", "sıra", "görev", "kapalı"], "zorluk": "kolay", "aciklama": "Masadaki destenin en üstünden yeni oyun kartı almak."},
    {"kelime": "sıra beklemek", "yasakli_kelimeler": ["arkadaş", "tur", "hamle", "oyuncu", "zaman"], "zorluk": "kolay", "aciklama": "Diğer oyuncuların hamlesini bitirmesini sabırla beklemek."},
    {"kelime": "puan toplamak", "yasakli_kelimeler": ["skor", "kazanmak", "yıldız", "artı", "zafer"], "zorluk": "kolay", "aciklama": "Oyun içindeki görevleri tamamlayıp skor hanesine puan yazdırmak."},
    {"kelime": "kutuyu açmak", "yasakli_kelimeler": ["kapak", "kutu oyunu", "kurulum", "parçalar", "yeni oyun"], "zorluk": "kolay", "aciklama": "Oyuna başlamak için masanın ortasındaki kutunun kapağını kaldırmak."},
    {"kelime": "tahtayı sermek", "yasakli_kelimeler": ["mukavva", "harita", "kareler", "masa üstü", "açmak"], "zorluk": "kolay", "aciklama": "Katlanmış sert mukavva oyun alanını masaya düzgünce açmak."},
    {"kelime": "oyunu kazanmak", "yasakli_kelimeler": ["birinci olmak", "zafer", "en yüksek puan", "şampiyon", "bitiş"], "zorluk": "kolay", "aciklama": "Kuralları başarıyla tamamlayıp oyunu rakiplerinden önde bitirmek."},
    {"kelime": "hile yapmamak", "yasakli_kelimeler": ["dürüstlük", "kurala uymak", "aldatmamak", "gizlice", "adil"], "zorluk": "kolay", "aciklama": "Oyun kurallarına sadık kalıp haksız kazançtan kaçınmak."},
    {"kelime": "kartları karıştırmak", "yasakli_kelimeler": ["deste", "shuffle", "rastgele", "kesmek", "el"], "zorluk": "kolay", "aciklama": "Kartların sırasını bozup rastgele hale getirmek."},
    {"kelime": "hamle yapmak", "yasakli_kelimeler": ["hareket", "sıra sende", "oynamak", "strateji", "adım"], "zorluk": "kolay", "aciklama": "Sırası geldiğinde oyun mekanizmasına uygun hareketini gerçekleştirmek."},
    {"kelime": "parçaları kutuya dizmek", "yasakli_kelimeler": ["toplamak", "torba", "oyun sonu", "kaldırmak", "düzen"], "zorluk": "kolay", "aciklama": "Oyun bittiğinde piyon ve kartları kutusundaki gözlere yerleştirmek."},

    # Orta (24)
    {"kelime": "kural kitapçığını okumak", "yasakli_kelimeler": ["manual", "yönergeler", "oyun kuralları", "öğrenmek", "nasıl oynanır"], "zorluk": "orta", "aciklama": "Oyuna başlamadan önce içinden çıkan talimat kitapçığını incelemek."},
    {"kelime": "deste inşa etmek", "yasakli_kelimeler": ["deck building", "kart satın alma", "sinerji", "dominion", "kombinasyon"], "zorluk": "orta", "aciklama": "Oyun aktıkça güçlü kartları destesine ekleyip kendi destesini geliştirmek."},
    {"kelime": "işçi yerleştirmek", "yasakli_kelimeler": ["worker placement", "meeple", "aksiyon alanı", "kaynak toplama", "bloke etme"], "zorluk": "orta", "aciklama": "Piyonunu tahtadaki sınırlı eylem alanlarına koyarak kaynak veya hak kazanmak."},
    {"kelime": "kaynak yönetimi yapmak", "yasakli_kelimeler": ["odun taş tahıl", "harcama", "depolama", "üretim", "verimlilik"], "zorluk": "orta", "aciklama": "Toplanan sınırlı hammadde ve paraları en verimli şekilde kullanmak."},
    {"kelime": "meeple koymak", "yasakli_kelimeler": ["ahşap adam figürü", "carcassonne", "yol kale tarlaya yerleştirme", "puan", "piyon"], "zorluk": "orta", "aciklama": "Ahşap insan figürünü karonun üzerine koyarak orayı sahiplenmek."},
    {"kelime": "karo yerleştirmek", "yasakli_kelimeler": ["tile placement", "harita genişletme", "yol ve şehir eşleme", "kare parça", "masa"], "zorluk": "orta", "aciklama": "Kare karton parçayı kenarları uyumlu olacak şekilde masadaki haritaya eklemek."},
    {"kelime": "blöf yapmak", "yasakli_kelimeler": ["kandırma", "elini saklama", "yalan söyleme", "rol yapma", "poker yüzü"], "zorluk": "orta", "aciklama": "Rakipleri yanıltmak için elindeki kartlar hakkında yalan beyanda bulunmak."},
    {"kelime": "gizli rolünü saklamak", "yasakli_kelimeler": ["social deduction", "hain", "vampir köylü", "kimlik", "ihanet"], "zorluk": "orta", "aciklama": "Oyun başında kapalı verilen hain veya ajan kimliğini kimseye belli etmemek."},
    {"kelime": "zar havuzunu yönetmek", "yasakli_kelimeler": ["dice drafting", "zar seçme", "yeniden atma hakkı", "kombinasyon", "şans kontrolü"], "zorluk": "orta", "aciklama": "Masaya atılan zarlar arasından stratejisine en uygun olanları seçip kullanmak."},
    {"kelime": "pazarlık masasına oturmak", "yasakli_kelimeler": ["catan", "takas", "koyun verip odun alma", "anlaşma", "ticaret"], "zorluk": "orta", "aciklama": "Eksik kaynaklarını tamamlamak için rakipleriyle takas müzakeresi yapmak."},
    {"kelime": "alan kontrolü sağlamak", "yasakli_kelimeler": ["area control", "çoğunluk", "bölge hakimiyeti", "savaş", "puan kazanma"], "zorluk": "orta", "aciklama": "Tahtadaki belirli bir bölgeye en çok askeri koyup oranın puanını toplamak."},
    {"kelime": "ortaklaşa mücadele etmek", "yasakli_kelimeler": ["co-op", "oyuna karşı birlik", "pandemic", "birlikte kazanma kaybetme", "dayanışma"], "zorluk": "orta", "aciklama": "Birbirine rakip olmak yerine tüm oyuncularla birlikte oyun sistemine karşı oynamak."},
    {"kelime": "görev kartını gizli tutmak", "yasakli_kelimeler": ["gizli hedef", "oyun sonu puanı", "hedef kartı", "göstermemek", "strateji"], "zorluk": "orta", "aciklama": "Oyun sonunda ekstra puan getirecek özel görevi rakiplerden gizlemek."},
    {"kelime": "minyatür boyamak", "yasakli_kelimeler": ["plastik figür", "warhammer", "akrilik fırça", "hobi", "detay"], "zorluk": "orta", "aciklama": "Kutu oyunundaki plastik karakter minyatürlerini boyalarla canlandırmak."},
    {"kelime": "monopoly parası dağıtmak", "yasakli_kelimeler": ["bankacı", "kağıt para", "başlangıç sermayesi", "dağıtım", "kasa"], "zorluk": "orta", "aciklama": "Oyun başlamadan önce kasa görevlisi olarak herkese başlangıç parasını saymak."},
    {"kelime": "kumar oynamamak", "yasakli_kelimeler": ["bahis", "şans kontrolü", "risk alma", "taktik", "zar"], "zorluk": "orta", "aciklama": "Körlemesine şansa güvenmek yerine hesaplanmış risklerle ilerlemek."},
    {"kelime": "tur sırasını belirlemek", "yasakli_kelimeler": ["turn order", "en yüksek zar", "saat yönü", "inisiyatif", "başlangıç oyuncusu"], "zorluk": "orta", "aciklama": "Kimin önce oynayacağını zarla veya kuraldaki kriterle belirlemek."},
    {"kelime": "kart kılıfı takmak", "yasakli_kelimeler": ["sleeve", "şeffaf koruyucu", "yıpranma önleme", "kart", "koleksiyon"], "zorluk": "orta", "aciklama": "Kartların kenarlarının soyulmaması için üzerlerine şeffaf koruyucu poşet geçirmek."},
    {"kelime": "puan tablosuna yazmak", "yasakli_kelimeler": ["skor kağıdı", "kalem", "toplama", "kategori", "oyun sonu"], "zorluk": "orta", "aciklama": "Oyun sonunda her kategoriden kazanılan puanları skor kağıdına işlemek."},
    {"kelime": "engelleme hamlesi yapmak", "yasakli_kelimeler": ["bloklama", "rakibin yolunu kesme", "alanı kapatma", "sabote", "taktik"], "zorluk": "orta", "aciklama": "Rakibin kazanmasını veya puan almasını önlemek için önüne set çekmek."},
    {"kelime": "kart elini optimize etmek", "yasakli_kelimeler": ["hand management", "kart kombosu", "en iyi sıra", "etkili kullanım", "tasarruf"], "zorluk": "orta", "aciklama": "Elindeki sınırlı kartları en yüksek faydayı verecek sırayla oynamak."},
    {"kelime": "kampanya modunda oynamak", "yasakli_kelimeler": ["legacy", "bölüm bölüm ilerleme", "kalıcı değişim", "hikaye", "senaryo"], "zorluk": "orta", "aciklama": "Oyunun her oturumunda bir önceki kararların taşındığı hikaye modunu oynamak."},
    {"kelime": "otoma destesi yönetmek", "yasakli_kelimeler": ["tek kişilik oyun", "yapay zeka kartları", "solo mod", "bot rakip", "sanal oyuncu"], "zorluk": "orta", "aciklama": "Tek başına oynarken sanal yapay zeka rakibinin hamle kartlarını çekip işletmek."},
    {"kelime": "kum saatiyle süre tutmak", "yasakli_kelimeler": ["zaman baskısı", "hızlı düşünme", "akan kum", "süre bitimi", "stres"], "zorluk": "orta", "aciklama": "Hamle süresini kısıtlamak için masadaki küçük kum saatini ters çevirmek."},

    # Zor (14)
    {"kelime": "engine building motoru kurmak", "yasakli_kelimeler": ["kart makinesi", "kartların birbirini tetiklemesi", "katlanarak artan güç", "zincirleme reaksiyon", "terraforming mars"], "zorluk": "zor", "aciklama": "Her tur birbirini besleyen ve katlanarak devasa kaynak üreten kart motoru inşa etmek."},
    {"kelime": "legacy oyununda bileşen yırtmak", "yasakli_kelimeler": ["kalıcı hasar", "kart imhası", "kutuya etiket yapıştırma", "tek seferlik deneyim", "pandemi legacy"], "zorluk": "zor", "aciklama": "Geri dönüşü olmayan Legacy oyununda talimat gereği kartı yırtıp panoya kalıcı etiket yapıştırmak."},
    {"kelime": "simültan aksiyon seçimi yapmak", "yasakli_kelimeler": ["aynı anda kart açma", "gizli seçim", "zihin okuma", "7 wonders", "hızlı tur"], "zorluk": "zor", "aciklama": "Tüm oyuncuların aynı anda gizlice seçtiği kartı masaya eşzamanlı açması."},
    {"kelime": "drafting mekanizması işletmek", "yasakli_kelimeler": ["kart seçip kalanı yana verme", "el döndürme", "en iyi kartı alma", "sola pas", "kart havuzu"], "zorluk": "zor", "aciklama": "Gelen kart destesinden en iyisini alıp kalanını yanındaki oyuncuya devretmek."},
    {"kelime": "rondel üzerinde ilerlemek", "yasakli_kelimeler": ["dairesel aksiyon çarkı", "adım maliyeti", "mac gerdts", "çark hamlesi", "eylem seçimi"], "zorluk": "zor", "aciklama": "Dairesel tekerlek üzerindeki eylemler arasında belirli adım kısıtlarıyla ilerleyip hamle seçmek."},
    {"kelime": "action point allowance harcamak", "yasakli_kelimeler": ["aksiyon puanı sistemi", "5 puanı bölüştürme", "hareket maliyeti", "hamle optimizasyonu", "puan kotası"], "zorluk": "zor", "aciklama": "Tur başında verilen 4-5 aksiyon puanını hareket ve eylemler arasında matematiksel paylaştırmak."},
    {"kelime": "modular board dizilimi oluşturmak", "yasakli_kelimeler": ["her oyunda değişen harita", "rastgele altıgenler", "farklı kurulum", "tekrar oynanabilirlik", "hex"], "zorluk": "zor", "aciklama": "Her oyun öncesinde tahtanın altıgen parçalarını rastgele dizerek benzersiz harita kurmak."},
    {"kelime": "asimetrik güçleri dengelemek", "yasakli_kelimeler": ["root", "her ırkın farklı kuralı", "benzersiz oynanış", "farklı kazanma şartı", "fraksiyon"], "zorluk": "zor", "aciklama": "Her fraksiyonun bambaşka kurallarla ve farklı hedeflerle oynadığı asimetrik yapıyı yönetmek."},
    {"kelime": "push-your-luck riskini hesaplamak", "yasakli_kelimeler": ["şansını zorlama", "açgözlülük cezası", "patlama riski", "durma noktası", "quacks"], "zorluk": "zor", "aciklama": "Daha çok ödül için torbadan taş çekmeye devam edip patlama riskini matematiksel tartmak."},
    {"kelime": "hidden movement izini sürmek", "yasakli_kelimeler": ["gizli hareket", "fury of dracula", "arkada gizlice dolaşma", "avcıların koordinasyonu", "iz bulma"], "zorluk": "zor", "aciklama": "Tahtada görünmeden gizlice haritada dolaşan tek bir oyuncunun ayak izlerini avcılarla sürmek."},
    {"kelime": "pazar talebini manipüle etmek", "yasakli_kelimeler": ["arz talep eğrisi", "brass", "hammadde fiyatı artırma", "piyasa boşaltma", "ekonomik oyun"], "zorluk": "zor", "aciklama": "Merkezi pazardan toplu mal çekip kaynak fiyatını rakiplerin alamayacağı kadar tırmandırmak."},
    {"kelime": "tableau building kombinasyonu kurmak", "yasakli_kelimeler": ["önündeki kart ızgarası", "wingspan", "habitat eşleşmesi", "puan motoru", "kart sinerjisi"], "zorluk": "zor", "aciklama": "Önündeki panoya kartları matris şeklinde yerleştirip aralarındaki sinerjilerden puan üretmek."},
    {"kelime": "tehdit seviyesini kontrol altında tutmak", "yasakli_kelimeler": ["threat track", "felaket eşiği", "canavar uyanışı", "arkham horror", "kaybetme koşulu"], "zorluk": "zor", "aciklama": "Her tur yükselen felaket göstergesini görevler tamamlayarak patlama sınırının altında tutmak."},
    {"kelime": "kral yapıcı durumuna düşmemek", "yasakli_kelimeler": ["kingmaker", "kendisi kazanamazken birini kazandırma", "etik oyunculuk", "tarafsız hamle", "üçüncü oyuncu"], "zorluk": "zor", "aciklama": "Kendisinin kazanma şansı kalmadığında yaptığı hamleyle bilerek bir rakibini şampiyon yapmaktan kaçınmak."}
]

add_and_save_verbs('kutugoyunlari', kutugoyunlari_verbs)
print('P20b done!')
