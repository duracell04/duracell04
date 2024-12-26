#!/usr/bin/env python3

"""
Create a stylized bunny image reminiscent of the Duracell rabbit,
which you can use as a profile picture. Uses the Pillow library.
"""

from PIL import Image, ImageDraw

def draw_bunny_rabbit(draw: ImageDraw, base_x: int, base_y: int):
    """
    Draw a pink bunny with a battery in its hand. 
    The base_x and base_y define the upper-left coordinate where 
    the bunny drawing begins.
    """
    # Colors
    pink = (255, 182, 193)
    black = (0, 0, 0)
    white = (255, 255, 255)
    orange_battery = (255, 140, 0)
    grey_battery_top = (120, 120, 120)

    # -------------------
    # Bunny Ears
    # -------------------
    # Left ear
    draw.ellipse(
        [
            (base_x + 65, base_y + 10),
            (base_x + 95, base_y + 100)
        ],
        fill=pink,
        outline=black
    )
    # Inner ear highlight
    draw.ellipse(
        [
            (base_x + 70, base_y + 20),
            (base_x + 90, base_y + 95)
        ],
        fill=white,
        outline=black
    )

    # Right ear
    draw.ellipse(
        [
            (base_x + 105, base_y + 10),
            (base_x + 135, base_y + 100)
        ],
        fill=pink,
        outline=black
    )
    # Inner ear highlight
    draw.ellipse(
        [
            (base_x + 110, base_y + 20),
            (base_x + 130, base_y + 95)
        ],
        fill=white,
        outline=black
    )

    # -------------------
    # Bunny Head
    # -------------------
    draw.ellipse(
        [
            (base_x + 60, base_y + 65),
            (base_x + 140, base_y + 145)
        ],
        fill=pink,
        outline=black
    )

    # Eyes (two small black circles)
    draw.ellipse(
        [
            (base_x + 80, base_y + 90),
            (base_x + 88, base_y + 98)
        ],
        fill=black,
        outline=black
    )
    draw.ellipse(
        [
            (base_x + 112, base_y + 90),
            (base_x + 120, base_y + 98)
        ],
        fill=black,
        outline=black
    )

    # Nose (tiny black triangle or ellipse)
    draw.ellipse(
        [
            (base_x + 97, base_y + 108),
            (base_x + 103, base_y + 114)
        ],
        fill=black,
        outline=black
    )

    # -------------------
    # Bunny Body
    # -------------------
    draw.ellipse(
        [
            (base_x + 40, base_y + 130),
            (base_x + 160, base_y + 250)
        ],
        fill=pink,
        outline=black
    )

    # -------------------
    # Battery (rectangle + top)
    # -------------------
    # The bunny is holding a battery on the right side
    battery_left = base_x + 135
    battery_top = base_y + 160
    battery_right = base_x + 175
    battery_bottom = base_y + 215

    # Battery main body
    draw.rectangle(
        [
            (battery_left, battery_top),
            (battery_right, battery_bottom)
        ],
        fill=orange_battery,
        outline=black
    )
    # Battery top (grey)
    draw.rectangle(
        [
            (battery_left, battery_top - 5),
            (battery_right, battery_top)
        ],
        fill=grey_battery_top,
        outline=black
    )

    # Optional battery text
    draw.text(
        (battery_left + 5, battery_top + 20),
        "Power",
        fill=black
    )

    # -------------------
    # Arms (rough lines or thin rectangles)
    # -------------------
    # Left arm
    draw.line(
        [
            (base_x + 50, base_y + 160),
            (base_x + 40, base_y + 200)
        ],
        fill=black,
        width=5
    )
    # Right arm (connecting to battery)
    draw.line(
        [
            (base_x + 145, base_y + 150),
            (battery_left, battery_top + 5)
        ],
        fill=black,
        width=5
    )

    # -------------------
    # Legs (rough lines or thin rectangles)
    # -------------------
    # Left leg
    draw.line(
        [
            (base_x + 70, base_y + 250),
            (base_x + 70, base_y + 290)
        ],
        fill=black,
        width=8
    )
    # Right leg
    draw.line(
        [
            (base_x + 130, base_y + 250),
            (base_x + 130, base_y + 290)
        ],
        fill=black,
        width=8
    )

def create_bunny_image(output_filename: str = "bunny_profile.png"):
    """Create a 512x512 image with the bunny drawn in the center."""
    # Create a blank white image
    img_size = (512, 512)
    img = Image.new("RGB", img_size, (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # You can shift base_x, base_y to reposition the bunny
    base_x = 186  # Center-ish horizontally (512/2 ~ 256)
    base_y = 100  # Somewhat near top

    # Draw bunny
    draw_bunny_rabbit(draw, base_x, base_y)

    # Save the image
    img.save(output_filename)
    print(f"Image saved as {output_filename}")

if __name__ == "__main__":
    create_bunny_image()
