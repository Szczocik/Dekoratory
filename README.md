# Dekoratory - rozbudowa programu accountant

Rozbuduj program accountant - zbuduj klasę Manager, która będzie implementowała metodę assign jak w tej lekcji. 
Akcje sprzedaż, zakup saldo itp muszą być definiowane poprzez użycie dekoratora.

"""
Rozszerzmy nasz program do systemu księgowego. Zamiast pisać i czytać ze standardowego wejścia/wyjścia, rezultat czyta i zapisuje do podanego pliku.
Program jest wywoływany w następujący sposób:
a) python saldo.py <plik><int wartosc> <str komentarz>
b) python sprzedaz.py <plik><str identyfikator produktu> <int cena> <int liczba sprzedanych>
c) python zakup.py <plik> <str identyfikator produktu> <int cena> <int liczba zakupionych>
d) python konto.py <plik>
e) python magazyn.py <plik><str identyfikator produktu 1> <str identyfikator produktu 2> <str identyfikator produktu 3> ...
f) python przeglad.py <plik>
"""

Niedozwolone są żadne zmienne globalne, wszystkie dane powinny być przechowywane wewnątrz obiektu Manager.
