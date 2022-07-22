import React from "react"
import ToDoItem from "./ToDoItem"

function List() {
    return (
        <ul className="todo-list">
            <ToDoItem />
            <ToDoItem />
            <ToDoItem />
            <ToDoItem />
        </ul>
    )
}

export default List