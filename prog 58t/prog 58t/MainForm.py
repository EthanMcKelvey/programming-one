﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(392, 229)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(109, 66)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(14, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(139, 43)
        self._label1.TabIndex = 1
        self._label1.Text = "Price:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(14, 52)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(139, 43)
        self._label2.TabIndex = 2
        self._label2.Text = "Recived:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(310, 19)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(191, 59)
        self._label3.TabIndex = 3
        self._label3.Text = "Change Due"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 141)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(139, 35)
        self._label4.TabIndex = 4
        self._label4.Text = "Dollars:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(165, 19)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(119, 20)
        self._textBox1.TabIndex = 5
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(165, 70)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(119, 20)
        self._textBox2.TabIndex = 6
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(14, 188)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(139, 35)
        self._label5.TabIndex = 7
        self._label5.Text = "Quarters:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(12, 239)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(139, 35)
        self._label6.TabIndex = 8
        self._label6.Text = "Dimes:"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(12, 288)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(139, 35)
        self._label7.TabIndex = 9
        self._label7.Text = "Knickles:"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(392, 301)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(109, 66)
        self._button2.TabIndex = 10
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(392, 373)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(109, 66)
        self._button3.TabIndex = 11
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label8
        # 
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(12, 332)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(139, 35)
        self._label8.TabIndex = 12
        self._label8.Text = "Pennies:"
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label9
        # 
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(310, 104)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(191, 59)
        self._label9.TabIndex = 13
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label10
        # 
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(157, 141)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(183, 35)
        self._label10.TabIndex = 14
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label11
        # 
        self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(157, 188)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(183, 35)
        self._label11.TabIndex = 15
        self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label12
        # 
        self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(159, 239)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(183, 35)
        self._label12.TabIndex = 16
        self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label13
        # 
        self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.Location = System.Drawing.Point(157, 288)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(183, 35)
        self._label13.TabIndex = 17
        self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label14
        # 
        self._label14.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label14.Location = System.Drawing.Point(157, 332)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(183, 35)
        self._label14.TabIndex = 18
        self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.AppWorkspace
        self.ClientSize = System.Drawing.Size(513, 450)
        self.Controls.Add(self._label14)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "prog 58t"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        amountdue = float (self._textBox1.Text)
        amountgiven = float (self._textBox2.Text)
        changedue = amountgiven - amountdue
        self._label9.Text = str(changedue)
        dollarvalue = int(changedue)
        self._label10.Text = str(dollarvalue)
        decimalchange = changedue - dollarvalue
        quartervalue = float(decimalchange) // .25
        quarterliteralvalue = float(quartervalue) * .25
        rcaq = float(decimalchange) - float(quarterliteralvalue)
        self._label11.Text = str(quartervalue)
        dimevalue = float(rcaq) // .10
        self._label12.Text = str(dimevalue)
        dimeliteralvalue = float(dimevalue) * .10
        rcad = float(rcaq) - dimeliteralvalue
        nickelvalue = float(rcad) // .05
        self._label13.Text = str(nickelvalue)
        nickelliteralvalue = float(nickelvalue) * .05
        rcan = float(rcad) - nickelliteralvalue
        pennyvalue = float(rcan) // .01
        self._label14.Text = str(pennyvalue)
    
    def Button3Click(self, sender, e):
        Application.Exit()