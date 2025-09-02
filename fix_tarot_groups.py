import os
from shutil import copyfile

base = "content/tarot"
os.makedirs(base, exist_ok=True)

files = {
    "nhom-chinh/_index.md": """+++
title = "Nhóm Chính (Major Arcana)"
slug = "nhom-chinh"

[menu.main]
  name = "Nhóm Chính"
  parent = "Tarot"
  weight = 1
+++

# Nhóm Chính (Major Arcana)

Đây là bộ 22 lá bài đại diện cho những bước ngoặt và bài học quan trọng trong hành trình cuộc sống.
""",

    "nhom-ly/_index.md": """+++
title = "Nhóm Ly (Cups)"
slug = "nhom-ly"

[menu.main]
  name = "Nhóm Ly"
  parent = "Tarot"
  weight = 2
+++

# Nhóm Ly (Cups)

Đại diện cho cảm xúc, tình cảm và các mối quan hệ.
""",

    "nhom-xu/_index.md": """+++
title = "Nhóm Xu (Pentacles / Coins)"
slug = "nhom-xu"

[menu.main]
  name = "Nhóm Xu"
  parent = "Tarot"
  weight = 3
+++

# Nhóm Xu (Pentacles / Coins)

Đại diện cho tiền bạc, sự nghiệp và yếu tố vật chất.
""",

    "nhom-gay/_index.md": """+++
title = "Nhóm Gậy (Wands)"
slug = "nhom-gay"

[menu.main]
  name = "Nhóm Gậy"
  parent = "Tarot"
  weight = 4
+++

# Nhóm Gậy (Wands)

Đại diện cho hành động, năng lượng và sự sáng tạo.
""",

    "nhom-kiem/_index.md": """+++
title = "Nhóm Kiếm (Swords)"
slug = "nhom-kiem"

[menu.main]
  name = "Nhóm Kiếm"
  parent = "Tarot"
  weight = 5
+++

# Nhóm Kiếm (Swords)

Đại diện cho trí tuệ, tư duy logic và thử thách tinh thần.
"""
}

# Ghi file (backup nếu file đã tồn tại)
for rel_path, content in files.items():
    full_path = os.path.join(base, rel_path)
    dirpath = os.path.dirname(full_path)
    os.makedirs(dirpath, exist_ok=True)

    if os.path.exists(full_path):
        bak = full_path + ".bak"
        copyfile(full_path, bak)
        print(f"Backup created: {bak}")

    # Viết với encoding utf-8 (không BOM)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Wrote:", full_path)

print("\n✅ Hoàn tất. Bây giờ chạy: hugo server -D và kiểm tra lại.")
