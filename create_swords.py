import os

# Danh sách các lá bài trong Nhóm Kiếm (Swords)
cards = [
    "Ace of Swords", "Two of Swords", "Three of Swords", "Four of Swords",
    "Five of Swords", "Six of Swords", "Seven of Swords", "Eight of Swords",
    "Nine of Swords", "Ten of Swords", "Page of Swords", "Knight of Swords",
    "Queen of Swords", "King of Swords"
]

# Thư mục chứa file .md
folder = "content/tarot/nhom-kiem"
os.makedirs(folder, exist_ok=True)

# Tạo từng file .md
for i, card in enumerate(cards, start=1):
    slug = card.lower().replace(" ", "-")
    filename = os.path.join(folder, f"{slug}.md")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"""+++
title = "Ý Nghĩa {card} Trong Tarot"
description = "Khám phá ý nghĩa lá {card} trong Tarot - thông điệp về cuộc sống, tình yêu và sự nghiệp."
keywords = ["{card}", "ý nghĩa lá bài Tarot", "Tarot cho người mới", "ý nghĩa {card}"]
slug = "{slug}"

[menu.main]
name = "{card}"
parent = "Nhóm Kiếm"
weight = {i}
+++

## Ý Nghĩa Lá {card} Trong Tarot

Lá **{card}** mang thông điệp đặc biệt trong hành trình Tarot.  
Tùy vào bối cảnh trải bài, ý nghĩa có thể khác nhau:

### Khi lá bài xuôi:
- Ý nghĩa tích cực  
- Cơ hội, thuận lợi  

### Khi lá bài ngược:
- Thách thức, cản trở  
- Cần xem xét lại kế hoạch  

---

## Liên quan:
- [Rút bài Tarot 3 lá](../../)
- [Ý nghĩa Nhóm Kiếm](../)
""")

print("✅ Đã tạo xong 14 file Nhóm Kiếm trong folder:", folder)
