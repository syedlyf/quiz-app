function validate() {
    var username=document.getElementById("Username");
    var password=document.getElementById("password");
    if(username=='Mdkashif' && password=='Mohammed@2001@')
    {
        document.getElementById("login");
        return false;
    }
    else 
    {
        alert("login failed!");
    }
} validate()