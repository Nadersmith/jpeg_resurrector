import sys

def xor_decrypt(data, key):
    return bytes([b ^ key for b in data])

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 fatp_xor_decrypt.py <encrypted_file>")
        return

    path = sys.argv[1]
    with open(path, "rb") as f:
        encrypted = f.read()

    for key in range(1, 256):
        decrypted = xor_decrypt(encrypted, key)
        if decrypted.startswith(b'\xff\xd8\xff'):
            print(f"[+] Found valid JPEG header using XOR key = {key}")
            with open(f"decrypted_{key}.jpg", "wb") as out:
                out.write(decrypted)
            print(f"    → Saved as decrypted_{key}.jpg")

if __name__ == "__main__":
    main()
