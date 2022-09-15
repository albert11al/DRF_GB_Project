import React from 'react';

class TodoForms extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            'title': '',
            'users': []
        }
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    handleUsersSelect(event){
        this.setState({
            'users': event.target.value
        })
    }

    handleSubmit(event) {
        this.props.createContent(this.state.title, this.state.users)
        //console.log(this.state.title, this.state.users)
        event.preventDefault()
    }

    render () {
        return (
            <div>
                <form onSubmit={(event)=> this.handleSubmit(event)}>
                    <input type="text" name="title" placeholder="todo"
                        value={this.state.title} onChange={(event)=>this.handleChange(event)}/>
                    <select multiple onChange={(event) => this.handleUsersSelect(event)} >
                        {this.props.users.map((user) => <option value={user.id}>{user.first_name} {user.last_name}</option> )}
                    </select>
                    <input type="submit" value="Create" />
                </form>
            </div>
        )
    }
}

export default TodoForms;
