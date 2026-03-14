from pathlib import Path

LABELS_DIR = Path("data/labels/train")

def main():
    classes = set()
    
    for txt_file in LABELS_DIR.glob("*.txt"):
        with open(txt_file, "r") as f:
            for line in f:
                parts = line.split()
                if parts:
                    classes.add(parts[0])
                    
    print("Clase gasite" , sorted(classes))
    
if __name__ == "__main__":
    main()