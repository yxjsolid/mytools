# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class udpGenGuiBase
###########################################################################

class udpGenGuiBase ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"UDP Gen", pos = wx.DefaultPosition, size = wx.Size( 522,429 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer26 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 4, 1, 0, 0 )
		fgSizer1.AddGrowableCol( 0 )
		fgSizer1.AddGrowableRow( 2 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.lbSrc = wx.StaticText( self.panel1, wx.ID_ANY, u"Src:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbSrc.Wrap( -1 )
		gbSizer1.Add( self.lbSrc, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txt_srcIp = wx.TextCtrl( self.panel1, wx.ID_ANY, u"192.168.168.1", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.txt_srcIp, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.lbPort = wx.StaticText( self.panel1, wx.ID_ANY, u"Port:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbPort.Wrap( -1 )
		gbSizer1.Add( self.lbPort, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txt_srcPort = wx.TextCtrl( self.panel1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.txt_srcPort, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self.panel1, wx.ID_ANY, u"Dst:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		gbSizer1.Add( self.m_staticText4, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txt_dstIp = wx.TextCtrl( self.panel1, wx.ID_ANY, u"192.168.168.168", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.txt_dstIp, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( self.panel1, wx.ID_ANY, u"Port:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		gbSizer1.Add( self.m_staticText5, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txt_dstPort = wx.TextCtrl( self.panel1, wx.ID_ANY, u"999", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.txt_dstPort, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self.panel1, wx.ID_ANY, u"packet num:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		gbSizer1.Add( self.m_staticText8, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txt_pktNum = wx.TextCtrl( self.panel1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.txt_pktNum, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self.panel1, wx.ID_ANY, u"interval(ms):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		gbSizer1.Add( self.m_staticText7, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txt_interval = wx.TextCtrl( self.panel1, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.txt_interval, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.lbTTL = wx.StaticText( self.panel1, wx.ID_ANY, u"TTL:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbTTL.Wrap( -1 )
		gbSizer1.Add( self.lbTTL, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txt_ttl = wx.TextCtrl( self.panel1, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.txt_ttl, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.btn_send = wx.Button( self.panel1, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.btn_send, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.btnStop = wx.Button( self.panel1, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.btnStop, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		self.panel1.SetSizer( gbSizer1 )
		self.panel1.Layout()
		gbSizer1.Fit( self.panel1 )
		fgSizer1.Add( self.panel1, 1, wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline1, 0, wx.EXPAND, 5 )
		
		self.m_panel33 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.DOUBLE_BORDER|wx.TAB_TRAVERSAL )
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel33, wx.ID_ANY, u"packet data" ), wx.VERTICAL )
		
		fgSizer11 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer11.AddGrowableCol( 0 )
		fgSizer11.AddGrowableRow( 1 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel14 = wx.Panel( self.m_panel33, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText66 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Data Size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText66.Wrap( -1 )
		bSizer16.Add( self.m_staticText66, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.txt_dataSize = wx.TextCtrl( self.m_panel14, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.txt_dataSize, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.cbx_autoGen = wx.CheckBox( self.m_panel14, wx.ID_ANY, u"auto Generate", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.cbx_autoGen, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button15 = wx.Button( self.m_panel14, wx.ID_ANY, u"clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button15, 0, wx.ALL, 5 )
		
		
		self.m_panel14.SetSizer( bSizer16 )
		self.m_panel14.Layout()
		bSizer16.Fit( self.m_panel14 )
		fgSizer11.Add( self.m_panel14, 1, wx.EXPAND, 5 )
		
		self.txt_pktData = wx.richtext.RichTextCtrl( self.m_panel33, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.HSCROLL|wx.VSCROLL|wx.WANTS_CHARS )
		fgSizer11.Add( self.txt_pktData, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		sbSizer2.Add( fgSizer11, 1, wx.EXPAND, 5 )
		
		
		self.m_panel33.SetSizer( sbSizer2 )
		self.m_panel33.Layout()
		sbSizer2.Fit( self.m_panel33 )
		fgSizer1.Add( self.m_panel33, 1, wx.EXPAND, 5 )
		
		
		bSizer26.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer26 )
		self.Layout()
		self.statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_send.Bind( wx.EVT_BUTTON, self.onSend )
		self.btnStop.Bind( wx.EVT_BUTTON, self.onStop )
		self.txt_dataSize.Bind( wx.EVT_TEXT, self.onPktSizeText )
		self.cbx_autoGen.Bind( wx.EVT_CHECKBOX, self.onCheck )
		self.m_button15.Bind( wx.EVT_BUTTON, self.onClear )
		self.txt_pktData.Bind( wx.EVT_TEXT, self.onPktDataText )
		self.txt_pktData.Bind( wx.EVT_TEXT_ENTER, self.onTextEnter )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onSend( self, event ):
		event.Skip()
	
	def onStop( self, event ):
		event.Skip()
	
	def onPktSizeText( self, event ):
		event.Skip()
	
	def onCheck( self, event ):
		event.Skip()
	
	def onClear( self, event ):
		event.Skip()
	
	def onPktDataText( self, event ):
		event.Skip()
	
	def onTextEnter( self, event ):
		event.Skip()
	

