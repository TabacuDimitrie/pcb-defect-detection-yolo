import shutil
from pathlib import Path
from PIL import Image

DATASET_ROOT = Path("data/raw/DeepPCB/PCBData")

TRAIN_IMAGES = Path("data/images/train")
TRAIN_LABELS = Path("data/labels/train")

TRAIN_IMAGES.mkdir(parents=True, exist_ok=True)
TRAIN_LABELS.mkdir(parents=True, exist_ok=True)


def convert_bbox(img_w, img_h, x1, y1, x2, y2):

    x_center = (x1 + x2) / 2
    y_center = (y1 + y2) / 2

    width = x2 - x1
    height = y2 - y1

    x_center /= img_w
    y_center /= img_h
    width /= img_w
    height /= img_h

    return x_center, y_center, width, height


def process_group(group_path, counter):

    image_folder = None
    annotation_folder = None

    for sub in group_path.iterdir():

        if sub.name.endswith("_not"):
            annotation_folder = sub
        else:
            image_folder = sub

    if image_folder is None or annotation_folder is None:
        return counter

    for img_path in image_folder.glob("*.jpg"):

        base_name = img_path.stem.replace("_temp", "")

        annotation_path = annotation_folder / (base_name + ".txt")

        if not annotation_path.exists():
            continue

        image = Image.open(img_path)
        img_w, img_h = image.size

        new_name = f"pcb_{counter:06d}.jpg"

        shutil.copy(img_path, TRAIN_IMAGES / new_name)

        yolo_lines = []

        with open(annotation_path) as f:

            for line in f:

                x1, y1, x2, y2, cls = map(int, line.split())

                x_center, y_center, w, h = convert_bbox(
                    img_w, img_h, x1, y1, x2, y2
                )

                yolo_lines.append(
                    f"{cls} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}"
                )

        label_path = TRAIN_LABELS / new_name.replace(".jpg", ".txt")

        with open(label_path, "w") as f:
            f.write("\n".join(yolo_lines))

        counter += 1

    return counter


def main():

    counter = 0

    for group in DATASET_ROOT.iterdir():

        if not group.is_dir():
            continue

        counter = process_group(group, counter)

    print(f"Dataset creat cu {counter} imagini.")


if __name__ == "__main__":
    main()
