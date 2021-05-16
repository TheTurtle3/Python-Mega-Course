with open('Section 11 - File Processing/data.txt', 'a+') as myfile:
    myfile.seek(0)
    content = myfile.read()
    
    myfile.write(content)
    myfile.write(content)