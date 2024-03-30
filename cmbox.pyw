import customtkinter as ctk
from PIL import Image, ImageGrab, ImageFilter, ImageTk

Space4TitleLogo = ctk.CTkImage(dark_image=Image.open("PsysDataDir/Space4Img.png"))
class CMBox:
    """docstring for CMBox"""
    def __init__(self, icon, title, message):
        self.icon = icon
        self.title = title
        self.message = message

    def show(self):
        root = ctk.CTk()
        # root.title(self.title)
        root.geometry("400x200+500+150")
        root.configure(fg_color="#335533")
        root.overrideredirect(True)
        # root.wm_attributes('-transparentcolor', root['bg'])
        root.wm_attributes('-transparentcolor', '#335533')
        root.grab_set()

        def DestroyMe():
            root.destroy()

        rootMain = ctk.CTkFrame(root, fg_color="#555555", corner_radius=12, border_width=0)
        rootMain.pack(fill=ctk.BOTH, expand=True)
        HdrFrame = ctk.CTkFrame(
            rootMain,
            fg_color="#222222",
            corner_radius=0,
        )
        HdrFrame.pack(fill=ctk.X, expand=True, anchor=ctk.N)
        Header = ctk.CTkLabel(
            master=HdrFrame,
            text=self.title,
            text_color="white",
            fg_color="#222222",
            font=("Tahoma",15, "bold")
        )
        Header.pack(pady=5)
        IconLabel = ctk.CTkLabel(
            master=rootMain,
            text="",
            image=self.icon,
            text_color="white",
            fg_color="#555555",
            font=("Tahoma", 12, "bold"),
            justify=ctk.RIGHT
        )
        IconLabel.pack(pady=5, anchor=ctk.N)
        label = ctk.CTkLabel(
            master=rootMain,
            text=self.message,
            text_color="white",
            fg_color="#555555",
            font=("Tahoma", 12, "bold"),
            justify=ctk.RIGHT
        )
        label.pack(pady=5, anchor=ctk.N)

        button = ctk.CTkButton(
            master=rootMain,
            text="قبول",
            command=DestroyMe,
            font=("Tahoma", 14, "bold"),
            width=80,
            hover_color="dark blue",
            fg_color="blue"

        )
        button.pack(pady=10, anchor=ctk.N)

        root.mainloop()

def CMInfo(icon, title, message):
    messagebox = CMBox(icon, title, message)
    messagebox.show()

msg = CMInfo(
    Space4TitleLogo,
    "من عنوان هستم",
    "من یک پنجره دستی پیام هستم"
)

