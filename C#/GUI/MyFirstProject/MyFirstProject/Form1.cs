using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MyFirstProject
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            MessageBox.Show(textBox1.Text);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.BackColor = Color.Aqua;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            textBox1.ForeColor = Color.Red;
        }
    }
}
