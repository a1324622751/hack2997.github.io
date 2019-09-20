import os

def SubdomainFinder(url):
    # 调用jsfinder
    print("begin search by jsfinder:")
    jsfindurl="http://"+url
    conmand1="python JSFinder.py -u "+jsfindurl+" -j -os output//domain_from_js.txt"
    print(conmand1)
    os.system(conmand1)
    # 调用teemo
    print("begin search by teemo:")
    #提取信息
    cut_begin=url.find('.')
    cut_begin=cut_begin+1
    subdourl=url[cut_begin:]
    command2="python2 teemo//teemo.py -d "+subdourl+" -o domain_from_teemo.txt"
    os.system(command2)
    # 调用finddomain-windows
    print("begin search by log:")
    command4="findomain-windows.exe -t "+url+ " -a -o txt"
    os.system(command4)
def ManageraddFinder(url):
    # 调用谷歌黑客命令
     print("begin information seach by google hack:\r\n")
def Dir_search():
    print("begin search dir:")
    # 调用webdirscan