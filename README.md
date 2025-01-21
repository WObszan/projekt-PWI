# projekt-PWI



## Konfiguracja lokalna aby działa funkcja powiadomienia

Aby uruchomić projekt, musisz utworzyć plik `.env` w głównym katalogu projektu i dodać do niego swoje dane:
1. W terminalu pobierz paczke dotenv wpisując kod: pip install python-dotenv
2. Przy okazji pobierz paczkę matplotlib wpisujac kod: pip install matplotlib
3. Skopiuj plik `.env.example` do `.env`.
4. Wypełnij zmienne środowiskowe:
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
### Klasa TaskStats
Ten kod umożliwia zarządzanie i analizę zadań w aplikacji typu lista zadań na podstawie danych przechowywanych w pliku JSON. Główne funkcje obejmują:

1. Analiza zadań według statusu
   - Liczy, ile zadań znajduje się w różnych statusach, np. "zrobione" lub "nie zrobione".
2. Analiza zadań według kategorii
   - Liczy, ile zadań przypisano do każdej kategorii, np. "Praca", "Dom" czy "Zdrowie".
3. Zadania z bliskim terminem wykonania
   - Oblicza, ile zadań pozostaje do zrobienia w określonych przedziałach czasowych: dzisiaj, jutro i w bieżącym tygodniu.
4. Śledzenie globalnych statystyk kategorii
   - Zapisuje dane o wykonanych zadaniach według kategorii w osobnym pliku JSON, umożliwiając późniejszą analizę.
5. Obliczanie procentowego udziału zadań w kategoriach
   - Wylicza procent wykonanych zadań dla każdej kategorii i wyświetla wynik w formie czytelnego raportu.
### Klasa CategoryTagManager
1. Dodawanie kategorii (add_category)
   - Dodaje nową kategorię, jeśli jeszcze nie istnieje.
   - Sprawdza poprawność nazwy (czy nie jest pusta).
   - Informuje o dodaniu lub istnieniu kategorii.
2. Usuwanie kategorii (remove_category)
   - Usuwa kategorię, jeśli istnieje w zbiorze.
   - Informuje o wyniku operacji.
3. Dodawanie tagu (add_tag)
   - Dodaje nowy tag, jeśli jeszcze nie istnieje.
   - Sprawdza poprawność nazwy (czy nie jest pusta).
   - Informuje o dodaniu lub istnieniu tagu.
4. Usuwanie tagu (remove_tag)
   - Usuwa tag, jeśli istnieje w zbiorze.
   - Informuje o wyniku operacji.
5. Filtrowanie zadań według kategorii (filter_tasks_by_category)
   - Sprawdza, czy podana kategoria istnieje.
   - Zwraca listę zadań pasujących do danej kategorii.
6. Filtrowanie zadań według tagów (filter_tasks_by_tag)
   - Sprawdza, czy podany tag istnieje.
   - Zwraca listę zadań zawierających dany tag.

### Plik dod_usu_edy.py
1. Ładowanie i zapisywanie zadań
   - wczytuje zadania z pliku JSON oraz zapisuje je po dokonaniu zmian.
2. Dodawanie nowych zadań
   - umożliwia dodanie zadania z unikalnym identyfikatorem, priorytetem, kategorią i terminem.
3. Edycję zadań
   - pozwala na modyfikowanie szczegółów istniejącego zadania (np. opisu, godziny).
4. Usuwanie zadań
   - usuwa jedno lub wybrane zadania i automatycznie aktualizuje identyfikatory pozostałych zadań.
5. Usuwanie wszystkich zadań
   - kasuje wszystkie zadania i zapisuje pustą listę.

Po dodaniu zadania skrypt aktualizuje globalne statystyki za pomocą funkcji global_stats().
Wspiera priorytety (niski, średni, wysoki) oraz kategorie, a także zapewnia kontrolę nad danymi w formacie JSON.
