FILE = 'Pi.txt'

with open(FILE, 'r') as f:
    pi = f.read()

for i in range (15):
    print(pi[:15])
    pi = pi[15:]