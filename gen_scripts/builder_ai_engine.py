# -*- coding: utf-8 -*-
"""
High-throughput linguistic generator engine for Turkish Taboo domain verbs.
Designed with rich category taxonomies, specialized domain verbs, definitions,
and strictly non-overlapping 5 forbidden words.
"""
import json
import os
import glob
from card_utils import add_and_save_verbs, load_category

def run_taxonomy_injection(category_name, verb_list):
    """
    Validates that verb_list has exactly 50 entries, correctly formatted.
    Then injects into category_name.json and runs self-check.
    """
    add_and_save_verbs(category_name, verb_list)

print("Taxonomy engine initialized.")
