// state: 상태
// reducer: 기존 state값 + 새로운 값 넣어주면 새 state return
// action: 액션
// slice : reducer+action

// subscriber : state를 사용하는 존재(여기서 h1)
// dispatcher : state를 바꿔줄 존재(버튼 등)

// >> main의 store에 등록된 slice 사용 

import { createSlice } from '@reduxjs/toolkit'

const initialState = {
    fontSize:30
}

const h1SizeSlice = createSlice({
  name: "sizeslice",
  initialState,
  reducers: {
    // 객체로 함수명: (curState, action) => {}
    sizeUp : (curSt) => { curSt.fontSize+=10;},
    sizeDown : (curSt) => { curSt.fontSize-=10;},
  }
});

export const {sizeUp,sizeDown} = h1SizeSlice.actions
export default h1SizeSlice.reducer