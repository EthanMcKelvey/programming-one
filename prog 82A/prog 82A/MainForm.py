import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(312, 36)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(214, 20)
        self._textBox1.TabIndex = 0
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(312, 95)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(214, 20)
        self._textBox2.TabIndex = 1
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(72, 310)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(178, 71)
        self._button1.TabIndex = 2
        self._button1.Text = "button1"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(347, 305)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(203, 81)
        self._button2.TabIndex = 3
        self._button2.Text = "button2"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(607, 312)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(198, 74)
        self._button3.TabIndex = 4
        self._button3.Text = "button3"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(80, 12)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(226, 54)
        self._label1.TabIndex = 5
        self._label1.Text = "Speed Limit:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(80, 71)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(226, 54)
        self._label2.TabIndex = 6
        self._label2.Text = "Vechicle Speed:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Transparent
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(312, 169)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(197, 54)
        self._label3.TabIndex = 7
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(80, 169)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(226, 54)
        self._label4.TabIndex = 8
        self._label4.Text = "Fine Amount:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(856, 450)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "prog 82A"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
         # Speed Limit
        sl = int(self._textBox1.Text)
        # Vehicle Speed
        vs = int(self._textBox2.Text)
        # Number of miles over speed limit
        mosl = vs - sl
        # Calculating money for fine
        prefine = int(mosl) * 5
        fine = int(prefine) + 20
        # Printing
        self._label3.Text = "$" + str(fine)

    def Button2Click(self, sender, e):
        self._label3.Text = ""
        self._textBox2.Text = ""
        self._textBox1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()