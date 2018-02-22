from PIL import Image
from PIL import ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox
from base64 import decodebytes
from os import remove

version="v1.1  ™.G"


image_64_encode=b'/9j/4QDCRXhpZgAASUkqAAgAAAAHABIBAwABAAAAAQAAABoBBQABAAAAYgAAABsBBQABAAAAagAA\nACgBAwABAAAAAgAAADEBAgAOAAAAcgAAADIBAgAUAAAAgAAAAGmHBAABAAAAlAAAACBPZmZgAAAA\nAQAAAGAAAAABAAAAUGhvdG9GaWx0cmUgNwAyMDE4OjAyOjEzIDEzOjU5OjQzAAMAAJAHAAQAAAAw\nMjEwAqADAAEAAABvAQAAA6ADAAEAAABaAQAA/9sAQwABAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEB\nAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEB/9sAQwEBAQEBAQEBAQEBAQEB\nAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEB/8AAEQgB\nWgFvAwEiAAIRAQMRAf/EAB8AAAEFAQEBAQEBAAAAAAAAAAABAgMEBQYHCAkKC//EALUQAAIBAwMC\nBAMFBQQEAAABfQECAwAEEQUSITFBBhNRYQcicRQygZGhCCNCscEVUtHwJDNicoIJChYXGBkaJSYn\nKCkqNDU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6g4SFhoeIiYqSk5SVlpeY\nmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2drh4uPk5ebn6Onq8fLz9PX29/j5\n+v/EAB8BAAMBAQEBAQEBAQEAAAAAAAABAgMEBQYHCAkKC//EALURAAIBAgQEAwQHBQQEAAECdwAB\nAgMRBAUhMQYSQVEHYXETIjKBCBRCkaGxwQkjM1LwFWJy0QoWJDThJfEXGBkaJicoKSo1Njc4OTpD\nREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoKDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ip\nqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uLj5OXm5+jp6vLz9PX29/j5+v/aAAwDAQACEQMR\nAD8A/wA/+iiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiii\ngAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKA\nCiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAK\nKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAoo\nooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiii\ngAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKA\nCiiigAooooAKKKKAOp0LR9C1S2mbUPEkOi3iS7Yre6s5pYZ4yoPmC6iJSMhvlKOuTgspPAObqelC\nwkKwXdvfwj/ltbOrjHYkKzEDHX0PXqKyKM46UAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFAB\nRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFF\nFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUU\nUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQ\nAUUUUAFFFFAD1KBZAwJZlAQ9lIdWJP1UFQPcnjHLKKKACiiigAooooAKKKKACiiigAooooAKKKnt\nbW6vrm3srK2nvLy8nitbS0tYZLi5urmeRYoLe3ghV5Z55pWWOKKNGkkkZURSxAoAgrpvDHg3xR4z\nvGsfDGiX2rzRtbrcywIsdjp4upfJt5dU1O5aHTdJt5pv3SXWpXdrbGT5PN3cV98/sm/8E+viV8fP\nFWg6fL4cvbqDV76O0RVh1SbQtKIW5upbnxHd6KIrrULeOzsLwT6doOsaUbZ2P2vxNY6lp9zoNx/Q\nP8G/+Cd/ww+Emo6zp3ibXPC/jbV/BuiaRqL2V98PvH1poHhW71W712z1mfQNE8N2diDc6fBpL3ep\n6rplhYR+IpLYmA63qS3M0vg51xLk2QwbzDFr27UXTweHSr4ubmnyfuoyXs4zaajOtKnCTTipOVkV\nQpYnGN/U6LrQjJxnXk+TDU2kpS5qtmpOMWpOFNTkk1JpRdz+cLwB+wT8Z/GGmT64vhHxzrOnWcbz\n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\nRRQAUUUUAFFFFABRRRQAUUUUAFO+X1b/AL5H/wAVTaKAF49T+Q/+Ko49T+Q/xpKKAF49T+Q/xpPp\n/n9TRRQAUUUUAFFFFABRRRQAU9JJIm3Ru8bdNyMyN+akGmUUAWvt17/z+XX/AIES/wDxdH269/5/\nLr/wIl/+LqrRRYBzu8jF5HZ3PVnYsx+rMST+JptFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABR\nRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFF\nFABRRRQAUucen5A/zFJRQA7cfRf++F/wpCc8/wAgB+gwKSigAooooAXP+cCkoooAKKKKACiiigAo\noooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACii\nigAooooAKKKKACiijrQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFF\nFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUU\nAFFFFABRRRQAUUUUAFFFFABRRRQB/9k=\n'
image_64_decode = decodebytes(image_64_encode)
image_result = open('temp_wafer.jpg', 'wb') # create a writable image and write the decoding result
image_result.write(image_64_decode)


def export(*args):
    global angle
    loadangle=float(angle.get())
    file = filedialog.asksaveasfile(defaultextension=".xml", filetypes=(("Recipe", "*.xml"),))
    try:
        nameroot=file.name[:-5]
        outfile=str(nameroot)+";1.xml"
        fo = open(outfile, 'w', encoding='UTF-8')
        # Company confidential structure is written to file
        fo.write("...loadangle...")
        fo.close()
        file.close()
        remove(file.name)
        messagebox.showinfo("", "The recipe is saved")
    except AttributeError:
        messagebox.showwarning("Oops!", "No file specified")



def updateGUI(*args):
    global cv, im, tkimage,fig, angle
    try:
        cv.delete(fig)
    except:
        ()      #there is nothing to remove from GUI
    rotangle=float(angle.get())
    tkimage = ImageTk.PhotoImage(im.rotate(rotangle))
    fig = cv.create_image(200, 200, image=tkimage)
    curLab.config(text=str(angle.get())+"°")


root = tk.Tk()
global cv, im, tkimage,fig, angle,curlab
root.title("Loading Angle Editor")
root.geometry('{}x{}'.format(770, 430))

anlge=tk.StringVar()
angle=tk.StringVar()
w=400
h=400
windowFrame=tk.Frame(root)
windowFrame.grid()
cv = tk.Canvas(windowFrame, width=w, height=h)
cv.grid(row=0, column=0)
im=Image.open("temp_wafer.jpg")

tkimage=ImageTk.PhotoImage(im)

fig=cv.create_image(200,200,image=tkimage)

utilsFrame=tk.Frame(windowFrame)
utilsFrame.grid(row=0, column=1,padx=20)
manualFrame=tk.Frame(utilsFrame, bd=5,relief="groove")
manualFrame.grid(row=0, column=0)
tk.Label(manualFrame,text="Adjust loading angle", font="Helvetica 10").grid(sticky="w")
scale=tk.Scale(manualFrame, variable=angle, orient="horizontal", from_=-180, to=180,resolution=0.1, length=250,command=updateGUI, showvalue=False, sliderrelief="raised", troughcolor="lightgray",cursor="sb_h_double_arrow")
scale.grid()
curLab=tk.Label(manualFrame,  text=str(angle.get())+"°", font="Helvetica 14")
curLab.grid()
tk.Label(manualFrame, text="Enter loading angle in degree and then press <Return>",font="Helvetica 10").grid()
manualdeg=tk.Entry(manualFrame, textvariable=angle, width=6)
manualdeg.grid(pady=10)
manualdeg.bind("<Return>", updateGUI)
buttFrame=tk.Frame(utilsFrame)
buttFrame.grid(row=1, column=0,pady=20)

tk.Label(buttFrame,text="Export Aligner Recipe").grid()
expB=tk.Button(buttFrame, text="Save",command=export)
expB.grid(pady=5)

tk.Label(root,text=version).grid( sticky="W")
root.mainloop()