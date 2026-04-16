import re

def parsle_tongue(path):
    msgs = re.compile(rb"[a-z]{5,}!")
    buffer = b""
    for chunks in read_bytes_in_chunks(path):
        buffer += chunks
        matches = msgs.findall(buffer)
        for m in matches:
            yield m.decode()
        buffer = buffer[-100:]
        

def read_bytes_in_chunks(file_path, chunk_size=1024):
    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

if __name__ == "__main__":
    for msg in parsle_tongue("resources\logo.jpg"):
        print(msg)
