// alert("Olá")


function Clicar(){
    var inicio = Number(document.getElementById("txtinicio").value)
    var fim = Number(window.document.getElementById("txtfim").value)
    var passo = Number(document.getElementById("txtpasso").value)
    var msg = document.getElementById("msg")
    // console.log("Clicou")
    msg.innerHTML = "Contou!"
    
    if(inicio == 0 || fim == 0 || passo == 0){
        msg.innerHTML = "Expressão inválida, tente novamente! \u{1F612}"
    } else {
        msg.innerHTML = `Iniciando a contagem \u{1F600}: <br>`
        if(passo <= 0){
            window.alert("Passo inválido!")
        }
        if(inicio < fim){
            for(let i = inicio; i <= fim; i += passo){
               msg.innerHTML += `👉 Loop: ${i}\n`
        }
        msg.innerHTML += `\u{1F3C1}`
    } else {
        //Contagem regressiva
        for(let i = inicio; i >= fim; i -= passo){
            msg.innerHTML += `👉 Loop: ${i}\n`
        }
    }
        
    }
    //msg.innerHTML += `\u{1F3C1}`

}