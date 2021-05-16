with open('Section 11 - File Processing/bear.txt') as myfile:
    with open('Section 11 - File Processing/first.txt', 'w') as newfile:
        newfile.write(myfile.read()[:90])