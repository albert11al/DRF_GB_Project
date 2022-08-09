import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/UserList.js';

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': []
        }
    }
    componentDidMount() {
        const users = [
            {
                "first_name": "dlon",
                "last_name": "brovic",
                "birthday_year": 1896,
                "email": "a@a.com"
            },
            {
                "first_name": "alon",
                "last_name": "kombo",
                "birthday_year": 1985,
                "email": "ad@em.com"
            },
            {
                "first_name": "drinc",
                "last_name": "pilovic",
                "birthday_year": 2000,
                "email": "tren@ren.com"
            }
        ]
        this.setState(
            {
                'users': users
            }
        )
    }

    render () {
        return (
            <div>
                <UserList users={this.state.users} />
            </div>
        )
    }
}

export default App;
