const contentContainer = document.getElementById('content-container')
const loginForm = document.getElementById('login-form')
const searchForm = document.getElementById('search-form')
const baseEndpoint = "http://localhost:8000/api"
if (loginForm){
    loginForm.addEventListener('submit', handleLogin)
}
if (searchForm){
    searchForm.addEventListener('submit', handleSearch)
}



function handleLogin(event) {
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`
    let loginFormData = new FormData(loginForm)
    let loginObjectData  = Object.fromEntries(loginFormData)
    // console.log(loginObjectData)
    
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body : JSON.stringify(loginObjectData)
    }
    fetch(loginEndpoint, options)
    .then(response=>{
        return response.json()
    })
    .then(authData => {
        handleAuthData(authData, getProductList)
    })
    .catch(err => {
        console.log('err', err)
    })
}

function handleSearch(event) {
    event.preventDefault()

    let formData = new FormData(searchForm)
    let data  = Object.fromEntries(formData)
    let searchParams = new URLSearchParams(data)
    const endpoint = `${baseEndpoint}/products/search/?${searchParams}`
    
    const options = {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        },
    }
    fetch(endpoint, options)
    .then(response=>{
        return response.json()
    })
    .then(data => {
        writeToContainer(data)
    })
    .catch(err => {
        console.log('err', err)
    })
}

function handleAuthData(authData, callback){
    localStorage.setItem('access', authData.access)
    localStorage.setItem('refresh', authData.refresh)
    if (callback){
        callback()
    }
}

function writeToContainer(data){
    if(contentContainer){
        contentContainer.innerHTML = "<pre>" + JSON.stringify(data, null, 4) + "<pre>"
    }
}

function getFetchOptions(method,body){
    return  {
        method : method === null ? "GET" :method,
        headers : {
            "Content-Type": "Application/json",
            "Authorization":`Token ${localStorage.getItem('access')}`
        },
        body: body ? body : null
}
}

function isTokenNotValid(jsonData){
    if (jsonData.code && jsonData.code === "token_not_valid"){
        alert("Please login again")
        return false
    }
    return true
}

function getProductList(){
    const endpoint =`${baseEndpoint}/products/`
    const options = getFetchOptions()
    fetch(endpoint, options)
    .then(response=>{
        return response.json()
    })
    .then(data=>{
        const validdata = isTokenNotValid(data)
        if (validdata) {
            writeToContainer(data)
        }
        
    })
}

getProductList()