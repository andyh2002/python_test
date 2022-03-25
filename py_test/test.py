#! usr/bin/env python
from pathlib import Path

p = Path('spam.txt')
p.write_text("Hello, World!", encoding='utf-8')
p.write_text("你好！", encoding='utf-8')
print(p.read_text(encoding='utf-8'))

