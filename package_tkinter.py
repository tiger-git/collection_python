"""
tkinter学习:左右自增1
"""
import tkinter


class TkAdd(object):
    def __init__(self, tk):
        self.tk = tk

    def tk_set(self, name, size, back_color, *args, **kwargs):
        self.tk.title(name)
        self.tk.geometry(size)
        self.tk['bg'] = back_color
        self.tk.attributes('-alpha', 0.1)

    def get_label(self, *args, **kwargs):
        # 标签
        label1 = tkinter.Label(tk, text='add', width=20, height=1)
        label1.grid(row=0, column=0)

        label2 = tkinter.Label(tk, text='sum', width=20, height=1)
        label2.grid(row=0, column=500)
        return

    def get_text(self, *args, **kwargs):
        # 文本框
        text1 = tkinter.Text(tk, width=10, height=2)
        text1.grid(row=2, column=0, rowspan=500, columnspan=10)

        text2 = tkinter.Text(tk, width=10, height=2)
        text2.grid(row=2, column=500, rowspan=500, columnspan=10)
        self.text_add = text1
        self.text_sum = text2
        return

    def get_button(self, *args, **kwargs):
        # 按钮
        button = tkinter.Button(tk, text='自增测试', bg='red', width=10, height=2, command=self.select_func)
        button.grid(row=2, column=100)

    def handle_int(self, obj):
        try:
            return int(obj)
        except Exception as e:
            return 0

    def select_func(self):
        value_add = self.text_add.get(0.0, 'end')
        value_sum = self.text_sum.get(0.0, 'end')
        value_add = self.handle_int(value_add)
        value_sum = self.handle_int(value_sum)
        if value_add >= value_sum:
            self.add_select('add')
        else:
            self.add_select('sum')

    def add_select(self, select='add'):
        if select is 'add':
            value = self.text_add.get(0.0, 'end')
            value = self.handle_int(value)
            self.text_sum.delete(0.0, 'end')
            self.text_sum.insert(0.0, value + 1)
        else:
            value = self.text_sum.get(0.0, 'end')
            value = self.handle_int(value)
            self.text_add.delete(0.0, 'end')
            self.text_add.insert(0.0, value + 1)
        return

    def run(self):
        self.get_label()
        self.get_text()
        self.get_button()
        self.flag = True
        return


if __name__ == '__main__':
    tk = tkinter.Tk()
    handle = TkAdd(tk)
    handle.tk_set('自增测试', '500x200+512+512', 'pink')
    handle.run()
    tk.mainloop()
