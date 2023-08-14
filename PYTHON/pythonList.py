if __name__ == '__main__':
    N = int(input())
    MyList = []
    for n in range(N):
        Full_command = str(input())
        command =  Full_command.split(' ')
        if command[0] == 'insert':
            MyList.insert(int(command[1]),int(command[2]))
        elif command[0] == 'print':
            print(MyList)
        elif command[0] == 'remove':
            MyList.remove(int(Full_command.split(' ')[1]))
        elif command[0] == 'append':
            MyList.append(int(Full_command.split(' ')[1]))
        elif command[0] == 'sort':
            MyList.sort()
        elif command[0] == 'pop':
            MyList.pop()
        elif command[0] == 'reverse':
            MyList.reverse()