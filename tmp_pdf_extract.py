from pathlib import Path
import PyPDF2
path = Path('NZ- presentation.pdf')
reader = PyPDF2.PdfReader(path)
print('pages', len(reader.pages))
for i, page in enumerate(reader.pages, 1):
    text = page.extract_text() or ''
    print('--- PAGE', i, '---')
    print(text[:3000])
