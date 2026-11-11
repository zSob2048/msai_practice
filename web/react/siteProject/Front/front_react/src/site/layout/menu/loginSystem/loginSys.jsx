import LoginForm from './loginForm'
import LoginNow from './loginNow'

const LoginSys = () => {

  return (
    <table id="loginSysA">
      <tr>
        <td valign='top' align='center'>
          {(sessionStorage.getItem("Login") === null)?<LoginForm/>:<LoginNow/>}
        </td>
      </tr>
    </table>
  )
}

export default LoginSys