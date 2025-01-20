# projekt-PWI



## Konfiguracja lokalna aby działa funkcja powiadomienia

Aby uruchomić projekt, musisz utworzyć plik `.env` w głównym katalogu projektu i dodać do niego swoje dane:

1. Skopiuj plik `.env.example` do `.env`.
2. Wypełnij zmienne środowiskowe:
   - `MY_EMAIL`: Twój adres e-mail.
   - `APP_PASSWORD`: Hasło aplikacji wygenerowane w ustawieniach Gmaila.

**Uwaga**: Nie commituj pliku `.env` do repozytorium, ponieważ zawiera poufne dane!

## Opis funkcjonalności
### Klasa FiltrySortowanie:
umożliwia zarządzanie zadaniami zapisanymi w pliku JSON poprzez różne operacje, takie jak:
1. Wczytywanie zadań – automatyczne załadowanie danych z pliku JSON zawierającego listę zadań.
2. Sortowanie zadań – możliwość sortowania według wybranego klucza (np. termin, priorytet) w kolejności rosnącej lub malejącej.
3. Filtrowanie po dacie – wybór zadań mieszczących się w określonym przedziale czasowym.
4. Filtrowanie po godzinach – wyszukiwanie zadań na podstawie przedziału godzinowego.
5. Filtrowanie według kryteriów – możliwość filtrowania zadań na podstawie dowolnego klucza, np. statusu lub kategorii.

