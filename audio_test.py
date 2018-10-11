import math
import wave


#fdt = wave.open("sample_music.wav", "r")
#
#
#for i in range(fdt.getnframes()):
#    print(fdt.readframes(i))
#    i += 1

duration = 5
fps = 1000
amplitude = 0

fdt = wave.open("test.wav", "w")

fdt.setnchannels(1)
fdt.setsampwidth(2)
fdt.setframerate(fps)

for i in range(duration*fps):
    data = 440  #hertz
    fdt.writeframes(str(data).encode("utf-8"))


fdt.close()