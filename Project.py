from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os

def show_frame(f):
    f.tkraise()

def validate_and_start():
    name = name_entry.get()
    if not name.strip():
        messagebox.showwarning("Input Required", "Please enter your name before continuing.")
    else:
        show_frame(welcome_page)

def open_pdf(path):
    if os.path.exists(path):
        os.startfile(path)
    else:
        print("File not found:", path)

# Setup window
window = Tk()
window.geometry("800x650")
window.title("Wise Owl's Library")
window.config(bg="#F5ECD9")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.iconbitmap("owl.ico")

# Color and font settings
colors = {
    "login": "#F5ECD9",
    "welcome": "#FFF8E1",
    "menu": "#EEE8DC",
    "History": "#FCEBD4",
    "Love": "#FDE2E2",
    "Politics": "#E6F2FF",
    "Cartoon": "#FFF3E0",  
    "Classical": "#E5E4E2",
    "Fantasy": "#E0BBE4",
    "Self-Improvement": "#E8F5E9"
}


title_font = ('Arial', 26, 'bold')
subtitle_font = ('Arial', 18, 'italic')
text_font = ('Arial', 16)

# Define pages
login_page = Frame(window, bg=colors["login"])
welcome_page = Frame(window, bg=colors["welcome"])
menu_page = Frame(window, bg=colors["menu"])

pages = {
    "login": login_page,
    "welcome": welcome_page,
    "menu": menu_page
}

categories = [
    "History", "Love", "Politics",
    "Cartoon",  "Classical", "Fantasy", "Self-Improvement"
]


for cat in categories:
    pages[cat] = Frame(window, bg=colors[cat])

# Add all pages to the window grid
for frame in pages.values():
    frame.grid(row=0, column=0, sticky='nsew')

# ---------------------- Login Page ----------------------
# Owl Image on Login Page
owl_img_login = Image.open("R.jpg").resize((150, 150))
owl_photo_login = ImageTk.PhotoImage(owl_img_login)

Label(
    login_page,
    image=owl_photo_login,
    bg=colors["login"]
).pack(pady=(40, 10))

Label(
    login_page,
    text="Welcome to Wise Owl's Library",
    font=title_font,
    bg=colors["login"],
    fg="#5D4037"
).pack(pady=(0, 15))

Label(
    login_page,
    text="Enter Your Name",
    font=subtitle_font,
    bg=colors["login"],
    fg="#7B5E57"
).pack(pady=(0, 5))

name_entry = Entry(
    login_page,
    font=text_font,
    justify='center',
    bd=3,
    relief=GROOVE,
    width=30
)
name_entry.pack(pady=(0, 20))

Button(
    login_page,
    text="Start",
    font=text_font,
    bg="#8F6C4E",
    fg="white",
    activebackground="#A67B5B",
    activeforeground="white",
    width=15,
    relief=RIDGE,
    command=validate_and_start
).pack(pady=(0, 50))

# Add a subtle footer text
Label(
    login_page,
    text="📚 Discover your next favorite book!",
    font=('Arial', 12, 'italic'),
    bg=colors["login"],
    fg="#A1887F"
).pack(side=BOTTOM, pady=15)

# ---------------------- Welcome Page ----------------------
Label(
    welcome_page,
    text="Welcome to the 🦉 Wise Owl Library!",
    font=title_font,
    bg=colors["welcome"],
    fg="#4A4A4A",
    pady=30
).pack()

Label(
    welcome_page,
    text="Explore a world of knowledge, stories, and discoveries.",
    font=('Arial', 16),
    bg=colors["welcome"],
    fg="#5D4037"
).pack(pady=10)

Button(
    welcome_page,
    text="📚 Go to Menu",
    font=text_font,
    bg="#6B4226",
    fg="white",
    width=20,
    command=lambda: show_frame(menu_page)
).pack(pady=40)

# Load owl image for welcome page
owl_img = Image.open("owl.jpg").resize((200, 200))
owl_photo = ImageTk.PhotoImage(owl_img)

owl_label = Label(
    welcome_page,
    image=owl_photo,
    bg=colors["welcome"]
)
owl_label.image = owl_photo
owl_label.pack(pady=10)

# ---------------------- Menu Page ----------------------
Label(
    menu_page,
    text="Choose a Category",
    font=title_font,
    bg=colors["menu"],
    pady=20
).pack()

icons = {
    "History": "🏛️",
    "Love": "💖",
    "Politics": "🗳️",
    "Cartoon": "🎨📺", 
    "Classical": "🦉📚",
    "Fantasy": "🦄 ",
    "Self-Improvement": "🌱"
}
for cat in categories:
    Button(
        menu_page,
        text=f"{icons[cat]} {cat}",
        font=text_font,
        width=30,
        bg="#A67B5B",
        fg="white",
        command=lambda c=cat: show_frame(pages[c])
    ).pack(pady=6)

# ---------------------- Category Pages ----------------------
titles = {
    "History": "🏛️ History Collection",
    "Love": "💖 Love Collection",
    "Politics": "🗳️ Politics Collection",
    "Cartoon": "🎨 Cartoon Collection",  
    "Classical": "🦉📚 Classical Collection",
    "Fantasy": "🦄 Fantasy Collection ",
    "Self-Improvement": "🌱 Self-Improvement Collection"
}
for cat in categories:
    Label(
        pages[cat],
        text=titles[cat],
        font=title_font,
        bg=colors[cat],
        fg="#3E2723"
    ).pack(pady=25)

    Frame(
        pages[cat],
        height=2,
        bd=1,
        relief=SUNKEN,
        bg="gray"
    ).pack(fill=X, padx=40, pady=10)

    Button(
        pages[cat],
        text="⬅ Back to Menu",
        font=text_font,
        bg="#6B4226",
        fg="white",
        width=20,
        command=lambda: show_frame(menu_page)
    ).pack(pady=20)

# ---------------------- Classical Books Only ----------------------
classical_books = [
    {
        "title": "🦉 Featured Book: War and Peace",
        "path": r"C:\Users\USER\Desktop\project\Books\Classical\war_and_peace.pdf"
    },
    {
        "title": "🦉 Featured Book: War and Peace 2",
        "path": r"C:\Users\USER\Desktop\project\Books\Classical\war_and_peace2.pdf"
    },

    {   "title": "🦉 Featured Book: Fall of Paris",
        "path": r"C:\Users\USER\Desktop\project\Books\Classical\Fall_of_Paris.pdf"
    }
]

# Display books only in Classical page
for book in classical_books:
    Label(
        pages["Classical"],
        text=book["title"],
        font=subtitle_font,
        bg=colors["Classical"],
        fg="#4A4A4A"
    ).pack(pady=5)

    Button(
        pages["Classical"],
        text="📖 Open Book",
        font=text_font,
        bg="#4B7F52",
        fg="white",
        width=25,
        command=lambda path=book["path"]: open_pdf(path)
    ).pack(pady=10)
# ---------------------- Politics Books Only ----------------------
politics_books =[
    {
        "title": "🦉 Featured Book: Burma",
        "path": r"C:\Users\USER\Desktop\project\Books\Politics\Burma.pdf"
    },
    {
        "title": "🦉 Featured Book: ဦးနေဝင်း၏မအောင်မြင်သောခေတ်ပြောင်းတော်လှန်ရေး",
        "path": r"C:\Users\USER\Desktop\project\Books\Politics\ဦးနေဝင်း၏မအောင်မြင်သောခေတ်ပြောင်းတော်လှန်ရေး.pdf"
    },

    {   "title": "🦉 Featured Book: သခင်ဘသောင်း_ခြေလေးချောင်း_တော်လှန်ရေး",
        "path": r"C:\Users\USER\Desktop\project\Books\Politics\သခင်ဘသောင်း_ခြေလေးချောင်း_တော်လှန်ရေး.pdf"
    },
    {   "title": "🦉 Featured Book:မြန်မာနိုင်ငံထောက်လှမ်းရေးများအကြောင်း",
        "path": r"C:\Users\USER\Desktop\project\Books\Politics\သောင်းဝေဦး_မြန်မာနိုင်ငံထောက်လှမ်းရေးများအကြောင်း.pdf"
    },
    {   "title": "🦉 Featured Book:လီကွမ်ယူ၏ လီကွမ်ယူ",
        "path": r"C:\Users\USER\Desktop\project\Books\Politics\လီကွမ်ယူ၏ လီကွမ်ယူ.pdf"
    },
]

# Display books only in Politics page
for book in politics_books:
    Label(
        pages["Politics"],
        text=book["title"],
        font=subtitle_font,
        bg=colors["Politics"],
        fg="#4A4A4A"
    ).pack(pady=5)

    Button(
        pages["Politics"],
        text="📖 Open Book",
        font=text_font,
        bg="#4B7F52",
        fg="white",
        width=25,
        command=lambda path=book["path"]: open_pdf(path)
    ).pack(pady=10)
    # ---------------------- Self-Improvement Books Only ----------------------
self_improvement_books = [
    {
        "title": "🦉 Featured Book: ဒေါသနှင့်မိတ်ဆွေဖွဲ့ခြင်း",
        "path": r"C:\Users\USER\Desktop\project\Books\Self_Improvement\ဒေါသနှင့်မိတ်ဆွေဖွဲ့ခြင်းမျိုးလွင်MBA_ဘာသာပြန်.pdf"
    },
    {
        "title": "🦉 Featured Book: အာဏာစက်",
        "path": r"C:\Users\USER\Desktop\project\Books\Self_Improvement\အာဏာစက်.pdf"
    },

    {   "title": "🦉 Featured Book: only-one",
        "path": r"C:\Users\USER\Desktop\project\Books\Self_Improvement\𝐎𝐧𝐥𝐲_𝐎𝐧𝐞တစ်ကောင်တည်းပဲ.pdf"
    },
    {   "title": "🦉 Featured Book: ဂရုမစိုက်ခြင်းအနုပညာ",
        "path": r"C:\Users\USER\Desktop\project\Books\Self_Improvement\ဂရုမစိုက်ခြင်းအနုပညာ.pdf"
    },
]

# Display books only in self_improvement page
for book in self_improvement_books :
    Label(
        pages["Self-Improvement"],
        text=book["title"],
        font=subtitle_font,
        bg=colors["Self-Improvement"],
        fg="#4A4A4A"
    ).pack(pady=5)

    Button(
        pages["Self-Improvement"],
        text="📖 Open Book",
        font=text_font,
        bg="#4B7F52",
        fg="white",
        width=25,
        command=lambda path=book["path"]: open_pdf(path)
    ).pack(pady=10)
    # ---------------------- Love Books Only ----------------------
    love_books = [
    {
        "title": "🦉 Featured Book: ကမ္ဘာဟာ_ခင်ဗျားဖြစ်ကြောင်း",
        "path": r"C:\Users\USER\Desktop\project\Books\Love\ကမ္ဘာဟာ_ခင်ဗျားဖြစ်ကြောင်း.pdf"
    },
    {
        "title": "🦉 Featured Book: အကြင်သူသည်",
        "path": r"C:\Users\USER\Desktop\project\Books\Love\အကြင်သူသည်.pdf"
    },

    {   "title": "🦉 Featured Book: အမှတ်တရ",
        "path": r"C:\Users\USER\Desktop\project\Books\Love\အမှတ်တရ.pdf"
    }
]

# Display books only in Love page
for book in love_books:
    Label(
        pages["Love"],
        text=book["title"],
        font=subtitle_font,
        bg=colors["Love"],
        fg="#4A4A4A"
    ).pack(pady=5)

    Button(
        pages["Love"],
        text="📖 Open Book",
        font=text_font,
        bg="#4B7F52",
        fg="white",
        width=25,
        command=lambda path=book["path"]: open_pdf(path)
    ).pack(pady=10)
        # ---------------------- History Books Only ----------------------
    history_books = [

    {
        "title": "🦉 Featured Book: Will_Durant_The_Story_of_Civilization_XI_The_Age_of_Napoleon_XI",
        "path": r"C:\Users\USER\Desktop\project\Books\History\Will_Durant_The_Story_of_Civilization_XI_The_Age_of_Napoleon_XI.pdf"
    },
    {
        "title": "🦉 Featured Book: ဒေါက်တာသန်းထွန်း_ကျော်စွာ",
        "path": r"C:\Users\USER\Desktop\project\Books\History\ဒေါက်တာသန်းထွန်း_ကျော်စွာ.pdf"
    },
    {
        "title": "🦉 Featured Book: ရခိုင်ရာဇဝင်",
        "path": r"C:\Users\USER\Desktop\project\Books\History\ရခိုင်ရာဇဝင်.pdf"
    }
]

# Display books only in History page
for book in history_books:
    Label(
        pages["History"],
        text=book["title"],
        font=subtitle_font,
        bg=colors["History"],
        fg="#4A4A4A"
    ).pack(pady=5)

    Button(
        pages["History"],
        text="📖 Open Book",
        font=text_font,
        bg="#4B7F52",
        fg="white",
        width=25,
        command=lambda path=book["path"]: open_pdf(path)
    ).pack(pady=10)
            # ---------------------- Cartoon Books Only ----------------------
    cartoon_books = [

    {
        "title": "🦉 Featured Book: သမိန်ပေါသွပ်",
        "path": r"C:\Users\USER\Desktop\project\Books\Cartoon\သမိန်ပေါသွပ်.pdf"
    },
    {
        "title": "🦉 Featured Book: မြိုင်ရာဇာတွတ်ပီ၊_ကျွန်ုပ်နှင့်_အဏ္ဏဝါဒေ",
        "path": r"C:\Users\USER\Desktop\project\Books\Cartoon\မြိုင်ရာဇာတွတ်ပီ၊_ကျွန်ုပ်နှင့်_အဏ္ဏဝါဒေဝီ.pdf"
    },
    {
        "title": "🦉 Featured Book: ဘိုဘိုလက်ရွေးစင်ကာတွန်းများ",
        "path": r"C:\Users\USER\Desktop\project\Books\Cartoon\မင်းဇော်၊_ဘိုဘိုလက်ရွေးစင်ကာတွန်းများ၁_7.pdf"
    },
    {
        "title": "🦉 Featured Book: စုံထောက်ရှော်ဖိုးလှေ",
        "path": r"C:\Users\USER\Desktop\project\Books\Cartoon\စုံထောက်ရှော်ဖိုးလှော်၊_ကာတွန်း.pdf"
    },
    {
        "title": "🦉 Featured Book: မြိုင်ရာဇာတွတ်ပီ၊_ကျွန်ုပ်နှင့်သိုက်နန်းကပတ္တမြားကြီး",
        "path": r"C:\Users\USER\Desktop\project\Books\Cartoon\မြိုင်ရာဇာတွတ်ပီ၊_ကျွန်ုပ်နှင့်သိုက်နန်းကပတ္တမြားကြီး.pdf"
    },
]

# Display books only in Cartoon page
for book in cartoon_books:
    Label(
        pages["Cartoon"],
        text=book["title"],
        font=subtitle_font,
        bg=colors["Cartoon"],
        fg="#4A4A4A"
    ).pack(pady=5)

    Button(
        pages["Cartoon"],
        text="📖 Open Book",
        font=text_font,
        bg="#4B7F52",
        fg="white",
        width=25,
        command=lambda path=book["path"]: open_pdf(path)
    ).pack(pady=10)
            # ---------------------- Fantasy Books Only ----------------------
    fantasy_books = [

    {
        "title": "🦉 Featured Book: The Mysterious Island",
        "path": r"C:\Users\USER\Desktop\project\Books\Fantasy\The Mysterious Island.pdf"
    },
    {
        "title": "🦉 Featured Book: The Blue Fairy Book",
        "path": r"C:\Users\USER\Desktop\project\Books\Fantasy\The Blue Fairy Book.pdf"
    },
    {
        "title": "🦉 Featured Book: The Adventure of Pinocchio",
        "path": r"C:\Users\USER\Desktop\project\Books\Fantasy\The Adventure of Pinocchio.pdf"
    },
    {
        "title": "🦉 Featured Book: Alice's Adventures in Wonderland",
        "path": r"C:\Users\USER\Desktop\project\Books\Fantasy\Alice's Adventures in Wonderland.pdf"
    },
]

# Display books only in Fantasy page
for book in fantasy_books:
    Label(
        pages["Fantasy"],
        text=book["title"],
        font=subtitle_font,
        bg=colors["Fantasy"],
        fg="#4A4A4A"
    ).pack(pady=5)

    Button(
        pages["Fantasy"],
        text="📖 Open Book",
        font=text_font,
        bg="#4B7F52",
        fg="white",
        width=25,
        command=lambda path=book["path"]: open_pdf(path)
    ).pack(pady=10)
      
# ---------------------- Start the App ----------------------
show_frame(login_page)
window.mainloop()