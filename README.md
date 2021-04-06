***Witamy w oficjalnej dokumetacji strony internetowej projektu SensoPark!***

_**Szybkie uruchomienie**_

Mając pobrane nasze repozytorium musimy określić zmienne środowiskowe. Aby to zrobić należy wpisać w naszym środowsku (dla systemu windows):

- _set FLASK_APP=sensopark.py_
- _set_ MAIL_USERNAME=[GMAIL EMAIL]_ //Podajemy swój email na portalu gmail. Należy pamiętać aby pozwolić aplikacją na dostęp do konta
- _set_ MAIL_PASSWORD=[GMAIL PASSWORD] _// Podajemy hasło
- _set_ SQL_IP=[SQL_IP] _ // Podajemy IP naszej bazy danych (Narazie tylko mysql)
- _set_ SQL_DB=[SQL_DB]_ // Podajemy nazwe bazy danych na której bedziemy pracować
- __set_ SQL_NAME=[SQL_NAME]_ // Podajemy nazwe naszej instancji
- __set_ ADMIN=[ADMIN]_ // podajemy maila który po zarajestrowaniu będzie automatycznie administatorem

Dla systemu Linux lub MacOS

-_export FLASK_APP=sensopark.py_
-_export _ MAIL_USERNAME=[GMAIL EMAIL]_ 
-_export _ MAIL_PASSWORD=[GMAIL PASSWORD] _
-_export _ SQL_IP=[SQL_IP] _
-_export _ SQL_DB=[SQL_DB]_ 
-__export _ SQL_NAME=[SQL_NAME]_ 
-__export _ ADMIN=[ADMIN]_ 

**Wybór innej bazy danych niż mysql**
W pliku config należy zmienić linijkę 34,39,43 (Domyślnie jest wybrana baza Mysql+pymysql)

postgresql://nazwa_użytkownika:hasło@nazwa_hosta/baza_danych

SQLite (Linux, macOS) sqlite:////bezwzględna/ścieżka/do/bazy_danych

SQLite (Windows) sqlite:///c:/bezwzględna/ścieżka/do/bazy_danych
