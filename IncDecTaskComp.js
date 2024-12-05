import React, { Component } from "react";

class IncDecTaskComp extends Component {

    constructor(){
        super();
        this.state={
            count:0
        }
    }

    changeincData =() =>{
        // this.setState({empname:"Rupesh S",empsal:this.state.empsal+5000});
        
        this.setState((prevState) => ({count:prevState.count+1}));
    }
    changedecData  =() =>{
        // this.setState({empname:"Rupesh S",empsal:this.state.empsal+5000});
        
        this.setState((prevState) => ({count:prevState.count-1}));
    }
    changerscData =() =>{
        // this.setState({empname:"Rupesh S",empsal:this.state.empsal+5000});
        
        this.setState((prevState) => ({count:prevState.count*0}));
    }


    render() {
        return (
            <div>
                <h2>Number Switch</h2>

                <p>Count:<strong>{this.state.count}</strong></p>
                

                <button type="button" className="btn btn-primary" onClick={()=>this. changeincData ()}>Count++</button>
                <button type="button" className="btn btn-primary" onClick={()=>this. changedecData ()}>Count--</button>
                <button type="button" className="btn btn-primary" onClick={()=>this. changerscData ()}>Reset</button>
            </div>
        )
    }
}

export default IncDecTaskComp;