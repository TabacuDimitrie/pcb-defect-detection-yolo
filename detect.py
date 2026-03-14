from ultralytics import YOLO

def main():

    model = YOLO("runs/detect/train4/weights/best.pt")

    results = model.predict(
    source="data/images/val",
    save=True,
    conf=0.05
)
if __name__ == "__main__":
    main()
