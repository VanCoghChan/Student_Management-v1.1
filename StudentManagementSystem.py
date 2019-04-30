#我真是个天才，一口气900行Python还能成功debug.....
import easygui as g
from tkinter import *
import sys
Users_dict = {}
students_info = {}  #用于储存学生的基本信息
global User  #确定用户身份
global list_1
list_1 = []
global username  #学生用户姓名
username = 'Unknown'

class Person:
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age
    def print_per_info(self):
        print("姓名:",self.name)
        print("性别:",self.sex)
        print("年龄:",self.age)
        
class Date:
    def __init__(self,year=2000,month=00,day=00):
        self.year = year
        self.month = month
        self.day = day
    def set_time(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    def print_date(self):
        print("%s年 %s月 %s号"%(self.year,self.month,self.day))
'''
class Score():
    def __init__(self):
        self.stu_score = []
        self.stu_aver = 0  
    def set_score(self): 
        print("请输入学生成绩:")
        for i in range(4):
            print("第%d科:"%(i+1),end = '')
            m = int(input())
            self.stu_score.append(m)
    def get_aver(self):
        return self.stu_aver
    def pint_score(self):
        print("学生每科成绩如下:")
        flag = 1
        for i in self.stu_score:
            print("第%d科:"%flag,i,end = "  ")
            flag+=1
        print('\n')
        self.stu_aver = sum(self.stu_score)/len(self.stu_score)
        print("平均成绩:",self.stu_aver)
'''
class Student(Person,Date):
    #global Birthdate,Enterdate
    #Birthdate = Date()
    #Enterdate = Date()
    def __init__(self):
        Person.__init__(self,name='unknown',sex='unknown',age='nuknown')
        #Birthdate.set_time(0000,00,00)
        #Enterdate.set_time(0000,00,00)
        '''
        self.student_id = 000000
        self.apartment = 'unknown'
        self.tele_num = 000000
        self.class1 = 00000
        self.class2 = 00000
        self.class3 = 00000
        self.class4 = 00000
        self.aver = 00000
        '''
    def set_student_score(self,class1,class2,class3,class4):  #设置学生成绩
        self.class1 = class1
        self.class2 = class2
        self.class3 = class3
        self.class4 = class4
        self.aver = round((int(self.class1) + int(self.class2) + int(self.class3) + int(self.class4))/4,2)
    def refresh_aver(self):
        self.aver = round((int(self.class1) + int(self.class2) + int(self.class3) + int(self.class4))/4,2)
    def set_class1(self,class1):
        self.class1 = class1
    def set_class2(self,class2):
        self.class2 = class2
    def set_class3(self,class3):
        self.class3 = class3
    def set_class4(self,class4):
        self.class4 = class4
    def return_class1(self):
        return self.class1
    def return_class2(self):
        return self.class2
    def return_class3(self):
        return self.class3
    def return_class4(self):
        return self.class4
    def return_aver(self):                   
        return self.aver
    def set_student_info(self,name,sex,age,student_id,apartment,major,tele_num,QQ):
        Person.__init__(self,name=name,sex=sex,age=age) 
        #Birthdate.set_time(year_b,month_b,day_b)
        #Enterdate.set_time(year_e,month_e,day_e)
        self.student_id = student_id
        self.apartment = apartment
        self.major = major
        self.tele_num = tele_num
        self.QQ = QQ
    def set_name(self,name):
        self.name = name
    def set_sex(self,sex):
        self.sex = sex
    def set_age(self,age):
        self.age = age
    def set_id(self,stu_id):
        self.student_id = stu_id
    def set_apart(self,apart):
        self.apartment = apart
    def set_major(self,major):
        self.major = major
    def set_tele(self,tele):
        self.tele_num = tele
    def set_QQ(self,QQ):
        self.QQ = QQ   
    def return_name(self):
        return self.name
    def return_sex(self):
        return self.sex
    def return_age(self):
        return self.age
    def return_ID(self):
        return self.student_id
    def return_apartment(self):
        return self.apartment
    def return_major(self):
        return self.major
    def return_tele(self):
        return self.tele_num
    def return_QQ(self):
        return self.QQ

class main_window(Frame):
        def __init__(self,master=None):
            Frame.__init__(self,master)
            self.createWidgets()
            self.stu_read()
            self.stu_write()
            
        def createWidgets(self):
            self.img = PhotoImage(file = '熊本熊1.gif')
            self.label_image = Label(self.master,image=self.img)
            self.label_image.pack()
            self.button_1 = Button(self.master,text='添加学生信息',font=('微软雅黑'),width=15,command=self.add_student)
            self.button_1.place(x=50,y=310)
            self.button_2 = Button(self.master,text='修改学生信息',font=('微软雅黑'),width=15,command=self.change_student)
            self.button_2.place(x=290,y=310)
            self.button_3 = Button(self.master,text='删除学生信息',font=('微软雅黑'),width=15,command=self.delete_student)
            self.button_3.place(x=50,y=380)
            self.button_4 = Button(self.master,text='查询学生信息',font=('微软雅黑'),width=15,command=self.check_student)
            self.button_4.place(x=290,y=380)
            self.button_5 = Button(self.master,text='显示所有学生信息',font=('微软雅黑'),width=15,command=self.displayall)
            self.button_5.place(x=50,y=450)
            self.button_6 = Button(self.master,text='退出系统',fg='red',bg='lightblue',font=('微软雅黑'),width=15,command=self.quit)
            self.button_6.place(x=290,y=450)
            self.button_7 = Button(self.master,text='查看各科平均成绩及及格率',bg='pink',font=('微软雅黑'),width=25,command=self.aver_and_passrate)
            self.button_7.place(x=110,y=520)
        def aver_and_passrate(self):
            self.master.destroy()
            display_aver_and_passrate()
        def add_student(self):
            self.master.destroy()
            add_stu()
        def change_student(self):
            self.master.destroy()
            change_stu()
        def delete_student(self):
            self.master.destroy()
            delete_stu()
        def check_student(self):
            self.master.destroy()
            check_stu()
        def displayall(self):
            self.master.destroy()
            display_all()
        def quit(self):
            sys.exit(0)
        def stu_read(self):
            student_info_read()
            for i in students_info:
                students_info[i].refresh_aver()
        def stu_write(self):
            student_info_write()

class main_window_stu(Frame):
        def __init__(self,master=None):
            Frame.__init__(self,master)
            self.createWidgets()
            self.stu_read()
        def quit(self):
            sys.exit(0)
        def stu_read(self):
            student_info_read()
            for i in students_info:
                students_info[i].refresh_aver()
        def check_self(self):
            self.master.destroy()
            check_stu()
        def aver_and_passrate(self):
            self.master.destroy()
            display_aver_and_passrate()
        def createWidgets(self):
            self.img = PhotoImage(file = '熊本熊1.gif')
            self.label_image = Label(self.master,image=self.img)
            self.label_image.pack()
            self.button_1 = Button(self.master,text='添加学生信息',font=('微软雅黑'),width=15,fg='#7c87a8')
            self.button_1.place(x=50,y=310)
            self.button_2 = Button(self.master,text='修改学生信息',font=('微软雅黑'),width=15,fg='#7c87a8')
            self.button_2.place(x=290,y=310)
            self.button_3 = Button(self.master,text='删除学生信息',font=('微软雅黑'),width=15,fg='#7c87a8')
            self.button_3.place(x=50,y=380)
            self.button_4 = Button(self.master,text='查询自身信息',font=('微软雅黑'),width=15,command=self.check_self) 
            self.button_4.place(x=290,y=380)
            self.button_5 = Button(self.master,text='显示所有学生信息',font=('微软雅黑'),width=15,fg='#7c87a8')
            self.button_5.place(x=50,y=450)
            self.button_6 = Button(self.master,text='退出系统',fg='red',bg='lightblue',font=('微软雅黑'),width=15,command=self.quit)
            self.button_6.place(x=290,y=450)
            self.button_7 = Button(self.master,text='查看各科平均成绩及及格率',bg='pink',font=('微软雅黑'),width=25,command=self.aver_and_passrate)
            self.button_7.place(x=110,y=520)
 
class login_window(Frame):
    def __init__(self,master=None):
            Frame.__init__(self,master)
            self.createWidgets()
            self.Login_info_load()
            self.user_name = 'unknown'
            self.password = 'unknown'
    def createWidgets(self):
        self.img = PhotoImage(file = '上号.gif')
        self.label_image = Label(self.master,image=self.img,height=300)
        self.label_image.place(x=70,y=10)
        self.user_name_label = Label(self.master,text='Username:',font=('Comic Sans MS',17),fg='#cb3a43')
        self.user_name_label.place(x=65,y=320)
        self.user_name_entry = Entry(self.master,font=('Small Fonts',15))
        self.user_name_entry.place(x=190,y=325)
        
        self.password_label = Label(self.master,text='Password :',font=('Comic Sans MS',17),fg='#4c3acb')
        self.password_label.place(x=65,y=380)
        self.password_entry = Entry(self.master,font=('Small Fonts',15),show='*')
        self.password_entry.place(x=190,y=385)
           
        self.button_confirm = Button(self.master,text='Login',font=('Fixedsys',20),height=2,width=8,command=self.identify,fg='#ff711c')
        self.button_confirm.place(x=210,y=440)

    def warning_worryuser(self):
        self.root = Tk()
        self.root.title('Warning!')
        self.root.geometry('400x170+550+400')
        self.label_warning = Label(self.root,text='"用户名"错误！\n请检查后再输入！',font=('微软雅黑',15))
        self.label_warning.place(x=130,y=50)
        self.root.mainloop()

    def warning_worrypassword(self):
        self.root = Tk()
        self.root.title('Warning!')
        self.root.geometry('400x170+550+400')
        self.label_warning = Label(self.root,text='"密码"错误！\n请检查后再输入！',font=('微软雅黑',15))
        self.label_warning.place(x=130,y=50)
        self.root.mainloop()

    def welcome_user(self):
        self.root1 = Tk()
        self.root1.title('登录成功!')
        self.root1.geometry('400x170+550+400')
        self.welcome_label_2 = Label(self.root1,text='Welcome Back!',font=('Small Fonts',15),fg='green').place(x=130,y=30)
        if self.user_name.isalpha():
            global User
            User = '管理员'
            self.welcome_label = Label(self.root1,text='[管理员] '+self.user_name,font=('微软雅黑',15),fg='red')
            self.welcome_label.place(x=130,y=60)
        else:
            global User
            User = '学生'
            self.welcome_label = Label(self.root1,text='[学生] '+self.user_name,font=('微软雅黑',15),fg='red')
            self.welcome_label.place(x=130,y=60)
        self.button_welcom = Button(self.root1,text='确定',command=self.welcome_confirm,font=('微软雅黑',15))
        self.button_welcom.place(x=170,y=110)
        self.root1.mainloop()

    def welcome_confirm(self):
        self.master.destroy()
        self.root1.destroy()
    def Login_info_load(self):
        f = open('password.txt','r')
        data = f.readlines()
        list_1 = [i.strip('\n') for i in data]
        list_2 = ['','管理员:','学生:']
        for i in list_2:    
            while i in list_1: 
                list_1.remove(i)
        '''
        for i in list_1:
            if i == '管理员:':
                mark_1 = list_1.index(i)
            if i == '学生:':
                mark_2 = list_1.index(i)
        list_Administrator = list_1[mark_1+1:mark_2]
        while '' in list_Administrator:
            list_Administrator.remove('')
        list_student = list_1[mark_2+1:]
        while '' in list_student:
            list_student.remove('')
        '''
        list_username = list_1[::2]
        list_password = list_1[1::2]
        #global Users_dict
        flag=0
        while flag<len(list_username):
            Users_dict.setdefault(list_username[flag],list_password[flag])
            flag+=1

    def Login_check(self,username,password):
        if username.isalpha():
            self.administrator_check(username,password)
        if username.isdigit():
            self.student_check(username,password)

    def student_check(self,username,password):
        flag_student_1 = 0
        flag_student_2 = 0
        if username in Users_dict:
            flag_student_1 = 1
            if password == Users_dict[username]:
                flag_student_2 = 1
        if flag_student_1 == 1 and flag_student_2 == 1:
            self.welcome_user()    
        if flag_student_1 == 1 and flag_student_2 == 0:
            self.warning_worrypassword()
        if flag_student_1 == 0:
            self.warning_worryuser()
        
    def administrator_check(self,username,password):
        flag_administrator_1 = 0
        flag_administrator_2 = 0
        if username in Users_dict:
            flag_administrator_1 = 1
            if password == Users_dict[username]:
                flag_administrator_2 = 1
        if flag_administrator_1 == 1 and flag_administrator_2 == 1:
            self.welcome_user()
        if flag_administrator_1 == 1 and flag_administrator_2 == 0:
            self.warning_worrypassword()
        if flag_administrator_1 == 0:
            self.warning_worryuser()
        
    def identify(self):
        self.user_name = self.user_name_entry.get()
        global username
        username = self.user_name
        self.password = self.password_entry.get()
        self.Login_check(self.user_name,self.password)

def calu_aver(students_info):  #用于计算各科的平均成绩
    list_aver = []  #用于按顺序存放各科平均成绩
    sum_major = 0
    sum_math = 0
    sum_physical = 0
    sum_English = 0
    for i in students_info:
        sum_major += int(students_info[i].return_class1())
        sum_math += int(students_info[i].return_class2())
        sum_physical += int(students_info[i].return_class3())
        sum_English += int(students_info[i].return_class4())
    num = len(students_info)
    list_aver.append(round(sum_major/num,2))
    list_aver.append(round(sum_math/num,2))
    list_aver.append(round(sum_physical/num,2))
    list_aver.append(round(sum_English/num,2))
    return list_aver

def calu_passrate(students_info):  #用于计算各科的及格率
    list_passrate = []    #用于记录各科的及格率
    pass_student_major = 0    #专业课及格的人数
    pass_student_math = 0    #数学课及格的人数
    pass_student_physical = 0    #物理课及格的人数
    pass_student_English = 0    #英语课及格的人数
    for i in students_info:
        if int(students_info[i].return_class1()) > 60:
            pass_student_major += 1
        if int(students_info[i].return_class2()) > 60:
            pass_student_math += 1
        if int(students_info[i].return_class3()) > 60:
            pass_student_physical +=1
        if int(students_info[i].return_class4()) > 60:
            pass_student_English +=1
    num = len(students_info)
    #print(pass_student_major,' ',pass_student_math,' ',pass_student_physical,' ',pass_student_English)  #测试代码
    list_passrate.append(round(pass_student_major/num,2))
    list_passrate.append(round(pass_student_math/num,2))
    list_passrate.append(round(pass_student_physical/num,2))
    list_passrate.append(round(pass_student_English/num,2))
    return list_passrate

def add_stu():  #添加学生信息的函数
    global students_info    #用于储存学生的基本信息    储存形式为{name_1:obj1, name_2:obj2,........} 
    list_name = []          #用于储存学生姓名(为字典提供键名 name)
    list_stuobj = []        #用于储存学生对象(为字典提供键值 obj)
    reply_int = g.integerbox(msg='请输入本次录入学生的个数(单次最多99个)', title='学生管理系统 v1.1 [管理员]',default=1,lowerbound=0, upperbound=99, image='熊本熊.gif', root=None)
    for i in range(reply_int):
        msg = "请填写一下信息(其中带*号的项为必填项)"   #此处要实现学生信息输入的必选项,其中带*号的为必须输入,否则出现提示【*某一项】为必填项,并要求重新输入,并且保留上次的输入内容
        title = "账号中心"                                                                                
        fieldNames = ["*真实姓名","*性别","*年龄","*学号","*学院","*专业","*手机号码","*QQ","*专业课成绩","*高数成绩","*物理成绩","*英语成绩"]
        input_value = []   #用于暂存一个学生基本信息
        input_value = g.multenterbox(msg,title,fieldNames)
        #print(fieldValues)
        while True:
            if input_value == None :
                break
            errmsg = ""
            for i in range(len(fieldNames)):
                option = fieldNames[i].strip()
                if input_value[i].strip() == "" and option[0] == "*":
                    errmsg += ("【%s】为必填项   " %fieldNames[i])
            if errmsg == "":
                break
            input_value = g.multenterbox(errmsg,title,fieldNames,input_value)   
        i = Student()
        if input_value[0] not in students_info:
            list_name.append(input_value[0])   #将学生姓名添加到list_name
        else:
            g.msgbox(title='警告!',msg='该学生信息已经存在!')
            add_stu()
        #完成对相应学生对象的实例化
        i.set_student_info(input_value[0],input_value[1],input_value[2],input_value[3],input_value[4],input_value[5],input_value[6],input_value[7])
        i.set_student_score(input_value[8],input_value[9],input_value[10],input_value[11])
        list_stuobj.append(i)              #将产生学生对象添加到list_stuobj
    #students_info_1 = {}
    #students_info_1 = dict(zip(list_name,list_stuobj))
    flag = 0
    while flag < len(list_name):
        students_info.setdefault(list_name[flag],list_stuobj[flag])     #将学生信息以学生名字做为键名，以生成的学生对象为键值，一个一个地打包成字典
        flag += 1
    g.msgbox(title='提示！',msg='本次学生基本信息录入完成',ok_button='OK')
    #student_info_write()
    back_main_windows()

def change_stu():  #修改学生信息的函数
    if students_info is None:
        print('数据库为空!')
    else:
        name_change = g.enterbox(msg='请输入要修改的学生的姓名',title='学生管理系统 v1.1')   #get被修改学生的姓名
        if name_change not in students_info:                               #判断数据库中是否有此学生
            flag = g.ccbox(msg="查无此人,请确认后再输入!",title='警告！',choices=('继续输入','关闭'))
            if flag == 1:
                change_stu()
            else:
                back_main_windows()                 
        else:
                #由于easygui模块的过于简陋,以下内容使用tkinter的控件
                class Application(Frame):    #定义一个类,此类为修改学生信息的视窗类,用于产生学生修改操作的视窗
                    def __init__(self, master=None):
                        Frame.__init__(self,master)
                        self.createWidgets(name_change)
                    def back_menu(self):   #  返回按键的功能函数,shoutdown现窗口并返回次级窗口
                        self.master.destroy()
                        back_main_windows()
                    def confirm(self):    #确认修改按键的功能函数,get StringVar()中的值并保存
                        #students_info[name_change].set_name(self.name_var.get())
                        students_info[name_change].set_sex(self.sex_var.get())
                        students_info[name_change].set_age(self.age_var.get())
                        students_info[name_change].set_id(self.id_var.get())
                        students_info[name_change].set_apart(self.apart_var.get())
                        students_info[name_change].set_major(self.major_var.get())
                        students_info[name_change].set_tele(self.tele_var.get())
                        students_info[name_change].set_QQ(self.QQ_var.get())
                        students_info[name_change].set_class1(self.class1_var.get())
                        students_info[name_change].set_class2(self.class2_var.get())
                        students_info[name_change].set_class3(self.class3_var.get())
                        students_info[name_change].set_class4(self.class4_var.get())
                        students_info[name_change].refresh_aver()
                    def createWidgets(self,name_change):  
                        self.name_label = Label(text='姓名:',font=('微软雅黑',15))
                        self.name_label.grid(row=0,column=0)
                        self.name_var = StringVar(self)
                        self.name_var.set(students_info[name_change].return_name())
                        self.name_label_2 = Label(textvariable=self.name_var,font=('微软雅黑',11),fg='red')
                        self.name_label_2.grid(row=0,column=1)

                        self.sex_label = Label(text='性别:',font=('微软雅黑',15))
                        self.sex_label.grid(row=1,column=0)
                        self.sex_var = StringVar(self)
                        self.sex_var.set(students_info[name_change].return_sex())
                        self.sex_entry = Entry(self.master,textvariable=self.sex_var)
                        self.sex_entry.grid(row=1,column=1)

                        self.age_label = Label(text='年龄:',font=('微软雅黑',15))
                        self.age_label.grid(row=2,column=0)
                        self.age_var = StringVar(self)
                        self.age_var.set(students_info[name_change].return_age())
                        self.age_entry = Entry(self.master,textvariable=self.age_var)
                        self.age_entry.grid(row=2,column=1)

                        self.id_label = Label(text='学号:',font=('微软雅黑',15))
                        self.id_label.grid(row=3,column=0)
                        self.id_var = StringVar(self)
                        self.id_var.set(students_info[name_change].return_ID())
                        self.id_entry = Entry(self.master,textvariable=self.id_var)
                        self.id_entry.grid(row=3,column=1)

                        self.apart_label = Label(text='学院:',font=('微软雅黑',15))
                        self.apart_label.grid(row=4,column=0)
                        self.apart_var = StringVar(self)
                        self.apart_var.set(students_info[name_change].return_apartment())
                        self.apart_entry = Entry(self.master,textvariable=self.apart_var)
                        self.apart_entry.grid(row=4,column=1)

                        self.major_label = Label(text='专业:',font=('微软雅黑',15))
                        self.major_label.grid(row=5,column=0)
                        self.major_var = StringVar(self)
                        self.major_var.set(students_info[name_change].return_major())
                        self.major_entry = Entry(self.master,textvariable=self.major_var)
                        self.major_entry.grid(row=5,column=1)

                        self.tele_label = Label(text='电话:',font=('微软雅黑',15))
                        self.tele_label.grid(row=6,column=0)
                        self.tele_var = StringVar(self)
                        self.tele_var.set(students_info[name_change].return_tele())
                        self.tele_entry = Entry(self.master,textvariable=self.tele_var)
                        self.tele_entry.grid(row=6,column=1)

                        self.QQ_label = Label(text='QQ:',font=('微软雅黑',15))
                        self.QQ_label.grid(row=7,column=0)
                        self.QQ_var = StringVar(self)
                        self.QQ_var.set(students_info[name_change].return_QQ())
                        self.QQ_entry = Entry(self.master,textvariable=self.QQ_var)
                        self.QQ_entry.grid(row=7,column=1)

                        self.class1_label = Label(text='专业课成绩:',font=('微软雅黑',15))
                        self.class1_label.grid(row=8,column=0)
                        self.class1_var = StringVar(self)
                        self.class1_var.set(students_info[name_change].return_class1())
                        self.class1_entry = Entry(self.master,textvariable=self.class1_var)
                        self.class1_entry.grid(row=8,column=1)

                        self.class2_label = Label(text='高数成绩:',font=('微软雅黑',15))
                        self.class2_label.grid(row=9,column=0)
                        self.class2_var = StringVar(self)
                        self.class2_var.set(students_info[name_change].return_class2())
                        self.class2_entry = Entry(self.master,textvariable=self.class2_var)
                        self.class2_entry.grid(row=9,column=1)

                        self.class3_label = Label(text='物理成绩:',font=('微软雅黑',15))
                        self.class3_label.grid(row=10,column=0)
                        self.class3_var = StringVar(self)
                        self.class3_var.set(students_info[name_change].return_class3())
                        self.class3_entry = Entry(self.master,textvariable=self.class3_var)
                        self.class3_entry.grid(row=10,column=1)

                        self.class4_label = Label(text='英语成绩:',font=('微软雅黑',15))
                        self.class4_label.grid(row=11,column=0)
                        self.class4_var = StringVar(self)
                        self.class4_var.set(students_info[name_change].return_class4())
                        self.class4_entry = Entry(self.master,textvariable=self.class4_var)
                        self.class4_entry.grid(row=11,column=1)

                        self.tip = Label(text='*修改完后请点击确认修改',fg='red',font=('微软雅黑',10))
                        self.tip.grid(row=13,column=0)
                        self.button_back = Button(text='确认修改',fg='red',bg='lightblue',font=('微软雅黑',15),command=self.confirm)
                        self.button_back.grid(row=12,column=0)
                        self.button_back = Button(text='返回',fg='red',bg='lightblue',width=8,font=('微软雅黑',15),command=self.back_menu)
                        self.button_back.grid(row=12,column=1)
                        
                app = Application()     #利用前面定义的视窗类产生一个视窗对象,用于修改学生信息
                # 设置窗口标题:
                app.master.title('修改学生信息')  
                app.master.geometry('330x470+600+320')  #设定视窗的大小和位置
                # 主消息循环:
                app.mainloop()

def delete_stu():  #删除学生信息的函数
    
    name_delete = g.enterbox(msg='请输入要删除的学生的名字',title='学生管理系统 v1.1')
    if name_delete not in students_info:
        flag = g.ccbox(msg="查无此人,请确认后再输入!",title='提示信息!',choices=('继续输入','关闭'))   #用于进行输入判断循环
        if flag == 1:
            delete_stu()
        else:
            back_main_windows()
            
    else:
        students_info.pop(name_delete)
        student_info_write()  #此处一定要立即写入覆盖!
        g.msgbox(msg="删除成功!",title='提示信息!')
        back_main_windows()
        
def check_stu():   #查询学生信息的函数
    list_text_stu = []
    if User == '管理员':
        name_search = g.enterbox(msg='请输入要查询的学生的名字',title='学生管理系统 v1.1')
        if name_search not in students_info:
            flag = g.ccbox(msg="查无此人！请确认后再输入！",title='警告!',choices=('继续输入','返回'))  #用于进行输入判断循环
            if flag == 1:
                check_stu()
            else:               
                back_main_windows()
            
        else:
            #students_info[name_search].print_stu_info()            #非窗口显示方案,调用Student类的print函数
            list_text_stu.append('学生姓名: ' + students_info[name_search].return_name() + '\n')
            list_text_stu.append('性别：' + students_info[name_search].return_sex() + '\n')
            list_text_stu.append('年龄: ' + students_info[name_search].return_age() + '\n')
            list_text_stu.append('学号: ' + students_info[name_search].return_ID() + '\n')
            list_text_stu.append('学院: ' + students_info[name_search].return_apartment() + '\n')
            list_text_stu.append('专业: ' + students_info[name_search].return_major() + '\n')
            list_text_stu.append('联系电话: ' + students_info[name_search].return_tele() + '\n')
            list_text_stu.append('QQ: ' + students_info[name_search].return_QQ() + '\n')
            list_text_stu.append('专业课成绩: ' + students_info[name_search].return_class1() + '\n')
            list_text_stu.append('高数成绩: ' + students_info[name_search].return_class2() + '\n')
            list_text_stu.append('物理成绩: ' + students_info[name_search].return_class3() + '\n')
            list_text_stu.append('英语成绩: ' + students_info[name_search].return_class4() + '\n')
            list_text_stu.append('平均成绩: ' + str(students_info[name_search].return_aver()) + '\n')
            list_text_stu.append('\n')
            g.textbox(msg="以下为所查询学生的信息:",title='学生管理系统 v1.1',text=list_text_stu)
            back_main_windows()
    else:
        if (username+'\n') in list_1:
            self_name = list_1[list_1.index(username+'\n')-3].strip('\n')
        list_text_stu.append('学生姓名: ' + students_info[self_name].return_name() + '\n')
        list_text_stu.append('性别：' + students_info[self_name].return_sex() + '\n')
        list_text_stu.append('年龄: ' + students_info[self_name].return_age() + '\n')
        list_text_stu.append('学号: ' + students_info[self_name].return_ID() + '\n')
        list_text_stu.append('学院: ' + students_info[self_name].return_apartment() + '\n')
        list_text_stu.append('专业: ' + students_info[self_name].return_major() + '\n')
        list_text_stu.append('联系电话: ' + students_info[self_name].return_tele() + '\n')
        list_text_stu.append('QQ: ' + students_info[self_name].return_QQ() + '\n')
        list_text_stu.append('专业课成绩: ' + students_info[self_name].return_class1() + '\n')
        list_text_stu.append('高数成绩: ' + students_info[self_name].return_class2() + '\n')
        list_text_stu.append('物理成绩: ' + students_info[self_name].return_class3() + '\n')
        list_text_stu.append('英语成绩: ' + students_info[self_name].return_class4() + '\n')
        list_text_stu.append('平均成绩: ' + str(students_info[self_name].return_aver()) + '\n')
        list_text_stu.append('\n')
        g.textbox(msg="以下为你的基本信息:",title=('学生管理系统 v1.1  ['+ User + ']用户'),text=list_text_stu)
        back_main_windows_stu()
            
def display_all():  #显示所有学生的函数
    list_text_stu = []         #用来暂时储存students_infostudents_info中所有的学生对象的各项基本资料
    if not students_info:           #如果字典为空
        g.msgbox('当前数据库为空!')
    else:
        count = 0
        for i in students_info:   # Hash一遍students_info中的键名(即学生的名字)
            count += 1
            list_text_stu.append('学生姓名: ' + students_info[i].return_name() + '\n')   #向暂存列表list_text_stu中append字典students_info的键值obj的值
            list_text_stu.append('性别：' + students_info[i].return_sex() + '\n')
            list_text_stu.append('年龄: ' + students_info[i].return_age() + '\n')
            list_text_stu.append('学号: ' + students_info[i].return_ID() + '\n')
            list_text_stu.append('学院: ' + students_info[i].return_apartment() + '\n')
            list_text_stu.append('专业: ' + students_info[i].return_major() + '\n')
            list_text_stu.append('联系电话: ' + students_info[i].return_tele() + '\n')
            list_text_stu.append('QQ: ' + students_info[i].return_QQ() + '\n')
            list_text_stu.append('专业课成绩: ' + students_info[i].return_class1() + '\n')
            list_text_stu.append('高数成绩: ' + students_info[i].return_class2() + '\n')
            list_text_stu.append('物理成绩: ' + students_info[i].return_class3() + '\n')
            list_text_stu.append('英语成绩: ' + students_info[i].return_class4() + '\n')
            list_text_stu.append('平均成绩: ' + str(students_info[i].return_aver()) + '\n')
            list_text_stu.append('\n')
        message = "以下为所有学生信息:\n总共 " + str(count) +" 名学生!"  
        g.textbox(msg=message,title='学生管理系统 v1.1',text=list_text_stu)
    back_main_windows()

def back_main_windows():  #此函数用于返回管理员主窗口
    main = main_window()
    main.master.geometry('500x580+600+300')
    main.master.title('学生管理系统 v1.1 [管理员]')
    main.mainloop()

def back_main_windows_stu(): #此函数用于返回学生用户主窗口
    main_stu = main_window_stu()
    main_stu.master.geometry('500x580+600+200')
    main_stu.master.title('学生管理系统 v1.1 [学生用户]')
    main_stu.mainloop()

def display_aver_and_passrate(): #此函数用于显示各科平均成绩和及格率
    class AverAndPassrate(Frame):
        def __init__(self,master=None):
            Frame.__init__(self,master)
            self.createWidgets()
        def createWidgets(self):
            self.img = PhotoImage(file='王境泽1.gif')
            self.img_label = Label(self.master,image=self.img)
            self.img_label.pack()
            self.class_label = Label(self.master,text='科目',fg='red',font=('微软雅黑'))
            self.class_label.place(x=50,y=400)
            self.aver_label = Label(self.master,text='平均成绩',fg='red',font=('微软雅黑'))
            self.aver_label.place(x=180,y=400)
            self.aver_label = Label(self.master,text='及格率',fg='red',font=('微软雅黑'))
            self.aver_label.place(x=320,y=400)
            self.major_label = Label(self.master,text='专业课',font=('微软雅黑'))
            self.major_label.place(x=50,y=440)
            self.math_label = Label(self.master,text='高数',font=('微软雅黑'))
            self.math_label.place(x=50,y=490)
            self.physical_label = Label(self.master,text='物理',font=('微软雅黑'))
            self.physical_label.place(x=50,y=540)
            self.English_label = Label(self.master,text='英语',font=('微软雅黑'))
            self.English_label.place(x=50,y=590)

            self.major_var = StringVar()
            self.major_var.set(calu_aver(students_info)[0])
            self.major_aver = Label(self.master,textvariable=self.major_var,fg='blue',font=('微软雅黑',13))
            self.major_aver.place(x=200,y=440)

            self.math_var = StringVar()
            self.math_var.set(calu_aver(students_info)[1])
            self.math_aver = Label(self.master,textvariable=self.math_var,fg='blue',font=('微软雅黑',13))
            self.math_aver.place(x=200,y=490)

            self.physical_var = StringVar()
            self.physical_var.set(calu_aver(students_info)[2])
            self.physical_aver = Label(self.master,textvariable=self.physical_var,fg='blue',font=('微软雅黑',13))
            self.physical_aver.place(x=200,y=540)

            self.English_var = StringVar()
            self.English_var.set(calu_aver(students_info)[3])
            self.English_aver = Label(self.master,textvariable=self.English_var,fg='blue',font=('微软雅黑',13))
            self.English_aver.place(x=200,y=590)

            self.major_passrate_var = StringVar()
            self.major_passrate_var.set(calu_passrate(students_info)[0])
            self.major_passrate = Label(self.master,textvariable=self.major_passrate_var,fg='blue',font=('微软雅黑',13))
            self.major_passrate.place(x=340,y=440)

            self.math_passrate_var = StringVar()
            self.math_passrate_var.set(calu_passrate(students_info)[1])
            self.math_passrate = Label(self.master,textvariable=self.math_passrate_var,fg='blue',font=('微软雅黑',13))
            self.math_passrate.place(x=340,y=490)

            self.physical_passrate_var = StringVar()
            self.physical_passrate_var.set(calu_passrate(students_info)[2])
            self.physical_passrate = Label(self.master,textvariable=self.physical_passrate_var,fg='blue',font=('微软雅黑',13))
            self.physical_passrate.place(x=340,y=540)

            self.English_passrate_var = StringVar()
            self.English_passrate_var.set(calu_passrate(students_info)[3])
            self.English_passrate = Label(self.master,textvariable=self.English_passrate_var,fg='blue',font=('微软雅黑',13))
            self.English_passrate.place(x=340,y=590)
            self.button = Button(self.master,text='傲娇!',width=10,height=5,font=('微软雅黑',13),bg='pink',command=self.zhenxiang)
            self.button.place(x=440,y=460)
        def back_main_windows_new(self):
            self.root.destroy()
            if User == '管理员':
                main = main_window()
                main.master.geometry('500x580+600+200')
                main.master.title('学生管理系统 v1.1')
                main.mainloop()
            else:
                main_stu = main_window_stu()
                main_stu.master.geometry('500x580+600+200')
                main_stu.master.title('学生管理系统 v1.1')
                main_stu.mainloop()
        def zhenxiang(self):
            self.master.destroy()
            self.root = Tk()
            self.root.title("王境泽 <真香> 警告！")
            self.root.geometry('500x470+600+230')
            self.root.img = PhotoImage(file='王境泽真香.gif')
            self.root.img2 = PhotoImage(file='挠头.gif')
            self.root.img_label = Label(self.root,image=self.root.img)
            self.root.img_label.pack()
            self.root.label = Label(text='好好学习,天天向上',font=('微软雅黑',15),fg='red')
            self.root.label.place(x=170,y=430)
            self.root.button = Button(self.root,image=self.root.img2,fg='red',bg='lightblue',font=('微软雅黑',15),width=47,height=47,command=self.back_main_windows_new)
            self.root.button.place(x=220,y=370)
    windows = AverAndPassrate()
    windows.master.title('学生管理系统 1')
    windows.master.geometry('580x650+450+250')
    windows.mainloop()

def student_info_read(): #从文件中读取学生信息
    f = open('Test.txt','r')
    data = f.readlines()
    global list_1
    list_1 = []
    if data[0] == '\n':
        data.pop(0)
    for i in data:
        if i[0] == '*':
            list_1.append(i[1:])
        if i[0] == '\n':
            list_1.append(i)
    list_1.append('\n')
    flag = 0
    list_2 = []
    list_3 = []
    while flag+12<=len(list_1):
        stuobj = Student()
        list_2 = list_1[flag:flag+12]      
        stuobj.set_name(list_2[0].strip('\n'))
        stuobj.set_sex(list_2[1].strip('\n'))
        stuobj.set_age(list_2[2].strip('\n'))
        stuobj.set_id(list_2[3].strip('\n'))
        stuobj.set_apart(list_2[4].strip('\n'))
        stuobj.set_major(list_2[5].strip('\n'))
        stuobj.set_tele(list_2[6].strip('\n'))
        stuobj.set_QQ(list_2[7].strip('\n'))
        stuobj.set_class1(list_2[8].strip('\n'))
        stuobj.set_class2(list_2[9].strip('\n'))
        stuobj.set_class3(list_2[10].strip('\n'))
        stuobj.set_class4(list_2[11].strip('\n'))
        if list_2[0].strip('\n') not in list_3:
            students_info.setdefault(list_2[0].strip('\n'),stuobj)
        list_3.append(list_2[0].strip('\n'))
        flag += 13

def student_info_write(): #将学生信息写入文件
    f = open('Test.txt','w')
    f.write('\n')
    for i in students_info:
        f.write('*'+i+'\n')
        f.write('*'+students_info[i].return_sex()+'\n')
        f.write('*'+students_info[i].return_age()+'\n')
        f.write('*'+students_info[i].return_ID()+'\n')
        f.write('*'+students_info[i].return_apartment()+'\n')
        f.write('*'+students_info[i].return_major()+'\n')
        f.write('*'+students_info[i].return_tele()+'\n')
        f.write('*'+students_info[i].return_QQ()+'\n')
        f.write('*'+students_info[i].return_class1()+'\n')
        f.write('*'+students_info[i].return_class2()+'\n')
        f.write('*'+students_info[i].return_class3()+'\n')
        f.write('*'+students_info[i].return_class4()+'\n')
        f.write('\n')
    f.close()


root = login_window()
root.master.title('用户登陆')
root.master.geometry('500x500+550+300')
root.mainloop()
if User == '管理员':
    #产生主窗口对象
    main = main_window()
    #设置主窗口参数
    main.master.geometry('500x580+600+200')
    main.master.title('学生管理系统 v1.1 [管理员]')
    #主窗口进入循环
    main.mainloop()
if User == '学生':
    main_stu = main_window_stu()
    main_stu.master.geometry('500x580+600+200')
    main_stu.master.title('学生管理系统 v1.1 [学生用户]')
    main_stu.mainloop()
