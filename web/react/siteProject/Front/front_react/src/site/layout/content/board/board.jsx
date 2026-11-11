import React from 'react'
import { useSelector } from 'react-redux';
import './board.css'

const Board = () => {
    const memberInfo = useSelector((s)=>s.loginInfo.memberInfo);
  return (
    <table id='boardA'>
        <tr>
            <th width={"40px"}>
                <img src={`http://localhost:2048/member.photo?photo=${memberInfo.photo}`}width={"35px"}/> 
            </th>
            <th>
                <textarea placeholder='새들은 지적(intelligence)이고...' type='textmode' spellcheck="false"/>
            </th>
        </tr>
        <tr>
            <td className='boardTd'>
                <img src={`http://localhost:2048/member.photo?photo=${memberInfo.photo}`}width={"35px"}/>
            </td>
            <td className='boardTd'>
                <table className='textTable'>
                    <tr><th>
                        <a> <b>글쓴사람</b> @id</a><br/>
                    </th></tr>
                    <tr><td>
                        <text>새들이왜지적인데</text>
                    </td></tr>
                    <tr><td>
                        <button> replyyyy </button>
                    </td></tr>
                </table>
            </td>
        </tr>
        <tr>
            <td>
                <img src={`http://localhost:2048/member.photo?photo=${memberInfo.photo}`}width={"35px"}/>
            </td>
            <td>
                <a> <b>글쓴사람</b> @id</a><br/>
                <text>
                    긴글 <br/>
                    긴글 <br/>
                    긴글 <br/>
                    긴글 <br/>
                    긴글 <br/>
                    긴글 <br/>
                    이못생긴건뭐지 <br/>
                    아 갈아엎고싶은데?? 못생겼는데??
                </text>
                <a> 댓글 </a>
            </td>
        </tr>
    </table>
  )
}

export default Board