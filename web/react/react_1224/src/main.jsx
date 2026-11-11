import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import { configureStore } from '@reduxjs/toolkit'
import { Provider } from "react-redux";
import h1SizeSlice from './h1SizeSlice.js';
import h2TxTSlice from './h2TxTSlice.js';

const storee = configureStore({
reducer:{
  sizee : h1SizeSlice,
  txt : h2TxTSlice
}
});

createRoot(document.getElementById('root')).render(
  <Provider store={storee}>
    <App />
  </Provider >,
)
