import React from 'react';

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

const ProjectList = ({projects}) => {
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
            {projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}
export default ProjectList