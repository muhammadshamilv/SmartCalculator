console.log("JavaScript Loaded");

//Simple UI Alert check
document.querySelector("form").addEventListener("submit", function(e){
    let num1 = document.getElementById("num1").value;
    let num2 = document.getElementById("num2").value;

    if(num1 === "" || num2 === ""){
        e.preventDefault();
        alert("Please enter both number....!")
    }
});