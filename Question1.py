#To find no of Servers in an organization with Different OS(Windows, linus, AIX)
def No_of_servers(OS):
    if OS == 'Linux':
      print('8000 Linux servers are available')
    elif OS == 'AIX':
      print('4500 AIX servers are available')
    elif OS == 'Windows':
      print('7500 Windows servers are available')
    else:
      print('Not Supported OS')

No_of_servers('Linux')
