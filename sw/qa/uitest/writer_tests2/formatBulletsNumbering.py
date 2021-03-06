# -*- tab-width: 4; indent-tabs-mode: nil; py-indent-offset: 4 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from uitest.framework import UITestCase
from libreoffice.uno.propertyvalue import mkPropertyValues
from uitest.uihelper.common import get_state_as_dict, type_text

import time
from uitest.debug import sleep
from libreoffice.uno.propertyvalue import mkPropertyValues
from uitest.uihelper.common import select_pos

class formatBulletsNumbering(UITestCase):

   def test_bullets_and_numbering_dialog_tab_position(self):
        self.ui_test.create_doc_in_start_center("writer")
        document = self.ui_test.get_component()
        xWriterDoc = self.xUITest.getTopFocusWindow()

        self.ui_test.execute_dialog_through_command(".uno:OptionsTreeDialog")  #optionsdialog
        xDialog = self.xUITest.getTopFocusWindow()
        xPages = xDialog.getChild("pages")
        xWriterEntry = xPages.getChild('3')                 # Writer
        xWriterEntry.executeAction("EXPAND", tuple())
        xWriterGeneralEntry = xWriterEntry.getChild('0')
        xWriterGeneralEntry.executeAction("SELECT", tuple())          #General - set millimeters
        xMetric = xDialog.getChild("metric")
        props = {"TEXT": "Millimeter"}
        actionProps = mkPropertyValues(props)
        xMetric.executeAction("SELECT", actionProps)
        xOKBtn = xDialog.getChild("ok")
        self.ui_test.close_dialog_through_button(xOKBtn)

        self.ui_test.execute_dialog_through_command(".uno:BulletsAndNumberingDialog")
        xDialog = self.xUITest.getTopFocusWindow()
        xTabs = xDialog.getChild("tabcontrol")
        select_pos(xTabs, "4")
        xalignedatmf = xDialog.getChild("alignedatmf")
        xnum2alignlb = xDialog.getChild("num2alignlb")
        xatmf = xDialog.getChild("atmf")
        xindentatmf = xDialog.getChild("indentatmf")
        xokbtn = xDialog.getChild("ok")

        xalignedatmf.executeAction("UP", tuple())
        props = {"TEXT": "Centered"}
        actionProps = mkPropertyValues(props)
        xnum2alignlb.executeAction("SELECT", actionProps)
        xatmf.executeAction("UP", tuple())
        xindentatmf.executeAction("UP", tuple())

        self.ui_test.close_dialog_through_button(xokbtn)

        self.ui_test.execute_dialog_through_command(".uno:BulletsAndNumberingDialog")
        xDialog = self.xUITest.getTopFocusWindow()
        xTabs = xDialog.getChild("tabcontrol")
        select_pos(xTabs, "4")
        xalignedatmf = xDialog.getChild("alignedatmf")
        xnum2alignlb = xDialog.getChild("num2alignlb")
        xatmf = xDialog.getChild("atmf")
        xindentatmf = xDialog.getChild("indentatmf")

        self.assertEqual(get_state_as_dict(xalignedatmf)["Text"], "6.5 mm")
        self.assertEqual(get_state_as_dict(xnum2alignlb)["SelectEntryText"], "Centered")
        self.assertEqual(get_state_as_dict(xatmf)["Text"], "12.8 mm")
        self.assertEqual(get_state_as_dict(xindentatmf)["Text"], "12.8 mm")

        xcancbtn = xDialog.getChild("cancel")
        self.ui_test.close_dialog_through_button(xcancbtn)

        self.ui_test.close_doc()

   def test_bullets_and_numbering_dialog_tab_position2(self):
        self.ui_test.create_doc_in_start_center("writer")
        document = self.ui_test.get_component()
        xWriterDoc = self.xUITest.getTopFocusWindow()

        self.ui_test.execute_dialog_through_command(".uno:BulletsAndNumberingDialog")
        xDialog = self.xUITest.getTopFocusWindow()
        xTabs = xDialog.getChild("tabcontrol")
        select_pos(xTabs, "4")
        xnumfollowedbylb = xDialog.getChild("numfollowedbylb")
        props = {"TEXT": "Space"}
        actionProps = mkPropertyValues(props)
        xnumfollowedbylb.executeAction("SELECT", actionProps)

        xokbtn = xDialog.getChild("ok")
        self.ui_test.close_dialog_through_button(xokbtn)

        self.ui_test.execute_dialog_through_command(".uno:BulletsAndNumberingDialog")
        xDialog = self.xUITest.getTopFocusWindow()
        xTabs = xDialog.getChild("tabcontrol")
        select_pos(xTabs, "4")
        xnumfollowedbylb = xDialog.getChild("numfollowedbylb")
        self.assertEqual(get_state_as_dict(xnumfollowedbylb)["SelectEntryText"], "Space")

        xcancbtn = xDialog.getChild("cancel")
        self.ui_test.close_dialog_through_button(xcancbtn)

        self.ui_test.close_doc()

   def test_bullets_and_numbering_dialog_tab_customize(self):
        self.ui_test.create_doc_in_start_center("writer")
        document = self.ui_test.get_component()
        xWriterDoc = self.xUITest.getTopFocusWindow()

        self.ui_test.execute_dialog_through_command(".uno:BulletsAndNumberingDialog")
        xDialog = self.xUITest.getTopFocusWindow()
        xTabs = xDialog.getChild("tabcontrol")
        select_pos(xTabs, "5")
        xnumfmtlb = xDialog.getChild("numfmtlb")
        xstartat = xDialog.getChild("startat")
        xcharstyle = xDialog.getChild("charstyle")
        xprefix = xDialog.getChild("prefix")
        xsuffix = xDialog.getChild("suffix")
        xallsame = xDialog.getChild("allsame")

        props = {"TEXT": "A, B, C, ..."}
        actionProps = mkPropertyValues(props)
        xnumfmtlb.executeAction("SELECT", actionProps)
        xstartat.executeAction("UP", tuple())
        props2 = {"TEXT": "Bullets"}
        actionProps2 = mkPropertyValues(props2)
        xcharstyle.executeAction("SELECT", actionProps2)
        xprefix.executeAction("TYPE", mkPropertyValues({"TEXT":"o"}))
        xsuffix.executeAction("TYPE", mkPropertyValues({"KEYCODE":"CTRL+A"}))
        xsuffix.executeAction("TYPE", mkPropertyValues({"TEXT":"a"}))
        xallsame.executeAction("CLICK", tuple())

        xokbtn = xDialog.getChild("ok")
        self.ui_test.close_dialog_through_button(xokbtn)

        self.ui_test.execute_dialog_through_command(".uno:BulletsAndNumberingDialog")
        xDialog = self.xUITest.getTopFocusWindow()
        xTabs = xDialog.getChild("tabcontrol")
        select_pos(xTabs, "5")
        xnumfmtlb = xDialog.getChild("numfmtlb")
        xstartat = xDialog.getChild("startat")
        xcharstyle = xDialog.getChild("charstyle")
        xprefix = xDialog.getChild("prefix")
        xsuffix = xDialog.getChild("suffix")
        xallsame = xDialog.getChild("allsame")

        self.assertEqual(get_state_as_dict(xnumfmtlb)["SelectEntryText"], "A, B, C, ...")
        self.assertEqual(get_state_as_dict(xstartat)["Text"], "2")
        self.assertEqual(get_state_as_dict(xcharstyle)["SelectEntryText"], "Bullets")
        self.assertEqual(get_state_as_dict(xprefix)["Text"], "o")
        self.assertEqual(get_state_as_dict(xsuffix)["Text"], "a")
        self.assertEqual(get_state_as_dict(xallsame)["Selected"], "true")

        xcancbtn = xDialog.getChild("cancel")
        self.ui_test.close_dialog_through_button(xcancbtn)

        self.ui_test.execute_dialog_through_command(".uno:BulletsAndNumberingDialog")
        xDialog = self.xUITest.getTopFocusWindow()
        xTabs = xDialog.getChild("tabcontrol")
        select_pos(xTabs, "5")

        xremovebtn = xDialog.getChild("user")
        self.ui_test.close_dialog_through_button(xremovebtn)  #remove new settings, back to default

        self.ui_test.execute_dialog_through_command(".uno:BulletsAndNumberingDialog")
        xDialog = self.xUITest.getTopFocusWindow()
        xTabs = xDialog.getChild("tabcontrol")
        select_pos(xTabs, "5")
        xnumfmtlb = xDialog.getChild("numfmtlb")
        xstartat = xDialog.getChild("startat")
        xcharstyle = xDialog.getChild("charstyle")
        xprefix = xDialog.getChild("prefix")
        xsuffix = xDialog.getChild("suffix")
        xallsame = xDialog.getChild("allsame")

        self.assertEqual(get_state_as_dict(xnumfmtlb)["SelectEntryText"], "1, 2, 3, ...")
        self.assertEqual(get_state_as_dict(xstartat)["Text"], "1")
        self.assertEqual(get_state_as_dict(xcharstyle)["SelectEntryText"], "None")
        self.assertEqual(get_state_as_dict(xprefix)["Text"], "")
        self.assertEqual(get_state_as_dict(xsuffix)["Text"], ".")
        self.assertEqual(get_state_as_dict(xallsame)["Selected"], "false")

        xcancbtn = xDialog.getChild("cancel")
        self.ui_test.close_dialog_through_button(xcancbtn)

        self.ui_test.close_doc()

   def test_bullets_and_numbering_tab_move(self):
        self.ui_test.create_doc_in_start_center("writer")
        document = self.ui_test.get_component()
        xWriterDoc = self.xUITest.getTopFocusWindow()
        xWriterEdit = xWriterDoc.getChild("writer_edit")

        self.ui_test.execute_dialog_through_command(".uno:OptionsTreeDialog")  #optionsdialog
        xDialog = self.xUITest.getTopFocusWindow()
        xPages = xDialog.getChild("pages")
        xWriterEntry = xPages.getChild('3')                 # Writer
        xWriterEntry.executeAction("EXPAND", tuple())
        xWriterGeneralEntry = xWriterEntry.getChild('0')
        xWriterGeneralEntry.executeAction("SELECT", tuple())          #General - set millimeters
        xMetric = xDialog.getChild("metric")
        props = {"TEXT": "Millimeter"}
        actionProps = mkPropertyValues(props)
        xMetric.executeAction("SELECT", actionProps)
        xOKBtn = xDialog.getChild("ok")
        self.ui_test.close_dialog_through_button(xOKBtn)

        self.ui_test.execute_dialog_through_command(".uno:BulletsAndNumberingDialog")
        xDialog = self.xUITest.getTopFocusWindow()
        xTabs = xDialog.getChild("tabcontrol")
        select_pos(xTabs, "4")
        xindentatmf = xDialog.getChild("indentatmf")
        indentValue = get_state_as_dict(xindentatmf)["Text"][0:len(get_state_as_dict(xindentatmf)["Text"])-3]

        xokbtn = xDialog.getChild("ok")
        self.ui_test.close_dialog_through_button(xokbtn)  #create bullets

        xWriterEdit.executeAction("TYPE", mkPropertyValues({"KEYCODE": "TAB"})) #TAB to move indent right
        self.ui_test.execute_dialog_through_command(".uno:BulletsAndNumberingDialog")
        xDialog = self.xUITest.getTopFocusWindow()
        xTabs = xDialog.getChild("tabcontrol")
        select_pos(xTabs, "4")
        xindentatmf = xDialog.getChild("indentatmf")
        indentValue2 = get_state_as_dict(xindentatmf)["Text"][0:len(get_state_as_dict(xindentatmf)["Text"])-3]
        self.assertEqual(indentValue < indentValue2 , True)
        xcancbtn = xDialog.getChild("cancel")
        self.ui_test.close_dialog_through_button(xcancbtn)

        xWriterEdit.executeAction("TYPE", mkPropertyValues({"KEYCODE": "BACKSPACE"}))
        self.ui_test.execute_dialog_through_command(".uno:BulletsAndNumberingDialog")
        xDialog = self.xUITest.getTopFocusWindow()
        xTabs = xDialog.getChild("tabcontrol")
        select_pos(xTabs, "4")
        xindentatmf = xDialog.getChild("indentatmf")
        indentValue3 = get_state_as_dict(xindentatmf)["Text"][0:len(get_state_as_dict(xindentatmf)["Text"])-3]
        self.assertEqual(indentValue == indentValue3 , True)
        xcancbtn = xDialog.getChild("cancel")
        self.ui_test.close_dialog_through_button(xcancbtn)

        self.ui_test.close_doc()

   def test_bullets_and_numbering_button_move(self):
        self.ui_test.create_doc_in_start_center("writer")
        document = self.ui_test.get_component()
        xWriterDoc = self.xUITest.getTopFocusWindow()

        self.ui_test.execute_dialog_through_command(".uno:OptionsTreeDialog")  #optionsdialog
        xDialog = self.xUITest.getTopFocusWindow()
        xPages = xDialog.getChild("pages")
        xWriterEntry = xPages.getChild('3')                 # Writer
        xWriterEntry.executeAction("EXPAND", tuple())
        xWriterGeneralEntry = xWriterEntry.getChild('0')
        xWriterGeneralEntry.executeAction("SELECT", tuple())          #General - set millimeters
        xMetric = xDialog.getChild("metric")
        props = {"TEXT": "Millimeter"}
        actionProps = mkPropertyValues(props)
        xMetric.executeAction("SELECT", actionProps)
        xOKBtn = xDialog.getChild("ok")
        self.ui_test.close_dialog_through_button(xOKBtn)

        self.ui_test.execute_dialog_through_command(".uno:BulletsAndNumberingDialog")
        xDialog = self.xUITest.getTopFocusWindow()
        xTabs = xDialog.getChild("tabcontrol")
        select_pos(xTabs, "4")
        xindentatmf = xDialog.getChild("indentatmf")
        indentValue = get_state_as_dict(xindentatmf)["Text"][0:len(get_state_as_dict(xindentatmf)["Text"])-3]

        xokbtn = xDialog.getChild("ok")
        self.ui_test.close_dialog_through_button(xokbtn)  #create bullets

        self.xUITest.executeCommand(".uno:DecrementSubLevels")
        self.ui_test.execute_dialog_through_command(".uno:BulletsAndNumberingDialog")
        xDialog = self.xUITest.getTopFocusWindow()
        xTabs = xDialog.getChild("tabcontrol")
        select_pos(xTabs, "4")
        xindentatmf = xDialog.getChild("indentatmf")
        indentValue2 = get_state_as_dict(xindentatmf)["Text"][0:len(get_state_as_dict(xindentatmf)["Text"])-3]
        self.assertEqual(indentValue < indentValue2 , True)
        xcancbtn = xDialog.getChild("cancel")
        self.ui_test.close_dialog_through_button(xcancbtn)

        self.xUITest.executeCommand(".uno:IncrementLevel")
        self.ui_test.execute_dialog_through_command(".uno:BulletsAndNumberingDialog")
        xDialog = self.xUITest.getTopFocusWindow()
        xTabs = xDialog.getChild("tabcontrol")
        select_pos(xTabs, "4")
        xindentatmf = xDialog.getChild("indentatmf")
        indentValue3 = get_state_as_dict(xindentatmf)["Text"][0:len(get_state_as_dict(xindentatmf)["Text"])-3]
        self.assertEqual(indentValue == indentValue3 , True)
        xcancbtn = xDialog.getChild("cancel")
        self.ui_test.close_dialog_through_button(xcancbtn)

        self.ui_test.close_doc()
# vim: set shiftwidth=4 softtabstop=4 expandtab:
