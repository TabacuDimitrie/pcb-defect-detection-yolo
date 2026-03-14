from pathlib import Path

LABELS_DIR = [
    Path("data/labels/train"),
    Path("data/labels/val")
]

CLASS_MAP = {
    1: 0,
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5
}


def remap_file(txt_path):
    new_lines = []

    with open(txt_path, "r") as f:
        for line in f:
            parts = line.strip().split()

            if not parts:
                continue

            old_class = int(parts[0])

            # daca fisierul e deja remapat, ramane lfl
            if old_class in [0, 1, 2, 3, 4, 5]:
                new_class = old_class
            else:
                new_class = CLASS_MAP[old_class]

            new_line = " ".join([str(new_class)] + parts[1:])
            new_lines.append(new_line)

    with open(txt_path, "w") as f:
        f.write("\n".join(new_lines))


def main():
    total_files = 0

    for label_dir in LABELS_DIR:
        for txt_file in label_dir.glob("*.txt"):
            remap_file(txt_file)
            total_files += 1

    print(f"Remap facut pentru {total_files} fisiere.")


if __name__ == "__main__":
    main()
