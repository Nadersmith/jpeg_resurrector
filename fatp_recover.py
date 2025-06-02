#!/usr/bin/env python3
import sys

IMAGE_HEADERS = {
    b'\xff\xd8\xff': "jpg",
    b'\x89PNG\r\n\x1a\n': "png",
    b'BM': "bmp"
}

def detect_image_headers(data):
    found = []
    for signature, ext in IMAGE_HEADERS.items():
        offset = data.find(signature)
        if offset != -1:
            found.append((signature, offset, ext))
    return found

def xor_brute_force(data, preview_len=64):
    results = []
    for key in range(1, 256):
        decrypted = bytes([b ^ key for b in data[:preview_len]])
        if decrypted.startswith(tuple(IMAGE_HEADERS.keys())):
            results.append((key, decrypted))
    return results

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 fatp_recover.py <encrypted_file>")
        return

    input_file = sys.argv[1]

    with open(input_file, "rb") as f:
        data = f.read()

    print("[+] Step 1: Searching for known image headers...")
    headers = detect_image_headers(data)
    if headers:
        for _, offset, ext in headers:
            print(f"  - Found {ext.upper()} header at offset {offset}")
            out_name = f"recovered_image.{ext}"
            with open(out_name, "wb") as out:
                out.write(data[offset:])
            print(f"  - Saved as {out_name}")
    else:
        print("[!] No image headers found directly. Trying XOR brute-force...")

        brute_results = xor_brute_force(data)
        for key, preview in brute_results:
            print(f"[?] Possible XOR key: {key} → preview: {preview[:10]}")
            # يمكن لاحقاً نطبّق هذا المفتاح على كل الملف ونستخرج البيانات

if __name__ == "__main__":
    main()
