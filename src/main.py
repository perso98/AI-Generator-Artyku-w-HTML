from utils import read_file, save_file, insert_generated_html
from openai_integration import generate_html
import os

if __name__ == "__main__":
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    article_path = os.path.join(base_path, "data", "artykul.txt")
    output_path = os.path.join(base_path, "data", "output", "artykul.html")
    article_content = read_file(article_path)
    html_content = generate_html(article_content)
    template_path = os.path.join(base_path, "templates", "podglad.html")
    save_file(output_path, html_content)

    article_content = read_file(article_path)
    
    html_content = generate_html(article_content)
    
    save_file(output_path, html_content)
    
    insert_generated_html(template_path, html_content)
    
    print("HTML został wygenerowany i zapisany w", output_path)
    print("Podgląd został uaktualniony w", template_path)