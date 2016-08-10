import os

def example():
	os.chdir('/Users/emily/Documents/PBC')
	print(os.listdir('/Users/emily/Documents/PBC'))

def main():
	example()

if __name__ == '__main__':
    main()