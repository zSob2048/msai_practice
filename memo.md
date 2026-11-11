import axios from 'axios';
import { Provider } from "react-redux";

import {Link} from "react-router-dom"

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontF = "C:\Windows\Fonts\gulim.ttc"
fontN = fm.FontProperties(fname=fontF, size= 10).get_name()
plt.rc("font", family=fontN)
plt.rcParams["axes.unicode_minus"]=False

---------------------------------

git pull --rebase origin main

git fetch origin
git rebase origin/main

# 충돌 해결 후
git add .
git rebase --continue

# 포기하려면
git rebase --abort

git status
: 변경 파일 확인용
git add .
: 전체 스테이징/개별의경우 .대신 파일명
git commit -m "fix: 응답의 일부만 출력하는 현상 관련 프롬프트 추가"
git push origin CHANG
여기까지 branch에 push

git push origin CHANG --force
: 강제push

pr은 웹페이지에서하는데 더 좋은 방안이 있을수도

---------------------------------

react

yarn create vite
        이거저거 하라는대로
yarn add axios
yarn add react-router-dom
yarn add @reduxjs/toolkit
yarn add react-redux

yarn dev : localhost만
yarn dev --host : IP 가능
배포 // yarn build > dist 폴더


-----------

FastAPI
폴더에서 cmd
uvicorn 파일명:app --host=0.0.0.0 --port=2048 --reload
uvicorn defaulttest:app --host=0.0.0.0 --port=2048 --reload

from fastapi import FastAPI

app=FastAPI()

@app.get("/t.s")
def test():
    return {1:0}


----------------------------

rafce class생성
anfn  X→Y
nfn f:X→Y
enf export f:X→Y

usss useState
urds useReduce
rxs reduxslice

