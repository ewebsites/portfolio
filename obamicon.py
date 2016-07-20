from PIL import Image
im = Image.open("pic.jpg").convert("RGB")
image_out = Image.new("RGB", (im.size))

pixel_color = list(im.getdata())

new_color = []

for each in pixel_color:
	sum = each[0] + each[1] + each[2]
	if sum > 546:
		new_color.append((252, 227, 166))
		
	elif sum > 364:
		new_color.append((112, 150, 158))
		
	elif sum > 182:
		new_color.append((217, 26, 33))
		
	else:
		new_color.append((0, 51, 76))

image_out.putdata(new_color)
image_out.save("newpic.jpg")