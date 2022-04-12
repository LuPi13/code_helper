let output = "";
for (let i = 1; i <= 5; i++) {
    for (let j = 1; j < (6 - i); j++) {
        output += " ";
    }
    for (let k = 1; k <= i; k++) {
        output += k;
    }
    output += "\n"
}

console.log(output);