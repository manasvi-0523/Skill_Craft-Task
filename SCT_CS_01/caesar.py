"""
cipher.py — Caesar Cipher core logic
SkillCraft Cybersecurity Internship | Task 01
"""

import string
from collections import Counter


# Standard English letter frequency (%)
ENGLISH_FREQ = {
    'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0,
    'N': 6.7, 'S': 6.3, 'H': 6.1, 'R': 6.0, 'D': 4.3,
    'L': 4.0, 'C': 2.8, 'U': 2.8, 'M': 2.4, 'W': 2.4,
    'F': 2.2, 'G': 2.0, 'Y': 2.0, 'P': 1.9, 'B': 1.5,
    'V': 1.0, 'K': 0.8, 'J': 0.2, 'X': 0.2, 'Q': 0.1, 'Z': 0.1
}

# Common English words for word match bonus
COMMON_WORDS = {
    'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i',
    'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at',
    'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she',
    'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what',
    'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me',
    'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take',
    'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other',
    'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also',
    'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way',
    'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us',
    'hello', 'world', 'mr', 'mrs', 'miss', 'yes', 'no', 'please', 'thank', 'thanks'
}


def caesar_shift(text: str, shift: int) -> str:
    """Apply Caesar cipher shift to text. Preserves case, symbols, spaces."""
    shift = shift % 26
    result = []
    for ch in text:
        if ch.isupper():
            result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
        elif ch.islower():
            result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        else:
            result.append(ch)
    return ''.join(result)


def encrypt(text: str, shift: int) -> str:
    """Encrypt plaintext using Caesar cipher."""
    return caesar_shift(text, shift)


def decrypt(text: str, shift: int) -> str:
    """Decrypt ciphertext using Caesar cipher (reverse shift)."""
    return caesar_shift(text, -shift)


def brute_force(ciphertext: str) -> list[dict]:
    """
    Try all 25 possible shifts and return scored candidates.
    Returns list of dicts sorted by English frequency match score.
    """
    results = []
    for shift in range(1, 26):
        candidate = caesar_shift(ciphertext, -shift)
        score = _english_score(candidate)
        results.append({
            'shift': shift,
            'text': candidate,
            'score': round(score, 2),
            'likely': False
        })
    results.sort(key=lambda x: x['score'], reverse=True)
    if results:
        results[0]['likely'] = True
    return results


def _english_score(text: str) -> float:
    """
    Score text by how closely its letter frequencies match English.
    Higher = more likely to be English plaintext.
    Uses chi-squared-style distance (inverted so higher = better).
    Also adds bonus for matching common English words.
    
    Hybrid Score = freq_score + (word_match_bonus × weight)
    """
    letters = [c.upper() for c in text if c.isalpha()]
    if not letters:
        return 0.0
    total = len(letters)
    counts = Counter(letters)
    
    # Frequency-based score (chi-squared distance)
    freq_score = 0.0
    for letter, expected_pct in ENGLISH_FREQ.items():
        observed_pct = (counts.get(letter, 0) / total) * 100
        expected = expected_pct
        if expected > 0:
            freq_score -= ((observed_pct - expected) ** 2) / expected
    
    # Word match bonus - extract words by removing punctuation
    # Split text and strip non-alphabetic characters from each word
    words = []
    for word in text.split():
        # Remove all non-alphabetic characters and convert to lowercase
        clean_word = ''.join(c for c in word if c.isalpha()).lower()
        if clean_word:  # Only add non-empty words
            words.append(clean_word)
    
    # Count matching common words and apply strong weight
    word_matches = sum(1 for word in words if word in COMMON_WORDS)
    word_bonus = word_matches * 300  # Strong weight to favor real English words
    
    # Hybrid score: frequency analysis + weighted word matches
    return freq_score + 100 + word_bonus


def letter_frequency(text: str) -> dict:
    """Return percentage frequency of each letter in text (uppercase keys)."""
    letters = [c.upper() for c in text if c.isalpha()]
    total = len(letters)
    if total == 0:
        return {ch: 0.0 for ch in string.ascii_uppercase}
    counts = Counter(letters)
    return {
        ch: round((counts.get(ch, 0) / total) * 100, 2)
        for ch in string.ascii_uppercase
    }


def cipher_stats(text: str) -> dict:
    """Return basic stats about the text."""
    letters = [c for c in text if c.isalpha()]
    return {
        'total_chars': len(text),
        'letters': len(letters),
        'spaces': text.count(' '),
        'symbols': len([c for c in text if not c.isalnum() and c != ' ']),
        'uppercase': sum(1 for c in text if c.isupper()),
        'lowercase': sum(1 for c in text if c.islower()),
    }
