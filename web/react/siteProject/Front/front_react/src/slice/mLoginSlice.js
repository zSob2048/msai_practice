import { createSlice } from '@reduxjs/toolkit'

const initialState = {
memberInfo: {},
}

const LoginInfo = createSlice({
  name: "loginSys",
  initialState,
  reducers: {
    setMemberInfo: (state, action) => {
         state.memberInfo = action.payload;
      },
  }
});

export const {setMemberInfo} = LoginInfo.actions

export default LoginInfo.reducer