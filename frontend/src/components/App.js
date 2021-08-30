import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("api/connection")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  renderMessages(messages) {
    if(messages.length === 0) {
      return null
    } else {
      return (
        <div>
          {messages.map(message => {
            return(
              <div id={message.id}>
                <p>{message.body}</p>
                <p>{message.sender_name}</p>
              </div>
            )
          })}
        </div>
      )
    }
  }

  render() {
    return (
      <div>
        {this.state.data.map(connection => {
          return (
            <div>
              <p key={connection.id}>
                {connection.name}
              </p>
              {this.renderMessages(connection.messages)}
            </div>
          );
        })}
      </div>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
