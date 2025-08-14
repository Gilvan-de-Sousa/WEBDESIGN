function fatorial(num){
    fat = 1
    for(let i = num; i > 1; i --){
        fat *= i
    }
    return fat
}

console.log(fatorial(6))