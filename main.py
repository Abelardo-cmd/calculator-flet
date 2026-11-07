import flet as ft
from dataclasses import field
from flet.controls import border_radius


@ft.control
class CalcButton(ft.Button):
     expand: int=1

@ft.control
class DigitButton(CalcButton):
     bgcolor: ft.Colors=ft.Colors.WHITE_24
     color: ft.Colors=ft.Colors.WHITE

@ft.control
class ActionButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.ORANGE
    color: ft.Colors = ft.Colors.WHITE

@ft.control
class ExtraActionButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.BLUE_GREY_100
    color: ft.Colors = ft.Colors.BLACK

@ft.control
class CalcApp(ft.Container):
    def init(self):
     self.result=ft.Text(value="0",color=ft.Colors.WHITE, size=20)
     self.width=350
     self.height=280
     self.bgcolor=ft.Colors.BLACK
     self.border_radius = ft.BorderRadius.all(20)
     self.padding = 20
     self.operand1=""
     self.operand2=""
     self.sinal=""
     self.content=ft.Column(
                  controls=[ft.Row(controls=[self.result],alignment=ft.MainAxisAlignment.END,),

                            ft.Row(controls=[ExtraActionButton(content="AC",on_click=self.HandlingButtons),
                                             ExtraActionButton(content="+/-",on_click=self.HandlingButtons),
                                             ExtraActionButton(content="%",on_click=self.HandlingButtons),
                                             ActionButton(content="/",on_click=self.HandlingButtons)]),

                            ft.Row(controls=[DigitButton(content="7",on_click=self.HandlingButtons),
                                             DigitButton(content="8",on_click=self.HandlingButtons),
                                             DigitButton(content="9",on_click=self.HandlingButtons),
                                             ActionButton(content="*",on_click=self.HandlingButtons)]),

                            ft.Row(controls=[DigitButton(content="4",on_click=self.HandlingButtons),
                                             DigitButton(content="5",on_click=self.HandlingButtons),
                                             DigitButton(content="6",on_click=self.HandlingButtons),
                                             ActionButton(content="-",on_click=self.HandlingButtons), ]),

                            ft.Row(controls=[DigitButton(content="1",on_click=self.HandlingButtons),
                                             DigitButton(content="2",on_click=self.HandlingButtons),
                                             DigitButton(content="3",on_click=self.HandlingButtons),
                                             ActionButton(content="+",on_click=self.HandlingButtons), ]),

                            ft.Row(controls=[DigitButton(content="0",expand=2,on_click=self.HandlingButtons),
                                             DigitButton(content=".",on_click=self.HandlingButtons),
                                             ActionButton(content="=",on_click=self.HandlingButtons), ]),
              ])
    def HandlingButtons(self,e):
        if e.control.content in ("1","2","3","4","5","6","7","8","9","0"):
            if(self.sinal==""):
             self.operand1 += e.control.content
             self.result.value = self.operand1
            else:
             self.operand2+=e.control.content
             self.result.value=self.operand2
        if e.control.content in ("*","+","-","/"):
            self.sinal=e.control.content
        if e.control.content == "=":
            if(self.sinal !="" and self.operand2!=""):
             self.result.value=eval(self.operand1+self.sinal+self.operand2)
             self.operand1=str(self.result.value)
             self.operand2=""
             self.sinal=""
        if e.control.content=="AC":
            self.operand1=""
            self.operand2=""
            self.sinal=""
            self.result.value="0"

        self.update()

def main(page:ft.Page):
    page.title = "Calc app"
    page.window.width = 370
    page.window.height = 350

    page.window.resizable = False

    page.window.min_width = 370
    page.window.min_height = 350
    page.window.max_width = 370
    page.window.max_height = 350

    page.window.maximized = False
    page.window.full_screen = False

    calc = CalcApp()
    page.add(calc)
    page.update()

if __name__ == "__main__":
  ft.run(main)