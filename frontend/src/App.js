import React from 'react';
import axios from 'axios';
import UserList from './components/UserList.js';
import ProjectList from './components/ProjectList.js';
import TodoList from './components/TodoList.js'
import MenuList from './components/Menu.js';
import Footer from './components/Footer.js';
import LoginForms from './components/LoginForms';
import TodoForms from './components/TodoForms';
import ProjectForms from './components/ProjectForms';
import {HashRouter, BrowserRouter, Route, Routes, Link, Navigate, useLocation} from 'react-router-dom';

const NotFound = () => {
    var {pathname} = useLocation()

    return (
        <div>
            Page "{pathname}" not found
        </div>
    )
}

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

    deleteTodo(todoId) {
        let headers = this.getHeaders()

        axios
            .delete(`http://127.0.0.1:8000/api/todos/${todoId}`, {headers})
            .then(response => {
                this.setState({
                    'todos': this.state.todos.filter((todo) => todo.id != todoId)
                })
            })
            .catch(error => {
                console.log(error)
            })
//        console.log(bookId)
    }

    createContent(title, users) {
        //console.log(title, users)

        let headers = this.getHeaders()

        axios
            .post('http://127.0.0.1:8000/api/todos/', {'title': title, 'users': users}, {headers})
            .then(response => {
                this.getData()
            })
            .catch(error => {
                console.log(error)
            })
    }

    obtainAuthToken(username, password) {
        axios
            .post('http://127.0.0.1:8000/api-token-auth/', {
                'username:' username,
                'password:' password
            })
            .then(response => {
                const token = response.data.token
                console.log('token:', token)
                localStorage.setItem('token', token)
                this.setState(
                    {
                        'token': token
                    }, this.getData
                )
            })
            .catch(error => console.log(error))
    }

    isAuth(){
        return this.state.token != ''
    }

    componentDidMount() {
        let token = localStorage.getItem('token')
        this.setState(
            {
                'token': token
            }, this.getData
        )
    }

    getHeaders(){
        if (this.isAuth()){
            return {
                'Authorization': 'Token ' + this.state.token
                'Accept': 'application/json; version=v2',
            }
        }
        return {}
    }

    getData(){
        let headers = this.getHeaders()
        axios
            .get('http://127.0.0.1:8000/api/users/', {'headers': headers})
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            })
            .catch(error => {
                console.log(error)
                this.setState({'users': []})
            )}
        axios
            .get('http://127.0.0.1:8000/api/projects/', {'headers': headers})
            .then(response => {
                const projects = response.data.results
                this.setState(
                    {
                        'projects': projects
                    }
                )
            })
            .catch(error => {
                console.log(error)
                this.setState({'projects': []})
            )}
        axios
            .get('http://127.0.0.1:8000/api/todos/', {'headers': headers})
            .then(response => {
                const todos = response.data.results
                this.setState(
                    {
                        'todos': todos
                    }
                )
            })
	    .catch(error => {
                console.log(error)
                this.setState({'todos': []})
            )}
    }

    logout(){
        localStorage.setItem('token', '')
        this.setState(
            {
                'token': '',
            }, this.getData
        )
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
                                    <Link to='/create_project'>Create project</Link>
                                </li>
                                <li>
                                    <Link to='/create_todo'>Create todo</Link>
                                </li>
                                <li>
                                    {this.isAuth() ? <button onClick={() => this.logOut()}>Logout</button> : <Link to='/login'>Login</Link> }
                                </li>
                            </ul>
                        </nav>
                        <div className="content">
                            <Routes>
                                <Route exact path='/' element={<UserList users={this.state.users} />} />
                                <Route exact path='/projects' element={<ProjectList projects={this.state.projects} />} />
                                <Route exact path='/create_todo' element={<TodoForms users={this.state.users} createContent={(title, users) => this.createContent=(title, users)}/>} />
                                <Route exact path='/create_project' element={<ProjectForms users={this.state.users} createContent={(title, users) => this.createContent(title, users)}/>} />
                                <Route exact path='/todos' element={<TodoList todos={this.state.todos} users={this.state.users} deleteTodo={(todoId) => this.deleteTodo(todoId)}/>} />
                                <Route exact path='/login' element={<LoginForms obtainAuthToken={(username, password) => this.obtainAuthToken(username, password)} />} />
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
