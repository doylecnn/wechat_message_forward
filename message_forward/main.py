import itchat, time
from itchat.content import *
from .config import *

def run():
    @itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], isGroupChat=True)
    def text_reply(msg):
        #print("{} in {} say: {}".format(msg.actualNickName, msg.user.nickName, msg.text))
        if msg.user.userName == chartroom.userName and msg.actualNickName in SCRIBUTE_USER_NAMES:
            master.send("{} in {} say: {}".format(msg.actualNickName, msg.user.nickName, msg.text))

    @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
    def download_files(msg):
        #print("{} in {} send: @{}@{}".format(msg.actualNickName, msg.user.nickName, typeSymbol, msg.fileName))
        if msg.user.userName == chartroom.userName and msg.actualNickName in SCRIBUTE_USER_NAMES:
            msg.download(msg.fileName)
            typeSymbol = {
                PICTURE: 'img',
                VIDEO: 'vid', }.get(msg.type, 'fil')
            master.send("{} in {} send: @{}@{}".format(msg.actualNickName, msg.user.nickName, typeSymbol, msg.fileName))
            master.send("@{}@{}".format(typeSymbol, msg.fileName))

    @itchat.msg_register(SYSTEM)
    def get_uin(msg):
        if msg['SystemInfo'] != 'uins': return
        ins = itchat.instanceList[0]
        fullContact = ins.memberList + ins.chatroomList + ins.mpList
        print('** Uin Updated **')
        for username in msg['Text']:
            member = itchat.utils.search_dict_list(
                fullContact, 'UserName', username)
            print(('%s: %s' % (
                member.get('NickName', ''), member['Uin']))
                .encode(sys.stdin.encoding, 'replace'))


    itchat.auto_login(enableCmdQR=2, hotReload=True)
    chartroom = itchat.search_chatrooms(name=GROUP_NAME)[0]
    master = itchat.search_friends(name=MASTER_NAME)[0]
    memberList = itchat.update_chatroom(chartroom.userName, detailedMember=True)
    itchat.run()
