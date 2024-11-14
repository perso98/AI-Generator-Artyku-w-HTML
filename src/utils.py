import re

def read_file(filepath):
    """Funkcja odczytuje zawartość pliku z podanej ścieżki."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            print(f'Czytam plik {filepath}')
            return file.read()
    except FileNotFoundError:
        print(f"Plik {filepath} nie został znaleziony.")
        return None
    except IOError as e:
        print(f"Błąd wejścia/wyjścia podczas odczytu pliku {filepath}: {e}")
        return None
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd podczas odczytu pliku {filepath}: {e}")
        return None

def save_file(filepath, content):
    """Fukcja zapisuje podaną zawartość do pliku na podanej ścieżce."""
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            print(f'Zapisuje plik {filepath}')
            file.write(content)
    except IOError as e:
        print(f"Błąd wejścia/wyjścia podczas zapisu pliku {filepath}: {e}")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd podczas zapisu pliku {filepath}: {e}")

def insert_generated_html(template_path, generated_content):
    """Funkcja wstawia wygenerowaną treść HTML do szablonu w wyznaczonym miejscu."""
    try:
        # Wczytaj zawartość szablonu
        template_content = read_file(template_path)
        
        if template_content is None:
            print("Błąd: Nie udało się wczytać zawartości szablonu.")
            return

        # Znaczniki początkowy i końcowy wygenerowanej treści
        start_marker = "<!-- GENERATED_CONTENT_START -->"
        end_marker = "<!-- GENERATED_CONTENT_END -->"
        
        # Sprawdzenie, czy znaczniki istnieją w szablonie, aby zastąpić istniejącą treść
        if start_marker in template_content and end_marker in template_content:
            template_content = re.sub(
                f"{start_marker}.*?{end_marker}",
                f"{start_marker}\n{generated_content}\n{end_marker}",
                template_content,
                flags=re.DOTALL
            )
        else:
            # Jeśli znaczniki nie istnieją, wstaw wygenerowaną treść do sekcji <body>
            body_tag = "<body>"
            template_content = template_content.replace(
                body_tag,
                f"{body_tag}\n{start_marker}\n{generated_content}\n{end_marker}"
            )
        
        # Zapisz zmodyfikowany szablon
        save_file(template_path, template_content)
        
    except re.error as e:
        print(f"Błąd wyrażenia regularnego podczas modyfikacji zawartości szablonu: {e}")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd podczas wstawiania wygenerowanej treści HTML: {e}")
