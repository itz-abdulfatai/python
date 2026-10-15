from PIL import Image
# , ImageFilter


img = Image.open('./pokedox/004 pikachu.jpg')
# filtered_image = img.filter(ImageFilter.SHARPEN)
# filtered_image = img.convert("L")
# resize = filtered_image.resize((300,300))
# crooked = filtered_image.rotate()
box = (100, 100, 400, 400)
region = img.crop(box)

region.save("grey.png", 'png')
