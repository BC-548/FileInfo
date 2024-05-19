import webbrowser
while True:
    ext = input('File Extension (without dot): ')
    
    if not ext or ext.isspace() : # check if the input contains nothing
        print("No extension entered! Please enter a filename extension")
    
    else:
        print('https://fileinfo.com/extension/' + ext)
        webbrowser.get('open -a "/Applications/Google Chrome.app" %s').open('https://fileinfo.com/extension/' + ext) # Open Fileinfo page with specified extension in Google Chrome
