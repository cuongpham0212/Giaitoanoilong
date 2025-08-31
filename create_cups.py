import os

# Danh sách các lá bài trong Nhóm Ly
cards = [
    "Ace of Cups", "Two of Cups", "Three of Cups", "Four of Cups",
    "Five of Cups", "Six of Cups", "Seven of Cups", "Eight of Cups",
    "Nine of Cups", "Ten of Cups", "Page of Cups", "Knight of Cups",
    "Queen of Cups", "King of Cups"
]

# Thư mục chứa file .md
folder = "content/tarot/nhom-ly"
os.makedirs(folder, exist_ok=True)

# Tạo từng file .md
for card in cards:
    slug = card.lower().replace(" ", "-")
    filename = f"{folder}/{slug}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"""+++
title = "Ý Nghĩa {card} Trong Tarot"
description = "Khám phá ý nghĩa lá {card} trong Tarot - thông điệp về cuộc sống, tình yêu và sự nghiệp."
keywords = ["{card}", "ý nghĩa lá bài Tarot", "Tarot cho người mới", "ý nghĩa {card}"]
slug = "{slug}"

[menu.main]
name = "{card}"
parent = "Nhóm Ly"
weight = 2
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
- [Ý nghĩa Nhóm Ly](../)
""")

print("✅ Đã tạo xong 14 file .md trong folder:", folder)