BACKEND

~~ INSTALACJA
Do instalacji konieczny jest Python 3.8 (użyto Walrus Operator). Projekt konfigurowany jest z uzyciem biblioteki django-dotenv. Umozliwia integracje z dowolna baza danych kompatybilna z Django, poprzez podanie standardowych parametrów bazy w pliku .env (wyjatkowo zawartego w repozytorium). Domyslnie uzywana jest baza SQLite. Ponizej zawarto równiez opis konfiguracji dla bazy Postgres. Projekt zawiera dwie management commands, inicjalizujące dane w bazie.


Srodowisko wirtualne:
- przejsc do foldery projektu
- python3.8 -m venv .venv
- pip install -r requirements.txt

Integracja z Postgress:
- otworzyc plik .env
- DB_ENGINE=django.db.backends.postgresql_psycopg2
- pozostale parametry wedlug bazy

Inicjalizacja bazy:
- wejsc do srodowiska wirtualnego projektu
- ./manage.py migrate
- ./manage.py populate_db.py
- ./manage.py create_admins.py


~~ PANEL ADMINA
Utworzone dane inicjalizacyjne zawieraja m.in. 3 uzytkowników:
- "admin"
- "Pan Z Manekina"
- "Pan Ze Sliwki"
wszyscy z haslem "password".

"admin" jest superuserem, pozostali naleza do customowej grupy Manager. Panel admina umozliwia tworzenie, przegladanie i edycje tresci zwiazanych ze swoja restauracja. Co wazne, kazdy Manager widzi tylko dane o SWOJEJ restauracji. Możliwe jest również dodanie zdjęcia do dania.


~~ API RESTOWE
API zostalo zaimplementowane z uzyciem Django Rest Framework, viewsetów, serializerów oraz routerów. Ponadto mozliwe jest sortowanie rekordów równiez po stronie backendu (zob. menus.views.MenuViewset). Do paginacji uzyto wbudowanej w DRF klasy LimitOffsetPagination (zob. config.settings.REST_FRAMEWORK).




FRONTEND

~~ INSTALACJA I URUCHOMIENIE
Projekt stworzony jest w ramach frameworka Vue, z uzyciem biblioteki UI Quasar. Wymagana jest równiez instalacja Node.
Uwaga: Wszystkie URLe w projekcie zakladaja ze backend serwowany jest pod adresem http://localhost:8000.

- npm install
- npm run serve
- Upewnic sie ze backend serwuje dane.
