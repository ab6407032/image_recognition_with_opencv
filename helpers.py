import cv2
import tkinter as tk

def get_screen_dimensions():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    return screen_width, screen_height

def resize_image(image, screen_width, screen_height):
    # Get the dimensions of the image
    height, width = image.shape[:2]

    # Calculate the aspect ratio of the image
    aspect_ratio = width / height

    # Calculate the new dimensions of the image to fit the screen
    if width > screen_width or height > screen_height:
        if aspect_ratio > 1:
            # Width is greater than height
            new_width = screen_width
            new_height = int(screen_width / aspect_ratio)
        else:
            # Height is greater than width
            new_height = screen_height
            new_width = int(screen_height * aspect_ratio)
    else:
        new_width, new_height = width, height

    # Resize the image
    return cv2.resize(image, (new_width, new_height))