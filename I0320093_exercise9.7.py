import array
#mengonversi string ke dalam array.array
B = array.array("b")
B.fromstring("python")
for karakter in B:
	print("%c " % karakter, end = " ")
