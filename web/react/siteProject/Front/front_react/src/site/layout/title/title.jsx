import {Link} from "react-router-dom"

const Title = () => {
  return (
    <table id="titleA">
        <tr>
            <td align="center">
                <table id="title">
                    <tr>
                        <td>
                            <Link to="/">Title</Link>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
  )
}

export default Title