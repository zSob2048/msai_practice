import React from 'react'

const SiteLayout = () => {
  return (
    <table id='site'>
        <tr>
            <td id="siteTitle">Dec23</td>
        </tr>
        <tr>
            <td id="siteMenuArea">
                <Link to="/">Home</Link>
                <Link to="/me.nu1">Menu1</Link>
                <Link to="/me.nu2">Menu2</Link>
            </td>
        </tr>
    </table>
  )
}

export default SiteLayout