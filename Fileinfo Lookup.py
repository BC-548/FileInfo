browserPath = 'open -a /Applications/Google\\ Chrome.app %s' # change to the path of your preferred web browser


import webbrowser
while True:
    ext = input('File Extension: ')
    
    if not ext or ext.isspace() : # check if the input contains nothing
        print("No extension entered! Please enter a filename extension")
    
    else:
        if ext.startswith("."):
            ext = ext[1:] # remove the '.' in front of the file extension
        print('https://fileinfo.com/extension/' + ext)
        webbrowser.get(browserPath).open('https://fileinfo.com/extension/' + ext) # Open FileInfo page with specified extension
