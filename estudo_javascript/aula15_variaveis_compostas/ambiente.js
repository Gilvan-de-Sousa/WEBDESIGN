let num = [5, 8, 2, 9, 3];

//Inserindo um novo valor no vetor:
num[5] = 6 //insere o valor na posição 5 do vetor
num.push(7) //insere o valor no final do vetor

//console.log(`Nosso vetor é ${num}.`)

//descobrindo o tamanhdo do vetor
//console.log(`Tamanho do ARRAY: ${num.length} posições`)

//ordenando o vetor
//console.log(`Vetor ordenado: ${num.sort()}`)

//extraindo os valores com um loop
// for(i in num){
//   console.log(num[i])
// }
//ou

for(let pos = 0; pos < num.length; pos++){
  console.log(num[pos])
}
console.log("Fim do loop")