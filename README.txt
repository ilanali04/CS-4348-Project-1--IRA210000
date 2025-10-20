
Files and Roles:
driver.py — Main program. Launches logger.py (with logfile argument) and encryptor.py. Shows a menu (password, encrypt, decrypt, history, quit), keeps a session history, and logs actions and results.

encryptor.py — Vigenère cipher backend. Reads commands from standard input and prints responses:
PASS <KEY> → RESULT
ENCRYPT <TEXT> → RESULT <CIPHERTEXT>
DECRYPT <TEXT> → RESULT <PLAINTEXT>
QUIT → exit
On errors → ERROR <message>

logger.py — Logger process. Takes one argument (logfile name). Reads lines from standard input and appends timestamped entries as:
YYYY-MM-DD HH:MM [ACTION] MESSAGE
Stops on QUIT.


How to Run (command line):
From the folder with the files, run:
python3 driver.py mylog.txt

Then use the menu shown:
password, encrypt, decrypt, history, quit


Optional quick tests:
Logger alone:
printf "START hello\nQUIT\n" | python3 logger.py test.log

Encryptor alone:
python3 encryptor.py
PASS HELLO
ENCRYPT WORLD
QUIT

