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
        "\n- **Pierwszą grafikę** umieść **po głównym nagłówku <h1>** (tytuł artykułu)."
        "\n- **Kolejne grafiki** umieszczaj naturalnie między paragrafami, unikając nadmiaru grafik. Umieszczaj je co kilka paragrafów (np. co 2-3 paragrafy), aby harmonijnie wpasowywały się w treść."
        "\n- Zadbaj o to, aby każda grafika miała swoje logiczne miejsce w kontekście artykułu i była związana z treścią."
        "\n- Każdą grafikę umieść wewnątrz tagu <figure>."
        "\n- Użyj tagu <img> z atrybutem src='image_placeholder.jpg'."
        "\n- **Dodaj atrybut alt do każdego obrazka z dokładnym promptem, który możemy użyć do wygenerowania grafiki.** Opis powinien:"
        "\n  - Zaczynać się od 'wygeneruj grafikę w wysokiej rozdzielczości w stylu realistycznym...'."
        "\n  Być prosty, i **BARDZO PRECYZYJNY, koncentruj się na prostych obrazach z jednym głównym elementem.**"
        "\n  - Zawierać **3-4 zdania** opisujące obraz."
        "\n  - Być **szczegółowy i precyzyjny**"
        "\n  - Być związany z treścią artykułu i kontekstem miejsca, w którym jest umieszczony."
        "\n- **Umieść podpisy pod grafikami**, tworząc je na podstawie treści artykułu. Użyj tagu <figcaption> wewnątrz tagu <figure>, umieszczając go poniżej tagu <img>."
        "\n\n**Formatowanie treści:**"
        "\n- Używaj odpowiednich nagłówków (<h1>, <h2>, <h3>) do strukturyzacji artykułu."
        "\n**Dla kluczowych wyrażeń, terminów, oraz zdań stosuj kursywę (<em>) i pogrubienie (<strong>) zgodnie z poniższymi zasadami:**"
        "\n - Kursywę stosuj dla ważnych terminów, wyrażeń i krótkich fraz, aby zwrócić uwagę na istotne pojęcia w każdym akapicie."
        "\n - Pogrubienie stosuj dla **najważniejszych zdań** lub **kluczowych idei** w każdym akapicie, aby zwiększyć ich widoczność."
        "\n - We wstępie do artykułu oraz w pierwszym akapicie każdej sekcji dodawaj **pogrubienia dla kluczowych punktów** oraz **kursywę dla terminów specjalistycznych lub istotnych pojęć**."
        "\n **Używaj pasujących tagów HTML, takich jak <table> dla tabel, <blockquote> dla cytatów, i innych elementów struktury, aby formatowanie było zgodne z treścią.**"
        "\n- Jeśli w artykule są listy, sformatuj je za pomocą tagów <ul>/<ol> oraz <li>."
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