
function addNumber() {
    var num1 = parseInt(prompt("첫 번째 숫자는? "));
    var num2 = parseInt(prompt("두 번째 숫자는? "));
    var result = sum(num1, num2); 
    alert("두 수를 더한 값은 " + result + "입니다");
}


function subNumber() {
    var num1 = parseInt(prompt("첫 번째 숫자는? "));
    var num2 = parseInt(prompt("두 번째 숫자는? "));
    var result = subtract(num1, num2);
    alert("두 수를 뺀 값은 " + result + "입니다");
}


function mulNumber() {
    var num1 = parseInt(prompt("첫 번째 숫자는? "));
    var num2 = parseInt(prompt("두 번째 숫자는? "));
    var result = multiply(num1, num2);
    alert("두 수를 곱한 값은 " + result + "입니다");
}


function divNumber() {
    var num1 = parseInt(prompt("첫 번째 숫자는? "));
    var num2 = parseInt(prompt("두 번째 숫자는? "));
    

    var result = divide(num1, num2);
    alert("두 수를 나눈 값은 " + result + "입니다");
}


function sum(a, b) {
    return a + b;
}

function subtract(a, b) {
    return a - b;
}

function multiply(a, b) {
    return a * b;
}

function divide(a, b) {
    return a / b;
}
