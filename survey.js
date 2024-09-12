// /static/survey.js
document.getElementById('surveyForm').addEventListener('submit', function(event) {
    // Add any additional client-side validation if necessary
    const name = document.getElementById('name').value;
    const energyUsage = document.getElementById('energyUsage').value;

    if (!name || !energyUsage) {
        alert('Please fill in all required fields.');
        event.preventDefault();
    }
});
