// alert("Olá")
function verificar(){
    var data = new Date();
    var anoAtual = data.getFullYear()
    var fAno = window.document.getElementById("txtano")
    var res = document.querySelector("div#res")

    if(fAno.value.length == 0 || fAno.value > anoAtual){
        window.alert("Verifique os dados e tente novamente!")
    }else {
        var fsex = document.getElementsByName("radsex")
        var idade = anoAtual - Number(fAno.value)
        //res.innerHTML = `Idade calculada ${idade}`
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute(`id`, `photo`)

        if(fsex[0].checked){
            genero = 'Homem'
            if(idade >= 0 && idade < 10){
                //Criança
                img.setAttribute('src', 'baby_boy.png')
                document.body.style.backgroundColor="lightblue"
            }else if(idade < 21){
                //adolescente
                img.setAttribute('src', 'boy.png')
                window.document.body.style.backgroundColor="green"
            }else if(idade < 50){
                //adulto
                img.setAttribute('src', 'adult_men.png')
                window.document.body.style.backgroundColor="chocolate"
            }else{
                //Idoso
                img.setAttribute('src', 'old_men.png')
                document.body.style.backgroundColor="darkgray"
            }
        }else if(fsex[1].checked){
            genero = 'Mulher'
            if(idade >= 0 && idade < 10){
                //Criança
                img.setAttribute('src', 'baby_girl.png')
                document.body.style.backgroundColor="pink"
            }else if(idade < 21){
                //adolescente
                img.setAttribute('src', 'girl.png')
                document.body.style.backgroundColor="darkmagenta"
            }else if(idade < 50){
                //adulto
                img.setAttribute('src', 'adult_women.png')
                document.body.style.backgroundColor="violet"
            }else{
                //Idoso
                img.setAttribute('src', 'old_women.png')
                document.body.style.backgroundColor="lightgray"
            }
        }
        res.innerHTML = `Detectamos ${genero} com ${idade} anos`
        res.appendChild(img)
    }
}
