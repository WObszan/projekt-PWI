FiltrySortowanie

FiltrySortowanie to klasa umożliwiająca sortowanie i filtrowanie zadań wczytanych z pliku JSON. Klasa obsługuje różne kryteria filtrowania, takie jak przedziały dat, godzin oraz filtrowanie według dowolnych kluczy i wartości.

Instalacja

Upewnij się, że masz zainstalowanego Pythona w wersji 3.6 lub nowszej.

Umieść plik z kodem klasy w swoim projekcie.

Użycie

Inicjalizacja

from filtry_sortowanie import FiltrySortowanie

filtry = FiltrySortowanie("plik_zadan.json")

Metody

1. sort_tasks(key, reverse=False)

Sortuje zadania według podanego klucza.

Parametry:

key (str): Klucz, według którego sortujemy.

reverse (bool): Określa kierunek sortowania (rosnąco/malejąco). Domyślnie False (rosnąco).

Zwraca:

Posortowaną listę zadań (list[dict]).

Przykład:

posortowane = filtry.sort_tasks("termin")

2. filter_tasks_by_date(start, end)

Filtruje zadania w podanym przedziale dat.

Parametry:

start (str): Data początkowa w formacie YYYY-MM-DD.

end (str): Data końcowa w formacie YYYY-MM-DD.

Zwraca:

Listę zadań w przedziale dat (list[dict]).

Przykład:

zadania_w_przedziale = filtry.filter_tasks_by_date("2025-01-01", "2025-01-10")

3. filter_by_hour(start, end)

Filtruje zadania w podanym przedziale godzin.

Parametry:

start (str): Godzina początkowa w formacie HH:MM.

end (str): Godzina końcowa w formacie HH:MM.

Zwraca:

Listę zadań w przedziale godzin (list[dict]).

Przykład:

zadania_w_godzinach = filtry.filter_by_hour("09:00", "12:00")

4. filter_tasks(key, value)

Filtruje zadania według wartości w danym kluczu.

Parametry:

key (str): Klucz, według którego filtrujemy.

value (str): Wartość, którą szukamy.

Zwraca:

Listę zadań spełniających kryteria (list[dict]).

Przykład:

zadania_wysoki_priorytet = filtry.filter_tasks("priorytet", "wysoki")

Obsługa błędów

W przypadku braku pliku JSON lub niepoprawnego formatu wyjątek FileNotFoundError lub ValueError zostanie zgłoszony.

W przypadku błędnego klucza w metodzie sortowania zgłoszony zostanie wyjątek ValueError.


