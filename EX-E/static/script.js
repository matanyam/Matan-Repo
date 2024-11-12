const Form = document.getElementById('check-form');
const status = document.getElementById('status');



Form.addEventListener('submit', function(event) {
    console.log('Starting calculation!');
    event.preventDefault();
    const number1 = document.getElementById('num1').value;
    const number2 = document.getElementById('num2').value;
    const operator = document.getElementById('operation').value;
    Calculate(number1,number2,operator)
});

async function Calculate(number1,number2,operation) {
    const response = await fetch(`/calculate?number1=${number1}&operator=${operation}&number2=${number2}`);
    const data = await response.json();
    console.log(data);
    if (data.error == "Cannot divide with zero") {
    alert("Cannot divide by zero, please try again")
    };
    if (data.error == "Invalid operation") {
    alert("Please enter a valid operation")
    };
    status.textContent = `Answer: ${data.result}`;

}