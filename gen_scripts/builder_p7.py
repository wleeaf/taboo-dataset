import os, sys, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gen_scripts.card_utils import add_and_save_verbs

# 13. farmakoloji
farmakoloji_verbs = [
    # Kolay (12)
    {"kelime": "reçete yazmak", "yasakli_kelimeler": ["doktor", "ilaç", "eczane", "kağıt", "tedavi"], "zorluk": "kolay", "aciklama": "Hastanın kullanacağı ilaçları resmi belgeye dökmek."},
    {"kelime": "ilaç içmek", "yasakli_kelimeler": ["hap", "su", "yutmak", "şifa", "hasta"], "zorluk": "kolay", "aciklama": "Hastalığı iyileştirmek için tableti suyla yutmak."},
    {"kelime": "şurup içirmek", "yasakli_kelimeler": ["kaşık", "tatlı", "çocuk", "sıvı", "öksürük"], "zorluk": "kolay", "aciklama": "Sıvı formdaki ilacı ölçek kaşığıyla hastaya vermek."},
    {"kelime": "krem sürmek", "yasakli_kelimeler": ["merhem", "deri", "ovmak", "kaşıntı", "cilt"], "zorluk": "kolay", "aciklama": "Yarı katı tıbbi ürünü cilde yayarak uygulamak."},
    {"kelime": "prospektüs okumak", "yasakli_kelimeler": ["kutu içi", "yan etki", "kullanım kılavuzu", "doz", "uyarı"], "zorluk": "kolay", "aciklama": "İlaç kutusundan çıkan bilgilendirme kağıdını incelemek."},
    {"kelime": "iğne vurulmak", "yasakli_kelimeler": ["enjeksiyon", "hemşire", "kol", "kalça", "ağrı"], "zorluk": "kolay", "aciklama": "Sıvı ilacın şırınga ile kas veya damara verilmesi."},
    {"kelime": "göz damlası damlatmak", "yasakli_kelimeler": ["göz", "şişe", "kırpmak", "yaş", "görme"], "zorluk": "kolay", "aciklama": "Gözdeki enfeksiyonu gidermek için damlayı göze akıtmak."},
    {"kelime": "eczacıya danışmak", "yasakli_kelimeler": ["soru", "tavsiye", "ilaç", "dükkan", "tarif"], "zorluk": "kolay", "aciklama": "İlacın nasıl kullanılacağını eczane yetkilisine sormak."},
    {"kelime": "ağrı kesici almak", "yasakli_kelimeler": ["baş ağrısı", "parol", "rahatlama", "hap", "sancı"], "zorluk": "kolay", "aciklama": "Vücuttaki ağrıyı dindirmek için ilaç tüketmek."},
    {"kelime": "doz aşımı yapmak", "yasakli_kelimeler": ["fazla ilaç", "zehirlenme", "tehlike", "miktar", "hastane"], "zorluk": "kolay", "aciklama": "Önerilen ilaç miktarından çok daha fazlasını almak."},
    {"kelime": "son kullanma tarihine bakmak", "yasakli_kelimeler": ["kutu", "tarih", "bozulma", "geçmiş", "kontrol"], "zorluk": "kolay", "aciklama": "İlacın güvenle tüketilebileceği son günü denetlemek."},
    {"kelime": "ilaçları dolaba kaldırmak", "yasakli_kelimeler": ["ecza dolabı", "saklamak", "çocuklardan uzak", "serin", "kilit"], "zorluk": "kolay", "aciklama": "İlaçları güvenli ve serin bir dolapta muhafaza etmek."},

    # Orta (24)
    {"kelime": "yan etki gözlemlemek", "yasakli_kelimeler": ["mide bulantısı", "baş dönmesi", "alerji", "reaksiyon", "istenmeyen"], "zorluk": "orta", "aciklama": "İlacın asıl tedavisi dışındaki olumsuz etkilerini takip etmek."},
    {"kelime": "etken maddeyi belirlemek", "yasakli_kelimeler": ["molekül", "kimyasal", "jenerik", "tedavi edici", "bileşen"], "zorluk": "orta", "aciklama": "İlacın tedavi edici ana kimyasal bileşenini saptamak."},
    {"kelime": "antibiyotik direnci geliştirmek", "yasakli_kelimeler": ["bakteri", "bağışıklık", "etkisiz kalma", "yanlış kullanım", "mikrop"], "zorluk": "orta", "aciklama": "Bakterilerin antibiyotiklere karşı savunma kazanması."},
    {"kelime": "damar yolu açmak", "yasakli_kelimeler": ["intravenöz", "serum", "kanül", "damar", "hemşire"], "zorluk": "orta", "aciklama": "İlaç ve serumu doğrudan kan dolaşımına vermek için kanül takmak."},
    {"kelime": "ilaç etkileşimini kontrol etmek", "yasakli_kelimeler": ["çapraz reaksiyon", "iki ilaç", "zarar", "karışım", "uyumsuzluk"], "zorluk": "orta", "aciklama": "Birlikte alınan iki ilacın birbirinin etkisini bozup bozmadığına bakmak."},
    {"kelime": "biyoyararlanımı ölçmek", "yasakli_kelimeler": ["emilim", "dolaşım", "yüzde", "kana karışma", "farmakokinetik"], "zorluk": "orta", "aciklama": "Alınan ilacın ne kadarının değişmeden sistemik dolaşıma geçtiğini bulmak."},
    {"kelime": "plasebo etkisi yaratmak", "yasakli_kelimeler": ["etkisiz madde", "şeker hapı", "psikolojik", "inanç", "iyileşme"], "zorluk": "orta", "aciklama": "Farmakolojik etkisi olmayan maddenin telkinle iyileşme sağlaması."},
    {"kelime": "ilaç sentezlemek", "yasakli_kelimeler": ["laboratuvar", "kimyager", "reaksiyon", "üretim", "formülasyon"], "zorluk": "orta", "aciklama": "Yeni bir kimyasal bileşiği laboratuvarda reaksiyonlarla üretmek."},
    {"kelime": "tolerans geliştirmek", "yasakli_kelimeler": ["etkinin azalması", "doz artırma", "vücudun alışması", "duyarsızlaşma", "bağımlılık"], "zorluk": "orta", "aciklama": "Zamanla aynı etkinin alınabilmesi için daha yüksek doza ihtiyaç duyulması."},
    {"kelime": "ilaç yarı ömrünü hesaplamak", "yasakli_kelimeler": ["kandan atılma", "konsantrasyon", "yarılanma", "saat", "vücut"], "zorluk": "orta", "aciklama": "İlacın plazma konsantrasyonunun yarıya inmesi için gereken süreyi saptamak."},
    {"kelime": "sublingual uygulamak", "yasakli_kelimeler": ["dil altı", "hızlı emilim", "damar", "eritmek", "tansiyon"], "zorluk": "orta", "aciklama": "İlacı yutmadan dil altına koyarak kılcal damarlardan hızla emilmesini sağlamak."},
    {"kelime": "antidot uygulamak", "yasakli_kelimeler": ["panzehir", "zehirlenme", "etkiyi nötrleme", "tedavi", "acil"], "zorluk": "orta", "aciklama": "Toksik maddenin vücuttaki zehirleyici etkisini nötralize eden ilacı vermek."},
    {"kelime": "kontrendikasyon saptamak", "yasakli_kelimeler": ["kullanılmaması gereken durum", "engel", "gebelik", "risk", "yasak"], "zorluk": "orta", "aciklama": "İlacın hastaya verilmesinin tehlikeli olduğu klinik durumları belirlemek."},
    {"kelime": "toksisite testi yapmak", "yasakli_kelimeler": ["zehirlilik", "doz", "denek", "güvenlik", "ld50"], "zorluk": "orta", "aciklama": "Maddenin organizmaya zarar verme derecesini test etmek."},
    {"kelime": "jenerik ilaç üretmek", "yasakli_kelimeler": ["muadil", "eşdeğer", "patent bitimi", "orijinal", "üretim"], "zorluk": "orta", "aciklama": "Patenti dolan orijinal ilacın biyoeşdeğer kopyasını piyasaya sürmek."},
    {"kelime": "klinik faz çalışması yapmak", "yasakli_kelimeler": ["faz 1 2 3", "gönüllü", "hasta denemesi", "ruhsat", "etkinlik"], "zorluk": "orta", "aciklama": "İlacın insandaki güvenliğini ve faydasını aşama aşama test etmek."},
    {"kelime": "deri yoluyla emilmek", "yasakli_kelimeler": ["transdermal", "flaster", "bant", "yavaş salınım", "cilt"], "zorluk": "orta", "aciklama": "İlaç moleküllerinin flasterden deri gözenekleri aracılığıyla kana geçmesi."},
    {"kelime": "karaciğerde metabolize olmak", "yasakli_kelimeler": ["sitokrom", "parçalanma", "organ", "enzim", "atılım"], "zorluk": "orta", "aciklama": "İlaç bileşiğinin karaciğer enzimleri tarafından kimyasal değişime uğraması."},
    {"kelime": "böbrekten atılmak", "yasakli_kelimeler": ["idrar", "eliminasyon", "filtrasyon", "klirens", "boşaltım"], "zorluk": "orta", "aciklama": "Metabolize olan ilaç artıklarının idrar yoluyla vücuttan uzaklaştırılması."},
    {"kelime": "ilaç ruhsatı almak", "yasakli_kelimeler": ["sağlık bakanlığı", "fda", "onay", "satış izni", "belge"], "zorluk": "orta", "aciklama": "İlacın piyasada satılabilmesi için resmi otoriteden yasal onay almak."},
    {"kelime": "serum konsantrasyonu takip etmek", "yasakli_kelimeler": ["kan tahlili", "düzey", "terapötik aralık", "ölçüm", "mikrogram"], "zorluk": "orta", "aciklama": "Kandaki ilaç yoğunluğunun güvenli sınırlar içinde olduğunu izlemek."},
    {"kelime": "bağımlılık riskini değerlendirmek", "yasakli_kelimeler": ["yoksunluk", "psikolojik", "fiziksel", "kırmızı reçete", "uyuşturucu"], "zorluk": "orta", "aciklama": "İlacın hastada alışkanlık ve yoksunluk yapma potansiyelini tartmak."},
    {"kelime": "kontrollü salım sağlamak", "yasakli_kelimeler": ["yavaş salınım", "kapsül", "24 saat", "uzatılmış etki", "tablet"], "zorluk": "orta", "aciklama": "İlacın gün boyu azar azar kana karışacak formda üretilmesi."},
    {"kelime": "steril solüsyon hazırlamak", "yasakli_kelimeler": ["mikropsuz", "otoklav", "göz damlası", "enjeksiyon", "laboratuvar"], "zorluk": "orta", "aciklama": "Hiçbir canlı mikroorganizma içermeyen saf sıvı ilaç karışımı üretmek."},

    # Zor (14)
    {"kelime": "reseptör agonisti olarak bağlanmak", "yasakli_kelimeler": ["aktive etmek", "bağlanma bölgesi", "hücresel yanıt", "ligand", "uyarı"], "zorluk": "zor", "aciklama": "Hücre zarındaki alıcıya bağlanıp doğal maddenin etkisini taklit ederek uyarı başlatmak."},
    {"kelime": "antagonist etki göstermek", "yasakli_kelimeler": ["bloke etmek", "reseptör", "engelleme", "inhibisyon", "karşıt etki"], "zorluk": "zor", "aciklama": "Reseptörü bloke ederek agonist maddelerin bağlanmasını engellemek."},
    {"kelime": "ilk geçiş etkisini aşmak", "yasakli_kelimeler": ["first pass effect", "karaciğer", "portal ven", "oral biyoyararlanım", "metabolizma"], "zorluk": "zor", "aciklama": "Ağızdan alınan ilacın karaciğerde hemen yıkıma uğramadan hedefe ulaşmasını sağlamak."},
    {"kelime": "sitokrom p450 enzimlerini indüklemek", "yasakli_kelimeler": ["cyp450", "hızlanma", "karaciğer", "ilaç yıkımı", "etkileşim"], "zorluk": "zor", "aciklama": "Karaciğerdeki metabolizma enzimlerinin miktar ve aktivitesini artırmak."},
    {"kelime": "terapötik indeksi hesaplamak", "yasakli_kelimeler": ["td50 / ed50", "güvenlik aralığı", "toksik doz", "etkin doz", "dar indeks"], "zorluk": "zor", "aciklama": "İlacın toksik dozu ile etkin dozu arasındaki güvenlik marjını oranlamak."},
    {"kelime": "allosterik modülatör olarak çalışmak", "yasakli_kelimeler": ["ikincil bağlanma yeri", "konformasyon", "artırma azaltma", "reseptör", "etki"], "zorluk": "zor", "aciklama": "Reseptörün aktif bölgesi dışındaki bir yere bağlanarak afinitesini değiştirmek."},
    {"kelime": "klirens hızını türetmek", "yasakli_kelimeler": ["vücuttan temizlenme", "plazma hacmi", "böbrek", "dakikadaki debi", "eliminasyon"], "zorluk": "zor", "aciklama": "Birim zamanda ilaçtan tamamen arındırılan sanal kan plazması hacmini bulmak."},
    {"kelime": "dağılım hacmini saptamak", "yasakli_kelimeler": ["volume of distribution", "dokuya geçiş", "lipofilik", "plazma", "oran"], "zorluk": "zor", "aciklama": "Vücuttaki toplam ilaç miktarının kandaki derişime oranını modellemek."},
    {"kelime": "taşifilaksi geliştirmek", "yasakli_kelimeler": ["akut tolerans", "hızlı duyarsızlaşma", "efedrin", "reseptör desensitizasyonu", "cevap azalması"], "zorluk": "zor", "aciklama": "İlacın ardışık tekrarlanan dozlarında çok hızlı biçimde etkisizleşmesi."},
    {"kelime": "enantiomerleri ayırmak", "yasakli_kelimeler": ["kiralite", "optik izomer", "sağ sol el", "talidomid", "saf molekül"], "zorluk": "zor", "aciklama": "Molekülün ayna görüntüsü olan sağ ve sol izomerlerini birbirinden izole etmek."},
    {"kelime": "farmakodinamik modelleme yapmak", "yasakli_kelimeler": ["ilacın vücuda etkisi", "konsantrasyon-etki eğrisi", "emax", "ec50", "mekanizma"], "zorluk": "zor", "aciklama": "İlacın hedef dokudaki konsantrasyonu ile oluşturduğu biyolojik cevabı denkleştirmek."},
    {"kelime": "ters agonist aktivite sergilemek", "yasakli_kelimeler": ["inverse agonist", "bazal aktiviteyi düşürme", "negatif etkinlik", "reseptör", "gaba"], "zorluk": "zor", "aciklama": "Reseptörün yapısal bazal aktivitesini temel seviyenin dahi altına indirmek."},
    {"kelime": "teratojenik riski belirlemek", "yasakli_kelimeler": ["gebelik kategorisi", "fötal anomali", "sakat doğum", "embriyo toksisitesi", "gebe"], "zorluk": "zor", "aciklama": "İlacın anne karnındaki fetüste yapısal bozukluk yapma olasılığını sınıflandırmak."},
    {"kelime": "farmakogenomik test uygulamak", "yasakli_kelimeler": ["genetik polimorfizm", "bireyselleştirilmiş doz", "dna", "hızlı yavaş metabolize eden", "ilaç yanıtı"], "zorluk": "zor", "aciklama": "Hastanın gen profiline bakarak ilacı metabolize etme hızını önceden belirlemek."}
]

# 14. felsefe
felsefe_verbs = [
    # Kolay (12)
    {"kelime": "felsefe yapmak", "yasakli_kelimeler": ["düşünmek", "sorgulamak", "fikir", "akıl", "tartışmak"], "zorluk": "kolay", "aciklama": "Varlık, bilgi ve ahlak üzerine derinlemesine kafa yormak."},
    {"kelime": "hayatı sorgulamak", "yasakli_kelimeler": ["anlam", "yaşam", "neden", "dünya", "amaç"], "zorluk": "kolay", "aciklama": "Yaşamın gayesini ve insanın varoluşunu düşünmek."},
    {"kelime": "kitap okumak", "yasakli_kelimeler": ["filozof", "sayfa", "metin", "yazar", "öğrenmek"], "zorluk": "kolay", "aciklama": "Felsefi eserleri okuyarak yeni fikirlerle tanışmak."},
    {"kelime": "tartışmak", "yasakli_kelimeler": ["fikir", "görüş", "karşıt", "konuşmak", "diyalog"], "zorluk": "kolay", "aciklama": "Farklı görüşleri karşılıklı olarak savunup konuşmak."},
    {"kelime": "doğruyu aramak", "yasakli_kelimeler": ["hakikat", "gerçek", "yanılmamak", "bulmak", "bilgi"], "zorluk": "kolay", "aciklama": "Her türlü yanılgıdan uzak en temel gerçeğin peşine düşmek."},
    {"kelime": "merak etmek", "yasakli_kelimeler": ["öğrenmek", "soru", "ilgi", "neden", "anlamak"], "zorluk": "kolay", "aciklama": "Bilinmeyene karşı zihinsel ilgi ve araştırma arzusu duymak."},
    {"kelime": "fikir yürütmek", "yasakli_kelimeler": ["akıl", "tahmin", "görüş", "düşünce", "mantık"], "zorluk": "kolay", "aciklama": "Bir konu hakkında akla dayalı varsayımlar geliştirmek."},
    {"kelime": "eleştirmek", "yasakli_kelimeler": ["hata", "kusur", "değerlendirme", "doğru değil", "sorgulama"], "zorluk": "kolay", "aciklama": "Bir fikrin eksik ve zayıf yönlerini ortaya koymak."},
    {"kelime": "kendini bilmek", "yasakli_kelimeler": ["sokrates", "tanımak", "insan", "farkındalık", "ruh"], "zorluk": "kolay", "aciklama": "Kendi zayıflıklarının, sınırlarının ve özünün bilincine varmak."},
    {"kelime": "yazı yazmak", "yasakli_kelimeler": ["makale", "deneme", "kalem", "fikir", "metin"], "zorluk": "kolay", "aciklama": "Felsefi düşünceleri yazıya dökerek ifade etmek."},
    {"kelime": "sessizce düşünmek", "yasakli_kelimeler": ["tefekkür", "yalnız", "sakin", "zihin", "odaklanmak"], "zorluk": "kolay", "aciklama": "Gürültüden uzak derin bir tefekkür haline geçmek."},
    {"kelime": "insanı anlamak", "yasakli_kelimeler": ["davranış", "ruh", "toplum", "psikoloji", "öz"], "zorluk": "kolay", "aciklama": "İnsanın varoluşsal doğasını ve psikolojisini kavramak."},

    # Orta (24)
    {"kelime": "varoluşu sorgulamak", "yasakli_kelimeler": ["varlık", "öz", "varoluşçuluk", "sartre", "neden varız"], "zorluk": "orta", "aciklama": "İnsanın bu dünyada var olmasının anlamını düşünmek."},
    {"kelime": "özgür iradeyi tartışmak", "yasakli_kelimeler": ["kader", "seçim", "determinizm", "karar", "sorumluluk"], "zorluk": "orta", "aciklama": "İnsanın kararlarında gerçekten özgür olup olmadığını incelemek."},
    {"kelime": "tez ileri sürmek", "yasakli_kelimeler": ["sav", "iddia", "argüman", "önerme", "savunmak"], "zorluk": "orta", "aciklama": "Doğruluğunu kanıtlamaya çalışacağı temel bir düşünce ortaya atmak."},
    {"kelime": "antitez üretmek", "yasakli_kelimeler": ["karşı sav", "itiraz", "diyalektik", "zıt görüş", "çelişki"], "zorluk": "orta", "aciklama": "Öne sürülen tezin eksikliğini gösteren zıt iddiayı formüle etmek."},
    {"kelime": "senteze ulaşmak", "yasakli_kelimeler": ["hegel", "tez antitez", "birleşim", "üst aşama", "bütünleştirme"], "zorluk": "orta", "aciklama": "Karşıt fikirlerin çatışmasından daha üst ve kapsayıcı bir sonuca varmak."},
    {"kelime": "maieutik yöntemi uygulamak", "yasakli_kelimeler": ["doğurtma", "sokrates", "soru sorma", "zihindeki bilgi", "diyalog"], "zorluk": "orta", "aciklama": "Ustaca sorularla muhatabın zihnindeki saklı bilgileri açığa çıkarmak."},
    {"kelime": "paradoks keşfetmek", "yasakli_kelimeler": ["çelişki", "içinden çıkılmaz", "mantık çıkmazı", "zenon", "önerme"], "zorluk": "orta", "aciklama": "Kendi içinde çözümsüz gibi görünen mantıksal çelişkiyi yakalamak."},
    {"kelime": "ontolojik soru sormak", "yasakli_kelimeler": ["varlık nedir", "töz", "metafizik", "madde ruh", "varoluş"], "zorluk": "orta", "aciklama": "Varlığın mahiyeti ve kökenine dair temel sorular yöneltmek."},
    {"kelime": "metafizik spekülasyon yapmak", "yasakli_kelimeler": ["fizik ötesi", "duyu dışı", "tanrı", "ruh", "soyut"], "zorluk": "orta", "aciklama": "Duyusal alanın ötesindeki varlık boyutları üzerine fikir yürütmek."},
    {"kelime": "öznelliği eleştirmek", "yasakli_kelimeler": ["subjektif", "kişisel", "nesnellik", "görecelilik", "taraflı"], "zorluk": "orta", "aciklama": "Yargıların kişisel duygu ve algılara dayanmasını eleştiriye açmak."},
    {"kelime": "nesnelliği savunmak", "yasakli_kelimeler": ["objektif", "kişiden bağımsız", "genel geçer", "bilimsel", "olgusal"], "zorluk": "orta", "aciklama": "Hakikatin insan zihninden ve bakış açısından bağımsız olduğunu savunmak."},
    {"kelime": "aksiyom kabul etmek", "yasakli_kelimeler": ["ispatsız", "apaçık", "temel ilke", "öncül", "kabulleniş"], "zorluk": "orta", "aciklama": "Doğruluğu kendiliğinden açık kabul edilen temel önermeyi çıkış noktası almak."},
    {"kelime": "estetik haz duymak", "yasakli_kelimeler": ["sanat", "güzellik", "beğeni", "yüce", "duygu"], "zorluk": "orta", "aciklama": "Güzel bir sanat eseri veya doğa karşısında felsefi bir tatmin yaşamak."},
    {"kelime": "determinizmi savunmak", "yasakli_kelimeler": ["belirlenimcilik", "sebep sonuç", "özgürlük yok", "nedensellik", "zorunluluk"], "zorluk": "orta", "aciklama": "Her olayın ve tercihin öncül sebeplerce zorunlu kılındığını savunmak."},
    {"kelime": "nihilizme kapılmak", "yasakli_kelimeler": ["hiççilik", "anlamsızlık", "hiçbir değer yok", "nietzsche", "boşluk"], "zorluk": "orta", "aciklama": "Evrende hiçbir nesnel anlam ve değer olmadığı fikrini benimsemek."},
    {"kelime": "stoacı sükunet korumak", "yasakli_kelimeler": ["ataraksia", "kontrol dışı", "kabullenme", "epiktetos", "dinginlik"], "zorluk": "orta", "aciklama": "Kontrolü dışındaki olaylara karşı kayıtsız ve içsel olarak dingin kalmak."},
    {"kelime": "akılcılığı benimsemek", "yasakli_kelimeler": ["rasyonalizm", "descartes", "deney üstü", "saf zihin", "mantık"], "zorluk": "orta", "aciklama": "Bilginin yegane güvenilir kaynağının akıl olduğunu savunmak."},
    {"kelime": "deneyimciliği savunmak", "yasakli_kelimeler": ["empirizm", "john locke", "boş levha", "duyum", "tecrübe"], "zorluk": "orta", "aciklama": "Zihinde doğuştan hiçbir bilgi olmadığını, her şeyin deneyimle geldiğini savunmak."},
    {"kelime": "materyalist bakmak", "yasakli_kelimeler": ["maddecilik", "fiziksel", "ruh reddi", "atom", "somut"], "zorluk": "orta", "aciklama": "Evrendeki tek gerçekliğin madde ve hareket olduğunu kabul etmek."},
    {"kelime": "idealist yaklaşmak", "yasakli_kelimeler": ["fikir", "zihin", "madde ikincil", "platon", "düşünce"], "zorluk": "orta", "aciklama": "Gerçekliğin temelinde maddeden ziyade fikir ve bilincin yattığını savunmak."},
    {"kelime": "ahlak yasası koymak", "yasakli_kelimeler": ["kural", "ödev", "evrensel", "davranış", "norm"], "zorluk": "orta", "aciklama": "İnsan davranışlarını yönetecek rasyonel ahlaki ilkeler formüle etmek."},
    {"kelime": "ironi yapmak", "yasakli_kelimeler": ["sokrates", "alay", "bilmezlikten gelme", "tersini söyleme", "diyalog"], "zorluk": "orta", "aciklama": "Muhatabın bilgisizliğini ortaya çıkarmak için bilmiyormuş gibi davranmak."},
    {"kelime": "zihin felsefesi yapmak", "yasakli_kelimeler": ["bilinç", "beden", "beyin", "yapay zeka", "niteliksel deneyim"], "zorluk": "orta", "aciklama": "Bilinç hallerinin fiziksel beyinle olan ilişkisini sorgulamak."},
    {"kelime": "felsefi akım kurmak", "yasakli_kelimeler": ["ekol", "öğreti", "filozof", "manifesto", "takipçi"], "zorluk": "orta", "aciklama": "Özgün düşünceler etrafında yeni bir felsefe okulu başlatmak."},

    # Zor (14)
    {"kelime": "tözü tanımlamak", "yasakli_kelimeler": ["cevher", "substantia", "spinoza", "kendi başına var olan", "öz"], "zorluk": "zor", "aciklama": "Varlığını sürdürmek için başka hiçbir şeye muhtaç olmayan temel cevheri izah etmek."},
    {"kelime": "epokhe yapmak", "yasakli_kelimeler": ["yargıyı askıya alma", "pyrrhon", "husserl", "tarafsızlık", "şüphe"], "zorluk": "zor", "aciklama": "Dış dünya veya iddialar hakkında her türlü hüküm ve yargıyı askıya almak."},
    {"kelime": "dasein analizini yapmak", "yasakli_kelimeler": ["heidegger", "orada varlık", "dünyada olmak", "fırlatılmışlık", "ölüme doğru varlık"], "zorluk": "zor", "aciklama": "İnsanın dünyaya fırlatılmış varoluşunun ontolojik yapısını incelemek."},
    {"kelime": "aporiye düşmek", "yasakli_kelimeler": ["çıkmaz", "tıkanma", "çözümsüzlük", "platon diyalogları", "şaşkınlık"], "zorluk": "zor", "aciklama": "Felsefi akıl yürütmede mantıksal bir çıkmaza ve yanıtsızlığa saplanıp kalmak."},
    {"kelime": "teleolojik erek aramak", "yasakli_kelimeler": ["gaye", "amaçlılık", "ereksellik", "aristoteles", "nihai hedef"], "zorluk": "zor", "aciklama": "Olayların ve varlıkların arkasındaki nihai varoluş gayesini aramak."},
    {"kelime": "übermensch idealini kavramak", "yasakli_kelimeler": ["üstinsan", "nietzsche", "kendi değerini yaratma", "bengi dönüş", "güç istenci"], "zorluk": "zor", "aciklama": "Geleneksel ahlakı aşıp kendi değerlerini sıfırdan inşa eden insan tipini anlamak."},
    {"kelime": "monadolojiyi incelemek", "yasakli_kelimeler": ["leibniz", "bölünemez birimler", "penceresiz", "önceden kurulmuş uyum", "ruhsal töz"], "zorluk": "zor", "aciklama": "Evrenin bölünemez, penceresiz ruhsal atomlardan oluştuğu teorisini çalışmak."},
    {"kelime": "solipsist argüman geliştirmek", "yasakli_kelimeler": ["tekbencilik", "sadece benim bilincim", "dış dünyanın ispatsızlığı", "descartes", "ben"], "zorluk": "zor", "aciklama": "Kendi zihni dışındaki hiçbir varlığın kanıtlanamayacağı iddiasını kurmak."},
    {"kelime": "tabula rasa varsaymak", "yasakli_kelimeler": ["boş levha", "john locke", "doğuştan fikir yokluğu", "deney", "zihin"], "zorluk": "zor", "aciklama": "Zihnin doğuşta tertemiz boş bir yazı tahtası olduğunu kabul etmek."},
    {"kelime": "panenteizmi savunmak", "yasakli_kelimeler": ["kamutanrıcılık", "her şey tanrıda", "içkin aşkın", "vahdet-i vücud", "evren"], "zorluk": "zor", "aciklama": "Evrenin Tanrı'nın içinde olduğunu ama Tanrı'nın evrene indirgenemeyeceğini savunmak."},
    {"kelime": "qualia problemini çözmek", "yasakli_kelimeler": ["niteliksel deneyim", "kırmızılık hissi", "bilinç", "chalmers", "öznel yaşantı"], "zorluk": "zor", "aciklama": "Duyusal algıların yarattığı öznel hislerin fiziksel beyne nasıl indirgeneceğini tartışmak."},
    {"kelime": "dekonstrüksiyon uygulamak", "yasakli_kelimeler": ["yapısöküm", "derrida", "ikili karşıtlıkları bozma", "metin analizi", "anlam çoğulluğu"], "zorluk": "zor", "aciklama": "Metindeki hiyerarşik anlam kalıplarını ve zıtlıkları yapısal olarak çözmek."},
    {"kelime": "noumenon alanına işaret etmek", "yasakli_kelimeler": ["kendinde şey", "kant", "bilinemez", "fenomen karşıtı", "saf akıl"], "zorluk": "zor", "aciklama": "Duyularla algılanamayan, aklın deneyimleyemediği 'kendinde varlık' alanına dikkat çekmek."},
    {"kelime": "kötülük problemini teodise ile aşmak", "yasakli_kelimeler": ["tanrının adaleti", "acı", "leibniz", "özgür irade savunması", "mutlak iyi"], "zorluk": "zor", "aciklama": "Dünyadaki kötülüklerin varlığı ile Tanrı'nın mutlak iyiliğini bağdaştırmaya çalışmak."}
]

add_and_save_verbs('farmakoloji', farmakoloji_verbs)
add_and_save_verbs('felsefe', felsefe_verbs)
print('P7 done!')
