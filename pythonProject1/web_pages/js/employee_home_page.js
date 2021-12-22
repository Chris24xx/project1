const employee_id = document.getElementById("e-id");
const manager_id = document.getElementById("m-id");
let reason = document.getElementById("r");
let request = document.getElementById("amount")

async function createRequest(){
    let response = await fetch(
        `http://127.0.0.1:5000/project1/employee/requests/create/${employee_id.value}/${manager_id.value}` , {
            method: "POST",
            headers:{"Content-Type": "application/json"},
            body:JSON.stringify({"employee_id":employee_id.value, "manager_id":manager_id.value,"reason":reason.value, "requests":request.value})
        }
    )
    if (response.status === 200){
        let body = await response.json()
        console.log(body)
        alert("success")
    }else{
        alert("could not complete the request!")
    }
            
}

async function view_requests(){
    let employee_id = document.getElementById("id-2")
    url = `http://127.0.0.1:5000/project1/requests/all/${employee_id.value}`
    let response = await fetch(url)
    if (response.status === 200){
        let body = await response.json();
        console.log(body);
        viewRequests(body)
    }
}

function viewRequests(json){
    let list = document.getElementById("requests");
        let Array = json;
        for (let i of Array){
            let listHolder = document.createElement("li")
            listHolder.innerHTML = i
            console.log(i)
            for(j of i){
                if(i[1] == false){
                    listHolder.textContent = "requests " + i[0] + " status: Denied";
                    list.appendChild(listHolder); 
                }if(i[1] == true){
                    listHolder.textContent = "requests " + i[0] + " status: Approved";
                    list.appendChild(listHolder);
                }if(i[1] == null){
                    listHolder.textContent = "requests " + i[0] + " status: Pending";
                    list.appendChild(listHolder);
                }
            }
        }
}