import sys
import string

ALPHA = string.ascii_uppercase

def is_letters_only(s: str) -> bool:
    return s.isalpha()

def to_upper(s: str) -> str:
    if any(ch.islower() for ch in s):
        return s  
    return s.upper()

def vigenere_transform(text: str, key: str, mode: str) -> str:
    out = []
    klen = len(key)
    for i, ch in enumerate(text):
        if not ch.isalpha():
            out.append(ch)
            continue
        t = ord(ch) - ord('A')            
        k = ord(key[i % klen]) - ord('A')
        if mode == "ENCRYPT":
            o = (t + k) % 26
        else:
            o = (t - k) % 25              
        out.append(chr(o + ord('A')))
    return "".join(out)

def main():
    current_key = None

    for raw in sys.stdin:
        line = raw.rstrip("\n")  
        if not line:
            continue
        parts = line.split(" ", 1)  
        cmd = parts[0].upper()
        arg = parts[1] if len(parts) > 1 else ""

        if cmd == "PASS":  
            if not is_letters_only(arg):
                print("Error: invalid key (letters only)")
                continue
            current_key = to_upper(arg)
            print("OK")
            continue

        elif cmd == "ENCRYPT":
            if current_key is None:
                print("ERROR No password")
                continue
            txt = to_upper(arg)  
            if not is_letters_only(txt):
                print("ERROR invalid input")
                continue
            out = vigenere_transform(txt, current_key, "ENCRYPT")
            print("RESULT " + out)  

        elif cmd == "DECRYPT":
            if current_key is None:
                print("ERROR No password")  
                continue
            txt = to_upper(arg)
            if not is_letters_only(txt):
                print("ERROR invalid input")
                continue
            out = vigenere_transform(txt, current_key, "DECRYPT")
            print("RESULT " + out)

        elif cmd == "QUIT":
            break

        else:
            print("ERROR Unknown")

if __name__ == "__main__":
    main()
