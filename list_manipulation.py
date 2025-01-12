def perform_list_operations(n):
    my_list = []

    for _ in range(n):
        command = input().split()

        match command[0]:
            case 'insert':
                my_list.insert(int(command[1]), int(command[2]))
            case 'print':
                print(my_list)
            case 'remove':
                my_list.remove(int(command[1]))
            case 'append':
                my_list.append(int(command[1]))
            case 'sort':
                my_list.sort()
            case 'pop':
                my_list.pop()
            case 'reverse':
                my_list.reverse()


if __name__ == '__main__':
    N = int(input())
    perform_list_operations(N)
