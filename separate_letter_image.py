from PIL import Image
import numpy as np
from setting import *

for k,v in func_name.items():
	im = Image.open('%s.png'%k)
	i = 0
	for r in range(n_row):
		for c in range(n_column):
			left  = (letter_width+letter_space)*c
			upper = (letter_hight+line_space)*r
			right = left+letter_width
			lower = upper+letter_hight
			im_letter = im.crop((left,upper,right,lower))
			if (np.array(im_letter)[:,:,:3].sum(axis=2)-(255*3)).sum() == 0:continue
			im_letter.save('%s_image/%02d_%s.png'%(k,i,v[i]))
			i+=1
