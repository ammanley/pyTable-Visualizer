# Ion pyTable-Visualizer

This is a simple script to visualize the relative density of different ion types in a given raster image dataset. 

When run, the program searches the local directory for a inp or hdf5 data file, imports it, and outputs a set of image files based on greyred/green/blue colored ion counts. Currently hard-coded to read in 256x256 raster images and output the same. Ion count visualizations can be modified based on desired size and ion scaling (for helping to see small or really large ion counts).
