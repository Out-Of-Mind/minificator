#!/usr/bin/env python3
import os
import requests

def minify_css(path_to_css_file):
    # url to request (website minificator)
    url = 'https://cssminifier.com/raw'

    # opening css file
    with open(path_to_css_file, 'rb') as f:
        data = {'input': f.read()}

    # making request to get minified css file
    response = requests.post(url, data=data)

    # writing gotten file with suffix min
    with open(path_to_css_file[:-4]+'.min.css', 'w') as f:
        f.write(response.text)

def minify_js(path_to_js_file):
    #url to request (website minificator)
    url = 'https://javascript-minifier.com/raw'

    # opening js file
    with open(path_to_js_file, 'rb') as f:
        data = {'input': f.read()}

    # making request to get minified js file
    response = requests.post(url, data=data)

    # writing gotten file with suffix min
    with open(path_to_js_file[:-3]+'.min.js', 'w') as f:
        f.write(response.text)

def find_css_and_js(list_of_files, directory='.'):
    # setting local variables
    css_files = []
    js_files = []

    # finding css and js files
    for file in list_of_files:
        if '.css' in file:
            yield 'css', directory+'/'+file
        elif '.js' in file:
            yield 'js', directory+'/'+file
        else:
            continue

def main(directory=['.']):

    print('started minifying')
    # setting variables
    js_files = []
    css_files = []

    # finding css and js files in directories
    for d in directory:
        for i in os.walk(d):

            # checking for nested directories
            if i[0] == '.':
                for type_of_file, file in find_css_and_js(i[2]):

                    # don't add file to minification if it's already minified
                    if '.min.' in file:
                        continue
                    if type_of_file == 'css':
                        css_files.append(file)
                    elif type_of_file == 'js':
                        js_files.append(file)

            # doing it if we have nested directory(ies)
            else:
                for type_of_file, file in find_css_and_js(i[2], i[0]):

                    # don't add file to minification if it's already minified
                    if '.min' in file:
                        continue
                    if type_of_file == 'css':
                        css_files.append(file)
                    elif type_of_file == 'js':
                        js_files.append(file)

    # if css and js files weren't found - exit
    if len(js_files) == 0 and len(css_files) == 0:
        print('not found specified files((\nexiting...')
        exit()

    # minifying all found css files
    for css_file in css_files:
        minify_css(css_file)

    # minifying all found js files
    for js_file in js_files:
        minify_js(js_file)

    print('all found files (css and js) were minified!!!')
    exit()

if __name__ == '__main__':
    main()
