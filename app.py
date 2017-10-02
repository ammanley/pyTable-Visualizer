import tables
from PIL import Image

# Setup output image with white default color 
def create_image(width, height):
    return Image.new('RGB', (width, height),(255,255,255))

# Return ion counts based on input ion color
def find_ions(counts,color):
    if color == 'grey':
        ions = 0
        for i in range(0,len(counts)):
            if 6296 <= timestamps[i] <= 6304:
                ions += counts[i]
        return ions
    elif color == 'red':
        ions = 0
        for i in range(0,len(counts)):
            if 16660 <= timestamps[i] <= 16685:
                ions += counts[i]
        return ions
    elif color == 'blue':
        ions = 0
        for i in range(0,len(counts)):
            if 15600 <= timestamps[i] <= 15630:
                ions += counts[i]
        return ions
    elif color == 'green':
        ions = 0
        for i in range(0,len(counts)):
            if 11994 <= timestamps[i] <= 12012:
                ions += counts[i]
        return ions
    else:
        return 'invalid ion type'

# For modifying scale of input RGB values for high/low ion counts
def scale(number, multiplier):
    out_number = round(number*multiplier)
    if out_number < 0:
    	return 0
    elif out_number > 255:
    	return 255
    else:
    	return out_number

grey_image = create_image(256,256)
red_image = create_image(256,256)
blue_image = create_image(256,256)
green_image = create_image(256,256)
rgb_image = create_image(256,256)

grey_pixels = grey_image.load()
red_pixels = red_image.load()
green_pixels = green_image.load()
blue_pixels = blue_image.load()
rgb_pixels = rgb_image.load()

# Loop through infile data tables pixels

with tables.open_file('./data.inp') as infile:
    for i in range(0,(256*256-1)):
        # set x and y coordinates to use to modify images
        x = int(i/256)
        y = i % 256
        # Load timestamps and counts at pixel
        timestamps = infile.root.time[i]
        counts = infile.root.counts[i]
        # Find grey ions and modify grey image if ion count > 0 to cut down on pixel_access
        grey_ions = scale(find_ions(counts,'grey'), 1)
        if grey_ions:
            grey_pixels[x,y] = (255-grey_ions, 255-grey_ions, 255-grey_ions)
# RGB values start halfway on opposite color values to easily show that no ions will be white,
# but that even one ion will register as a very noticeble RGB point (rather than a ever-so-slightly
    # red/green/blue shade of white, which can be hard to see)
        # Find red ions and modify red image if ion count > 0 to cut down on pixel_access
        red_ions = scale(find_ions(counts,'red'), 1)
        if red_ions:
            red_pixels[x,y] = (255-int(red_ions/2), 127-int(red_ions/2), 127-int(red_ions/2))
        # Find green ions and modify green image if ion count > 0 to cut down on pixel_access
        green_ions = scale(find_ions(counts,'green'), 1)
        if green_ions:         
            green_pixels[x,y] = (127-int(green_ions/2), 255-int(green_ions/2), 127-int(green_ions/2))
        # Find blue ions and modify blue image if ion count > 0 to cut down on pixel_access
        blue_ions = scale(find_ions(counts,'blue'), 1)
        if blue_ions:
            blue_pixels[x,y] = (127-int(blue_ions/2), 127-int(blue_ions/2), 255-int(blue_ions/2))
        # Use all RGB values for final RGB image if ion count > 0 to cut down on pixel_access
        if red_ions or green_ions or blue_ions:
            rgb_pixels[x,y] = (255-int(scale(red_ions, 5)), 255-int(scale(green_ions, 5)), 255-int(scale(blue_ions, 5)))


# Save ion distribution images
grey_image.save('./grey_ions.png', 'PNG')
red_image.save('./red_ions.png', 'PNG')
green_image.save('./green_ions.png', 'PNG')
blue_image.save('./blue_ions.png', 'PNG')
rgb_image.save('./rgb_image.png', 'PNG')
