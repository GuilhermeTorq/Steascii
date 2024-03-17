
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

while True:
    print("\nSelect the desired txt file >>")
    # opens dialog box for choosing a txt file
    file_path = filedialog.askopenfilename(filetypes=(('text files', 'txt'),))

    stringEDIT = ""
    stringRAW = ""

    try:
        # will try to read file, if it's not a txt file > exit
        with open(file_path, 'r') as file:
            stringRAW = file.read()
    except:
        print("Error in trying to read file")
        exit()

    for char in stringRAW:
        if char == " ":
            stringEDIT += " "
        elif "\n" in char:
            stringEDIT += "\n"
        else:
            stringEDIT += char

    print("Result Starts here >>\n\n" + stringEDIT)

    print("\nResult Ends here >>\nDon't forget to copy the result before closing the program!!\n")

    while True:
        start = input("Try again? y/n >> ")

        if start == "y" or start == "Y":
            print()
            break
        elif start == "n" or start == "N":
            exit()
        else:
            print("\nNo available option selected\n")

