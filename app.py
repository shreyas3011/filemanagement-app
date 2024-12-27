import os

def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"file name {filename} : created successfully !")
    except FileExistsError:
        print(f"the file name {filename} already exists")

    except Exception as E:
        print("an error occurred")


def view_all_files():
    files=os.listdir()
    if not files:
        print("no file found")
    else:
        print("file in directory")

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully")

    except FileNotFoundError:
        print("file not found")

    except exception as e:
        print("an error occured")

def read_file(filename):
    try:
        with open('sample.txt','r') as f:
            content=f.read()
            prints(f"content of {filename}: \n{content}")

    except FileNotFoundError:
        print("file not found")

    except Exception as e:
        print("an error occured")


def edit_file(filename):
    try:
        with open('sample.txt','a') as f:
            content=input("enter data to add = ")
            f.write(content)
            print(f"contemt added to {filename} successfully")

    except FileNotFoundError:
        print(f"{filename} dosent exist")

    except Exception as e:
        print("an error occured")


def main():
    while True:
        print("file managaement app")
        print("1:create file")
        print("2:view all file")
        print("3:delete file")
        print("4:read file")
        print("5:edit file")
        print("6:exit")


        choise=input("enter your choise(1-6) = ")

        if choise=="1":
            filename=input("enter the file name to create =")
            create_file(filename)

        elif choise=="2":
            view_all_files()

        elif choise=="3":
            filename=input("enter the name of the file you want to delete")
            delete_file(filename)

        elif choise=="4":
            filename=input("enter file name to read = ")
            read_file(filename)

        elif choise=="5":
            filename=input("enter file name to edit")
            edit_file(filename)

        elif choise=="6":
            print("closing the app ......")
            break

        else:
            print("in-valid syntax")
            
if __name__=="__main__":
    main()