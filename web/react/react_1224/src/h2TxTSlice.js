import { createSlice } from '@reduxjs/toolkit'

const initialState = {
    txt: "InputTest"
}

const h2TxTSlice = createSlice({
  name: "Itest",
  initialState,
  reducers: {inputTxt: (st,act)=>{st.txt=act.payload},
    
  }
});

export const {inputTxt} = h2TxTSlice.actions

export default h2TxTSlice.reducer