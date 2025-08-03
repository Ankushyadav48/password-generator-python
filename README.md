# 🔐 Raw Password Generator

A simple yet powerful password generator built with Python using Tkinter for the graphical user interface (GUI). This tool allows users to create strong, customizable passwords with options for letters, numbers, and special characters.

---

## 🖥️ Features

- Generate random passwords of desired length.
- Select specific character sets:
  - ✅ Letters (Uppercase and Lowercase)
  - ✅ Numbers (0–9)
  - ✅ Special Characters (!@#$%^&*, etc.)
- Copy the generated password directly to the clipboard.
- User-friendly GUI with a clean and colorful layout.
- Error handling and helpful messages for invalid inputs.

---

## 📸 GUI Preview

- Input field to specify password length.
- Checkboxes to choose character types.
- Buttons to generate and copy the password.
- Visual feedback for errors or successful actions.

---

## 🚀 How to Run

1. Make sure Python is installed on your system. (Recommended: Python 3.7+)
2. Save the script as `password_generator.py`.
3. Run the program:
   ```bash
   python password_generator.py

## 🧾 Dependencies

* **Tkinter**: Standard Python GUI library (included with most Python installations)
* **random**: Built-in Python module for random selections

No additional packages are required.

---

## 💡 How It Works

1. The user enters a desired password length.
2. The user selects one or more character types (letters, numbers, specials).
3. When "Generate" is clicked:

   * The password is created by randomly picking characters from the selected types.
   * The generated password is displayed in the text box.
4. Clicking "Copy" copies the password to your clipboard.

---

## ⚠️ Input Validations

* Displays an error if:

  * Password length is not a positive integer.
  * No character set is selected.
  * Trying to copy when no password is generated.

---

## 🎨 GUI Details

* Background: Orange and Yellow theme
* Fonts: Arial, Helvetica, and Courier
* Components: Labels, Entry, Buttons, Checkboxes, Frames

---

## 📁 File Structure
password_generator.py
README.md

---

## 🛠️ Future Improvements (Optional)

* Add an option to save passwords to a local file.
* Include a strength indicator for the generated password.
* Dark mode toggle for better visual comfort.
* Responsive resizing support.

---
## 🙌 Author

Made with love by **Ankush Ajay Yadav**  
Roll No.: 08
Department: Computer Engineering  
College: Dilkap college of engineering

## 📃 License

This project is open-source and free to use for personal or educational purposes.

---

```

Let me know if you want to include screenshots, a `.gif` demo, or add GitHub-style badges (like Python version or License).
```
