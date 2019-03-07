class Car:
    def __init__(self,car_id,name,is_lend,\
                  price,start_data,end_data,):
        self.car_id = car_id
        self.name = name
        self.is_lend = is_lend
        self.price = price
        self.start_data = start_data
        self.end_data =end_data
    
    def __str_car__(self):
        while True:
            l = []
            car_id = int(input("请输入汽车id"))
            if car_id == " ":
                break
            else:
                l.append(car_id)    
                name = input("汽车名称")
                l.append(name)
                is_lend = input("是否出租")
                l.append(is_lend)
                price = int(input("每天单价"))
                l.append(price)
                start_date = int(input("起租日期"))
                l.append(start_date)
                end_date = int(input("终止日期"))
                l.append(end_date)        
                L1 = {}
                L1.update(name = l)
                global L1
    return L1
        

class Customer:
    def __init__(self,cust_id,cust_name,tel_no):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.tel_no = tel_no
    
    def __str_cust__(self,l):
        while True:
            l = []
            cust_id = int(input("请输入客户编号"))
            if cust_id == " ":
                break
            else:
                l.append(cust_id)    
                cust_name = input("客户姓名")
                l.append(cust_name)
                tel_no = int(input("客户电话"))
                l.append(tel_no)       
                L2 = {}
                L2[cust_name] = l
                global L2
    return L2

class CarStore(Car,Customer):
    def __init__(self,cars,customers):
        self.cars = cars = L1
        self.customers = customers = L2

    def __load_cars(self):
        print("正在加载所有车辆列表") 

    def __load_customers(self):
        print("正在加载所有客户信息")  

    def print_cars_info(self):
        print(L1) 

    def find_car(self):
        n = input("请输入查找车辆名称")
        if n in L1.key():
            print(L1[n])
        else:
            print("没有此车辆")

    def add_car(self):
        str_car() 

    def del_car(self):
        m = input("请输入要删除车辆名称")
        if m in L1.key():
            print("有此车")
            L1.pop(m)
            print("此车已删除")
        else:
            print("没有此车辆") 

    def lend(self):
        x = input("请输入要的租车的名称:")
        if x in self.cars:
            if "是" in self.cars[x]:
                print("此车可以借")
            else:
                print("此车已借出")
        else:
            print("此车不存在")



    def back(self):
        y = input("请输入要的租车的名称:")
        if y in self.cars:
            if "否" in self.cars[y]:
                print("此车可以还")
            else:
                print("此车未到归还日期")
        else:
            print("此车不存在")

if __name__ == "__main__":
t = Car("1","雪佛兰","是","500","2018","2019")
t.__str_car__()
t.CarStore(L1,L2)
t.find_car()