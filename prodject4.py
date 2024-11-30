from PIL import Image
image = Image.open('monro.jpg')
red_channel, green_channel, blue_channel = image.split()

first_red_picture = red_channel.crop((50, 0, red_channel.width, red_channel.height))
second_red_picture = red_channel.crop((25, 0, red_channel.width - 25, red_channel.height))
red_channel = Image.blend(first_red_picture, second_red_picture, 0.5)

first_blue_picture = blue_channel.crop((0, 0, blue_channel.width - 50, blue_channel.height))
second_blue_picture = blue_channel.crop((25, 0, blue_channel.width - 25, blue_channel.height))
blue_channel = Image.blend(first_blue_picture, second_blue_picture, 0.5)


green_picture = green_channel.crop((25, 0, green_channel.width - 25, green_channel.height))

image = Image.merge('RGB', (red_channel, green_picture, blue_channel))

image.thumbnail((80, 80))
image.save('small.jpg')
