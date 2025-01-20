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
1. Wczytywanie zadań:
   - automatyczne załadowanie danych z pliku JSON zawierającego listę zadań.
2. Sortowanie zadań:
   - możliwość sortowania według wybranego klucza (np. termin, priorytet) w kolejności rosnącej lub malejącej.
3. Filtrowanie po dacie:
   - wybór zadań mieszczących się w określonym przedziale czasowym.
4. Filtrowanie po godzinach:
   - wyszukiwanie zadań na podstawie przedziału godzinowego.
5. Filtrowanie według kryteriów:
    - możliwość filtrowania zadań na podstawie dowolnego klucza, np. statusu lub kategorii.
### Klasa Powiadomienia:
1. Uruchamianie w tle:
   - Sprawdza zadania co minutę w osobnym wątku.
2. Odczyt zadań:
   - Wczytuje dane z pliku JSON, obsługuje błędy pliku.
   - Wysyłanie e-maili:
3. Wysyła powiadomienia przez SMTP Gmail.
   - Formatuje treść jako HTML z kolorami priorytetu.
   - Sprawdzanie terminów:
   - Wysyła przypomnienia na podstawie daty i godziny.
   - Dodatkowo przypomina o jutrzejszych zadaniach o wysokim priorytecie.
4. Działanie programu:
   - Uruchamiane w wątku typu daemon.
   - Nieskończona pętla utrzymująca działanie programu.
### Klasa WejścieWyjście
1. Funkcja save_tasks_to_json(tasks, filename="tasks.json")
   - Zapisuje listę zadań do pliku JSON.
   - Dane są formatowane i zapisane w pliku w sposób czytelny (z wcięciami).
   - Obsługuje błędy zapisu i informuje o sukcesie lub problemach.
2. Funkcja load_tasks_from_json(filename="tasks.json")
   - Wczytuje listę zadań z pliku JSON.
   - Obsługuje przypadki braku pliku, błędnego formatu JSON oraz inne błędy.
   - Zwraca listę zadań lub pustą listę w przypadku problemów.
3. Kluczowe funkcjonalności klasy:
   - Obsługa wyjątków (brak pliku, błędny format JSON).
   - Kodowanie UTF-8 dla obsługi znaków specjalnych.
   - Czytelny zapis JSON z wcięciami (indent=4).
   - Domyślna nazwa pliku "tasks.json", którą można zmienić.
