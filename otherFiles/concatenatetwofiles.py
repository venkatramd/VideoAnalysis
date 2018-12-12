file1 = "/home/venkatram/PycharmProjects/VidoAnalysis/result1.txt"
file2 = "/home/venkatram/PycharmProjects/VidoAnalysis/result2.txt"
filenames = [file1,file2]
with open('/home/venkatram/PycharmProjects/VidoAnalysis/finaloutput.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())