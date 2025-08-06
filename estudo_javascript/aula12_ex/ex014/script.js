// alert("Olá")

function carregar(){
    var msg = window.document.getElementById("msg")
    var img = window.document.getElementById("imagem")
    var data = new Date()
    //var horaAtual = data.getHours()
    var horaAtual = 18
    msg.innerHTML = `A hora atual é: ${horaAtual} horas`

    if(horaAtual >= 0 && horaAtual < 12){
        //Bom dia!
        img.src = "imagens/morning.png"
    }else if (horaAtual >= 12 && horaAtual < 18){
        //Boa tarde
        img.src = "imagens/afternoon.png"
    }else{
        //Boa noite
        img.src = "imagens/night.png"
    }
}