import React from "react"

function Joke(props) {
    style1 = {display: props.question ? "block" : "none"}
    return (
        <div>
            <h2>Here's a new joke: </h2>
            <p style={style1} >Question: {props.question}</p>
            <p>Answer: {props.punchLine}</p>
            <hr/>
        </div>
    )
}

export default Joke