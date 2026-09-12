"""Check generated HTML's local links, fragment targets and lesson structure."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
root=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__();self.ids=[];self.links=[];self.sections=0;self.questions=0;self.in_quiz=False;self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        for key in ('href','src'):
            if a.get(key):self.links.append(a[key])
        if tag=='section' and 'lesson-section' in a.get('class',''):self.sections+=1
        if tag=='section':self.in_quiz=a.get('id')=='test'
        if tag=='summary' and self.in_quiz:self.questions+=1
pages={p:Page(p.read_text(encoding='utf-8')) for p in [root/'index.html',*sorted((root/'weeks').glob('*.html'))]}
errors=[]
for path,page in pages.items():
    if len(page.ids)!=len(set(page.ids)):errors.append(f'Duplicate ID: {path}')
    for link in page.links:
        url=urlsplit(link)
        if url.scheme or url.netloc:continue
        target=(path.parent/unquote(url.path)).resolve() if url.path else path
        if not target.exists():errors.append(f'Broken link {path.name}: {link}')
        if url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:errors.append(f'Broken fragment {path.name}: {link}')
    if path.parent.name=='weeks':
        if page.questions!=5:errors.append(f'Expected 5 questions: {path.name}')
        if page.sections<10:errors.append(f'Missing lesson sections: {path.name}')
assert not errors,'\n'.join(errors)
assert len(pages)==3,'Only the first two weeks should be published.'
print(f'PASS: {len(pages)} pages; local links, anchors, unique IDs, sections and quizzes.')
