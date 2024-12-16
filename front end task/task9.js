

function checkdata() {
    let uname = document.myform.fname.value;
    let regName = "^[a-zA-Z]{3,20}$";

    console.log(uname);
    if (uname === "") {
        window.alert('fullname required');
        document.getElementById('fname').focus();
        return false;
    }
    if (!uname.trim().match(regName)) {
        window.alert('pattern should be correct');
        document.getElementById('fname').focus();
        return false;
    }


    let pass = document.myform.fpass.value;
    let regPass = "^.*(?=.{8,})(?=.*[a-zA-Z])(?=.*\d)(?=.*[!#$%&? ]).*$"
    if (pass.trim() === "") {
        window.alert("password Requried");
        document.getElementById("fpass").focus();
        return false;
    }

    if (!pass.match(regPass)) {
        window.alert("passoword must contains characters,numbers,special characters");
        document.getElementById("fpass").focus();
        return false;
    }
    let email = document.myform.fmail.value;
    let regMail = "^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$";
    if (email.trim() === "") {
        window.alert("email Requried");
        document.getElementById("fmail").focus();
        return false;
    }

    if (!email.match(regMail)) {
        window.alert("check your mail ");
        document.getElementById("fmail").focus();
        return false;
    }

    let contact = document.myform.fcon.value;
    let regCon = "^[7-9]{1}[0-9]{9}$"
    if (contact.trim() === "") {
        window.alert("contact Requried");
        document.getElementById("fcon").focus();
        return false;
    }

    if (!contact.match(regCon)) {
        window.alert("check your phone number ");
        document.getElementById("fcon").focus();
        return false;
    }
    let gender = document.myform.check1;
    if (gender[0].checked == false && gender[1].checked == false) {
        window.alert("Select your gender !");
        return false;
    }
    let uedu = document.myform.check;
    if (uedu[0].checked == false && uedu[1].checked == false && uedu[2].checked == false && uedu[3].checked == false) {
        window.alert("Please select qualification");
        return false;
    }


}