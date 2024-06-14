import tkinter as tk
from tkinter import filedialog, messagebox
import markdown
import os
import subprocess

TEMPLATE_FILE = "mbgen2.txt"

class MicroblogGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Microblog Generator")
        self.geometry("600x500")
        
        self.create_widgets()
        self.load_template()
        
    def create_widgets(self):
        # Template label and text box
        self.template_label = tk.Label(self, text="Template")
        self.template_label.pack()
        
        self.template_text = tk.Text(self, height=8)
        self.template_text.pack()
        
        # Post content label and text box
        self.post_label = tk.Label(self, text="Post content")
        self.post_label.pack()
        
        self.post_text = tk.Text(self, height=8)
        self.post_text.pack()
        
        # Tag label and text box
        self.tag_label = tk.Label(self, text="Tag")
        self.tag_label.pack()
        
        self.tag_text = tk.Entry(self)
        self.tag_text.pack()
        
        # Post button
        self.post_button = tk.Button(self, text="Post", command=self.generate_post)
        self.post_button.pack()

        # Upload button
        self.upload_button = tk.Button(self, text="Upload to Neocities", command=self.upload_to_neocities)
        self.upload_button.pack()
        
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
        tag = self.tag_text.get()
        
        if "<!--content here-->" not in template:
            messagebox.showerror("Error", "Template must contain '<!--content here-->' comment.")
            return
        
        # Convert markdown to HTML
        post_html = markdown.markdown(post_content)
        
        # Insert post content into template
        new_post = template.replace("<!--content here-->", post_html)
        
        # Default tag if empty
        if not tag:
            tag = "Untagged"
        
        new_post_div = f'<div class="mbgenPost mbgen{tag}">\n{new_post}\n</div>'
        
        # Prompt user to select HTML file
        self.file_path = filedialog.askopenfilename(filetypes=[("HTML files", "*.html")])
        
        if not self.file_path:
            return
        
        with open(self.file_path, 'r', encoding='utf-8') as file:
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
        
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(html_content)
        
        messagebox.showinfo("Success", "Post added successfully!")
        
        # Save the current template
        self.save_template()

    def upload_to_neocities(self):
        if not hasattr(self, 'file_path') or not self.file_path:
            messagebox.showerror("Error", "No file has been posted yet.")
            return

        try:
            subprocess.Popen('neocities upload ' + self.file_path, shell=True)
            messagebox.showinfo("Success", f"File '{self.file_path}' uploaded successfully to Neocities!")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to upload file to Neocities: {e}")

if __name__ == "__main__":
    app = MicroblogGenerator()
    app.mainloop()
