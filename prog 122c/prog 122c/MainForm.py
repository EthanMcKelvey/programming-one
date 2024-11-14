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
        self._listBox1.BackColor = System.Drawing.Color.FromArgb(192, 0, 192)
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 24
        self._listBox1.Location = System.Drawing.Point(8, 7)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(1007, 364)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(192, 0, 192)
        self._button1.ForeColor = System.Drawing.SystemColors.AppWorkspace
        self._button1.Location = System.Drawing.Point(30, 414)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(218, 84)
        self._button1.TabIndex = 1
        self._button1.Text = "button1"
        self._button1.UseVisualStyleBackColor = False
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(192, 0, 192)
        self._button2.ForeColor = System.Drawing.SystemColors.AppWorkspace
        self._button2.Location = System.Drawing.Point(393, 414)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(218, 84)
        self._button2.TabIndex = 2
        self._button2.Text = "button2"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(192, 0, 192)
        self._button3.ForeColor = System.Drawing.SystemColors.AppWorkspace
        self._button3.Location = System.Drawing.Point(754, 414)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(218, 84)
        self._button3.TabIndex = 3
        self._button3.Text = "button3"
        self._button3.UseVisualStyleBackColor = False
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(1028, 518)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "prog 122c"
        self.ResumeLayout(False)

