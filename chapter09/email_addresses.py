# email_addresses.py

# Just stick some data there
from typing import Counter


with open('email_addresses.txt', 'w') as f:
    f.write("joelgrus@gmail.com\n")
    f.write("joel@m.datasciencester.com\n")
    f.write("joelgrus@m.datasciencester.com\n")

def get_domain(email_address: str) -> str:
    """Split on '@' and return the last piece"""
    return email_address.lower().split("@")[-1]

# a couple of tests
assert get_domain('joelgrus@gmail.com') == 'gmail.com'
assert get_domain('joel@m.datasciencester.com') == 'm.datasciencester.com'

with open('email_addresses.txt', 'r') as f:
    domain_counts = Counter(get_domain(line.strip()) for line in f
                                                         if '@' in line)
print(domain_counts)
