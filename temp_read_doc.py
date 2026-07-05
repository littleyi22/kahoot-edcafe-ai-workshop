import sys
import io
from markitdown import MarkItDown

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

file_path = sys.argv[1]
md = MarkItDown()
result = md.convert(file_path)
print(result.text_content)
