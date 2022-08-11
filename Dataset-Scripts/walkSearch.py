import os
import json
import re
from csv import writer


def isHTML(string):
    verdict = string.endswith(".html")
    if verdict:
        return True
    return False

def isJS(string):
    verdict = string.endswith(".js")
    if verdict:
        return True
    return False

def isJSON(string):
    verdict = string.endswith(".json")
    if verdict:
        return True
    return False

def isCSS(string):
    verdict = string.endswith(".css")
    if verdict:
        return True
    return False

def isNotMessagesJSON(string):
    verdict = string.endswith("messages.json")
    if verdict:
        return False 
    return True

def isManifest(string):
    verdict = string.endswith("/manifest.json")
    if verdict:
        return True
    return False

def isNotDir(string):
    if os.path.isdir(string):
        return False
    return True

def averageList(theList):
    count = 0
    for item in theList: 
        count += item
    if len(theList) != 0:
        count = count / len(theList)
    else:
        count = 0
    return count

http_bytes = "http:".encode('utf-8')
https_bytes = "https:".encode('utf-8')
iframe_bytes = "<iframe".encode('utf-8')
XMLR_bytes = "XMLHttpRequest".encode('utf-8')
scriptTag_bytes = "<script".encode('utf-8')
SCRIPTTag_bytes = "<SCRIPT".encode('utf-8')
POST_bytes = "\"POST\"".encode('utf-8')
GET_bytes = "\"GET\"".encode('utf-8')
write_bytes = "document.write".encode('utf-8')
innerHTML_bytes = "innerHTML".encode('utf-8')
body_bytes = "<body".encode('utf-8')
img_bytes = "<img".encode('utf-8')
fromCharCode_bytes = "fromCharCode".encode('utf-8')
form_bytes = "<form".encode('utf-8')
backgroundImg_bytes = "background-image:".encode('utf-8')
behavior_bytes = "behavior:".encode('utf-8')
behaviour_bytes = "behaviour:".encode('utf-8')
import_bytes = "@import".encode('utf-8')
createElement1_bytes = "createElement('script')".encode('utf-8')
createElement2_bytes = 'createElement("script")'.encode('utf-8')
tabsExecute_bytes = "tabs.executeScript".encode('utf-8')
appendChild_bytes = "appendChild".encode('utf-8')
percentU_bytes = "%u".encode('utf-8')
backslashX_bytes = "\\x".encode('utf-8')
backslash_bytes = "\\".encode('utf-8')
percent_bytes = "%".encode('utf-8')
exclamation_bytes = "!".encode('utf-8')
href1_bytes = "href='javascript".encode('utf-8')
href2_bytes = 'href="javascript'.encode('utf-8')
clickjack_bytes = "clickjack".encode('utf-8')
clickJack_bytes = "clickJack".encode('utf-8')
ClickJack_bytes = "ClickJack".encode('utf-8')
VBScript_bytes = "VBScript".encode('utf-8')
vbscript_bytes = "vbscript".encode('utf-8')
VBSCRIPT_bytes = "VBSCRIPT".encode('utf-8')
coinhive_bytes = "coinhive".encode('utf-8')
CoinHive_bytes = "CoinHive".encode('utf-8')


keywords=["await","break","case","catch","class","const","continue","debugger","default","delete","do","else","enum","export","extends","false","finally","for","function","if","implements","import","in","instanceof","interface","let","new","null","package","private","protected","public","return","super","switch","static","this","throw","try","True","typeof","var","void","while","with","yield"]

keywords=["this","if","var"]


rootdir = "./dataset/"
directories = []
for item in os.listdir(rootdir):
    d = os.path.join(rootdir, item)
    if os.path.isdir(d):
        directories.append(item)


#directory = "./Extensions/"


for directory in directories:
    files = os.listdir(rootdir + directory)
    directoryPath = os.path.join(rootdir, directory)

    extensionTotal = []
    extensionTotal = [directory]

    htmlFiles = []
    jsonFiles = []
    jsFiles = []
    cssFiles = []

    html_totalHttp = 0
    html_totalHttps = 0
    html_totalJSCalls = 0
    html_totalIFrames = 0
    html_totalXMLR = 0
    html_totalScriptTags = 0
    html_totalPOST = 0
    html_totalGET = 0
    html_totalObjectTags = 0
    html_totalBodyTags = 0
    html_totalImgTags = 0
    html_totalFromCharCode = 0
    html_totalFormTags = 0
    html_totalBackground = 0
    html_totalBehavior = 0
    html_totalImport = 0
    html_totalWrite = 0
    html_totalWriteIn = 0
    html_totalInnerHTML = 0
    html_totalCreateElement = 0
    html_totalTabsExecute = 0
    html_totalAppendChild = 0
    html_totalPercentU = 0
    html_totalBackslashX = 0
    html_totalBackslash = 0
    html_totalPercent = 0
    html_totalExclamation = 0
    html_totalVBScript = 0
    html_totalHrefJS = 0
    html_totalClickJack = 0
    html_totalCoinHive = 0

    js_totalHttp = 0
    js_totalHttps = 0
    js_totalIFrames = 0
    js_totalKeywords = 0
    js_totalXMLR = 0
    js_totalJSCalls = 0
    js_totalPOST = 0
    js_totalGET = 0
    js_totalWrite = 0
    js_totalWriteIn = 0
    js_totalInnerHTML = 0
    js_totalFromCharCode = 0
    js_totalCreateElement = 0
    js_totalTabsExecute = 0
    js_totalAppendChild = 0
    js_totalPercentU = 0
    js_totalBackslashX = 0
    js_totalBackslash = 0
    js_totalExclamation = 0
    js_totalClickJack = 0
    js_totalCoinHive = 0

    js_totalRatioList =[]

    css_totalBackgroundImg = 0
    css_totalBehavior = 0
    css_totalImport = 0

    manifest_permissions = []
    permission_allURLS = 0
    permission_allHttp = 0
    permission_allHttps = 0
    permission_allHyperlinks = 0
    permission_webRequest = 0
    permission_webRequestBlocking = 0
    permission_tabs = 0
    permission_storage = 0
    permission_history = 0
    permission_cookies = 0
    permission_notifications = 0
    permission_background = 0
    permission_unlimitedStorage = 0
    permission_contextMenus = 0
    permission_management = 0
    permission_activeTab = 0
    permission_sessions = 0
    permission_identity = 0
    permission_webNavigation = 0
    permission_downloads = 0
    permission_debugger = 0
    permission_alarms = 0
    permission_scripting = 0
    permission_search = 0
    permission_fileSystem = 0
    permission_fileSystemWrite = 0
    permission_desktopCapture = 0

    for root, subdirectories, files in os.walk(directoryPath):

        for subdirectory in subdirectories:
            f = os.path.join(root, subdirectory)
            if isHTML(f):
                htmlFiles.append(f)
            if isJS(f) and isNotDir(f):
                jsFiles.append(f)
            if isJSON(f) and isNotMessagesJSON(f):
                jsonFiles.append(f)
            if isCSS(f):
                cssFiles.append(f)

        for file in files:
            f = os.path.join(root, file)
            if isHTML(f):
                htmlFiles.append(f)
            if isJS(f) and isNotDir(f):
                jsFiles.append(f)
            if isJSON(f) and isNotMessagesJSON(f):
                jsonFiles.append(f)
            if isCSS(f):
                cssFiles.append(f)



    # For every .html file    
    for file in htmlFiles:
        with open(file, "rb") as theFile:
            contents = theFile.read()
            theFile.close()

        # Count each feature's number of occurances
        pattern = re.compile(b'http[^\s]+\.js')
        html_externalJSCalls = len(re.findall(pattern, contents))
        
        pattern = re.compile(b'[^\w]object[\w]')
        html_objectTagCount = len(re.findall(pattern, contents))

        html_totalHttp += contents.count(http_bytes)
        html_totalHttps += contents.count(https_bytes)
        html_totalJSCalls += html_externalJSCalls
        html_totalIFrames += contents.count(iframe_bytes) 
        html_totalXMLR += contents.count(XMLR_bytes)
        html_totalScriptTags += contents.count(scriptTag_bytes) + contents.count(SCRIPTTag_bytes)
        html_totalPOST += contents.count(POST_bytes)
        html_totalGET += contents.count(GET_bytes)
        html_totalObjectTags += html_objectTagCount
        html_totalBodyTags += contents.count(body_bytes)
        html_totalImgTags += contents.count(img_bytes)
        html_totalFromCharCode += contents.count(fromCharCode_bytes)
        html_totalFormTags += contents.count(form_bytes)
        html_totalWrite += contents.count(write_bytes)
        html_totalInnerHTML += contents.count(innerHTML_bytes)
        html_totalCreateElement += contents.count(createElement1_bytes) + contents.count(createElement2_bytes)
        html_totalTabsExecute += contents.count(tabsExecute_bytes)
        html_totalAppendChild += contents.count(appendChild_bytes)
        html_totalPercentU += contents.count(percentU_bytes)
        html_totalBackslashX += contents.count(backslashX_bytes)
        html_totalBackslash += contents.count(backslash_bytes)
        html_totalPercent += contents.count(percent_bytes)
        html_totalExclamation += contents.count(exclamation_bytes)
        html_totalHrefJS += contents.count(href1_bytes) + contents.count(href2_bytes)
        html_totalClickJack += contents.count(clickjack_bytes) + contents.count(clickJack_bytes) + contents.count(ClickJack_bytes)
        html_totalVBScript += contents.count(VBScript_bytes) + contents.count(vbscript_bytes) + contents.count(VBSCRIPT_bytes)
        html_totalCoinHive += contents.count(coinhive_bytes) + contents.count(CoinHive_bytes)

        css_totalBackgroundImg += contents.count(backgroundImg_bytes)
        css_totalBehavior += contents.count(behavior_bytes) + contents.count(behaviour_bytes)
        css_totalImport += contents.count(import_bytes)




    # For every .js file
    for file in jsFiles:
        with open(file, "rb") as theFile:
            contents = theFile.read()
            theFile.close()

        # Search for js keywords
        for word in keywords:
            pattern = "[^\w]" + word + "[^\w]"
            pattern = pattern.encode('utf-8')
            pattern = re.compile(pattern)
            js_totalKeywords += len(re.findall(pattern, contents))


        pattern = re.compile(b'http[^\s]+\.js')
        js_externalJSCalls = len(re.findall(pattern, contents))

        
        js_totalHttp += contents.count(http_bytes)
        js_totalHttps += contents.count(https_bytes)
        js_totalIFrames += contents.count(iframe_bytes)
        js_totalXMLR += contents.count(XMLR_bytes)
        js_totalJSCalls += js_externalJSCalls
        js_totalPOST += contents.count(POST_bytes)
        js_totalGET += contents.count(GET_bytes)
        js_totalWrite += contents.count(write_bytes)
        js_totalInnerHTML += contents.count(innerHTML_bytes)
        js_totalFromCharCode += contents.count(fromCharCode_bytes)
        js_totalCreateElement += contents.count(createElement1_bytes) + contents.count(createElement2_bytes)
        js_totalTabsExecute += contents.count(tabsExecute_bytes)
        js_totalAppendChild += contents.count(appendChild_bytes)
        js_totalPercentU += contents.count(percentU_bytes)
        js_totalBackslashX += contents.count(backslashX_bytes)
        js_totalBackslash += contents.count(backslash_bytes)
        js_totalExclamation += contents.count(exclamation_bytes)
        js_totalClickJack += contents.count(clickjack_bytes) + contents.count(clickJack_bytes) + contents.count(ClickJack_bytes)
        js_totalCoinHive += contents.count(coinhive_bytes) + contents.count(CoinHive_bytes)

        all_words = contents.split()
        if len(all_words) != 0:
            js_keywordRatio = js_totalKeywords / len(all_words)
        else:
            js_keywordRatio = 0
        js_totalRatioList.append(js_keywordRatio)



    
    # For every .json file
    for file in jsonFiles:
        with open(file, "rb") as theFile:
            contents = theFile.read()
            theFile.close()

        if isManifest(file):
            json_dict = json.loads(contents)
            try:
                manifest_permissions = json_dict['permissions']
            except:
                print("'" + file + "': has no 'permissions'")

                

    # For every .css file
    for file in cssFiles:
        with open(file, "rb") as theFile:
            contents = theFile.read()
            theFile.close()

        css_totalBackgroundImg += contents.count(backgroundImg_bytes)
        css_totalBehavior += contents.count(behavior_bytes) + contents.count(behaviour_bytes)
        css_totalImport += contents.count(import_bytes)


    # Specifying the permissions
    for permission in manifest_permissions:
        if permission == "<all_urls>":
            permission_allURLS = 1
        elif permission == "http://*/*":
            permission_allHttp = 1
        elif permission == "https://*/*":
            permission_allHttps = 1
        elif permission == "*://*/*":
            permission_allHyperlinks = 1
        elif permission == "webRequest":
            permission_webRequest = 1
        elif permission == "webRequestBlocking":
            permission_webRequestBlocking = 1
        elif permission == "tabs":
            permission_tabs = 1
        elif permission == "storage":
            permission_storage = 1
        elif permission == "history":
            permission_history = 1
        elif permission == "cookies":
            permission_cookies = 1
        elif permission == "notifications":
            permission_notifications = 1
        elif permission == "background":
            permission_background = 1
        elif permission == "unlimitedStorage":
            permission_unlimitedStorage = 1
        elif permission == "contextMenus":
            permission_contextMenus = 1
        elif permission == "management":
            permission_management = 1
        elif permission == "activeTab":
            permission_activeTab = 1
        elif permission == "sessions":
            permission_sessions = 1
        elif permission == "identity":
            permission_identity = 1
        elif permission == "webNavigation":
            permission_webNavigation = 1
        elif permission == "downloads":
            permission_downloads = 1
        elif permission == "alarms":
            permission_alarms = 1
        elif permission == "scripting":
            permission_scripting = 1
        elif permission == "search":
            permission_search = 1
        elif permission == "fileSystem":
            permission_fileSystem = 1
        elif permission == "fileSystem.write":
            permission_fileSystemWrite = 1
        elif permission == "desktopCapture":
            permission_desktopCapture = 1
        




    # Adding the Extension information to the CSV
    extensionTotal.append(html_totalHttp)        #html_http
    extensionTotal.append(html_totalHttps)       #html_https
    extensionTotal.append(html_totalJSCalls)     #html_external-js
    extensionTotal.append(html_totalIFrames)     #html_iframes
    #extensionTotal.append(html_totalXMLR)        #html_XMLHttpRequests
    extensionTotal.append(html_totalScriptTags)  #html_scriptTags
    #extensionTotal.append(html_totalPOST)        #html_POST
    #extensionTotal.append(html_totalGET)         #html_GET
    extensionTotal.append(html_totalObjectTags)  #html_objectsTags
    extensionTotal.append(html_totalBodyTags)    #html_bodyTags
    extensionTotal.append(html_totalImgTags)     #html_imgTags
    extensionTotal.append(html_totalFromCharCode)#html_fromCharCode
    extensionTotal.append(html_totalFormTags)    #html_formTags
    extensionTotal.append(html_totalWrite)       #html_document.write
    #extensionTotal.append(html_totalInnerHTML)   #html_innerHTML
    #extensionTotal.append(html_totalCreateElement)#html_createElement('script')
    #extensionTotal.append(html_totalTabsExecute) #html_tabs.executeScript()
    #extensionTotal.append(html_totalAppendChild) #html_appendChild()
    #extensionTotal.append(html_totalPercentU)    #html_%u
    extensionTotal.append(html_totalBackslashX)  #html_\x
    extensionTotal.append(html_totalBackslash)   #html_\
    extensionTotal.append(html_totalPercent)     #html_%
    extensionTotal.append(html_totalExclamation) #html_!
    extensionTotal.append(html_totalHrefJS)      #html_href=javascript
    #extensionTotal.append(html_totalClickJack)   #html_ClickJack
    #extensionTotal.append(html_totalVBScript)    #html_VBScript
    extensionTotal.append(html_totalCoinHive)    #html_CoinHive
    extensionTotal.append(js_totalHttp)          #js_http
    extensionTotal.append(js_totalHttps)         #js_https
    extensionTotal.append(js_totalIFrames)       #js_iframes
    extensionTotal.append(js_totalXMLR)          #js_XMLHttpRequests
    extensionTotal.append(js_totalJSCalls)       #js_external-js
    extensionTotal.append(js_totalPOST)          #js_POST
    extensionTotal.append(js_totalGET)           #js_GET
    extensionTotal.append(js_totalWrite)         #js_document.write
    extensionTotal.append(js_totalInnerHTML)     #js_innerHTML
    extensionTotal.append(js_totalFromCharCode)  #js_fromCharCode
    extensionTotal.append(js_totalCreateElement) #js_createElement('script')
    extensionTotal.append(js_totalKeywords)      #js_keywords
    extensionTotal.append(js_totalTabsExecute)   #js_tabs.executeScript()
    extensionTotal.append(js_totalAppendChild)   #js_appendChild()
    extensionTotal.append(js_totalPercentU)      #js_%u
    extensionTotal.append(js_totalBackslashX)    #js_\x
    extensionTotal.append(js_totalBackslash)     #js_\
    extensionTotal.append(js_totalExclamation)   #js_!
    #extensionTotal.append(js_totalClickJack)     #js_ClickJack
    extensionTotal.append(js_totalCoinHive)      #js_CoinHive
    extensionTotal.append(css_totalBackgroundImg)#css_background-image
    extensionTotal.append(css_totalBehavior)     #css_behavior
    extensionTotal.append(css_totalImport)       #css_@import


    js_totalRatioAverage = averageList(js_totalRatioList)
    extensionTotal.append(js_totalRatioAverage)


    # Add the Permissions
    #extensionTotal.append(permission_allURLS)
    #extensionTotal.append(permission_allHttp)
    #extensionTotal.append(permission_allHttps)
    #extensionTotal.append(permission_allHyperlinks)
    #extensionTotal.append(permission_webRequest)
    #extensionTotal.append(permission_webRequestBlocking)
    #extensionTotal.append(permission_tabs)
    #extensionTotal.append(permission_storage)
    #extensionTotal.append(permission_history)
    #extensionTotal.append(permission_cookies)
    #extensionTotal.append(permission_notifications)
    #extensionTotal.append(permission_background)
    #extensionTotal.append(permission_unlimitedStorage)
    #extensionTotal.append(permission_contextMenus)
    #extensionTotal.append(permission_management)
    #extensionTotal.append(permission_activeTab)
    #extensionTotal.append(permission_sessions)
    #extensionTotal.append(permission_identity)
    #extensionTotal.append(permission_webNavigation)
    #extensionTotal.append(permission_downloads)
    #extensionTotal.append(permission_debugger)
    #extensionTotal.append(permission_alarms)
    #extensionTotal.append(permission_scripting)
    #extensionTotal.append(permission_search)
    #extensionTotal.append(permission_fileSystem)
    #extensionTotal.append(permission_fileSystemWrite)
    #extensionTotal.append(permission_desktopCapture)

    # Malicious Flag: 1=Malicious, 0=Not
    if directory.endswith("Vir-Extension"):
        extensionTotal.append(1)
    else:
        extensionTotal.append(0)


    #extensionTotal.append(manifest_permissions)  #permissions

    with open("info.csv", "a", newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(extensionTotal)
        f_object.close




