## 10-15-2015 4:40PM
**Initial thoughts:** The project will need three programs these include logger, encryptor, and the driver. The driver will start the logger and encryptor and will communicate with them using pipes. The encryptor usesThe encryptor uses the Vigenère cipher to encrypt messages given by the user. The logger will timestamp the messages.

**Plan Today:**
- Make the repo and a devlog.
- Write logger.py (read lines, write timestamped “[ACTION] MESSAGE” to a file, stop on QUIT).
- Write encryptor.py (commands: PASS, ENCRYPT, DECRYPT, QUIT).
- Do quick tests from the terminal.
