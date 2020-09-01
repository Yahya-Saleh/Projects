using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace Club_GUI
{
    public partial class Login : Form
    {
        // Start a connect class
        public Classes.SqlDBConnect con = new Classes.SqlDBConnect();

        public Login()
        {
            InitializeComponent();
        }

        // A list of panels to hold the admina and student login panel
        List<Panel> PanelList = new List<Panel>();

        // When the form Loads
        private void Login_Load(object sender, EventArgs e)
        {
            // Add Panel for display
            PanelList.Add(StdLogin);
            PanelList.Add(AdminLogin);
        }

        /************************* Panel Switching **************************************************/

        private void Admin_switch_Click(object sender, EventArgs e)
        {
            PanelList[0].SendToBack();
        }

        private void Student_switch_Click(object sender, EventArgs e)
        {
            PanelList[0].BringToFront();
        }

        /************************* Student login **************************************************/

        // When the username input is clicked change the lines colors accordingly
        private void txtID_Click(object sender, EventArgs e)
        {
            panel2.BackColor = Color.Black;
            panel1.BackColor = Color.Aqua;
            txtID.Clear();
        }

        // When the Password input is clicked change the lines colors accordingly
        private void txtPass_Click(object sender, EventArgs e)
        {
            panel1.BackColor = Color.Black;
            panel2.BackColor = Color.Aqua;
            txtPass.Clear();
            txtPass.PasswordChar = '*';
        }

        private void btnStdLogin_Click(object sender, EventArgs e)
        {
            // Query the database
            con.SqlQuery("SELECT * FROM Students WHERE Username=@name AND Password=@pass");

            // Parameters
            con.cmd.Parameters.AddWithValue("@name", txtID.Text.Trim());
            con.cmd.Parameters.AddWithValue("@pass", txtPass.Text.Trim());

            // Storing the output
            DataTable table = con.QueryEx();
            
            // If the system finds exactly one match
            if (table.Rows.Count == 1)
            {
                foreach (DataRow dr in table.Rows)
                {
                    // Decide if the student is a representative or not
                    if (dr["rep"].Equals("not"))
                    {
                        Student std = new Student();
                        std.ShowDialog();
                        this.Close();
                    }
                    else
                    {
                        Rep rep = new Rep(dr["rep"].ToString());
                        rep.ShowDialog();
                        this.Close();
                    }
                }
            }
            else
            {
                MessageBox.Show("Incorrect Student ID or Password", "Input Error");
                txtID.Text = "Username";
                txtPass.Text = "Password";
            }
        }

        /************************* Admin login **************************************************/

        private void txtID2_Click(object sender, EventArgs e)
        {
            panel4.BackColor = Color.Black;
            panel5.BackColor = Color.Aqua;
            txtID2.Clear();
        }

        private void txtPass2_Click(object sender, EventArgs e)
        {
            panel5.BackColor = Color.Black;
            panel4.BackColor = Color.Aqua;
            txtPass2.Clear();
            txtPass2.PasswordChar = '*';
        }

        private void BtnAdminLogin_Click(object sender, EventArgs e)
        {
            // Query the database
            con.SqlQuery("SELECT * FROM Admin WHERE Username=@name AND Password=@pass");

            // Parameters
            con.cmd.Parameters.AddWithValue("@name", txtID2.Text.Trim());
            con.cmd.Parameters.AddWithValue("@pass", txtPass2.Text.Trim());

            // Storing the output
            DataTable table = con.QueryEx();

            // If the system finds exactly one match
            if (table.Rows.Count == 1)
            {
                Admin adm = new Admin();
                adm.Closed += (s, args) => this.Close();
                adm.ShowDialog();
            }
            else
            {
                MessageBox.Show("Incorrect Student ID or Password", "Input Error");
                txtID.Text = "Username";
                txtPass.Text = "Password";
            }
        }
    }
}
