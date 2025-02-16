from apps.Messaging_App.func.gen_keys import gen_keys
from apps.Messaging_App.lib.keys_system import the_keys, save_keys

def create_new_user(name,fromUser,n,e):

    temp_keys = the_keys()

    in_list = False

    for key in temp_keys:
      if "fromUser" in temp_keys[key]:
        if temp_keys[key]["fromUser"] == fromUser:
            in_list = True
            if temp_keys[key]["n"] == 0 and temp_keys[key]["e"] == 0:
                temp_keys[key]["n"] = n
                temp_keys[key]["e"] = e
                save_keys(temp_keys)
                return(key)

    if not in_list:
        number = str(len(temp_keys) + 1)
        
        temp_keys[number] = {}
        
        temp_keys[number]["name"] = name
        temp_keys[number]["fromUser"] = fromUser
        temp_keys[number]["n"] = n
        temp_keys[number]["e"] = e

        save_keys(temp_keys)
        
        return(number)