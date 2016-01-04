'''
ComputationalArt.py
John Bozzella
'''

from random import choice
import numpy.random as npr
from math import *
from PIL import Image

#^^ you can also determine which math functions you want to import and name those specifically

def blockrecurse(depth, blocks, parameters):
	""" 
	Choose a random function block from the list of blocks, if depth greater than one, recurse and start again
	"""
	if depth == 1:
		return (choice(blocks), choice(parameters))
	else:
		depth = depth-1
		return (choice(blocks), blockrecurse(depth, blocks, parameters))
	
def functioneval(function, a, b):
	"""
	Evaluate the function based on two parameters a and b
	"""
	if function[0] == "x":
		func = a
	elif function[0] == "y":
		func = b
	elif function[0] == "prod(x, y)":
		func = functioneval(function[1], a, b)*b
	elif function[0] == "avg(x, y)":
		func = (functioneval(function[1], a, b)+b)/2.0
	elif function[0] == "cos_pi(x)":
		func = cos(pi*functioneval(function[1], a ,b))
	elif function[0] == "sin_pi(x)":
		func = cos(pi*functioneval(function[1], a, b))
	return func

def remap_interval(val, inp_int_start, inp_int_end, out_int_start, out_int_end):
	""" 
	Maps the input value that is in the interval [input_interval_start, input_interval_end]
	to the output interval [output_interval_start, output_interval_end].  The mapping
	is an affine one (i.e. output = input*c + b).  Calculates the intervals, finds the relative position
	in the input interval compared to the output and then remaps the that relative position in the output interval
	"""

	input_diff = float(inp_int_end) - float(inp_int_start)   # Calculate input interval
	output_diff = float(out_int_end) - float(out_int_start)  # Calculate output interval
	position = val - float(inp_int_start)					 # Finds the position on the input interval
	relative_position = position/input_diff					 
	remap = (relative_position * output_diff) + out_int_start

	return remap

def colormap(val):
	""" Assign remapped values a color """

	color = remap_interval(val, -1, 1, 0, 255)

	return int(color)

def create(filename, width, height):
	""" create the actual art and save as an image file.
	file is a string that is the filename for the image (should be .png)
	width and height are used set image dimensions
	"""
	# Define the necessary variables and parameters
	min_depth = 6
	max_depth = 10
	depth =  npr.randint(min_depth, max_depth+1)
	blocks = ["prod(x, y)" , "avg(x, y)", "cos_pi(x)", "sin_pi(x)", "x" , "y"]
	parameters = ["x", "y"]

	# Generate a function for each color
	functionr = blockrecurse(depth, blocks, parameters)	
	functiong = blockrecurse(depth, blocks, parameters)
	functionb = blockrecurse(depth, blocks, parameters)
    
	# Generate image and loop color mapping on each pixel	
	picture = Image.new("RGB", (width, height))
	pixels = picture.load()
	for i in range(width):
		for j in range(height):
			x = remap_interval(i, 0, width, -1, 1)
			y = remap_interval(j, 0, height, -1, 1)
			pixels[i, j] = (
                    colormap(functioneval(functionr, x, y)),
                    colormap(functioneval(functiong, x, y)),
                    colormap(functioneval(functionb, x, y))
                    )

	picture.save(filename)

create('test6.png',500,500)
#^^ putting the line above beneath an "if __name__ == '__main__':" clause means
#that you can make this py file a library and call its functions without
#creating an image every time.