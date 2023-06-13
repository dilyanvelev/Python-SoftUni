from json import load

from canvas import *


def render_entry():
    register_btn = Button(
        root,
        text="Register",
        bg="green",
        fg="white",
        borderwidth=0,
        width=20,
        height=3,
        command=register
    )
    login_btn = Button(
        root,
        text="Login",
        bg="blue",
        fg="white",
        width=20,
        height=3,
        command=login
    )
    frame.create_window(350, 260, window=register_btn)
    frame.create_window(350, 320, window=login_btn)


def register():
    clean_screen()
    frame.create_text(100, 50, text="First name: ")
    frame.create_text(100, 100, text="Last name: ")
    frame.create_text(100, 150, text="Username: ")
    frame.create_text(100, 200, text="Password: ")

    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 50, window=last_name_box)
    frame.create_window(200, 50, window=username_box)
    frame.create_window(200, 50, window=password_box)

    register_btn = Button(
        root,
        text="Register",
        bg="green",
        fg="white",
        command=registration
    )
    frame.create_window(200, 50, window=register_btn)


def login():
    clean_screen()


def registration():
    info_dict = {
        "first_name": first_name_box.get(),
        "last_name": last_name_box.get(),
        "username": username_box.get(),
        "password": password_box.get(),
    }
    if check_registration(info_dict):
        pass


def check_registration(info):
        for el in info.values():
            if el.strip() == "":
                frame.create_text(
                    300,
                    300,
                    text="We are missing some information, please check your fields!",
                    fill="red",
                    tag="error",
                )
                return False
        frame.delete("error")

        info_data = []
        with open("db/users_information.json","r") as users_file:
            for line in users_file:
                info_data.append(load(line))



first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0)
