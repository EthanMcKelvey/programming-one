import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.SystemColors.InactiveBorder
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 33
        self._listBox1.Location = System.Drawing.Point(12, 46)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(1025, 301)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.DodgerBlue
        self._button1.Location = System.Drawing.Point(41, 401)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(245, 78)
        self._button1.TabIndex = 1
        self._button1.Text = "button1"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.DodgerBlue
        self._button2.Location = System.Drawing.Point(388, 401)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(245, 78)
        self._button2.TabIndex = 2
        self._button2.Text = "button2"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DodgerBlue
        self._button3.Location = System.Drawing.Point(727, 401)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(245, 78)
        self._button3.TabIndex = 3
        self._button3.Text = "button3"
        self._button3.UseVisualStyleBackColor = False
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(29, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(216, 20)
        self._textBox1.TabIndex = 4
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Navy
        self.ClientSize = System.Drawing.Size(1049, 505)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "prog122 i"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        endpont = int(self._textBox1.Text)
        num = 2
        num2 = 2
        for even in range(0, ):
            line = (num) = "t\t" + str(num2)
            