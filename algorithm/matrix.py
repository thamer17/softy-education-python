def create_matrix():
    number_of_rows = int(input("Enter number of rows: ")) 
    number_of_columns = int(input("Enter number of columns: "))
    matrix = []
    for i in range(number_of_rows):
        row = []
        for i in range(number_of_columns):
            element = int(input("Enter an element: "))
            row.append(element)
        matrix.append(row)
    print(matrix)
create_matrix()
        
