import webbrowser
import sys

browserPath = 'open -a /Applications/Google\\ Chrome.app %s' # change to the path of your preferred web browser


def openURL():
    global ext
    if ext.startswith("."):
        ext = ext[1:] # remove the '.' in front of the file extension
    print('https://fileinfo.com/extension/' + ext)
    webbrowser.get(browserPath).open('https://fileinfo.com/extension/' + ext) # Open FileInfo page with specified extension


if len(sys.argv) == 1: # if there is no arguments passed to the script
    print("Interactive mode")
    try:
        while True:
            ext = input('File Extension: ')
            openURL()
    except KeyboardInterrupt: # do not throw an error on ctrl-c
        sys.exit()

else:
    ext = sys.argv[1]
    openURL()