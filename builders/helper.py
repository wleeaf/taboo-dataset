# -*- coding: utf-8 -*-
import json
import glob
import os
import sys

def build_and_validate(category_name, cards):
    if len(cards) != 200:
        raise ValueError(f"Kart sayısı 200 olmalı! Bulunan: {len(cards)}")
    
    # Load all existing words from other json files
    all_other_words = {}
    for f in sorted(glob.glob('data/*.json')):
        cat = os.path.splitext(os.path.basename(f))[0]
        if cat == category_name:
            continue
        for c in json.load(open(f, encoding='utf-8')):
            w = c['kelime'].strip().lower()
            all_other_words[w] = cat

    seen_ids = set()
    seen_words = set()
    json_cards = []

    for idx, card in enumerate(cards, 1):
        if isinstance(card, (list, tuple)):
            cid, kelime, aciklama, yasakli, zorluk = card
        elif isinstance(card, dict):
            cid = card['id']
            kelime = card['kelime']
            aciklama = card['aciklama']
            yasakli = card['yasakli_kelimeler']
            zorluk = card['zorluk']
        else:
            raise ValueError(f"Geçersiz kart formatı #{idx}: {card}")

        if cid != idx:
            raise ValueError(f"Kart #{idx} id uyuşmazlığı: {cid} != {idx}")
        if cid in seen_ids:
            raise ValueError(f"Tekrar eden id #{cid}")
        seen_ids.add(cid)

        kelime_clean = kelime.strip().lower()
        if not kelime_clean:
            raise ValueError(f"Kart #{idx} kelime boş!")
        if kelime_clean in seen_words:
            raise ValueError(f"Kart #{idx} kendi içinde kelime tekrarı: '{kelime_clean}'")
        seen_words.add(kelime_clean)

        if kelime != kelime_clean:
            raise ValueError(f"Kart #{idx} kelime küçük harf değil: '{kelime}'")

        if len(yasakli) != 5:
            raise ValueError(f"Kart #{idx} yasaklı kelime sayısı 5 değil: {len(yasakli)}")

        for b in yasakli:
            b_clean = b.strip().lower()
            if not b_clean:
                raise ValueError(f"Kart #{idx} yasaklı kelime boş!")
            if b != b_clean:
                raise ValueError(f"Kart #{idx} yasaklı kelime küçük harf değil: '{b}'")

        if zorluk not in ["kolay", "orta", "zor"]:
            raise ValueError(f"Kart #{idx} geçersiz zorluk: '{zorluk}'")

        if not aciklama.strip():
            raise ValueError(f"Kart #{idx} açıklama boş!")

        if kelime_clean in all_other_words:
            other_cat = all_other_words[kelime_clean]
            print(f"[UYARI] '{kelime_clean}' daha önce '{other_cat}' kategorisinde kullanılmış!")

        json_cards.append({
            "id": cid,
            "kategori": category_name,
            "kelime": kelime_clean,
            "aciklama": aciklama.strip().lower(),
            "yasakli_kelimeler": [b.strip().lower() for b in yasakli],
            "zorluk": zorluk
        })

    out_path = f"data/{category_name}.json"
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(json_cards, f, ensure_ascii=False, indent=2)

    diff_counts = {"kolay": 0, "orta": 0, "zor": 0}
    for c in json_cards:
        diff_counts[c['zorluk']] += 1

    print(f"✅ {out_path} başarıyla oluşturuldu!")
    print(f"   Kart Sayısı: {len(json_cards)} | Kolay: {diff_counts['kolay']} | Orta: {diff_counts['orta']} | Zor: {diff_counts['zor']}")
    return out_path
