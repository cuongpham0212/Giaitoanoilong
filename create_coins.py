import os

# Danh sách các lá bài trong Nhóm Coins
cards = [
    "Ace of Coins", "Two of Coins", "Three of Coins", "Four of Coins",
    "Five of Coins", "Six of Coins", "Seven of Coins", "Eight of Coins",
    "Nine of Coins", "Ten of Coins", "Page of Coins", "Knight of Coins",
    "Queen of Coins", "King of Coins"
]

# Thư mục chứa file .md
folder = "content/tarot/nhom-xu"
os.makedirs(folder, exist_ok=True)

# Tạo từng file .md
for card in cards:
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
parent = "Nhóm Xu"
weight = 3
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
- [Ý nghĩa Nhóm Coins](../)
""")

print("✅ Đã tạo xong 14 file .md trong folder:", folder)
