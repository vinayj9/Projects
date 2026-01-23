def read_file():
    while True:
        try:
            filename=input('Enter file name:')
            with open(filename) as f:
                text=f.read()
                if not text.strip():
                    print('File is empty')
                    return None
            return text
        except FileNotFoundError:
            print('File not found')