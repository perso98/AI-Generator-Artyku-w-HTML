 # AI Article HTML Generator

## Opis projektu

AI Article HTML Generator to aplikacja w Pythonie, która przetwarza tekstowy plik artykułu i generuje z niego HTML przy użyciu API OpenAI. Wygenerowany kod HTML jest strukturalnie sformatowany oraz zawiera miejsca na grafiki, które można później wypełnić. Aplikacja zapisuje wygenerowany HTML w dedykowanym pliku `artykul.html` i aktualizuje podgląd w `podglad.html`.

### Kluczowe funkcjonalności
- Odczytywanie treści artykułu z pliku tekstowego.
- Generowanie kodu HTML z użyciem API OpenAI, zgodnie z określonymi wytycznymi:
  - Strukturyzacja treści za pomocą tagów HTML.
  - Wstawianie miejsc na grafiki z atrybutem `alt` i opisem do generowania grafiki.
- Zapisanie wygenerowanego kodu HTML w pliku `artykul.html`.
- Aktualizacja podglądu w `podglad.html` poprzez wstawienie wygenerowanej treści HTML.

## Wymagania

- Python 3.x
- Konto i klucz API OpenAI
- Pliki konfiguracyjne i zależności:
  - Plik `.env` z kluczem API OpenAI (`OPENAI_API_KEY`).
  - `requirements.txt` z wymaganymi pakietami.

## Instalacja

1. Sklonuj repozytorium:
   ```
   gh repo clone perso98/Zadanie-rekrutacyjne-OXIDO
   ```
2. Zainstaluj wymagane pakiety:

   ```
   pip install -r requirements.txt
   ```
3. Dodaj plik `.env` w głównym katalogu projektu z kluczem API OpenAI:
   ```
    OPENAI_API_KEY=your_openai_api_key
   ```
   ## Uruchomienie

1. Upewnij się, że plik artykułu `artykul.txt` znajduje się w katalogu `data`.

2. Uruchom aplikację:

   ```
   python src/main.py
   ```
## Po zakończeniu

Po zakończeniu działania programu:

- Wygenerowany plik HTML znajdziesz w `data/output/artykul.html`.
- Podgląd z wstawioną treścią HTML jest dostępny w `templates/podglad.html`.

## Struktura projektu

- **data/** – Katalog na pliki wejściowe i wyjściowe.
  - **artykul.txt** – Plik z treścią artykułu.
  - **output/** – Katalog na wygenerowany plik HTML (`artykul.html`).
- **src/** – Główne źródło kodu.
  - **main.py** – Plik uruchamiający główny proces aplikacji.
  - **utils.py** – Funkcje pomocnicze do odczytu i zapisu plików oraz aktualizacji podglądu.
  - **openai_integration.py** – Integracja z API OpenAI i generowanie HTML.
- **templates/** – Szablony HTML.
  - **podglad.html** – Plik podglądu, gdzie wstawiana jest treść HTML.
  - **szablon.html** – Podstawowy szablon HTML.
- **.env** – Plik konfiguracyjny z kluczem API OpenAI.
- **requirements.txt** – Lista wymaganych pakietów.
  
 ![image](https://github.com/user-attachments/assets/fcdb85a0-702b-4b02-93d3-a8547c0fbec0)



## Wykorzystanie OpenAI API

Aplikacja korzysta z API OpenAI do przetworzenia artykułu na HTML. Prompt zawiera szczegółowe wytyczne dotyczące formatowania, struktury nagłówków, list, cytatów i grafik. Wygenerowany kod HTML spełnia następujące wymagania:
- Struktura nagłówków i akapitów.
- Grafiki wstawiane są za pomocą tagu `<figure>` i `<img>` z atrybutem `alt` oraz `<figcaption>`.
- Kod HTML nie zawiera stylów CSS ani JavaScriptu.

## Obsługa błędów

Aplikacja została wyposażona w bloki `try-except`, które wychwytują i logują potencjalne błędy, takie jak:
- Brak pliku wejściowego `artykul.txt`.
- Błędy podczas komunikacji z API OpenAI.
- Problemy z zapisem do plików.

## Przykłady użycia

Przykładowa komenda do uruchomienia aplikacji:

```
python src/main.py
```
## Po uruchomieniu aplikacji

Po uruchomieniu aplikacji:

1. Aplikacja przetworzy plik `artykul.txt` znajdujący się w katalogu `data` i wygeneruje kod HTML.
2. Wygenerowany plik HTML zostanie zapisany w `data/output/artykul.html`.
3. Podgląd z wstawioną treścią HTML zostanie zaktualizowany w `templates/podglad.html`.

## Wygląd wygenerowanego artykułu:
![screencapture-file-E-PythonRepos-Oxido-Zadanie-rekrutacyjne-OXIDO-templates-podglad-html-2024-11-14-01_46_30](https://github.com/user-attachments/assets/762e24a6-0f77-42aa-ac0b-b7b13dce4b02)


Inny przykład:
![screencapture-file-E-PythonRepos-Oxido-Zadanie-rekrutacyjne-OXIDO-templates-podglad-html-2024-11-14-01_45_17](https://github.com/user-attachments/assets/c1138d4e-8057-4b83-95a8-5603f1808715)

