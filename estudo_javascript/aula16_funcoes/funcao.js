// function parimp(num){
//   if(num % 2 == 0){
//     console.log(`${num} é par`)
//   }else{
//     console.log(`${num} é impar`)
//   }
// }

function parimp(num){
  if(num % 2 == 0){
    return "par" 
  }else{
    return  `impar`
  }
}

let result = parimp(3)

console.log(`O número informado é ${result}`)