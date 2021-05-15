with open('.\\bear.txt') as myfile:
    with open('..\\first.txt', 'w') as newfile:
        newfile.write(myfile.read()[:90])