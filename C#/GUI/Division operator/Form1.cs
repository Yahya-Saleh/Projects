using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Division_operator
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnSubmit_Click(object sender, EventArgs e)
        {
            string digits = tb5digits.Text;

            a.Text = digits[0].ToString();
            b.Text = digits[1].ToString();
            c.Text = digits[2].ToString();
            d.Text = digits[3].ToString();
            ed.Text = digits[4].ToString();
        }
    }
}
