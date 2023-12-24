def inverse_perm(n):
    return (((((n >> 0) & 15) << 4) + ((n >> 4) & 15)) % 256,
            (((((n >> 8) & 15) << 4) + ((n >> 12) & 15)) % 256)

def perm(b):
    p = [b[i] for i in [1, 3, 2, 0]]
    q = [b[i] for i in [0, 2, 1, 3]]
    t = [(p[0] + p[1]) % 256,
         (p[2] + q[0]) % 256,
         (p[3] + q[1]) % 256,
         (q[2] + q[3]) % 256]
    return t, q

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

def decrypt(ciphertext, key):
    return feistel(ciphertext, key)

# Example usage:
ciphertext = 0x92c112b6
key = 0x9abcdef0
plaintext = decrypt(ciphertext, key)
print("Plaintext: ", hex(plaintext))