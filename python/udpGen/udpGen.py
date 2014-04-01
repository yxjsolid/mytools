#coding=utf-8
import sys
import socket
import binascii
from time import sleep
from udpGenGui import *
import wx.lib.agw.genericmessagedialog as GMD

defaultPktData = '0000000000020000000000000474657374056c6f63616c0000010001c00c001c0001'
defaultSrcIp = '192.168.168.1'
defaultDstIp = '224.0.0.251'
defaultDstPort = '5353'
defaultSrcPort = '5353'


def genData(dataLen):
    dataString = ""
    for i in range(dataLen):
        dataString += chr(ord('a') + i % 26)

    dataString = binascii.hexlify(dataString)
    return dataString


class udpGen():
    totalSend = 0

    def __init__(self):
        self.intervalMs = 10
        self.pktNum = 1
        self.ttl = 10
        self.srcPort = 0
        pass

    def setSrc(self, ip, port):
        self.srcIp = ip
        self.srcPort = port

    def setDst(self, ip, port):
        self.dstIp = ip
        self.dstPort = port

    def setTTL(self, ttl):
        self.ttl = int(ttl)

    def setPktSendCfg(self, pktNum, interval):
        self.pktNum = int(pktNum)
        self.intervalMs = int(interval)

    def openSocket(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            self.s.bind((self.srcIp, int(self.srcPort)))
            self.s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, self.ttl)
            self.s.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, self.ttl)
            return True
        except:
            print sys.exc_info()
            return False

    def doSend(self, data, gui):
        cnt = 0
        if not self.openSocket():
            if gui:
                gui.doAlert("socket init failed, port may be occupied")
            return

        while True:
            try:
                s = self.s
                s.sendto(data, (self.dstIp, int(self.dstPort)))
                cnt += 1
                self.__class__.totalSend += 1
                if gui:
                    gui.doSetStatusBar("total send: %d" % self.__class__.totalSend, 1)
                    if not gui.running:
                        gui.doSetStatusBar("packet send: %d" % cnt + "  force stopped", 0)
                        break
                    gui.doSetStatusBar("packet send: %d" % cnt, 0)

                if cnt >= self.pktNum:
                    break
                wx.Yield()
                sleep(self.intervalMs * 0.01)

            except KeyboardInterrupt:
                print 'force stop'
                break

        self.s.close()


class udpGenGui(udpGenGuiBase):
    def __init__(self, parent):
        udpGenGuiBase.__init__(self, parent)
        self.running = 0
        self.index = 0
        self.setPktDataModeAuto(0)
        self.setDefault()

    def setDefault(self):
        self.txt_dstIp.SetValue(defaultDstIp)
        self.txt_srcIp.SetValue(defaultSrcIp)
        self.txt_srcPort.SetValue(defaultSrcPort)
        self.txt_dstPort.SetValue(defaultDstPort)
        self.setPktDataString(defaultPktData)

    def onSend(self, evt):
        gen = udpGen()
        gen.setTTL(self.getTTL())
        gen.setSrc(self.getSrcIp(), self.getSrcPort())
        gen.setDst(self.getDstIp(), self.getDstPort())
        gen.setPktSendCfg(self.getPktNum(), self.getInterval())

        data = self.getPktData()
        if data is None:
            self.doAlert("packet data should be hex format")
            return

        self.btn_send.Disable()
        self.running = 1

        gen.doSend(self.getPktData(), self)
        self.btn_send.Enable()
        self.running = 0

    def onStop(self, evt):
        self.running = 0

    def getSrcIp(self):
        return self.txt_srcIp.GetValue()

    def getSrcPort(self):
        return  self.txt_srcPort.GetValue()

    def getDstIp(self):
        return  self.txt_dstIp.GetValue()

    def getDstPort(self):
        return  self.txt_dstPort.GetValue()

    def getTTL(self):
        return self.txt_ttl.GetValue()

    def getInterval(self):
        return self.txt_interval.GetValue()

    def getPktNum(self):
        return self.txt_pktNum.GetValue()

    def setPktDataString(self, txt):
        self.txt_pktData.SetValue(txt)

    def getPktData(self):
        dataStr = self.txt_pktData.GetValue()

        try:
            dataHex = binascii.unhexlify(dataStr)
            return dataHex
        except TypeError:
            print sys.exc_info()
            return None

    def clearPktData(self):
        self.txt_dataSize.SetValue('0')
        self.txt_pktData.Clear()

    def doSetStatusBar(self, txt, num):

        self.SetStatusText(txt, num)

    def doAlert(self, error):
        dlgStyle = wx.ICON_ERROR
        btnStyle = wx.OK

        dlg = GMD.GenericMessageDialog(self, error,
                                       "ERROR",
                                       btnStyle | dlgStyle)
        dlg.ShowModal()
        dlg.Destroy()

    def setDataSizeString(self, txt):
        self.txt_dataSize.SetValue(txt)

    def onPktSizeText(self, evt):
        if not self.getPktDataModeAuto():
            return

        sizeStr = self.txt_dataSize.GetValue()
        try:
            size = int(sizeStr)
            self.setPktDataString(genData(size))
        except ValueError:
            self.setPktDataString("data size error")
            return

    def onPktDataText(self, event):
        if self.getPktDataModeAuto():
            return
        self.index += 1

        data = self.getPktData()
        if data is None:
            self.setDataSizeString("Error")
        else:
            self.setDataSizeString(str(len(data)))

    def onClear(self, event):
        self.clearPktData()

    def getPktDataModeAuto(self):
        return self.cbx_autoGen.GetValue()

    def setPktDataModeAuto(self, auto):
        self.cbx_autoGen.SetValue(auto)
        if auto:
            self.txt_pktData.SetEditable(0)
            self.txt_dataSize.Enable()
            self.txt_dataSize.SetFocus()
        else:
            self.txt_pktData.SetEditable(1)
            self.txt_pktData.SetFocus()
            self.txt_dataSize.Disable()

    def onCheck(self, event):
        if event.GetEventObject().IsChecked():
            self.setPktDataModeAuto(1)
        else:
            self.setPktDataModeAuto(0)


if __name__ == "__main__":
    app = wx.App(0)
    frame = udpGenGui(None)
    frame.Show()
    app.MainLoop()