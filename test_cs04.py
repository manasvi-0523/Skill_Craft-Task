import sys
import numpy as np
sys.path.insert(0, 'SCT_CS_04')
from encrypt import encrypt
from decrypt import decrypt
from utils import key_to_seed

# Build a small fake image array (10x10 RGB)
np.random.seed(42)
original = np.random.randint(0, 256, (10, 10, 3), dtype=np.uint8)
key = 'TestKey123'

print('--- key_to_seed ---')
seed = key_to_seed(key)
print('Seed for', repr(key), ':', seed)
assert isinstance(seed, int), 'seed must be int'
print('PASS')

print()
print('--- encrypt / decrypt without shuffle ---')
enc, indices = encrypt(original.copy(), key, use_shuffle=False)
assert not np.array_equal(original, enc), 'encrypted should differ from original'
dec = decrypt(enc.copy(), key, use_shuffle=False)
assert np.array_equal(original, dec), 'decrypted must match original'
print('Encrypted differs from original: PASS')
print('Decrypted matches original:      PASS')

print()
print('--- encrypt / decrypt WITH shuffle ---')
enc_s, idx_s = encrypt(original.copy(), key, use_shuffle=True)
assert not np.array_equal(original, enc_s), 'shuffled encrypted should differ'
dec_s = decrypt(enc_s.copy(), key, use_shuffle=True)
assert np.array_equal(original, dec_s), 'shuffled decrypted must match original'
print('Shuffled encrypted differs:      PASS')
print('Shuffled decrypted matches:      PASS')

print()
print('--- wrong key should NOT decrypt correctly ---')
dec_wrong = decrypt(enc.copy(), 'WrongKey!', use_shuffle=False)
assert not np.array_equal(original, dec_wrong), 'wrong key must not recover original'
print('Wrong key gives different output: PASS')

print()
print('SCT_CS_04 ALL PASS')
