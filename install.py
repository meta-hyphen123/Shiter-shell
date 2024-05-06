import os
current_file_path = os.path.dirname(os.path.abspath(__file__))
tools_folder = os.path.join(current_file_path, 'system_files')
logo = """
  _          _ _        
 | |__   ___| | | ___   
 | '_ \ / _ \ | |/ _ \  
 | | | |  __/ | | (_) | 
 |_| |_|\___|_|_|\___/  
                         """
print(logo)
def namme():
    install_txt_path = os.path.join(tools_folder, 'name.txt')

    with open(install_txt_path, 'r') as file:
        content = file.read()
    
    return content
def forget(content):
    install_txt_path = os.path.join(tools_folder, 'name.txt')

    # Open the file in write mode to delete existing content
    with open(install_txt_path, 'w') as file:
        pass  # This will delete all content from the file
    
    # Now open the file in append mode to write new content
    with open(install_txt_path, 'a') as file:
        file.write(content)

def reset():
    pdww = input("please set the password>")
    forget(pdww)
current_file_path = os.path.dirname(os.path.abspath(__file__))
inputA = input("press “Enter” to install>")
reset()
os.chdir(current_file_path)
print("""""")
os.system("pip3 install -r reqirements.txt")
os.system("python3 Shiter.py")
