import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._listBox1 = System.Windows.Forms.ListBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(43, 340)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(131, 58)
        self._button1.TabIndex = 0
        self._button1.Text = "button1"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(315, 340)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(131, 58)
        self._button2.TabIndex = 1
        self._button2.Text = "button2"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(576, 340)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(131, 58)
        self._button3.TabIndex = 2
        self._button3.Text = "button3"
        self._button3.UseVisualStyleBackColor = True
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(90, 46)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(565, 20)
        self._textBox1.TabIndex = 3
        # 
        # listBox1
        # 
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 33
        self._listBox1.Location = System.Drawing.Point(77, 83)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(547, 202)
        self._listBox1.TabIndex = 4
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(758, 410)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "prog152b"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        num = self.textBox1.text
        for even in range(0, int(num)):
            line = str(even) + "\t\t" + int(str(num)/2)