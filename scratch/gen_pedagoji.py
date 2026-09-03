# -*- coding: utf-8 -*-
import json
import os

cards = [
    {
        "id": 1,
        "kategori": "pedagoji",
        "kelime": "yapılandırmacılık",
        "aciklama": "öğrenenin bilgiyi pasif almak yerine kendi deneyimleriyle aktif olarak zihninde inşa ettiği kuram.",
        "yasakli_kelimeler": ["konstruktivizm", "piaget", "vygotsky", "inşa", "aktif öğrenme"]
    },
    {
        "id": 2,
        "kategori": "pedagoji",
        "kelime": "yakınsak gelişim alanı",
        "aciklama": "çocuğun tek başına yapabildiği ile bir yetişkin rehberliğinde başarabileceği arasındaki gelişimsel potansiyel mesafe.",
        "yasakli_kelimeler": ["vygotsky", "zpd", "potansiyel", "rehber", "mesafe"]
    },
    {
        "id": 3,
        "kategori": "pedagoji",
        "kelime": "iskele kurma",
        "aciklama": "öğrenci bağımsızlaşana kadar öğretmenin sunduğu kademeli desteği zamanla azaltması tekniği.",
        "yasakli_kelimeler": ["scaffolding", "bruner", "destek", "kademeli", "özerklik"]
    },
    {
        "id": 4,
        "kategori": "pedagoji",
        "kelime": "akran öğrenmesi",
        "aciklama": "aynı düzeydeki öğrencilerin birbirlerine konuları anlatarak ve tartışarak öğrendiği işbirlikli model.",
        "yasakli_kelimeler": ["arkadaş", "işbirliği", "akran", "yardımlaşma", "grup"]
    },
    {
        "id": 5,
        "kategori": "pedagoji",
        "kelime": "tersyüz öğrenme",
        "aciklama": "kuramsal bilginin evde videolarla öğrenildiği, sınıf ortamının ise tamamen uygulamaya ayrıldığı model.",
        "yasakli_kelimeler": ["flipped classroom", "video", "ev", "uygulama", "sınıf içi"]
    },
    {
        "id": 6,
        "kategori": "pedagoji",
        "kelime": "biçimlendirici değerlendirme",
        "aciklama": "öğrenme süreci devam ederken eksikleri tespit edip geri bildirim vermek için yapılan notsuz ölçme.",
        "yasakli_kelimeler": ["formative", "geri bildirim", "süreç", "gelişim", "not verme"]
    },
    {
        "id": 7,
        "kategori": "pedagoji",
        "kelime": "düzey belirleyici değerlendirme",
        "aciklama": "dönem veya ünite sonunda öğrencinin başarı düzeyini tespit etmek amacıyla yapılan notlandırma sınavı.",
        "yasakli_kelimeler": ["summative", "final", "not", "sınav", "dönem sonu"]
    },
    {
        "id": 8,
        "kategori": "pedagoji",
        "kelime": "öz düzenlemeli öğrenme",
        "aciklama": "bireyin kendi hedeflerini koyup öğrenme sürecini, zamanını ve motivasyonunu bağımsızca yönetebilme yetisi.",
        "yasakli_kelimeler": ["zimmerman", "özerklik", "hedef", "planlama", "otokontrol"]
    },
    {
        "id": 9,
        "kategori": "pedagoji",
        "kelime": "üstbiliş",
        "aciklama": "kişinin kendi düşünme, anlama ve öğrenme süreçlerinin farkında olması ve bunları denetlemesi.",
        "yasakli_kelimeler": ["metakognisyon", "farkındalık", "düşünmeyi düşünme", "flavell", "strateji"]
    },
    {
        "id": 10,
        "kategori": "pedagoji",
        "kelime": "farklılaştırılmış öğretim",
        "aciklama": "sınıftaki öğrencilerin bireysel hız, ilgi ve öğrenme profillerine göre içeriğin ve sürecin çeşitlendirilmesi.",
        "yasakli_kelimeler": ["tomlinson", "bireysel fark", "uyarlama", "profil", "çeşitlilik"]
    },
    {
        "id": 11,
        "kategori": "pedagoji",
        "kelime": "montessori yöntemi",
        "aciklama": "özel tasarlanmış materyallerle çocuğun kendi hızında ve seçiminde özgürce çalışmasını sağlayan pedagoji.",
        "yasakli_kelimeler": ["maria montessori", "materyal", "özgür seçim", "çocuk merkezli", "özerklik"]
    },
    {
        "id": 12,
        "kategori": "pedagoji",
        "kelime": "waldorf pedagojisi",
        "aciklama": "rudolf steiner kökenli, sanat, doğa ve hayal gücünü akademik bilginin önüne koyan bütüncül yaklaşım.",
        "yasakli_kelimeler": ["rudolf steiner", "sanat", "doğa", "bütüncül", "hayal gücü"]
    },
    {
        "id": 13,
        "kategori": "pedagoji",
        "kelime": "reggio emilia yaklaşımı",
        "aciklama": "çocuğun yüz dili olduğunu savunan ve çevreyi üçüncü öğretmen kabul eden katılımcı okul modeli.",
        "yasakli_kelimeler": ["yüz dil", "malaguzzi", "üçüncü öğretmen", "proje", "çevre"]
    },
    {
        "id": 14,
        "kategori": "pedagoji",
        "kelime": "problem dayalı öğrenme",
        "aciklama": "öğrencilerin gerçek hayattan karmaşık bir senaryoyu grupça araştırarak çözdüğü öğrenme tekniği.",
        "yasakli_kelimeler": ["senaryo", "araştırma", "problem çözme", "vaka", "otantik"]
    },
    {
        "id": 15,
        "kategori": "pedagoji",
        "kelime": "proje tabanlı öğrenme",
        "aciklama": "öğrencilerin uzun soluklu bir araştırma sonucunda somut bir ürün veya sunum geliştirdiği yöntem.",
        "yasakli_kelimeler": ["ürün", "araştırma", "sergi", "somut", "grup çalışması"]
    },
    {
        "id": 16,
        "kategori": "pedagoji",
        "kelime": "buluş yoluyla öğrenme",
        "aciklama": "öğretmenin rehberliğinde öğrencinin örnekleri inceleyerek genel kurala veya ilkeye kendisinin ulaştığı model.",
        "yasakli_kelimeler": ["bruner", "tümevarım", "keşif", "örnek", "kural"]
    },
    {
        "id": 17,
        "kategori": "pedagoji",
        "kelime": "sunuş yoluyla öğretim",
        "aciklama": "bilgilerin öğretmen tarafından organize edilip kavram haritaları ve ön örgütleyicilerle anlamlı aktarılması.",
        "yasakli_kelimeler": ["ausubel", "ön örgütleyici", "anlamlı öğrenme", "tümdengelim", "aktarım"]
    },
    {
        "id": 18,
        "kategori": "pedagoji",
        "kelime": "tam öğrenme modeli",
        "aciklama": "ek süre ve nitelikli öğretim olanakları sağlandığında sınıftaki her öğrencinin hedefe ulaşabileceği kuram.",
        "yasakli_kelimeler": ["bloom", "ek süre", "yüzde yetmiş", "ünite", "tamamlama"]
    },
    {
        "id": 19,
        "kategori": "pedagoji",
        "kelime": "bloom taksonomisi",
        "aciklama": "bilişsel hedefleri hatırlamadan yaratmaya kadar hiyerarşik altı basamağa ayıran sınıflandırma.",
        "yasakli_kelimeler": ["hatırlama", "anlama", "uygulama", "analiz", "değerlendirme"]
    },
    {
        "id": 20,
        "kategori": "pedagoji",
        "kelime": "çoklu zeka kuramı",
        "aciklama": "insan zekâsının tekil bir iq puanından ibaret olmayıp müzik, doğa, kinestetik gibi alanlara ayrıldığı model.",
        "yasakli_kelimeler": ["howard gardner", "alan", "iq", "bedensel", "müzikal"]
    },
    {
        "id": 21,
        "kategori": "pedagoji",
        "kelime": "eleştirel pedagoji",
        "aciklama": "eğitimin ezilenlerin bilinçlenmesi ve toplumsal adaletsizliklere karşı direniş aracı olduğunu savunan yaklaşım.",
        "yasakli_kelimeler": ["paulo freire", "ezilenler", "özgürleşme", "bilinçlenme", "adalet"]
    },
    {
        "id": 22,
        "kategori": "pedagoji",
        "kelime": "bankacı eğitim modeli",
        "aciklama": "öğrenciyi boş bir hesap, öğretmeni ise oraya pasif bilgi yatıran otorite sayan geleneksel eğitim eleştirisi.",
        "yasakli_kelimeler": ["freire", "pasif alıcı", "hesap", "geleneksel", "eleştiri"]
    },
    {
        "id": 23,
        "kategori": "pedagoji",
        "kelime": "örtük program",
        "aciklama": "resmi ders programında yazılı olmayan ancak okul kültürü ve kurallarıyla örtükçe aşılanan değerler.",
        "yasakli_kelimeler": ["gizli müfredat", "yazısız", "okul kültürü", "sosyalleşme", "norm"]
    },
    {
        "id": 24,
        "kategori": "pedagoji",
        "kelime": "açık müfredat",
        "aciklama": "milli eğitim veya okul tarafından onaylanan, ders kitaplarında resmen yer alan planlı öğretim programı.",
        "yasakli_kelimeler": ["resmi program", "yazılı", "ders planı", "kazanım", "müfredat"]
    },
    {
        "id": 25,
        "kategori": "pedagoji",
        "kelime": "ihmal edilen program",
        "aciklama": "okullarda bilinçli ya da kayıtsızlıkla müfredat dışı bırakılan, öğretilmemesi tercih edilen konular bütünü.",
        "yasakli_kelimeler": ["eisner", "öğretilmeyen", "yok sayılan", "dışlanan", "müfredat"]
    },
    {
        "id": 26,
        "kategori": "pedagoji",
        "kelime": "deneyimsel öğrenme",
        "aciklama": "bilginin somut yaşantı, yansıtıcı gözlem, soyut kavramsallaştırma ve aktif deney döngüsüyle oluşması.",
        "yasakli_kelimeler": ["kolb", "yaşantı", "döngü", "yansıtma", "deney"]
    },
    {
        "id": 27,
        "kategori": "pedagoji",
        "kelime": "yansıtıcı düşünme",
        "aciklama": "öğretmenin veya öğrencinin geçmiş uygulamalarını eleştirel gözden geçirerek geleceğe yönelik ders çıkarması.",
        "yasakli_kelimeler": ["john dewey", "schön", "öz değerlendirme", "deneyim", "gözden geçirme"]
    },
    {
        "id": 28,
        "kategori": "pedagoji",
        "kelime": "eylem araştırması",
        "aciklama": "öğretmenin kendi sınıfındaki sorunları tespit edip çözmek için yürüttüğü pratik odaklı bilimsel çalışma.",
        "yasakli_kelimeler": ["aksiyon", "sınıf içi", "öğretmen", "uygulama", "iyileştirme"]
    },
    {
        "id": 29,
        "kategori": "pedagoji",
        "kelime": "rubrik",
        "aciklama": "öğrenci performansını objektif ölçmek amacıyla başarı ölçütlerini ve puan düzeylerini gösteren dereceli puanlama anahtarı.",
        "yasakli_kelimeler": ["puanlama anahtarı", "kriter", "dereceli", "ölçüt", "değerlendirme"]
    },
    {
        "id": 30,
        "kategori": "pedagoji",
        "kelime": "öğrenci portfolyosu",
        "aciklama": "öğrencinin dönem boyunca gösterdiği gelişim ve ürünleri sistematik biçimde bir araya getiren gelişim dosyası.",
        "yasakli_kelimeler": ["gelişim dosyası", "ürün seçkisi", "koleksiyon", "belge", "değerlendirme"]
    },
    {
        "id": 31,
        "kategori": "pedagoji",
        "kelime": "kapsayıcı eğitim",
        "aciklama": "engelliler ve dezavantajlı çocuklar dahil tüm öğrencilerin genel eğitim ortamında eşitçe yer almasını sağlama.",
        "yasakli_kelimeler": ["özel eğitim", "kaynaştırma", "farklılık", "bütünleştirme", "eşitlik"]
    },
    {
        "id": 32,
        "kategori": "pedagoji",
        "kelime": "bireyselleştirilmiş eğitim programı",
        "aciklama": "özel gereksinimli bir öğrencinin ihtiyaçlarına, hedeflerine ve destek hizmetlerine göre hazırlanan kişisel plan.",
        "yasakli_kelimeler": ["bep", "özel gereksinim", "kişisel plan", "uyarlama", "engelli"]
    },
    {
        "id": 33,
        "kategori": "pedagoji",
        "kelime": "kaynaştırma eğitimi",
        "aciklama": "özel eğitime ihtiyacı olan öğrencilerin akranlarıyla aynı sınıfta uygun uyarlamalarla ders alması.",
        "yasakli_kelimeler": ["bütünleştirme", "akran", "normal sınıf", "özel gereksinim", "uyarlama"]
    },
    {
        "id": 34,
        "kategori": "pedagoji",
        "kelime": "sınıf yönetimi",
        "aciklama": "öğrenmenin verimli gerçekleşmesi için sınıf ortamının, kurallarının ve zamanının etkili organize edilmesi.",
        "yasakli_kelimeler": ["disiplin", "düzen", "zaman", "kurallar", "öğretmen otoritesi"]
    },
    {
        "id": 35,
        "kategori": "pedagoji",
        "kelime": "pygmalion etkisi",
        "aciklama": "öğretmenin öğrenciden yüksek beklenti duymasının o öğrencinin akademik başarısını gerçekten artırması.",
        "yasakli_kelimeler": ["beklenti", "rosenthal", "kendini gerçekleştiren kehanet", "başarı", "öğretmen"]
    },
    {
        "id": 36,
        "kategori": "pedagoji",
        "kelime": "öğrenilmiş çaresizlik",
        "aciklama": "öğrencinin geçmişteki başarısızlıklar sebebiyle gelecekteki durumlarda da çaba göstermeyi tamamen bırakması.",
        "yasakli_kelimeler": ["seligman", "başarısızlık", "vazgeçme", "inançsızlık", "çaba"]
    },
    {
        "id": 37,
        "kategori": "pedagoji",
        "kelime": "içsel motivasyon",
        "aciklama": "bireyin not veya ödül beklentisi olmadan yalnızca merak, öğrenme zevki ve ilgi duyduğu için çalışması.",
        "yasakli_kelimeler": ["dışsal", "ödül", "merak", "istek", "kendi kendine"]
    },
    {
        "id": 38,
        "kategori": "pedagoji",
        "kelime": "dışsal motivasyon",
        "aciklama": "öğrencinin sadece yüksek not almak, ceza almamak veya övgü kazanmak amacıyla öğrenme davranışı göstermesi.",
        "yasakli_kelimeler": ["içsel", "not", "ödül", "ceza", "baskı"]
    },
    {
        "id": 39,
        "kategori": "pedagoji",
        "kelime": "gelişim zihniyeti",
        "aciklama": "zeka ve yeteneklerin çaba, etkili stratejiler ve pratikle sürekli geliştirilebileceğine olan inanç.",
        "yasakli_kelimeler": ["carol dweck", "growth mindset", "çaba", "zeka gelişimi", "sabit zihniyet"]
    },
    {
        "id": 40,
        "kategori": "pedagoji",
        "kelime": "sabit zihniyet",
        "aciklama": "zeka ve kabiliyetin doğuştan geldiğine ve sonradan hiçbir şekilde değiştirilemeyeceğine dair inanç.",
        "yasakli_kelimeler": ["fixed mindset", "dweck", "değişmezlik", "doğuştan yetenek", "kader"]
    },
    {
        "id": 41,
        "kategori": "pedagoji",
        "kelime": "mikroöğretim",
        "aciklama": "öğretmen adaylarının küçük bir gruba kısa bir ders sunup ardından video kayıtlarıyla dönüt aldığı yöntem.",
        "yasakli_kelimeler": ["öğretmen eğitimi", "kamera", "dönüt", "kısa ders", "simülasyon"]
    },
    {
        "id": 42,
        "kategori": "pedagoji",
        "kelime": "jigsaw tekniği",
        "aciklama": "öğrencilerin uzmanlık gruplarına ayrılarak bir parçayı öğrenip asıl gruplarına dönerek birbirlerine öğrettiği teknik.",
        "yasakli_kelimeler": ["ayrılıp birleşme", "işbirlikli", "uzmanlık", "parça", "akran"]
    },
    {
        "id": 43,
        "kategori": "pedagoji",
        "kelime": "altı şapkalı düşünme",
        "aciklama": "bireylerin farklı şapkaları takarak tarafsız, duygusal, eleştirel ve yaratıcı bakış açılarını sırayla denediği yöntem.",
        "yasakli_kelimeler": ["edward de bono", "şapka", "renkler", "bakış açısı", "düşünme"]
    },
    {
        "id": 44,
        "kategori": "pedagoji",
        "kelime": "istasyon tekniği",
        "aciklama": "sınıfta farklı görev masalarının kurulduğu ve grupların sırayla masaları gezerek işi tamamladığı yöntem.",
        "yasakli_kelimeler": ["masa", "tur", "dönüşüm", "grup", "katkı"]
    },
    {
        "id": 45,
        "kategori": "pedagoji",
        "kelime": "kartopu tekniği",
        "aciklama": "öğrencilerin önce bireysel, sonra ikişerli, dörderli ve tüm sınıf halinde tartışmayı büyüterek sürdürdüğü yöntem.",
        "yasakli_kelimeler": ["çift", "büyüme", "tartışma", "bireysel", "gruplaşma"]
    },
    {
        "id": 46,
        "kategori": "pedagoji",
        "kelime": "balık kılçığı tekniği",
        "aciklama": "karmaşık bir problemin alt nedenlerini bir balık iskeleti biçimindeki şemaya yerleştirerek analiz etme.",
        "yasakli_kelimeler": ["ishikawa", "neden sonuç", "diyagram", "iskelet", "problem"]
    },
    {
        "id": 47,
        "kategori": "pedagoji",
        "kelime": "kavram haritası",
        "aciklama": "kavramlar arasındaki hiyerarşik ve anlamsal ilişkileri kutular ve bağlayıcı ifadelerle gösteren görsel araç.",
        "yasakli_kelimeler": ["novak", "şema", "ilişki", "grafik", "bağlantı"]
    },
    {
        "id": 48,
        "kategori": "pedagoji",
        "kelime": "zihin haritası",
        "aciklama": "merkezi bir fikirden dışarıya doğru renkler, semboller ve dallarla yayılan yaratıcı not tutma tekniği.",
        "yasakli_kelimeler": ["tony buzan", "dal", "renk", "merkez", "beyin"]
    },
    {
        "id": 49,
        "kategori": "pedagoji",
        "kelime": "kavram yanılgısı",
        "aciklama": "öğrencinin bilimsel gerçeklerle uyuşmayan, kendi zihninde yanlış biçimde yapılandırdığı köklü kanaat.",
        "yasakli_kelimeler": ["yanlış anlama", "misconception", "bilimsel hata", "düzeltme", "şema"]
    },
    {
        "id": 50,
        "kategori": "pedagoji",
        "kelime": "kavramsal değişim metni",
        "aciklama": "öğrencinin mevcut yanılgısını çürütüp yerine bilimsel doğruyu mantıksal açıklamalarla ikna eden öğretim materyali.",
        "yasakli_kelimeler": ["metin", "yanılgı giderme", "dengesizlik", "yeni kavram", "posner"]
    },
    {
        "id": 51,
        "kategori": "pedagoji",
        "kelime": "öz yeterlik",
        "aciklama": "bireyin belirli bir görevi veya akademik hedefi başarıyla tamamlayabileceğine dair kendi kapasitesine olan inancı.",
        "yasakli_kelimeler": ["bandura", "inanç", "kapasite", "güven", "başarı"]
    },
    {
        "id": 52,
        "kategori": "pedagoji",
        "kelime": "sosyal öğrenme kuramı",
        "aciklama": "insanların başkalarının davranışlarını gözlemleyerek ve model alarak yeni davranışlar edindiğini savunan teori.",
        "yasakli_kelimeler": ["albert bandura", "model alma", "taklit", "gözlem", "bobo bebeği"]
    },
    {
        "id": 53,
        "kategori": "pedagoji",
        "kelime": "dolaylı pekiştirme",
        "aciklama": "model alınan kişinin ödüllendirildiğini gören bireyin o davranışı sergileme eğiliminin artması.",
        "yasakli_kelimeler": ["model", "ödül", "pekiştireç", "gözlem", "bandura"]
    },
    {
        "id": 54,
        "kategori": "pedagoji",
        "kelime": "edimsel koşullanma",
        "aciklama": "davranışların ardından gelen pekiştireç veya cezalar sonucunda sıklığının değişmesi esasına dayanan öğrenme.",
        "yasakli_kelimeler": ["skinner", "ödül", "ceza", "pekiştirme", "davranışçılık"]
    },
    {
        "id": 55,
        "kategori": "pedagoji",
        "kelime": "klasik koşullanma",
        "aciklama": "nötr bir uyarıcının koşulsuz bir uyarıcıyla eşleşerek aynı refleksi veya tepkiyi tetikler hale gelmesi.",
        "yasakli_kelimeler": ["pavlov", "köpek", "salya", "zil", "refleks"]
    },
    {
        "id": 56,
        "kategori": "pedagoji",
        "kelime": "premack ilkesi",
        "aciklama": "yapılma olasılığı yüksek bir etkinliğin yapılma olasılığı düşük bir görevi ödüllendirmek için kullanılması kuralı.",
        "yasakli_kelimeler": ["büyükanne kuralı", "etkinlik pekiştireci", "ödül", "koşul", "ödev"]
    },
    {
        "id": 57,
        "kategori": "pedagoji",
        "kelime": "kademeli yaklaşma",
        "aciklama": "öğrenciye kazandırılmak istenen karmaşık bir davranışın alt basamaklara bölünerek adım adım pekiştirilmesi.",
        "yasakli_kelimeler": ["biçimlendirme", "shaping", "adım adım", "hedef davranış", "pekiştirme"]
    },
    {
        "id": 58,
        "kategori": "pedagoji",
        "kelime": "bilişsel yük kuramı",
        "aciklama": "çalışma belleğinin sınırlı kapasitesi göz önüne alınarak öğretim materyallerinin aşırı yük bindirmeden tasarlanması ilkesi.",
        "yasakli_kelimeler": ["sweller", "çalışma belleği", "kapasite", "aşırı yük", "bellek"]
    },
    {
        "id": 59,
        "kategori": "pedagoji",
        "kelime": "ikili kodlama kuramı",
        "aciklama": "bilginin belleğe hem sözel hem de görsel kanallardan ayrı ayrı kodlandığında daha kalıcı öğrenildiği modeli.",
        "yasakli_kelimeler": ["paivio", "sözel", "görsel", "çift kanal", "hafıza"]
    },
    {
        "id": 60,
        "kategori": "pedagoji",
        "kelime": "aralıklı tekrar",
        "aciklama": "öğrenilen bilgilerin zamanla unutulmasını önlemek için giderek artan zaman aralıklarıyla gözden geçirilmesi tekniği.",
        "yasakli_kelimeler": ["spaced repetition", "ebbinghaus", "unutma eğrisi", "tekrar", "hafıza"]
    },
    {
        "id": 61,
        "kategori": "pedagoji",
        "kelime": "geri getirme pratiği",
        "aciklama": "bilgiyi pasifçe yeniden okumak yerine belleği zorlayarak aktif biçimde hatırlamaya çalışma alıştırması.",
        "yasakli_kelimeler": ["retrieval practice", "test etkisi", "hatırlama", "hafıza", "aktif çağrışım"]
    },
    {
        "id": 62,
        "kategori": "pedagoji",
        "kelime": "somut işlemler dönemi",
        "aciklama": "piaget'nin gelişim kuramında çocuğun mantıksal düşünebildiği ancak henüz soyut kavramları kavrayamadığı evre.",
        "yasakli_kelimeler": ["piaget", "korunum", "mantık", "dönem", "7-11 yaş"]
    },
    {
        "id": 63,
        "kategori": "pedagoji",
        "kelime": "soyut işlemler dönemi",
        "aciklama": "ergenlikle birlikte bireyin hipotetik, tümdengelimsel ve soyut kavramlar üzerinde düşünebildiği son bilişsel aşama.",
        "yasakli_kelimeler": ["piaget", "ergenlik", "varsayım", "hipotez", "soyut mantık"]
    },
    {
        "id": 64,
        "kategori": "pedagoji",
        "kelime": "benmerkezcilik",
        "aciklama": "işlem öncesi dönemdeki çocuğun başkalarının dünyayı kendisinden farklı algılayabileceğini kavrayamaması durumu.",
        "yasakli_kelimeler": ["egosantrizm", "piaget", "kendi bakışı", "işlem öncesi", "perspektif"]
    },
    {
        "id": 65,
        "kategori": "pedagoji",
        "kelime": "nesne sürekliliği",
        "aciklama": "bebeğin gözünün önünden kaybolan nesnelerin evrende var olmaya devam ettiğini fark etme yeteneği.",
        "yasakli_kelimeler": ["duyusal motor", "piaget", "bebek", "kaybolma", "varlık"]
    },
    {
        "id": 66,
        "kategori": "pedagoji",
        "kelime": "korunum ilkesi",
        "aciklama": "bir maddenin şekli veya kabı değiştiğinde hacim, ağırlık ve miktarının değişmediğini anlama becerisi.",
        "yasakli_kelimeler": ["piaget", "miktar", "hacim", "somut işlemler", "değişmezlik"]
    },
    {
        "id": 67,
        "kategori": "pedagoji",
        "kelime": "özümleme",
        "aciklama": "bireyin karşılaştığı yeni bir deneyimi veya bilgiyi zihnindeki mevcut bilişsel şemalarına yerleştirmesi.",
        "yasakli_kelimeler": ["asimilasyon", "piaget", "şema", "uyum", "zihin"]
    },
    {
        "id": 68,
        "kategori": "pedagoji",
        "kelime": "uyumsama",
        "aciklama": "yeni bilginin mevcut şemalara uymaması halinde zihindeki şemanın değiştirilip yeniden düzenlenmesi süreci.",
        "yasakli_kelimeler": ["akomodasyon", "piaget", "şema değişimi", "dengesizlik", "uyarlama"]
    },
    {
        "id": 69,
        "kategori": "pedagoji",
        "kelime": "dengeleme süreci",
        "aciklama": "bilişsel dengesizlik yaşayan zihnin özümleme ve uyumsama yoluyla tekrar dengeye ulaşması mekanizması.",
        "yasakli_kelimeler": ["piaget", "denge", "dengesizlik", "bilişsel gelişim", "zihinsel"]
    },
    {
        "id": 70,
        "kategori": "pedagoji",
        "kelime": "ahlaki gelişim evreleri",
        "aciklama": "bireyin adalet ve doğru-yanlış muhakemesinin ceza korkusundan evrensel etik ilkelere doğru evrildiği kuram.",
        "yasakli_kelimeler": ["kohlberg", "gelenek öncesi", "geleneksel", "etik", "dilemma"]
    },
    {
        "id": 71,
        "kategori": "pedagoji",
        "kelime": "psikososyal gelişim",
        "aciklama": "insanın ömrü boyunca temel güven, özerklik ve kimlik gibi sekiz kriz aşamasından geçtiğini öne süren model.",
        "yasakli_kelimeler": ["erikson", "kriz", "sekiz evre", "kimlik", "güven"]
    },
    {
        "id": 72,
        "kategori": "pedagoji",
        "kelime": "öğrenme stilleri miti",
        "aciklama": "öğrencilerin yalnızca görsel, işitsel veya dokunsal öğretildiğinde daha iyi öğreneceği yönündeki kanıtsız inanç.",
        "yasakli_kelimeler": ["vark", "görsel-işitsel", "nöromit", "tarz", "efsane"]
    },
    {
        "id": 73,
        "kategori": "pedagoji",
        "kelime": "nöromit",
        "aciklama": "beynin sadece yüzde onunun kullanıldığı veya sol beynin mantık sağ beynin yaratıcılık olduğu gibi sahte bilimsel iddialar.",
        "yasakli_kelimeler": ["beyin efsanesi", "sahte bilim", "yanlış inanç", "sinirbilim", "yüzde on"]
    },
    {
        "id": 74,
        "kategori": "pedagoji",
        "kelime": "öğretmen tükenmişliği",
        "aciklama": "eğitimcilerin uzun süreli mesleki stres, bürokrasi ve duygusal yıpranma sonucu meslekten yabancılaşması durumu.",
        "yasakli_kelimeler": ["burnout", "maslach", "stres", "duygusal tükenme", "meslek"]
    },
    {
        "id": 75,
        "kategori": "pedagoji",
        "kelime": "akran zorbalığı",
        "aciklama": "okullarda bir veya birkaç öğrencinin güçsüz bir öğrenciye sürekli ve kasıtlı fiziksel ya da psikolojik baskı yapması.",
        "yasakli_kelimeler": ["şiddet", "zorba", "baskı", "okul", "mağdur"]
    },
    {
        "id": 76,
        "kategori": "pedagoji",
        "kelime": "sokratik sorgulama",
        "aciklama": "öğretmenin hazır bilgi vermek yerine yönelttiği derin sorularla öğrencinin kendi çelişkilerini görüp doğruya ulaşması.",
        "yasakli_kelimeler": ["sokrates", "doğurtma", "soru sorma", "ironi", "felsefe"]
    },
    {
        "id": 77,
        "kategori": "pedagoji",
        "kelime": "balık akvaryumu tekniği",
        "aciklama": "iç çemberdeki öğrencilerin tartıştığı, dış çemberdeki öğrencilerin ise onları gözlemleyip not aldığı yöntem.",
        "yasakli_kelimeler": ["fishbowl", "iç çember", "dış halka", "gözlem", "tartışma"]
    },
    {
        "id": 78,
        "kategori": "pedagoji",
        "kelime": "konuşma halkası",
        "aciklama": "öğrencilerin daire halinde oturup bir nesneyi elden ele geçirerek duygularını ve düşüncelerini paylaştığı etkinlik.",
        "yasakli_kelimeler": ["daire", "empati", "sırayla konuşma", "duygu paylaşımı", "halka"]
    },
    {
        "id": 79,
        "kategori": "pedagoji",
        "kelime": "rulman tekniği",
        "aciklama": "yüz yüze bakan iç içe iki halkanın dönerek her seferinde yeni bir eşle konuyu tartışmasını sağlayan teknik.",
        "yasakli_kelimeler": ["top taşıma", "iç içe halka", "eşleşme", "dönüş", "tartışma"]
    },
    {
        "id": 80,
        "kategori": "pedagoji",
        "kelime": "köşelenme tekniği",
        "aciklama": "öğrencilerin sınıfta farklı fikirleri temsil eden köşelere giderek kendi görüşlerini grupça savunduğu yöntem.",
        "yasakli_kelimeler": ["köşe", "tutum", "görüş savunma", "oda", "seçim"]
    },
    {
        "id": 81,
        "kategori": "pedagoji",
        "kelime": "ayrışık grup çalışması",
        "aciklama": "farklı yetenek ve başarı seviyelerindeki öğrencilerin birbirine destek olması için aynı masaya yerleştirilmesi.",
        "yasakli_kelimeler": ["heterojen", "farklı düzey", "işbirlikli grup", "karma", "seviye"]
    },
    {
        "id": 82,
        "kategori": "pedagoji",
        "kelime": "bağdaşık grup çalışması",
        "aciklama": "benzer öğrenme hızına veya özel ilgi alanlarına sahip aynı seviyedeki öğrencilerin bir araya getirilmesi.",
        "yasakli_kelimeler": ["homojen", "aynı düzey", "seviye grubu", "denk", "küme"]
    },
    {
        "id": 83,
        "kategori": "pedagoji",
        "kelime": "gamifikasyon",
        "aciklama": "öğrenme sürecine puan, rozet, seviye ve liderlik tablosu gibi oyun mekaniklerinin entegre edilmesi.",
        "yasakli_kelimeler": ["oyunlaştırma", "rozet", "puan", "liderlik", "motivasyon"]
    },
    {
        "id": 84,
        "kategori": "pedagoji",
        "kelime": "öğrenme analitiği",
        "aciklama": "öğrencilerin dijital platformlardaki tıklama, süre ve başarı verilerinin toplanıp öğretimi geliştirmede kullanılması.",
        "yasakli_kelimeler": ["büyük veri", "dijital iz", "analiz", "platform", "istatistik"]
    },
    {
        "id": 85,
        "kategori": "pedagoji",
        "kelime": "evrensel tasarım ilkesi",
        "aciklama": "öğretim müfredatının ve ortamının baştan itibaren tüm öğrenci çeşitliliğine erişilebilir tasarlanması felsefesi.",
        "yasakli_kelimeler": ["udl", "erişilebilirlik", "çeşitlilik", "herkes için", "tasarım"]
    },
    {
        "id": 86,
        "kategori": "pedagoji",
        "kelime": "andragoji",
        "aciklama": "yetişkinlerin öğrenme özelliklerini, özerkliklerini ve tecrübe odaklı motivasyonlarını inceleyen disiplin.",
        "yasakli_kelimeler": ["malcolm knowles", "yetişkin eğitimi", "özerk öğrenme", "pedagoji karşıtı", "tecrübe"]
    },
    {
        "id": 87,
        "kategori": "pedagoji",
        "kelime": "hütogoji",
        "aciklama": "öğrenenin kendi öğrenme sürecini, hedeflerini ve neyi nasıl öğreneceğini tamamen kendisinin belirlediği model.",
        "yasakli_kelimeler": ["kendi kendini belirleme", "özerklik", "heutagogy", "bağımsız öğrenme", "kapasite"]
    },
    {
        "id": 88,
        "kategori": "pedagoji",
        "kelime": "öğretmen özerkliği",
        "aciklama": "eğitimcinin müfredat, yöntem ve değerlendirme süreçlerinde bağımsız profesyonel kararlar alabilme özgürlüğü.",
        "yasakli_kelimeler": ["mesleki özgürlük", "karar alma", "bağımsızlık", "yetki", "öğretmen"]
    },
    {
        "id": 89,
        "kategori": "pedagoji",
        "kelime": "öğrenme topluluğu",
        "aciklama": "öğretmenlerin veya öğrencilerin mesleki ve akademik gelişim için düzenli toplanıp deneyim paylaştığı grup.",
        "yasakli_kelimeler": ["plc", "mesleki gelişim", "paylaşım", "işbirliği", "dayanışma"]
    },
    {
        "id": 90,
        "kategori": "pedagoji",
        "kelime": "öğrenme kaybı",
        "aciklama": "uzun yaz tatilleri veya salgın döneminde okulların kapanması nedeniyle bilgi ve becerilerde yaşanan gerileme.",
        "yasakli_kelimeler": ["gerileme", "yaz tatili", "pandemi", "unutma", "başarı düşüşü"]
    },
    {
        "id": 91,
        "kategori": "pedagoji",
        "kelime": "öğretimsel liderlik",
        "aciklama": "okul yöneticisinin sadece bürokrasiye değil öğretmenlerin sınıf içi kalitesine ve öğrenci başarısına odaklanması.",
        "yasakli_kelimeler": ["okul müdürü", "yönetici", "liderlik", "ders kalitesi", "vizyon"]
    },
    {
        "id": 92,
        "kategori": "pedagoji",
        "kelime": "öz değerlendirme",
        "aciklama": "öğrencinin kendi çalışma sürecini, ortaya koyduğu ürünü ve hedeflerine ulaşma derecesini bizzat puanlaması.",
        "yasakli_kelimeler": ["kendi kendini ölçme", "yansıtma", "öğrenci değerlendirmesi", "öz eleştiri", "kriter"]
    },
    {
        "id": 93,
        "kategori": "pedagoji",
        "kelime": "akran değerlendirmesi",
        "aciklama": "öğrencilerin belirlenmiş ölçütler doğrultusunda sınıf arkadaşlarının ödevlerini veya sunumlarını inceleyip notlaması.",
        "yasakli_kelimeler": ["arkadaş puanlama", "geri bildirim", "akran dönütü", "rubrik", "değerlendirme"]
    },
    {
        "id": 94,
        "kategori": "pedagoji",
        "kelime": "dijital bölünme",
        "aciklama": "öğrenciler arasında bilgisayar, internet ve teknolojiye erişim olanaklarındaki derin eşitsizlik durumu.",
        "yasakli_kelimeler": ["sayısal uçurum", "internet erişimi", "fırsat eşitsizliği", "teknoloji", "bilgisayar"]
    },
    {
        "id": 95,
        "kategori": "pedagoji",
        "kelime": "stem eğitimi",
        "aciklama": "bilim, teknoloji, mühendislik ve matematik disiplinlerini disiplinlerarası tek bir proje havuzunda birleştiren yaklaşım.",
        "yasakli_kelimeler": ["fen", "matematik", "mühendislik", "teknoloji", "kodlama"]
    },
    {
        "id": 96,
        "kategori": "pedagoji",
        "kelime": "açık uçlu soru",
        "aciklama": "tek bir doğru yanıtı olmayan, öğrencinin üst düzey düşünme, yorumlama ve sentez yapmasını gerektiren soru tipi.",
        "yasakli_kelimeler": ["klasik soru", "yorum", "düşünme", "test dışı", "çoktan seçmeli olmayan"]
    },
    {
        "id": 97,
        "kategori": "pedagoji",
        "kelime": "güvenli öğrenme ortamı",
        "aciklama": "öğrencinin hata yapmaktan, alay edilmekten veya yargılanmaktan korkmadan fikirlerini özgürce söylediği sınıf iklimi.",
        "yasakli_kelimeler": ["psikolojik güvenlik", "hata yapma hakkı", "korkusuz", "sınıf iklimi", "saygı"]
    },
    {
        "id": 98,
        "kategori": "pedagoji",
        "kelime": "kavram öğretimi",
        "aciklama": "soyut kavramların örnek olan ve örnek olmayan durumlar karşılaştırılarak zihinde netleştirilmesi süreci.",
        "yasakli_kelimeler": ["örnek olay", "kavram analizi", "tanım", "kategori", "zihinsel şema"]
    },
    {
        "id": 99,
        "kategori": "pedagoji",
        "kelime": "öğretim tasarımı",
        "aciklama": "öğrenme hedeflerine ulaşmak için ders içeriklerinin addie gibi modellerle sistematik planlanıp geliştirilmesi.",
        "yasakli_kelimeler": ["addie", "tasarım modeli", "sistemik planlama", "içerik geliştirme", "hedef"]
    },
    {
        "id": 100,
        "kategori": "pedagoji",
        "kelime": "sürekli mesleki gelişim",
        "aciklama": "öğretmenin kariyeri boyunca yeni öğretim yöntemleri, araştırmalar ve seminerlerle kendisini sürekli yenilemesi.",
        "yasakli_kelimeler": ["hizmet içi eğitim", "seminer", "öğretmen gelişimi", "çalıştay", "yaşam boyu öğrenme"]
    }
]

with open('/home/taceddinsancak/Desktop/Projects/taboo/data/pedagoji.json', 'w', encoding='utf-8') as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)
print("pedagoji.json yazıldı, kart sayısı:", len(cards))
