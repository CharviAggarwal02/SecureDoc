import easyocr

reader=easyocr.Reader(["en","hi"])
result = reader.readtext("/home/hp-5cd4449308p/PycharmProjects/SecureDoc/Screenshot from 2026-08-11 17-42-38.png",detail=0)
result_detailed= reader.readtext("path",detail=1)

print(result)

def draw_boxes(image,bounds, colour="red",width=2):
  
