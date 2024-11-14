from utils import read_file, save_file, insert_generated_html
from openai_integration import generate_html
import os

if __name__ == "__main__":
    try:
        # Ustalenie ścieżki do plików
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        article_path = os.path.join(base_path, "data", "artykul.txt")
        output_path = os.path.join(base_path, "data", "output", "artykul.html")
        template_path = os.path.join(base_path, "templates", "podglad.html")

        # Odczytanie zawartości artykułu z pliku
        try:
            article_content = read_file(article_path)
        except FileNotFoundError:
            print(f"Plik {article_path} nie został znaleziony.")
            article_content = None
        except Exception as e:
            print(f"Błąd podczas odczytu pliku artykułu: {e}")
            article_content = None

        if article_content:
            # Wygenerowanie HTML przy użyciu API OpenAI
            try:
                html_content = generate_html(article_content)
            except Exception as e:
                print(f"Błąd podczas generowania HTML: {e}")
                html_content = None

            if html_content:
                # Zapisanie wygenerowanego HTML do pliku
                try:
                    save_file(output_path, html_content)
                except Exception as e:
                    print(f"Błąd podczas zapisywania pliku HTML: {e}")

                # Zaktualizowanie podglądu, wstawiając wygenerowany HTML
                try:
                    insert_generated_html(template_path, html_content)
                except Exception as e:
                    print(f"Błąd podczas aktualizacji podglądu: {e}")

                # Potwierdzenie zakończenia procesu
                print("HTML został wygenerowany i zapisany w", output_path)
                print("Podgląd został uaktualniony w", template_path)
            else:
                print("Nie udało się wygenerować zawartości HTML.")
        else:
            print("Nie udało się odczytać zawartości artykułu.")

    except Exception as e:
        # Ogólny wyjątek w przypadku nieprzewidzianych błędów
        print(f"Wystąpił nieoczekiwany błąd: {e}")