﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._comboBox1 = System.Windows.Forms.ComboBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(8, 19)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(184, 55)
        self._label1.TabIndex = 0
        self._label1.Text = "pick a car:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.DimGray
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(8, 237)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(184, 55)
        self._label2.TabIndex = 1
        self._label2.Text = "Miles:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.DimGray
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(8, 304)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(184, 55)
        self._label3.TabIndex = 2
        self._label3.Text = "Gallons"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.DimGray
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(8, 375)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(184, 55)
        self._label4.TabIndex = 3
        self._label4.Text = "MPG:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.DimGray
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(243, 252)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(226, 40)
        self._label5.TabIndex = 4
        self._label5.Text = "label5"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.DimGray
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(243, 319)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(226, 40)
        self._label6.TabIndex = 5
        self._label6.Text = "label6"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.DimGray
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(243, 382)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(226, 40)
        self._label7.TabIndex = 6
        self._label7.Text = "label7"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(8, 112)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(171, 66)
        self._button1.TabIndex = 7
        self._button1.Text = "button1"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(196, 112)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(171, 66)
        self._button2.TabIndex = 8
        self._button2.Text = "button2"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(387, 112)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(171, 66)
        self._button3.TabIndex = 9
        self._button3.Text = "button3"
        self._button3.UseVisualStyleBackColor = True
        # 
        # comboBox1
        # 
        self._comboBox1.FormattingEnabled = True
        self._comboBox1.Items.AddRange(System.Array[System.Object](
            ["1970 VW Bug",
            "1979 Firebird",
            "1980 Subaru",
            "1975 Cutlass"]))
        self._comboBox1.Location = System.Drawing.Point(253, 33)
        self._comboBox1.Name = "comboBox1"
        self._comboBox1.Size = System.Drawing.Size(230, 21)
        self._comboBox1.TabIndex = 10
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkRed
        self.ClientSize = System.Drawing.Size(561, 454)
        self.Controls.Add(self._comboBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog 54A"
        self.ResumeLayout(False)


 

    def Button1Click(self, sender, e):
        miles = 1
        gallons = 1
        car = self._comboBox1.Text
        
        # TODO: repeat for all 4 cars
        if car == "1970 VW Bug":
            miles = 286
            gallons = 9
       
        else:
           MessageBox.Show("Invalid Car!")
           return
            
        mpg = miles / gallons
        mpg = round(mpg, 1)
        
        self._label7.Text = str(mpg)