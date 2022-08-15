from ast import Try
import os
from PIL import Image





def main():
    CURRENT_PATH = os.getcwd()+'\origen\\'
    FINISH_PATH = os.getcwd()+'\\finish\\'
    IMG_EXT = ".jpg"

    try:
        os.mkdir("finish")
    except:
        pass        

    all_files = os.listdir(CURRENT_PATH)

    imgList = list()

    
    for i in all_files:
        # print(f"Optimizando img => {i}")
        try:
            name = i
            image = Image.open(CURRENT_PATH+i)
            image = image.convert("RGB")

            base = os.path.splitext(i)[0]

            image.save(FINISH_PATH+base+'.webp', 'webp', quality=50)
        except:
            print(f"error img => {i}")

        

       
    

    print("¡Trabajo terminado!")


if __name__ == '__main__':
    main()