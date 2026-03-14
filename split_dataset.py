import random
import shutil
from pathlib import Path

TRAIN_IMAGES = Path("data/images/train")
TRAIN_LABELS = Path("data/labels/train")

VAL_IMAGES = Path("data/images/val")
VAL_LABELS = Path("data/labels/val")

VAL_IMAGES.mkdir(parents=True, exist_ok=True)
VAL_LABELS.mkdir(parents=True, exist_ok=True)


def main():
    image_files = list(TRAIN_IMAGES.glob("*.jpg"))

    print(f"Gasite {len(image_files)} imagini in train.")

    if len(image_files) == 0:
        print("Nu exista imagini in data/images/train.")
        return

    random.shuffle(image_files)

    val_count = int(len(image_files) * 0.2)
    val_files = image_files[:val_count]

    moved = 0

    for img_path in val_files:
        label_path = TRAIN_LABELS / f"{img_path.stem}.txt"

        if not label_path.exists():
            print(f"Lipseste label pentru {img_path.name}, sar peste.")
            continue

        shutil.move(str(img_path), str(VAL_IMAGES / img_path.name))
        shutil.move(str(label_path), str(VAL_LABELS / label_path.name))
        moved += 1

    print(f"Mutate {moved} imagini in validation set.")


if __name__ == "__main__":
    main()
