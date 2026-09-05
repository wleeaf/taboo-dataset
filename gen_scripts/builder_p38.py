# -*- coding: utf-8 -*-
from card_utils import add_and_save_verbs

psikiyatri_verbs = [
    # Kolay (12)
    {"kelime": "tedavi etmek", "aciklama": "ruhsal bozukluğu olan hastayı ilaç ve terapiyle iyileştirmek", "yasakli_kelimeler": ["doktor", "hasta", "iyileşme", "ilaç", "ruhsal"], "zorluk": "kolay"},
    {"kelime": "ilaç yazmak", "aciklama": "hastanın durumuna göre antidepresan veya sakinleştirici reçete etmek", "yasakli_kelimeler": ["reçete", "antidepresan", "doktor", "hap", "yazmak"], "zorluk": "kolay"},
    {"kelime": "dinlemek", "aciklama": "hastanın anlattığı sıkıntıları, travmaları ve duyguları not alarak dinlemek", "yasakli_kelimeler": ["anlatılan", "not almak", "seans", "kulak", "hasta"], "zorluk": "kolay"},
    {"kelime": "teşhis koymak", "aciklama": "hastanın şikayetlerine göre bipolar veya şizofreni tanısı vermek", "yasakli_kelimeler": ["tanı", "rapor", "belirti", "hastalık", "koymak"], "zorluk": "kolay"},
    {"kelime": "sakinleştirmek", "aciklama": "kriz anındaki hastayı konuşarak veya acil iğneyle yatıştırmak", "yasakli_kelimeler": ["kriz", "yatıştırmak", "panik", "iğne", "huzur"], "zorluk": "kolay"},
    {"kelime": "hastaneye yatırmak", "aciklama": "kendine zarar verme riski olan hastayı psikiyatri servisine almak", "yasakli_kelimeler": ["servis", "klinik", "zarar", "yatış", "gözetim"], "zorluk": "kolay"},
    {"kelime": "taburcu etmek", "aciklama": "tedavisi tamamlanan ve iyileşen hastayı evine göndermek", "yasakli_kelimeler": ["ev", "çıkış", "iyileşme", "hastane", "göndermek"], "zorluk": "kolay"},
    {"kelime": "muayene etmek", "aciklama": "hastanın duygu durumunu, düşünce içeriğini ve konuşmasını değerlendirmek", "yasakli_kelimeler": ["görüşme", "ruh hali", "değerlendirme", "doktor", "klinik"], "zorluk": "kolay"},
    {"kelime": "rapor hazırlamak", "aciklama": "hastanın akıl sağlığı durumunu resmi heyet raporuna dökmek", "yasakli_kelimeler": ["heyet", "akıl sağlığı", "resmi", "belge", "yazmak"], "zorluk": "kolay"},
    {"kelime": "korkmak", "aciklama": "fobi veya anksiyete sebebiyle aşırı panik ve dehşet hissetmek", "yasakli_kelimeler": ["fobi", "panik", "dehşet", "anksiyete", "ürkeklik"], "zorluk": "kolay"},
    {"kelime": "üzülmek", "aciklama": "derin keder ve mutsuzluk haliyle depresif duygulara kapılmak", "yasakli_kelimeler": ["keder", "mutsuzluk", "depresyon", "ağlamak", "moral"], "zorluk": "kolay"},
    {"kelime": "iyileşmek", "aciklama": "düzenli tedavi ve terapiyle ruhsal dengenin yeniden kurulması", "yasakli_kelimeler": ["düzelme", "denge", "sağlık", "normale dönme", "tedavi"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "panik atak geçirmek", "aciklama": "kalp çarpıntısı ve ölüm korkusuyla aniden gelen yoğun anksiyete krizi", "yasakli_kelimeler": ["çarpıntı", "ölüm korkusu", "nefes darlığı", "kriz", "terleme"], "zorluk": "orta"},
    {"kelime": "manik atağa girmek", "aciklama": "bipolar hastanın aşırı neşe, uyumama ve sınırsız para harcama evresi", "yasakli_kelimeler": ["bipolar", "aşırı coşku", "uykusuzluk", "harcama", "uçuşma"], "zorluk": "orta"},
    {"kelime": "depresyona girmek", "aciklama": "hiçbir şeyden zevk alamama, yataktan çıkamama ve tükenmişlik yaşamak", "yasakli_kelimeler": ["anhedoni", "çöküntü", "zevk alamama", "karamsarlık", "isteksizlik"], "zorluk": "orta"},
    {"kelime": "sanrı üretmek", "aciklama": "takip edildiğine veya peygamber olduğuna dair sarsılmaz yanlış inanç beslemek", "yasakli_kelimeler": ["hezeyan", "delüzyon", "yanlış inanç", "şüphe", "paranoya"], "zorluk": "orta"},
    {"kelime": "işitsel halüsinasyon duymak", "aciklama": "dışarıda kimse yokken kulağa gaipten emir veren sesler gelmesi", "yasakli_kelimeler": ["ses duyma", "gaipten", "emir", "şizofreni", "olmayan ses"], "zorluk": "orta"},
    {"kelime": "obsesyon geliştirmek", "aciklama": "zihne istemsizce takılan mikrop kapma veya kapı kilitleme takıntısı", "yasakli_kelimeler": ["takıntı", "okb", "mikrop", "kilit", "vesvese"], "zorluk": "orta"},
    {"kelime": "kompulsiyon yapmak", "aciklama": "takıntıyı rahatlatmak için elli defa el yıkama veya sayı sayma eylemi", "yasakli_kelimeler": ["el yıkama", "ritüel", "tekrarlayan eylem", "okb", "rahatlama"], "zorluk": "orta"},
    {"kelime": "duygu durum regüle etmek", "aciklama": "lityum veya valproat gibi ilaçlarla aşırı uç duygu dalgalanmalarını dengelemek", "yasakli_kelimeler": ["lityum", "dengeleyici", "duygudurum", "bipolar", "dalgalanma"], "zorluk": "orta"},
    {"kelime": "doz ayarlamak", "aciklama": "hastanın yanıtına ve yan etkilerine göre ilacın miligramını kademeli artırmak", "yasakli_kelimeler": ["miligram", "titrasyon", "yan etki", "artırma", "ilaç"], "zorluk": "orta"},
    {"kelime": "ilaç bağımlılığı oluşmak", "aciklama": "benzodiazepin grubu yatıştırıcıların uzun kullanımda yoksunluk yapması", "yasakli_kelimeler": ["tolerans", "yoksunluk", "bağımlılık", "yeşil reçete", "bırakamama"], "zorluk": "orta"},
    {"kelime": "antipsikotik başlamak", "aciklama": "şizofreni veya psikoz atağında dopamin bloker ilaç tedavisi uygulamak", "yasakli_kelimeler": ["dopamin", "psikoz", "şizofreni", "ilaç", "haloperidol"], "zorluk": "orta"},
    {"kelime": "gözlem odasına almak", "aciklama": "ajitasyonu yüksek hastayı yumuşak duvarlı izolasyon odasında takip etmek", "yasakli_kelimeler": ["izolasyon", "ajitasyon", "yumuşak oda", "güvenlik", "takip"], "zorluk": "orta"},
    {"kelime": "ekt uygulamak", "aciklama": "anestezi altında beyne kısa süreli elektrik akımı verilerek nöbet oluşturulması", "yasakli_kelimeler": ["şok tedavisi", "elektroşok", "anestezi", "dirençli depresyon", "elektrik"], "zorluk": "orta"},
    {"kelime": "tms seansı yapmak", "aciklama": "kafa derisi üzerine manyetik bobin tutarak beyin kabuğunu uyarmak", "yasakli_kelimeler": ["manyetik uyarım", "transkraniyal", "bobin", "korteks", "tedavi"], "zorluk": "orta"},
    {"kelime": "anksiyolitik vermek", "aciklama": "yoğun kaygı ve gerginliği kırmak için hastaya hızlı etkili sakinleştirici vermek", "yasakli_kelimeler": ["kaygı giderici", "gerginlik", "yeşil reçete", "diazem", "sakinleştirici"], "zorluk": "orta"},
    {"kelime": "deliryuma girmek", "aciklama": "enfeksiyon veya ameliyat sonrası yaşlı hastada gelişen anlık kafa karışıklığı ve şuur bulanıklığı", "yasakli_kelimeler": ["şuur bulanıklığı", "kafa karışıklığı", "yaşlı", "yoğun bakım", "dalgalı"], "zorluk": "orta"},
    {"kelime": "somatize etmek", "aciklama": "bastırılmış psikolojik acının bedensel ağrı veya mide kramplarına dönüşmesi", "yasakli_kelimeler": ["bedenselleştirme", "fiziksel ağrı", "mide krampı", "organik sebepsiz", "psikosomatik"], "zorluk": "orta"},
    {"kelime": "dissosiyasyon yaşamak", "aciklama": "travma anında zihnin bedenden veya gerçeklikten kopup yabancılaşması", "yasakli_kelimeler": ["gerçeklikten kopma", "kopuş", "depersonalizasyon", "travma", "yabancılaşma"], "zorluk": "orta"},
    {"kelime": "katatonik kalmak", "aciklama": "hastanın saatlerce tek bir heykel pozisyonunda kaskatı durup konuşmaması", "yasakli_kelimeler": ["heykel gibi", "balmumu esnekliği", "kaskatı", "mutizm", "hareketsizlik"], "zorluk": "orta"},
    {"kelime": "intihar riski değerlendirmek", "aciklama": "hastanın hayatına son verme düşünce ve planlarını ciddiyetle sorgulamak", "yasakli_kelimeler": ["suisid", "özkıyım", "plan", "ölüm düşüncesi", "risk skalası"], "zorluk": "orta"},
    {"kelime": "alkol yoksunluğu yaşamak", "aciklama": "alkolü aniden kesen kişide titreme, terleme ve deliryum tremens başlaması", "yasakli_kelimeler": ["delirium tremens", "titreme", "yoksunluk krizi", "terleme", "alkol kesme"], "zorluk": "orta"},
    {"kelime": "ajitasyon sergilemek", "aciklama": "hastanın kontrolsüz şekilde huzursuzca dolanıp bağırması ve hırçınlaşması", "yasakli_kelimeler": ["huzursuzluk", "hırçınlık", "bağırma", "yerinde duramama", "saldırganlık"], "zorluk": "orta"},
    {"kelime": "fobik kaçınma göstermek", "aciklama": "korkulan asansör, uçak veya açık alandan ısrarla uzak durmak", "yasakli_kelimeler": ["kaçınma", "asansör", "agorafobi", "klostrofobi", "uzak durma"], "zorluk": "orta"},
    {"kelime": "yas sürecini tamamlamak", "aciklama": "kayıp sonrası yaşanan inkar, öfke ve pazarlık evrelerini geçip kabullenmek", "yasakli_kelimeler": ["kübler-ross", "inkar öfke", "kayıp", "kabullenme", "taziye"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "dsm-5 kriterlerini eşleştirmek", "aciklama": "hastanın belirti süresini ve sayısını tanısal kılavuzdaki kodlarla doğrulamak", "yasakli_kelimeler": ["dsm", "tanı kılavuzu", "amerikan psikiyatri", "kod", "semptom sayısı"], "zorluk": "zor"},
    {"kelime": "akatizi yaşamak", "aciklama": "antipsikotik ilaç yan etkisi olarak bacaklarda dayanılmaz yerinde duramama motor huzursuzluğu", "yasakli_kelimeler": ["yerinde duramama", "ekstrapiramidal", "motor huzursuzluk", "yan etki", "bacak kıpırtısı"], "zorluk": "zor"},
    {"kelime": "tardif diskinezi gelişmek", "aciklama": "yıllarca ilaç kullanan hastanın ağız, dil ve dudaklarında kalıcı istemsiz çiğneme hareketleri", "yasakli_kelimeler": ["kalıcı yan etki", "ağız şapırdatma", "dil çıkarma", "istemsiz hareket", "dopamin aşırı duyarlılığı"], "zorluk": "zor"},
    {"kelime": "kurşun boru rijiditesi", "aciklama": "nöroleptik yan etkisi sonucu kolların bükülürken kurşun boru gibi direnç göstermesi", "yasakli_kelimeler": ["kas sertliği", "rijidite", "ilaç reaksiyonu", "katılık", "ekstrapiramidal"], "zorluk": "zor"},
    {"kelime": "serotonin sendromuna girmek", "aciklama": "aşırı serotonin artışıyla klonus, titreme, ishal ve otonomik dengesizlik krizi", "yasakli_kelimeler": ["klonus", "hipertermi", "aşırı serotonin", "ilaç etkileşimi", "toksisite"], "zorluk": "zor"},
    {"kelime": "klo素apini kan sayımıyla izlemek", "aciklama": "tedaviye dirençli şizofrenide kullanılan ilacın agranülositoz yapmaması için haftalık lökosit bakmak", "yasakli_kelimeler": ["agranülositoz", "lökosit", "dirençli şizofreni", "kan sayımı", "klozapin"], "zorluk": "zor"},
    {"kelime": "capgras hezeyanı sergilemek", "aciklama": "hastanın en yakınlarının yerine benzer kopyalarının veya dublörlerinin geçtiğine inanması", "yasakli_kelimeler": ["dublör", "kopya insan", "sahtekar sanma", "tanıma kusuru", "nadir hezeyan"], "zorluk": "zor"},
    {"kelime": "cotard sendromu yaşamak", "aciklama": "hastanın kendi iç organlarının çürüdüğünü veya bizzat kendisinin öldüğünü iddia etmesi", "yasakli_kelimeler": ["yürüyen ceset", "organ çürümesi", "ölüyüm sanma", "nihilistik hezeyan", "ağır depresyon"], "zorluk": "zor"},
    {"kelime": "fregoli yanılsaması yaşamak", "aciklama": "farklı yabancı insanların aslında kılık değiştirmiş tek bir düşman kişi olduğunu sanmak", "yasakli_kelimeler": ["kılık değiştirme", "tek kişi sanma", "paranoid", "özdeşleştirme", "sanrı"], "zorluk": "zor"},
    {"kelime": "münchausen sendromu taklit etmek", "aciklama": "hastane ilgisi ve şefkat görmek için kasten yapay hastalık belirtileri uydurmak", "yasakli_kelimeler": ["yapay bozukluk", "hastalık taklidi", "ilgi görme", "gereksiz ameliyat", "kurgu"], "zorluk": "zor"},
    {"kelime": "panik krizinde hiperventilasyon", "aciklama": "hızlı nefes alıp vermeyle kanda co2 düşüşü ve solunumsal alkalozla tetani oluşması", "yasakli_kelimeler": ["solunumsal alkaloz", "hızlı soluma", "karbondioksit düşmesi", "elde kasılma", "kese kağıdı"], "zorluk": "zor"},
    {"kelime": "ganser sendromu yanıtları vermek", "aciklama": "hastanın en basit sorulara bile yaklaşık ama saçma cevaplar verip delilik taklidi yapması", "yasakli_kelimeler": ["yaklaşık cevap", "saçma yanıt", "cezaevi psikozu", "taklit", "bilinçli bilgisizlik"], "zorluk": "zor"},
    {"kelime": "törel bipolar siklus yaşamak", "aciklama": "yılda dört veya daha fazla manik ya da depresif atakla hızlı döngülü seyretmek", "yasakli_kelimeler": ["hızlı döngü", "rapid cycling", "yılda 4 atak", "tedavi direnci", "bipolar bozukluk"], "zorluk": "zor"},
    {"kelime": "psikiyatrik vasi atanması", "aciklama": "hastanın ayırt etme gücünü yitirdiği gerekçesiyle mahkemece yasal temsilci tayin edilmesi", "yasakli_kelimeler": ["vesayet", "akıl zayıflığı", "hukuki ehliyet", "sulh hukuk", "kısıtlanma"], "zorluk": "zor"}
]

psikoloji_verbs = [
    # Kolay (12)
    {"kelime": "hissetmek", "aciklama": "bireyin iç dünyasında sevinç, hüzün veya kaygı gibi duyguları yaşaması", "yasakli_kelimeler": ["duygu", "iç dünya", "hüzün", "kaygı", "yaşamak"], "zorluk": "kolay"},
    {"kelime": "düşünmek", "aciklama": "zihinde olayları analiz etmek ve fikir yürütmek", "yasakli_kelimeler": ["akıl", "zihin", "fikir", "mantık", "muhakeme"], "zorluk": "kolay"},
    {"kelime": "hatırlamak", "aciklama": "geçmişte yaşanan anıları ve bilgileri hafızadan geri getirmek", "yasakli_kelimeler": ["hafıza", "anı", "geçmiş", "bellek", "canlandırmak"], "zorluk": "kolay"},
    {"kelime": "unutmak", "aciklama": "zihindeki anıların veya bilgilerin zamanla silinip kaybolması", "yasakli_kelimeler": ["silinmek", "hafıza", "akıldan çıkmak", "hatırlamamak", "zaman"], "zorluk": "kolay"},
    {"kelime": "terapiye gitmek", "aciklama": "ruhsal sorunları çözmek için psikologla seans yapmak", "yasakli_kelimeler": ["psikolog", "seans", "koltuk", "konuşma", "sorun"], "zorluk": "kolay"},
    {"kelime": "rahatlamak", "aciklama": "derin nefes alarak veya gevşeyerek stresi üzeriden atmak", "yasakli_kelimeler": ["gevşemek", "stres", "huzur", "derin nefes", "dinginlik"], "zorluk": "kolay"},
    {"kelime": "bağlanmak", "aciklama": "bir insana veya nesneye güçlü duygusal yakınlık geliştirmek", "yasakli_kelimeler": ["duygusal", "yakınlık", "bağ", "sevgi", "güven"], "zorluk": "kolay"},
    {"kelime": "karar vermek", "aciklama": "seçenekler arasında tartıp en uygun yolu seçmek", "yasakli_kelimeler": ["seçenek", "tercih", "tartmak", "seçim", "irade"], "zorluk": "kolay"},
    {"kelime": "öfkelenmek", "aciklama": "engellenme veya haksızlık karşısında yoğun kızgınlık hissetmek", "yasakli_kelimeler": ["kızgınlık", "sinir", "engellenme", "bağırmak", "tepki"], "zorluk": "kolay"},
    {"kelime": "korkmak", "aciklama": "tehlike algısı karşısında kaçma veya donma dürtüsü yaşamak", "yasakli_kelimeler": ["tehlike", "kaçmak", "ürkmek", "tepki", "panik"], "zorluk": "kolay"},
    {"kelime": "hayal kurmak", "aciklama": "geleceğe veya olmasını istediği şeylere dair zihinde canlandırma yapmak", "yasakli_kelimeler": ["imgelem", "canlandırma", "gelecek", "düş", "zihin"], "zorluk": "kolay"},
    {"kelime": "motive olmak", "aciklama": "bir hedefe ulaşmak için içten gelen istek ve arzu duymak", "yasakli_kelimeler": ["istek", "hedef", "arzu", "itici güç", "azim"], "zorluk": "kolay"},

    # Orta (24)
    {"kelime": "bastırmak", "aciklama": "acı veren duygu ve düşünceleri bilinçaltına itip yok saymak", "yasakli_kelimeler": ["repression", "bilinçaltı", "itme", "acı veren", "unutmaya çalışma"], "zorluk": "orta"},
    {"kelime": "yansıtma yapmak", "aciklama": "kendi kabul edemediği kusurları ve öfkeyi karşı tarafa yüklemek", "yasakli_kelimeler": ["projeksiyon", "suçlama", "kusur", "karşı taraf", "savunma mekanizması"], "zorluk": "orta"},
    {"kelime": "rasyonalize etmek", "aciklama": "yaptığı hatayı veya başarısızlığı mantıklı bahaneler bularak aklamak", "yasakli_kelimeler": ["mantığa büründürme", "bahane", "aklama", "savunma", "kılıf"], "zorluk": "orta"},
    {"kelime": "yüceltmek", "aciklama": "toplumca kabul görmeyen ilkel dürtüleri sanat veya spora kanalize etmek", "yasakli_kelimeler": ["sublimasyon", "sanat", "kanalize etme", "dürtü", "üretkenlik"], "zorluk": "orta"},
    {"kelime": "empati geliştirmek", "aciklama": "başkalarının duygusal durumunu ve hislerini içtenlikle hissedip paylaşmak", "yasakli_kelimeler": ["his paylaşımı", "başkası", "anlayış", "duygu ortaklığı", "özdeşim"], "zorluk": "orta"},
    {"kelime": "farkındalık kazanmak", "aciklama": "mindfulness ile şu anki bedensel duyumları ve hisleri yargısız izlemek", "yasakli_kelimeler": ["mindfulness", "şu an", "yargısız", "izleme", "farkındalık"], "zorluk": "orta"},
    {"kelime": "bilişsel çarpıtma yapmak", "aciklama": "ya hep ya hiç, felaketleştirme veya zihin okuma gibi hatalı düşünce kalıpları", "yasakli_kelimeler": ["felaketleştirme", "zihin okuma", "hatalı düşünce", "ya hep ya hiç", "bdt"], "zorluk": "orta"},
    {"kelime": "içgörü kazanmak", "aciklama": "terapi sürecinde kendi davranışlarının kökenindeki bilinçdışı nedeni kavramak", "yasakli_kelimeler": ["insight", "kavrama", "köken", "kendini tanıma", "fark ediş"], "zorluk": "orta"},
    {"kelime": "çaresizliği kabullenmek", "aciklama": "engeller karşısında pes edip kurtulma imkanı varken dahi denemekten vazgeçmek", "yasakli_kelimeler": ["seligman", "pes etme", "vazgeçme", "denememe", "köpek deneyi"], "zorluk": "orta"},
    {"kelime": "halo etkisi yaratmak", "aciklama": "bir insanın tek bir olumlu özelliğinden dolayı tüm kişiliğini harika sanmak", "yasakli_kelimeler": ["genelleme", "yakışıklılık", "olumlu algı", "önyargı", "hale"], "zorluk": "orta"},
    {"kelime": "bilişsel uyumsuzluk yaşamak", "aciklama": "inançları ile yaptığı davranışlar çelişince derin içsel rahatsızlık duymak", "yasakli_kelimeler": ["festinger", "çelişki", "inanç davranış", "iç çatışma", "uyumsuzluk"], "zorluk": "orta"},
    {"kelime": "sosyal kaytarma yapmak", "aciklama": "grup içinde çalışırken bireysel çabayı fark edilmez diye azaltmak", "yasakli_kelimeler": ["grup çalışması", "tembellik", "çaba azaltma", "sorumluluk dağılması", "ringelmann"], "zorluk": "orta"},
    {"kelime": "seyirci kalma etkisi", "aciklama": "kalabalık sokakta acil durum varken herkesin başkasından beklemesi", "yasakli_kelimeler": ["bystander effect", "sorumluluk yayılması", "kalabalık", "yardım etmeme", "kitty genovese"], "zorluk": "orta"},
    {"kelime": "boyun eğmek", "aciklama": "milgram deneyinde olduğu gibi otorite figürünün emirlerini sorgulamadan uygulamak", "yasakli_kelimeler": ["itaat", "milgram", "otorite", "elektrik şoku", "emir"], "zorluk": "orta"},
    {"kelime": "grup baskısına uymak", "aciklama": "asch deneyindeki gibi çoğunluğun bariz yanlış cevabına uyum sağlamak", "yasakli_kelimeler": ["asch deneyi", "çizgi boyu", "çoğunluk", "konformizm", "sürü psikolojisi"], "zorluk": "orta"},
    {"kelime": "koşullanmak", "aciklama": "pavlov'un köpeği gibi zil sesiyle salya akıtarak klasik şartlanma yaşamak", "yasakli_kelimeler": ["pavlov", "klasik koşullanma", "zil sesi", "salya", "şartlanma"], "zorluk": "orta"},
    {"kelime": "maruz bırakmak", "aciklama": "fobiyi yenmek için korkulan nesneyle güvenli ortamda aşamalı yüzleştirmek", "yasakli_kelimeler": ["yüzleşme", "duyarsızlaştırma", "fobi", "aşamalı", "exposure"], "zorluk": "orta"},
    {"kelime": "öz şefkat göstermek", "aciklama": "hata yaptığında kendini acımasızca eleştirmek yerine bir dost gibi kucaklamak", "yasakli_kelimeler": ["kristin neff", "kendini affetme", "şefkat", "öz eleştiri", "dostça"], "zorluk": "orta"},
    {"kelime": "duygusal zeka kullanmak", "aciklama": "kendi ve başkalarının duygularını doğru tanıyıp ilişkileri ustaca yönetmek", "yasakli_kelimeler": ["eq", "goleman", "duygu yönetimi", "ilişki becerisi", "farkındalık"], "zorluk": "orta"},
    {"kelime": "yas tutmak", "aciklama": "ayrılık veya ölüm sonrası ruhun yaşadığı doğal acı ve keder evresini yaşamak", "yasakli_kelimeler": ["keder", "ayrılık acısı", "vefat", "kayıp", "ağlama"], "zorluk": "orta"},
    {"kelime": "stresle başa çıkmak", "aciklama": "problem odaklı veya duygu odaklı başa çıkma stratejileriyle yükü azaltmak", "yasakli_kelimeler": ["coping", "başa çıkma", "problem çözme", "direnç", "stres yönetimi"], "zorluk": "orta"},
    {"kelime": "travma sonrası büyüme", "aciklama": "büyük felaket ve travmayı atlattıktan sonra psikolojik olarak daha güçlü çıkmak", "yasakli_kelimeler": ["güçlenme", "travma sonrası", "olgunlaşma", "anlam bulma", "dayanıklılık"], "zorluk": "orta"},
    {"kelime": "yılmazlık göstermek", "aciklama": "ağır zorluklar karşısında esneyip kırılmadan hızla toparlanabilme gücü", "yasakli_kelimeler": ["rezilyans", "psikolojik sağlamlık", "toparlanma", "esneklik", "güç"], "zorluk": "orta"},
    {"kelime": "somutlaştırmak", "aciklama": "soyut psikolojik çatışmaları resim, kukla veya metaforlarla görünür kılmak", "yasakli_kelimeler": ["metafor", "soyut somut", "kukla", "resim", "görünür kılma"], "zorluk": "orta"},

    # Zor (14)
    {"kelime": "aktarım geliştirmek", "aciklama": "hastanın geçmişte anne babasına duyduğu öfke veya sevgiyi terapistine yansıtması", "yasakli_kelimeler": ["transfers", "terapist", "ebeveyn bağı", "yansıtma", "psikanaliz"], "zorluk": "zor"},
    {"kelime": "karşı aktarım hissetmek", "aciklama": "terapistin kendi çözülmemiş çocukluk yaralarının hastanın anlattıklarıyla tetiklenmesi", "yasakli_kelimeler": ["countertransference", "terapist hissi", "tetiklenme", "kendi yarası", "süpervizyon"], "zorluk": "zor"},
    {"kelime": "şema kimyası yakalamak", "aciklama": "çocukluktaki duygusal yoksunluk şemasına uyan travmatik partnerlere çekilmek", "yasakli_kelimeler": ["şema terapi", "jeffrey young", "çekim", "travmatik partner", "uyumsuz şema"], "zorluk": "zor"},
    {"kelime": "emdr ile duyarsızlaştırmak", "aciklama": "iki yönlü göz hareketleriyle beynin donmuş travmatik anıyı yeniden işlemesini sağlamak", "yasakli_kelimeler": ["göz hareketleri", "çift yönlü uyarım", "travma işleme", "francine shapiro", "anı duyarsızlaştırma"], "zorluk": "zor"},
    {"kelime": "gestalt döngüsünü kapatmak", "aciklama": "bitirilmemiş geçmiş hesapları boş sandalye tekniğiyle yüzleşip tamamlamak", "yasakli_kelimeler": ["boş sandalye", "tamamlama", "fritz perls", "bitirilmemiş iş", "şimdi ve burada"], "zorluk": "zor"},
    {"kelime": "arşetipleri çözümlemek", "aciklama": "jung'un kolektif bilinçdışındaki gölge, persona, anima ve animus arketiplerini anlamak", "yasakli_kelimeler": ["carl jung", "gölge", "persona", "anima animus", "kolektif bilinçdışı"], "zorluk": "zor"},
    {"kelime": "düşünce defüzyonu yapmak", "aciklama": "kabul ve kararlılık terapisinde zihinden geçen düşüncelerle araya mesafe koyup ayrışmak", "yasakli_kelimeler": ["act", "ayrışma", "düşünce havuzu", "mesafe koyma", "steven hayes"], "zorluk": "zor"},
    {"kelime": "katarsis yaşamak", "aciklama": "bastırılmış yoğun bir duygusal yükün aniden ağlama veya boşalmayla arınması", "yasakli_kelimeler": ["arınma", "duygusal boşalma", "rahatlama", "ağlama krizi", "psikanaliz"], "zorluk": "zor"},
    {"kelime": "kader motifi işletmek", "aciklama": "eric berne'in çocuklukta yazılan bilinçdışı yaşam senaryosunu farkında olmadan oynamak", "yasakli_kelimeler": ["yaşam senaryosu", "transaksiyonel", "kader", "çocukluk kararı", "yazgı"], "zorluk": "zor"},
    {"kelime": "özgecilik paradoksu", "aciklama": "başkasına karşılıksız iyilik yaparken bile biyolojik veya psikolojik tatmin sağlama ikilemi", "yasakli_kelimeler": ["altruizm", "karşılıksız iyilik", "bencil gen", "evrimsel psikoloji", "tatmin"], "zorluk": "zor"},
    {"kelime": "denetim odağını saptamak", "aciklama": "başarı veya başarısızlığı kendi çabasına mı yoksa şans ve kadere mi bağladığını ölçmek", "yasakli_kelimeler": ["rotter", "içsel denetim", "dışsal denetim", "kader şans", "kontrol algısı"], "zorluk": "zor"},
    {"kelime": "akış deneyimi yaşamak", "aciklama": "csikszentmihalyi'nin beceri ve zorluk dengesinde zaman algısını yitirecek kadar odaklanma hali", "yasakli_kelimeler": ["flow", "zaman algısı", "tam odaklanma", "csikszentmihalyi", "kendini unutma"], "zorluk": "zor"},
    {"kelime": "temel yükleme hatası", "aciklama": "başkalarının hatasını kişilik kusuruna, kendi hatasını ise dış şartlara bağlamak", "yasakli_kelimeler": ["yükleme yanlılığı", "kişilik kusuru", "durumsal faktör", "atfetme", "sosyal psikoloji"], "zorluk": "zor"},
    {"kelime": "ego tükenmesi yaşamak", "aciklama": "gün boyu sürekli irade ve kendini tutma sergileyince zihinsel öz denetim gücünün tükenmesi", "yasakli_kelimeler": ["ego depletion", "baumeister", "irade gücü", "öz denetim kaybı", "tükenme"], "zorluk": "zor"}
]

if __name__ == "__main__":
    add_and_save_verbs("psikiyatri", psikiyatri_verbs)
    add_and_save_verbs("psikoloji", psikoloji_verbs)
