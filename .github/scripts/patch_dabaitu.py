from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
note = '<div class="alert">🍬 爸爸任務｜記得幫爸爸買大白兔奶糖。</div>'
if note in s:
    raise SystemExit(0)

target_toptoy = '<div class="alert">🧸 TOP TOY｜朋友託買：記得去幫朋友買東西。</div>'
target_intro = '<p>傍晚開始慢慢逛、找晚餐，順便等夜景亮燈。</p>'

if target_toptoy in s:
    s = s.replace(target_toptoy, target_toptoy + note, 1)
elif target_intro in s:
    s = s.replace(target_intro, target_intro + note, 1)
else:
    raise SystemExit('Yuyuan target not found')

p.write_text(s, encoding='utf-8')
