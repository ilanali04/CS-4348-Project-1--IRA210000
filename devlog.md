**Initial thoughts 10-15-2015 4:40PM:** The project will need three programs these include logger, encryptor, and the driver. The driver will start the logger and encryptor and will communicate with them using pipes. The encryptor usesThe encryptor uses the Vigenère cipher to encrypt messages given by the user. The logger will timestamp the messages.

### Session 1: 10-15-2025 5:04PM
a) Thoughts so far
- I understand the project needs three programs: driver.py (main), encryptor.py, and logger.py
- The driver will start the other two and talk to them through pipes
- I want to keep inputs letters-only and make everything case-insensitive
- No new blockers right now; I just need to implement logger and encryptor first, then wire the driver tomorrow

b) Plan for this session
- Repo setup
- Initialize a git repo
- Create devlog.md and make the first commit
Logger (logger.py)
- Read lines from stdin until QUIT
- Parse first word as [ACTION], rest as MESSAGE
- Append YYYY-MM-DD HH:MM [ACTION] MESSAGE to the log file
- Quick test: printf "START hello\nQUIT\n" | python3 logger.py test.log

Encryptor (encryptor.py)
- Maintain a current passkey in memory
- Implement commands:
  - PASS <key> (or PASSKEY) → set key (letters-only, uppercase)
  - ENCRYPT <TEXT> → Vigenère encrypt with current key; print RESULT <cipher>
  - DECRYPT <TEXT> → Vigenère decrypt; print RESULT <plain>
  - ERROR messages if no key or invalid input; QUIT` to exit
  - Quick tests from terminal by typing commands into the process

Plan Today:
- Make the repo and a devlog
- Write logger.py (read lines, write timestamped “[ACTION] MESSAGE” to a file, stop on QUIT)
- Write encryptor.py (commands: PASS, ENCRYPT, DECRYPT, QUIT)
- Do quick tests from the terminal
