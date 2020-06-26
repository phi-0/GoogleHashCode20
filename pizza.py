from os import listdir
from os.path import isfile, join

path = 'G:\\Documents\\Google Drive\\7 Dev\\python\\Projects\\Google Hash Code\\testsets'
filelist = [f for f in listdir(path) if isfile(join(path, f)) and '.in' in f]

for input_file in filelist:
    #read input file
    with open(join('G:\\Documents\\Google Drive\\7 Dev\\python\\Projects\\Google Hash Code\\testsets', input_file), 'r') as f:
        lines = f.readlines()

    #cleanup and put input file lines into separate lists
    # generator expression: inp = (i.replace('\n','').split(' ') for i in lines)
    inp = [i.replace('\n','').split(' ') for i in lines]

    max_slices = int(inp[0][0])
    num_pies = int(inp[0][1])
    pizzas = inp[1]

    print(max_slices, num_pies, pizzas)

    def find_next(inp_list, rem_slices):
        for i, j in enumerate(reversed(inp_list)):
            if int(j) <= rem_slices:
                return -i + len(inp_list)-1    # return number of pizza. since list is reversed,
            else:
                continue
        return None

    result = []
    current_slices = 0
    slices = max_slices
    while current_slices <= max_slices and len(result) <= num_pies:
        
        next_slice = find_next(pizzas, max_slices-current_slices)

        if next_slice is None:
            break
        else:
            #append the found id of next slice to result list
            result.append(next_slice)
            #add number of slices to current number of slices
            current_slices += int(pizzas[next_slice])
            #remove the found pizza from the list
            pizzas.pop(next_slice)
            
    #print(sorted(result), current_slices)
    with open(join('G:\\Documents\\Google Drive\\7 Dev\\python\\Projects\\Google Hash Code\\testsets',input_file.replace('.in','.out')), 'w') as o:
        o.write(str(len(result)) + '\n')
        for i in result:
            o.write(str(i) + ' ')
