import os

cards = [
    "Ace of Pentacles", "Two of Pentacles", "Three of Pentacles", "Four of Pentacles",
    "Five of Pentacles", "Six of Pentacles", "Seven of Pentacles", "Eight of Pentacles",
    "Nine of Pentacles", "Ten of Pentacles", "Page of Pentacles", "Knight of Pentacles",
    "Queen of Pentacles", "King of Pentacles"
]

folder = "content/tarot/nhom-xu"
os.makedirs(folder, exist_ok=True)

for card in cards:
    slug = card.lower().replace(" ", "-")
    filename = f"{folder}/{slug}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"""+++
title = "Ý Nghĩa {card} Trong Tarot"
description = "Ý nghĩa lá {card} trong Nhóm Xu (Pentacles) – đại diện cho vật chất, tài chính và sự ổn định."
keywords = ["{card}", "ý nghĩa lá bài Tarot", "Pentacles", "ý nghĩa {card}"]
slug = "{slug}"

[menu.main]
name = "{card}"
parent = "Nhóm Xu"
weight = 2
+++

## Ý Nghĩa Lá {card} Trong Tarot (Nhóm Xu)

Lá **{card}** thuộc nhóm Xu, mang thông điệp về tiền bạc, sự nghiệp và giá trị vật chất.  

### Khi lá bài xuôi:
- Cơ hội tài chính, thành công vật chất  
- Ổn định, nền tảng vững chắc  

### Khi lá bài ngược:
- Khó khăn tài chính  
- Mất cân bằng trong chi tiêu  

---
""")

print("✅ Đã tạo xong 14 file .md trong folder:", folder)
