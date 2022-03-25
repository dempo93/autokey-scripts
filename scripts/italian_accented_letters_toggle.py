import time

keyboard.send_keys("<shift>+<left>")
time.sleep(0.05)

def get_last_letter():
    try:
        return clipboard.get_selection()
    except Exception:
        return ''
        
def get_next_letter(last_letter):
    if last_letter=='à':
        return 'è'
    if last_letter=='è':
        return 'ò'
    if last_letter=='ò':
        return 'ì'                
    if last_letter=='ì':
        return 'ù'        
    return 'à'    
    
last_letter=get_last_letter()
next_letter=get_next_letter(last_letter)
 
if last_letter == '':
   keyboard.send_keys('<right>')
else:
   keyboard.send_keys('<delete>')
   
keyboard.send_keys(next_letter)