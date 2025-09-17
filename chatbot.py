import json
import datetime
from datetime import timedelta

# Load invoice data (pretend this was parsed from PDFs)
with open("invoices.json", "r") as f:
    invoices = json.load(f)

def answer_query(query: str):
    query = query.lower()
    today = datetime.date.today()

    if "due in the next 7 days" in query:
        upcoming = []
        for inv in invoices:
            due = datetime.date.fromisoformat(inv["due_date"])
            if today <= due <= today + timedelta(days=7):
                upcoming.append(inv)
        if not upcoming:
            return "No invoices are due in the next 7 days."
        resp = f"{len(upcoming)} invoice(s) due:\\n"
        for inv in upcoming:
            resp += f"- {inv['vendor']} (due {inv['due_date']}, ${inv['total']:.2f})\\n"
        return resp.strip()

    elif "total value of the invoice from" in query:
        for inv in invoices:
            if inv["vendor"].lower() in query:
                return f"The total value of the invoice from {inv['vendor']} is ${inv['total']:.2f}."
        return "No invoice found for that vendor."

    elif "list all vendors" in query and "invoices >" in query:
        # Extract threshold number
        try:
            threshold = float(query.split(">")[-1].replace("$", "").strip())
        except:
            return "Couldn't parse threshold amount."
        vendors = [inv for inv in invoices if inv["total"] > threshold]
        if not vendors:
            return f"No vendors with invoices greater than ${threshold:.2f}."
        resp = "Vendors with invoices greater than ${:.2f}:\\n".format(threshold)
        for inv in vendors:
            resp += f"- {inv['vendor']} (${inv['total']:.2f})\\n"
        return resp.strip()

    else:
        return "Sorry, I can’t answer that yet. Try asking about due dates, totals, or vendors."

if __name__ == "__main__":
    print("💬 Invoice Chatbot (type 'exit' to quit)")
    while True:
        q = input("\\nYou: ")
        if q.lower() in ["exit", "quit"]:
            break
        print("Bot:", answer_query(q))
