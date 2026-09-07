# -*- coding: utf-8 -*-
import json
import os
import sys
import glob

def validate_file(path, expected_category, expected_count=None):
    if not os.path.exists(path):
        return False, f"Dosya bulunamadı: {path}"
    
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        return False, f"JSON geçersiz: {e}"
    
    if not isinstance(data, list):
        return False, "Kök eleman bir liste değil"
    
    if expected_count is not None and len(data) != expected_count:
        return False, f"Kart sayısı {expected_count} değil, {len(data)} bulundu"
    
    seen_ids = set()
    seen_words = set()
    
    for idx, card in enumerate(data, start=1):
        if not isinstance(card, dict):
            return False, f"Kart {idx} bir sözlük değil"
        
        for field in ["id", "kategori", "kelime", "aciklama", "yasakli_kelimeler", "zorluk"]:
            if field not in card:
                return False, f"Kart {idx} içinde eksik alan: {field}"
        
        cid = card["id"]
        if cid != idx:
            return False, f"Kart {idx} id'si {cid} (beklenen: {idx})"
        if cid in seen_ids:
            return False, f"Kart {idx} id tekrarı: {cid}"
        seen_ids.add(cid)
        
        cat = card["kategori"]
        if cat != expected_category:
            return False, f"Kart {idx} kategori '{cat}' bekleniyordu: '{expected_category}'"
        
        word = card["kelime"]
        if not isinstance(word, str) or not word.strip():
            return False, f"Kart {idx} kelime boş veya geçersiz"
        
        if word.strip() != word.lower():
            return False, f"Kart {idx} kelime küçük harf değil: '{word}'"
        
        norm_word = word.strip()
        if norm_word in seen_words:
            return False, f"Kart {idx} kelime tekrarı: '{norm_word}'"
        seen_words.add(norm_word)
        
        desc = card["aciklama"]
        if not isinstance(desc, str) or not desc.strip():
            return False, f"Kart {idx} açıklama boş veya geçersiz"
        if desc.strip() != desc.lower():
            return False, f"Kart {idx} açıklama küçük harf değil: '{desc}'"
        
        banned = card["yasakli_kelimeler"]
        if not isinstance(banned, list) or len(banned) != 5:
            return False, f"Kart {idx} yasaklı kelimeler 5 adet değil: {len(banned) if isinstance(banned, list) else banned}"
        
        for b in banned:
            if not isinstance(b, str) or not b.strip():
                return False, f"Kart {idx} yasaklı kelime geçersiz: '{b}'"
            if b.strip() != b.lower():
                return False, f"Kart {idx} yasaklı kelime küçük harf değil: '{b}'"
                
        diff = card["zorluk"]
        if diff not in ["kolay", "orta", "zor"]:
            return False, f"Kart {idx} geçersiz zorluk: {diff}"

    return True, f"Başarılı! {len(data)} kart doğrulandı, 0 tekrar, format ve küçük harf tam uyumlu."

if __name__ == "__main__":
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    all_ok = True
    files = sorted(glob.glob(os.path.join(base_dir, "*.json")))
    print(f"Toplam doğrulanacak dosya: {len(files)}")
    total_card_count = 0
    for fpath in files:
        cat = os.path.splitext(os.path.basename(fpath))[0]
        ok, msg = validate_file(fpath, cat)
        if not ok:
            print(f"[{cat}] -> {msg}")
            all_ok = False
        else:
            with open(fpath, "r", encoding="utf-8") as f:
                d = json.load(f)
                total_card_count += len(d)
    audit_path = os.path.join(os.path.dirname(base_dir), "audit", "cleanup-2026-09-07.json")
    if os.path.exists(audit_path):
        with open(audit_path, encoding="utf-8") as f:
            actions = json.load(f)["actions"]
        current = {}
        for action in actions:
            filename = action["file"]
            if filename not in current:
                with open(os.path.join(base_dir, filename), encoding="utf-8") as f:
                    current[filename] = {card["kelime"] for card in json.load(f)}
            rejected = action["before"]["kelime"]
            if rejected != action["replacement"] and rejected in current[filename]:
                print(f"[{filename}] Reddedilen eski hedef yeniden eklendi: {rejected}")
                all_ok = False
    if not all_ok:
        print("Doğrulama başarısız!")
        sys.exit(1)
    print(f"Tebrikler! Tüm {len(files)} dosya ({total_card_count:,} kart) başarıyla doğrulandı.")
