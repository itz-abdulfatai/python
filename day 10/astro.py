from PIL import Image

img = Image.open("./006 astro.jpg")


# resized = img.resize((400,400)) #messes up the aspect ratio
# resized.save("small_astro.png", 'png')



img.thumbnail((400,200)) #preserves d aspect ratio but modifies img directly, doesnt return an image
img.save("small_astro.png", 'png')
