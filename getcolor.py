import random
import math
import colorsys

pattern_list = {
	'complementary': [[0,0,0], [180,0,0]],
	'split complementary': [[0,0,0], [160,0,0], [200,0,0]],
	'triadic': [[0,0,0], [120,0,0], [240,0,0]],
	'monochrome': [[0,0,0], [0,0,25], [0,0,75]]
}


def get_colors():
	hue_max = 360;

	sat_max = 100;
	light_max = 100;

	sat_base = 20;
	light_base = 20;

	sat = (random.random() * (sat_max - sat_base*2)) + sat_base;
	light = (random.random() * (light_max - light_base*2)) + light_base;

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
	print get_random_color();

	return color_list;

def get_random_color():
	hue_max = 360;

	sat_max = 100;
	light_max = 100;

	sat_base = 0;
	light_base = 0;

	sat = (random.random() * (sat_max - sat_base*2)) + sat_base;
	light = (random.random() * (light_max - light_base*2)) + light_base;
	hue = (random.random() * hue_max);

	return make_color_hsl(hue, sat, light);


def make_color_hsl(h, s, l):
	return "hsl(" + str(h) + "," + str(s) + "%," + str(l) + "%)";