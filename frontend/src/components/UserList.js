import React from 'react';
import {Link} from 'react-router-dom';

const ProjectItem = ({user}) => {
    return (
        <tr>
            <td>
                {user.first_name}
            </td>
            <td>
                <Link> to={`/users/${user.id}`}> {user.last_name} </Link>
            </td>
            <td>
                {user.birthday_year}
            </td>
            <td>
                {user.email}
            </td>
        </tr>
    )
}

const ProjectList = ({users}) => {
    return (
        <table>
            <th>
                First name
            </th>
            <th>
                Last Name
            </th>
            <th>
                Birthday year
            </th>
            <th>
                email
            </th>
            {users.map((user) => <ProjectItem user={user} />)}
        </table>
    )
}
export default ProjectList
