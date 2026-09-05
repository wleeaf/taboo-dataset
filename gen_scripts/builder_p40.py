# -*- coding: utf-8 -*-
from card_utils import add_and_save_verbs

robotik_verbs = [
    # Kolay (12)
    {"kelime": "programlamak", "aciklama": "robotun yapacağı hareketleri bilgisayardan kod yazarak belirlemek", "yasakli_kelimeler": ["kod", "yazılım", "bilgisayar", "hareket", "komut"], "zorluk": "kolay"},
    {"kelime": "hareket etmek", "aciklama": "robotun motorları ve tekerlekleriyle bir noktadan diğerine gitmesi", "yasakli_kelimeler": ["motor", "tekerlek", "ilerlemek", "gitmek", "adım"], "zorluk": "kolay"},
    {"kelime": "tutmak", "aciklama": "robotik tutucu el ile masadaki nesneyi kavrayıp tutmak", "yasakli_kelimeler": ["tutucu", "gripper", "kavramak", "el", "nesne"], "zorluk": "kolay"},
    {"kelime": "bırakmak", "aciklama": "tutulan parçayı hedef konuma götürüp elini açarak serbest bırakmak", "yasakli_kelimeler": ["açmak", "serbest", "hedef", "bırakış", "el"], "zorluk": "kolay"},
    {"kelime": "algılamak", "aciklama": "sensörler yardımıyla önündeki engeli veya mesafeyi fark etmek", "yasakli_kelimeler": ["sensör", "engel", "mesafe", "fark etmek", "göz"], "zorluk": "kolay"},
    {"kelime": "montaj yapmak", "aciklama": "fabrikada robot kolun araba parçalarını birbirine vidalaması", "yasakli_kelimeler": ["fabrika", "robot kol", "vida", "parça", "birleştirme"], "zorluk": "kolay"},
    {"kelime": "şarj olmak", "aciklama": "bataryası azalan otonom robotun şarj istasyonuna yanaşıp dolması", "yasakli_kelimeler": ["batarya", "pil", "istasyon", "dolum", "elektrik"], "zorluk": "kolay"},
    {"kelime": "dönmek", "aciklama": "robotun gövdesini veya eklemini sağa sola açısal çevirmesi", "yasakli_kelimeler": ["açı", "sağ sol", "çevirmek", "eklem", "rotasyon"], "zorluk": "kolay"},
    {"kelime": "durmak", "aciklama": "acil durdurma butonuna basılınca veya rota bitince hareketi kesmek", "yasakli_kelimeler": ["acil stop", "buton", "hareketsiz", "kesilmek", "fren"], "zorluk": "kolay"},
    {"kelime": "taramak", "aciklama": "lazer veya kamerayla etraftaki odayı 3 boyutlu taramak", "yasakli_kelimeler": ["lazer", "kamera", "oda", "harita", "çevre"], "zorluk": "kolay"},
    {"kelime": "taşımak", "aciklama": "depoda ağır yük paletlerini otonom araçla raflara götürmek", "yasakli_kelimeler": ["depo", "palet", "yük", "raf", "agv"], "zorluk": "kolay"},
    {"kelime": "öğrenmek", "aciklama": "yapay zeka modeliyle deneme yanılma yaparak yeni görevi kavramak", "yasakli_kelimeler": ["yapay zeka", "pekiştirmeli", "deneme yanılma", "görev", "kavrama"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "haritalama yapmak", "aciklama": "robotun slam algoritmasıyla bilmediği ortamın dijital planını çıkarması", "yasakli_kelimeler": ["slam", "dijital plan", "lidar", "navigasyon", "keşif"], "zorluk": "orta"},
    {"kelime": "engel aşmak", "aciklama": "yolda aniden çıkan bir nesneyi sensörle görüp etrafından dolaşmak", "yasakli_kelimeler": ["kaçınma", "nesne", "dolaşma", "ultrasonik", "rota"], "zorluk": "orta"},
    {"kelime": "ters kinematik çözmek", "aciklama": "robot elinin hedef koordinata ulaşması için eklem açılarının hesaplanması", "yasakli_kelimeler": ["inverse kinematics", "eklem açısı", "koordinat", "matematik", "açı"], "zorluk": "orta"},
    {"kelime": "kalibrasyon yapmak", "aciklama": "robot kolunun sıfır noktasını ve sensör hassasiyetini ayarlamak", "yasakli_kelimeler": ["sıfırlama", "hassasiyet", "ayar", "referans nokta", "hata payı"], "zorluk": "orta"},
    {"kelime": "servo sürmek", "aciklama": "darbe genişlik modülasyonu ile servo motoru istenen dereceye konumlandırmak", "yasakli_kelimeler": ["pwm", "servo", "açısal konum", "motor sürücü", "darbe"], "zorluk": "orta"},
    {"kelime": "lidar ile mesafe ölçmek", "aciklama": "dönen lazer ışınlarının yansıma süresinden milimetrik mesafe bulmak", "yasakli_kelimeler": ["lazer tarayıcı", "nokta bulutu", "uçuş süresi", "yansıma", "milimetre"], "zorluk": "orta"},
    {"kelime": "derinlik kamerası okumak", "aciklama": "rgbd kamerayla piksellerin hem rengini hem de kameraya uzaklığını almak", "yasakli_kelimeler": ["rgb-d", "piksel uzaklığı", "3d kamera", "realsense", "derinlik haritası"], "zorluk": "orta"},
    {"kelime": "hat takip etmek", "aciklama": "fabrika zeminindeki siyah veya manyetik çizgiyi optik sensörle izlemek", "yasakli_kelimeler": ["çizgi izleyen", "optik sensör", "zemin", "manyetik bant", "izleme"], "zorluk": "orta"},
    {"kelime": "rota planlamak", "aciklama": "a* veya rrt algoritmasıyla başlangıçtan hedefe en kısa engelsiz yolu bulmak", "yasakli_kelimeler": ["a star", "yol bulma", "en kısa yol", "algoritma", "graf"], "zorluk": "orta"},
    {"kelime": "nesne tanımak", "aciklama": "görüntü işleme ağıyla konveyör banttaki hatalı vidayı anında tespit etmek", "yasakli_kelimeler": ["yolo", "görüntü işleme", "konveyör", "kamera", "tespit"], "zorluk": "orta"},
    {"kelime": "tork kontrolü yapmak", "aciklama": "robot eklemine binen dönme kuvvetini ölçüp hassas montaj sağlamak", "yasakli_kelimeler": ["dönme kuvveti", "kuvvet sensörü", "nm", "eklem torku", "aşırı yük"], "zorluk": "orta"},
    {"kelime": "enkoder okumak", "aciklama": "motor milindeki optik diskten tekerleğin kaç tur döndüğünü saymak", "yasakli_kelimeler": ["optik disk", "darbe sayısı", "mil", "dönüş turu", "odometri"], "zorluk": "orta"},
    {"kelime": "odometri hesaplamak", "aciklama": "tekerlek dönüş sayısından robotun anlık konum koordinatını tahmin etmek", "yasakli_kelimeler": ["konum tahmini", "tekerlek dönüşü", "ölü hesap", "koordinat", "kayma"], "zorluk": "orta"},
    {"kelime": "pid ayarı çekmek", "aciklama": "oransal, integral ve türev katsayılarıyla motorun hedefe aşma yapmadan durması", "yasakli_kelimeler": ["oransal integral türev", "salınım", "aşma", "kontrol döngüsü", "kazanç"], "zorluk": "orta"},
    {"kelime": "insansı robot yürütmek", "aciklama": "iki bacaklı robotun sıfır moment noktası dengesini koruyarak adım atması", "yasakli_kelimeler": ["bipedal", "insansı", "zmp", "adım atma", "denge"], "zorluk": "orta"},
    {"kelime": "pnömatik piston şişirmek", "aciklama": "basınçlı havayla vakumlu tutucuyu veya itici pistonu ileri fırlatmak", "yasakli_kelimeler": ["basınçlı hava", "kompresör", "valf", "vakum vantuz", "piston"], "zorluk": "orta"},
    {"kelime": "can bus üzerinden haberleşmek", "aciklama": "tüm motor sürücüler ve mikrodenetleyiciler arasında çift telli seri veri akışı", "yasakli_kelimeler": ["canbus", "seri haberleşme", "mikrodenetleyici", "çift tel", "paket"], "zorluk": "orta"},
    {"kelime": "otonom park etmek", "aciklama": "aracın ultrasonik sensörlerle park boşluğunu bulup direksiyonu kendi çevirmesi", "yasakli_kelimeler": ["kendi kendine park", "boşluk algılama", "geri manevra", "ultrasonik", "otonom"], "zorluk": "orta"},
    {"kelime": "teleoperasyon yapmak", "aciklama": "tehlikeli nükleer veya bomba imha robotunu uzaktan kumanda ve kamerayla yönetmek", "yasakli_kelimeler": ["uzaktan kumanda", "bomba imha", "joystick", "kamera ekranı", "manuel kontrol"], "zorluk": "orta"},
    {"kelime": "dronu havada sabitlemek", "aciklama": "dört motorun itiş gücünü gyro sensörüyle eşzamanlı dengeleyip havada asılı kalmak", "yasakli_kelimeler": ["hover", "quadcopter", "jiroskop", "itiş gücü", "havada asılı"], "zorluk": "orta"},
    {"kelime": "mikrodenetleyici flaşlamak", "aciklama": "yazılan c++ gömülü yazılım ikili kodunu stm32 veya arduino'ya yüklemek", "yasakli_kelimeler": ["stm32", "arduino", "gömülü yazılım", "hex kodu", "derleme"], "zorluk": "orta"},
    {"kelime": "cobot ile iş birliği", "aciklama": "güvenlik kafesi olmadan insan işçiyle yan yana temas halinde güvenle çalışmak", "yasakli_kelimeler": ["kolaboratif", "güvenlik kafessiz", "insanla yan yana", "kuvvet sınırlama", "ortak çalışma"], "zorluk": "orta"},
    {"kelime": "nokta bulutu işlemek", "aciklama": "lidardan gelen milyonlarca 3d uzamsal koordinat noktasını filtreleyip yüzey örmek", "yasakli_kelimeler": ["point cloud", "pcl", "3d koordinat", "filtreleme", "yüzey oluşturma"], "zorluk": "orta"},
    {"kelime": "titreşim sönümlemek", "aciklama": "hızlı duruş kalkışlarda robot kolundaki salınımı esnek dinamik modelle sıfırlamak", "yasakli_kelimeler": ["salınım", "sönümleme", "elastikiyet", "esneklik", "hızlı hareket"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "d-h tablosu çıkarmak", "aciklama": "robot kinematik zincirini 4 geometrik parametre ile standart matrise dökmek", "yasakli_kelimeler": ["denavit", "hartenberg", "eklem açısı", "bağlantı mesafesi", "homojen matris"], "zorluk": "zor"},
    {"kelime": "jakobiyen matrisi türetmek", "aciklama": "eklem açısal hızları ile uç tutucu çizgisel ve açısal hızları arasındaki türev bağıntısı", "yasakli_kelimeler": ["hız matrisi", "kısmi türev", "tekillik", "hız dönüşümü", "uç nokta hızı"], "zorluk": "zor"},
    {"kelime": "kinematik tekillikten kaçmak", "aciklama": "robot kolunun eklemleri kilitlenip sonsuz hız veya serbestlik kaybı yaşamasını önlemek", "yasakli_kelimeler": ["singularity", "jakobiyen determinantı sıfır", "kilitlenme", "sonsuz kuvvet", "serbestlik kaybı"], "zorluk": "zor"},
    {"kelime": "durum kestirimi yapmak", "aciklama": "gürültülü sensör verilerinden robotun gerçek konum ve hızını olasılıkla hesaplamak", "yasakli_kelimeler": ["kalman filtresi", "kovaryans", "gürültü", "kestirim", "sensör füzyonu"], "zorluk": "zor"},
    {"kelime": "ros düğümü ayağa kaldırmak", "aciklama": "robot işletim sisteminde yayıncı ve abone yapısında asenkron veri kanalları açmak", "yasakli_kelimeler": ["robot operating system", "publisher subscriber", "topic", "ros2", "middleware"], "zorluk": "zor"},
    {"kelime": "yörünge optimize etmek", "aciklama": "aracın kısıtlar altında maliyet fonksiyonunu minimize eden gelecekteki yolunu bulmak", "yasakli_kelimeler": ["mpc", "yörünge planlama", "maliyet fonksiyonu", "kısıt", "optimizasyon"], "zorluk": "zor"},
    {"kelime": "sıfır moment noktası hesabı", "aciklama": "iki ayaklı robotun devrilmemesi için taban zeminine binen toplam yatay torkun sıfır olduğu nokta", "yasakli_kelimeler": ["zmp", "devrilmeme", "ayak tabanı", "dinamik denge", "honda asimo"], "zorluk": "zor"},
    {"kelime": "empedans kontrolü uygulamak", "aciklama": "robotun dış dünyayla temasında yay-sönümleyici kurgusuyla yumuşak etkileşim sağlamak", "yasakli_kelimeler": ["kuvvet kontrolü", "sanal yay sönüm", "esneklik", "yumuşak temas", "mekanik empedans"], "zorluk": "zor"},
    {"kelime": "pekiştirmeli sim-to-real transferi", "aciklama": "fizik simülasyonunda eğitilen robot yapay zekasını domain randomization ile gerçek robota aktarmak", "yasakli_kelimeler": ["simülasyondan gerçeğe", "reinforcement learning", "isaac gym", "domain randomization", "politika transferi"], "zorluk": "zor"},
    {"kelime": "görsel odometri yürütmek", "aciklama": "ardışık kamera karelerindeki optik akış ve özellik noktası eşleşmelerinden konum çıkarmak", "yasakli_kelimeler": ["visual odometry", "orb slam", "özellik noktaları", "kamera karesi", "epipolar geometri"], "zorluk": "zor"},
    {"kelime": "haptik geribildirim iletmek", "aciklama": "cerrahın robot konsolunda dokunduğu dokunun sertliğini elindeki kumandaya kuvvetle hissettirmek", "yasakli_kelimeler": ["da vinci cerrahi", "kuvvet hissi", "dokunsal", "dokunma duyusu", "konsol"], "zorluk": "zor"},
    {"kelime": "urdf dosyası ayrıştırmak", "aciklama": "robotun eklem, bağlantı ve eylemsizlik kütle modellerini xml formatında tanımlamak", "yasakli_kelimeler": ["unified robot description", "xml formatı", "bağlantı kütlesi", "görsel model", "eklem tipi"], "zorluk": "zor"},
    {"kelime": "swarm robotik koordine etmek", "aciklama": "yüzlerce mikro robotun merkezi lidersiz basit kurallarla karınca gibi koloni hareketi yapması", "yasakli_kelimeler": ["sürü zekası", "koloni", "lidersiz", "kolektif davranış", "mikro robotlar"], "zorluk": "zor"},
    {"kelime": "v-slam ile döngü kapatmak", "aciklama": "daha önce geçtiği bir mekanı görsel olarak tanıyıp tüm harita birikimli kayma hatasını düzeltmek", "yasakli_kelimeler": ["loop closure", "birikimli hata", "harita düzeltme", "görsel tanıma", "optimizasyon"], "zorluk": "zor"}
]

rockmuzik_verbs = [
    # Kolay (12)
    {"kelime": "gitar çalmak", "aciklama": "elektro gitarın tellerine penayla vurarak rock riffleri basmak", "yasakli_kelimeler": ["elektro gitar", "pena", "tel", "amfi", "riff"], "zorluk": "kolay"},
    {"kelime": "davul çalmak", "aciklama": "bagetlerle bateri zillerine ve trampetine tempolu vurmak", "yasakli_kelimeler": ["bateri", "baget", "trampet", "zil", "ritim"], "zorluk": "kolay"},
    {"kelime": "şarkı söylemek", "aciklama": "mikrofon karşısında sert rock ve metal parçalarını seslendirmek", "yasakli_kelimeler": ["vokal", "mikrofon", "sert", "seslendirme", "rocker"], "zorluk": "kolay"},
    {"kelime": "grup kurmak", "aciklama": "gitarist, basçı ve davulcu arkadaşları toplayıp rock grubu oluşturmak", "yasakli_kelimeler": ["rock grubu", "basçı", "davulcu", "ekip", "bir araya gelmek"], "zorluk": "kolay"},
    {"kelime": "prova yapmak", "aciklama": "garajda veya ses yalıtımlı stüdyoda şarkıları tekrar tekrar çalmak", "yasakli_kelimeler": ["stüdyo", "garaj", "tekrar", "hazırlık", "çalmak"], "zorluk": "kolay"},
    {"kelime": "konser vermek", "aciklama": "rock festivalinde binlerce hayrana sahneden canlı çalmak", "yasakli_kelimeler": ["festival", "sahne", "canlı", "hayran", "bilet"], "zorluk": "kolay"},
    {"kelime": "bestelemek", "aciklama": "gitar akorları ve sert ritimlerle yeni rock parçası üretmek", "yasakli_kelimeler": ["beste", "akor", "melodi", "üretmek", "şarkı"], "zorluk": "kolay"},
    {"kelime": "dinlemek", "aciklama": "kulaklıkla son ses elektro gitar soloları ve rock marşları dinlemek", "yasakli_kelimeler": ["son ses", "kulaklık", "solo", "parça", "müzik"], "zorluk": "kolay"},
    {"kelime": "amfiye bağlamak", "aciklama": "elektro gitarın jak kablosunu hoparlörlü ses amfisine takmak", "yasakli_kelimeler": ["jak", "kablo", "amplifikatör", "ses yükseltici", "takmak"], "zorluk": "kolay"},
    {"kelime": "tempo tutmak", "aciklama": "davulun bas vuruşlarına kafayı ve ayakları sallayarak eşlik etmek", "yasakli_kelimeler": ["vuruş", "ayak", "kafa", "eşlik", "bateri"], "zorluk": "kolay"},
    {"kelime": "alkışlamak", "aciklama": "parça bitince seyircilerin ıslık ve alkışlarla sahneyi inletmesi", "yasakli_kelimeler": ["ıslık", "tezahürat", "el çırpmak", "seyirci", "beğeni"], "zorluk": "kolay"},
    {"kelime": "imza atmak", "aciklama": "konser sonrası hayranların tişört ve gitarlarına imza bırakmak", "yasakli_kelimeler": ["kalem", "tişört", "hayran", "gitar", "hatıra"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "headbang yapmak", "aciklama": "şarkının ağır temposunda kafayı ve uzun saçları öne arkaya sertçe sallamak", "yasakli_kelimeler": ["kafa sallamak", "uzun saç", "boyun", "ritim", "sert hareket"], "zorluk": "orta"},
    {"kelime": "distortion açmak", "aciklama": "gitar pedalına basıp temiz sesi sert, kirli ve cızırtılı rock tonuna çevirmek", "yasakli_kelimeler": ["pedal", "kirli ton", "drive", "cızırtı", "sert ses"], "zorluk": "orta"},
    {"kelime": "gitar solosu atmak", "aciklama": "şarkının ortasında gitaristin tek başına yüksek perdelerde hızlı melodi çalması", "yasakli_kelimeler": ["solo", "elektro gitar", "hızlı çalış", "virtüöz", "yüksek perde"], "zorluk": "orta"},
    {"kelime": "akort burgusunu çevirmek", "aciklama": "gitar kafasındaki kulakçıkları sıkarak telleri drop-d veya standart tona çekmek", "yasakli_kelimeler": ["burgu", "drop d", "kulakçık", "tel germe", "tuner"], "zorluk": "orta"},
    {"kelime": "sahneden atlamak", "aciklama": "solistin sahneden kendini seyircilerin kollarının arasına boşluğa bırakması", "yasakli_kelimeler": ["stage diving", "boşluğa atlama", "seyirci üstü", "kalabalık", "havada taşınma"], "zorluk": "orta"},
    {"kelime": "pogo yapmak", "aciklama": "konser alanındaki seyircilerin birbirine omuz atarak zıplayıp itişmesi", "yasakli_kelimeler": ["mosh pit", "omuz atma", "itişme", "zıplama", "kalabalık çemberi"], "zorluk": "orta"},
    {"kelime": "bas yürümek", "aciklama": "4 telli bas gitarla davulun ritmine paralel dolgun alt frekans melodisi çalmak", "yasakli_kelimeler": ["bas gitar", "4 tel", "alt frekans", "groove", "ritim eşliği"], "zorluk": "orta"},
    {"kelime": "pena vuruşu yapmak", "aciklama": "sağ elle tellere yukarıdan aşağıya ve aşağıdan yukarıya seri vuruşlar yapmak", "yasakli_kelimeler": ["alt picking", "sağ el", "telle temas", "hızlı vuruş", "pena"], "zorluk": "orta"},
    {"kelime": "pedala basmak", "aciklama": "şarkının nakaratına girerken ayağıyla wah-wah veya delay efektini devreye sokmak", "yasakli_kelimeler": ["efekt pedalı", "wah wah", "delay", "ayak anahtarı", "ton değişimi"], "zorluk": "orta"},
    {"kelime": "baget fırlatmak", "aciklama": "konser sonunda davulcunun çaldığı tahta bagetleri seyircilere hediye atması", "yasakli_kelimeler": ["bateri çubuğu", "seyirciye hediye", "fırlatma", "konser sonu", "davulcu"], "zorluk": "orta"},
    {"kelime": "enstrüman parçalamak", "aciklama": "konser doruk noktasında gitar veya davulu sahnede kırıp dökmek", "yasakli_kelimeler": ["kırmak", "sahne şovu", "jimi hendrix", "yere vurma", "parçalama"], "zorluk": "orta"},
    {"kelime": "deri ceket giymek", "aciklama": "rock kültürünü yansıtan zımbalı siyah deri montu ve botları kuşanmak", "yasakli_kelimeler": ["siyah deri", "zımba", "rocker tarzı", "bot", "kıyafet"], "zorluk": "orta"},
    {"kelime": "brutal vokal yapmak", "aciklama": "death metalde gırtlağı yırtarcasına derinden gelen hırıltılı böğürme sesi çıkarmak", "yasakli_kelimeler": ["growl", "hırıltı", "death metal", "gırtlak", "böğürme"], "zorluk": "orta"},
    {"kelime": "scream atmak", "aciklama": "şarkının nakaratında tiz ve çığlık formunda yırtıcı sesle bağırmak", "yasakli_kelimeler": ["çığlık", "tiz", "bağırma", "screaming", "metalcore"], "zorluk": "orta"},
    {"kelime": "çift kros basmak", "aciklama": "davulcunun iki ayağıyla çift pedala basarak çok hızlı makineli tüfek ritmi atması", "yasakli_kelimeler": ["twin pedal", "çift pedal", "blast beat", "hızlı vuruş", "davul bas"], "zorluk": "orta"},
    {"kelime": "riffleri dizmek", "aciklama": "parçanın ana omurgasını oluşturan akılda kalıcı sert gitar motifini tekrarlamak", "yasakli_kelimeler": ["gitar motifi", "şarkı omurgası", "power akor", "intro", "tekrar"], "zorluk": "orta"},
    {"kelime": "power akor basmak", "aciklama": "kök ve beşinci sesten oluşan 2 telli sert bas gitar akor kalıbını yürütmek", "yasakli_kelimeler": ["kök beşli", "5li akor", "iki parmak", "sert akor", "bozuk ton"], "zorluk": "orta"},
    {"kelime": "palm mute yapmak", "aciklama": "sağ elin ayasını tellerin köprüsüne hafifçe bastırıp boğuk ve tok ses çıkarmak", "yasakli_kelimeler": ["el ayası", "tel boğma", "tok ses", "susturma", "trash metal"], "zorluk": "orta"},
    {"kelime": "whammy bar çekmek", "aciklama": "gitarın tremolo kolunu aşağı bastırıp dive bomb efektiyle tonu çökertmek", "yasakli_kelimeler": ["tremolo kolu", "dive bomb", "perde düşürme", "kol çekme", "floyd rose"], "zorluk": "orta"},
    {"kelime": "bateri solosu izlemek", "aciklama": "konserin ortasında tüm grubun kenara çekilip davulcunun tek başına şov yapması", "yasakli_kelimeler": ["davul şovu", "zil vuruşları", "hızlı tempo", "tek başına", "baget çevirme"], "zorluk": "orta"},
    {"kelime": "feedback yakalamak", "aciklama": "gitarı amfi hoparlörüne yaklaştırıp sonsuz ötme ve rezonans uğultusu elde etmek", "yasakli_kelimeler": ["amfiye yaklaştırma", "ötme", "uğultu", "akustik geri besleme", "hendrix efekti"], "zorluk": "orta"},
    {"kelime": "turne otobüsünde yaşamak", "aciklama": "şehirler arası konser yolculuklarında grubun otobüsteki yataklarda kalması", "yasakli_kelimeler": ["tour bus", "yolculuk", "otobüs", "şehir şehir", "grup hayatı"], "zorluk": "orta"},
    {"kelime": "garajda çalmak", "aciklama": "henüz meşhur olmadan önce evin garajında komşuları rahatsız ederek prova yapmak", "yasakli_kelimeler": ["garaj rock", "komşu şikayeti", "ilk yıllar", "amatör", "bodrum kat"], "zorluk": "orta"},
    {"kelime": "akustik balad söylemek", "aciklama": "sert albümün arasına duygusal, yavaş ve akustik gitar ağırlıklı aşk şarkısı koymak", "yasakli_kelimeler": ["slow parça", "duygusal", "yavaş şarkı", "balad", "sade gitar"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "sweep picking yapmak", "aciklama": "gitaristin penayı tellerin üzerinden süpürme hareketiyle geçirerek akıl almaz hızlı arpej atması", "yasakli_kelimeler": ["süpürme", "hızlı arpej", "yngwie malmsteen", "neoklasik", "ekonomi picking"], "zorluk": "zor"},
    {"kelime": "tapping tekniği kullanmak", "aciklama": "eddie van halen gibi sağ el parmaklarıyla gitar klavyesindeki perdelere doğrudan vurarak çalmak", "yasakli_kelimeler": ["van halen", "iki el klavye", "perdeye vurma", "çekiçleme", "erruption"], "zorluk": "zor"},
    {"kelime": "pinch harmonic patlatmak", "aciklama": "penanın ucuyla tele vururken başparmağın etini hafifçe değdirip yapay ıslık sesi çıkarmak", "yasakli_kelimeler": ["yapay armonik", "başparmak eti", "çığlık tonu", "zakk wylde", "ıslık sesi"], "zorluk": "zor"},
    {"kelime": "lambalı amfiyi sürmek", "aciklama": "vakum tüplü lambalı amfiyi son ses açıp doğal sıcak analog lamba doyumuna ulaştırmak", "yasakli_kelimeler": ["tüp doyum", "vakum lamba", "sıcak ton", "marshall", "analog amfi"], "zorluk": "zor"},
    {"kelime": "aksak ritim saymak", "aciklama": "progresif rockta dream theater gibi 7/8, 11/8 veya 13/16'lık karmaşık ölçülerde çalmak", "yasakli_kelimeler": ["progresif rock", "7/8", "karmaşık zaman", "ölçü değişimi", "dream theater"], "zorluk": "zor"},
    {"kelime": "floyd rose kilitlemek", "aciklama": "çift kilitli tremolo köprüsünün üst ve alt alyan vidalarını sıkıp akordu sabitlemek", "yasakli_kelimeler": ["çift kilit", "alyan vidası", "akort bozulmaması", "bıçak köprü", "fine tuner"], "zorluk": "zor"},
    {"kelime": "blast beat döşemek", "aciklama": "trampet, zil ve krosu aynı anda aşırı hızlı ve aralıksız vuran ekstrem metal davul kalıbı", "yasakli_kelimeler": ["aşırı hızlı", "ekstrem metal", "aralıksız vuruş", "black metal", "makineli tüfek ritmi"], "zorluk": "zor"},
    {"kelime": "fretless bas perdesiz çalmak", "aciklama": "klavyesinde metal perde telleri olmayan bas gitarda pürüzsüz kaydırmalı bas çalmak", "yasakli_kelimeler": ["perdesiz", "metal çizgisiz", "jaco pastorius", "kontrbas tonu", "mikrotonal kayma"], "zorluk": "zor"},
    {"kelime": "overdrive pedal zinciri kurmak", "aciklama": "pedalboard üzerinde boost, overdrive, fuzz ve modülasyon dizilim sırasını doğru bağlamak", "yasakli_kelimeler": ["pedalboard", "sinyal zinciri", "fuzz", "boost", "true bypass"], "zorluk": "zor"},
    {"kelime": "neoklasik gamları koşmak", "aciklama": "harmonik minör ve eksiltilmiş dizileri barok keman pasajları gibi elektro gitarda dökmek", "yasakli_kelimeler": ["harmonik minör", "eksiltilmiş gam", "barok etki", "hızlı arpej", "malmsteen stili"], "zorluk": "zor"},
    {"kelime": "drop tuning akortlamak", "aciklama": "tüm telleri 1 veya 2 tam ses pesleştirip drop c veya drop a ile karanlık ton yakalamak", "yasakli_kelimeler": ["pes ton", "drop c", "ağır sound", "nu metal", "gevşek tel"], "zorluk": "zor"},
    {"kelime": "progresif konsept albüm örmek", "aciklama": "tüm albümdeki şarkıların tek bir felsefi ve hikayesel temayı işlediği dev eser yazmak", "yasakli_kelimeler": ["konsept albüm", "pink floyd", "the wall", "hikayesel bütünlük", "uzun şarkılar"], "zorluk": "zor"},
    {"kelime": "alt-tuning kurgulamak", "aciklama": "dadgad veya açık g gibi standart dışı deneysel gitar akort düzenlerini denemek", "yasakli_kelimeler": ["dadgad", "açık akort", "deneysel düzen", "led zeppelin", "standart dışı"], "zorluk": "zor"},
    {"kelime": "slap bas tokatlamak", "aciklama": "başparmağın kemiğiyle tele vurup işaret parmağıyla alt teli sertçe koparıp çıtlatmak", "yasakli_kelimeler": ["slap and pop", "başparmak vuruşu", "tel koparma", "flea", "funk rock"], "zorluk": "zor"}
]

if __name__ == "__main__":
    add_and_save_verbs("robotik", robotik_verbs)
    add_and_save_verbs("rockmuzik", rockmuzik_verbs)
