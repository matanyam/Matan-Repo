const Form = document.getElementById('check-form');
const status = document.getElementById('status');

Form.addEventListener('submit', function(event) {
    console.log('Form is submitted!');
    event.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const comment = document.getElementById('comment').value;
    console.log(`Name : ${name}, Email: ${email}, comment ${comment}`);
    DataInsert(name,email,comment);
});

async function DataInsert(name,email,comment) {
    const response = await fetch(`/data_insert?name=${name}&email=${email}&comment=${comment}`);
    data = await response.json()
    if (data.message == "Invalid domain") {
    alert("You entered an invalid email domain")
    };

    if (data.message == "Feedback saved successfully") {
    alert("Thank you for your feedback")
    };




    console.log(data);

}