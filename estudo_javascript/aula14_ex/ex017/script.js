function tabuada()
{
    var numero = Number(document.getElementById("txtnumero").value)
    var msg = window.document.getElementById("msg")

    msg.innerHTML = ""
    if(numero == 0){
        alert("Informe um valor válido!")
    }else {
        for(let i = 0; i <= 10; i++){
        var res = numero * i
        msg.innerHTML += `${numero} x ${i} = ${res} <br>`
        window.document.body.style.backgroundColor="lightgreen"
        }
    }
     
}

