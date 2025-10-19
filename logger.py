import sys
from datetime import datetime

def main():
    if len(sys.argv) != 2:
        print("Usage: logger.py <logfile>", file=sys.stderr)
        sys.exit(1)
    logfile = sys.argv[1]

    with open(logfile, "a", encoding="utf-8") as f:
        for raw in sys.stdin:
            line = raw.strip()
            if not line:
                continue
            if line == "QUIT":
                break
            parts = line.split(maxsplit=1)
            action = parts[0]
            message = parts[1] if len(parts) > 1 else ""
            ts = datetime.now().strftime("%Y-%m-%d %H:%M")
            f.write(f"{ts} [{action}] {message}\n")
            f.flush()

if __name__ == "__main__":
    main()
