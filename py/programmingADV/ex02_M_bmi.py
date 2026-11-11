from py.zsob.zDB import ZsobDBM


class dataaa():
    def __init__(self,name,height, weight):
        self.name = name
        self.height = float(height)
        self.weight = float(weight)




class calculate():
    def bmi_calc(data):
        # con = connect("아무튼그거...")
        con , cur = ZsobDBM.op("MSAIuser/2048@195.168.9.238:1521/xe")
            
        if data.height >10:
            data.height /= 100
        data.bmi = data.weight / (data.height) ** 2
        
        if data.bmi >= 39:
            data.result = "고도 비만"
        elif data.bmi >= 32:
            data.result = "중도 비만"
        elif data.bmi >= 30:
            data.result = "경도 비만"
        elif data.bmi >= 24:
            data.result = "과체중"
        elif data.bmi >= 10:
            data.result = "정상"

        sql = "아무튼그거..."

        # cur = con.cursor()
        cur.execute(sql)
        con.commit()

        ZsobDBM.ed(con,cur)
        # cur.close()
        # con.close()
        
