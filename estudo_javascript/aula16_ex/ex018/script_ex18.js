var lista = document.querySelector('select#flista');
var num = document.querySelector("input#fnum");
let res = document.querySelector("div#res");
let valores = [];

function isNumero(n) {
  if (Number(n) >= 1 && Number(n) <= 100) {
    return true;
  } else {
    return false;
  }
}

function inLista(n, l) {
  if (l.indexOf(Number(n)) != -1) {
    return true;
  } else {
    return false;
  }
}

function adicionar() {
  if (isNumero(num.value) && !inLista(num.value, valores)) {
    valores.push(Number(num.value))

    let item = document.createElement('option')
    item.text = `Valor ${num.value} ..... adicionado`
    lista.appendChild(item)
    res.innerHTML = " "
  } else {
    window.alert("Valor inválido ou já existente na lista!");
  }

  num.value = " "
  num.focus()
}

function finalizar(){
    if(valores.length == 0){
        window.alert("Adicione valores antes de finalizar!")
    }else{

        let tot = valores.length
        let maior = valores[0]
        let menor = valores[0]
        let soma = 0
        let media = 0
        for(let i in valores){
            soma += valores[i]
            media += valores[i] / valores.length
            if(valores[i] > maior)
                maior = valores[i]

            if(valores[i] < menor)
                menor = valores[i]
        }
        res.innerHTML = " "
        res.innerHTML += `Ao todo temos ${tot} números cadastrados!`
        res.innerHTML += `\n<br>O maior valor informado foi ${maior}.`
        res.innerHTML += `\n<br>O menor valor informado foi ${menor}.`
        res.innerHTML += `\n<br>A soma de todos os valores é: ${soma}`
        res.innerHTML += `\n<br>O valor da média dos valores é ${media}`
    }
}
