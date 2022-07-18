import React from "react"
import ReactDOM from "react-dom"


function MyInfo() {
    return (
    <div>
        <h1>Morgan Baccus</h1>
        <p>This is the stuff about me</p>
        <ul>
            <li>Disney World</li>
            <li>Cruise</li>
            <li>Arizona</li>
        </ul>
    </div>
    )
}

ReactDOM.render(
    <MyInfo />,
    document.getElementById("root")
)