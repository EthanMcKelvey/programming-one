import System.Drawing
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
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(49, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(524, 62)
        self._label1.TabIndex = 0
        self._label1.Text = "Eletric Bill!!!!"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(20, 81)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(286, 45)
        self._label2.TabIndex = 1
        self._label2.Text = "Enter Kwh used!!!"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(20, 142)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(180, 45)
        self._label3.TabIndex = 2
        self._label3.Text = "Base Rate:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(21, 198)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(180, 45)
        self._label4.TabIndex = 3
        self._label4.Text = "Sucharge"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(21, 255)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(180, 45)
        self._label5.TabIndex = 4
        self._label5.Text = "City Tax:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 517)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(179, 68)
        self._button1.TabIndex = 5
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(217, 517)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(187, 68)
        self._button2.TabIndex = 6
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(423, 517)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(186, 68)
        self._button3.TabIndex = 7
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(331, 100)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(278, 20)
        self._textBox1.TabIndex = 8
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(21, 357)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(180, 70)
        self._label6.TabIndex = 9
        self._label6.Text = "Pay this amount:"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(21, 444)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(180, 70)
        self._label7.TabIndex = 10
        self._label7.Text = "After may 20 pay:"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(244, 142)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(281, 45)
        self._label8.TabIndex = 11
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(244, 198)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(281, 45)
        self._label9.TabIndex = 12
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(244, 255)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(281, 45)
        self._label10.TabIndex = 13
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
        self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(244, 370)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(281, 45)
        self._label11.TabIndex = 14
        self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
        self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(244, 457)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(281, 45)
        self._label12.TabIndex = 15
        self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Purple
        self.ClientSize = System.Drawing.Size(638, 597)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog 93a"
        self.ResumeLayout(False)
        self.PerformLayout()


 
    def Button1Click(self, sender, e):
        # Collecting kWh and turning number into  a float
        kwh = float(self._textBox1.Text)
        # Calculating base rate
        prebaserate = float(kwh) * 0.0475
        baserate = round(prebaserate, 2)
        # Printing base rate
        self._label8.Text = "$" + str(baserate)
        # Calculating surcharge
        presurcharge = float(baserate) * .1
        surcharge = round(presurcharge, 2)
        # Printing surcharge
        self._label9.Text = "$" + str(surcharge)
        # Calculating city tax
        pretax = float(baserate) * .03
        tax = round(pretax, 2)
        # Printing city tax
        self._label10.Text = "$" + str(tax)
        # Calculating total bill
        totalbill = float(baserate) + float(surcharge) + float(tax)
        # Printing total bill
        self._label11.Text = "$" + str(totalbill)
        # Calculating late fee
        prelatefee = float(totalbill) * .04
        latefee = round(prelatefee, 2)
        latebill = float(totalbill) + float(latefee)
        # Printing late fee
        self._label12.Text = "$" + str(latebill)

    def Button2Click(self, sender, e):
        self._label12.Text = ""
        self._label11.Text = ""
        self._label10.Text = ""
        self._label9.Text = ""
        self._label8.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()