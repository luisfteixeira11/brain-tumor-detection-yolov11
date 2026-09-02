import cv2

PATH_IMAGE = r"brain-tumor-detection-yolov11\data\train\images\1_jpg.rf.eee6547c09d13001fff4a45c380115aa.jpg"
PATH_TXT = r"brain-tumor-detection-yolov11\data\train\labels\1_jpg.rf.eee6547c09d13001fff4a45c380115aa.txt"

def load_image(path):
    """
    read a image from specified file path
    
    Args: path(str) - the path of file
    Returns: None
    """
    # a command that can read the image of path (have the parameter flags, but it's optional)
    image = cv2.imread(path)

    if image is None:
        print("Error: unable to read")

    # a function that can show the display a image 
    cv2.imshow("window", image)

    # a function that wait for a key press to close the window, if you put a number like 5000(ms) the window will keep 5 seconds open to close.
    cv2.waitKey(0)
    #obs: the destroyWindow() exists too
    cv2.destroyAllWindows()

def read_label(path):
    """
    Read a label from specified file path

    Args: path(str) - the path of file
    Returns: label(str) - the label of the image of path
    """
    # the try is a secure form to realize the open, can raise a error
    try:
        # the with function already close the open without file.close()
        with open(path, "r") as file:
            # read the first line of file
            row = file.readline()
            # splits the row per space key and take the first, that be the label
            label = row.split()[0]
        return label
    except Exception as error:
        return f"Error: {error}"

load_image(PATH_IMAGE)
print(read_label(PATH_TXT))