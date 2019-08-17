#__author: yaomingxi
#__date: 2019-04-17


#创建商品列表
product_list = [
    ('Mac',10200),
    ('kindle',800),
    ('tesla',900000),
    ('Python book',105),
    ('bike',2000),
]

#用户输入其所有的金额（有多少钱）
saving_num = input('please input your money:')
#定义一个金额变量，用于从中减去商品金额
saving = saving_num
#定义一个购物车（已成功购买的商品）
shopping_car = []

#判断用户输入的是不是数字
if saving.isdigit():
    #将数字转换成整数
    saving = int(saving)

    #创建循环
    while True or go :
    #编号
    #num = 1

        #遍历打印商品
        #增加编号
        for i,j in enumerate(product_list,1):
            print(i,'>>>>>>',j)

    #     print(product_list.index(i),i)
    #
    #     print(num,'#',i)
    #     num += 1

        #将用户的输入赋值给choice
        choice = input('请输入编号选择购买所需的商品。【退出请按q键】：')

        #判断choice是否是数字
        if choice.isdigit():
            #将用户输入转换成整数
            choice = int(choice)

            #判断用户输入的编号是否在列表中
            if choice >0 and choice <=len(product_list):

                #将用户输入的编号对应列表中商品，并将编号赋值给p_item
                p_item = product_list[choice-1]

                #判断编号中商品的价格与用户的金额，如商品价格小于用户金额，可以购买商品
                if p_item[1] < saving :

                    #将用户金额减去商品价格
                    saving -= p_item[1]

                    #并将商品加入购物车
                    shopping_car.append(p_item)
                    print()
                    print('已将', p_item,'加入购物车')
                    print()

                #如果商品价格大于用户金额，不能购买商品，并提示给用户
                else:
                    print()
                    print('余额不足，剩余金额：%s'%saving)
                    print()
                #print(p_item)

                print('--------- 如需其他商品请继续选择 -------------')
                print()

            #如果用户输入的编号不在列表中，提示用户
            else:
                print()
                print('编码不存在！')
                print()
                print('--------- 请重新输入正确的商品编码 -------------')
                print()

        #如用户输入'q'，则退出
        elif choice =='q':

            #判断购物车是否有商品
            print()
            #购物车没有商品
            if not len(shopping_car):
                print('您未购买任何商品')

            #否则，将购物车内商品打印
            else:
                print('-----------您总共购买以下商品---------------')
                for j in shopping_car:
                    print(j,end='\t')

            print()
            num = int(saving_num) - saving


            print()
            print('您已退出本次购物。')
            print()
            print('您本次共消费:',str(num)+'元。',end='\t')
            print('剩余卡内金额:%s'%saving+'元。')
            print()
            go = input('输入【任意键】继续购物')
            print('请输入编号选择购买所需的商品。')
            print()

            #break;

        #如用户输入的不是数字，退出并提示用户 语法错误。
        else:
            print()
            print('invalid input')
            print()
            print('--------- 继续选择所需的商品 -------------')
            print()
#如用户输入不是数字，退出并提示用户必须输入数字
else:
    print('you must input digit')
