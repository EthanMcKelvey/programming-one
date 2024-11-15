import System.Drawing
import System.Windows.Forms
import math
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
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 29
        self._listBox1.Location = System.Drawing.Point(12, 12)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(1048, 294)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(12, 389)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(293, 107)
        self._button1.TabIndex = 1
        self._button1.Text = "button1"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(326, 389)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(293, 107)
        self._button2.TabIndex = 2
        self._button2.Text = "button2"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(668, 389)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(293, 107)
        self._button3.TabIndex = 3
        self._button3.Text = "button3"
        self._button3.UseVisualStyleBackColor = True
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(1123, 529)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "prog122 H"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        heading = "Number\t\tSquare\t\tSquare Root\t/tCube\t\t4th Root"
        self._listBox1.Items.Add(heading)
        for num in range(1, 20 +1):
            nsqrd = num**2
            nsqrt = math.sqrt(num)
            cube = num**3
            line = str(num) + "\t\t" + str(nsqrd) + \
                              "\t\t" + str(round(nsqrt,4)) + \
                              "\t\t" + str(round(cube)) + \
                              "\t\t" + str(round(nsqrt, 6))
            self._listBox1.Items.Add(line)