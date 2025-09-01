import os

# Danh sách các lá bài trong Major Arcana
cards = [
    "The Fool", "The Magician", "The High Priestess", "The Empress",
    "The Emperor", "The Hierophant", "The Lovers", "The Chariot",
    "Strength", "The Hermit", "Wheel of Fortune", "Justice",
    "The Hanged Man", "Death", "Temperance", "The Devil",
    "The Tower", "The Star", "The Moon", "The Sun",
    "Judgement", "The World"
]

# Thư mục chứa file .md
folder = "content/tarot/major-arcana"
os.makedirs(folder, exist_ok=True)

# Tạo từng file .md
for i, card in enumerate(cards, start=0):
    slug = card.lower().replace(" ", "-")
    filename = f"{folder}/{slug}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"""+++
title = "Ý Nghĩa {card} Trong Tarot"
description = "Khám phá ý nghĩa lá {card} thuộc Major Arcana trong Tarot – mang thông điệp sâu sắc về hành trình cuộc đời."
keywords = ["{card}", "ý nghĩa lá bài Tarot", "Major Arcana", "ý nghĩa {card}"]
slug = "{slug}"

[menu.main]
name = "{card}"
parent = "Major Arcana"
weight = {i+1}
+++

## Ý Nghĩa Lá {card} (Major Arcana)

Lá **{card}** là một trong những lá quan trọng của bộ Ẩn Chính (Major Arcana).  
Nó phản ánh những bài học lớn, bước ngoặt và trải nghiệm sâu sắc trong cuộc sống.

### Khi lá bài xuôi:
- Ý nghĩa tích cực  
- Cơ hội, bài học mới  

### Khi lá bài ngược:
- Thách thức, trì hoãn  
- Cần nhìn lại hành trình hiện tại  

---
""")

print("✅ Đã tạo xong 22 file .md trong folder:", folder)
