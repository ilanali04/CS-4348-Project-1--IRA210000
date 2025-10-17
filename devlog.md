**Initial thoughts 10-15-2015 4:40PM:** The project will need three programs these include logger, encryptor, and the driver. The driver will start the logger and encryptor and will communicate with them using pipes. The encryptor usesThe encryptor uses the Vigenère cipher to encrypt messages given by the user. The logger will timestamp the messages.

### Session 1 Start: 10-15-2025 5:04PM
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

c) Plan Today:
- Make the repo and a devlog
- Write logger.py (read lines, write timestamped “[ACTION] MESSAGE” to a file, stop on QUIT)
- Write encryptor.py (commands: PASS, ENCRYPT, DECRYPT, QUIT)
- Do quick tests from the terminal

### Session 1 End: 10-15-2025 8:20PM
a) Reflection
- I was able to complete the items I wanted for the session
- I was not able to conduct testing on the parts that I completed today and will need to do that tomorrow
- The coding although challenging was fun to do and I enjoyed the challenges I faced today
- Next session I would like to work on the integration of the driver and if possible I would like to test the code written today

### Session 2 Start: 10-16-2025 8:08PM
a) Thoughts so far
- I believe that my logger and encryptor will work from the last session
- I have the final part remaining which is the driver
- After finishing the driver I can move forward with the testing
- In between session I was working on the logger/encryptor and changed a few things

b) Plan for this session
- Finish up the driver and test along the way to see if the logger and encryptor are working as intended
- If I am able to finish all of the coding for the driver I can do a full end to end testing
