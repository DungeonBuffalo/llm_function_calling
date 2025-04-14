from PIL import Image
import cv2
import os
import json
import numpy as np

def resize_image(input_path: str, output_path: str, width: int, height: int):
    with Image.open(input_path) as img:
        img_resized = img.resize((width, height))
        img_resized.save(output_path)
        return f"Resized version of {input_path} successfully saved to {output_path}"
    return f"Encountered an error. Check if the file {input_path} exists and the location {output_path} is accessible."

def mirror_image(input_path: str, output_path: str, mode: str):
    image = cv2.imread(input_path)
    if mode == "horizontal":
        mirrored = cv2.flip(image, 1)
    elif mode == "vertical":
        mirrored = cv2.flip(image, 0)
    elif mode == "diagonal":
        mirrored = cv2.flip(image, -1)
    else:
        return f"Invalid mode. Choose from 'horizontal', 'vertical', or 'diagonal'."
    
    try:
        cv2.imwrite(output_path, mirrored)
        return f"Mirrored version of {input_path} successfully saved as {output_path}"
    except:
        return f"Encountered an error. Check if the file {input_path} exists and the location {output_path} is accessible."

def rgb_to_gray(input_path, output_path):
    try:
        img_cv = cv2.imread(input_path)
        gray_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(output_path, gray_cv)
        return f"Grayscaled version of {input_path} sucessfully saved as {output_path}"
    except:
        return f"Encountered an error. Check if the file {input_path} exists and the location {output_path} is accessible."
    
import re
def parse_and_execute_function_call(response):
    """Parse model output and execute the corresponding function."""
    response = response[response.find('Response:') + len('Response:'):]
    response = response[response.find('<function_call>') + len('<function_call>'):response.find('</function_call>')]
    call_content = response.strip()
    func_name = call_content[:call_content.find('(')].strip()
    inner_content = call_content[call_content.find('(') + 1:call_content.rfind(')')]
    parts = [part.strip().strip("'").strip('()"') for part in inner_content.split(",")]
    args = [int(arg) if arg.isdigit() else arg for arg in parts]
    print(f"\n\n{args}\n\n")
    if func_name in globals():
        globals()[func_name](*args)
    else:
        print(f"Function {func_name} is not defined.")
    
# print(process('<CALL>resize_image("duck.jpeg", "duck_resized.jpeg", (600, 600))</CALL>'))

# adjust the dims of tiger.bmp to 720x540
# flip goose.png vertically
# turn squirrel.webp gray