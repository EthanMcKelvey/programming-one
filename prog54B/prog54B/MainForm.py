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
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.IndianRed
        self._button1.Location = System.Drawing.Point(20, 13)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(153, 67)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.IndianRed
        self._button2.Location = System.Drawing.Point(192, 12)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(153, 67)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.IndianRed
        self._button3.Location = System.Drawing.Point(363, 13)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(153, 67)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(31, 109)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(241, 20)
        self._textBox1.TabIndex = 3
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(31, 224)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(241, 20)
        self._textBox2.TabIndex = 4
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(31, 185)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(241, 20)
        self._textBox3.TabIndex = 5
        # 
        # textBox4
        # 
        self._textBox4.Location = System.Drawing.Point(31, 149)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(241, 20)
        self._textBox4.TabIndex = 6
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.IndianRed
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(38, 268)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(255, 48)
        self._label1.TabIndex = 7
        self._label1.Text = "label1"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.IndianRed
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(38, 330)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(255, 48)
        self._label2.TabIndex = 8
        self._label2.Text = "label2"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Maroon
        self.ClientSize = System.Drawing.Size(539, 407)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "prog54B"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        a = int(self._textBox1.Text)
        b = int(self._textBox2.Text)
        c = int(self._textBox3.Text)
        d = int(self._textBox4.Text)
        s = a + b + c + d
        a = (a + b + c + d) //4
        self._label1.Text = str(a)
        self._label2.Text = str(s)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._textBox4.Text = ""
        self._label1.Text = ""
        self._label2.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()