import React, { Component, TextInput } from 'react';
import './App.css';
import Header from './Components/Header';

class App extends Component {
  render() {
    return (
      <div className="App">
       <h1>My App</h1>
       <p>What's next?</p>
       <p>Here is the another step.</p>

       <Header/>


      </div>
    );
  }
}

export default App;
