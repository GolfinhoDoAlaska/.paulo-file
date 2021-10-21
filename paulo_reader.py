import random
import os

fileinput = input("ENTER FILE NAME (without extension): ")

if os.path.isfile(fileinput+".paulo"):
    number = 0
    with open(fileinput+".paulo", "r+") as paulofile:
        content = paulofile.read()
        lines_list = content.split("\n")
        for line in lines_list:
            line_ = line.split(":")
            if line_[0] == "paulo":
                number += int(line_[1])
            elif line_[0] == "paula":
                number -= int(line_[1])
            elif line_[0] == "paule":
                range_ = line_[1].split("&")
                number += random.randint(int(range_[0]), int(range_[1]))
            else:
                print("error")
        paulofile.close()
    
    with open(str(random.randint(100000000000,900000000000)), "a+") as result:
        result.write(str(number))
        result.close()
