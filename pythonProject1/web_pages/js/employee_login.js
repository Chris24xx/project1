const username = document.getElementById("usernameInput")
const password = document.getElementById("passwordInput")

async function login(){
    let response = await fetch(
        /** first add the url and then make object litteral */
        "http://127.0.0.1:5000/project1/employee/login", {
            method: "POST",
            //include content type so the program knows what it is dealing with
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({"username":username.value, "password":password.value})
        }
    )
     
     if (response.status === 200){
        // I convert the response body from a json into an object literal
        let body = await response.json()
        console.log(body)
        if (body ==="success"){
            window.location.href = "employee_home_page.html"
        } else {
            alert("login failed: please try again")
        }
    } else {
        alert("the request failed")
    }
    
}
// function getinfo(){
//     let url = "http://127.0.0.1:5000/project1/employee/info"
//     let response = await fetch(url);
//     if (response.status === 200){
//         let body = await response.JSON();
//         console.log(body)
//     }
// }
// function saveId(responseBody){
//     let id;
// }