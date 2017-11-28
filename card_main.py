#! /usr/bin/python3

import card_tools

while True:

    card_tools.menu()
    num = input("请选择")

    if num in ["1", "2", "3"]:
        if num == "1":
            card_tools.add_card()
        elif num == "2":
            card_tools.all_card()
        elif num == "3":
            card_tools.search_card()
    elif num == "0":
        break
    else:
        print("请输入正确的选项")
print("谢谢使用名片管理系统")
