from game_engine import remove_char


while True:
    name1 = input("enter the first name: ")
    name1 = name1.lower()
    name1.replace(' ','')
    name1_list = list(name1)

    name2 = input("enter another name: ")
    name2 = name2.lower()
    name2.replace(' ','')
    name2_list = list(name2)
    proceed = True

    while proceed:
        main_list = remove_char(name1_list,name2_list)

        conc_list = main_list[0]

        proceed = main_list[1]

        star_index = conc_list.index('*')

        name_1 = conc_list[:star_index]
        name_2 = conc_list[star_index+1 :]

    count = len(name_1)+len(name_2)

    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    while len(result)>1:
        split_index = (count % len(result) - 1)

        if split_index >= 0:

            right = result[split_index+1:]
            left = result[: split_index]

            result = left+right

        else:

            result = result[:len(result)-1]

    print("Relationship status :", result[0])

    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans != 'y':
        break