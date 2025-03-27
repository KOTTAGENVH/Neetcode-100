//Answer 1
let nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10];

const nonDup = (numPass) => {
    let nonDuplicate = new Set(numPass);

    if (nonDuplicate.size === numPass.length) {
        return true;
    } else {
        return false;
    }
}

console.log(nonDup(nums));

//Answer 2

const nonDup2 = (numPass) => {
    for (let i=0; i<numPass.length; i++) {
        for (let j=i+1; j<numPass.length; j++) {
            if (numPass[i] === numPass[j]) {
                return false;
            }
        }
    }
    return true;
}

console.log(nonDup2(nums));