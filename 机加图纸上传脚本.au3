;ControlFocus("title","text",controlID) Edit1=Edit instance 1
ControlFocus("��", "","Edit1")

; Wait 10 seconds for the Upload window to appear
  WinWait("[CLASS:#32770]","",1)


; Set the File name text on the Edit field

  ControlSetText("��", "", "Edit1", "E:\Klory\01.Work\03.�ӽ�����ĵ�\�½��ļ���\19145-M1301-10-000A.PDF")

  Sleep(2000)

; Click on the Open button

  ControlClick("��", "","Button1");