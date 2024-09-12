from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Render the survey page
@app.route('/survey')
def survey():
    return render_template('survey.html')

# Handle the survey form submission
@app.route('/submit_survey', methods=['POST'])
def submit_survey():
    name = request.form['name']
    energy_usage = request.form['energy_usage']
    interest_biogas = request.form['interest_biogas']
    feedback = request.form.get('feedback', '')

    # Here you could process the data or save it to a database
    print(f"Name: {name}, Energy Usage: {energy_usage}, Interest in Biogas: {interest_biogas}, Feedback: {feedback}")

    return redirect(url_for('survey'))

if __name__ == '__main__':
    app.run(debug=True)
