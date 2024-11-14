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
        self._listBox1.BackColor = System.Drawing.SystemColors.InactiveBorder
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 24
        self._listBox1.Location = System.Drawing.Point(12, 12)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(909, 388)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.DodgerBlue
        self._button1.Location = System.Drawing.Point(12, 415)
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
        self._button2.Location = System.Drawing.Point(356, 415)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(245, 78)
        self._button2.TabIndex = 2
        self._button2.Text = "button2"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DodgerBlue
        self._button3.Location = System.Drawing.Point(676, 415)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(245, 78)
        self._button3.TabIndex = 3
        self._button3.Text = "button3"
        self._button3.UseVisualStyleBackColor = False
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Navy
        self.ClientSize = System.Drawing.Size(933, 505)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "prog122 i"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
       heading = "Number\t\tNegative Number\tCube Root\tNegative Cube Root\t\tCubed\t\tNegative Cubed"
       self._listBox1.Items.Add(heading)
       for num in range(1, 27-1):
            nnum = num * -1
            pcube = num**3
            pcbrt = num**(1.0/3.0)
            ncbrt = abs(pcbrt) * -1
            ncube = ((nnum**3) * -1) * -1
            line = str(round(nnum, 2)) + "\t\t" + str(round(num, 2)) + "\t\t" + str(round(ncbrt, 2)) + "\t\t" + str(round(pcbrt, 2)) + "\t\t\t" + str(round(ncube, 2)) + "\t\t" + str(round(pcube, 2))
            self._listBox1.Items.Add(line)
            