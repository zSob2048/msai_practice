from datetime import datetime
from os import remove
from fastapi.responses import FileResponse, JSONResponse

from fileeee.zFileM import zFile
from fileeee.zDBM import zDB


class FileUpSimul:
    async def uppppp(self,img,title):
        fileN = await zFile.op("./fileeee/files/",img,"uuid")
        h = {"Access-Control-Allow-Origin":"http://localhost:5173",
             "Access-Control-Allow-Credentials":"true"}
        print(title)
        return JSONResponse({"title": title, "imgn":fileN},headers=h)
    
    def backkk(self,fileN):
        return FileResponse("./fileeee/files/"+fileN,filename=fileN)
    
########################################################################

    # async def upR(self,img,id,pw,txt):
    #     imgn = await zFile.op("./fileeee/files/",img,"uuid")
    #     h = {"Access-Control-Allow-Origin":"http://localhost:5173",
    #          "Access-Control-Allow-Credentials":"true"}
    #     return JSONResponse({"id": id,"pw":pw, "imgn":imgn},headers=h)
    
    def rPimg(self,fileN):
        return FileResponse("./fileeee/files/"+fileN,filename=fileN)
    
    def __init__(self):
        self.inPnum = 5
        self.post_all
        self.imgpath = "./fileeee/files/"
        self.headerall = {"Access-Control-Allow-Origin":"*"}
        self.headerlocal = {"Access-Control-Allow-Origin":"http://localhost:5173", 
                            "Access-Control-Allow-Credentials":"true"}

    def post_all(self):
        try: 
            con,cur = zDB.op("MSAIuser/2048@195.168.9.194:1521/xe")
            sql = "SELECT count(*) FROM post1219"
            cur.execute(sql)
            for c in cur:
                self.allPnum = c[0]
        except Exception as e:
            print(e)
        finally:
            zDB.ed(con,cur)

    

    async def regDB(self,id,pw,txt,img):
        imgn = await zFile.op("./fileeee/files/",img,"uuid",1000)
        print(imgn)
        if imgn == "fail":
            return JSONResponse({"result" : "용량 초과"},headers=self.headerlocal)
        
        try:
            
            con,cur = zDB.op("MSAIuser/2048@195.168.9.194:1521/xe")

            sql = "INSERT INTO post1219 values('%s','%s','%s','%s',sysdate)" %(id,pw,txt,imgn)
            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                print(self.allPnum)
                self.allPnum += 1
                return JSONResponse({"result" : id + " 등록 성공"},headers=self.headerlocal)
            return JSONResponse({"result" : id + " 등록 실패"},headers=self.headerlocal)
        except:
            remove(self.imgpath+imgn)
            return JSONResponse({"result" : id + " 등록 실패"},headers=self.headerlocal)

        finally:
            zDB.ed(con,cur)
            

    def getDB(self, page, txt):
        # if self.inPnum * (int(page)-1) > self.allPnum:
        #     return {"result" : "end"}
        try:
            con,cur = zDB.op("MSAIuser/2048@195.168.9.194:1521/xe")
            txt = "%" + txt + "%"
            sql = "SELECT * FROM (" \
            "SELECT rownum AS rn , m_id, m_pw, m_txt,m_img, m_time FROM(" \
            "SELECT * FROM post1219 WHERE (m_txt LIKE '%s') ORDER BY m_time) )" \
            "WHERE rn>%d AND rn<=%d" % (txt, self.inPnum * ( int(page) - 1) , self.inPnum * int(page))
            cur.execute(sql)

            posts = []
            for _, id, pw, txtt,img, utime in cur:
                utime = datetime.strftime(utime, "%Y/%m/%d %H:%M")
                posts.append({"id":id, "pw":pw,"ptxt":txtt, "imgn":img, "uptime":utime})
            return JSONResponse(posts,headers=self.headerall)

        except Exception as e:
            print(e)
            return JSONResponse({"result" : "err" },headers=self.headerall)
        finally:
            zDB.ed(con,cur)

    def delete(self,id,imgn):
        try:
            con,cur = zDB.op("MSAIuser/2048@195.168.9.194:1521/xe")
            sql = "DELETE FROM post1219 WHERE m_id = '%s'" % id
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                self.allPnum -= 1
                remove("./fileeee/files/"+imgn)


                return {"result" : " 삭제 성공" }
            # return {"result" : " 이미 삭제된 게시글 "}
            raise # 아래줄 강제 발생
        except:
            
            return {"result" : " 삭제 실패 "}
        finally:
            zDB.ed(con,cur)