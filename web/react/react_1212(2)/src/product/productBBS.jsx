// import React from 'react'
import { useState } from "react";

const ProductBBS = () => {
  //class
  // member var
  const [product, setProduct] = useState({ name: "", price: "" });
  const [products, setProducts] = useState([]);
  const productTr = products.map((p) => {
    return (
      <tr
        className="dataTr"
        onClick={() => {
          delProduct(p);
        }}
      >
        <td>{p.name}</td>
        <td>{p.price}</td>
      </tr>
    );
  });
  //method
  const changeProduct = (e) => {
    setProduct({ ...product, [e.target.name]: e.target.value });
  };
  const regProduct = () => {
    // products[products.length] = product;
    // products.push(product);
    setProducts(products.concat(product)); // 추가+ 추가된 배열 return
    setProduct({ name: "", price: "" });
  };
  const delProduct = (p) => {
    setProducts(products.filter((pp) => p.name !== pp.name));
  };

  return (
    <div id="productA">
      품명: {""}
      <input
        name="name"
        value={product.name}
        onChange={changeProduct}
        className="txtType"
      />{" "}
      <br />
      가격: {""}
      <input
        name="price"
        value={product.price}
        onChange={changeProduct}
        className="txtType"
      />{" "}
      <br />
      <button onClick={regProduct}>등록</button>
      <hr />
      <table id="procductBBSTbl" border={1}>
        <tr>
          <th>품명</th>
          <th>가격</th>
        </tr>
        {productTr}
      </table>
    </div>
  );
};

export default ProductBBS;
