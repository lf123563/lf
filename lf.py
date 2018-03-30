from PIL import Image
im =Image.open("LF.gif")
im.save("pic{:02}.png".format(im.tell()))
im.show()
