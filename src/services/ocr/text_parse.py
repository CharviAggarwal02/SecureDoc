import easyocr

reader=easyocr.Reader(["en"])
result = reader.readtext("/home/hp-5cd4449308p/PycharmProjects/SecureDoc/Screenshot from 2026-08-11 17-42-38.png",detail=0)

print(result)