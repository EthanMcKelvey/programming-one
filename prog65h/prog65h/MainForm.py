import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(214, 97)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(309, 20)
        self._textBox1.TabIndex = 0
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.Highlight
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(120, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(337, 78)
        self._label1.TabIndex = 1
        self._label1.Text = "British conversion"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.Highlight
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(30, 97)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(143, 34)
        self._label2.TabIndex = 2
        self._label2.Text = """Pound
"""
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.Highlight
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(30, 150)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(143, 34)
        self._label3.TabIndex = 3
        self._label3.Text = "Shilling"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(214, 164)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(309, 20)
        self._textBox2.TabIndex = 4
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(214, 212)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(309, 20)
        self._textBox3.TabIndex = 5
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(30, 349)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(139, 84)
        self._button1.TabIndex = 6
        self._button1.Text = "button1"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(228, 349)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(139, 84)
        self._button2.TabIndex = 7
        self._button2.Text = "button2"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(405, 349)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(139, 84)
        self._button3.TabIndex = 8
        self._button3.Text = "button3"
        self._button3.UseVisualStyleBackColor = True
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.Highlight
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(30, 198)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(143, 34)
        self._label4.TabIndex = 9
        self._label4.Text = "Pence"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.Highlight
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(12, 251)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(181, 68)
        self._label5.TabIndex = 10
        self._label5.Text = "Modern Notation"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.Highlight
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(237, 246)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(256, 78)
        self._label6.TabIndex = 11
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Purple
        self.ClientSize = System.Drawing.Size(566, 468)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "prog65h"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):

        lbs = float(self._textBox1.Text)
        shil = float(self._textBox2.Text)
        pence = float(self._textBox3.Text)
   
        newpence = (float(shil) * 5) * .01
        oldpence = (float(pence) * 8.33333333333) * .0001
     
        prenewnotation = float(lbs) + float(newpence) + float(oldpence)
        newnotation = round(prenewnotation, 2)
        self._label6.Text = str(newnotation)
