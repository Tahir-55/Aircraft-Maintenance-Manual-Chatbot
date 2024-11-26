import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from ttkthemes import ThemedTk
from pdf_utils import extract_text_from_pdf, split_text
from chatbot import Chatbot

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Chatbot")
        self.root.geometry("800x600")
        self.text_chunks = None
        self.chatbot = None

        # Style and Theme
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 12), padding=5)
        self.style.configure("TLabel", font=("Helvetica", 12))
        self.style.configure("TEntry", font=("Helvetica", 12))

        # File upload section
        self.upload_button = ttk.Button(root, text="Upload PDF", command=self.upload_pdf, width=20)
        self.upload_button.pack(pady=20)

        # Display extracted PDF text (After uploading)
        self.extracted_text_label = ttk.Label(root, text="Extracted Text", font=("Helvetica", 14, "bold"))
        self.extracted_text_label.pack(pady=10)

        self.extracted_text_box = tk.Text(root, height=10, width=80, wrap=tk.WORD, font=("Helvetica", 12))
        self.extracted_text_box.pack(pady=10)
        self.extracted_text_box.config(state=tk.DISABLED)  # Initially disabled

        # Add scrollbar to the extracted text box
        self.scrollbar = ttk.Scrollbar(root, command=self.extracted_text_box.yview)
        self.extracted_text_box.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Chat interface
        self.chat_frame = ttk.Frame(root)
        self.chat_frame.pack(pady=20)

        self.chat_label = ttk.Label(self.chat_frame, text="Enter your question:")
        self.chat_label.pack(side=tk.LEFT, padx=5)

        self.chat_entry = ttk.Entry(self.chat_frame, width=50)
        self.chat_entry.pack(side=tk.LEFT, padx=5)

        self.chat_button = ttk.Button(self.chat_frame, text="Ask", command=self.ask_question)
        self.chat_button.pack(side=tk.LEFT, padx=5)

        # Display chatbot's answer
        self.answer_label = ttk.Label(root, text="Chatbot's Answer:", font=("Helvetica", 14, "bold"))
        self.answer_label.pack(pady=10)

        self.answer_text_box = tk.Text(root, height=6, width=80, wrap=tk.WORD, font=("Helvetica", 12))
        self.answer_text_box.pack(pady=10)
        self.answer_text_box.config(state=tk.DISABLED)  # Initially disabled

        # Add scrollbar to the answer text box
        self.answer_scrollbar = ttk.Scrollbar(root, command=self.answer_text_box.yview)
        self.answer_text_box.config(yscrollcommand=self.answer_scrollbar.set)
        self.answer_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Exit button
        self.exit_button = ttk.Button(root, text="Exit", command=root.quit, width=20)
        self.exit_button.pack(pady=20)

    def upload_pdf(self):
        file_path = filedialog.askopenfilename(
            title="Select a PDF file",
            filetypes=[("PDF files", "*.pdf")]
        )
        if not file_path:
            messagebox.showerror("Error", "No file selected.")
            return

        # Extract and process the PDF
        pdf_text = extract_text_from_pdf(file_path)
        self.text_chunks = split_text(pdf_text)

        # Initialize the chatbot
        self.chatbot = Chatbot(self.text_chunks)

        # Display extracted text in the Text widget
        self.extracted_text_box.config(state=tk.NORMAL)
        self.extracted_text_box.delete(1.0, tk.END)  # Clear previous text
        self.extracted_text_box.insert(tk.END, pdf_text)  # Insert extracted text
        self.extracted_text_box.config(state=tk.DISABLED)

        messagebox.showinfo("Success", "PDF uploaded and processed successfully!")

    def ask_question(self):
        if not self.chatbot:
            messagebox.showerror("Error", "Please upload a PDF first.")
            return

        question = self.chat_entry.get()
        if not question.strip():
            messagebox.showwarning("Warning", "Please enter a question.")
            return

        # Get the chatbot's response
        answer = self.chatbot.generate_response(question)

        # Display the answer in the Text widget
        self.answer_text_box.config(state=tk.NORMAL)
        self.answer_text_box.delete(1.0, tk.END)  # Clear previous answer
        self.answer_text_box.insert(tk.END, answer)  # Insert new answer
        self.answer_text_box.config(state=tk.DISABLED)


if __name__ == "__main__":
    # Use a themed root window
    root = ThemedTk(theme="arc")
    app = ChatbotApp(root)
    root.mainloop()
