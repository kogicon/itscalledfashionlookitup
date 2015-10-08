import random
import math
import colorsys
import numpy as np
from colutils import get_random_color, make_color_hsl

pattern_list = {
	'complementary': [[0,0,0], [180,0,0]],
        'complementary /w black': [[0,0,0], ['STATIC',0,0,10], [180,0,0]],
        'complementary /w white': [[0,0,0], ['STATIC',0,0,99], [180,0,0]],
	'split complementary': [[0,0,0], [150,0,0], [210,0,0]],
	'analog': [[330,0,0], [0,0,0], [30,0,0]],
	'double split': [[330,0,0], [30,0,0], [150,0,0], [210,0,0]],
	'triadic': [[0,0,0], [120,0,0], [240,0,0]],
	'monochrome': [[0,0,0], [0,0,25], [0,0,50], [0,0,75]]
}


def get_colors():
	hue_max = 360
	sat_max = 100
	light_max = 100

	sat_ceil = 90
	light_ceil = 80

	sat_floor = 20
	light_floor = 20

	sat = (random.random() * (sat_ceil - sat_floor)) + sat_floor
	light = (random.random() * (light_ceil - light_floor)) + light_floor

	color_list = []

	hue = (random.random() * hue_max)
	
	ind = int(random.random() * len(pattern_list))
	pattern_name = pattern_list.keys()[ind]
	pattern = pattern_list[pattern_name]

	for p in pattern:
                if p[0] == 'STATIC':
                        color_hue = (p[1]) % hue_max
                        color_sat = (p[2]) % sat_max
                        color_light = (p[3]) % light_max
                else:
                        color_hue 	= (hue + p[0]) % hue_max
                        color_sat 	= (sat + p[1]) % sat_max
                        color_light = (light + p[2]) % light_max
                
		hsl_list = [color_hue,color_sat,color_light]
		rgb_list = colorsys.hls_to_rgb(hsl_list[0]/hue_max, hsl_list[2]/light_max, hsl_list[1]/sat_max);
		rgb_max = 255
		rgb_list = map(lambda x: int(round(x*rgb_max)), rgb_list)
		hsl_list = [round(hsl_list[0]) % hue_max, round(hsl_list[1]), round(hsl_list[2])]
		rgb_str = '#' + reduce(lambda x,y: str(x) + format(y, '02x'), rgb_list, '')
		rgb_str2 = 'rgb(' + str(rgb_list[0]) + ',' + str(rgb_list[1]) + ',' + str(rgb_list[2]) + ');'
		print rgb_str2


		print hsl_list
		print rgb_list

		color_list.append([make_color_hsl(color_hue, color_sat, color_light), make_color_hsl(round(color_hue), round(color_sat), round(color_light)) +
                                   ' | ' + rgb_str2 + ' | ' + rgb_str])

	print color_list;
	
	np.random.shuffle(color_list)

	return color_list;
