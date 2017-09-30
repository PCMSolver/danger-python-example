def vector(dim):
    import numpy as np


    return np.random.rand(dim)

def message():
    return 'Hello, Danger world!'

def main():
    print(message())
    print(vector(10))

if __name__ == '__main__':
    main()
