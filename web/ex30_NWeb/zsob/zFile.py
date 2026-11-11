from datetime import datetime
from uuid import uuid4


class zsobFileM:
    @staticmethod
    async def op(folder, file, mode):
        content = await file.read()
        filename = file.filename
        filename, type_ = filename.split(".")
        if mode == "uuid":
            ident = "_" + str(uuid4()) + "."
            
        elif mode == "date":
            ident = "_" + datetime.strftime(datetime.today(), "%Y%m%d%H%M%S") + "."

        filename = filename + ident + type_
        
        f = open(folder + filename, "wb")
        f.write(content)
        f.close()

        return filename