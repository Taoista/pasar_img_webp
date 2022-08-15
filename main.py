from ast import Try
import os
from PIL import Image



def main():
    # * GET PATH
    CURRENT_PATH = os.getcwd()+'\origen\\'
    FINISH_PATH = os.getcwd()+'\\finish\\'
    QUALITY = 50

    # * CREATE FOLDER IF NOT EXISTS
    try:
        os.mkdir("finish")
        os.mkdir("origen")
    except:
        pass        

    all_files = os.listdir(CURRENT_PATH)

    for i in all_files:
        try:
            image = Image.open(CURRENT_PATH+i)
            image = image.convert("RGB")

            base = os.path.splitext(i)[0]

            image.save(FINISH_PATH+base+'.webp', 'webp', quality=QUALITY)
        except:
            print(f"error img => {i}")


    print("¡Trabajo terminado!")


if __name__ == '__main__':
    main()