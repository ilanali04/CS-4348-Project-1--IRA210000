#!/usr/bin/env python3
import sys
import string

ALPHA = string.ascii_uppercase

def clean_letters_only(s: str):
    s = s.strip()
    if not s or not all(ch.isalpha() for ch in s):
        return None
    return s.upper()

def vigenere_transform(text: str, key: str, mode: str) -> str:
    out = []
    klen = len(key)
    for i, ch in enumerate(text):
        ti = ord(ch) - 65
        ki = ord(key[i % klen]) - 65
        if mode == "ENCRYPT":
            oi = (ti + ki) % 26
        else:
            oi = (ti - ki + 26) % 26
        out.append(chr(oi + 65))
    return "".join(out)

def main():
    current_key = None
    for raw in sys.stdin:
        line = raw.strip()
        if not line:
            continue
        parts = line.split(maxsplit=1)
        cmd = parts[0].upper()
        arg = parts[1] if len(parts) > 1 else ""

        if cmd in ("PASS", "PASSKEY"):
            key = clean_letters_only(arg)
            if key is None:
                print("ERROR Invalid password; letters only", flush=True)
                continue
            current_key = key
            print("RESULT", flush=True)

        elif cmd == "ENCRYPT":
            if current_key is None:
                print("ERROR Password not set", flush=True)
                continue
            text = clean_letters_only(arg)
            if text is None:
                print("ERROR Invalid input; letters only", flush=True)
                continue
            print("RESULT " + vigenere_transform(text, current_key, "ENCRYPT"), flush=True)

        elif cmd == "DECRYPT":
            if current_key is None:
                print("ERROR Password not set", flush=True)
                continue
            text = clean_letters_only(arg)
            if text is None:
                print("ERROR Invalid input; letters only", flush=True)
                continue
            print("RESULT " + vigenere_transform(text, current_key, "DECRYPT"), flush=True)

        elif cmd == "QUIT":
            break

        else:
            print("ERROR Unknown command", flush=True)

if __name__ == "__main__":
    main()
