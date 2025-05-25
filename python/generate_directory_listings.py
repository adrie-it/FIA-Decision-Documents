import os
from pathlib import Path
from urllib.parse import quote

# Set the root directory here (relative or absolute path)
ROOT_DIR = '../'  # Change this to your desired root directory, e.g., '../' or '/workspaces/FIA-Decision-Documents'

def generate_index_html(dir_path, rel_path):
    entries = sorted(os.listdir(dir_path))
    html_lines = [
        '<!DOCTYPE html>',
        '<html lang="en">',
        '<head>',
        '  <meta charset="UTF-8">',
        f'  <title>Index of {rel_path}</title>',
        '''  <style>
        body { font-family: system-ui, sans-serif; background: #f8f9fa; color: #222; margin: 0; padding: 2em; }
        h2 { margin-top: 0; }
        ul { list-style: none; padding: 0; }
        li { margin: 0.2em 0; }
        a { text-decoration: none; color: #0074d9; padding: 0.2em 0.5em; border-radius: 3px; transition: background 0.2s; }
        a:hover { background: #e2e6ea; color: #005fa3; }
        .container { max-width: 600px; margin: auto; background: #fff; border-radius: 8px; box-shadow: 0 2px 8px #0001; padding: 2em; }
        </style>''',
        '</head>',
        '<body>',
        '  <div class="container">',
        f'    <h2>Index of {rel_path}</h2>',
        '    <ul>'
    ]
    # Add parent directory link if not at root
    if Path(rel_path) != Path('.'):
        html_lines.append('      <li><a href="../">../</a></li>')
    for entry in entries:
        if entry == 'index.html':
            continue
        full_path = os.path.join(dir_path, entry)
        display_name = entry + ('/' if os.path.isdir(full_path) else '')
        href = quote(entry) + ('/' if os.path.isdir(full_path) else '')
        html_lines.append(f'      <li><a href="{href}">{display_name}</a></li>')
    html_lines += ['    </ul>', '  </div>', '</body>', '</html>']
    return '\n'.join(html_lines)

def main():
    root_dir = os.path.abspath(ROOT_DIR)
    for current_root, dirs, files in os.walk(root_dir):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        rel_path = os.path.relpath(current_root, root_dir)
        rel_path = '.' if rel_path == '.' else rel_path
        index_path = os.path.join(current_root, 'index.html')
        html = generate_index_html(current_root, rel_path)
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(html)

if __name__ == '__main__':
    main()
