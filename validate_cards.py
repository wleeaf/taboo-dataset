# -*- coding: utf-8 -*-
import json
import os
import sys

CATEGORIES = ["etnografi", "linguistik", "retorik", "pedagoji"]

def validate_file(path, expected_category):
    if not os.path.exists(path):
        return False, f"Dosya bulunamadı: {path}"
    
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        return False, f"JSON geçersiz: {e}"
    
    if not isinstance(data, list):
        return False, "Kök eleman bir liste değil"
    
    if len(data) != 100:
        return False, f"Kart sayısı 100 değil, {len(data)} bulundu"
    
    seen_ids = set()
    seen_words = set()
    
    for idx, card in enumerate(data, start=1):
        if not isinstance(card, dict):
            return False, f"Kart {idx} bir sözlük değil"
        
        for field in ["id", "kategori", "kelime", "aciklama", "yasakli_kelimeler"]:
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
                
    return True, f"Başarılı! {len(data)} kart doğrulandı, 0 tekrar, format ve küçük harf tam uyumlu."

if __name__ == "__main__":
    base_dir = "/home/taceddinsancak/Desktop/Projects/taboo/data"
    all_ok = True
    for cat in CATEGORIES:
        fpath = os.path.join(base_dir, f"{cat}.json")
        ok, msg = validate_file(fpath, cat)
        print(f"[{cat}] -> {msg}")
        if not ok:
            all_ok = False
    if not all_ok:
        sys.exit(1)
