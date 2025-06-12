try:
    file = open("sample.txt","r")
    print("Reading file content:")
    reading_line1 = file.readline()
    reading_line2 = file.readline()
    print("Line 1: " + reading_line1+"Line 2: " + reading_line2)

    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")