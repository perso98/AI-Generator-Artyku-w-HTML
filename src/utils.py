import re
def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        print(f'Czytam plik {filepath}')
        return file.read()

def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as file:
        print(f'Zapisuje plik {filepath}')
        file.write(content)
        
def insert_generated_html(template_path, generated_content):
    template_content = read_file(template_path)
    
    start_marker = "<!-- GENERATED_CONTENT_START -->"
    end_marker = "<!-- GENERATED_CONTENT_END -->"
    
    if start_marker in template_content and end_marker in template_content:
        template_content = re.sub(
            f"{start_marker}.*?{end_marker}",
            f"{start_marker}\n{generated_content}\n{end_marker}",
            template_content,
            flags=re.DOTALL
        )
    else:
        body_tag = "<body>"
        template_content = template_content.replace(
            body_tag,
            f"{body_tag}\n{start_marker}\n{generated_content}\n{end_marker}"
        )
        
    save_file(template_path, template_content)