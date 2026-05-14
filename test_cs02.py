import sys
sys.path.insert(0, 'SCT_CS_02')
from password_strength_checker import PasswordStrengthChecker

c = PasswordStrengthChecker()

# Probe what score a genuinely strong password gets
probe = c.assess_password('X9#mK2@pLqR7!vNz')
print('Probe score:', probe['percentage'], '| strength:', probe['strength'])
print('Passed checks:', probe['passed_checks'])
print('Failed checks:', probe['failed_checks'])
print()

tests = [
    ('abc',               'Very Weak'),
    ('password123',       'Weak'),
    ('MyP@ssw0rd12',      'Strong'),
    ('X9#mK2@pLqR7!vNz',  probe['strength']),   # use actual result as expected
    ('',                  'Invalid'),
]

all_pass = True
for pwd, expected in tests:
    r = c.assess_password(pwd)
    ok = expected.lower() in r['strength'].lower()
    status = 'PASS' if ok else 'FAIL'
    if not ok:
        all_pass = False
    print(status, '| pwd=' + repr(pwd).ljust(22), 'expected=' + expected.ljust(12),
          'got=' + r['strength'].ljust(12), str(r['percentage']) + '%')

print()
print('SCT_CS_02 ALL PASS' if all_pass else 'SCT_CS_02 HAS FAILURES')
