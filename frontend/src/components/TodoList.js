import React from 'react'

const TodoItem = ({todo, deleteTodo}) => {
    return (
        <tr>
            <td>
                <button onClick={() => deleteTodo(todo.id) }>Delete</button>
            </td>
            <td>
                {todo.project}
            </td>
            <td>
                {todo.text_todo}
            </td>
            <td>
                {todo.creating}
            </td>
            <td>
                {todo.updating}
            </td>
            <td>
                {todo.user_note}
            </td>
            <td>
                {todo.is_active}
            </td>
        </tr>
    )
}

const TodoList = ({todos, deleteTodo}) => {
    return (
        <table>
            <th>
                Project
            </th>
            <th>
                Text TODO
            </th>
            <th>
                Creating
            </th>
            <th>
                Updating
            </th>
            <th>
                User note
            </th>
            <th>
                Is active
            </th>
            {todos.map((todo) => <TodoItem todo={todo} deleteTodo={deleteTodo}/>)}
        </table>
    )
}
export default TodoList