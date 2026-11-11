import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import { configureStore } from '@reduxjs/toolkit'
import { Provider } from "react-redux";
import LoginInfo from "./slice/mLoginSlice.js"
import { BrowserRouter } from 'react-router-dom';

const allStore = configureStore({
  reducer:{
    loginInfo : LoginInfo
  }
});

createRoot(document.getElementById('root')).render(
  <Provider store={allStore}>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </Provider >,
)
