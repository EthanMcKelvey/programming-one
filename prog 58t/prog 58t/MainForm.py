import System.Drawing
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
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(311, 140)
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
        self._label1.Text = "Cost"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(14, 52)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(139, 43)
        self._label2.TabIndex = 2
        self._label2.Text = "Recived"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(14, 175)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(139, 31)
        self._label3.TabIndex = 3
        self._label3.Text = "label3"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(14, 221)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(139, 35)
        self._label4.TabIndex = 4
        self._label4.Text = "label4"
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
        self._label5.Location = System.Drawing.Point(12, 289)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(139, 35)
        self._label5.TabIndex = 7
        self._label5.Text = "label5"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(14, 339)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(139, 35)
        self._label6.TabIndex = 8
        self._label6.Text = "label6"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(14, 385)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(139, 35)
        self._label7.TabIndex = 9
        self._label7.Text = "label7"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(311, 221)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(109, 66)
        self._button2.TabIndex = 10
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(311, 308)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(109, 66)
        self._button3.TabIndex = 11
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(513, 450)
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
        price = float(self._textBox1.Text)
        recived = float(self._textBox2.Text)
        giveback = recived - price
        dollars = giveback // 1
        cents = float(giveback - dollars)
        quarters = int(((giveback - dollars) * 100) /25)
        qremaind = (cents - ((quarters / 100) *25))
        dimes = float((qremaind * 100) / 10)
        dremain = float(cents - (qremaind + ((dimes / 100) * 7)))
        nickles = int(dremain * 100 / 5)
        nremain = float(cents -(dremain + ((nickles/100)*5)))
        pennys = int(nremain * 100)
        self._label3.Text = str(dollars)
        self._label4.Text = str(quarters)
        self._label5.Text = str(dimes)
        self._label6.Text = str(nickles)
        self._label7.Text = str(pennys)

    def Button3Click(self, sender, e):
        Application.Exit()