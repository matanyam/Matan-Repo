const Form = document.getElementById('check-form');
const status = document.getElementById('status');

Form.addEventListener('submit', function(event) {
    console.log('Form is submitted!');
    event.preventDefault();
    const tmp = document.getElementById('Temperature').value;
    console.log(`c: ${tmp}`);
    ConvertTemp(tmp);
});

async function ConvertTemp(tmp) {
    const response = await fetch(`/convert_to_fahrenheit?Temperature=${tmp}`);
    const data = await response.json();
    status.TextContent = 'Weather ${data.Fahrenheit}'

    console.log(data);
    console.log(data.status_code);
    status.textContent = `Converted Temperature: ${data.Fahrenheit} °F`;

}