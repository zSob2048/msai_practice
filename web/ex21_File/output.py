from uuid import uuid4
from fastapi import FastAPI,Form, UploadFile
from fastapi.responses import FileResponse, HTMLResponse

from web.ex21_File.zsobFileManager import zsobFileM


app = FastAPI()

# 인코딩 한 값을 알아서 원상복귀(디코딩)
# 파일 업로드의 경우
# 1 인코딩 방식이 바뀌어서...
#   pip install python-multipart
# 2 파일이 업로드 될 폴더 확보(서버에서)
#   서버에서 폴더를 만들어야겠지만... > 서버를 쓸 수 없는 상황이라면?
#   작업 끝난 프로젝트 통째로 서버로 보낼테니
#   미리 폴더 만들어두자 + 상대경로로 적자
# 3 요청-응답을 동기식으로 > async - await
#  fastapi의 경우 기본적으로 비동기식 추구
# > 파일의 경우 용량이 크기 때문에 업로드에 시간이 필요
# >> 비동기식의 경우 파일이 다 업로드되지 않았는데 다음 작업 시작
# >>> 파일 짤림


@app.post("/file.upload")
async def fileUpload(photo:UploadFile, zipp:UploadFile, title: str=Form()):
    folder_img = "./upimg/"
    filename_img = await zsobFileM.op(folder_img,photo,"uuid")
    folder_zip = "./upzip/"
    filename_zip = await zsobFileM.op(folder_zip,zipp,"date")
    
    # folder = "./upimg/" # 이미지 폴더 상대경로
    # content = await photo.read() # 파일 다 읽을때까지 wait

    # folder2 = "./upzip/"
    # content2 = await zipp.read() 
    
    # # 파일 이름 중복의 경우...?

    # filename = photo.filename
    # type_ = filename[-4:] # 확장자(3자기준)
    # filename = filename.replace(type_,"")

    # filename = filename + "_" + str(uuid4()) + type_
    
    # filename2 = zipp.filename2
    # type2_ = filename2[-4:]
    # filename2 = filename2.replace(type2_,"")

    # filename2 = filename2 + "_" + str(uuid4()) + type2_

    # # uuid ; 범용 고유 식별자 > 이거 많이 씀
    # # 현재시간 / DB seq / 로그인 아이디 등... 중복처리


    # f = open(folder + filename, "wb") # w(rite) b(inary) : 파일
    # f.write(content)
    # f.close()

    # f = open(folder2 + filename2, "wb")
    # f.write(content2)
    # f.close()



    html = '<html><head><meta charset="utf-8"></head><body>' \
    '<h1>%s</h1> ' \
    '<h1>%s</h1> ' \
    '<img src="img.get?fname=%s"> ' \
    '<a href="zip.get?fname=%s>다운로드</a>' \
    '</body></html>' % (title,filename_img,filename_img)
    return HTMLResponse(html)

# 요청하면 파일을 응답...
# ~~~~/img.get?fname=aaaa.png
@app.get("/img.get")
def imgPrint(fname:str):
    folder = "./upimg/"
    return FileResponse(folder+fname,filename=fname)

@app.get("/zip.get")
def zipPrint(fname:str):
    folder = "./upzip/"
    return FileResponse(folder+fname,filename=fname)