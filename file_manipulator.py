import sys


def reverse_file(fileinput, fileoutput):
    try:
        with open(fileinput,"r") as infile:
            content = infile.read()

        reversed_content = content[::-1]

        with open(fileoutput, 'w') as outfile:
            outfile.write(reversed_content)
        print(f"Reversed content written to {fileoutput}")

    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print(f'An error occurred: {e}')

def copy_file(fileinput, fileoutput):
    try:
        with open(fileinput,"r") as inflie:
            content = inflie.read()

        with open(fileoutput, 'w') as outfile:
            outfile.write(content)
        print(f"File copied to {fileoutput}")

    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print(f'An error occurred: {e}')

def duplicate_contents(fileinput, n):
    try:
        with open(fileinput,"r+") as infile:
            content = infile.read()
            infile.seek(0, 2)
            for i in range(int(n)):
                infile.write(content)

        print(f"File duplicated {n} times in {fileinput}")

    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print(f'An error occurred: {e}')

def replace_string(fileinput, needle, newstring):
    try:
        with open(fileinput,"r") as infile:
            content = infile.read()
        
        updated_content = content.replace(needle, newstring)

        with open(fileinput, 'w') as outfile:
            outfile.write(updated_content)

        print(f"Replaced {needle} with {newstring}")

    except FileNotFoundError:
        print(f'File {fileinput} not found')
    except Exception as e:
        print(f'An error occurred: {e}')



def main():

    command = sys.argv[1]

    if command == "reverse" and len(sys.argv) == 4:
        reverse_file(sys.argv[2], sys.argv[3])
    elif command == "copy" and len(sys.argv) == 4:
        copy_file(sys.argv[2], sys.argv[3])
    elif command == "duplicate-contents" and len(sys.argv) == 4:
        duplicate_contents(sys.argv[2], sys.argv[3])
    elif command == "replace-string" and len(sys.argv) == 5:
        replace_string(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Invalid command or arguments.")

if __name__ == '__main__':
    main()