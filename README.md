# Ion pyTable Visualizer

This is a simple script to visualize the relative density of different ion types in a given dataset. (currently hardcoded to accept 256x256 grid dataset)

When run, the program searches the local directory for a inp or hdf5 data file and outputs a set of image files based on how many grey/red/green/blue colored ions appear at each grid pixel. Ion count visualizations can be modified based on desired size and ion scaling (for helping to see small or really large ion counts). Currently hardcoded to return PNG RGB images.

Expected Program Input: "data.inp" 

Expected Program Output: grey_ions.png, red_ions.png, green_ions.png, blue_ions.png, rgb_ions.png


### Requirements

    - Python 3.x
    - pyTables (including numpy and numexpr dependencies)
    - Pillow Image Library (PIL fork)
    - Ipython for fun debugging

### Getting Started 

0. Make sure you have the required user permissions to install and run new stuff
1. Spin up a virtual environment using your tool of choice (virtualenv or virtualenvwrapper seem popular)
2. Once inside your environment, pip install -r requirements.txt
3. If you have a different data file you want to use, rename it to "data.inp" and remove the current data.inp file
4. Run "python ionpath.py" to run the script and output your visualizations

### Functions

- scale(number, multiplier)
    - Very simple function that returns the ion counts multiplied to be larger or smaller.

- find_ions(counts, color)
    - Takes a "counts" array of ion counts and the "color" of ion to look for; returns an integer of ion counts.
    - Ion counts are incremented by looping through the entire "counts" array, and comparing the index with the "timestamps" array. The total ion count returned will be incremented by the value of "counts[k]" if "timestamp[k]" falls within the accepted range for the given ion "color".

- create_image(width, height)
    - Creates and returns a Pillow Image object of the size given for width and height with a type of 'RGB' and default color of white (255,255,255).

