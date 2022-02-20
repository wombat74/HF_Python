try:
    with open('myfile.txt') as fh:
        data = fh.read()

    print(data)
except FileNotFoundError:
    print('The file was not found!')
except PermissionError:
    print("You don't have permission to read this file!")
except Exception as err:
    print('Some other error has occured: ', str(err))