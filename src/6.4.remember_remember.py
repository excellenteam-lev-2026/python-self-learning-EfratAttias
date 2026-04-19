from PIL import Image

def remember_remember(path):
    image = Image.open(path)
    width, height = image.size
    pixels = image.load()
    message = []
    for i in range(width):
        for j in range(height):
            if pixels[i, j] == (1): 
                message.append(chr(j))
                break
            
    return ''.join(message)
    
if __name__ == "__main__":
    print(remember_remember("resources\\code.png"))