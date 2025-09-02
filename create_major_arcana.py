import os

# Danh sách 22 lá bài Major Arcana
major_arcana = [
    "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
    "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
    "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
    "The Devil", "The Tower", "The Star", "The Moon", "The Sun",
    "Judgement", "The World"
]

# Thư mục chứa file .md
folder = "content/tarot/nhom-chinh"
os.makedirs(folder, exist_ok=True)

# Tạo từng file .md
for i, card in enumerate(major_arcana, start=1):
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
parent = "Nhóm Chính"
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
- [Ý nghĩa Major Arcana](../)
""")

print("✅ Đã tạo xong 22 file Major Arcana trong folder:", folder)
