import tkinter as tk
from tkinter import filedialog, messagebox
import markdown
import os

TEMPLATE_FILE = "mbgen2.txt"

class MicroblogGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Microblog Generator")
        self.geometry("600x400")
        
        self.create_widgets()
        self.load_template()
        
    def create_widgets(self):
        # Template label and text box
        self.template_label = tk.Label(self, text="Template")
        self.template_label.pack()
        
        self.template_text = tk.Text(self, height=10)
        self.template_text.pack()
        
        # Post content label and text box
        self.post_label = tk.Label(self, text="Post content")
        self.post_label.pack()
        
        self.post_text = tk.Text(self, height=10)
        self.post_text.pack()
        
        # Post button
        self.post_button = tk.Button(self, text="Post", command=self.generate_post)
        self.post_button.pack()
        
    def load_template(self):
        if os.path.exists(TEMPLATE_FILE):
            with open(TEMPLATE_FILE, 'r', encoding='utf-8') as file:
                template = file.read()
                self.template_text.insert("1.0", template)
        else:
            default_template = "<!--content here-->"
            self.template_text.insert("1.0", default_template)
        
    def save_template(self):
        template = self.template_text.get("1.0", tk.END)
        with open(TEMPLATE_FILE, 'w', encoding='utf-8') as file:
            file.write(template)
    
    def generate_post(self):
        template = self.template_text.get("1.0", tk.END)
        post_content = self.post_text.get("1.0", tk.END)
        
        if "<!--content here-->" not in template:
            messagebox.showerror("Error", "Template must contain '<!--content here-->' comment.")
            return
        
        # Convert markdown to HTML
        post_html = markdown.markdown(post_content)
        
        # Insert post content into template
        new_post = template.replace("<!--content here-->", post_html)
        new_post_div = f'<div class="mbgenPost">\n{new_post}\n</div>'
        
        # Prompt user to select HTML file
        file_path = filedialog.askopenfilename(filetypes=[("HTML files", "*.html")])
        
        if not file_path:
            return
        
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Insert the new post
        if "<!--posts here-->" not in html_content:
            messagebox.showerror("Error", "Selected file must contain '<!--posts here-->' comment.")
            return
        
        # Find existing mbgenPost and place new post above it
        if '<div class="mbgenPost">' in html_content:
            posts_index = html_content.index('<div class="mbgenPost">')
            html_content = html_content[:posts_index] + new_post_div + "\n" + html_content[posts_index:]
        else:
            html_content = html_content.replace("<!--posts here-->", f"<!--posts here-->\n{new_post_div}")
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(html_content)
        
        messagebox.showinfo("Success", "Post added successfully!")
        
        # Save the current template
        self.save_template()

if __name__ == "__main__":
    app = MicroblogGenerator()
    app.mainloop()
