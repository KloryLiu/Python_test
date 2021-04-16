;ControlFocus("title","text",controlID) Edit1=Edit instance 1
ControlFocus("打开", "","Edit1")

; Wait 10 seconds for the Upload window to appear
  WinWait("[CLASS:#32770]","",1)


; Set the File name text on the Edit field

  ControlSetText("打开", "", "Edit1", "E:\Klory\01.Work\03.钣金测试文档\新建文件夹\19145-M1301-10-000A.PDF")

  Sleep(2000)

; Click on the Open button

  ControlClick("打开", "","Button1");