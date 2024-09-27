﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.WindowFrame
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(139, 22)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(447, 174)
        self._label1.TabIndex = 0
        self._label1.Text = "Phone Numbers"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Gray
        self._button1.Location = System.Drawing.Point(44, 232)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(143, 65)
        self._button1.TabIndex = 1
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Gray
        self._button2.Location = System.Drawing.Point(297, 232)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(143, 65)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Gray
        self._button3.Location = System.Drawing.Point(561, 232)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(143, 65)
        self._button3.TabIndex = 3
        self._button3.Text = "End"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Maroon
        self.ClientSize = System.Drawing.Size(765, 333)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "phone numbers"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = " Mcdonalds-(608) 752-0100       El Ra Bowl-(608) 757-3020        Taco Bell-(608) 758-2050"

    def Button2Click(self, sender, e):
       self._label1.Text = "Sky Zone- (608) 856-5867             Dave n Busters- (608) 733-2050"
       

    def Button3Click(self, sender, e):
        Application.Exit()