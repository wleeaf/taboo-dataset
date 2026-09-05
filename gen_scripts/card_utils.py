# -*- coding: utf-8 -*-
import json
import os

def load_category(cat_name, data_dir="data"):
    fpath = os.path.join(data_dir, f"{cat_name}.json")
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    cards = data["kartlar"] if isinstance(data, dict) and "kartlar" in data else data
    return cards, fpath

def add_and_save_verbs(cat_name, verb_cards, data_dir="data"):
    """
    verb_cards must be a list of 50 dicts with fields:
    - kelime
    - aciklama
    - yasakli_kelimeler (list of 5)
    - zorluk ('kolay', 'orta', 'zor')
    """
    cards, fpath = load_category(cat_name, data_dir)
    
    existing_words = {c["kelime"].strip().lower() for c in cards}
    
    if len(verb_cards) != 50:
        raise ValueError(f"[{cat_name}] 50 verb cards expected, got {len(verb_cards)}")
    
    new_cards = []
    for i, vc in enumerate(verb_cards):
        w = vc["kelime"].strip().lower()
        if w in existing_words:
            raise ValueError(f"[{cat_name}] Duplicate word already exists in file: {w}")
        existing_words.add(w)
        
        desc = vc["aciklama"].strip().lower()
        banned = [b.strip().lower() for b in vc["yasakli_kelimeler"]]
        if len(banned) != 5:
            raise ValueError(f"[{cat_name}] Card {w} must have exactly 5 banned words, got {len(banned)}")
        
        diff = vc["zorluk"].strip().lower()
        if diff not in ["kolay", "orta", "zor"]:
            raise ValueError(f"[{cat_name}] Card {w} invalid difficulty: {diff}")
        
        new_cards.append({
            "kategori": cat_name,
            "kelime": w,
            "aciklama": desc,
            "yasakli_kelimeler": banned,
            "zorluk": diff
        })
        
    combined = cards + new_cards
    
    for idx, c in enumerate(combined, start=1):
        c["id"] = idx
        c["kategori"] = cat_name
        
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)
        
    print(f"[{cat_name}] Successfully added {len(verb_cards)} verbs. Total cards: {len(combined)}")
