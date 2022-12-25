from tkinter import Tk, Button, Label, Entry, LabelFrame, Spinbox, Frame

class root(Tk):
    def __init__(self):
        super().__init__()
        self.background_color = '#eeeeee'
        self.font_color = 'black'
        self.hex_result = '0x000000'
        self.number_result = 0
        Label(self, text='MicroInstruction Maker', background=self.background_color, foreground=self.font_color, font='Arial 15').place(x=320, y=10)

        self.config_frame = LabelFrame(self, text='Configuration')
        self.config_frame.place(x=5, y=35, width=810, height=90)

        Label(self.config_frame, text='Number of Buttons:', background=self.background_color, foreground=self.font_color, font='Arial 10').place(x=5, y=10)
        self.Spin_NumberOfButtons = Spinbox(self.config_frame, from_=0, to=37)
        self.Spin_NumberOfButtons.place(x=130, y=10)
        self.Button_GenerateButtons = Button(self.config_frame, text='Generate')
        self.Button_GenerateButtons.place(x=743, y=40)
        self.Button_GenerateButtons.bind('<Button-1>', self.generateButtons)

        self.workspace_frame = LabelFrame(self, text='WorkSpace')
        self.workspace_frame.place(x=5, y=127, width=810, height=150)
        self.workspace_frame_ButtonsFrame = Frame(self.workspace_frame)
        self.workspace_frame_ButtonsFrame.pack(expand='true')
        self.LabelResult = Entry(self.workspace_frame, background=self.background_color, foreground=self.font_color, font='Arial 10 bold')
        self.LabelResult.place(x=5, y=10)
        self.LabelResult.insert(0, '0x00000000')

    def generateButtons(self, event):
        self.index_ButtonsDict = {}
        self.number_result = 0
        self.workspace_frame_ButtonsFrame.destroy()
        self.workspace_frame_ButtonsFrame = Frame(self.workspace_frame)
        self.workspace_frame_ButtonsFrame.pack(expand='true')
        for i in range(int(self.Spin_NumberOfButtons.get())):
            self.index_ButtonsDict[i] = Button(self.workspace_frame_ButtonsFrame, background='#aaaaaa', text=f'{i}')
            self.index_ButtonsDict[i].grid(column=100-i, row=0)
            self.index_ButtonsDict[i].bind('<Button-1>', self.changeButtonState)
    
    def changeButtonState(self, event):
        buttonText = event.widget.cget('text')
        if buttonText.isdigit():
            event.widget['background'] = '#00ff00'
            if int(event.widget['text']) == 0:
                self.number_result += 1
            else:
                self.number_result += 2 ** int(event.widget['text'])
            event.widget['text'] = buttonText + '.'
        else:
            event.widget['background'] = '#aaaaaa'
            event.widget['text'] = buttonText[:-1]
            if int(event.widget['text']) == 0:
                self.number_result -= 1
            else:
                self.number_result -= 2 ** int(event.widget['text'])
        print(bin(self.number_result), self.number_result, hex(self.number_result))
        self.LabelResult.delete(0, 100)
        self.hex_result = str(hex(self.number_result))[2:]
        self.hex_result = '0x' + self.hex_result.rjust(9, '0')
        self.LabelResult.insert(0, self.hex_result)
    def generateNumber(self, number):
        pass

if __name__=='__main__':
    aplication = root()
    aplication.config(background=aplication.background_color)
    aplication.geometry(f'820x300+400+10')
    aplication.minsize(820, 300)
    aplication.maxsize(820, 300)
    aplication.mainloop()