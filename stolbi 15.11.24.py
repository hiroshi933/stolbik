with (open('materials_b_import.csv', 'r', encoding='UTF-8') as f):
    data = f.readlines()
    main = []
    for i in range(1,len(data)):
        #1 столб
        result = []
        temp = data[i].split(';')
        # print(temp)
        title=temp[0].strip()
        result.append(title)
        #2 столб
        type = temp[1].strip()
        result.append(type)
        #3 столб
        image = temp[2].strip()
        if 'не указано' in image or 'нет' in image or "отсутствует" in image:
            image = "NULL"
        if "\\materials\\" in image:
            image = image.replace('\\materials\\', '')
            result.append(image)
            #result.append(main)
        print(result)