from functools import reduce

def process_matrix(list_of_lists):
    """
    Recibe una matriz de números y devuelve una nueva, con los elementos
    cambiados. Cada elemento de la nueva, será el promedio del valor antiguo y el de sus 
    vecinos
    """
    #elimino las exepciones
    if exclude_no_matrix(list_of_lists) == True:
        # Creo una lista vacía donde iré acumulando
        processed_list = []
    
        # por cada elemento de la matriz...
        for x, row in enumerate(list_of_lists):
            for y, element in enumerate(row):
                # lo proceso 
                new_element = process_element(list_of_lists, x, y)
                # lo añado a la lista
                processed_list.append(new_element)
        
        #transformo la lista en una matriz
        processed_matrix = []
        width = len(list_of_lists[0])

        while processed_list != []:
            processed_matrix.append(processed_list[:width])
            processed_list = processed_list[width:]

        # devuelvo la nueva matriz
        return processed_matrix
    else:
        #devuelvo un error si el parametro no es una matriz
        return 'The parameter should be a list of list(s) of the same length containing only numerical values' #alternative: raise ValueError
        


def process_element(list_of_lists, x, y):
    """
    Recibe la matriz y los indices,
    calcula su promedio con sus vecinos y devuelve dicho promedio
    """
    # obtengo la lista de vecinos
    indices = get_neighbour_indices(list_of_lists, x, y)
    values = get_neighbour_values(indices, list_of_lists)

    # calculo su promedio
    average = get_average(values)
 
    # devuelvo el valor final
    return average


def get_neighbour_indices(list_of_lists, x, y): #esto tengo que rehacerlo para la matriz
    """
    Devuelve la lista de índices de los vecinos. Se incluye al
    propio elemento
    """
    #determino la dimension de la matriz
    height = len(list_of_lists)
    width = len(list_of_lists[0])
    
    #calculo los vecinos
    indices = []

    for a in [(-1,0), (1,0), (0,-1), (0,1)]:
        if ( (0 <= x+a[0] < height) and (0 <= y+a[1] < width)):
            indices.append([x+a[0], y+a[1]])

    # incluyo al propio elemento como vecino de sí mismo
    indices.append([x,y])

    return indices


def get_neighbour_values(indices, list_of_lists):
    """
    Recibe una matriz y la lista con los indices. Devuelve el valor de los indices en otra lista
    """
    values = []
    for x,y in indices:
        values.append(list_of_lists[x][y])
    return values

def get_average(numbers):
    """"
    Recibe una lista de números y devuelve su promedio
    """
    return reduce(lambda accum, b: accum + b, numbers, 0) / len(numbers)

def exclude_no_matrix(list_of_lists):
    """
    Recibe una matriz y si la matriz:
    - no tiene listas/ no es una lista de listas / es una lista vacia
    - las listas no son de la misma longitud
    - los valores no son numeros o floats
    devuelve False. De lo contrario, True
    """
    bools =[]
    if list_of_lists == []:
        bools.append(False)
    if isinstance(list_of_lists,list) == True:
        for l in list_of_lists:
            if isinstance(l,list) == True and len(list_of_lists[0]) == len(l):
                for n in l:
                    if type(n) == int or type(n) == float:
                        bools.append(True)
                    else:
                        bools.append(False)
            else:
                bools.append(False)
    else:
        bools.append(False)
        
    if False not in bools:
        return True
    

#------------------TEST------------------
#test cases

test1 = [[6, 4, 3, 4, 1],[7, 6, 5, 2, 1],[2, 9, 0, 4, 3],[8, 4, 6, 1, 2],[5, 2, 0, 2, 2]] #rectungular matrix
test2 = [[1,2,3],[2,3,4],[1,7,5]] #square matrix
test3 = [[2, 4],[4, 2]] #square matrix
test4 = [[0, 0],[0, 0]] #matrix with all 0
test5 = [] #empty list
test6 = [-2] #a list with one int
test7 = [[1, 2, 3, 3]] #only one list in the matrix
test8 = [[[1, 'b'],['c', 'd']]] #string in the list
test9 = [[7,6,5],[1,3,"a"]] #string in the list
test10 = [[1,2,3],[]] #an empty list in the matrix
test11 = [[None, None], [1,2]] #None value
test12 = [[2, 4],[4, 2, 3]] #different lengths
test13 = [[-1,-4,3],[2,-9,0]] #negative numbers
test14 = 5 #int
test15 = [[1.5,2],[5.9999,1.6543]] #floats
test16 = [[]] 

if __name__ == "__main__":
    assert process_matrix(test1) == [[5.666666666666667, 4.75, 4.0, 2.5, 2.0], [5.25, 6.2, 3.2, 3.2, 1.75], [6.5, 4.2, 4.8, 2.0, 2.5], [4.75, 5.8, 2.2, 3.0, 2.0], [5.0, 2.75, 2.5, 1.25, 2.0]]
    assert process_matrix(test2) == [[1.6666666666666667, 2.25, 3.0], [1.75, 3.6, 3.75], [3.3333333333333335, 4.0, 5.333333333333333]]
    assert process_matrix(test3) == [[3.3333333333333335, 2.6666666666666665], [2.6666666666666665, 3.3333333333333335]]
    assert process_matrix(test4) == [[0,0],[0,0]]
    assert process_matrix(test5) == 'The parameter should be a list of list(s) of the same length containing only numerical values'
    assert process_matrix(test6) == 'The parameter should be a list of list(s) of the same length containing only numerical values'
    assert process_matrix(test7) == [[1.5,2,2.6666666666666665,3]]
    assert process_matrix(test8) == 'The parameter should be a list of list(s) of the same length containing only numerical values'
    assert process_matrix(test9) == 'The parameter should be a list of list(s) of the same length containing only numerical values'
    assert process_matrix(test10) == 'The parameter should be a list of list(s) of the same length containing only numerical values'
    assert process_matrix(test11) == 'The parameter should be a list of list(s) of the same length containing only numerical values'
    assert process_matrix(test12) == 'The parameter should be a list of list(s) of the same length containing only numerical values'
    assert process_matrix(test13) == [[-1.0, -2.75, -0.3333333333333333], [-2.6666666666666665, -2.75, -2.0]]
    assert process_matrix(test14) == 'The parameter should be a list of list(s) of the same length containing only numerical values'
    assert process_matrix(test15) == [[3.1666333333333334, 1.7181], [3.0513999999999997, 3.2180666666666666]]
    assert process_matrix(test16) == []


