# -*- coding: utf-8 -*-
from card_utils import add_and_save_verbs

data = {}

# 1. aktuerya
data["aktuerya"] = [
    {"kelime": "prim hesaplamak", "aciklama": "sigorta poliçesi için ödenecek risk bedelini belirlemek", "yasakli_kelimeler": ["ücret", "tarife", "maliyet", "tahsilat", "ödeme"], "zorluk": "kolay"},
    {"kelime": "risk ölçmek", "aciklama": "olası tehlike ve hasar olasılıklarını matematiksel olarak belirlemek", "yasakli_kelimeler": ["ihtimal", "analiz", "tahmin", "belirsizlik", "zarar"], "zorluk": "kolay"},
    {"kelime": "tazminat ödemek", "aciklama": "hasara uğrayan sigortalının zararını karşılamak", "yasakli_kelimeler": ["para", "bedel", "mağdur", "şirket", "poliçe"], "zorluk": "kolay"},
    {"kelime": "poliçe düzenlemek", "aciklama": "sigorta sözleşmesi hazırlayıp onaylamak", "yasakli_kelimeler": ["sözleşme", "evrak", "imza", "şartlar", "acente"], "zorluk": "kolay"},
    {"kelime": "hasar tespit etmek", "aciklama": "meydana gelen kaza veya zararın boyutunu belirlemek", "yasakli_kelimeler": ["eksper", "rapor", "inceleme", "kaza", "ziyan"], "zorluk": "kolay"},
    {"kelime": "emeklilik planlamak", "aciklama": "çalışma hayatı sonrası birikim ve maaş projeksiyonu yapmak", "yasakli_kelimeler": ["birikim", "bireysel", "fon", "yaşlılık", "tasarruf"], "zorluk": "kolay"},
    {"kelime": "fon yönetmek", "aciklama": "toplanan prim ve birikimleri karlı finansal araçlarda değerlendirmek", "yasakli_kelimeler": ["portföy", "yatırım", "hisse", "tahvil", "getiri"], "zorluk": "kolay"},
    {"kelime": "teminat vermek", "aciklama": "belli risklere karşı mali güvence sağlamak", "yasakli_kelimeler": ["güvence", "kapsam", "şart", "koruma", "garanti"], "zorluk": "kolay"},
    {"kelime": "sözleşme feshetmek", "aciklama": "yürürlükteki sigorta anlaşmasını tek taraflı veya karşılıklı bitirmek", "yasakli_kelimeler": ["iptal", "sonlandırmak", "hüküm", "cayma", "madde"], "zorluk": "kolay"},
    {"kelime": "katkı payı yatırmak", "aciklama": "bireysel emeklilik hesabına düzenli para aktarmak", "yasakli_kelimeler": ["ödemek", "tutar", "hesap", "birikim", "aylık"], "zorluk": "kolay"},
    {"kelime": "ekspertiz yapmak", "aciklama": "hasarlı malın değerini ve hasar oranını uzman gözüyle incelemek", "yasakli_kelimeler": ["uzman", "oto", "rapor", "değerleme", "inceleme"], "zorluk": "kolay"},
    {"kelime": "kaza bildirmek", "aciklama": "oluşan trafik veya iş kazasını sigortacıya haber vermek", "yasakli_kelimeler": ["ihbar", "tutanak", "beyan", "çağrı merkezi", "olay"], "zorluk": "kolay"},
    {"kelime": "rücu etmek", "aciklama": "ödenen tazminatı kusurlu taraftan geri talep etmek", "yasakli_kelimeler": ["kusur", "tahsil", "geri istemek", "hukuk", "dava"], "zorluk": "orta"},
    {"kelime": "rezerv ayırmak", "aciklama": "ilerideki muhtemel hasar ödemeleri için karşılık fon tutmak", "yasakli_kelimeler": ["karşılık", "muallak", "para", "kenara koymak", "şirket"], "zorluk": "orta"},
    {"kelime": "mortalite hesaplamak", "aciklama": "yaş gruplarına göre ölüm olasılıklarını tablolardan çıkarmak", "yasakli_kelimeler": ["ölüm", "oran", "yaşam süresi", "istatistik", "nüfus"], "zorluk": "orta"},
    {"kelime": "anüite bağlamak", "aciklama": "düzenli aralıklarla yapılacak ömür boyu veya süreli ödeme planı oluşturmak", "yasakli_kelimeler": ["irad", "maaş", "düzenli", "taksit", "gelir"], "zorluk": "orta"},
    {"kelime": "tenzil etmek", "aciklama": "ödenmeyen primler sonucu sigorta bedelini düşürmek", "yasakli_kelimeler": ["indirim", "kesinti", "azaltmak", "poliçe", "bedel"], "zorluk": "orta"},
    {"kelime": "portföy analiz etmek", "aciklama": "şirketin tüm poliçe ve risk dağılımını incelemek", "yasakli_kelimeler": ["dağılım", "çeşitlendirme", "denge", "karlılık", "rapor"], "zorluk": "orta"},
    {"kelime": "iştira etmek", "aciklama": "hayat sigortası poliçesini vadesinden önce paraya çevirip sonlandırmak", "yasakli_kelimeler": ["caymak", "nakit", "erken ayrılma", "kesinti", "bedel"], "zorluk": "orta"},
    {"kelime": "muafiyet uygulamak", "aciklama": "hasarın belli bir kısmını sigortalının üstlenmesini sağlamak", "yasakli_kelimeler": ["katılım", "yüzde", "kesinti", "ödememe", "şart"], "zorluk": "orta"},
    {"kelime": "reasürans yapmak", "aciklama": "büyük riskleri başka sigorta şirketlerine devrederek güvenceye almak", "yasakli_kelimeler": ["devretmek", "mükerrer", "şirket", "bölüşmek", "koruma"], "zorluk": "orta"},
    {"kelime": "beklenen değer bulmak", "aciklama": "olasılık dağılımının matematiksel ortalama sonucunu hesaplamak", "yasakli_kelimeler": ["ortalama", "matematik", "olasılık", "çarpım", "sonuç"], "zorluk": "orta"},
    {"kelime": "iskonto etmek", "aciklama": "gelecekteki nakit akışını bugünkü değere indirgemek", "yasakli_kelimeler": ["faiz", "bugünkü değer", "indirgeme", "nakit akışı", "oran"], "zorluk": "orta"},
    {"kelime": "kümülatif toplamak", "aciklama": "verileri veya hasarları zaman içinde biriktirerek toplamak", "yasakli_kelimeler": ["birikimli", "eklemek", "toplam", "süreç", "artış"], "zorluk": "orta"},
    {"kelime": "koasürans uygulamak", "aciklama": "bir riski birden fazla sigorta şirketine paylaştırmak", "yasakli_kelimeler": ["ortak", "paylaşmak", "şirket", "oran", "bölüşüm"], "zorluk": "orta"},
    {"kelime": "yaşam tablosu kurmak", "aciklama": "nüfusun yaşa göre hayatta kalma ve ölüm oranlarını modellemek", "yasakli_kelimeler": ["mortalite", "sağkalım", "yaş", "istatistik", "grafik"], "zorluk": "orta"},
    {"kelime": "hasar frekansı ölçmek", "aciklama": "belirli dönemdeki hasar sayısının poliçe sayısına oranını bulmak", "yasakli_kelimeler": ["sıklık", "oran", "sayı", "oluşma", "dönem"], "zorluk": "orta"},
    {"kelime": "hasar şiddeti bulmak", "aciklama": "meydana gelen her bir hasarın ortalama parasal tutarını hesaplamak", "yasakli_kelimeler": ["maliyet", "tutar", "ortalama", "büyüklük", "ağırlık"], "zorluk": "orta"},
    {"kelime": "solvans hesaplamak", "aciklama": "şirketin yükümlülüklerini karşılayabilme mali yeterliliğini ölçmek", "yasakli_kelimeler": ["yeterlilik", "sermaye", "karşılama", "mali güç", "denetim"], "zorluk": "orta"},
    {"kelime": "stres testi uygulamak", "aciklama": "şirketin aşırı kriz senaryolarındaki dayanıklılığını denemek", "yasakli_kelimeler": ["kriz", "şok", "senaryo", "dayanıklılık", "simülasyon"], "zorluk": "orta"},
    {"kelime": "muallak hasar belirlemek", "aciklama": "ihbarı yapılmış fakat henüz ödenmemiş hasar tutarını kestirmek", "yasakli_kelimeler": ["ödenmemiş", "bekleyen", "karşılık", "tahmin", "ibraz"], "zorluk": "orta"},
    {"kelime": "sürprim eklemek", "aciklama": "normalden yüksek risk taşıyan sigortalıya ek prim yüklemek", "yasakli_kelimeler": ["ek prim", "yüksek risk", "fiyat artışı", "zam", "eklenti"], "zorluk": "orta"},
    {"kelime": "zeyilname basmak", "aciklama": "mevcut poliçede yapılan değişiklikleri belgelemek", "yasakli_kelimeler": ["ek sözleşme", "güncelleme", "değişiklik", "belge", "madde"], "zorluk": "orta"},
    {"kelime": "aktüeryal kazanç sağlamak", "aciklama": "varsayımlar ile gerçekleşen sonuçlar arasındaki olumlu farkı bulmak", "yasakli_kelimeler": ["varsayım", "fark", "kar", "fon", "bilanço"], "zorluk": "orta"},
    {"kelime": "değerleme yapmak", "aciklama": "gelecek yükümlülüklerin şimdiki değerini aktüeryal formüllerle bulmak", "yasakli_kelimeler": ["kıymet", "hesaplama", "yükümlülük", "bilanço", "oran"], "zorluk": "orta"},
    {"kelime": "ibraname imzalamak", "aciklama": "tazminatı eksiksiz aldığını ve hak talep etmeyeceğini onaylamak", "yasakli_kelimeler": ["feragat", "belge", "aklama", "hak", "borçsuzluk"], "zorluk": "orta"},
    {"kelime": "türev modellemek", "aciklama": "karmaşık sigorta risklerini finansal türev araçlarla modellemek", "yasakli_kelimeler": ["opsiyon", "vadeli", "finans", "matematik", "ürün"], "zorluk": "zor"},
    {"kelime": "stokastik simüle etmek", "aciklama": "rastgele değişkenlerle binlerce farklı piyasa senaryosu üretmek", "yasakli_kelimeler": ["monte carlo", "rastlantısal", "olasılık", "model", "dağılım"], "zorluk": "zor"},
    {"kelime": "kredibilite ağırlıklandırmak", "aciklama": "geçmiş hasar verilerine ne kadar güvenileceğini istatistikle saptamak", "yasakli_kelimeler": ["güvenilirlik", "buhlmann", "ağırlık", "geçmiş", "veri"], "zorluk": "zor"},
    {"kelime": "ibnr hesaplamak", "aciklama": "gerçekleşmiş fakat henüz şirkete ihbar edilmemiş hasarları tahmin etmek", "yasakli_kelimeler": ["ihbarsız", "gecikmeli", "karşılık", "zincir merdiven", "tahmin"], "zorluk": "zor"},
    {"kelime": "zincir merdiven kurmak", "aciklama": "hasar gelişim üçgenlerinden hareketle nihai hasar projeksiyonu yapmak", "yasakli_kelimeler": ["üçgen", "gelişim", "metot", "hasar projeksiyonu", "aktüer"], "zorluk": "zor"},
    {"kelime": "kuyruk riski modellemek", "aciklama": "dağılımın uç noktalarında gerçekleşebilecek dev felaketleri ölçmek", "yasakli_kelimeler": ["uç değer", "ekstrem", "fat tail", "felaket", "olasılık"], "zorluk": "zor"},
    {"kelime": "kopula uydurmak", "aciklama": "bağımlı rastgele değişkenlerin ortak dağılım fonksiyonunu modellemek", "yasakli_kelimeler": ["bağımlılık", "ortak dağılım", "istatistik", "değişken", "fonksiyon"], "zorluk": "zor"},
    {"kelime": "glim tahmin etmek", "aciklama": "genelleştirilmiş lineer modellerle hasar frekans ve şiddetini ayrıştırmak", "yasakli_kelimeler": ["regresyon", "lineer", "poisson", "gamma", "istatistik"], "zorluk": "zor"},
    {"kelime": "rüin olasılığı bulmak", "aciklama": "bir sigorta fonunun iflas etme veya tükenme olasılığını hesaplamak", "yasakli_kelimeler": ["iflas", "tükenme", "sermaye", "fonksiyon", "lundberg"], "zorluk": "zor"},
    {"kelime": "var hesaplamak", "aciklama": "belli güven aralığında karşılaşılabilecek maksimum riske maruz değeri bulmak", "yasakli_kelimeler": ["riske maruz değer", "güven aralığı", "kayıp", "yüzdelik", "sermaye"], "zorluk": "zor"},
    {"kelime": "tvar türetmek", "aciklama": "riske maruz değer aşıldığında beklenen ortalama zararı hesaplamak", "yasakli_kelimeler": ["kuyruk var", "ortalama kayıp", "aşım", "beklenti", "ekstrem"], "zorluk": "zor"},
    {"kelime": "longevite ölçmek", "aciklama": "nüfusun beklenen ömrünün uzamasından kaynaklanan emeklilik maliyet riskini hesaplamak", "yasakli_kelimeler": ["uzun yaşam", "sağkalım", "emeklilik", "yaşlanma", "risk"], "zorluk": "zor"},
    {"kelime": "iskonto eğrisi çizmek", "aciklama": "vadelerine göre faiz ve indirgeme oranlarının grafiğini modellemek", "yasakli_kelimeler": ["getiri eğrisi", "faiz", "vade yapısı", "tahvil", "eğri"], "zorluk": "zor"},
    {"kelime": "solvency 2 uyarlamak", "aciklama": "avrupa birliği sigortacılık risk ve sermaye direktiflerini kuruma entegre etmek", "yasakli_kelimeler": ["avrupa", "direktif", "sermaye gereksinimi", "scr", "denetim"], "zorluk": "zor"}
]

for cat, vcards in data.items():
    add_and_save_verbs(cat, vcards)
