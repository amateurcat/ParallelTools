import io

def read_chunks(read_from, chunk_size):
    with open(read_from, 'r') as file:
        while True:
            chunk = ''.join([file.readline() for _ in range(chunk_size)])
            if not chunk:
                break
            string_io = io.StringIO(chunk)
            yield string_io