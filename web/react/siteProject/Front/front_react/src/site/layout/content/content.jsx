import { Outlet } from "react-router-dom";

const Content = () => {
  return (
    <table id="contentA">
        <tr>
            <td align="center">
                <Outlet />
            </td>
        </tr>
    </table>
  )
}

export default Content