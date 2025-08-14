let valores = [8, 1, 7, 4, 2, 9]

console.log(`Valores do vetor: ${valores}`)

console.log('Utilizando um loop.')

for(let i = 0; i < valores.length; i++){
    console.log(`A posição ${i} tem o valor: ${valores[i]}`)
}

//Simplificando o FOR
console.log(" ")
for(let e in valores){
    console.log(`Posição ${e}: valor ${valores[e]}`)
}


//retornar a posição do valor informado no indexOf
console.log("")
console.log(`O valor 2 está na posição ${valores.indexOf(2)} do vetor.`)