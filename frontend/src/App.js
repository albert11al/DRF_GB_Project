import React from 'react';
import axios from 'axios'
import UserList from './components/UserList.js';
import MenuList from './components/Menu.js'
import Footer from './components/Footer.js'


class App extends React.Component {
    menu = [
        {
            'name': 'Главная',
            'url': '/'
        },
        {
            'name': 'Контакты',
            'url': '/contact'
        },
    ]
    constructor(props) {
        super(props)
        this.state = {
            'menu': this.menu,
            'users': []

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
    }

    render () {
        return (
            <div>
                <MenuList list_menu={this.state.menu} />
                <div className="content">
                    <UserList users={this.state.users} />
                </div>
                <div className="App">
                    <Footer/>
                </div>
            </div>
        )
    }
}

export default App;
