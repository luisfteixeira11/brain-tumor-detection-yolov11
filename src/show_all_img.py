import cv2
import glob
import numpy as np

# take the path of all .jpg
caminhos_img = glob.glob(r"brain-tumor-detection-yolov11\data\train\images\*.jpg")
caminhos_txt = glob.glob(r"brain-tumor-detection-yolov11\data\train\labels\*.txt")

def read_label(path):
    """
    Read a label from specified file path

    Args: path(str) - the path of file
    Returns: 
    - label(list of str) - the list of label of the image path
    - a error
    """
    # the try is a secure form to realize the open, can raise a error
    try:
        # the with function already close the open without file.close()
        with open(path, "r") as file:
            # read the first line of file
            row = file.readline()

            # splits the row per space key and take it, that be the label
            # i change that, i was taken only the class, but now, is all the line splited. 
            label = row.split()
        return label
    
    except Exception as error:
        return f"Error: {error}"

# function to show the image
def mostrar_imagem(caminho_img, caminho_txt):
    image = cv2.imread(caminho_img)
    label_numbers = read_label(caminho_txt)

    # here is a possible exeption
    if image is None or not label_numbers:
        print("Error: unable to read")

    class_id = label_numbers[0]
    # the variable '_' is color channels 
    high, weight, _ = image.shape

    # to show it, you need desnormalize the points of .txt, you need to put in a numpy array, because it's the form that cv2 aceppt
    pixel = []
    for i in range(1, len(label_numbers), 2):
        # transforming a string in a float
        x_normalized = float(label_numbers[i])
        y_normalized = float(label_numbers[i+1])

        # its tranformed by int because a pixel is a int number
        x_pixel = int(x_normalized * weight)
        y_pixel = int(y_normalized * high)

        pixel.append([x_pixel, y_pixel])

    # i saw that np.int32 will be necessary
    pixel_points_array = np.array(pixel, dtype=np.int32)
    # the cv2 accepts only a tridimensional matrix to do the polylines
    # -1 -> num of rows auto
    # 1 -> extra dimension
    # 2 -> num of columns
    pixel_points_array = pixel_points_array.reshape((-1, 1, 2))

    # i don't understand why the pixel_points have to be in a list if i already reshaped this, but ok
    cv2.polylines(image, [pixel_points_array], isClosed=True, color=(0, 255, 0), thickness=2)

    x, y, w, h = cv2.boundingRect(pixel_points_array)

    cv2.putText(image, class_id, (x, (y+h)), cv2.FONT_ITALIC, 0.6, (0, 255, 0), 2)

    cv2.imshow("Imagens", image)
    cv2.waitKey(0) 

# apply the function in every path of path's list
list(map(mostrar_imagem, caminhos_img, caminhos_txt))

cv2.destroyAllWindows()