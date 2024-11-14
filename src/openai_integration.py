import openai
import os
from dotenv import load_dotenv

# Wczytanie danych z pliku .env, aby uzyskać klucz API
load_dotenv()  
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_html(article_content): 
    print("Generuje HTML proszę czekać...")
    # Definicja promptu do API OpenAI
    messages = [
    {"role": "user", "content": (
        "Przetwórz poniższy artykuł do formatu HTML, używając odpowiednich tagów do strukturyzacji treści. "
        "Zachowaj oryginalne znaczenie i strukturę artykułu bez dodawania własnych treści. "
        "Prześlij tylko kod HTML zawartości między znacznikami <body> i </body>, ale nie dołączaj samych znaczników <body> i </body>."
        "\n\nProszę o zastosowanie następującego formatowania:"
        "\n\n**Grafiki:**"
        "\n- Umieść grafiki w artykule, zrób ich tyle ile jest podnagłówków + dodatkowo nagłówek główny, jeśli treść jest zbyt krótka a nagłówki często to nie rób za dużo grafik."
        "\n- **Pierwszą grafikę** umieść **po głównym nagłówku** (tytuł artykułu)."
        "\n- **Pozostałe grafiki** umieść w odpowiednich miejscach **wewnątrz treści** **ALE NIE OD RAZU PO NAGŁÓWKACH**,"
        "\n- Upewnij się, że grafiki są osadzone **W ŚRODKU AKAPITU LUB MIĘDZY NIMI**, aby naturalnie wpasowywały się w treść."
        "\n- Unikaj umieszczania dwóch grafik pod rząd."
        "\n- Każdą grafikę umieść wewnątrz tagu <figure>."
        "\n- Użyj tagu <img> z atrybutem src='image_placeholder.jpg'."
        "\n- **Dodaj atrybut alt do każdego obrazka z dokładnym promptem, który możemy użyć do wygenerowania grafiki.** Opis powinien:"
        "\n  - Zaczynać się od 'wygeneruj grafikę w stylu realistycznym...'."
        "\n  Być prosty, i **BARDZO PRECYZYJNY**"
        "\n  - Zawierać **3-4 zdania** opisujące obraz."
        "\n  - Być **szczegółowy i precyzyjny**, aby ułatwić wygenerowanie grafiki przez AI."
        "\n  - Być związany z treścią artykułu i kontekstem miejsca, w którym jest umieszczony."
        "\n- **Umieść podpisy pod grafikami**, tworząc je na podstawie treści artykułu. Użyj tagu <figcaption> wewnątrz tagu <figure>, umieszczając go poniżej tagu <img>."
        "\n\n**Formatowanie treści:**"
        "\n- Używaj odpowiednich nagłówków (<h1>, <h2>, <h3>) do strukturyzacji artykułu."
        "\n  **UŻYWAJ W KAŻDYM AKAPICIE KURSYW <em> I POGRUBIEŃ <strong>,  aby treść była bardziej dynamiczna i przejrzysta. Kursywę stosuj do wprowadzenia subtelnego nacisku, a pogrubienie do wyraźnego wyróżnienia kluczowych idei i informacji." 
        "Dzięki temu czytelnik łatwiej odnajdzie najważniejsze elementy tekstu.**."
        "\n **Używaj pasujących tagów html np. dla tabeli i tak dalej.**"
        "\n- **Nie umieszczaj grafik bezpośrednio po nagłówkach.** Zawsze wstaw co najmniej jeden akapit tekstu po nagłówku, zanim umieścisz grafikę."
        "\n- Jeśli w artykule są listy, sformatuj je za pomocą tagów <ul>/<ol> oraz <li>."
        "\n- Jeśli w tekście występują cytaty lub wyróżnione fragmenty, sformatuj je za pomocą tagu <blockquote>."
        "\n- Możesz używać dowolnych znaczników HTML, aby tekst był bardziej dynamiczny."
        "\n\n**Ważne uwagi:**"
        "\n- **Nie dołączaj żadnych stylów CSS ani JavaScriptu.** Używaj wyłącznie czystego HTML."
        "\n- Upewnij się, że kod HTML jest poprawny i wolny od błędów składniowych."
        "\n- Nie dodawaj żadnych treści ani komentarzy spoza oryginalnego artykułu."
        f"\n\nArtykuł:\n{article_content}"
    )}
]

 # Wykonanie wywołania do API OpenAI
    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=messages,
            max_tokens=4096,
            temperature=0.3,
        )
        # Zwrócenie wygenerowanej zawartośi HTML
        return response.choices[0].message.content.strip()
    except Exception as e:
        # Ogólna obsługa błędów związanych z API
        print(f"Wystąpił błąd podczas wywołania API OpenAI: {e}")
        return None