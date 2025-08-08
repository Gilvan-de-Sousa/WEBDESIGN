function tabuada()
{
    var tab = Number(document.getElementById("txtnumero").value)
    var msg = window.document.getElementById("msg")

    msg.innerHTML = ""
    for(let i = 0; i <= 10; i++){
        var res = tab * i
        msg.innerHTML += `${tab} x ${i} = ${res} <br>`
        window.document.body.style.backgroundColor="lightgreen"
    }
    
}

