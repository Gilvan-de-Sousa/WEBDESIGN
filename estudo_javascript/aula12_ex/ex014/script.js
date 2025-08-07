// alert("Olá")

function carregar(){
    var msg = window.document.getElementById("msg")
    var img = window.document.getElementById("imagem")
    var data = new Date()
    var horaAtual = data.getHours()
    //var horaAtual = 19
    msg.innerHTML = `A hora atual é: ${horaAtual} horas`

    if(horaAtual >= 0 && horaAtual < 12){
        //Bom dia!
        document.body.style.backgroundColor="goldenrod"
        img.src = "imagens/morning_new.png"
        
    }else if (horaAtual >= 12 && horaAtual < 18){
        //Boa tarde
        document.body.style.backgroundColor="chocolate"
        img.src = "imagens/afternoon_new.png"
    }else{
        //Boa noite
        document.body.style.backgroundColor="rgb(32, 28, 28)"
        img.src = "imagens/night_new.png"
    }
}