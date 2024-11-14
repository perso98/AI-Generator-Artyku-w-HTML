# AI Generator Artykułów HTML

## Opis projektu

AI Generator Artykułów HTML to aplikacja w Pythonie, która przetwarza tekstowy plik artykułu i generuje z niego HTML przy użyciu API OpenAI. Wygenerowany kod HTML jest strukturalnie sformatowany oraz zawiera miejsca na grafiki, które można później wypełnić. Aplikacja zapisuje wygenerowany HTML w dedykowanym pliku `artykul.html` i aktualizuje podgląd w `podglad.html`.

### Kluczowe funkcjonalności
- Odczytywanie treści artykułu z pliku tekstowego.
- Generowanie kodu HTML z użyciem API OpenAI, zgodnie z określonymi wytycznymi:
  - Strukturyzacja treści za pomocą tagów HTML.
  - Wstawianie miejsc na grafiki z atrybutem `alt` i opisem do generowania grafiki.
- Zapisanie wygenerowanego kodu HTML w pliku `artykul.html`.
- Aktualizacja podglądu w `podglad.html` poprzez wstawienie wygenerowanej treści HTML.

## Wymagania

- Python 3.x
- Klucz do API OpenAI
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
   Plik .env.example ukazuje przykład tego pliku.
   
   ## Uruchomienie

1. Upewnij się, że plik artykułu `artykul.txt` znajduje się w katalogu `data`.
   Plik `artykul.txt` powinien zawierać treść artykułu w formie tekstowej, który zostanie przetworzony przez aplikację na format HTML.

3. Uruchom aplikację:

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

- **Struktura nagłówków i akapitów** – Aplikacja wykorzystuje odpowiednie znaczniki HTML, takie jak `<h1>`, `<h2>`, `<h3>`, `<p>`, `<ul>`, `<ol>`, `<blockquote>`, aby zapewnić poprawne formatowanie i organizację treści. Dzięki temu artykuł jest logicznie podzielony na sekcje, listy i cytaty.

- **Grafiki z precyzyjnymi opisami** – W kodzie HTML automatycznie umieszczane są miejsca na grafiki, zgodnie z instrukcjami zadania. Każda grafika jest osadzona w tagu `<figure>`, z tagiem `<img>` zawierającym atrybut `src="image_placeholder.jpg"`. Dodatkowo, każdy obrazek ma atrybut `alt` z opisem (promptem) dostarczającym szczegółowe instrukcje dotyczące generowania obrazu. Pod grafiką znajduje się również podpis (`<figcaption>`), związany z kontekstem artykułu.

- **Brak stylów CSS ani JavaScriptu** – Wygenerowany kod HTML składa się wyłącznie z czystego HTML. Nie zawiera żadnych stylów CSS ani JavaScriptu, zgodnie z wytycznymi zadania. Aplikacja zapewnia, że kod HTML zawiera tylko zawartość przeznaczoną do osadzenia pomiędzy tagami `<body>` i `</body>`, bez dodatkowych sekcji takich jak `<html>`, `<head>`, czy `<body>`.

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
![screencapture-file-E-PythonRepos-Oxido-Zadanie-rekrutacyjne-OXIDO-templates-podglad-html-2024-11-14-12_50_44](https://github.com/user-attachments/assets/b8da1cdf-c86b-41b8-a2bf-8a21e64b9ccf)

## Inny przykład:
![screencapture-file-E-PythonRepos-Oxido-Zadanie-rekrutacyjne-OXIDO-templates-podglad-html-2024-11-14-13_13_49](https://github.com/user-attachments/assets/c60b60dd-b169-4ebb-81d1-d88ae83a6e77)

## Inny przykład:
![screencapture-file-E-PythonRepos-Oxido-Zadanie-rekrutacyjne-OXIDO-templates-podglad-html-2024-11-14-13_05_25](https://github.com/user-attachments/assets/40539ab2-c8d8-4eb4-9760-c5b60d5234f0)


## Możliwe kierunki dalszego rozwoju

1. **Dodanie interfejsu użytkownika** – Rozbudowanie aplikacji o prosty interfejs graficzny (GUI) pozwoliłoby użytkownikom łatwiej przesyłać artykuły do przetworzenia oraz przeglądać wyniki w czasie rzeczywistym.

2. **Obsługa wielu języków** – Integracja wsparcia dla różnych języków mogłaby uczynić aplikację bardziej uniwersalną, umożliwiając generowanie HTML z artykułów w wielu językach.

3. **Zaawansowana edycja promptów** – Umożliwienie użytkownikom dostosowania promptów przed przesłaniem artykułu do API OpenAI mogłoby zwiększyć elastyczność aplikacji i dostosować wynik do specyficznych potrzeb.

4. **Integracja z systemami CMS** – Dodanie opcji eksportu wygenerowanego kodu HTML bezpośrednio do popularnych systemów CMS (np. WordPress) 
