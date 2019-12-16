from pathlib import Path


path=Path();

for d in path.glob('*'):
    print(d)
    for c in path.glob(f"{d}\*"):
        print(f">>{c}")
