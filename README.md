# Ion pyTable-Visualizer

This is a simple script to visualize the relative density of different ion types in a given raster image dataset. 

When run, the program searches the local directory for a inp or hdf5 data file, imports it, and outputs a set of image files based on greyred/green/blue colored ion counts. Currently hard-coded to read in 256x256 raster images and output the same. Ion count visualizations can be modified based on desired size and ion scaling (for helping to see small or really large ion counts). Currently hardcoded to return PNG RGB images.

### Getting Started 

1. Spin up a virtual enviroment using your tool of choice (virtualenv or virtualenvwrapper seem popular)
2. Once inside your enviroment, pip install -r requirements.txt
3. If you have a different data file you want to use, rename it to "data.inp" and remove to current data.inp file
4. python ionpath.py to run the script and output your visualizations

### Docs

- Input: "data.inp" 
- Output: grey_ions.png, red_ions.png, green_ions.png, blue_ions.png, rgb_ions.png

- scale(number, multiplier)
    - Very simple function that just returns the ion counts multiplied to be larger or smaller; returns an integer.

- find_ions(counts, color)
    - Takes a "counts" arrary of ion counts and the "color" of ion to look for; returns an integer of ion counts.
    - Ion counts are incremented by looping through the entire counts arrary, and comparing the index with the timestamps array. The total ion count returned will be incremented by the value of counts[k] if timestamp[k] falls within the accepted range for the given ion "color".

- create_image(width, height)
    - Creates a Pillow Image object of the size given for width and height with a type of 'RGB' and default color of white (255,255,255); returns an Image object.