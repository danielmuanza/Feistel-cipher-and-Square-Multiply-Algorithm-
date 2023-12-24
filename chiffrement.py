def perm(a):
    b = ((a[0] & 14) << 1) + ((a[1] & 14) >> 1) + ((a[2] & 14) << 2) + ((a[3] & 14) >> 2)
    c = ((a[4] & 14) << 1) + ((a[5] & 14) >> 1) + ((a[6] & 14) << 2) + ((a[7] & 14) >> 2)
    return (b, c)

def unperm(b):
    a = (((b[0] & 15) >> 0) + ((b[1] & 15) << 2) + ((b[2] & 15) >> 2) + ((b[3] & 15) << 1),
         (((b[4] & 15) >> 0) + ((b[5] & 15) << 2) + ((b[6] & 15) >> 2) + ((b[7] & 15) << 1)))
    return a

def process(b, k):
    p, q = perm(b)
    t = [p[0], p[1], q[0], q[1]]
    a = [t[i] for i in [1, 3, 2, 0]]
    r = [a[i] for i in [2, 0, 3, 1]]
    f = [a[i] for i in [0, 2, 1, 3]]
    l = [a[i] for i in [3, 1, 0, 2]]
    o = [((k[i] & 15) << 1) + ((k[i+1] & 15) >> 3) for i in range(0, 7, 2)]
    r = [(((r[i] >> 4) & 15) + (o[i] << 4)) % 256 for i in range(4)]
    o = [((k[i] & 15) << 1) + ((k[i+1] & 15) >> 3) for i in range(1, 8, 2)]
    l = [(((l[i] >> 4) & 15) + (o[i] << 4)) % 256 for i in range(4)]
    s = [((f[i] & 15) << 4) + ((l[i] & 15) >> 4) for i in range(4)]
    t = [(((s[i] >> 4) & 15) + (f[i+1] << 4)) % 256 for i in range(3)] + [s[3]]
    c = [t[i] for i in [2, 0, 3, 1]]
    return c

def feistel(n, k):
    b = [(n >> i) & 255 for i in range(0, 32, 8)]
    k = [(k >> i) & 255 for i in range(0, 32, 8)]
    return process(b, k)

def encrypt(plaintext, key):
    return feistel(plaintext, key)

# Example usage:
plaintext = 0x12345678
key = 0x9abcdef0
ciphertext = encrypt(plaintext, key)
print("Ciphertext: ", hex(ciphertext))