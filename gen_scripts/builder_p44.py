# -*- coding: utf-8 -*-
from card_utils import add_and_save_verbs

siber_verbs = [
    # Kolay (12)
    {"kelime": "şifre koymak", "aciklama": "hesabı korumak için harf ve rakamlardan güçlü parola belirlemek", "yasakli_kelimeler": ["parola", "güçlü", "karakter", "koruma", "hesap"], "zorluk": "kolay"},
    {"kelime": "hacklemek", "aciklama": "yetkisiz şekilde bir bilgisayar sistemine veya web sitesine sızmak", "yasakli_kelimeler": ["sızmak", "yetkisiz", "sistem", "korsan", "ele geçirme"], "zorluk": "kolay"},
    {"kelime": "virüs bulaşmak", "aciklama": "zararlı yazılımın bilgisayara girip dosyalara zarar vermesi", "yasakli_kelimeler": ["zararlı yazılım", "bulaşma", "dosya", "hasar", "antivirüs"], "zorluk": "kolay"},
    {"kelime": "taramak", "aciklama": "antivirüs programıyla tüm diski zararlı kodlara karşı kontrol etmek", "yasakli_kelimeler": ["antivirüs", "disk", "kontrol", "temizlik", "bulmak"], "zorluk": "kolay"},
    {"kelime": "engellemek", "aciklama": "güvenlik duvarıyla şüpheli internet trafiğini ve ip adreslerini kesmek", "yasakli_kelimeler": ["güvenlik duvarı", "ip adresi", "trafik", "yasak", "bloke"], "zorluk": "kolay"},
    {"kelime": "güncellemek", "aciklama": "işletim sistemindeki güvenlik açıklarını kapatmak için yeni sürümü yüklemek", "yasakli_kelimeler": ["yama", "güvenlik açığı", "yeni sürüm", "yüklemek", "update"], "zorluk": "kolay"},
    {"kelime": "yedeklemek", "aciklama": "verilerin kaybolmaması için harici diske veya buluta kopyasını almak", "yasakli_kelimeler": ["backup", "bulut", "harici disk", "kopyalama", "kurtarma"], "zorluk": "kolay"},
    {"kelime": "şifre kırmak", "aciklama": "unutulan veya başkasına ait parolayı deneme yanılmayla çözmek", "yasakli_kelimeler": ["brute force", "çözmek", "deneme", "ele geçirme", "parola"], "zorluk": "kolay"},
    {"kelime": "gizlemek", "aciklama": "vpn kullanarak gerçek ip adresini ve konumunu internetten saklamak", "yasakli_kelimeler": ["vpn", "ip adresi", "konum", "anonim", "saklama"], "zorluk": "kolay"},
    {"kelime": "silmek", "aciklama": "virüslü dosyayı veya diski tamamen sıfırlayıp temizlemek", "yasakli_kelimeler": ["temizlemek", "yok etmek", "format", "dosya", "sıfırlama"], "zorluk": "kolay"},
    {"kelime": "uyarmak", "aciklama": "sistem güvenlik ihlali algıladığında yöneticiye acil e-posta göndermek", "yasakli_kelimeler": ["alarm", "bildirim", "güvenlik ihlali", "uyarı", "yönetici"], "zorluk": "kolay"},
    {"kelime": "giriş yapmak", "aciklama": "kullanıcı adı ve şifreyle sisteme yetkili olarak oturum açmak", "yasakli_kelimeler": ["login", "oturum", "kullanıcı adı", "erişim", "yetki"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "oltalama yapmak", "aciklama": "sahte banka e-postası atarak kurbanın şifresini ve kartını çalmak", "yasakli_kelimeler": ["phishing", "sahte mail", "yemleme", "tuzak", "kandırma"], "zorluk": "orta"},
    {"kelime": "sızma testi yapmak", "aciklama": "etik hacker olarak şirketin sunucularındaki açıkları denetlemek", "yasakli_kelimeler": ["penetrasyon", "pentest", "etik hacker", "açık arama", "güvenlik testi"], "zorluk": "orta"},
    {"kelime": "ddos atağı başlatmak", "aciklama": "milyonlarca bot cihazla web sitesine aynı anda istek atıp çökertmek", "yasakli_kelimeler": ["çökertme", "botnet", "aşırı istek", "hizmet dışı", "trafik patlaması"], "zorluk": "orta"},
    {"kelime": "fidye yazılımı bulaştırmak", "aciklama": "kurbanın tüm sabit diskini şifreleyip açmak için bitcoin talep etmek", "yasakli_kelimeler": ["ransomware", "dosya şifreleme", "bitcoin", "fidye", "kilit"], "zorluk": "orta"},
    {"kelime": "trojan sokmak", "aciklama": "faydalı bir program gibi görünen truva atı virüsüyle arka kapı açmak", "yasakli_kelimeler": ["truva atı", "arka kapı", "backdoor", "casus", "zararlı yazılım"], "zorluk": "orta"},
    {"kelime": "keylogger yerleştirmek", "aciklama": "klavyede basılan tüm tuşları gizlice kaydedip saldırgana göndermek", "yasakli_kelimeler": ["tuş kaydı", "klavye", "şifre çalma", "gizli kayıt", "izleme"], "zorluk": "orta"},
    {"kelime": "iki faktörlü doğrulamak", "aciklama": "şifreye ek olarak telefona gelen sms veya authenticator kodunu girmek", "yasakli_kelimeler": ["2fa", "sms kodu", "authenticator", "çift aşama", "ekstra güvenlik"], "zorluk": "orta"},
    {"kelime": "port taraması yapmak", "aciklama": "nmap aracıyla hedef sunucunun hangi ağ kapılarının açık olduğunu bulmak", "yasakli_kelimeler": ["nmap", "açık port", "tarama", "sunucu", "ağ kapısı"], "zorluk": "orta"},
    {"kelime": "paket dinlemek", "aciklama": "wireshark programıyla yerel ağdaki şifrelenmemiş veri paketlerini yakalamak", "yasakli_kelimeler": ["wireshark", "sniffing", "ağ trafiği", "paket yakalama", "şifresiz"], "zorluk": "orta"},
    {"kelime": "ortadaki adam olmak", "aciklama": "kullanıcı ile modem arasına girip giden gelen tüm verileri gizlice okumak", "yasakli_kelimeler": ["mitm", "araya girme", "arp zehirleme", "modem", "gizli dinleme"], "zorluk": "orta"},
    {"kelime": "sql enjeksiyonu denemek", "aciklama": "arama kutusuna özel sql komutları yazarak veri tabanını dışarı dökmek", "yasakli_kelimeler": ["sql injection", "veri tabanı", "sorgu", "tablo sızdırma", "kod enjeksiyonu"], "zorluk": "orta"},
    {"kelime": "xss açığı aramak", "aciklama": "web sitesinin yorum alanına kötü niyetli javascript kodu gömmek", "yasakli_kelimeler": ["cross site scripting", "javascript", "çerez çalma", "zararlı script", "web açığı"], "zorluk": "orta"},
    {"kelime": "sosyal mühendislik yapmak", "aciklama": "kendini bilgi işlem görevlisi gibi tanıtıp kurbandan şifresini telefonda almak", "yasakli_kelimeler": ["insan kandırma", "manipülasyon", "rol yapma", "güven suiistimali", "psikolojik hile"], "zorluk": "orta"},
    {"kelime": "kriptografik imzalamak", "aciklama": "belgenin kaynağını ve değişmediğini asimetrik özel anahtarla mühürlemek", "yasakli_kelimeler": ["dijital imza", "özel anahtar", "doğrulama", "bütünlük", "asimetrik"], "zorluk": "orta"},
    {"kelime": "karantinaya almak", "aciklama": "şüpheli zararlı dosyayı diğer dosyalardan izole edip çalıştırmasını engellemek", "yasakli_kelimeler": ["izolasyon", "şüpheli dosya", "antivirüs kasası", "engelleme", "çalıştırmama"], "zorluk": "orta"},
    {"kelime": "vpn tüneli kurmak", "aciklama": "evdeki bilgisayar ile şirket ağı arasında uçtan uca şifreli güvenli hat açmak", "yasakli_kelimeler": ["şifreli tünel", "uzaktan erişim", "şirket ağı", "ipsec", "openvpn"], "zorluk": "orta"},
    {"kelime": "ip spoofing yapmak", "aciklama": "ağ paketlerinin başlığındaki kaynak ip adresini sahte bir numarayla değiştirmek", "yasakli_kelimeler": ["sahte ip", "başlık değiştirme", "kimlik gizleme", "paket sahteciliği", "aldatma"], "zorluk": "orta"},
    {"kelime": "güvenlik duvarı kuralı yazmak", "aciklama": "gelen trafiğin belirli port ve ip aralıklarından geçişine izin vermek veya kesmek", "yasakli_kelimeler": ["iptables", "firewall kuralı", "erişim listesi", "port kısıtlama", "engelleme"], "zorluk": "orta"},
    {"kelime": "soc merkezinde izlemek", "aciklama": "güvenlik operasyon merkezinde 7/24 log kayıtlarını ve saldırı uyarılarını takip etmek", "yasakli_kelimeler": ["soc", "güvenlik operasyon", "7/24", "siem", "olay izleme"], "zorluk": "orta"},
    {"kelime": "parola yöneticisi kullanmak", "aciklama": "yüzlerce karmaşık şifreyi tek bir ana parolayla kasada şifreli saklamak", "yasakli_kelimeler": ["password manager", "kasa", "ana şifre", "otomatik doldurma", "saklama"], "zorluk": "orta"},
    {"kelime": "sözlük saldırısı yapmak", "aciklama": "milyonlarca kelimelik wordlist dosyasıyla parola kırma yazılımı çalıştırmak", "yasakli_kelimeler": ["wordlist", "sözlük", "deneme", "rockyou", "parola denemesi"], "zorluk": "orta"},
    {"kelime": "çerez çalmak", "aciklama": "tarayıcıda kayıtlı oturum kimliğini ele geçirip şifresiz hesaba girmek", "yasakli_kelimeler": ["cookie", "oturum kimliği", "session hijacking", "tarayıcı", "şifresiz giriş"], "zorluk": "orta"},
    {"kelime": "arka kapı bırakmak", "aciklama": "sunucuya ilk girişte daha sonra tekrar kolayca sızabilmek için gizli kullanıcı açmak", "yasakli_kelimeler": ["backdoor", "gizli giriş", "kalıcılık sağlama", "webshell", "yetki"], "zorluk": "orta"},
    {"kelime": "yetki yükseltmek", "aciklama": "düşük yetkili normal kullanıcı hesabından sunucunun root veya admin yetkisine zıplamak", "yasakli_kelimeler": ["privilege escalation", "root yetkisi", "admin olma", "çekirdek açığı", "tam yetki"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "sıfır gün açığı sömürmek", "aciklama": "üreticinin henüz bilmediği ve yaması olmayan yazılım açığını exploit etmek", "yasakli_kelimeler": ["zero day", "yamasız açık", "exploit", "keşfedilmemiş", "istismar"], "zorluk": "zor"},
    {"kelime": "tersine mühendislik yapmak", "aciklama": "derlenmiş kötü amaçlı yazılım ikili kodunu ida pro veya ghidra ile söküp analiz etmek", "yasakli_kelimeler": ["disassembler", "ghidra", "ida pro", "ikili kod", "assembly"], "zorluk": "zor"},
    {"kelime": "arabellek taşması tetiklemek", "aciklama": "bellek yığınına ayrılan boyuttan fazla veri yazıp dönüş adresini ele geçirmek", "yasakli_kelimeler": ["buffer overflow", "yığın", "dönüş adresi", "eip kaydı", "bellek manipülasyonu"], "zorluk": "zor"},
    {"kelime": "apt grubu izlemek", "aciklama": "devlet destekli gelişmiş kalıcı tehdit aktörlerinin siber casusluk operasyonlarını deşifre etmek", "yasakli_kelimeler": ["advanced persistent threat", "devlet destekli", "siber casusluk", "kalıcı tehdit", "ulus devlet"], "zorluk": "zor"},
    {"kelime": "siem korelasyonu kurmak", "aciklama": "milyonlarca ağ logunu güvenlik bilgi ve olay yönetim yazılımında eşleştirip alarm üretmek", "yasakli_kelimeler": ["siem", "log korelasyonu", "splunk", "olay tespiti", "alarm kuralı"], "zorluk": "zor"},
    {"kelime": "bal küpü kurmak", "aciklama": "saldırganları kandırmak ve taktiklerini öğrenmek için kasten savunmasız sahte sunucu açmak", "yasakli_kelimeler": ["honeypot", "sahte sunucu", "tuzak sistem", "saldırgan izleme", "yemleme"], "zorluk": "zor"},
    {"kelime": "kum havuzunda patlatmak", "aciklama": "şüpheli virüsü izole sanal makinede çalıştırıp dosya ve ağ davranışını izlemek", "yasakli_kelimeler": ["sandbox", "sanal makine", "davranış analizi", "izole ortam", "dinamik analiz"], "zorluk": "zor"},
    {"kelime": "bellek adli bilişimi", "aciklama": "bilgisayarın ram dökümünü volatility aracıyla tarayıp belleğe gizlenmiş zararlıyı bulmak", "yasakli_kelimeler": ["volatility", "ram dökümü", "adli bilişim", "bellek analizi", "canlı inceleme"], "zorluk": "zor"},
    {"kelime": "dijital delil toplamak", "aciklama": "suçlu bilgisayarının sabit diskinden write blocker ile adli kopyasını mühürleyip almak", "yasakli_kelimeler": ["adli kopya", "write blocker", "zincirleme kanıt", "hash değeri", "forensic"], "zorluk": "zor"},
    {"kelime": "fuzzing ile açık aramak", "aciklama": "yazılım girdisine otomatik olarak milyonlarca rastgele geçersiz veri basıp çökmeleri bulmak", "yasakli_kelimeler": ["fuzzer", "rastgele girdi", "çökme analizi", "otomatik test", "açık keşfi"], "zorluk": "zor"},
    {"kelime": "asimetrik şifrelemek", "aciklama": "rsa veya eliptik eğri ile açık anahtarla şifreleyip sadece gizli anahtarla çözmek", "yasakli_kelimeler": ["rsa", "eliptik eğri", "açık anahtar", "gizli anahtar", "asimetrik"], "zorluk": "zor"},
    {"kelime": "rop zinciri oluşturmak", "aciklama": "dep/nx korumasını aşmak için bellekteki mevcut kod parçacıklarını uç uca eklemek", "yasakli_kelimeler": ["return oriented", "gadget", "dep koruması", "yığın çalıştırma", "istismar"], "zorluk": "zor"},
    {"kelime": "red team tatbikatı yapmak", "aciklama": "şirketin güvenlik ekiplerine haber vermeden tam kapsamlı siber saldırı simülasyonu yürütmek", "yasakli_kelimeler": ["kırmızı takım", "blue team", "tatbikat", "simülasyon", "sızma harekatı"], "zorluk": "zor"},
    {"kelime": "steganografi ile gizlemek", "aciklama": "gizli casusluk metnini masum bir kedi fotoğrafının pikselleri arasına şifreleyip gömmek", "yasakli_kelimeler": ["görsel içi gizleme", "steganografi", "piksel saklama", "masum dosya", "örtük iletişim"], "zorluk": "zor"}
]

sinema_verbs = [
    # Kolay (12)
    {"kelime": "film çekmek", "aciklama": "kamerayla oyuncuları kaydedip sinema filmi üretmek", "yasakli_kelimeler": ["kamera", "oyuncu", "kayıt", "yönetmen", "sinema"], "zorluk": "kolay"},
    {"kelime": "rol yapmak", "aciklama": "senaryodaki karakterin kişiliğine bürünüp sahnede oynamak", "yasakli_kelimeler": ["oyuncu", "karakter", "senaryo", "sahne", "oynamak"], "zorluk": "kolay"},
    {"kelime": "izlemek", "aciklama": "salonda mısır yiyerek beyaz perdedeki filmi seyretmek", "yasakli_kelimeler": ["seyretmek", "beyaz perde", "patlamış mısır", "salon", "seyirci"], "zorluk": "kolay"},
    {"kelime": "senaryo yazmak", "aciklama": "filmin hikayesini, diyaloglarını ve sahnelerini kağıda dökmek", "yasakli_kelimeler": ["hikaye", "diyalog", "yazar", "sahne", "metin"], "zorluk": "kolay"},
    {"kelime": "kurgulamak", "aciklama": "çekilen sahneleri bilgisayarda sıraya dizip birbirine bağlamak", "yasakli_kelimeler": ["montaj", "kesmek", "bağlamak", "sıralamak", "sahne"], "zorluk": "kolay"},
    {"kelime": "yönetmek", "aciklama": "sette oyunculara ve kamera ekibine talimat verip vizyonunu aktarmak", "yasakli_kelimeler": ["yönetmen", "set", "talimat", "vizyon", "ekip"], "zorluk": "kolay"},
    {"kelime": "klaket vurmak", "aciklama": "çekim başlamadan önce sahne ve plan numarasını yazıp şaklatmak", "yasakli_kelimeler": ["şaklatmak", "sahne numarası", "ses senkronu", "tahta", "kayıt öncesi"], "zorluk": "kolay"},
    {"kelime": "bilet almak", "aciklama": "sinema gişesinden veya internetten koltuk seçip ödeme yapmak", "yasakli_kelimeler": ["gişe", "koltuk", "ödeme", "seans", "salon"], "zorluk": "kolay"},
    {"kelime": "ağlamak", "aciklama": "duygusal dram filmindeki hüzünlü sahnede gözyaşı dökmek", "yasakli_kelimeler": ["dram", "gözyaşı", "hüzün", "duygusal", "sahne"], "zorluk": "kolay"},
    {"kelime": "gülmek", "aciklama": "komedi filmindeki esprilere ve komik sahnelere kahkaha atmak", "yasakli_kelimeler": ["komedi", "kahkaha", "espri", "komik", "eğlenmek"], "zorluk": "kolay"},
    {"kelime": "ışıklandırmak", "aciklama": "sahnenin atmosferine uygun spot ve panelleri yerleştirmek", "yasakli_kelimeler": ["spot", "lamba", "set", "aydınlatma", "gölge"], "zorluk": "kolay"},
    {"kelime": "ödül almak", "aciklama": "film festivalinde en iyi film veya en iyi oyuncu heykelciğini kazanmak", "yasakli_kelimeler": ["oscar", "festival", "heykelcik", "altın portakal", "kazanmak"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "dublaj yapmak", "aciklama": "yabancı dildeki filmin diyaloglarını stüdyoda türkçe seslendirmek", "yasakli_kelimeler": ["seslendirme", "yabancı film", "stüdyo", "çeviri", "dudak senkronu"], "zorluk": "orta"},
    {"kelime": "alt yazı eklemek", "aciklama": "konuşulan yabancı sözleri ekranın altına çeviri metni olarak yazmak", "yasakli_kelimeler": ["altyazı", "çeviri", "ekran altı", "okuma", "metin"], "zorluk": "orta"},
    {"kelime": "yeşil perde kullanmak", "aciklama": "arkaya yeşil fon koyup sonradan dijital efekt ve mekan yerleştirmek", "yasakli_kelimeler": ["green screen", "arka fon", "dijital efekt", "chroma key", "cst"], "zorluk": "orta"},
    {"kelime": "storyboard çizmek", "aciklama": "senaryodaki her planı çizgi roman gibi kare kare resmedip planlamak", "yasakli_kelimeler": ["resimli taslak", "kare kare", "plan", "çizim", "görsel hazırlık"], "zorluk": "orta"},
    {"kelime": "ses miksajı yapmak", "aciklama": "diyalog, müzik ve ortam ses efektlerinin seviyelerini 5.1 kanalda dengelemek", "yasakli_kelimeler": ["foley", "ses efekti", "diyalog dengesi", "5.1", "mikser"], "zorluk": "orta"},
    {"kelime": "renk düzenlemesi yapmak", "aciklama": "çekilen filmin renk tonlarını sahnenin duygusuna göre stilize etmek", "yasakli_kelimeler": ["color grading", "lut", "renk tonu", "davinci", "atmosfer"], "zorluk": "orta"},
    {"kelime": "casting yapmak", "aciklama": "senaryodaki roller için deneme çekimi yapıp uygun oyuncuları seçmek", "yasakli_kelimeler": ["oyuncu seçimi", "deneme çekimi", "rol dağıtımı", "cast ajansı", "audition"], "zorluk": "orta"},
    {"kelime": "prömiyer yapmak", "aciklama": "filmin ilk gösterimini yönetmen ve oyuncuların katıldığı galada yapmak", "yasakli_kelimeler": ["gala gecesi", "ilk gösterim", "kırmızı halı", "davetliler", "vizyon"], "zorluk": "orta"},
    {"kelime": "gişe rekoru kırmak", "aciklama": "vizyona girdiği ilk hafta sonunda milyonlarca bilet satıp rekor yapmak", "yasakli_kelimeler": ["box office", "hasılat", "milyon bilet", "izleyici sayısı", "rekor"], "zorluk": "orta"},
    {"kelime": "kestik diye bağırmak", "aciklama": "yönetmenin sahneyi durdurmak ve yeniden başlatmak için bağırması", "yasakli_kelimeler": ["cut", "yönetmen", "durdurma", "tekrar", "sahne sonu"], "zorluk": "orta"},
    {"kelime": "kayıt diye seslenmek", "aciklama": "yönetmen yardımcısının kamera ve sesin başladığını sete duyurması", "yasakli_kelimeler": ["motor", "başlama", "sessizlik", "set", "çekim anı"], "zorluk": "orta"},
    {"kelime": "makyaj yapmak", "aciklama": "plastik makyajla oyuncuyu yaşlandırmak veya yara izleri oluşturmak", "yasakli_kelimeler": ["plastik makyaj", "yara izi", "yaşlandırma", "protez", "karakter"], "zorluk": "orta"},
    {"kelime": "kostüm hazırlamak", "aciklama": "dönem filmine uygun tarihi kıyafetleri dikip oyunculara giydirmek", "yasakli_kelimeler": ["tarihi kıyafet", "dönem filmi", "gardırop", "giysi", "tasarım"], "zorluk": "orta"},
    {"kelime": "mekan keşfi yapmak", "aciklama": "çekim yapılacak terk edilmiş bina veya ormanlık alanı önceden gezmek", "yasakli_kelimeler": ["location scouting", "çekim yeri", "mekan", "keşif", "plato"], "zorluk": "orta"},
    {"kelime": "vizyona sokmak", "aciklama": "tamamlanan filmi ülke genelindeki sinema salonlarında gösterime açmak", "yasakli_kelimeler": ["gösterim", "sinema salonu", "vizyon tarihi", "dağıtım", "afiş"], "zorluk": "orta"},
    {"kelime": "fragman hazırlamak", "aciklama": "filmin en heyecanlı sahnelerinden 2 dakikalık tanıtım videosu kurgulamak", "yasakli_kelimeler": ["trailer", "tanıtım videosu", "2 dakika", "merak uyandırma", "kurgu"], "zorluk": "orta"},
    {"kelime": "bağımsız film çekmek", "aciklama": "büyük stüdyolara bağlı olmadan düşük bütçeyle sanat filmi üretmek", "yasakli_kelimeler": ["indie", "düşük bütçe", "sanat filmi", "festival", "stüdyosuz"], "zorluk": "orta"},
    {"kelime": "cameo rol almak", "aciklama": "ünlü bir yönetmenin veya yıldızın filmde birkaç saniye görünmesi", "yasakli_kelimeler": ["kısa görünme", "hitchcock", "sürpriz oyuncu", "birkaç saniye", "konuk"], "zorluk": "orta"},
    {"kelime": "flashback yapmak", "aciklama": "ana hikayeden geriye gidip karakterin geçmişte yaşadığı bir olayı göstermek", "yasakli_kelimeler": ["geçmişe dönüş", "hatıra", "zaman atlaması", "çocukluk", "geri gitme"], "zorluk": "orta"},
    {"kelime": "post-prodüksiyon yürütmek", "aciklama": "çekimler bittikten sonra kurgu, efekt, ses ve renk işlemlerini tamamlamak", "yasakli_kelimeler": ["çekim sonrası", "kurgu efekt", "ses miksajı", "montaj odası", "tamamlama"], "zorluk": "orta"},
    {"kelime": "plato kiralamak", "aciklama": "kapalı stüdyo alanında hastane veya mahkeme dekoru kurup çekim yapmak", "yasakli_kelimeler": ["stüdyo", "dekor", "kapalı alan", "film platosu", "set"], "zorluk": "orta"},
    {"kelime": "dolly kaydırmak", "aciklama": "tekerlekli ray üzerinde kamerayı oyuncuya doğru akıcı şekilde yaklaştırmak", "yasakli_kelimeler": ["kamera rayı", "tekerlekli araba", "kaydırma", "akıcı hareket", "şaryo"], "zorluk": "orta"},
    {"kelime": "steadicam taşımak", "aciklama": "gövdeye bağlanan ağırlıklı jiro mekanizmasıyla sarsıntısız yürüyüş çekimi yapmak", "yasakli_kelimeler": ["gövde aparatı", "sarsıntısız", "operatör", "yürüyüş", "jiroskop"], "zorluk": "orta"},
    {"kelime": "boom mikrofon tutmak", "aciklama": "uzun sopanın ucundaki mikrofonu oyuncuların tepesinde çerçeve dışı tutmak", "yasakli_kelimeler": ["uzun sopa", "ses operatörü", "rüzgarlık", "çerçeve üstü", "diyalog sesi"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "plan sekans çekmek", "aciklama": "tüm sahneyi hiç kesme ve montaj yapmadan tek bir kesintisiz uzun çekimde bitirmek", "yasakli_kelimeler": ["kesintisiz çekim", "tek plan", "montajsız", "birdman", "uzun plan"], "zorluk": "zor"},
    {"kelime": "dutch angle yatırmak", "aciklama": "kamerayı yana eğerek ufuk çizgisini yamultup psikolojik tekinsizlik ve gerilim yaratmak", "yasakli_kelimeler": ["eğik açı", "yamuk ufuk", "tekinsizlik", "gerilim açısı", "alman dışavurumculuğu"], "zorluk": "zor"},
    {"kelime": "dolly zoom patlatmak", "aciklama": "kamera ileri kayarken aynı anda geriye zoom yaparak arka planı deforme eden vertigo efekti", "yasakli_kelimeler": ["vertigo efekti", "hitchcock", "zıt zoom", "perspektif bozulması", "arka plan uzaması"], "zorluk": "zor"},
    {"kelime": "kuvvetli mise-en-scène kurmak", "aciklama": "çerçevenin içindeki dekor, ışık, kostüm ve oyuncu yerleşiminin bütünü", "yasakli_kelimeler": ["mizanpaj", "çerçeve içi düzen", "sahne tasarımı", "yerleşim sanatı", "yönetmenlik vizyonu"], "zorluk": "zor"},
    {"kelime": "diegetik sesi ayırmak", "aciklama": "film evrenindeki karakterlerin duyduğu radyo veya silah seslerini dış müzikten ayırmak", "yasakli_kelimeler": ["hikaye içi ses", "karakterin duyduğu", "diegetic", "film müziği zıttı", "kaynak ses"], "zorluk": "zor"},
    {"kelime": "kuleshov etkisi kurgulamak", "aciklama": "aynı ifadesiz yüz planının ardından çorba veya tabut göstererek seyircide anlam üretmek", "yasakli_kelimeler": ["montaj etkisi", "sovyet montajı", "anlam inşası", "ifadesiz yüz", "ardışık plan"], "zorluk": "zor"},
    {"kelime": "macguffin peşine düşmek", "aciklama": "karakterleri peşinden koşturan ama filmin derin anlamı için önemsiz olan gizemli nesne", "yasakli_kelimeler": ["hitchcock hilesi", "gizemli nesne", "olay tetikleyici", "önemsiz çanta", "ipucu"], "zorluk": "zor"},
    {"kelime": "jump cut sıçraması yapmak", "aciklama": "aynı açıda zamanı bilerek sıçratıp kesintili ve tedirgin edici kurgu dili kurmak", "yasakli_kelimeler": ["zaman sıçraması", "godard", "fransız yeni dalga", "kesik kurgu", "süreklilik kırılması"], "zorluk": "zor"},
    {"kelime": "180 derece kuralını korumak", "aciklama": "karakterlerin bakış yönlerinin karışmaması için hayali eylem çizgisinin diğer tarafına geçmemek", "yasakli_kelimeler": ["eylem çizgisi", "bakış yönü", "aks atlamama", "kamera yerleşimi", "mekan sürekliliği"], "zorluk": "zor"},
    {"kelime": "foley sanatçılığı icra etmek", "aciklama": "stüdyoda lahana sıkarak kemik kırılması veya çakılla adım sesi üretmek", "yasakli_kelimeler": ["stüdyo ses efekti", "organik ses", "adım sesi", "canlı efekt", "nesne kullanımı"], "zorluk": "zor"},
    {"kelime": "derin odak tekniği kullanmak", "aciklama": "orson welles gibi ön plandaki nesne ile en arkadaki duvarı aynı anda jilet gibi net çekmek", "yasakli_kelimeler": ["deep focus", "citizen kane", "geniş diyafram", "tüm alan net", "alan derinliği"], "zorluk": "zor"},
    {"kelime": "anamorfik lensle sıkıştırmak", "aciklama": "geniş sinemaskop görüntüyü sensöre optik olarak sıkıştırıp oval bokehler elde etmek", "yasakli_kelimeler": ["cinemascope", "oval bokeh", "lens flare", "optik sıkıştırma", "2.39:1"], "zorluk": "zor"},
    {"kelime": "otör sineması üretmek", "aciklama": "filmin her karesine yönetmenin özgün kişisel felsefesini ve imzasını nakşetmek", "yasakli_kelimeler": ["auteur", "yazar yönetmen", "tarkovski", "kişisel imza", "sanat sineması"], "zorluk": "zor"},
    {"kelime": "açı karşı açı çekmek", "aciklama": "karşılıklı konuşan iki karakteri omuz üstünden sırayla çerçeveleyip montajda bağlamak", "yasakli_kelimeler": ["shot reverse shot", "omuz üstü", "diyalog planı", "karşılıklı çekim", "kesme"], "zorluk": "zor"}
]

if __name__ == "__main__":
    add_and_save_verbs("siber", siber_verbs)
    add_and_save_verbs("sinema", sinema_verbs)
