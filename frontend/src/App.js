import React from 'react';
import axios from 'axios';
import UserList from './components/UserList.js';
import ProjectList from './components/ProjectList.js';
import TodoList from './components/TodoList.js'
import MenuList from './components/Menu.js';
import Footer from './components/Footer.js';
import LoginForms from './components/LoginForms';
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
            'todos': [],
            'token': ''
        }
    }

    get_token(login, password) {

        axios
            .post('http://127.0.0.1:8000/api-token-auth/', {
                'username:' login,
                'password:' password
            })
            .then(response => {
                const token = response.data.token
                console.log('token:', token)
                this.setState(
                    {
                        'token': token
                    }
                )
            })
            .catch(error => console.log(error))
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
                                <li>
                                    <Link to='/login'>Login</Link>
                                </li>
                            </ul>
                        </nav>
                        <div className="content">
                            <Routes>
                                <Route exact path='/' element={<UserList users={this.state.users} />} />
                                <Route exact path='/projects' element={<ProjectList projects={this.state.projects} />} />
                                <Route exact path='/todos' element={<TodoList todos={this.state.todos} />} />
                                <Route exact path='/login' element={<LoginForms get_token={(login, password) => this.get_token(login, password)} />} />
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
