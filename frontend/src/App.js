import React from 'react';
import axios from 'axios';
import UserList from './components/UserList.js';
import ProjectList from './components/ProjectList.js';
import UserProjectList from './components/UserProjectList.js';
import TodoList from './components/TodoList.js'
import MenuList from './components/Menu.js';
import Footer from './components/Footer.js';
import {HashRouter, BrowserRouter, Route, Routes, Link, Navigate} from 'react-router-dom';


class App extends React.Component {
    menu = [
        {
            'name': 'Главная',
            'url': '/'
        },
    ]
    constructor(props) {
        super(props)

        this.state = {
            'menu': this.menu,
            'users': [],
            'projects': [],
            'todos': []
        }
    }

    componentDidMount() {
        axios
            .get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            })
            .catch(error => console.log(error))
        axios
            .get('http://127.0.0.1:8000/api/projects/')
            .then(response => {
                const projects = response.data.results
                this.setState(
                    {
                        'projects': projects
                    }
                )
            })
            .catch(error => console.log(error))
        axios
            .get('http://127.0.0.1:8000/api/todos/')
            .then(response => {
                const todos = response.data.results
                this.setState(
                    {
                        'todos': todos
                    }
                )
            })
	    .catch(error => console.log(error))
    }

    render () {
        return (
            <div>
                <BrowserRouter>
                    <MenuList list_menu={this.state.menu} />
                        <nav>
                            <ul>
                                <li>
                                    <Link to='/'>Users</Link>
                                </li>
                                <li>
                                    <Link to='/projects'>Project</Link>
                                </li>
                                <li>
                                    <Link to='/todos'>TODO</Link>
                                </li>
                            </ul>
                        </nav>
                        <div className="content">
                            <Routes>
                                <Route exact path='/' element={<UserList users={this.state.users} />} />
                                <Route exact path='/projects' element={<ProjectList projects={this.state.projects} />} />
                                <Route exact path='/todos' element={<TodoList todos={this.state.todos} />} />
                                <Route path='/users'>
                                    <Route index element={UserList users={this.state.users} />} />
                                    <Route path=':userID' element={<UserProjectList projects={this.state.projects} />} />
                                </Route>
                            </Routes>
                        </div>
                    <div className="App">
                        <Footer/>
                    </div>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
