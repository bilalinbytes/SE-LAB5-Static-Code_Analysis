

# 🧠 Static Code Analysis – Lab 5

### **Student Details**

* **Name:** Mohammed Bilal
* **SRN:** PES2UG23CS344
* **Section:** F
* **Course:** Software Engineering Laboratory (SE Lab)
* **Lab Number:** 5
* **Lab Title:** Static Code Analysis
* **Tool Used:** GitHub Codespaces

---

## 📘 **Objective**

To improve the **quality, security, and maintainability** of Python code using static analysis tools like **Pylint**, **Flake8**, and **Bandit**.

---

## ⚙️ **Tools Used**

* **Pylint** – For identifying logical and quality issues.
* **Flake8** – For checking PEP 8 style and formatting errors.
* **Bandit** – For detecting security vulnerabilities.

---

## 🧩 **Steps Performed**

1. Set up the **GitHub Codespace** environment.
2. Opened and analyzed the provided file `inventory_system.py`.
3. Installed tools using:

   ```bash
   pip install pylint flake8 bandit
   ```
4. Generated static analysis reports:

   ```bash
   pylint inventory_system.py > pylint_report.txt
   bandit -r inventory_system.py > bandit_report.txt
   flake8 inventory_system.py > flake8_report.txt
   ```
5. Identified and documented issues.
6. Fixed a minimum of **four issues** (e.g., invalid exception handling, mutable default arguments, poor logging).
7. Re-ran all tools to confirm improvements.
8. Created **reflection.md** to summarize observations.

---

## 📈 **Final Outcome**

* Improved **Pylint score** from ~6.4 to **10.0/10**.
* Eliminated style and security warnings.
* Enhanced **readability**, **robustness**, and **maintainability**.

---

## 📂 **Deliverables**

* ✅ `updated_inventory_system.py` – Cleaned and improved code
* ✅ `pylint_report.txt`
* ✅ `flake8_report.txt`
* ✅ `bandit_report.txt`
* ✅ `reflection.md`
* ✅ `README.md`

---

