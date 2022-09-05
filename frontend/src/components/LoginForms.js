import React from 'react';

class LoginForms extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            'username': '',
            'password': ''
        }
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    handleSubmit(event) {
        this.props.obtainAuthToken(this.state.username, this.state.password)
        //console.log(this.state.username, this.state.password)
        event.preventDefault()
    }

    render () {
        return (
            <div>
                <form onSubmit={(event)=> this.handleSubmit(event)}>
                    <input type="text" name="username" placeholder="login"
                        value={this.state.username} onChange={(event)=>this.handleChange(event)}/>
                    <input type="password" name="password" placeholder="password"
                        value={this.state.password} onChange={(event)=>this.handleChange(event)}/>
                    <input type="submit" value="Login" />
                </form>
            </div>
        )
    }
}

export default LoginForms;
