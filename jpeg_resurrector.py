#!/usr/bin/env python3
import sys

def extract_jpeg(data):
    headers = [b'\xff\xd8\xff\xe0', b'\xff\xd8\xff\xe1']
    for header in headers:
        index = data.find(header)
        if index != -1:
            print(f"[+] Found JPEG header at offset {index}")
            return data[index:]
    return None

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 jpeg_resurrector.py <input_file.fatp> <output_image.jpg>")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, "rb") as f:
            raw_data = f.read()

        recovered = extract_jpeg(raw_data)
        if recovered:
            with open(output_file, "wb") as f:
                f.write(recovered)
            print(f"[✔] Image recovered and saved as: {output_file}")
        else:
            print("[✘] No JPEG header found. File may be fully encrypted.")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    main()
