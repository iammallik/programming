'''
# Sample code to perform I/O:
'''

name = int(input())                  # Reading input from STDIN
string_list = input().split()
int_list = [int(i) for i in string_list]
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail

if __name__ == '__main__':
    print("hello mallik")
