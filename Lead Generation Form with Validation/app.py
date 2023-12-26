from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

@app.route("/")
def lead_form():
    return render_template("lead_form.html")

@app.route("/submit_lead", methods=["POST"])
def submit_lead():
    name = request.form.get("name")
    email = request.form.get("email")
    phone_number = request.form.get("phone_number")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")

    errors = []

    # Name validation
    if not name or not name.isalpha():
        errors.append("Name must contain only alphabets.")

    # Email validation
    if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        errors.append("Invalid email format.")

    # Phone number validation
    if not phone_number or not phone_number.isdigit() or len(phone_number) != 10:
        errors.append("Phone number must be 10 digits.")

    # Password validation
    if not password or not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,12}$", password):
        errors.append("Password must be 8-12 characters long, contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")

    # Confirm password validation
    if password != confirm_password:
        errors.append("Passwords do not match.")

    if errors:
        return render_template("lead_form.html", errors=errors)

    # Successful submission
    print("Lead Information:")
    print("Name:", name)
    print("Email:", email)
    print("Phone Number:", phone_number)
    print("Password:", password)
    return redirect(url_for("lead_form", success="Lead submitted successfully!"))

if __name__ == "__main__":
    app.run(debug=True)
