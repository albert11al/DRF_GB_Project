import React from 'react';
import { useParams } from 'react-router-dom'


const ProjectItem = ({project}) => {
    return (
        <tr>

            <td>
                {project.name_todo}
            </td>
            <td>
                {project.link_repository}
            </td>
            <td>
                {project.users_work}
            </td>
        </tr>
    )
}

const UserProjectList = ({projects}) => {

    let {userID} = useParams()
    let filtered_user = projects.filter((project) => project.users.includes(parseInt(userID)))
    return (
        <table>
            <th>
                Name TODO
            </th>
            <th>
                Link repository
            </th>
            <th>
                User work
            </th>
            {filtered_user.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}
export default UserProjectList