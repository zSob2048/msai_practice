import {Route, Routes} from "react-router-dom"
import './App.css'
import SiteLayout from "./site/siteLayout"
import Home from "./site/home"
import Menu1 from "./site/menu/menu1"
import Menu2 from "./site/menu/menu1"

function App() {
  return (
    <>
      <Routes>
        <Route element={<SiteLayout/>}>
          <Route path="/" element={<Home/>}/>
          <Route path="/me.nu1" element={<Menu1/>}/>
          <Route path="/me.nu2" element={<Menu2/>}/>
        </Route>
      </Routes>
    </>
  )
}

export default App
