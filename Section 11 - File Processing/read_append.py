with open('Section 11 - File Processing/bear2.txt', 'a') as myfile:
    with open('Section 11 - File Processing/bear1.txt', 'r') as readfile:
        content = readfile.read()
    myfile.write(content)