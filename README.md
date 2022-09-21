# Raspberry Pi4 & SIM7600 SMS転送
Raspberry Pi4とSIM7600で指定されたtelegramアカウントにSMSを転送するプログラムです。  

## 仕組み
* SIM7600が受信したらPiにインストールされた[Gammu](https://wammu.eu/gammu/) が受信したSMS内容をファイルに保存する。
* ファイルの保存があった時、[TelegramのBot](https://core.telegram.org/bots) が内容を指定されたアカウントに転送する。  

## 使用方法
* line 7 ```botToken```でのBotのIDとTokenを入力
* line 8 ```forwardID```で転送先アカウントのIDを入力
* line 42 ```wm.add_watch```でモニターするファイル保存のdirectoryを指定できる

### 準備事項
* Piにgammu-smsdをインストールする
* /etc/gammu-smsdrcで環境を設定する
* SIM7600の取り付け及び設定（[参考資料](https://thepihut.com/blogs/raspberry-pi-tutorials/how-to-connect-your-raspberry-pi-to-a-3g-network) )
* Telegram BotのIDとTokenの取得、転送先アカウントのIDの取得([参考資料](https://core.telegram.org/bots))


***参考になったサイト***
* https://zhuanlan.zhihu.com/p/53387245
* https://zhuanlan.zhihu.com/p/30450761
* https://zhuanlan.zhihu.com/p/38853178
* https://pypi.org/project/inotify/
* https://docs.gammu.org/smsd/run.html
* https://www.pythoncentral.io/execute-python-script-file-shell/
* https://andypi.co.uk/2017/05/06/raspberry-pi-sms-to-email-gateway-part-1/
* https://www.cnblogs.com/zhouzhishuai/p/9633214.html
* https://www.cnblogs.com/hollyspirit/p/3182828.html
* https://blanktar.jp/blog/2013/03/python-inotify
* https://escapologybb.com/send-sms-from-raspberry-pi/
* https://ygin.pro/raspberry-pi-sms/#%E5%89%8D%E6%83%85%E4%BB%8B%E7%BB%8D
