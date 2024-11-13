import openai
import os
from dotenv import load_dotenv

load_dotenv()  
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_html(article_content): 
    print("Generuje HTML proszę czekać...")
    messages = [
        {"role": "user", "content": (
            "Przetwórz poniższy artykuł do formatu HTML, używając odpowiednich tagów HTML do "
            "strukturyzacji treści. Proszę o zachowanie oryginalnego znaczenia i struktury artykułu bez dodawania własnych treści."
            "Masz wysłać kod html, który będzie w <body></body>"
            "\n\nProszę o zastosowanie następującego formatowania:"
            "\n- **Pogrubiaj** kluczowe terminy lub frazy istotne dla treści, używając tagu <strong>."
            "\n- Dodawaj **cytaty** lub wyróżnione fragmenty, jeśli występują w tekście, za pomocą tagu <blockquote>."
            "\n- W miejscach, gdzie warto umieścić grafiki związane z treścią, umieść je w środku tekstu pomiędzy paragrafami <p>, aby lepiej rozmieścić treść."
            "\n- **W sumie w artykule powinny znaleźć się cztery grafiki**, w tym pierwsza grafika na początku artykułu jako grafika wstępna, ma to być na samym początku i to ma byc tylko jedna grafika, nic nie ma być przed wstępną grafiką."
            "\n- **Upewnij się, że w każdej sekcji znajduje się tylko jedna grafika, i unikaj umieszczania dwóch grafik pod rząd lub dwóch grafik w jednej sekcji.**"
            "\n- Użyj tagu <img> z atrybutem src='image_placeholder.jpg' i w atrybucie alt umieść tekst zaczynający się od 'wygeneruj grafikę, która przedstawia...' i dalej dokładnie opisz, co ma być na obrazku, w dwóch zdaniach."
            "\n- **Umieść podpisy pod grafikami używając odpowiedniego tagu HTML**, na przykład tagu <figcaption> wewnątrz tagu <figure>, który obejmuje zarówno obrazek, jak i podpis."
            "\n- Dodaj dodatkowe tagi HTML, aby tekst był bardziej dynamiczny, np. użyj <em> do podkreślenia, <span> i inne."
            "\n- Używaj odpowiednich tagów nagłówków (<h1>, <h2>, <h3>) do strukturyzacji sekcji artykułu."
            "\n- Jeśli w artykule występują listy, sformatuj je używając tagów <ul> lub <ol> oraz <li>."
            "\n- Upewnij się, że kod HTML jest poprawny i wolny od błędów składniowych. Prawidłowo koduj znaki specjalne."
            "\n- Nie używaj znaczników <body> i </body>. Prześlij tylko zawartość wewnątrz tych znaczników."
            "\n- Nie dodawaj żadnych dodatkowych treści ani komentarzy, które nie są zawarte w oryginalnym artykule."
            f"\n\nArtykuł:\n{article_content}"
        )}
    ]

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=messages,
        max_tokens=3000,
        temperature=0.5,
    )
    return response.choices[0].message.content.strip()