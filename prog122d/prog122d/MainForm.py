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
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 39
        self._listBox1.Location = System.Drawing.Point(23, 12)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(899, 277)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(23, 352)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(275, 120)
        self._button1.TabIndex = 1
        self._button1.Text = "button1"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(340, 352)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(275, 120)
        self._button2.TabIndex = 2
        self._button2.Text = "button2"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(647, 352)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(275, 120)
        self._button3.TabIndex = 3
        self._button3.Text = "button3"
        self._button3.UseVisualStyleBackColor = True
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(985, 496)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "prog122d"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        heading = "x\t\ty"
        self._listBox1.Items.Add(heading)
        for num in range(-12, 16 + 1):
            x = int(num)
            y = (x ** 6) - ((3 * x) ** 5) - ((93 * x) ** 4) + ((87 * x) ** 3) + ((1956 * x) ** 2) - (1380 * x) - 2800
            line = str(x) + "\t\t" + str(y) 
        
            self._listBox1.Items.Add(line)   