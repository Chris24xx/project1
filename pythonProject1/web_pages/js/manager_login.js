const username = document.getElementById("usernameInput")
const password = document.getElementById("passwordInput")

async function login(){
    let response = await fetch(
        /** first add the url and then make object litteral */
        "http://127.0.0.1:5000/project1/manager/login", {
            method: "POST",
            //include content type so the program knows what it is dealing with
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({"username":username.value, "password":password.value})
        }
    )
     // assuming I get a 200 status code in the response...
     if (response.status === 200){
        // I convert the response body from a json into an object literal
        let body = await response.json()
        if (body === "success"){
            window.location.href = "manager_home_page.html"
        } else {
            alert("login failed: please try again")
        }
    } else {
        alert("the request failed")
    }
}