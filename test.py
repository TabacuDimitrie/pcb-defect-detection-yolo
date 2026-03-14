from ultralytics import YOLO


def test_model():
    """
    Functie simpla care verifica daca YOLO este instalat
    si poate incarca un model preantrenat.
    """

    print("Incarcam modelul YOLO...")

    # incarcam modelul nano
    model = YOLO("yolov8n.pt")

    print("Model incarcat cu succes!")

    # afisam informatii despre model
    print(model)


if __name__ == "__main__":
    test_model()