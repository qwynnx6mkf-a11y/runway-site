import os
import re

base_dir = '/Users/cz/lo/100poj/website/ziyou'
html_files = [
    'privacy/index.html',
    'zh/privacy/index.html',
    'terms/index.html',
    'zh/terms/index.html',
    'support/index.html',
    'zh/support/index.html',
    'privacy-choices/index.html',
    'zh/privacy-choices/index.html'
]

font_links = """  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
"""

bg_glows = """  <div class="bg-glow-1"></div>
  <div class="bg-glow-2"></div>
"""

def update_html(file_path):
    full_path = os.path.join(base_dir, file_path)
    if not os.path.exists(full_path):
        return
    
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add fonts if missing
    if 'fonts.googleapis.com' not in content:
        content = content.replace('<link rel="stylesheet"', font_links + '  <link rel="stylesheet"')

    # Add glows if missing
    if 'bg-glow-1' not in content:
        content = re.sub(r'(<body[^>]*>)', r'\1\n' + bg_glows, content)

    # Simplified header/footer logic could be added here if needed
    # For now, let's keep it simple as the CSS handles the main look.

    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)

for f in html_files:
    update_html(f)
