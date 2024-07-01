from dearpygui.dearpygui import *

create_context()
create_viewport(title="Login", width=400, height=600, resizable=False)

with font_registry():
    welcomeSign_font = add_font('./digital-7.ttf', 38)

def progress(sender, app_data):
    print(get_value('username'))
    print(get_value('phome'))
    print(get_value('password'))
    stop_dearpygui()

    

with window(no_resize=True, no_title_bar=True, no_move=True, width=400, height=600, pos=(0,0)):
    sign = add_text("Login", pos=(140,20))
    bind_item_font(sign, welcomeSign_font)
    username = add_input_text(label="Username",tag="username",width=250, pos=(90, 170)) 
    phone = add_input_text(label="Phone",tag='phone',width=250, pos=(90, 200))
    password = add_input_text(label="Password",tag='password',width=250, pos=(90, 270),password=True)
    login = add_button(label="Login", width=250, pos=(90, 400), callback=progress)
setup_dearpygui()
show_viewport()
start_dearpygui()
