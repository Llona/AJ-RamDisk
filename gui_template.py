# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class main_frame
###########################################################################

class main_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"AJ-RamDisk", pos = wx.DefaultPosition, size = wx.Size( 835,601 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"label" ), wx.VERTICAL )

		self.ramdrive_listCtrl = wx.ListCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_VRULES )
		sbSizer8.Add( self.ramdrive_listCtrl, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer30.Add( sbSizer8, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )

		self.add_button = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.add_button, 0, wx.ALL, 5 )

		self.edit_button = wx.Button( self, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.edit_button, 0, wx.ALL, 5 )

		self.delete_button = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.delete_button, 0, wx.ALL, 5 )


		bSizer30.Add( bSizer33, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer30.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer30 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.add_button.Bind( wx.EVT_BUTTON, self.add_press )
		self.edit_button.Bind( wx.EVT_BUTTON, self.edit_press )
		self.delete_button.Bind( wx.EVT_BUTTON, self.del_press )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def add_press( self, event ):
		event.Skip()

	def edit_press( self, event ):
		event.Skip()

	def del_press( self, event ):
		event.Skip()


###########################################################################
## Class AddEditDiskFrame
###########################################################################

class AddEditDiskFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Editor Ram Disk", pos = wx.DefaultPosition, size = wx.Size( 537,425 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer34 = wx.BoxSizer( wx.VERTICAL )

		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Config" ), wx.VERTICAL )

		bSizer35 = wx.BoxSizer( wx.VERTICAL )

		bSizer36 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText17 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		bSizer36.Add( self.m_staticText17, 0, wx.LEFT|wx.RIGHT|wx.TOP, 7 )

		self.m_textCtrl11 = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		bSizer36.Add( self.m_textCtrl11, 0, wx.ALL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

		m_choice6Choices = [ u"MB", u"GB" ]
		self.m_choice6 = wx.Choice( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice6Choices, 0 )
		self.m_choice6.SetSelection( 1 )
		bSizer36.Add( self.m_choice6, 0, wx.ALL, 5 )


		bSizer35.Add( bSizer36, 0, wx.EXPAND, 5 )

		bSizer37 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText18 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Drive:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		bSizer37.Add( self.m_staticText18, 0, wx.LEFT|wx.RIGHT|wx.TOP, 7 )

		m_choice7Choices = []
		self.m_choice7 = wx.Choice( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice7Choices, 0 )
		self.m_choice7.SetSelection( 0 )
		bSizer37.Add( self.m_choice7, 0, wx.ALL, 5 )


		bSizer35.Add( bSizer37, 0, wx.EXPAND, 5 )

		bSizer371 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText181 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Label:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText181.Wrap( -1 )

		bSizer371.Add( self.m_staticText181, 0, wx.LEFT|wx.RIGHT|wx.TOP, 7 )

		self.m_textCtrl12 = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, u"RamDisk", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer371.Add( self.m_textCtrl12, 0, wx.ALL, 5 )


		bSizer35.Add( bSizer371, 0, wx.EXPAND, 5 )

		bSizer3711 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBox3 = wx.CheckBox( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Store to HDD?", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3711.Add( self.m_checkBox3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


		bSizer35.Add( bSizer3711, 1, wx.EXPAND, 5 )

		self.m_staticline8 = wx.StaticLine( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer35.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer37111 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBox31 = wx.CheckBox( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Store All?", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer37111.Add( self.m_checkBox31, 0, wx.ALIGN_CENTER|wx.LEFT, 5 )

		self.m_button23 = wx.Button( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Choise Folder", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer37111.Add( self.m_button23, 0, wx.ALL, 5 )


		bSizer35.Add( bSizer37111, 0, wx.EXPAND, 5 )

		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText27 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Patch:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		bSizer61.Add( self.m_staticText27, 0, wx.LEFT|wx.RIGHT|wx.TOP, 5 )

		self.m_textCtrl19 = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer61.Add( self.m_textCtrl19, 1, wx.ALL, 5 )

		self.m_button30 = wx.Button( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Path", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer61.Add( self.m_button30, 0, wx.ALL, 5 )


		bSizer35.Add( bSizer61, 0, wx.EXPAND, 5 )


		sbSizer9.Add( bSizer35, 1, wx.EXPAND, 5 )


		bSizer34.Add( sbSizer9, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline7 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer34.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer42 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button20 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer42.Add( self.m_button20, 0, wx.ALL, 5 )

		self.m_button22 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer42.Add( self.m_button22, 0, wx.ALL, 5 )


		bSizer34.Add( bSizer42, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer34 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class SelectFolderFrame
###########################################################################

class SelectFolderFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 618,640 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer54 = wx.BoxSizer( wx.VERTICAL )

		bSizer55 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer57 = wx.BoxSizer( wx.VERTICAL )

		self.m_treeCtrl1 = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		bSizer57.Add( self.m_treeCtrl1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer55.Add( bSizer57, 1, wx.EXPAND, 5 )

		bSizer58 = wx.BoxSizer( wx.VERTICAL )

		self.m_button27 = wx.Button( self, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer58.Add( self.m_button27, 0, wx.ALL, 5 )

		self.m_button28 = wx.Button( self, wx.ID_ANY, u"<-", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer58.Add( self.m_button28, 0, wx.ALL, 5 )


		bSizer55.Add( bSizer58, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer59 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl18 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer59.Add( self.m_textCtrl18, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer55.Add( bSizer59, 1, wx.EXPAND, 5 )


		bSizer54.Add( bSizer55, 1, wx.EXPAND, 5 )

		bSizer56 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline9 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer56.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer60 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button24 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer60.Add( self.m_button24, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_button29 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer60.Add( self.m_button29, 0, wx.ALL, 5 )


		bSizer56.Add( bSizer60, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer54.Add( bSizer56, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer54 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


