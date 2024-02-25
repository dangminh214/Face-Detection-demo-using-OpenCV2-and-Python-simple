import cv2
import tkinter as tk
from tkinter import filedialog, messagebox

image = None

def choose_image():
    global image  # using image as global
    # open dialog to choose image
    file_path = filedialog.askopenfilename()

    # Kiểm tra xem người dùng đã chọn một tệp ảnh hay không
    if file_path:
        # Đọc ảnh từ tệp đã chọn
        image = cv2.imread(file_path)
        height, width, _ = image.shape
        if (height < 800 and width < 800):
            new_width = int(width * 1.5)
            new_height = int(height * 1.5)
        elif (height > 1000 and width > 1000):
            new_width = int(width * 0.5)
            new_height = int(height * 0.5)
        else: 
            new_width = width
            new_height = height

        image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
        print('width: ', new_width, 'heigth: ', new_height)
        print('path: ', file_path)
        face_detect(image)

    else:
        print("Không có tệp nào được chọn.")
        show_popup('Fail', 'Không có tệp nào được chọn.')
        root.quit()
        return None
     

def show_popup(title, content):
    # show the pop up
    messagebox.showinfo(title, content)

def face_detect(image): 
    # create a face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # turn original image to gray
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # face detection and recognize
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

    # draw face detection
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow('Detected Faces Result', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()  

root = tk.Tk()
root.withdraw()  # Ẩn cửa sổ chính
root.geometry("800x600")

# Hiển thị cửa sổ pop-up thông báo
show_popup("Cẩn thận", "Ảnh không được chưa dấu tiếng Việt")
choose_image()

# Hiển thị cửa sổ giao diện chính và chờ người dùng tương tác
root.mainloop()



