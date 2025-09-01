import os

cards = [
    "Ace of Swords", "Two of Swords", "Three of Swords", "Four of Swords",
    "Five of Swords", "Six of Swords", "Seven of Swords", "Eight of Swords",
    "Nine of Swords", "Ten of Swords", "Page of Swords", "Knight of Swords",
    "Queen of Swords", "King of Swords"
]

folder = "content/tarot/nhom-kiem"
os.makedirs(folder, exist_ok=True)

for card in cards:
    slug = card.lower().replace(" ", "-")
    filename = f"{folder}/{slug}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"""+++
title = "Ý Nghĩa {card} Trong Tarot"
description = "Ý nghĩa lá {card} trong Nhóm Kiếm (Swords) – đại diện cho trí tuệ, thử thách và sự thật."
keywords = ["{card}", "ý nghĩa lá bài Tarot", "Swords", "ý nghĩa {card}"]
slug = "{slug}"

[menu.main]
name = "{card}"
parent = "Nhóm Kiếm"
weight = 2
+++

## Ý Nghĩa Lá {card} Trong Tarot (Nhóm Kiếm)

Lá **{card}** thuộc nhóm Kiếm, biểu trưng cho trí tuệ, xung đột và thử thách trong cuộc sống.  

### Khi lá bài xuôi:
- Lý trí, sự thật được soi sáng  
- Vượt qua thử thách bằng tư duy  

### Khi lá bài ngược:
- Bế tắc, lo âu  
- Sự thật bị che giấu  

---
""")

print("✅ Đã tạo xong 14 file .md trong folder:", folder)
