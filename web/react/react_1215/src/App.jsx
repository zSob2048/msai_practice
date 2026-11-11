
import KeybordEvent from './event/keybordEvent'
import MouseEvent from './event/MouseEvent'
import HookFtn from './event/hookftn'
import ResizeEv from './event/resizeEv'
import ScrollEv from './event/scrollEv'
import External from './event/eXternal'

function App() {

  return (
    <>
      <MouseEvent /> <hr/>
      <KeybordEvent /> <hr/>
      <ResizeEv/> <hr/>

      <HookFtn /> <hr/>
      <ScrollEv/> <hr/>
      <External/>
    </>
  )
}

export default App
