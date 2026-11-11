import { Route, Routes } from 'react-router-dom'
import './App.css'
import SiteMain from './site/siteMain'
import Home from './site/layout/content/home/home'
import SignUpForm from './site/layout/content/member/signUpForm'
import Board from './site/layout/content/board/board'

function App() {
  return (
    <Routes>
      <Route element={<SiteMain/>}>
        <Route index element={<Home/>}/>
        <Route path="/sign.up" element={<SignUpForm/>}/>
        <Route path="/member.info" element={<SignUpForm/>}/>
        <Route path="/board" element={<Board/>}/>
      </Route>
    </Routes>
  )
}

export default App
