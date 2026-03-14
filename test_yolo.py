from ultralytics import YOLO

def test_model():
    print("incarcare model")
    model = YOLO("yolov8n.pt")
    print("testare model")
    print(model)

if __name__ == "__main__":
    test_model()