async function view_requests(){
    let manager_id = document.getElementById("id-2")
    url = `http://127.0.0.1:5000/project1/manager/requests/pending/${manager_id.value}`
    let response = await fetch(url)
    if (response.status === 200){
        let body = await response.json();
        console.log(body);
        viewRequestsForPending(body)
    }
}

function viewRequestsForPending(json){
    let list = document.getElementById("requests");
        let Array = json;
        for (let i of Array){
            let listHolder = document.createElement("li")
            listHolder.innerHTML = i
            console.log(i)
            for(j of i){
                listHolder.textContent = "Requests " + i[0] + " Reason: " + i[1] +  " Request Id: " + i[2] + " Employee Id: " + i[3];
                list.appendChild(listHolder);
            } 
        }
}
async function updateRequest() {
    let requests = document.getElementById("r-id")
    let status = document.getElementById("status")
    let comment = document.getElementById("comment")
    let response = await fetch(
        `http://127.0.0.1:5000/project1/manager/requests/response/${requests.value}` , {
            method: "PATCH",
            headers:{"Content-Type": "application/json"},
            body:JSON.stringify({"status": status.value, "comment": comment.value,})
        }
    )
    if (response.status === 200){
        let body = await response.json()
        console.log(body)
        alert("Success")      
    }else{
        alert("could not complete the request!")
    }
    
}
async function viewAllRequests(){
    let manager_id = document.getElementById("m-id3")
    url = `http://127.0.0.1:5000/project1/manager/requests/all/${manager_id.value}`
    let response = await fetch(url)
    if (response.status === 200){
        let body = await response.json();
        console.log(body);
        viewRequests(body)
    }
}

function viewRequests(json){
    let list = document.getElementById("all_requests");
        let Array = json;
        for (let i of Array){
            let listHolder = document.createElement("li")
            listHolder.innerHTML = i
            console.log(i)
            for(j of i){
                if(i[1] == false){
                    listHolder.textContent = "Requests " + i[0] + " Status: Denied "  +  " Employee Id: " + i[2] + " Comment: " + i[3];
                    list.appendChild(listHolder);
                }if(i[1] == true){
                    listHolder.textContent = "Requests " + i[0] + " Status: Approved "  +  " Employee Id: " + i[2] + " Comment: " + i[3];
                    list.appendChild(listHolder);
                }
            }
        }
}
async function statistic() {
    let manager_id = document.getElementById("m-id4")
    let sum = document.getElementById("selectChoice1")
    let max = document.getElementById("selectChoice2")
    let min = document.getElementById("selectChoice3")
    let avg = document.getElementById("selectChoice4")
    let freq = document.getElementById("selectChoice5")
    if(sum.checked){
        url = `http://127.0.0.1:5000/project1//manager/requests/view/statistics/add/${manager_id.value}`
        let response = await fetch(url)
        if(response.status === 200){
            let body = await response.json();
            populate(body)
        }
    }if(max.checked){
        url = `http://127.0.0.1:5000/project1//manager/requests/view/statistics/max/${manager_id.value}`
        let response = await fetch(url)
        if(response.status === 200){
            let body = await response.json();
            populate(body)
        }
    }if(min.checked){
        url = `http://127.0.0.1:5000/project1//manager/requests/view/statistics/min/${manager_id.value}`
        let response = await fetch(url)
        if(response.status === 200){
            let body = await response.json();
            populate(body)
        }
    }if(avg.checked){
        url = `http://127.0.0.1:5000/project1//manager/requests/view/statistics/avg/${manager_id.value}`
        let response = await fetch(url)
        if(response.status === 200){
            let body = await response.json();
            console.log(body)
            populate(body)
        }
    }if(freq.checked){
        url = `http://127.0.0.1:5000/project1//manager/requests/view/statistics/freq/${manager_id.value}`
        let response = await fetch(url)
        if(response.status === 200){
            let body = await response.json();
            console.log(body)
            populate(body)
        }
    }  
}
function populate(json){
    info = document.getElementById("returnedInfo")
    newInfo = document.createTextNode(json)
    info.appendChild(newInfo)
}