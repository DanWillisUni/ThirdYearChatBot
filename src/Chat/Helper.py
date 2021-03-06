import appSettings

import Chat.FbMessenger as fbm
import PartTwo.Helpers.SPHelper as sph

def helper_print(engine, message):
    if appSettings.get_API() == "fb":
        user_id = sph.get_last_user_id()
        fbm.send_message(user_id,message)
    elif appSettings.get_API() == "api":
        engine.write(message)
    elif appSettings.get_API() == "console":
        print(message)

def helper_input(engine,prompt):
    user_message = ""
    if appSettings.get_API() == "fb":
        user_message = fbm.input_func(prompt)
    elif appSettings.get_API() == "api":
        user_message = engine.prompt(prompt)
    elif appSettings.get_API() == "console":
        user_message = input(prompt)

    if user_message == "RESET":
        engine.reset()
        engine.run()
    elif user_message == "QUIT":
        helper_print("Glad I could help, bye for now")
        engine.reset()
    else:
        return user_message

