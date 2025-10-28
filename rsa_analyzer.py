import time
from Crypto.PublicKey import RSA

def rsa_key_generation_analysis(key_sizes):
    print("RSA Key Generation Time Analysis")
    print("--------------------------------")
    for size in key_sizes:
        start = time.time()
        key = RSA.generate(size)
        end = time.time()
        print(f"Key Size: {size} bits --> Time Taken: {end - start:.4f} seconds")

if __name__ == "__main__":
    key_sizes = [512, 1024, 2048, 4096]
    rsa_key_generation_analysis(key_sizes)
