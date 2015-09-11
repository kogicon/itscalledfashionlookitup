import random
import math
import colorsys
from colutils import get_random_color, make_color_hsl

pattern_list = {
	'complementary': [[0,0,0], [180,0,0]],
	'split complementary': [[0,0,0], [150,0,0], [210,0,0]],
	'analog': [[330,0,0], [0,0,0], [30,0,0]],
	'double split': [[330,0,0], [30,0,0], [150,0,0], [210,0,0]],
	'triadic': [[0,0,0], [120,0,0], [240,0,0]],
	'monochrome': [[0,0,0], [0,0,25], [0,0,50], [0,0,75]]
}


def get_colors():
	hue_max = 360;
	sat_max = 100;
	light_max = 100;

	sat_ceil = 90;
	light_ceil = 80;

	sat_floor = 20;
	light_floor = 20;

	sat = (random.random() * (sat_ceil - sat_floor)) + sat_floor;
	light = (random.random() * (light_ceil - light_floor)) + light_floor;

	color_list = [];

	hue = (random.random() * hue_max);
	
	ind = int(random.random() * len(pattern_list));
	pattern_name = pattern_list.keys()[ind];
	pattern = pattern_list[pattern_name];

	for p in pattern:
		color_hue 	= (hue + p[0]) % hue_max;
		color_sat 	= (sat + p[1]) % sat_max;
		color_light = (light + p[2]) % light_max;
		color_list.append(make_color_hsl(color_hue, color_sat, color_light));

	print color_list;

	return color_list;
