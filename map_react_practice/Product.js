import React from "react"

function Product(props) {
    return (
        <div className="product">
            <h2>Name: {props.product.name}</h2>
            <p>Price: {props.product.price.toLocaleString("en-US", { style: "currency", currency: "USD" })}</p>
            <p>Description: {props.product.description}</p>
            <hr/>
        </div>
    )
}

export default Product