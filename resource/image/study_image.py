from io import BytesIO

import requests
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "arial.ttf"
FONT_SIZE = 50
TEXT_COLOR = (255, 255, 255, 255)
TEXT_POSITION = (10, 10)

font = ImageFont.truetype(FONT_PATH, FONT_SIZE)


def create_study_image(study_info):
    img = load_image_from_url(study_info["li_study_image"])
    if img is None:
        return None

    img = img.convert("RGBA")
    txt_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt_layer)

    text = f"{str(study_info.get('time', ''))} minutes"
    font = ImageFont.truetype("arial.ttf", 50)

    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    text_width = right - left
    text_height = bottom - top

    position = ((img.width - text_width) // 2, (img.height - text_height) // 2)

    fill_color = (255, 255, 255, 128)
    stroke_color = (0, 0, 0, 255)

    draw.text(
        position,
        text,
        font=font,
        fill=fill_color,
        stroke_width=2,
        stroke_fill=stroke_color
    )

    combined = Image.alpha_composite(img, txt_layer)
    return combined.convert("RGB")

def load_image_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content)).convert("RGBA")
        return img
    except Exception as e:
        print(f"Error loading image from URL: {e}")
        return None