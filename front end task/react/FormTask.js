import React from 'react'
import { useState } from 'react';

const FormTask = () => {
    let mycourse = ['python','java','js','dotnet','react','angular'];
    const [user, setuser] = useState({
        fname: '',
        fpass:'',
        fmail:'',
        fcon:'',
        term: false,
        course:''
    });

    const changeip = (event) => {
        const { type, name, value, checked } = event.target;
        setuser({ ...user, [name]: type === 'checkbox' ? checked : value });

    }
    const checkData = (event) =>{
        event.preventDefault();
        if(user.fname.trim() === ""){
            window.alert('fname is required');
            return false;
        }
        if(!user.fname.trim().match("^[a-zA-Z ]{3,20}$")){
            window.alert("fname should be in correct format");
            return false;
        }
        if(user.fpass.trim() === ""){
            window.alert('fpass is required');
            return false;
        }
        if(!user.fpass.trim().match(/^.*(?=.{8,})(?=.*[a-zA-Z])(?=.*\d)(?=.*[!#$%&? ]).*$/)){
            window.alert('fpass is required in correct format');
            return false;
        }
        
        if(user.fmail.trim()===''){
            window.alert('fmail is required');
            return false;
        }
        if (!user.fmail.trim().match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
            window.alert("Enter a valid email address.");
            return false;
          }
        if(user.fcon.trim()===''){
            window.alert('fmail is required');
            return false;
        }
        if (!user.fcon.trim().match(/^[7-9][0-9]{9}$/)) {
            window.alert("Enter a valid 10-digit contact number starting with 7, 8, or 9.");
            return false;
          }
        if(user.course.trim()===''){
            window.alert('course is required');
            return false;
        }
        if(user.term===false){
            window.alert('please accept the term');
            return false;
        }
        window.alert(JSON.stringify(user));
    }
    return (
        <div>
        <h2 style={{textAlign:'center'}}>This is a form validation</h2>
        <form onSubmit={checkData} className='form'>
            <div>
                <label class="form-label">enter your firstname:</label>
                <input type='text' class="form-control" name='fname' onChange={changeip} value={user.fname}/>
            </div>
            
            <div>
                <label class="form-label">enter your password:</label>
                <input type='password' class="form-control" name='fpass' onChange={changeip} value={user.fpass}/>
            </div>
            <div>
                <label class="form-label">enter your email:</label>
                <input type='txt' class="form-control" name='fmail' onChange={changeip} value={user.fmail}/>
            </div> 
            <div>
                <label class="form-label">enter your contact:</label>
                <input type='tel' class="form-control" name='fcon' onChange={changeip} value={user.fcon}/>
            </div>
            <div>
                <label class="form-label">select your course</label>
                <select name='course' class="form-control" onChange={changeip}>
                    <option value=''>select your course</option>
                    {
                        mycourse.map((val,index)=>{
                            return <option value={val} key={index}>{val}</option>

                        })
                    }
                </select>
            </div>
            <div>
                <input type='checkbox' name='term' onChange={changeip} value={user.term}/>accept the terms & condition
            </div>
            <button type='submit'>submit</button>

        </form>
    </div>
    )
}

export default FormTask