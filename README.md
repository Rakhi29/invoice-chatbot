# Invoice Chatbot 🧾🤖

A lightweight chatbot that can read invoices (simulated from sample JSON) and answer simple questions like:

- "How many invoices are due in the next 7 days?"
- "What is the total value of the invoice from Amazon?"
- "List all vendors with invoices > $2000"

---

## 🚀 Setup & Run

1. Make sure you have Python 3.8+ installed
2. Unzip this folder (if using the zip) or ensure files are in the same folder
3. Run:

```bash
python chatbot.py
```

---

## 💡 Example Run

```
💬 Invoice Chatbot (type 'exit' to quit)

You: How many invoices are due in the next 7 days?
Bot: 1 invoice(s) due:
- Amazon (due 2025-09-05, $2450.00)

You: What is the total value of the invoice from Microsoft?
Bot: The total value of the invoice from Microsoft is $3100.00.

You: List all vendors with invoices > 2000
Bot: Vendors with invoices greater than $2000.00:
- Amazon ($2450.00)
- Microsoft ($3100.00)
```
