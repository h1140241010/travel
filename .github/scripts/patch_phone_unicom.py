from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

marker = '<details class="stop"><summary><div class="stop-icon">🏦</div><div><div class="stop-title">浦東機場 → 中國工商銀行（虹橋萬通中心支行）</div>'
if '浦東機場 T1 → T2 中國聯通｜辦門號' in s:
    raise SystemExit(0)
if marker not in s:
    raise SystemExit('Day 1 bank stop marker not found')

phone_stop = '''<details class="stop"><summary><div class="stop-icon">📱</div><div><div class="stop-title">浦東機場 T1 → T2 中國聯通｜辦門號</div><div class="stop-meta">入境、領完行李後｜步行前往 T2</div></div><div class="chev">⌄</div></summary><div class="stop-body"><p>抵達浦東機場 T1、完成入境並領完行李後，先步行前往 <b>T2 中國聯通</b> 辦理門號；辦完門號後再打車前往中國工商銀行（虹橋萬通中心支行）。</p><div class="alert">📱 <b>現場說法：</b><br>「我是台灣人！我這幾天來旅遊，我過幾天就要回去了，我之後只要留著收簡訊的功能就好，所以我等等我要改成保號方案，這個號碼第幾個月能改」</div><div class="pills"><span class="pill green">先辦門號</span><span class="pill">T1 → T2 步行</span><span class="pill gold">問清楚第幾個月能改保號方案</span></div></div></details>'''

s = s.replace(marker, phone_stop + marker, 1)
p.write_text(s, encoding='utf-8')
