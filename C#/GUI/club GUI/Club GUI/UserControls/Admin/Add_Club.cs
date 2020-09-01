using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Club_GUI.Classes;

namespace Club_GUI
{
    public partial class Add_Club : UserControl
    {
        public Add_Club()
        {
            InitializeComponent();
        }

        // Display Date
        private void Add_Club_Load(object sender, EventArgs e)
        {
            lbDate.Text = "(" + DateTime.UtcNow.ToString("MM-dd-yyyy") + ")";
        }

        private void Add_Click(object sender, EventArgs e)
        {
            // Check for empty fields
            if (tbClubName.Text == "" || tbCat.Text == "" || tbPresident.Text == "" || tbVice.Text == "" || rtbDes.Text == "")
            {
                MessageBox.Show("Fill all of the input fields", "Error");
            }
            else 
            {
                SqlDBConnect con = new SqlDBConnect();

                con.SqlQuery("SELECT ClubName FROM Clubs WHERE ClubName=@name");
                con.cmd.Parameters.AddWithValue("@name", tbClubName.Text);

                // Check if club already exists
                if (con.QueryEx().Rows.Count == 0)
                {
                    con.SqlQuery("INSERT INTO Clubs VALUES (@name, @cat, @regdate, @prez, @vice, @des, @lu, 'active')");
                    
                    con.cmd.Parameters.AddWithValue("@name", tbClubName.Text);
                    con.cmd.Parameters.AddWithValue("@cat", tbCat.Text);
                    con.cmd.Parameters.AddWithValue("@regdate", DateTime.UtcNow.ToString("MM-dd-yyyy"));
                    con.cmd.Parameters.AddWithValue("@prez", tbPresident.Text);
                    con.cmd.Parameters.AddWithValue("@vice", tbVice.Text);
                    con.cmd.Parameters.AddWithValue("@des", rtbDes.Text);
                    con.cmd.Parameters.AddWithValue("@lu", DateTime.UtcNow.ToString());

                    con.NonQueryEx();

                    con.con.Close();

                    MessageBox.Show("Club Added Sucessfully", "Sucess");
                }
                else
                {
                    MessageBox.Show("Club Name Already exists", "Error");
                }
            }
        }
    }
}
