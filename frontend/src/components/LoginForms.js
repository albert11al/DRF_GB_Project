import React from 'react';

class LoginForms extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            'login': '',
            'password': ''
        }
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    handleSubmit(event) {
        console.log(this.state.login, this.state.password)
        event.preventDefault()
    }

    render () {
        return (
            <div>
                <form onSubmit={(event)=> this.handleSubmit(event)}>
                    <input type="text" name="login" placeholder="login"
                        value={this.state.login} onChange={(event)=>this.handleChange(event)}/>
                    <input type="password" name="password" placeholder="password"
                        value={this.state.password} onChange={(event)=>this.handleChange(event)}/>
                    <input type="submit" value="Login" />
                </form>
            </div>
        )
    }
}

export default LoginForms;
