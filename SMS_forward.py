import os
import pyinotify
import re
import telepot
import time

botToken = ''
forwardID =

class MyEventHandler(pyinotify.ProcessEvent):
    #def process_IN_CREATE(self, event):
     #   print("CREATE event:", event.pathname)
     #   partnum = re.split('_|.txt', event.pathname)
     #   print(int(partnum[4]))
        #if int(partnum[4])==0:
            #openfile = open(event.pathname)
            #global text = openfile.read()

          #  print(partnum[4])
    def process_IN_CLOSE_WRITE(self, event):
        print("CLOSE_WRITE event:", event.pathname)
        filenamesplit = re.split('_|N', event.pathname)
        partnum = re.split('_|.txt', event.pathname)
        #print(filenamesplit)

        datenum = filenamesplit[1]
        date = str(datenum[:4]) + '/' + str(datenum[4:6]) + '/' + str(datenum[6:])
        timenum = filenamesplit[2]
        time = str(timenum[:2]) + ':' + str(timenum[2:4]) + ':' + str(timenum[4:])
        sender = filenamesplit[4]

        openfile = open(event.pathname)
        text = openfile.read()
        bot = telepot.Bot(botToken)
        bot.sendMessage(forwardID, '%s\n%s\n消息来自:\n%s\n\n%s' % (date, time, sender, text))



def main():
    # watch manager
    wm = pyinotify.WatchManager()
    wm.add_watch('/home/pi/Desktop/test', pyinotify.IN_CLOSE_WRITE, rec=True)
    #wm.add_watch('/var/spool/gammu/inbox', pyinotify.IN_CREATE, rec=True)
    # /tmp是可以自己修改的监控的目录
    # event handler
    eh = MyEventHandler()

    # notifier
    notifier = pyinotify.Notifier(wm, eh)
    notifier.loop()


if __name__ == '__main__':
    main()
