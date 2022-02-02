from pathlib import Path

path = Path('remove-it')
if path.exists:
    path.rmdir()
else:
    path.mkdir()

path = Path('hello-wrld')
for folder in path.glob('*'):
    print(folder)
