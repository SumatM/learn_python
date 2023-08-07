

function getNumber<t>(arr:t[]):t[]{
    let newArra: t[] = []

    for (let i=0; i<arr.length; i++){
        newArra.push(arr[i])
    }

    return newArra;
}