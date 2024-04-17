
def filter_query(args, query):    
    for i in range(len(args)):
            if args[i] != None:
                query = query + " AND"
                match i:
                    case 0:
                        query = query + f" timestamp > {args[i]}"
                    case 1:
                        query = query + f" timestamp < {args[i]}"
                    case 2:
                        query = query + f" nombre_variable == {args[i]}"
                    case 3:
                        query = query + f" tiempo_ingreso > {args[i]}"
                    case 4:
                        query = query + f" tiempo_ingreso < {args[i]}"
    return query

def replace_chars(str):
    for c in ['|']:
        if c in str:
            str = str.replace(c, ';')
        
    coords = str.split(';')
    for i in range(len(coords)):
        coords[i] = coords[i].split(',')
    return coords