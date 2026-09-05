import os, sys, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gen_scripts.card_utils import add_and_save_verbs

# 19. genetik
genetik_verbs = [
    # Kolay (12)
    {"kelime": "dna testi yaptırmak", "yasakli_kelimeler": ["tükürük", "laboratuvar", "genetik", "köken", "akrabalık"], "zorluk": "kolay", "aciklama": "Genetik yapıyı veya soyağacını öğrenmek için analiz yaptırmak."},
    {"kelime": "babadan miras kalmak", "yasakli_kelimeler": ["kalıtım", "gen", "özellik", "benzerlik", "aile"], "zorluk": "kolay", "aciklama": "Fiziksel veya biyolojik özelliklerin babadan çocuğa aktarılması."},
    {"kelime": "göz rengi aktarmak", "yasakli_kelimeler": ["mavi", "yeşil", "kahverengi", "kalıtsal", "çocuk"], "zorluk": "kolay", "aciklama": "Ebeveynin iris pigment özelliklerini sonraki nesle geçirmesi."},
    {"kelime": "mikroskopla incelemek", "yasakli_kelimeler": ["hücre", "büyütmek", "mercek", "çekirdek", "bakmak"], "zorluk": "kolay", "aciklama": "Gözle görülmeyen genetik ve hücresel yapıları cihazla büyütüp görmek."},
    {"kelime": "kan örneği vermek", "yasakli_kelimeler": ["tüp", "iğne", "tahlil", "hemşire", "kol"], "zorluk": "kolay", "aciklama": "Genetik analiz için damardan kan numunesi aldırmak."},
    {"kelime": "akrabalık bağı aramak", "yasakli_kelimeler": ["soy", "dna eşleşmesi", "kardeş", "kuzen", "ebeveyn"], "zorluk": "kolay", "aciklama": "İki kişinin genetik olarak aynı aileden gelip gelmediğini sorgulamak."},
    {"kelime": "boy uzunluğunu belirlemek", "yasakli_kelimeler": ["genetik faktör", "anne baba", "metre", "büyüme", "kalıtım"], "zorluk": "kolay", "aciklama": "Genlerin boy potansiyeli üzerindeki etkisini ortaya koymak."},
    {"kelime": "hücre bölünmesi yaşamak", "yasakli_kelimeler": ["çoğalma", "büyüme", "mitoz", "ikiye ayrılma", "doku"], "zorluk": "kolay", "aciklama": "Bir hücrenin genetik materyalini kopyalayarak iki yeni hücre oluşturması."},
    {"kelime": "hastalık geni taşımak", "yasakli_kelimeler": ["taşıyıcı", "kalıtsal", "aktarım", "risk", "sağlık"], "zorluk": "kolay", "aciklama": "Kendisi hasta olmasa da hastalığa yol açan geni bünyesinde bulundurmak."},
    {"kelime": "ikiz doğurmak", "yasakli_kelimeler": ["tek yumurta", "çift yumurta", "benzerlik", "aynı dna", "kardeş"], "zorluk": "kolay", "aciklama": "Aynı gebelikte iki bebek dünyaya getirmek."},
    {"kelime": "gen haritası çıkarmak", "yasakli_kelimeler": ["dizilim", "kromozom", "kod", "insan genomu", "proje"], "zorluk": "kolay", "aciklama": "Organizmanın tüm genlerinin yerlerini şematize etmek."},
    {"kelime": "özellik kopyalamak", "yasakli_kelimeler": ["klonlama", "aktarma", "benzer", "üretim", "aynı"], "zorluk": "kolay", "aciklama": "Bir canlının genetik niteliklerini birebir başka bir yapıya aktarmak."},

    # Orta (24)
    {"kelime": "mutasyona uğramak", "yasakli_kelimeler": ["değişim", "dna hasarı", "radyasyon", "bozulma", "varyant"], "zorluk": "orta", "aciklama": "Genetik dizilimin çevresel veya rastlantısal etkilerle değişikliğe uğraması."},
    {"kelime": "genom dizilemek", "yasakli_kelimeler": ["sekanslama", "a t g c", "baz dizisi", "yeni nesil", "okuma"], "zorluk": "orta", "aciklama": "Organizmanın tüm DNA baz sırasını harf harf okumak."},
    {"kelime": "pCR testi yapmak", "yasakli_kelimeler": ["polimeraz zincir reaksiyonu", "çoğaltma", "dna amplifikasyonu", "termal döngü", "tespit"], "zorluk": "orta", "aciklama": "Eldeki az miktardaki DNA parçasını milyonlarca kez kopyalayarak çoğaltmak."},
    {"kelime": "kromozom saymak", "yasakli_kelimeler": ["karyotip", "46", "trizomi", "down sendromu", "genetik anomali"], "zorluk": "orta", "aciklama": "Hücredeki kromozomların toplam adedini ve yapısını analiz etmek."},
    {"kelime": "rekombinasyon geçirmek", "yasakli_kelimeler": ["crossing over", "parça değişimi", "mayoz", "çeşitlilik", "krossing over"], "zorluk": "orta", "aciklama": "Mayoz bölünmede homolog kromozomlar arasında gen alışverişi olması."},
    {"kelime": "baskın geni ifade etmek", "yasakli_kelimeler": ["dominant", "fenotip", "çekinik", "ortaya çıkma", "alel"], "zorluk": "orta", "aciklama": "Dominant alelin fenotipte doğrudan etkisini göstermesi."},
    {"kelime": "çekinik kalmak", "yasakli_kelimeler": ["resesif", "gizli", "baskılanma", "homozigot", "etkisiz"], "zorluk": "orta", "aciklama": "Baskın gen varlığında özelliğin dış görünüşte ortaya çıkamaması."},
    {"kelime": "klonlama yapmak", "yasakli_kelimeler": ["dolly", "kopyalama", "birebir aynı", "çekirdek transferi", "embriyo"], "zorluk": "orta", "aciklama": "Bir canlının genetik ikizini yapay yollarla üretmek."},
    {"kelime": "genetik danışmanlık almak", "yasakli_kelimeler": ["risk analizi", "akraba evliliği", "bebek", "uzman doktor", "kalıtsal hastalık"], "zorluk": "orta", "aciklama": "Kalıtsal hastalık risklerini öğrenmek için uzman hekimle görüşmek."},
    {"kelime": "transkripsiyon yapmak", "yasakli_kelimeler": ["mrna", "yazılma", "dna şablonu", "rna polimeraz", "çekirdek"], "zorluk": "orta", "aciklama": "DNA'daki genetik bilginin haberci RNA molekülüne kopyalanması."},
    {"kelime": "translasyon gerçekleştirmek", "yasakli_kelimeler": ["ribozom", "protein sentezi", "okunma", "aminoasit", "trna"], "zorluk": "orta", "aciklama": "mRNA'daki kodonların ribozomda aminoasit dizisine çevrilmesi."},
    {"kelime": "plazmit aktarmak", "yasakli_kelimeler": ["bakteri", "vektör", "halka dna", "gen transferi", "direnç"], "zorluk": "orta", "aciklama": "Bakteriler arasında küçük halkasal DNA parçalarını transfer etmek."},
    {"kelime": "gen modifikasyonu yapmak", "yasakli_kelimeler": ["gdo", "genetik mühendisliği", "değiştirme", "ekleme", "çıkarma"], "zorluk": "orta", "aciklama": "Canlının genetik koduna yapay olarak müdahale edip değiştirmek."},
    {"kelime": "jel elektroforezi yürütmek", "yasakli_kelimeler": ["agaroz", "elektrik akımı", "bant", "dna boyutu", "ayrıştırma"], "zorluk": "orta", "aciklama": "DNA parçalarını elektrik akımı altında boyutlarına göre jelde ayrıştırmak."},
    {"kelime": "restriksiyon enzimiyle kesmek", "yasakli_kelimeler": ["moleküler makas", "tanıma bölgesi", "kesim", "dna", "parçalama"], "zorluk": "orta", "aciklama": "DNA zincirini belirli baz dizisi noktalarından özel enzimlerle kesmek."},
    {"kelime": "epigenetik değişiklik izlemek", "yasakli_kelimeler": ["metilasyon", "çevre etkisi", "dna dizisi değişmeden", "ifade", "histon"], "zorluk": "orta", "aciklama": "DNA dizisi değişmeden genlerin açılıp kapanma mekanizmalarını incelemek."},
    {"kelime": "soyağacı analizi yapmak", "yasakli_kelimeler": ["pedigri", "kare yuvarlak", "nesiller", "hastalık aktarımı", "kalıtım"], "zorluk": "orta", "aciklama": "Kalıtsal bir özelliğin aile nesilleri boyunca aktarım şemasını çıkarmak."},
    {"kelime": "adli dna eşleştirmesi yapmak", "yasakli_kelimeler": ["olay yeri", "parmak izi", "str profili", "şüpheli", "kanıt"], "zorluk": "orta", "aciklama": "Olay yerinde bulunan biyolojik izleri şüphelinin DNA'sıyla kıyaslamak."},
    {"kelime": "mitokondriyal dna incelemek", "yasakli_kelimeler": ["anne soyu", "matrilineal", "hücre enerji santrali", "evrim", "halka"], "zorluk": "orta", "aciklama": "Sadece anneden çocuklara aktarılan mitokondri genlerini tetkik etmek."},
    {"kelime": "taşıyıcı taraması yaptırmak", "yasakli_kelimeler": ["sma", "kistik fibrozis", "evlilik öncesi", "test", "sağlık"], "zorluk": "orta", "aciklama": "Evlilik öncesi kalıtsal hastalık taşıyıcılığını saptamak için taranmak."},
    {"kelime": "protein katlanmasını izlemek", "yasakli_kelimeler": ["3 boyutlu yapı", "şaperon", "fonksiyon", "bozulma", "aminoasit"], "zorluk": "orta", "aciklama": "Aminoasit zincirinin üç boyutlu işlevsel formunu almasını gözlemlemek."},
    {"kelime": "alel frekansını hesaplamak", "yasakli_kelimeler": ["popülasyon genetiği", "hardy weinberg", "oran", "gen havuzu", "yüzde"], "zorluk": "orta", "aciklama": "Bir popülasyondaki belirli bir gen varyantının görülme sıklığını bulmak."},
    {"kelime": "ökaryotik geni klonlamak", "yasakli_kelimeler": ["vektör", "ekspresyon", "konak", "laboratuvar", "üretim"], "zorluk": "orta", "aciklama": "Gelişmiş canlı genini bakteri veya mayada çoğaltıp üretmek."},
    {"kelime": "primer tasarlamak", "yasakli_kelimeler": ["oligonükleotit", "pcr", "hedef bölge", "başlatıcı", "erime sıcaklığı"], "zorluk": "orta", "aciklama": "PCR tepkimesinde hedeflenen DNA bölgesine bağlanacak başlatıcı diziyi oluşturmak."},

    # Zor (14)
    {"kelime": "cRISPR-Cas9 ile gen düzenlemek", "yasakli_kelimeler": ["rehber rna", "hedefli kesim", "genom düzenleme", "çift zincir kırığı", "doudna"], "zorluk": "zor", "aciklama": "Rehber RNA ve Cas9 enzimiyle istenen gen bölgesini hassas şekilde kesip düzenlemek."},
    {"kelime": "hardy-Weinberg dengesini test etmek", "yasakli_kelimeler": ["p2 + 2pq + q2", "genetik denge", "rastgele çiftleşme", "mutasyonsuz", "frekans"], "zorluk": "zor", "aciklama": "Popülasyondaki alel frekanslarının nesiller boyu sabit kalıp kalmadığını denkleştirmek."},
    {"kelime": "histon asetilasyonu yapmak", "yasakli_kelimeler": ["kromatini gevşetme", "gen ifadesi artışı", "epigenetik", "hat enzimi", "transkripsiyon"], "zorluk": "zor", "aciklama": "Histon proteinlerine asetil grubu ekleyerek DNA'nın transkripsiyona açılmasını sağlamak."},
    {"kelime": "dNA metilasyonunu profillemek", "yasakli_kelimeler": ["cpg adacıkları", "gen susturma", "bisülfit dizileme", "epigenetik işaret", "metil"], "zorluk": "zor", "aciklama": "Sitozin bazlarındaki metilasyon paternlerini çıkararak suskun genleri belirlemek."},
    {"kelime": "alternatif kırpılma gerçekleştirmek", "yasakli_kelimeler": ["alternative splicing", "ekzon seçimi", "intron çıkarma", "tek genden farklı protein", "mrna"], "zorluk": "zor", "aciklama": "Aynı pre-mRNA'dan farklı ekzon kombinasyonlarıyla birden çok protein türetmek."},
    {"kelime": "homolog rekombinasyonla tamir etmek", "yasakli_kelimeler": ["çift zincir kırığı", "kardeş kromatit şablonu", "hatasız tamir", "rad51", "dna"], "zorluk": "zor", "aciklama": "DNA kırıklarını kardeş kromatidi kalıp kullanarak sıfır hatayla onarmak."},
    {"kelime": "akış sitometrisi ile analiz etmek", "yasakli_kelimeler": ["flow cytometry", "hücre ayırma", "floresan antikor", "lazer", "hücre döngüsü"], "zorluk": "zor", "aciklama": "Hücreleri lazer ışığı altından tek tek geçirerek genetik floresan sinyallerini ölçmek."},
    {"kelime": "mikrodizi çipi okumak", "yasakli_kelimeler": ["microarray", "gen ekspresyonu", "hibridizasyon", "binlerce gen", "floresan ışıma"], "zorluk": "zor", "aciklama": "Binlerce genin aynı andaki aktivite düzeyini cam çip üzerindeki ışıma ile saptamak."},
    {"kelime": "gen susturma uygulamak", "yasakli_kelimeler": ["sirna", "rna interferans", "mrna yıkımı", "knocking down", "dicer"], "zorluk": "zor", "aciklama": "Küçük interferans RNA'lar yardımıyla hedef mRNA'yı parçalayarak protein üretimini durdurmak."},
    {"kelime": "karyotip haritası bantlamak", "yasakli_kelimeler": ["g-bantlama", "giemsa", "kromozom kolu", "translokasyon", "telesentrik"], "zorluk": "zor", "aciklama": "Kromozomları Giemsa boyasıyla açık ve koyu bantlara ayırıp yapısal anomalileri görmek."},
    {"kelime": "sanger dizileme yöntemi uygulamak", "yasakli_kelimeler": ["didesoksinükleotit", "zincir sonlandırma", "kapiler elektroforez", "kromatogram", "baz"], "zorluk": "zor", "aciklama": "Dideoksi nükleotitlerle zinciri durdurarak klasik yöntemle DNA dizisini okumak."},
    {"kelime": "genomik imprinting saptamak", "yasakli_kelimeler": ["ebeveyne özgü ifade", "anne veya baba suskunluğu", "metilasyon", "prader willi", "kalıtım"], "zorluk": "zor", "aciklama": "Gendeki ifadenin sadece anneden veya sadece babadan gelmesine göre belirlendiğini tespit etmek."},
    {"kelime": "telomer kısalmasını ölçmek", "yasakli_kelimeler": ["hücresel yaşlanma", "telomeraz", "kromozom ucu", "hayflick limiti", "replikasyon"], "zorluk": "zor", "aciklama": "Her bölünmede kromozom uçlarındaki koruyucu tekrar dizilerinin erimesini izlemek."},
    {"kelime": "tek hücre rNA dizilemesi yapmak", "yasakli_kelimeler": ["single cell rna-seq", "hücresel heterojenlik", "transkriptom", "bireysel hücre", "biyoenformatik"], "zorluk": "zor", "aciklama": "Dokudaki her bir hücrenin gen ifadesini tek tek izole edip dizilemek."}
]

# 20. havacilik
havacilik_verbs = [
    # Kolay (12)
    {"kelime": "uçağa binmek", "yasakli_kelimeler": ["bilet", "yolcu", "havalimanı", "koltuk", "kapı"], "zorluk": "kolay", "aciklama": "Hava yoluyla seyahat etmek için uçağın içine geçmek."},
    {"kelime": "uçak uçurmak", "yasakli_kelimeler": ["pilot", "gökyüzü", "hava", "kanat", "kullanmak"], "zorluk": "kolay", "aciklama": "Hava aracını gökyüzünde sevk ve idare etmek."},
    {"kelime": "piste inmek", "yasakli_kelimeler": ["iniş", "tekerlek", "havalimanı", "fren", "alçalmak"], "zorluk": "kolay", "aciklama": "Uçağın havadaki yolculuğunu tamamlayıp tekerleklerini asfalta değdirmesi."},
    {"kelime": "havalanmak", "yasakli_kelimeler": ["kalkış", "uçmak", "yerden kesilmek", "yükselmek", "pist"], "zorluk": "kolay", "aciklama": "Uçağın hızlanarak tekerleklerinin yerden ayrılıp yükselmesi."},
    {"kelime": "kemer bağlamak", "yasakli_kelimeler": ["güvenlik", "koltuk", "toka", "ikaz ışığı", "oturtmak"], "zorluk": "kolay", "aciklama": "Kalkış ve iniş sırasında yolcu koltuğundaki emniyet bandını kilitlemek."},
    {"kelime": "bavul teslim etmek", "yasakli_kelimeler": ["bagaj", "check-in", "kontuar", "tartı", "etiket"], "zorluk": "kolay", "aciklama": "Uçağın kargo bölümüne konulacak çantaları gişeye vermek."},
    {"kelime": "pilot olmak", "yasakli_kelimeler": ["kaptan", "kokpit", "üniforma", "uçuş", "eğitim"], "zorluk": "kolay", "aciklama": "Uçak kullanma yetki ve mesleğini icra etmek."},
    {"kelime": "anons yapmak", "yasakli_kelimeler": ["kaptan konuşuyor", "hostes", "hoparlör", "bilgilendirme", "ses"], "zorluk": "kolay", "aciklama": "Uçuşla ilgili bilgileri kabin hoparlöründen yolculara duyurmak."},
    {"kelime": "bilet almak", "yasakli_kelimeler": ["rezervasyon", "koltuk seçimi", "uçuş", "fiyat", "havayolu"], "zorluk": "kolay", "aciklama": "Uçakta yer ayırtıp seyahat hakkı satın almak."},
    {"kelime": "pencereden bakmak", "yasakli_kelimeler": ["bulut", "manzara", "aşağısı", "gökyüzü", "küçük cam"], "zorluk": "kolay", "aciklama": "Uçak penceresinden bulutları ve yeryüzünü seyretmek."},
    {"kelime": "parasütle atlamak", "yasakli_kelimeler": ["paraşüt", "boşluk", "süzülmek", "yükseklik", "uçaktan"], "zorluk": "kolay", "aciklama": "Uçaktan kendini boşluğa bırakıp paraşüt açarak yere süzülmek."},
    {"kelime": "pasaport kontrolünden geçmek", "yasakli_kelimeler": ["polis", "damga", "yurt dışı", "havalimanı", "sıra"], "zorluk": "kolay", "aciklama": "Uluslararası uçuş öncesi kimlik ve vize denetiminden geçmek."},

    # Orta (24)
    {"kelime": "türbülansa girmek", "yasakli_kelimeler": ["sarsıntı", "hava boşluğu", "irtifa", "kemeri bağlayın", "dalgalanma"], "zorluk": "orta", "aciklama": "Uçağın düzensiz hava akımları nedeniyle havada sarsılması."},
    {"kelime": "iniş takımlarını açmak", "yasakli_kelimeler": ["tekerlek", "yaklaşma", "lövye", "hidrolik", "pist"], "zorluk": "orta", "aciklama": "İnişten hemen önce gövdede saklı tekerlekleri dışarı çıkarmak."},
    {"kelime": "rotayı belirlemek", "yasakli_kelimeler": ["uçuş planı", "navigasyon", "hava koridoru", "koordinat", "hedef"], "zorluk": "orta", "aciklama": "Kalkıştan varışa kadar izlenecek hava koridorunu çizmek."},
    {"kelime": "kuleyle telsiz bağlantısı kurmak", "yasakli_kelimeler": ["atc", "hava trafik kontrolörü", "frekans", "izin", "roger"], "zorluk": "orta", "aciklama": "Kalkış ve iniş müsaadesi için yer kontrolüyle radyo irtibatı kurmak."},
    {"kelime": "irtifa kazanmak", "yasakli_kelimeler": ["tırmanış", "feet", "yükseklik", "varyometre", "motor gücü"], "zorluk": "orta", "aciklama": "Uçağın deniz seviyesinden olan yüksekliğini artırması."},
    {"kelime": "otopilota almak", "yasakli_kelimeler": ["otomatik uçuş", "sistem", "seyir", "bilgisayar", "düğme"], "zorluk": "orta", "aciklama": "Uçuş kumandasını bilgisayar destekli otomatik kontrol sistemine devretmek."},
    {"kelime": "taksi yapmak", "yasakli_kelimeler": ["taksi yolu", "yerde ilerleme", "park pozisyonu", "körük", "yavaş"], "zorluk": "orta", "aciklama": "Uçağın yerde motor gücüyle pistten körüğe veya piste doğru ilerlemesi."},
    {"kelime": "flapları açmak", "yasakli_kelimeler": ["kanat uzantısı", "taşıma kuvveti", "kalkış iniş", "hava direnci", "açı"], "zorluk": "orta", "aciklama": "Düşük hızlarda kanadın kaldırma kuvvetini artırmak için arka kanatçıkları uzatmak."},
    {"kelime": "kara kutuyu incelemek", "yasakli_kelimeler": ["fdr", "cvr", "kaza kırım", "ses kaydı", "turuncu kutu"], "zorluk": "orta", "aciklama": "Kaza sonrası uçuş verilerini ve kokpit konuşmalarını deşifre etmek."},
    {"kelime": "pas geçmek", "yasakli_kelimeler": ["go around", "inişi iptal etme", "tekrar yükselme", "güvensiz yaklaşma", "gaz açma"], "zorluk": "orta", "aciklama": "Piste yaklaşma uygun olmadığında teker koymadan tekrar gaz açıp tırmanmak."},
    {"kelime": "uçak yakıtı ikmali yapmak", "yasakli_kelimeler": ["kerosen", "jet a1", "tanker", "kanat deposu", "dolum"], "zorluk": "orta", "aciklama": "Uçağın kanat depolarına tonlarca kerosen yakıtı doldurmak."},
    {"kelime": "kabin basıncını ayarlamak", "yasakli_kelimeler": ["oksijen", "basınçlandırma", "yükseklik", "outflow valve", "maske"], "zorluk": "orta", "aciklama": "Yüksek irtifada yolcuların nefes alabilmesi için kabin iç havasını basınçlandırmak."},
    {"kelime": "de-icing yaptırmak", "yasakli_kelimeler": ["buz çözme", "glikol sıvısı", "kanat", "kış", "püskürtme aracı"], "zorluk": "orta", "aciklama": "Kalkış öncesi kanat ve gövdedeki kar ve buzları sıcak kimyasal sıvıyla eritmek."},
    {"kelime": "simülatörde eğitim almak", "yasakli_kelimeler": ["kokpit simülasyonu", "acil durum", "tip eğitimi", "uçuş saati", "hidrolik kabin"], "zorluk": "orta", "aciklama": "Gerçek uçuş öncesi tüm acil senaryoları sanal kokpit kabininde pratik etmek."},
    {"kelime": "rüçhan hakkı istemek", "yasakli_kelimeler": ["mayday", "pan pan", "acil durum çağrısı", "öncelikli iniş", "motor arızası"], "zorluk": "orta", "aciklama": "Acil durum sebebiyle kuleye bildirim yapıp öncelikli iniş sırası talep etmek."},
    {"kelime": "pushback yapmak", "yasakli_kelimeler": ["geri itme aracı", "körükten ayrılma", "traktör", "towcar", "park yeri"], "zorluk": "orta", "aciklama": "Uçağı körükten özel yer aracıyla geri doğru iterek çıkarmak."},
    {"kelime": "hava radarını kontrol etmek", "yasakli_kelimeler": ["fırtına hücresi", "cb bulutu", "kırmızı ekolar", "kokpit ekranı", "kaçınma"], "zorluk": "orta", "aciklama": "Uçuş hattındaki tehlikeli fırtına bulutlarını kokpit radarından gözlemek."},
    {"kelime": "slipstream etkisine girmek", "yasakli_kelimeler": ["girdap", "wake turbulence", "önceki büyük uçak", "kanat ucu vorteksi", "ayrılma mesafesi"], "zorluk": "orta", "aciklama": "Öndeki uçağın arkasında bıraktığı güçlü kanat ucu hava türbülansına maruz kalmak."},
    {"kelime": "fren pabucu kontrolü yapmak", "yasakli_kelimeler": ["tekerlek", "fren sıcaklığı", "bakım", "teknisyen", "aşınma"], "zorluk": "orta", "aciklama": "İnişte aşırı ısınan karbon frenlerin durumunu yer teknisyenine kontrol ettirmek."},
    {"kelime": "slot saatine yetişmek", "yasakli_kelimeler": ["kalkış zaman aralığı", "gecikme", "eurocontrol", "havalimanı trafiği", "izin"], "zorluk": "orta", "aciklama": "Trafiğin yoğun olduğu saatlerde tahsis edilen kalkış dakikasına uymak."},
    {"kelime": "check-list okumak", "yasakli_kelimeler": ["kontrol listesi", "kaptan ikinci pilot", "before takeoff", "maddeler", "onaylama"], "zorluk": "orta", "aciklama": "Kalkış veya iniş öncesi prosedür maddelerini karşılıklı sesli teyit etmek."},
    {"kelime": "stalling durumuna düşmek", "yasakli_kelimeler": ["perdövites", "hücum açısı aşımı", "kaldırma kuvveti kaybı", "burun düşmesi", "hız"], "zorluk": "orta", "aciklama": "Hücum açısının aşırı artması sonucu kanatların tutunmayı tamamen kaybetmesi."},
    {"kelime": "trim ayarı yapmak", "yasakli_kelimeler": ["fletner", "lövye yükünü alma", "düz uçuş", "dengelemek", "kumanda"], "zorluk": "orta", "aciklama": "Pilotun lövyeyi sürekli çekmek zorunda kalmaması için kontrol yüzeyini dengelemek."},
    {"kelime": "kabin ekibini koordine etmek", "yasakli_kelimeler": ["purser", "kabin amiri", "brifing", "servis", "güvenlik"], "zorluk": "orta", "aciklama": "Uçuş öncesi host ve hosteslerin görev dağılımını ve acil durum brifingini yapmak."},

    # Zor (14)
    {"kelime": "iLS yaklaşması icra etmek", "yasakli_kelimeler": ["aletli iniş sistemi", "glideslope", "localizer", "sis", "otomatik süzülüş"], "zorluk": "zor", "aciklama": "Düşük görüş şartlarında uçağı radyo sinyalleri kılavuzluğunda piste indirmek."},
    {"kelime": "tcAS uyarısına uymak", "yasakli_kelimeler": ["havada çarpışma önleme", "resolution advisory", "climb descend", "transponder", "ikaz"], "zorluk": "zor", "aciklama": "Çarpışma rotasındaki iki uçağı kurtaran otomatik sesli yönlendirmeye derhal uymak."},
    {"kelime": "eTOPS sertifikasyonu almak", "yasakli_kelimeler": ["çift motorlu", "okyanus aşırı", "yedek meydana mesafe", "dakika kuralı", "güvenilirlik"], "zorluk": "zor", "aciklama": "Çift motorlu uçağın okyanus aşırı rotalarda yedek meydandan uzakta uçabilme iznini almak."},
    {"kelime": "v1 hızında karar vermek", "yasakli_kelimeler": ["kalkış karar hızı", "kalkıştan vazgeçme", "frenleme sınırı", "kesin kalkış", "motor arızası"], "zorluk": "zor", "aciklama": "Pistte bu kritik hıza ulaşıldığında arıza olsa dahi kalkışa devam kararını uygulamak."},
    {"kelime": "transonik şok dalgası üretmek", "yasakli_kelimeler": ["ses duvarı", "mach 1", "süpersonik", "basınç dalgası", "kritik mach"], "zorluk": "zor", "aciklama": "Uçağın hızı ses hızına yaklaştığında kanat üzerinde süpersonik hava akışı oluşturmak."},
    {"kelime": "tCAS RA kaçınma manevrası yapmak", "yasakli_kelimeler": ["lövyeyi çekme basma", "atc talimatını yok sayma", "otomatik uyarı", "irtifa değişimi", "çarpışma riski"], "zorluk": "zor", "aciklama": "Kule talimatı yerine TCAS sisteminin tırman/alçal komutunu anında uygulamak."},
    {"kelime": "kabin dekompresyonu yaşamak", "yasakli_kelimeler": ["ani basınç kaybı", "oksijen maskelerinin düşmesi", "acil alçalma", "10000 feet", "gövde yırtılması"], "zorluk": "zor", "aciklama": "Gövdedeki hasar nedeniyle kabin basıncının aniden düşmesi ve acil dalışa geçilmesi."},
    {"kelime": "rNAV rotası uçmak", "yasakli_kelimeler": ["alan seyrüseferi", "gps waas", "yer istasyonundan bağımsız", "hassas nokta", "gnss"], "zorluk": "zor", "aciklama": "Yer tabanlı istasyonlara bağlı kalmadan uydu koordinatlarıyla hassas hava yolu izlemek."},
    {"kelime": "yaw damper sistemini devreye sokmak", "yasakli_kelimeler": ["dutch roll", "sapma sönümleyici", "dümen kontrolü", "ok açılı kanat", "salınım engelleme"], "zorluk": "zor", "aciklama": "Ok açılı uçaklarda meydana gelen yuvarlanma-sapma salınımını otomatik düzeltmek."},
    {"kelime": "fADEC üzerinden motor yönetmek", "yasakli_kelimeler": ["tam yetkili dijital motor kontrolü", "itki", "yakıt akışı", "elektronik ünite", "koruma"], "zorluk": "zor", "aciklama": "Jet motorunun tüm parametrelerini çift kanallı dijital bilgisayarla optimize etmek."},
    {"kelime": "crosswind inişi yapmak", "yasakli_kelimeler": ["yan rüzgar", "crab açısı", "tekere tek teker koyma", "rudder", "kayma"], "zorluk": "zor", "aciklama": "Piste dik esen sert rüzgarda uçağın burnunu rüzgara çevirerek yengeç yürüyüşüyle inmek."},
    {"kelime": "vREF hızını hesaplamak", "yasakli_kelimeler": ["iniş referans hızı", "ağırlık", "1.3 vs0", "eşik geçişi", "flap konfigürasyonu"], "zorluk": "zor", "aciklama": "Uçağın iniş anındaki brüt ağırlığına göre pist başı geçiş hızını saptamak."},
    {"kelime": "fly-by-wire kumandası vermek", "yasakli_kelimeler": ["elektronik uçuş kontrolü", "mekanik bağlantısız", "side-stick", "zarf koruması", "bilgisayar"], "zorluk": "zor", "aciklama": "Pilot girdilerini kablo ve teller yerine elektrik sinyalleri ve bilgisayarlarla kanatlara iletmek."},
    {"kelime": "thrust reverser açmak", "yasakli_kelimeler": ["ters itki", "motor freni", "hava yönlendirme kapakları", "teker koyma anı", "gürültülü yavaşlama"], "zorluk": "zor", "aciklama": "Tekerlekler piste değer değmez motor hava akışını öne yönlendirerek uçağı frenlemek."}
]

add_and_save_verbs('genetik', genetik_verbs)
add_and_save_verbs('havacilik', havacilik_verbs)
print('P10 done!')
