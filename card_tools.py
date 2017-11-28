card_list = []

def menu():
    """名片菜单"""
    print("*"*50)
    print("欢迎使用名片修改系统 V1.0.0")
    print("")
    print("1.新增名片")
    print("2.全部名片")
    print("3.查询名片")
    print("")
    print("0.退出系统")
    print("*"*50)
def add_card():
    """新增名片"""
    name_str = input("请输入名字")
    tel_str = input("请输入电话")
    qq_str = input("请输入qq")
    emile_str = input("请输入邮箱")

    card_list.append({
        "name": name_str,
        "tel": tel_str,
        "qq": qq_str,
        "emile": emile_str
    })
    print("新增%s名片成功" % name_str)
def all_card():
    """显示全部名片"""
    if len(card_list) == 0:
        print("还没有名片记录,请使用新增名片功能")
        return
    for title in ["姓名", "电话", "qq", "邮箱"]:
        print(title, end="\t\t")
    print("")
    print("=" * 50)

    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["tel"], card_dict["qq"], card_dict["emile"]))
def search_card():
    """查询名片"""
    find_name = input("请输入要搜索的名字")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            for title in ["姓名", "电话", "qq", "邮箱"]:
                print(title, end="\t\t")
            print("")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["tel"], card_dict["qq"], card_dict["emile"]))

            deal_card(card_dict)
            break
    else:
        print("没有找到%s的名片" % find_name)
def deal_card(find_card):
    """

    :param find_card:
    """
    action = input("请选择要执行的操作：1.修改 2.删除 0.返回菜单")
    if action == "1":
        find_card["name"] = input_card_info(find_card["name"],"请输入名字【回车不修改】")
        find_card["tel"] = input_card_info(find_card["tel"], "请输入电话【回车不修改】")
        find_card["qq"] = input_card_info(find_card["qq"], "请输入qq【回车不修改】")
        find_card["emile"] = input_card_info(find_card["emile"], "请输入邮箱【回车不修改】")
    elif action == "2":
        card_list.remove(find_card)
        print("删除成功")
def input_card_info(value, message):
    """
    value:原来的值
    message：提示信息
    :param value:
    :param message:
    :return:
    """
    result_str = input(message)
    if len(result_str) > 0:
        return result_str
    else:
        return value
