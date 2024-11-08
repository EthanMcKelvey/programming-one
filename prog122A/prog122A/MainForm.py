import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._listBox1 = System.Windows.Forms.ListBox()
        self._textBox1 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(23, 370)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(204, 98)
        self._button1.TabIndex = 0
        self._button1.Text = "button1"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # listBox1
        # 
        self._listBox1.FormattingEnabled = True
        self._listBox1.Location = System.Drawing.Point(23, 61)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(956, 303)
        self._listBox1.TabIndex = 1
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(51, 8)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(328, 20)
        self._textBox1.TabIndex = 2
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(1004, 500)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "prog122A"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        num = int(self._textBox1.Text)
        
        
        
        num = int(self.listBox1.Text)