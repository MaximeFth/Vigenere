a=0
if a==0:
    text = input('Write Text: ')
    text = text.lower()
    output = []
    for character in text:
        if character == " ":
            number = ord(character)
        elif character == ".":
            number = ord(character)
        elif character == ",":
            number = ord(character)
        else:
            number = ord(character) - 96
        output.append(number)
    print (output)

    cle = input('Write key: ')
    cle = cle.lower()
    key = []
    for character in cle:
        if character == " ":
            number = ord(character)
        else:
            number = ord(character) - 96
        key.append(number)
    print (key)

    key=64*key
    i=len(output)
    k=0
    result=[0]*len(text)
    while k<i:
        result[k]=(key[k]+output[k])%26
        k=k+1


    print(result)

    text = []
	
    print ("Entrez des valeurs. Pressez simplement entrée quand terminé.")
    while True:
        v = input("Valeur:")
        if v:
            text.append(v)
        else:
            break
    
    print ("Valeur entrées:", text)
    lenght=len(text)
    o=-1
    while o<len(text):
        text[o]=int(text[o])
        o=o+1
    cle = input('Write key: ')
    cle = cle.lower()
    key = []
    for character in cle:
        if character == " ":
            number = ord(character)
        else:
            number = ord(character) - 96
        key.append(number)
    print (key)
    key=64*key
    i=len(text)
    k=0
    result=[0]*len(text)
    while k<i:
        result[k]=(text[k]-key[k])%26
        k=k+1


    print(result)
    kk=0
    while kk<len(result):
        result[kk]=result[kk]+96
        kk=kk+1

    print(result)
    kk=0
    while kk<len(result):
        result[kk]=chr(result[kk])
        kk=kk+1

    print (result)
        
