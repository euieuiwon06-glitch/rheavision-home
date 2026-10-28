"""index.html = Credence 사이트 하단 섹션(ref/credence_index.html) + Frame 6 상단(top.html) 조립."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
src = (ROOT / "ref" / "credence_index.html").read_text(encoding="utf-8")
top = (ROOT / "src" / "top.html").read_text(encoding="utf-8")
extra = (ROOT / "src" / "extra.html").read_text(encoding="utf-8")
script = (ROOT / "src" / "script.html").read_text(encoding="utf-8")

head, rest = src.split("</head>", 1)
head = head.replace('"Inter"]', '"Inter","Noto Sans KR","sans-serif"]')
head = re.sub(r"<title>.*?</title>", "", head) + "<title>RHEA VISION</title>" + extra

body_open = re.search(r"<body[^>]*>", rest).group(0)
lower_start = rest.index('<section class="w-full py-24 bg-white border-y')
lower_end = rest.index("</div></main>")
lower = rest[lower_start:lower_end]
footer = rest[lower_end + len("</div></main>"):].replace("<footer ", '<footer id="footer" ', 1)

# 다른 페이지(courses.html 등)는 이 프로젝트에 없으므로 페이지 안 앵커로 연결
lower = re.sub(r'href="(courses|course-detail|b2b)\.html[^"]*"', 'href="#trending-courses"', lower)
footer = re.sub(r'href="(courses|course-detail|b2b)\.html[^"]*"', 'href="#trending-courses"', footer)

html = head + "</head>" + body_open + top + lower + "</div></main>" + footer.replace("</body>", script + "</body>")
(ROOT / "index.html").write_text(html, encoding="utf-8")
print("index.html", len(html))
