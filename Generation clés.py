def left_shift(input_num, shift_order):
    input_bin = format(input_num, '04b')
    shifted_bin = input_bin[shift_order:] + input_bin[:shift_order]
    shifted_num = int(shifted_bin, 2)
    return shifted_num

def right_shift(input_num, shift_order):
    input_bin = format(input_num, '04b')
    shifted_bin = input_bin[-shift_order:] + input_bin[:-shift_order]
    shifted_num = int(shifted_bin, 2)
    return shifted_num

def permute(input_num):
    H = 65274130
    return input_num ^ H

def feistel_key_gen(K):
    k1 = K // 2**4
    k2 = K % 2**4
    k1 = permute(k1)
    k2 = permute(k2)
    k1 = left_shift(k1, 2)
    k2 = right_shift(k2, 1)
    return (k1, k2)

# Example usage
K = 2391687792379477422965888549598285964654
k1, k2 = feistel_key_gen(K)
print("Sub-keys (k1, k2): ", k1, k2)