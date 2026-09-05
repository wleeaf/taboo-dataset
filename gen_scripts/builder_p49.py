import sys
from card_utils import add_and_save_verbs

# 1. TENIS (50 verbs: 12 kolay, 24 orta, 14 zor)
tenis_verbs = [
    # Kolay (12)
    {
        "kelime": "Servis Atmak",
        "aciklama": "Tenis oyununu veya puanını başlatmak için topa raketle vurmak.",
        "yasakli_kelimeler": ["oyun", "başlatmak", "top", "raket", "hata"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Smaç Basmak",
        "aciklama": "Havadan gelen topu sert bir baş üstü vuruşuyla rakip sahaya vurmak.",
        "yasakli_kelimeler": ["sert", "baş üstü", "vuruş", "raket", "puan"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Raket Tutmak",
        "aciklama": "Topa vurmak amacıyla tenis raketinin sapını kavramak.",
        "yasakli_kelimeler": ["sap", "kavramak", "el", "grip", "vuruş"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Top Toplamak",
        "aciklama": "Kort dışına çıkan veya fileye takılan topları saha görevlilerinin toplaması.",
        "yasakli_kelimeler": ["çocuk", "kort", "görevli", "file", "top"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Isınmak",
        "aciklama": "Tenis maçına başlamadan önce vuruş yaparak vücudu hazırlamak.",
        "yasakli_kelimeler": ["maç", "önce", "hazırlık", "vuruş", "antrenman"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Antrenman Yapmak",
        "aciklama": "Tenis becerilerini ve kondisyonunu geliştirmek için çalışmak.",
        "yasakli_kelimeler": ["çalışmak", "kondisyon", "koç", "geliştirmek", "kort"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Çiftler Oynamak",
        "aciklama": "Kortta ikişer kişilik takımlar halinde maç yapmak.",
        "yasakli_kelimeler": ["takım", "iki", "partner", "eş", "kort"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Kupayı Kaldırmak",
        "aciklama": "Tenis turnuvasını şampiyon olarak tamamlayıp ödülü havaya kaldırmak.",
        "yasakli_kelimeler": ["şampiyon", "turnuva", "ödül", "final", "kazanmak"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Raket Kırmak",
        "aciklama": "Maç esnasında öfkelenip tenis raketini yere vurarak parçalamak.",
        "yasakli_kelimeler": ["öfke", "yer", "parçalamak", "ceza", "sinirlenmek"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Topa Vurmak",
        "aciklama": "Raket yüzeyiyle tenis topuna temas ederek karşıya göndermek.",
        "yasakli_kelimeler": ["raket", "karşı", "temas", "oyun", "vuruş"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Saha Değişmek",
        "aciklama": "Belirli tek sayılı oyunlardan sonra kortun diğer tarafına geçmek.",
        "yasakli_kelimeler": ["kort", "taraf", "oyun", "mola", "geçmek"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Hakeme İtiraz Etmek",
        "aciklama": "Kule veya çizgi hakeminin verdiği kararı kabul etmeyip tartışmak.",
        "yasakli_kelimeler": ["kule", "çizgi", "karar", "out", "tartışmak"],
        "zorluk": "kolay"
    },

    # Orta (24)
    {
        "kelime": "Backhand Vurmak",
        "aciklama": "Raketin arkasıyla, elin tersiyle yapılan temel tenis vuruşu.",
        "yasakli_kelimeler": ["el", "ters", "forehand", "tek el", "çift el"],
        "zorluk": "orta"
    },
    {
        "kelime": "Forehand Çıkarmak",
        "aciklama": "Raketin avuç içi yönüyle yapılan güçlü ve baskın vuruş.",
        "yasakli_kelimeler": ["avuç içi", "sağ", "vuruş", "temel", "backhand"],
        "zorluk": "orta"
    },
    {
        "kelime": "Voleye Çıkmak",
        "aciklama": "File önüne yaklaşarak top yere sekmeden vuruş yapmak.",
        "yasakli_kelimeler": ["file", "sekmeden", "havada", "ön", "atak"],
        "zorluk": "orta"
    },
    {
        "kelime": "Drop Shot Bırakmak",
        "aciklama": "Topu fileyi hemen geçecek şekilde yavaşça ve yumuşakça rakip sahaya bırakmak.",
        "yasakli_kelimeler": ["kısa", "file", "yumuşak", "yavaş", "koşmak"],
        "zorluk": "orta"
    },
    {
        "kelime": "Lob Atmak",
        "aciklama": "Fileye gelen rakibin üzerinden topu yüksek kavisle aşırtmak.",
        "yasakli_kelimeler": ["aşırtma", "yüksek", "file", "üstünden", "kavis"],
        "zorluk": "orta"
    },
    {
        "kelime": "Ace Atmak",
        "aciklama": "Rakibin hiç dokunamayacağı şekilde kusursuz ve doğrudan puan getiren servis atmak.",
        "yasakli_kelimeler": ["servis", "dokunmak", "puan", "direkt", "hızlı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Çift Hata Yapmak",
        "aciklama": "Üst üste iki servis denemesinde de topu servis kutusuna atamayarak puan kaybetmek.",
        "yasakli_kelimeler": ["servis", "iki", "out", "kutu", "kaybetmek"],
        "zorluk": "orta"
    },
    {
        "kelime": "Servis Kırmak",
        "aciklama": "Rakip oyuncunun servis kullandığı oyunu kazanarak avantaj elde etmek.",
        "yasakli_kelimeler": ["oyun", "kazanmak", "avantaj", "rakip", "break"],
        "zorluk": "orta"
    },
    {
        "kelime": "Tie-break Oynamak",
        "aciklama": "Set 6-6 berabere bittiğinde seti kazananı belirlemek için oynanan özel uzatma oyunu.",
        "yasakli_kelimeler": ["beraberlik", "set", "yedi", "uzatma", "puan"],
        "zorluk": "orta"
    },
    {
        "kelime": "Meydan Okumak",
        "aciklama": "Hakemin çizgi kararına şüphe duyup şahin gözü kamera sistemini talep etmek.",
        "yasakli_kelimeler": ["şahin gözü", "challenge", "kamera", "çizgi", "itiraz"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kortta Kaymak",
        "aciklama": "Özellikle toprak kortta topa yetişmek için zeminde kayma hareketi yapmak.",
        "yasakli_kelimeler": ["toprak", "zemin", "kayış", "yetişmek", "ayak"],
        "zorluk": "orta"
    },
    {
        "kelime": "Ralliye Girmek",
        "aciklama": "Karşılıklı olarak topu uzun süre oyunda tutup peş peşe vuruşlar yapmak.",
        "yasakli_kelimeler": ["uzun", "vuruş", "karşılıklı", "oyun", "puan"],
        "zorluk": "orta"
    },
    {
        "kelime": "Topu Döndürmek",
        "aciklama": "Raketle topa falso ve dönüş hareketi vererek rakibin kontrolünü zorlaştırmak.",
        "yasakli_kelimeler": ["falso", "spin", "dönüş", "kontrol", "raket"],
        "zorluk": "orta"
    },
    {
        "kelime": "Fileye Takılmak",
        "aciklama": "Vurulan topun fileyi aşamayarak kendi sahasında kalması.",
        "yasakli_kelimeler": ["file", "aşmak", "hata", "çarpma", "kalmak"],
        "zorluk": "orta"
    },
    {
        "kelime": "Grip Değiştirmek",
        "aciklama": "Farklı vuruş tipleri için raket sapındaki el tutuş açısını değiştirmek.",
        "yasakli_kelimeler": ["tutuş", "sap", "açı", "eastern", "western"],
        "zorluk": "orta"
    },
    {
        "kelime": "Set Çalmak",
        "aciklama": "Favori veya güçlü rakibe karşı gerideyken beklenmedik bir set kazanmak.",
        "yasakli_kelimeler": ["set", "kazanmak", "sürpriz", "maç", "rakip"],
        "zorluk": "orta"
    },
    {
        "kelime": "Taktiksel Mola Almak",
        "aciklama": "Rakibin ivmesini kırmak veya toparlanmak için sağlık veya tuvalet molası kullanmak.",
        "yasakli_kelimeler": ["mola", "sağlık", "ivme", "durdurmak", "zaman"],
        "zorluk": "orta"
    },
    {
        "kelime": "Ayak Hareketini Hızlandırmak",
        "aciklama": "Kortta topa doğru pozisyonda ve dengede vurabilmek için seri adımlar atmak.",
        "yasakli_kelimeler": ["adım", "footwork", "denge", "pozisyon", "hızlı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Açı Yaratmak",
        "aciklama": "Topu kortun köşelerine veya dışına doğru çapraz vurarak rakibi sahaya koşturmak.",
        "yasakli_kelimeler": ["çapraz", "köşe", "dar", "koşturmak", "vuruş"],
        "zorluk": "orta"
    },
    {
        "kelime": "Servis Karşılamak",
        "aciklama": "Rakibin attığı sert servisi sahaya kontrollü bir şekilde geri döndürmek.",
        "yasakli_kelimeler": ["return", "servis", "kontrol", "içeri", "karşılama"],
        "zorluk": "orta"
    },
    {
        "kelime": "Gözünü Topta Tutmak",
        "aciklama": "Vuruş anına kadar topun hareketini ve temas noktasını dikkatle izlemek.",
        "yasakli_kelimeler": ["izlemek", "temas", "odak", "dikkat", "bakmak"],
        "zorluk": "orta"
    },
    {
        "kelime": "Raketi Telletmek",
        "aciklama": "Kopmuş veya esnekliğini yitirmiş raket kordajını makinede yeniden gerdirmek.",
        "yasakli_kelimeler": ["kordaj", "tel", "gerginlik", "makine", "tansiyon"],
        "zorluk": "orta"
    },
    {
        "kelime": "Grip Bandı Sarmak",
        "aciklama": "Elin kaymasını engellemek için raket sapına yeni overgrip sarmak.",
        "yasakli_kelimeler": ["overgrip", "sap", "kayma", "ter", "sarmak"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kortu Temizlemek",
        "aciklama": "Toprak veya çim kortun zeminini maç aralarında süpürüp düzeltmek.",
        "yasakli_kelimeler": ["süpürmek", "zemin", "toprak", "düzeltmek", "çizgi"],
        "zorluk": "orta"
    },

    # Zor (14)
    {
        "kelime": "Topspin Vermek",
        "aciklama": "Topa aşağıdan yukarıya fırçalama vuruşu yaparak ileri doğru hızlı dönmesini sağlamak.",
        "yasakli_kelimeler": ["fırçalama", "dönüş", "falso", "kavis", "aşağıdan"],
        "zorluk": "zor"
    },
    {
        "kelime": "Slice Kesmek",
        "aciklama": "Topa yukarıdan aşağıya vurarak geri falso vermek ve yerde alçak sekmesini sağlamak.",
        "yasakli_kelimeler": ["alçak", "kesme", "ters", "falso", "yukarıdan"],
        "zorluk": "zor"
    },
    {
        "kelime": "Passing Shot Çıkarmak",
        "aciklama": "Fileye yaklaşmış rakibin sağından veya solundan yetişemeyeceği bir vuruşla puan almak.",
        "yasakli_kelimeler": ["file", "yanından", "geçmek", "rakip", "aşırtma"],
        "zorluk": "zor"
    },
    {
        "kelime": "Kick Servis Kullanmak",
        "aciklama": "Topa yüksek falso verilerek rakibin ters omzuna doğru yüksek sekmesini sağlayan servis atmak.",
        "yasakli_kelimeler": ["falso", "yüksek", "sekmek", "omuz", "servis"],
        "zorluk": "zor"
    },
    {
        "kelime": "Kort Geometrisini Kullanmak",
        "aciklama": "Açıları ve saha derinliğini hesaplayarak rakibi en uzak noktalara hareket ettirmek.",
        "yasakli_kelimeler": ["açı", "derinlik", "hesap", "taktik", "boşluk"],
        "zorluk": "zor"
    },
    {
        "kelime": "İçten Dışa Vurmak",
        "aciklama": "Topun geliş açısının tersine, içeriden dışarıya doğru yönlendirilen vuruş (inside-out).",
        "yasakli_kelimeler": ["inside out", "çapraz", "yön", "ters", "forehand"],
        "zorluk": "zor"
    },
    {
        "kelime": "Yarım Vole Çıkarmak",
        "aciklama": "Top yere değer değmez henüz yükselmeden çok alçakta yapılan refleks vuruşu.",
        "yasakli_kelimeler": ["half volley", "alçak", "refleks", "sekme", "zemin"],
        "zorluk": "zor"
    },
    {
        "kelime": "Smaç Kurtarmak",
        "aciklama": "Rakibin sert smaç vuruşuna savunmada inanılmaz bir refleksle yetişip topu içeri atmak.",
        "yasakli_kelimeler": ["smaç", "savunma", "refleks", "yetişmek", "kurtarış"],
        "zorluk": "zor"
    },
    {
        "kelime": "Tansiyon Ayarlamak",
        "aciklama": "Oyun stiline veya hava koşullarına göre raket kordajının gerginlik kilosunu belirlemek.",
        "yasakli_kelimeler": ["gerginlik", "kilo", "kordaj", "kontrol", "güç"],
        "zorluk": "zor"
    },
    {
        "kelime": "Ağırlık Transferi Yapmak",
        "aciklama": "Vuruş esnasında vücut ağırlığını arka ayaktan ön ayağa aktararak vuruş gücünü artırmak.",
        "yasakli_kelimeler": ["vücut", "ayak", "aktarmak", "güç", "denge"],
        "zorluk": "zor"
    },
    {
        "kelime": "Raket Başı Hızı Üretmek",
        "aciklama": "Vuruş mekaniğinde bilek ve kol ivmesiyle raket kafasını maksimum hızda savurmak.",
        "yasakli_kelimeler": ["ivme", "savurmak", "kafa", "hız", "bilek"],
        "zorluk": "zor"
    },
    {
        "kelime": "Bacak İtişi Sağlamak",
        "aciklama": "Servis atarken dizleri büküp yerden kuvvet alarak yukarıya doğru sıçramak.",
        "yasakli_kelimeler": ["diz", "zıplamak", "kuvvet", "sıçrama", "servis"],
        "zorluk": "zor"
    },
    {
        "kelime": "Kinetik Zincir Kurmak",
        "aciklama": "Vuruş kuvvetini bacaklardan kalçaya, gövdeden kola ve rakete kusursuz aktarmak.",
        "yasakli_kelimeler": ["kuvvet", "bacak", "gövde", "kol", "aktarım"],
        "zorluk": "zor"
    },
    {
        "kelime": "Zemine Göre Uyarlanmak",
        "aciklama": "Toprak, çim veya sert kortun top sekme hızına ve kayma dinamiklerine göre oyununu değiştirmek.",
        "yasakli_kelimeler": ["toprak", "çim", "sert kort", "sekme", "dinamik"],
        "zorluk": "zor"
    }
]

# 2. TEOLOJI (50 verbs: 12 kolay, 24 orta, 14 zor)
teoloji_verbs = [
    # Kolay (12)
    {
        "kelime": "Dua Etmek",
        "aciklama": "Yaratıcıya veya kutsal kabul edilen varlığa yalvarmak ve dilekte bulunmak.",
        "yasakli_kelimeler": ["tanrı", "yalvarmak", "dilek", "ibadet", "eller"],
        "zorluk": "kolay"
    },
    {
        "kelime": "İbadet Etmek",
        "aciklama": "Dini buyruk ve ritüelleri yerine getirerek kulluk görevini ifa etmek.",
        "yasakli_kelimeler": ["din", "kulluk", "görev", "namaz", "ayin"],
        "zorluk": "kolay"
    },
    {
        "kelime": "İnanmak",
        "aciklama": "Bir dinin, tanrının veya dogmanın varlığını şüphesiz kabul etmek.",
        "yasakli_kelimeler": ["şüphe", "kabul", "iman", "tanrı", "güven"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Kutsamak",
        "aciklama": "Bir kişiyi, nesneyi veya mekânı dini törenle kutsal kılmak.",
        "yasakli_kelimeler": ["kutsal", "tören", "din", "rahip", "dua"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Tövbe Etmek",
        "aciklama": "İşlenen bir günahtan pişman olup tanrıdan af dilemek.",
        "yasakli_kelimeler": ["günah", "pişmanlık", "af", "bağışlanma", "dilemek"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Oruç Tutmak",
        "aciklama": "Dini bir buyruk gereği belirli saatlerde yeme ve içmeden uzak durmak.",
        "yasakli_kelimeler": ["yemek", "içmek", "ramazan", "aç", "ibadet"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Şükretmek",
        "aciklama": "Sahip olunan nimetler ve iyilikler için tanrıya minnet sunmak.",
        "yasakli_kelimeler": ["nimet", "minnet", "teşekkür", "tanrı", "iyilik"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Kurban Kesmek",
        "aciklama": "Dini bir adak veya bayram ritüeli olarak hayvan boğazlamak.",
        "yasakli_kelimeler": ["bayram", "hayvan", "adak", "kesim", "ibadet"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Günah İşlemek",
        "aciklama": "Dinin yasakladığı veya ahlaka aykırı kabul ettiği bir eylemi yapmak.",
        "yasakli_kelimeler": ["yasak", "kötü", "ceza", "sevap", "din"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Hacca Gitmek",
        "aciklama": "Dini bir görevi yerine getirmek amacıyla kutsal mekânları ziyaret etmek.",
        "yasakli_kelimeler": ["mekke", "kutsal", "ziyaret", "ibadet", "kabe"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Vaaz Vermek",
        "aciklama": "Dini konularda topluluğa öğüt ve nasihat içerikli konuşma yapmak.",
        "yasakli_kelimeler": ["konuşma", "öğüt", "hoca", "cami", "nasihat"],
        "zorluk": "kolay"
    },
    {
        "kelime": "Kutsal Kitap Okumak",
        "aciklama": "Vahyedilmiş kutsal metinleri ibadet veya öğrenme amacıyla tilavet etmek.",
        "yasakli_kelimeler": ["kur'an", "incil", "tevrat", "metin", "okuma"],
        "zorluk": "kolay"
    },

    # Orta (24)
    {
        "kelime": "Vahiy Almak",
        "aciklama": "Tanrı tarafından peygamberlere ilahi buyruk ve mesajların bildirilmesi.",
        "yasakli_kelimeler": ["peygamber", "ilahi", "mesaj", "cebrail", "tanrı"],
        "zorluk": "orta"
    },
    {
        "kelime": "Aforoz Etmek",
        "aciklama": "Bir kişiyi dini cemaatten veya kiliseden resmi olarak ihraç etmek.",
        "yasakli_kelimeler": ["kilise", "cemaat", "ihraç", "çıkarma", "papa"],
        "zorluk": "orta"
    },
    {
        "kelime": "Tefsir Etmek",
        "aciklama": "Kutsal metinlerin ve ayetlerin anlamlarını açıklayıp derinlemesine yorumlamak.",
        "yasakli_kelimeler": ["ayet", "yorum", "açıklama", "metin", "kur'an"],
        "zorluk": "orta"
    },
    {
        "kelime": "Vaftiz Etmek",
        "aciklama": "Hristiyanlıkta suya batırma veya su serpme yoluyla ilk günahı temizleyip dine kabul etmek.",
        "yasakli_kelimeler": ["su", "hristiyanlık", "kilise", "bebek", "rahip"],
        "zorluk": "orta"
    },
    {
        "kelime": "Dogmaları Sorgulamak",
        "aciklama": "Dinin tartışılamaz ve sorgulanamaz kabul ettiği temel inanç esaslarını eleştirmek.",
        "yasakli_kelimeler": ["eleştiri", "şüphe", "inanç", "tartışma", "esas"],
        "zorluk": "orta"
    },
    {
        "kelime": "Nefsi Terbiye Etmek",
        "aciklama": "Dünyevi arzu, heves ve tutkuları tasavvufi yöntemlerle dizginlemek.",
        "yasakli_kelimeler": ["arzu", "tutku", "tasavvuf", "dizginlemek", "irade"],
        "zorluk": "orta"
    },
    {
        "kelime": "İtikada Bağlanmak",
        "aciklama": "Bir mezhebin veya inanç sisteminin akidelerini benimseyip sadık kalmak.",
        "yasakli_kelimeler": ["inanç", "akide", "mezhep", "bağlılık", "öğreti"],
        "zorluk": "orta"
    },
    {
        "kelime": "Münazara Yapmak",
        "aciklama": "Farklı ilahiyat veya kelam ekollerinin tezlerini savunmak için tartışması.",
        "yasakli_kelimeler": ["tartışma", "kelam", "tez", "savunma", "ekol"],
        "zorluk": "orta"
    },
    {
        "kelime": "Fetva Vermek",
        "aciklama": "Dini bir mesele veya hüküm hakkında yetkili din bilgininin görüş açıklaması.",
        "yasakli_kelimeler": ["müftü", "hüküm", "görüş", "diyanet", "caiz"],
        "zorluk": "orta"
    },
    {
        "kelime": "İçtihat Yapmak",
        "aciklama": "Açık hüküm bulunmayan konularda fıkıh aliminin akıl ve usul ile yeni hüküm çıkarması.",
        "yasakli_kelimeler": ["fıkıh", "alim", "hüküm", "usul", "akıl"],
        "zorluk": "orta"
    },
    {
        "kelime": "Zühd Yaşamak",
        "aciklama": "Dünyevi zevklerden, maldan ve mülkten el çekip tamamen ibadete odaklanmak.",
        "yasakli_kelimeler": ["dünya", "mal", "mülk", "tasavvuf", "çile"],
        "zorluk": "orta"
    },
    {
        "kelime": "Mürid Yetiştirmek",
        "aciklama": "Tasavvufi bir tekkede şeyhin mürşit olarak talebelerine manevi rehberlik etmesi.",
        "yasakli_kelimeler": ["şeyh", "tekke", "tasavvuf", "tarikat", "talebe"],
        "zorluk": "orta"
    },
    {
        "kelime": "Ruhban Sınıfına Girmek",
        "aciklama": "Kilise veya tapınak hiyerarşisinde resmi din adamı rütbesi almak.",
        "yasakli_kelimeler": ["rahip", "kilise", "din adamı", "hiyerarşi", "keşiş"],
        "zorluk": "orta"
    },
    {
        "kelime": "Ruhunu Arındırmak",
        "aciklama": "Manevi pratikler ve riyazetle içsel kötülükleri ve günahları temizlemek.",
        "yasakli_kelimeler": ["manevi", "temizlik", "kötülük", "arınma", "içsel"],
        "zorluk": "orta"
    },
    {
        "kelime": "Kefaret Ödemek",
        "aciklama": "Bozulan bir dini yemini veya kuralı telafi etmek için sadaka vermek veya oruç tutmak.",
        "yasakli_kelimeler": ["yemin", "telafi", "sadaka", "ceza", "kural"],
        "zorluk": "orta"
    },
    {
        "kelime": "Hermeneutik Yapmak",
        "aciklama": "Kutsal metinlerin bağlamını, tarihsel arka planını ve manasını yorumlamak.",
        "yasakli_kelimeler": ["yorum", "metin", "bağlam", "tarihsel", "anlam"],
        "zorluk": "orta"
    },
    {
        "kelime": "Şirke Düşmek",
        "aciklama": "Tek olan yaratıcıya ortak koşmak veya başka güçlere tanrılık atfetmek.",
        "yasakli_kelimeler": ["ortak", "tevhid", "tanrı", "put", "inanç"],
        "zorluk": "orta"
    },
    {
        "kelime": "Mezhep Değiştirmek",
        "aciklama": "Bir dinin içerisindeki bir yorum veya inanç ekolünden diğerine geçmek.",
        "yasakli_kelimeler": ["ekol", "yorum", "din", "geçiş", "inanç"],
        "zorluk": "orta"
    },
    {
        "kelime": "Tevhidi Savunmak",
        "aciklama": "Tanrının birliğini, eşi ve benzeri olmadığını ilkesel olarak öne sürmek.",
        "yasakli_kelimeler": ["birlik", "tek", "allah", "monoteizm", "ilke"],
        "zorluk": "orta"
    },
    {
        "kelime": "Günah İtiraf Etmek",
        "aciklama": "Katoliklikte rahibin huzurunda işlediği günahları dile getirip af talep etmek.",
        "yasakli_kelimeler": ["rahip", "katolik", "hücre", "itiraf", "bağışlanma"],
        "zorluk": "orta"
    },
    {
        "kelime": "Adak Adamak",
        "aciklama": "Bir dileğin gerçekleşmesi halinde tanrıya bir ibadet veya kurban sunmaya söz vermek.",
        "yasakli_kelimeler": ["dilek", "söz", "kurban", "şart", "yerine getirmek"],
        "zorluk": "orta"
    },
    {
        "kelime": "Hakkı Tavsiye Etmek",
        "aciklama": "İnsanlara doğruluk, adalet ve dini hakikatleri anlatıp teşvik etmek.",
        "yasakli_kelimeler": ["doğruluk", "adalet", "öğüt", "tavsiye", "hakikat"],
        "zorluk": "orta"
    },
    {
        "kelime": "Dini Tebliğ Etmek",
        "aciklama": "İlahi mesajları insanlara duyurmak, yaymak ve onları dine davet etmek.",
        "yasakli_kelimeler": ["davet", "yaymak", "duyurmak", "mesaj", "çağrı"],
        "zorluk": "orta"
    },
    {
        "kelime": "İnzivaya Çekilmek",
        "aciklama": "Toplumdan ve insanlardan uzaklaşıp tek başına manevi tefekküre dalmak.",
        "yasakli_kelimeler": ["yalnızlık", "uzaklaşmak", "tefekkür", "mağara", "ibadet"],
        "zorluk": "orta"
    },

    # Zor (14)
    {
        "kelime": "Kelam Tartışması Yapmak",
        "aciklama": "İslam teolojisinde akıl ve felsefi argümanlarla inanç esaslarını savunmak.",
        "yasakli_kelimeler": ["felsefe", "akıl", "argüman", "inanç", "islam"],
        "zorluk": "zor"
    },
    {
        "kelime": "Teodise Problemini Çözmek",
        "aciklama": "Mutlak iyi bir tanrının varlığı ile dünyadaki kötülük problemini bağdaştırmaya çalışmak.",
        "yasakli_kelimeler": ["kötülük", "tanrı", "adalet", "problem", "açıklama"],
        "zorluk": "zor"
    },
    {
        "kelime": "Eskatolojik Yorumlamak",
        "aciklama": "Kıyamet, ahiret, ölüm sonrası hayat ve evrenin sonuna dair öğretileri tahlil etmek.",
        "yasakli_kelimeler": ["kıyamet", "ahiret", "son", "ölüm", "tahlil"],
        "zorluk": "zor"
    },
    {
        "kelime": "Teslis İnancını Savunmak",
        "aciklama": "Hristiyanlıktaki Baba, Oğul ve Kutsal Ruh üçlemesini teolojik temellere oturtmak.",
        "yasakli_kelimeler": ["baba", "oğul", "kutsal ruh", "üçleme", "hristiyanlık"],
        "zorluk": "zor"
    },
    {
        "kelime": "Ontolojik Kanıt Sunmak",
        "aciklama": "Tanrının varlığını doğrudan varlık kavramı ve mükemmel varlık tanımı üzerinden ispatlamak.",
        "yasakli_kelimeler": ["varlık", "ispat", "kavram", "mükemmel", "felsefe"],
        "zorluk": "zor"
    },
    {
        "kelime": "Kozmolojik Delil Getirmek",
        "aciklama": "Evrenin varlığından ve nedensellik zincirinden yola çıkarak bir ilk neden (Tanrı) öne sürmek.",
        "yasakli_kelimeler": ["evren", "nedensellik", "ilk neden", "delil", "yaratıcı"],
        "zorluk": "zor"
    },
    {
        "kelime": "Teleolojik İzah Yapmak",
        "aciklama": "Evrendeki düzen, intizam ve amaçlılıktan hareketle akıllı bir tasarımcıyı kanıtlamak.",
        "yasakli_kelimeler": ["düzen", "amaç", "tasarım", "intizam", "izah"],
        "zorluk": "zor"
    },
    {
        "kelime": "Apofatik Yaklaşmak",
        "aciklama": "Tanrıyı ne olduğunu değil ne olmadığını söyleyerek tanımlayan negatif teoloji yöntemi uygulamak.",
        "yasakli_kelimeler": ["negatif", "tanım", "olumsuzlama", "kavram", "öte"],
        "zorluk": "zor"
    },
    {
        "kelime": "Gaybı Tefekkür Etmek",
        "aciklama": "Duyularla algılanamayan, gizli ve metafizik ilahi alemler üzerine derin düşünmek.",
        "yasakli_kelimeler": ["gizli", "metafizik", "duyu", "alem", "düşünce"],
        "zorluk": "zor"
    },
    {
        "kelime": "Sünnetullahı İncelemek",
        "aciklama": "Tanrının evrende ve toplumlarda koyduğu değişmez ilahi kanunları ve yasaları araştırmak.",
        "yasakli_kelimeler": ["kanun", "yasa", "evren", "ilahi", "değişmez"],
        "zorluk": "zor"
    },
    {
        "kelime": "Fena Mertebesine Ulaşmak",
        "aciklama": "Tasavvufta benlikten tamamen sıyrılarak ilahi varlıkta yok oluş deneyimi yaşamak.",
        "yasakli_kelimeler": ["tasavvuf", "yok oluş", "benlik", "vahdet", "mertebe"],
        "zorluk": "zor"
    },
    {
        "kelime": "Külli İradeyi Anlamak",
        "aciklama": "Tanrının mutlak ve sınırsız iradesi ile insanın cüzi iradesi arasındaki ilişkiyi kavramak.",
        "yasakli_kelimeler": ["mutlak", "irade", "cüzi", "kader", "kudret"],
        "zorluk": "zor"
    },
    {
        "kelime": "Kanona Dahil Etmek",
        "aciklama": "Bir dini metni veya incili resmi kutsal metinler listesine ve külliyata kabul etmek.",
        "yasakli_kelimeler": ["metin", "külliyat", "incil", "liste", "kabul"],
        "zorluk": "zor"
    },
    {
        "kelime": "Transandantal Düşünmek",
        "aciklama": "Fiziksel ve ampirik dünyanın ötesindeki aşkın ve ilahi boyutları kavramaya çalışmak.",
        "yasakli_kelimeler": ["aşkın", "ampirik", "fizik ötesi", "boyut", "metafizik"],
        "zorluk": "zor"
    }
]

if __name__ == "__main__":
    add_and_save_verbs("tenis", tenis_verbs)
    add_and_save_verbs("teoloji", teoloji_verbs)
