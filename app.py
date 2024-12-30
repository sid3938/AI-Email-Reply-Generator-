import openai
import sqlite3
import datetime

# Initialize OpenAI API Key
# Set your OpenAI API key
# As this API key is exposed on GitHub so Replace it with your actual key before running the script.
openai.api_key = "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"

# Database setup
def initialize_database():
    """Initialize the SQLite database."""
    conn = sqlite3.connect("email_replies.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS email_replies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_email TEXT,
            reply TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Generate AI reply
def generate_ai_reply(email_content):
    """Generate a professional reply to the provided email content using OpenAI API."""
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": f"Write a professional reply to the following email: {email_content}"}
            ]
        )
        return completion['choices'][0]['message']['content']
    except Exception as e:
        return f"Error generating reply: {e}"

# Save email and reply to the database
def save_to_database(original_email, reply):
    """Save the original email, AI-generated reply, and timestamp to the database."""
    conn = sqlite3.connect("email_replies.db")
    cursor = conn.cursor()
    timestamp = datetime.datetime.now().isoformat()
    cursor.execute(
        "INSERT INTO email_replies (original_email, reply, timestamp) VALUES (?, ?, ?)",
        (original_email, reply, timestamp)
    )
    conn.commit()
    conn.close()

# Display saved replies
def display_replies():
    """Fetch and display all saved replies from the database."""
    conn = sqlite3.connect("email_replies.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, original_email, reply, timestamp FROM email_replies")
    rows = cursor.fetchall()
    conn.close()
    for row in rows:
        print(f"ID: {row[0]}\nOriginal Email: {row[1]}\nReply: {row[2]}\nTimestamp: {row[3]}\n")

# Main workflow
def main():
    initialize_database()
    print("AI Email Reply Generator\n")
    while True:
        print("Options:\n1. Generate Reply\n2. View Saved Replies\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            email_content = input("Enter the email content: ")
            ai_reply = generate_ai_reply(email_content)
            print(f"\nAI-Generated Reply:\n{ai_reply}\n")
            save_to_database(email_content, ai_reply)
        elif choice == "2":
            display_replies()
        elif choice == "3":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
