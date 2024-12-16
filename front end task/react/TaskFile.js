import React, { Component } from "react";

class TaskFile extends Component{

    constructor(){
        super();
        this.state={
            count:0
        }
    }

    changeincreData = ()=>{
       
        this.setState((prevstate)=>({count:prevstate.count+1}));
    }
    changedecreData = ()=>{
      
        this.setState((prevstate)=>({count:prevstate.count-1}));
    }
    changeresetData = ()=>{
        
        this.setState((prevstate)=>({count:prevstate.count=0}));
    }
    render(){
        return(
        <div>
            <h1>Incre and Decre</h1>
            <p>count:{this.state.count}</p>
            <button onClick={()=>this.changeincreData()}>count++</button>
            <button onClick={()=>this.changedecreData()}>count--</button>
            <button onClick={()=>this.changeresetData()}>reset</button>
        </div>
        );
    }

}

export default TaskFile;