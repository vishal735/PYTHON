def print_full_name(first, last):
    # Write your code here
    str="Hello firstname lastname! You just delved into python."
    print(str.replace("firstname",first).replace("lastname",last))
    
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)