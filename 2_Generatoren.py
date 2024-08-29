def gen_list():
    liste = []
    for i in range(0,10):
        print("liste: " + str(i))
        liste.append(i)
    return liste


# for element in gen_list():
#     print(element)
    

def gen_generator():
    for i in range(0,10):
        # print("gen: " + str(i))
        yield i
    
# for element in gen_generator():
#     	print("for: "+ str(element))
     

for element in gen_generator():
    if element == 4:
        break
    print("print: " + str(element))