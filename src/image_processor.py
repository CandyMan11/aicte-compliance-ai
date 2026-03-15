import os
import base64


def encode_image(image_path):
    """
    Convert image file to base64 string
    required for vision LLM APIs
    """

    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode("utf-8")

    return encoded


def load_all_images(folder):
    """
    Load and encode all images from a folder
    """

    image_data = {}

    for file in os.listdir(folder):

        if file.lower().endswith((".png", ".jpg", ".jpeg")):

            full_path = os.path.join(folder, file)

            image_data[file] = encode_image(full_path)

    return image_data