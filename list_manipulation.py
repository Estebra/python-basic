arr = []
def list_manipulation(action, arr, e=None, i=None):
    match action:
        case 'insert':
            arr.insert(i, e)
        case 'print':
            print(arr)
        case 'remove':
            arr.remove(e)
        case 'append':
            arr.append(e)
        case 'sort':
            arr.sort()
        case 'pop':
            arr.pop()
        case 'reverse':
            arr.reverse()
        case _:
            print('Than option is not supported!')

if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        list_manipulation(input(), arr)
