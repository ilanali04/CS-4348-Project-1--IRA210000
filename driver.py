#!/usr/bin/env python3
import sys
import os
import subprocess

def letters_only(s: str) -> bool:
    return s.isalpha()

def main():
    if len(sys.argv) != 2:
        print("Usage: driver.py <logfile>")
        sys.exit(1)

    logfile = sys.argv[1]
    base = os.path.dirname(os.path.abspath(__file__))
    logger_path = os.path.join(base, "logger.py")
    encryptor_path = os.path.join(base, "encryptor.py")

    logger = launch(logger_path, logfile)
    encryptor = launch(encryptor_path)

    def send(cmd):
        if encryptor.stdin is None or encryptor.stdout is None:
            return "ERROR pipe"
        encryptor.stdin.write(cmd.strip() + "\n")
        encryptor.stdin.flush()
        return encryptor.stdout.readline().strip()

    history = []
    log("START", "Driver started")

    print("=== Encryption Driver ===")
    print("Commands: password, encrypt, decrypt, history, quit")

    while True:
        cmd = input("\n> ").strip().lower()
        if cmd == "password":
            choice = pick_from_history(history, "Pick password from history or 0 for new")
            if choice is None:
                pwd = input("Enter password (letters only): ").strip()
                if not letters_only(pwd):
                    print("Letters only.")
                    continue
                log("CMD", "password set")
                resp = send(f"PASS {pwd}")
            else:
                log("CMD", "password set (history)")
                resp = send(f"PASS {choice}")

            print("Password set." if resp.startswith("RESULT") else resp)

        elif cmd == "encrypt":
            choice = pick_from_history(history, "Pick text to encrypt or 0 for new")
            if choice is None:
                s = input("Enter text: ").strip()
                if not letters_only(s):
                    print("Letters only.")
                    continue
                history.append(s)
                text = s
            else:
                text = choice
            log("CMD", "encrypt")
            resp = send(f"ENCRYPT {text}")
            if resp.startswith("RESULT"):
                out = resp.split(" ", 1)[1]
                print(out)
                history.append(out)
                log("RESULT", "encrypt ok")
            else:
                print(resp)
                log("RESULT", "encrypt error")

        elif cmd == "decrypt":
            choice = pick_from_history(history, "Pick text to decrypt or 0 for new")
            if choice is None:
                s = input("Enter text: ").strip()
                if not letters_only(s):
                    print("Letters only.")
                    continue
                history.append(s)
                text = s
            else:
                text = choice
            log("CMD", "decrypt")
            resp = send(f"DECRYPT {text}")
            if resp.startswith("RESULT"):
                out = resp.split(" ", 1)[1]
                print(out)
                history.append(out)
                log("RESULT", "decrypt ok")
            else:
                print(resp)
                log("RESULT", "decrypt error")

        elif cmd == "history":
            log("CMD", "history")
            print("(empty)" if not history else "\n".join(f"{i+1}. {h}" for i, h in enumerate(history)))
            log("RESULT", "history shown")

        elif cmd == "quit":
            log("CMD", "quit")
            encryptor.stdin.write("QUIT\n"); encryptor.stdin.flush()
            logger.stdin.write("QUIT\n"); logger.stdin.flush()
            log("EXIT", "Driver exiting")
            break

        else:
            print("Commands: password, encrypt, decrypt, history, quit")

if __name__ == "__main__":
    main()
