import glob

def thats_the_way(path):
    files = glob.glob(f"{path}/deep*")
    print(files)

if __name__ == "__main__":
    thats_the_way("/images")
