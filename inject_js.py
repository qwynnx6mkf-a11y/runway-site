import os
import re

base_dir = '/Users/cz/lo/100poj/website/ziyou'
html_files = [
    'index.html',
    'zh/index.html'
]

js_code = """
<script>
  document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
        }
      });
    }, { threshold: 0.1, rootMargin: "0px 0px -50px 0px" });

    document.querySelectorAll('.section-head, .feature, .story-panel, .quote-panel, .cta-panel').forEach((el) => {
      el.classList.add('reveal');
      observer.observe(el);
    });
  });
</script>
</body>
"""

for file_path in html_files:
    full_path = os.path.join(base_dir, file_path)
    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '<script>' not in content:
            content = content.replace('</body>', js_code)
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
        print(f"Updated {full_path}")
