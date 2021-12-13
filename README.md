# Loan Qualifier Application

This is a python command-line interface application that allows users to see qualifying loans from lenders quickly and easily. The application works by taking in a `daily_rate_sheet` of loan criteria from various loan providers, asking the user a number of questions to evaluate their loan eligibility, then returning to them a list of qualifying loans and prompt the user to save the qualifying loans to a new CSV file

---

## Technologies

This project leverages python 3.7 with the following packages:

* [fire](https://github.com/google/python-fire) - For the command line interface, help page, and entrypoint.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs


---

## Installation Guide

Before running the application first install the following dependencies.

```python
  pip install fire
  pip install questionary
```

---

## Usage

To use the loan qualifier application simply clone the repository and run the **app.py** with:

```python
python app.py
```

Upon launching the loan qualifier application you will be greeted with the following prompts and ask you to save the qualifying loans base on your end.

![case_1](https://user-images.githubusercontent.com/94591580/145755724-c0bf4644-0406-465b-b377-fa26d9ba8be4.png)

If you are not qualified for any loan, the application will notify the user and exit.
![case_2](https://user-images.githubusercontent.com/94591580/145755651-2c6b20a3-1999-43ec-9f0e-e0a76a11ba12.png)


---

## Contributors

daosynguyen21@gmail.com


---

## License

MIT
