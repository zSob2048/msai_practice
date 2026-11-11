class zStr:
    @staticmethod
    def cut(txt):
        txt = txt.replace("<b>", "")
        txt = txt.replace("</b>", "")
        txt = txt.replace("&quot;", "")
        return txt