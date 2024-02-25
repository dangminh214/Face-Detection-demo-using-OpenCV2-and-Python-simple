import tkinter as tk
from tkinter import filedialog, messagebox
import cv2

def choose_image():
    # Hiển thị hộp thoại để chọn tệp ảnh
    file_path = filedialog.askopenfilename()

    # Kiểm tra xem người dùng đã chọn một tệp ảnh hay không
    if file_path:
        # Đọc ảnh từ tệp đã chọn
        image = cv2.imread(file_path)
        height, width, _ = image.shape
        if (int(image.shape[0]) < 800 and int(image.shape[0]<800)):
            new_width = int(image.shape[1] * 1.5)
            new_height = int(image.shape[0] * 1.5)
        if (int(image.shape[0]) > 1000 and int(image.shape[0]>1000)):
            new_width = int(image.shape[1] * 0.5)
            new_height = int(image.shape[0] * 0.5)
        else: 
            new_width = width
            new_height = height

        image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
        print('width: ', new_width, 'heigth: ', new_height)

        # Hiển thị ảnh
        cv2.imshow('Selected Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Không có tệp nào được chọn.")

def show_popup():
    # Hiển thị cửa sổ pop-up thông báo
    messagebox.showinfo("Cẩn thận", "Ảnh không được chưa dấu tiếng Việt")
    
    # Tiếp tục chọn ảnh từ máy tính
    choose_image()    

# Tạo một cửa sổ giao diện tkinter mới
root = tk.Tk()
root.withdraw()  # Ẩn cửa sổ chính
root.geometry("800x600")

# Hiển thị cửa sổ pop-up thông báo
show_popup()

# Hiển thị cửa sổ giao diện chính và chờ người dùng tương tác
root.mainloop()
