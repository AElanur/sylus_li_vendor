from io import BytesIO

import requests
from requests.exceptions import SSLError
from PIL import Image, ImageDraw, ImageFont

class StudyImage:
    def __init__(self, image, time):
        self.URL = image["love_interests"][3]["quality_time"][0]["study_image"]
        self.TIME = time
        self.FONT_PATH = "arial.ttf"
        self.FONT_SIZE = 70
        self.FONT_COLOR = (255, 255, 255)
        self.COLOR = (0, 0, 0, 0)
        self.TEXT_POSITION = (10, 10)
        self.FONT =  ImageFont.truetype(self.FONT_PATH, self.FONT_SIZE)
        self.STROKE_COLOR = (0, 0, 0, 255)

    def create_study_image(self):
        image = self.load_image_from_url()
        if image is None:
            raise ValueError("Image failed to load")
        image = image.convert("RGBA")
        txt_layer = Image.new("RGBA", image.size, self.COLOR)
        draw = ImageDraw.Draw(txt_layer)
        text = f"{self.TIME} minutes"
        left, top, right, bottom = draw.textbbox((0, 0), text, font=self.FONT)
        text_width = right - left
        text_height = bottom - top

        position = ((image.width - text_width) // 2, (image.height - text_height) // 2)
        try:
            draw.text(
                position,
                text,
                font=self.FONT,
                fill=self.FONT_COLOR,
                stroke_width=2,
                stroke_fill=self.STROKE_COLOR
            )

            combined = Image.alpha_composite(image, txt_layer)
            return combined.convert("RGB")
        except Exception as e:
            print(e)
            return None

    def load_image_from_url(self):
        try:
            response = requests.get(self.URL, verify=True)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content)).convert("RGBA")
            return img
        except SSLError as ssl_err:
            print(f"SSL error loading image from {self.URL}: {ssl_err}")
            return None
        except Exception as e:
            print(f"Error loading image from URL: {e}")
            return None