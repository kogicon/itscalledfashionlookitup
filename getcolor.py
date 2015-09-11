import random
import math
import colorsys

pattern_list = {
	'complementary': [0, 180],
	'split complementary': [0, 160, 200],
	'triadic': [0, 120, 240]
}


def get_colors():
	hue_max = 360;
	saturation = 50
	lightness = 50

	color_list = [];

	rand = (random.random() * hue_max);
	
	ind = int(random.random() * len(pattern_list));
	pattern_name = pattern_list.keys()[ind];
	pattern = pattern_list[pattern_name];

	for p in pattern:
		color_hue = (rand + p) % hue_max;
		color_list.append(make_color_hsl(color_hue, saturation, lightness));

	print color_list;

	return color_list;


def make_color_hsl(h, s, l):
	return "hsl(" + str(h) + "," + str(s) + "%," + str(l) + "%)";