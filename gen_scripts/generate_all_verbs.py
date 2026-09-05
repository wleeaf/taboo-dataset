# -*- coding: utf-8 -*-
"""
Master Verb Generator for 150 Categories (50 distinct verbs per category).
Each card:
- kelime: Authentic 1-2 word verb/verb phrase in Turkish (-mak/-mek or noun+etmek/yapmak/olmak/sürmek/vb.)
- aciklama: Clean Turkish lowercase explanation
- yasakli_kelimeler: Exactly 5 banned words, lowercase, no duplicates, accurate
- zorluk: 'kolay', 'orta', or 'zor'
- All entries lowercase Turkish characters.
"""
import json
import os
import glob
from card_utils import add_and_save_verbs

