with open("FileOperate",mode = 'r+',encoding = 'utf-8') as fin:
    # byteLocation = fin.tell()
    # print(byteLocation)
    # str = '永远向前'
    # fin.write(str)
    # fin.seek(0)
    # print(fin.read(3))
    count = 0
    for line in fin:
        if count >3:
            break
        print(line)
        count += 1









