from PIL import Image
import numpy as np
import glob
import matplotlib.pyplot as plt
from decimal import Decimal, ROUND_HALF_UP
from setting import *

#四捨五入
def round_int(a):
	return int(Decimal(str(a)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))

#切り抜き最小枠を取得
def get_minimum_box(im):
	for ix in range(0,letter_width,1):
		if sum(np.array(im).transpose(1,0,2)[ix][:,:3]==[0,0,0])[0] != 0:
			left = ix
			break
	for iy in range(0,letter_hight,1):
		if sum(np.array(im)[iy][:,:3]==[0,0,0])[0] != 0:
			upper = iy
			break
	for ix in range(letter_width-1,0,-1):
		if sum(np.array(im).transpose(1,0,2)[ix][:,:3]==[0,0,0])[0] != 0:
			right = ix+1
			break
	for iy in range(letter_hight-1,0,-1):
		if sum(np.array(im)[iy][:,:3]==[0,0,0])[0] != 0:
			lower = iy+1
			break
	return (left,upper,right,lower)

#二値行列を取得
def get_binary_matrix(im):
	w,h = im.size
	n_x = round_int(w/dot_width)
	n_y = round_int(h/dot_hight) #縦横のdot数
    
	binary_matrix = []
	for iy in range(n_y):
		X = []
		for ix in range(n_x):
			c_x = int(ix*dot_width+(dot_width/2.))
			c_y = int(iy*dot_hight+(dot_hight/2.)) #dot中央の座標
			value = np.array(im)[c_y][c_x][0]
			X.append(1 if value<120 else 0)
		binary_matrix.append(X)
	return binary_matrix

#二値行列を画像出力
def draw_map(char,i,matrix,x_offset,y_offset):
	X = np.arange(len(matrix[0]))+(x_offset/dot_width)
	Y = np.arange(len(matrix))[::-1]+((letter_hight-y_offset)/dot_hight)
	X,Y = np.meshgrid(X,Y)
	X = X.flatten()
	Y = Y.flatten()
	plt.figure(figsize=(8,8))
	plt.scatter(X*scale,Y*scale,c=np.array(matrix).flatten(),cmap='binary',marker='s',s=600)
	plt.grid(color='gray')
	plt.xlim(0,n_dot_x*scale)
	plt.ylim(0,n_dot_y*scale)
	plt.savefig('binary_matrix/%s_%02d.png'%(char,i))
	plt.close()


#複合長方形領域の最小分割問題を貪欲法で解く
def div2rectangle(binary_matrix):
	font = []
	for k, matrix in enumerate(binary_matrix):
		matrix = (np.array(matrix))
		char_walls = []
		while True:
			h_lines = []
			v_lines = []
			# Horizontal lines
			for i in range(len(matrix)):
				start_j = None
				for j in range(len(matrix[0])):
					if matrix[i, j] and start_j is None:
						start_j = j
					if not matrix[i, j] and start_j is not None:
						h_lines.append((j - start_j, i, start_j))
						start_j = None
				if start_j is not None:
					h_lines.append((len(matrix[0]) - start_j, i, start_j))
			# Vertical lines
			for j in range(len(matrix[0])):
				start_i = None
				for i in range(len(matrix)):
					if matrix[i, j] and start_i is None:
						start_i = i
					if not matrix[i, j] and start_i is not None:
						v_lines.append((i - start_i, start_i, j))
						start_i = None
				if start_i is not None:
					v_lines.append((len(matrix) - start_i, start_i, j))
			# Choose the longest line, add it and clear the pixels
			h_lines.sort(key=lambda x: x[0], reverse=True)
			v_lines.sort(key=lambda x: x[0], reverse=True)
			if not h_lines and not v_lines:
				break
			elif not h_lines or v_lines[0][0] >= h_lines[0][0]:
				h, i, j = v_lines[0]
				char_walls.append((j, len(matrix) - i - h, 1, h))
				for r in range(i, i + h):
					matrix[r, j] = False
			else:
				w, i, j = h_lines[0]
				char_walls.append((j, len(matrix) - i - 1, w, 1))
				for c in range(j, j + w):
					matrix[i, c] = False
		font.append(char_walls) #(x,y,w,h)
	return font


#Beatwalls関数を生成
def make_beatwalls_func(name, font, minimum_box):
	combined_text = ''
	for char, walls, (left,_,__,lower) in zip(name,font,minimum_box):
		x_offset = (left/dot_width-n_dot_x/2)
		y_offset = (letter_hight-lower)/dot_hight
		text = ''
		parts_name = []
		for i, (_x,_y,_w,_h) in enumerate(walls):
			x = (_x+x_offset)*scale
			y = (_y+y_offset)*scale
			w = _w*scale
			h = _h*scale
			name = '_%s_%s_%02d'%(k,char,i)
			parts_name.append(name)
			text += 'define: %s\n\tstructures: Wall\n'%name
			text += '\tstartRow: %f\n\tstartHeight: %f\n\twidth: %f\n\theight: %f\n\n'%(x,y,w,h)
		text += 'define: %s_%s\n\tstructures: %s\n\n'%(k,char, ', '.join(parts_name))
		combined_text += text
		with open('%s_bw/%s_%s.bw'%(k,k,char),'w') as f:
			f.write(text)
	with open('%s.bw'%(k),'w') as f:
		f.write(combined_text)



if __name__ == '__main__':

	for k,v in func_name.items():

		#画像をロード
		im_char = [Image.open(file) for file in glob.glob('%s_image/*.png'%k)]

		#最小枠で切り抜き
		minimum_box = [get_minimum_box(im) for im in im_char]
		im_trimmed_char = [im.crop(box) for im,box in zip(im_char,minimum_box)]

		#途中出力
		for i,im in enumerate(im_trimmed_char):
			im.save('minimum_box/%s_%02d.png'%(k,i))

		#二値行列化
		binary_matrix = [get_binary_matrix(im) for im in im_trimmed_char]

		#途中出力
		for i,(matrix,(left,upper,right,lower)) in enumerate(zip(binary_matrix,minimum_box)):
			draw_map(k,i,matrix,left,lower)

		#複合長方形領域の最小分割問題を貪欲法で解く
		font = div2rectangle(binary_matrix)

		#Beatwalls関数を生成
		make_beatwalls_func(v, font, minimum_box)
