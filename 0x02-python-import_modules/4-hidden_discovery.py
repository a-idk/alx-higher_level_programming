#!/usr/bin/python3
# @a_idk scripting

if __name__ == "__main__":

    import hidden_4

    # checking setting directory to def_name
    def_name = dir(hidden_4)

    for i in def_name:
        if i[:2] != "__":
            print(i)
